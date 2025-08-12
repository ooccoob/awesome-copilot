/*
  自动生成 zh-cn/list.md：统计源/目标目录下 Markdown 文件的行数与修改时间，并附中文用途描述。
*/
const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve("d:/mycode/awesome-copilot");
const OUT_FILE = path.join(REPO_ROOT, "localization", "zh-cn", "list.md");

const CATEGORIES = [
  {
    name: "chatmodes",
    src: path.join(REPO_ROOT, "chatmodes"),
    tgt: path.join(REPO_ROOT, "localization", "zh-cn", "chatmodes"),
    suffix: ".chatmode.md",
  },
  {
    name: "instructions",
    src: path.join(REPO_ROOT, "instructions"),
    tgt: path.join(REPO_ROOT, "localization", "zh-cn", "instructions"),
    suffix: ".instructions.md",
  },
  {
    name: "localization",
    src: path.join(REPO_ROOT, "localization"),
    tgt: path.join(REPO_ROOT, "localization", "zh-cn", "localization"),
    suffix: ".md",
  },
];

function walkMarkdownFiles(dir) {
  const results = [];
  if (!fs.existsSync(dir)) return results;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) {
      results.push(...walkMarkdownFiles(full));
    } else if (e.isFile() && e.name.toLowerCase().endsWith(".md")) {
      results.push(full);
    }
  }
  return results;
}

function countLines(filePath) {
  try {
    // Stream count to avoid loading huge files fully into memory
    const data = fs.readFileSync(filePath, "utf8");
    if (data.length === 0) return 0;
    let lines = 0;
    for (let i = 0; i < data.length; i++) if (data[i] === "\n") lines++;
    // If file doesn't end with newline, add one line
    if (!data.endsWith("\n")) lines++;
    return lines;
  } catch {
    return null;
  }
}

function fmtTime(ts) {
  if (!ts) return "";
  try {
    const d = new Date(ts);
    const pad = (n) => String(n).padStart(2, "0");
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(
      d.getDate()
    )} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
  } catch {
    return "";
  }
}

// 从 README.md 提取部分说明（仅对 instructions 有用）
function parseReadmeDescriptions() {
  const map = new Map();
  const readmePath = path.join(REPO_ROOT, "README.md");
  if (!fs.existsSync(readmePath)) return map;
  const text = fs.readFileSync(readmePath, "utf8");
  // 匹配表格中形如 | [Title](instructions/xxx.md) | Description | 的行
  const regex =
    /\|\s*\[[^\]]+\]\((instructions\/[^)]+)\)\s*\|\s*([^|]+?)\s*\|/gi;
  let m;
  while ((m = regex.exec(text)) !== null) {
    const rel = m[1].trim();
    const desc = m[2].trim();
    // 保存英文描述，后续转中文（粗略映射）
    map.set(rel.replace(/\\/g, "/"), desc);
  }
  return map;
}

function toChineseDescription(category, fileName, relPath, readmeMap) {
  // 优先使用 README 中的描述
  if (category === "instructions") {
    const key = `instructions/${relPath.replace(/\\/g, "/")}`;
    if (readmeMap.has(key)) {
      return enToZh(readmeMap.get(key)) || readmeMap.get(key);
    }
  }
  // 基于文件名的启发式中文描述
  const base = fileName
    .replace(/\.md$/i, "")
    .replace(/[-_.]+/g, " ")
    .trim();
  const title = humanizeTitle(base);
  switch (category) {
    case "chatmodes":
      return `聊天模式：${title}`;
    case "instructions":
      return `指令与最佳实践：${title}`;
    case "localization":
      return `本地化源文档：${title}`;
    default:
      return title;
  }
}

function humanizeTitle(s) {
  // 常见关键词的中文化
  const tokens = s.split(/\s+/).map((t) => t.toLowerCase());
  const mapped = tokens.map((t) => {
    switch (t) {
      case "azure":
        return "Azure";
      case "functions":
        return "函数";
      case "typescript":
        return "TypeScript";
      case "bicep":
        return "Bicep";
      case "terraform":
        return "Terraform";
      case "playwright":
        return "Playwright";
      case "postgresql":
        return "PostgreSQL";
      case "sql":
        return "SQL";
      case "mssql":
        return "SQL Server";
      case "csharp":
      case "c#":
        return "C#";
      case "dotnet":
      case ".net":
        return ".NET";
      case "blazor":
        return "Blazor";
      case "nextjs":
      case "next":
        return "Next.js";
      case "nestjs":
        return "NestJS";
      case "reactjs":
      case "react":
        return "React";
      case "kubernetes":
        return "Kubernetes";
      case "docker":
        return "Docker";
      case "linux":
        return "Linux";
      case "windows":
        return "Windows";
      case "python":
        return "Python";
      case "ruby":
        return "Ruby";
      case "go":
        return "Go";
      case "rust":
        return "Rust";
      case "security":
        return "安全";
      case "a11y":
      case "accessibility":
        return "无障碍";
      case "debug":
        return "调试";
      case "planner":
      case "plan":
        return "规划";
      case "prd":
        return "PRD";
      case "janitor":
        return "代码清理";
      case "prompt":
        return "提示工程";
      default:
        return t.replace(/^(\w)/, (m) => m.toUpperCase());
    }
  });
  return mapped.join(" ");
}

