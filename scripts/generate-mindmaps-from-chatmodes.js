#!/usr/bin/env node
// generate-mindmaps-from-chatmodes.js
// Scans chatmodes/*.md, uses my-copilot-mindmap.prompt.md as template, calls OpenAI chat API,
// writes output files to my-custom/Mind Map/chatmodes/*.mindmap.md
// Maintains manifest.json and processing.log

const fs = require("fs").promises;
const path = require("path");
const crypto = require("crypto");

const ROOT = path.resolve(__dirname, ".."); // d:/mycode/awesome-copilot
const CHATMODES_DIR = path.join(ROOT, "chatmodes");
const TEMPLATE_PATH = path.join(
  ROOT,
  "my-custom",
  "prompts",
  "my-copilot-mindmap.prompt.md"
);
const OUT_BASE = path.join(ROOT, "my-custom", "Mind Map", "chatmodes");
const MANIFEST_PATH = path.join(ROOT, "my-custom", "Mind Map", "manifest.json");
const LOG_PATH = path.join(ROOT, "my-custom", "Mind Map", "processing.log");

async function ensureDir(dir) {
  await fs.mkdir(dir, { recursive: true });
}

function sha256(buf) {
  return crypto.createHash("sha256").update(buf).digest("hex");
}

function parseArgs() {
  const argv = process.argv.slice(2);
  const opts = {
    sample: null,
    dryRun: false,
    model: process.env.OPENAI_MODEL || "gpt-4o",
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--sample=")) opts.sample = parseInt(a.split("=")[1], 10);
    if (a === "--dry-run") opts.dryRun = true;
    if (a.startsWith("--model=")) opts.model = a.split("=")[1];
  }
  return opts;
}

async function listMdFiles(dir) {
  const names = await fs.readdir(dir);
  return names.filter((n) => n.endsWith(".md")).map((n) => path.join(dir, n));
}

async function readTemplate() {
  try {
    return await fs.readFile(TEMPLATE_PATH, "utf8");
  } catch (e) {
    throw new Error(`Template not found at ${TEMPLATE_PATH}: ${e.message}`);
  }
}

async function loadManifest() {
  try {
    const raw = await fs.readFile(MANIFEST_PATH, "utf8");
    return JSON.parse(raw);
  } catch (e) {
    return [];
  }
}

async function saveManifest(manifest) {
  await ensureDir(path.dirname(MANIFEST_PATH));
  await fs.writeFile(MANIFEST_PATH, JSON.stringify(manifest, null, 2), "utf8");
}

async function appendLog(entry) {
  await ensureDir(path.dirname(LOG_PATH));
  const line = JSON.stringify(entry) + "\n";
  await fs.appendFile(LOG_PATH, line, "utf8");
}

async function callOpenAI(systemPrompt, userPrompt, model) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) throw new Error("OPENAI_API_KEY not set in environment");

  const payload = {
    model,
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userPrompt },
    ],
    temperature: 0.2,
    max_tokens: 3000,
  };

  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`OpenAI API error ${res.status}: ${text}`);
  }
  const data = await res.json();
  const content = data.choices?.[0]?.message?.content;
  if (!content) throw new Error("No content in assistant response");
  return content.trim();
}

function buildSystemPrompt() {
  return (
    `You are a structured assistant that returns a single-line JSON object describing a write_file action. Follow these rules:\n` +
    `1) Only output a single-line JSON object; no extra text.\n` +
    `2) The JSON must be one of: {"action":"write_file","path":"...","encoding":"utf-8","content":"<base64>","summary":"..."} or {"action":"write_file","path":"...","content_plain":"..."} or {"action":"error","message":"..."}.\n` +
    `3) content should be base64 when possible to avoid escaping issues.\n` +
    `4) Use the user-provided document content only; do not invent facts beyond it.\n`
  );
}

function buildUserPrompt(template, mdContent, outputPath) {
  // Inject MD content and a concrete question into the template
  const question = `请基于下面的文档内容，生成一个结构化的 mindmap 风格的 Markdown 文本，必须包含：\n- 摘要（50-120 字）\n- 结构化要点（有序或无序列表）\n- 思维导图（可用 markdown 列表或 mermaid）\n- 实际使用说明（至少 5 条示例问题，标注哪些是“合成示例”）\n\n请将生成结果写入文件: ${outputPath}，并以单行 JSON 响应，符合 system 格式要求。`;

  // If template contains placeholder {{MD_CONTENT}}, replace it; otherwise prepend the MD
  let prompt = template.includes("{{MD_CONTENT}}")
    ? template.replace("{{MD_CONTENT}}", mdContent)
    : `${mdContent}\n\n${question}`;
  // Append explicit question and output instruction
  prompt += `\n\n${question}`;
  return prompt;
}

