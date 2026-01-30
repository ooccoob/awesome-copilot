const { chromium } = require("playwright");

async function exploreHosUIWebsite() {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  const baseUrl = "http://127.0.0.1:8080/hos/index.html";
  const visitedPages = new Map();
  const allLinks = [];

  try {
    // 访问起始页面
    console.log("开始探索 HosUI 文档网站...");
    await page.goto(`${baseUrl}#/zh-CN/component/installation`, {
      waitUntil: "domcontentloaded",
    });

    // 收集所有内部链接
    const links = await page.evaluate(() => {
      const internalLinks = Array.from(
        document.querySelectorAll('a[href^="#"]')
      ).map((link) => ({
        href: link.href,
        text: link.textContent.trim(),
        hash: link.getAttribute("href"),
      }));

      // 去重并过滤有效链接
      return internalLinks.filter(
        (link, index, self) =>
          link.hash &&
          link.hash !== "#" &&
          self.findIndex((l) => l.hash === link.hash) === index
      );
    });

    console.log(`发现 ${links.length} 个内部链接`);
    allLinks.push(...links);

    // 访问每个链接并收集页面标题
    for (const link of links) {
      try {
        const fullUrl = `${baseUrl}${link.hash}`;
        console.log(`访问: ${link.text} (${link.hash})`);

        await page.goto(fullUrl, { waitUntil: "domcontentloaded" });
        await page.waitForTimeout(1000);

        const pageTitle = await page.title();
        const currentUrl = page.url();

        visitedPages.set(link.hash, {
          title: pageTitle,
          linkText: link.text,
          url: currentUrl,
          hash: link.hash,
        });

        console.log(`  页面标题: ${pageTitle}`);
      } catch (error) {
        console.error(`访问 ${link.hash} 时出错:`, error.message);
        visitedPages.set(link.hash, {
          title: "ERROR",
          linkText: link.text,
          url: "ERROR",
          hash: link.hash,
          error: error.message,
        });
      }
    }
  } catch (error) {
    console.error("探索过程中出错:", error);
  } finally {
    await browser.close();
  }

  return { visitedPages, allLinks };
}

// 运行脚本并生成报告
async function generateReport() {
  const { visitedPages, allLinks } = await exploreHosUIWebsite();

  console.log("\n=== 网站探索报告 ===");
  console.log(`总共发现链接: ${allLinks.length}`);
  console.log(
    `成功访问页面: ${
      Array.from(visitedPages.values()).filter((p) => p.title !== "ERROR")
        .length
    }`
  );
  console.log(
    `访问失败页面: ${
      Array.from(visitedPages.values()).filter((p) => p.title === "ERROR")
        .length
    }`
  );

  console.log("\n=== 所有页面标题列表 ===");
  for (const [hash, pageInfo] of visitedPages) {
    if (pageInfo.title !== "ERROR") {
      console.log(`${pageInfo.linkText}: "${pageInfo.title}"`);
    } else {
      console.log(`${pageInfo.linkText}: 访问失败 - ${pageInfo.error}`);
    }
  }

  console.log("\n=== 页面分类统计 ===");
  const categories = {
    guide: [],
    components: [],
    development: [],
  };

  for (const [hash, pageInfo] of visitedPages) {
    if (hash.includes("/guide")) {
      categories.guide.push(pageInfo);
    } else if (hash.includes("/component")) {
      categories.components.push(pageInfo);
    } else {
      categories.development.push(pageInfo);
    }
  }

  console.log(`指南页面: ${categories.guide.length}`);
  console.log(`组件页面: ${categories.components.length}`);
  console.log(`其他页面: ${categories.development.length}`);

  return { visitedPages, allLinks, categories };
}

// 运行报告生成
generateReport().catch(console.error);

module.exports = { exploreHosUIWebsite, generateReport };
