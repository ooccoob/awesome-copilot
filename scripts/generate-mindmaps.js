const fs = require("fs");
const path = require("path");

const workspaceRoot = path.resolve(__dirname, "..");
const targets = ["prompts", "chatmodes", "instructions"];
const promptPath = path.join(
  workspaceRoot,
  "my-custom",
  "prompts",
  "my-copilot-mindmap.prompt.md"
);
const outBase = path.join(workspaceRoot, "my-custom", "Mind Map");
const manifestPath = path.join(outBase, "manifest.json");
const processingLog = path.join(outBase, "processing.log");

function readPromptTemplate() {
  if (!fs.existsSync(promptPath)) {
    console.error("转换规则文件不存在:", promptPath);
    process.exit(1);
  }
  return fs.readFileSync(promptPath, "utf8");
}

function collectMdFiles() {
  const results = [];
  targets.forEach((dir) => {
    const dirPath = path.join(workspaceRoot, dir);
    if (!fs.existsSync(dirPath)) return;
    const files = fs.readdirSync(dirPath);
    files.forEach((f) => {
      const p = path.join(dirPath, f);
      if (fs.statSync(p).isFile() && p.endsWith(".md")) results.push(p);
    });
  });
  return results;
}

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

function loadManifest() {
  if (!fs.existsSync(manifestPath)) return null;
  try {
    return JSON.parse(fs.readFileSync(manifestPath, "utf8"));
  } catch (e) {
    console.error("无法解析 manifest（非法 JSON）:", manifestPath);
    return null;
  }
}

function saveManifest(manifest) {
  ensureDir(outBase);
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf8");
}

function appendLog(line) {
  ensureDir(outBase);
  const t = new Date().toISOString();
  fs.appendFileSync(processingLog, `[${t}] ${line}\n`, "utf8");
}

function parsePromptTemplateForQuestionHints(promptTemplate) {
  // 兼容旧接口：保留简单提示提取
  const lines = promptTemplate.split(/\r?\n/);
  const hints = [];
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i].toLowerCase();
    if (
      l.includes("示例问题") ||
      l.includes("example questions") ||
      l.includes("问题示例")
    ) {
      hints.push(lines.slice(i, i + 6).join(" "));
    }
  }
  if (!hints.length)
    hints.push("请基于本文内容生成针对实现/设计/运维/风险/测试的具体问题。");
  return hints[0];
}

function parsePromptTemplateForContract(promptTemplate) {
  // 解析模板以提取：示例问题类别（最多5类，每类含示例），以及双语标题提示
  const lines = promptTemplate.split(/\r?\n/);
  // 找到“实际使用说明示例问题”或类似节的起始行
  let start = -1;
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i];
    if (/实际使用说明示例问题|示例问题|实际使用说明/i.test(l)) {
      start = i;
      break;
    }
  }

  const questionCategories = [];
  if (start >= 0) {
    // 采集该节直到下一个大标题（##）或空行连续两行
    const section = [];
    for (let i = start + 1; i < lines.length; i++) {
      const l = lines[i];
      if (/^#{1,6}\s/.test(l)) break;
      section.push(l);
    }

    // 在 section 中寻找以数字或短横开头的分类或以序号开始的行
    section.forEach((ln) => {
      const trimmed = ln.trim();
      if (!trimmed) return;
      // 形式：1. 成本/性能: 示例..., 或 - 成本/性能: 示例...
      let m = trimmed.match(
        /^\s*(?:[-*]|\d+[.)])\s*([^:：\n]+)[:：-]?\s*(.*)$/
      );
      if (m) {
        const name = m[1].trim();
        const rest = (m[2] || "").trim();
        const examples = rest
          ? rest
              .split(/[；;，,、]/)
              .map((s) => s.trim())
              .filter(Boolean)
          : [];
        questionCategories.push({ name, examples });
        return;
      }
      // 有时分类写成：成本/性能（Cost/Performance）
      m = trimmed.match(/^\s*([^:‑—\n]+?)\s*[:‑—]?\s*$/);
      if (m && trimmed.length < 60) {
        const name = m[1].trim();
        questionCategories.push({ name, examples: [] });
      }
    });
  }

  // 保底五类：如果解析不到，使用默认分类
  const defaults = [
    "成本/性能",
    "错误处理/弹性",
    "定义/实现细节",
    "集成/互联模式",
    "架构决策/扩展性",
  ];
  for (let i = 0; i < defaults.length; i++) {
    if (!questionCategories[i])
      questionCategories[i] = { name: defaults[i], examples: [] };
  }

  // 解析双语标题示例：寻找包含 '/' 的行，且两侧看起来像中文/英文
  const bilingual = [];
  lines.forEach((ln) => {
    const m = ln.match(/^-?\s*(.+?)\s*\/\s*(.+)$/);
    if (m) {
      const left = m[1].trim();
      const right = m[2].trim();
      // 简单过滤：左右两侧长度合理
      if (left.length > 0 && right.length > 0)
        bilingual.push({ cn: left, en: right });
    }
  });

  // fallback hint
  const generalHint = parsePromptTemplateForQuestionHints(promptTemplate);

  return {
    questionCategories: questionCategories.slice(0, 5),
    bilingual,
    generalHint,
  };
}