async function processFile(filePath, template, opts, manifest) {
  const rel = path.relative(ROOT, filePath);
  const base = path.basename(filePath, ".md");
  const outPath = path.join(OUT_BASE, `${base}.mindmap.md`);
  await ensureDir(path.dirname(outPath));

  const id = manifest.length + 1;
  const entry = {
    id,
    srcPath: rel,
    outPath: path.relative(ROOT, outPath),
    status: "pending",
    startTime: null,
    endTime: null,
    error: null,
  };
  manifest.push(entry);
  await saveManifest(manifest);

  entry.status = "in-progress";
  entry.startTime = new Date().toISOString();
  await saveManifest(manifest);

  try {
    const mdContent = await fs.readFile(filePath, "utf8");
    const userPrompt = buildUserPrompt(
      template,
      mdContent,
      path.relative(ROOT, outPath)
    );

    if (opts.dryRun) {
      entry.status = "done";
      entry.endTime = new Date().toISOString();
      await appendLog({
        ts: new Date().toISOString(),
        id: entry.id,
        src: entry.srcPath,
        out: entry.outPath,
        status: entry.status,
        note: "dry-run",
      });
      await saveManifest(manifest);
      console.log(`[dry-run] processed ${entry.srcPath} -> ${entry.outPath}`);
      return;
    }

    const systemPrompt = buildSystemPrompt();
    const assistantText = await callOpenAI(
      systemPrompt,
      userPrompt,
      opts.model
    );

    // assistantText should be a single-line JSON
    let meta;
    try {
      meta = JSON.parse(assistantText);
    } catch (e) {
      throw new Error(
        "Assistant did not return valid JSON: " + assistantText.slice(0, 500)
      );
    }

    if (meta.action === "error") {
      throw new Error("Assistant error: " + meta.message);
    }

    if (meta.action === "write_file") {
      if (meta.content) {
        const buf = Buffer.from(meta.content, "base64");
        await fs.writeFile(outPath, buf);
      } else if (meta.content_plain) {
        await fs.writeFile(outPath, meta.content_plain, "utf8");
      } else {
        throw new Error("No content provided by assistant");
      }

      const written = await fs.readFile(outPath);
      entry.status = "done";
      entry.endTime = new Date().toISOString();
      entry.bytes = written.length;
      entry.sha256 = sha256(written);
      await appendLog({
        ts: new Date().toISOString(),
        id: entry.id,
        src: entry.srcPath,
        out: entry.outPath,
        status: entry.status,
        bytes: entry.bytes,
        sha256: entry.sha256,
      });
      await saveManifest(manifest);
      console.log(`WROTE ${entry.outPath}`);
    } else {
      throw new Error(
        "Unsupported action from assistant: " + JSON.stringify(meta)
      );
    }
  } catch (err) {
    entry.status = "failed";
    entry.endTime = new Date().toISOString();
    entry.error = String(err.message || err);
    await appendLog({
      ts: new Date().toISOString(),
      id: entry.id,
      src: entry.srcPath,
      out: entry.outPath,
      status: entry.status,
      error: entry.error,
    });
    await saveManifest(manifest);
    console.error(`FAILED ${entry.srcPath}: ${entry.error}`);
  }
}

async function main() {
  const opts = parseArgs();
  console.log("Options:", opts);
  await ensureDir(OUT_BASE);
  const files = await listMdFiles(CHATMODES_DIR);
  console.log(`Found ${files.length} .md files in ${CHATMODES_DIR}`);
  const template = await readTemplate();
  const manifest = await loadManifest();

  const targets = opts.sample ? files.slice(0, opts.sample) : files;
  console.log(`Processing ${targets.length} files...`);

  for (const f of targets) {
    // skip files that already appear done in manifest
    const rel = path.relative(ROOT, f);
    const exists = manifest.find(
      (m) => m.srcPath === rel && m.status === "done"
    );
    if (exists) {
      console.log(`Skipping already-done: ${rel}`);
      continue;
    }
    await processFile(f, template, opts, manifest);
  }

  console.log("Finished run. Manifest at", MANIFEST_PATH, "log at", LOG_PATH);
}

main().catch((err) => {
  console.error("Fatal:", err);
  process.exitCode = 1;
});