// 粗略英文到中文的描述映射（仅覆盖常见词）
function enToZh(s) {
  if (!s) return s;
  return s
    .replace(
      /Guidance for creating more accessible code/gi,
      "为创建更易用的代码提供指南"
    )
    .replace(
      /Comprehensive best practices for AI prompt engineering.*responsible AI usage.*/gi,
      "AI 提示工程与安全的综合最佳实践，涵盖偏见缓解与负责任的 AI 使用"
    )
    .replace(
      /Angular-specific coding standards and best practices/gi,
      "Angular 专用的编码规范与最佳实践"
    )
    .replace(
      /Guidelines for building REST APIs with ASP.NET/gi,
      "使用 ASP.NET 构建 REST API 的指南"
    )
    .replace(
      /TypeScript patterns for Azure Functions/gi,
      "Azure Functions 的 TypeScript 编码范式"
    )
    .replace(
      /Azure Verified Modules \(AVM\) and Terraform/gi,
      "Azure Verified Modules (AVM) 与 Terraform 实践"
    )
    .replace(
      /Infrastructure as Code with Bicep/gi,
      "使用 Bicep 的基础设施即代码（IaC）实践"
    )
    .replace(
      /Blazor component and application patterns/gi,
      "Blazor 组件与应用模式"
    );
}

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

function generate() {
  const readmeDescMap = parseReadmeDescriptions();
  const sections = [];
  const summaries = [];

  for (const cat of CATEGORIES) {
    const files = walkMarkdownFiles(cat.src);
    const srcCount = files.length;
    const tgtFiles = walkMarkdownFiles(cat.tgt);
    const tgtCount = tgtFiles.length;
    summaries.push({ category: cat.name, srcCount, tgtCount });

    const rows = [];
    for (const full of files) {
      const rel = path.relative(cat.src, full).replace(/\\/g, "/");
      const fileName = path.basename(full);
      const tgt = path.join(cat.tgt, rel);
      const srcStat = fs.existsSync(full) ? fs.statSync(full) : null;
      const tgtStat = fs.existsSync(tgt) ? fs.statSync(tgt) : null;
      const srcLines = fs.existsSync(full) ? countLines(full) : null;
      const tgtLines = fs.existsSync(tgt) ? countLines(tgt) : null;
      const desc = toChineseDescription(cat.name, fileName, rel, readmeDescMap);

      rows.push({
        rel,
        desc,
        srcLines: srcLines ?? "",
        tgtLines: tgtLines ?? "",
        srcMtime: srcStat ? fmtTime(srcStat.mtime) : "",
        tgtMtime: tgtStat ? fmtTime(tgtStat.mtime) : "",
      });
    }

    // 排序：相对路径
    rows.sort((a, b) => a.rel.localeCompare(b.rel));

    // 生成表格 Markdown
    const md = [];
    md.push(`### ${cat.name}`);
    md.push("");
    md.push(`源文件总数：${srcCount} | 目标文件总数：${tgtCount}`);
    md.push("");
    md.push("| 文件 | 描述 | 源行数 | 目标行数 | 源修改时间 | 目标修改时间 |");
    md.push("| --- | --- | ---: | ---: | --- | --- |");
    for (const r of rows) {
      md.push(
        `| ${r.rel} | ${r.desc} | ${r.srcLines} | ${r.tgtLines} | ${r.srcMtime} | ${r.tgtMtime} |`
      );
    }
    md.push("");
    sections.push(md.join("\n"));
  }

  const now = fmtTime(Date.now());
  const header = [
    "## 清单统计（自动生成）",
    "",
    `生成时间：${now}`,
    "",
    "- 本文档统计以下源/目标目录中的 Markdown 文件（递归）：",
    "  - 源：chatmodes、instructions、localization",
    "  - 目标：localization/zh-cn/{chatmodes,instructions,localization}",
    "",
  ].join("\n");

  const disclaimer = [
    "---",
    "",
    "**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动生成，可能包含错误。如发现不当或错误的描述，请在[问题反馈](../../issues)中指出。",
  ].join("\n");

  const content = [header, ...sections, disclaimer, ""].join("\n");

  ensureDir(path.dirname(OUT_FILE));
  fs.writeFileSync(OUT_FILE, content, "utf8");
}

if (require.main === module) {
  generate();
  console.log(`Written: ${OUT_FILE}`);
}

module.exports = { generate };