function generateMindmapContent(srcPath, srcContent, promptTemplate) {
  // 提取基本信息
  const lines = srcContent.split(/\r?\n/);
  const title = lines.find((l) => /^#\s/.test(l)) || path.basename(srcPath);
  const firstPara = lines.slice(0, 20).find((l) => l.trim());
  const headings = lines.filter((l) => /^##?\s/.test(l)).slice(0, 20);

  // 从模板中获取示例问题提示
  const questionHint = parsePromptTemplateForQuestionHints(promptTemplate);

  // 生成 5 个示例问题：基于标题、主要 headings 与模板提示
  const questionCandidates = [];
  const core = title.replace(/^#+\s*/, "");
  const topHeadings = headings.map((h) => h.replace(/^#+\s*/, "")).slice(0, 5);
  // 组合生成问题（简单规则驱动）
  questionCandidates.push(`如何在项目中实现 "${core}" 的关键部分？`);
  if (topHeadings[0])
    questionCandidates.push(
      `关于 ${topHeadings[0]}，有哪些常见的实现陷阱和规避策略？`
    );
  if (topHeadings[1])
    questionCandidates.push(
      `为确保 ${topHeadings[1]} 的健壮性，应考虑哪些测试与监控措施？`
    );
  questionCandidates.push(
    `在部署或运维层面，需要注意哪些与 ${core} 相关的风险？`
  );
  questionCandidates.push(
    `如果要扩展 ${core} 的能力，下一步可以优先实现哪些功能？`
  );

  // 如果数量不足，用模板提示生成占位问题
  while (questionCandidates.length < 5) {
    questionCandidates.push(`${questionHint}（请根据上下文细化）`);
  }

  let md = `## 摘要\n\n`;
  md += `**来源文件**: ${path.relative(workspaceRoot, srcPath)}\n\n`;
  md += `**标题**: ${core}\n\n`;
  md += `**简介**: ${firstPara || ""}\n\n`;

  md += `## 结构化要点\n\n`;
  if (topHeadings.length) {
    topHeadings.forEach((h) => {
      md += `- ${h}\n`;
    });
  } else {
    md += `- (未检测到明确小标题，建议手动审阅并补充要点)\n`;
  }

  md += `\n## 思维导图格式\n\n`;
  md += `- ${core}\n`;
  topHeadings.forEach((h) => (md += `  - ${h}\n`));

  md += `\n## 典型示例问题（自动生成，示例5条）\n\n`;
  questionCandidates.slice(0, 5).forEach((q) => {
    md += `- ${q}\n`;
  });

  md += `\n## 生成说明\n\n`;
  md += `本文件由脚本自动生成，使用转换规则： ${path.relative(
    workspaceRoot,
    promptPath
  )}\n`;

  return md;
}

function processAll(sampleCount) {
  const promptTemplate = readPromptTemplate();
  const mdFiles = collectMdFiles();
  console.log("发现 md 文件数量:", mdFiles.length);

  const summary = { total: mdFiles.length, done: 0, failed: [] };

  // If manifest exists and user opted to use it, process manifest entries in order
  const manifest = loadManifest();
  let toProcess = [];
  if (manifest && useManifest) {
    console.log("使用 manifest 驱动处理: ", manifestPath);
    // select entries with status pending
    const pending = manifest.filter((e) => e.status === "pending");
    toProcess = pending.map((e) => path.join(workspaceRoot, e.srcPath));
    if (typeof sampleCount === "number" && sampleCount > 0)
      toProcess = toProcess.slice(0, sampleCount);
  } else {
    toProcess =
      typeof sampleCount === "number" && sampleCount > 0
        ? mdFiles.slice(0, sampleCount)
        : mdFiles;
  }

  toProcess.forEach((src) => {
    // If manifest-driven, find corresponding manifest entry
    const rel = path.relative(workspaceRoot, src);
    let manifestEntry = null;
    if (manifest) manifestEntry = manifest.find((m) => m.srcPath === rel);

    try {
      if (manifestEntry) {
        manifestEntry.status = "in-progress";
        manifestEntry.startTime = new Date().toISOString();
        saveManifest(manifest);
        appendLog(`开始处理 ${rel}`);
      }

      const content = fs.readFileSync(src, "utf8");
      const relParent = path.basename(path.dirname(src));
      const outDir = path.join(outBase, relParent);
      ensureDir(outDir);
      const outName = path.basename(src).replace(/\.md$/, ".mindmap.md");
      const outPath = path.join(outDir, outName);
      const mindmap = generateMindmapContent(src, content, promptTemplate);
      fs.writeFileSync(outPath, mindmap, "utf8");
      summary.done += 1;
      console.log("生成:", outPath);
      appendLog(`生成: ${outPath}`);

      if (manifestEntry) {
        manifestEntry.status = "done";
        manifestEntry.endTime = new Date().toISOString();
        manifestEntry.error = null;
        saveManifest(manifest);
        appendLog(`完成 ${rel}`);
      }
    } catch (e) {
      console.error("处理失败:", src, e.message);
      summary.failed.push({ file: src, error: e.message });
      appendLog(`失败 ${rel}: ${e && e.message}`);
      if (manifestEntry) {
        manifestEntry.status = "failed";
        manifestEntry.endTime = new Date().toISOString();
        manifestEntry.error = e && e.message;
        saveManifest(manifest);
      }
    }
  });

  console.log("完成：", summary.done, "/", toProcess.length);
  if (summary.failed.length) {
    console.log("失败列表：", summary.failed);
  }
}

// CLI: 可选 --sample N 来处理前 N 个文件
const arg = process.argv.find((a) => a.startsWith("--sample"));
let sampleCount = 0;
if (arg) {
  const parts = arg.split("=");
  sampleCount = parts[1] ? parseInt(parts[1], 10) : 0;
}

// CLI: --use-manifest 切换为由 manifest 驱动处理
const useManifest = process.argv.includes("--use-manifest");

processAll(sampleCount);
