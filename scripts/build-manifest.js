const fs = require("fs");
const path = require("path");

const workspaceRoot = path.resolve(__dirname, "..");
const targets = ["prompts", "chatmodes", "instructions"];
const outBase = path.join(workspaceRoot, "my-custom", "Mind Map");
const manifestPath = path.join(outBase, "manifest.json");

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
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

function loadManifest() {
  if (!fs.existsSync(manifestPath)) return null;
  try {
    return JSON.parse(fs.readFileSync(manifestPath, "utf8"));
  } catch (e) {
    console.error("无法解析 manifest（非法 JSON）:", manifestPath, e?.message);
    return null;
  }
}

function saveManifest(manifest) {
  ensureDir(outBase);
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf8");
}

function buildManifest(force) {
  ensureDir(outBase);
  const discovered = collectMdFiles();
  console.log("发现 md 文件数量:", discovered.length);

  let manifest = loadManifest();
  if (!manifest || force) {
    manifest = [];
  }

  const existingBySrc = {};
  (manifest || []).forEach((m) => {
    if (m?.srcPath) existingBySrc[m.srcPath] = m;
  });

  let added = 0;
  discovered.forEach((src) => {
    const rel = path.relative(workspaceRoot, src);
    if (existingBySrc[rel]) return; // keep existing
    const relParent = path.basename(path.dirname(src));
    const outName = path.basename(src).replace(/\.md$/, ".mindmap.md");
    const outRel = path.join(
      path.relative(workspaceRoot, outBase),
      relParent,
      outName
    );
    const entry = {
      id: manifest.length + added + 1,
      srcPath: rel,
      outPath: outRel,
      status: "pending",
      startTime: null,
      endTime: null,
      error: null,
    };
    manifest.push(entry);
    existingBySrc[rel] = entry;
    added += 1;
  });

  saveManifest(manifest);
  console.log(
    `manifest 已写入: ${manifestPath} （新增 ${added} 条，总计 ${manifest.length} 条）`
  );
}

// CLI
const arg = process.argv.find((a) => a.startsWith("--force"));
const force = !!arg;
buildManifest(force);
