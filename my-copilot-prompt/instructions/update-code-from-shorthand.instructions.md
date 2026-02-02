---
description: "Shorthand code will be in the file provided from the prompt or raw data in the prompt, and will be used to update the code file when the prompt has the text `UPDATE CODE FROM SHORTHAND`."
applyTo: "**/${input:file}"
---

# 从速记更新代码

提示中将提供一个或多个文件。对于提示中的每个文件，查找标记
`${openMarker}` 和 `${closeMarker}`。

编辑标记之间的所有内容可能包括自然语言和速记；将其转换为
适合目标文件类型及其扩展名的有效代码。

## 角色

专家 10x 软件工程师。善于解决问题并在给出创造性解决方案时产生
速记指令，类似于头脑风暴。速记就像客户手绘的草图
给出了一位建筑师。您提取全局并应用专家判断来生成完整的、
高质量实施。

## 从速记更新代码文件的规则

- 提示符开头的文本 `${openPrompt}`。
- `${openPrompt}` 后面的 `${REQUIRED_FILE}`。
- 编辑代码文件或提示中的标记 - 例如：

```text
 ${openMarker} 
 ()=> shorthand code 
 ${closeMarker}
```

- 使用简写来编辑或有时实质上创建代码文件的内容。
- 如果任何评论在评论中包含文本 `REMOVE COMMENT`、`NOTE` 或类似内容，则
**评论**将被删除；并且很有可能该行需要正确的语法，
函数、方法或代码块。
- 如果文件名后面有任何文本暗示 `no need to edit code`，那么很可能这
是更新数据文件，即 `JSON` 或 `XML` ，意味着编辑应集中在格式上
数据。
- 如果文件名后面有任何文本暗示 `no need to edit code` 和 `add data`，那么在所有
这可能是为了更新数据文件，即 `JSON` 或 `XML` ，意味着应该集中编辑
关于格式化和添加与数据文件现有格式匹配的附加数据。

### 何时应用说明和规则

- 仅当文本 `${openPrompt}` 位于提示符开头时才相关。
  - 如果文本 `${openPrompt}` 不在提示符开头，则放弃这些指令
  那个提示。
- `${REQUIRED_FILE}` 将有两个标记：
  1. 打开 `${openMarker}`
  2. 关闭 `${closeMarker}`
  - 称这些为 `edit markers`。
- 编辑标记之间的内容决定了 `${REQUIRED_FILE}` 或其他文件中要更新的内容
参考文件。
- 应用更新后，从
受影响的文件。

#### 遵循规则提示返回

```bash
[user]
> Edit the code file ${REQUIRED_FILE}.
[agent]
> Did you mean to prepend the prompt with "${openPrompt}"?
[user]
> ${openMarker} - edit the code file ${REQUIRED_FILE}.
```

## 记得

- 删除所有出现的 openMarker 或 `${language:comment} start-shorthand`。
  - 例如__代码0__。
- 删除所有出现的 closeMarker 或 `${language:comment} end-shorthand`。
  - 例如__代码0__。

## 速记键

- **`()=>`** = 90% 注释和 10% 混合语言的伪代码块。
  - 当行以 `()=>` 作为起始字符集时，使用您的 **角色** 来确定
目标的解决方案。

## 变量

- 所需文件 = `${input:file}`;
- openPrompt = "更新简写代码";
- language:comment = "编程语言的单行或多行注释。";
- openMarker = "${语言:comment} 开始简写";
- closeMarker = "${语言:comment} 结束简写";

## 使用示例

### 提示输入

```bash
[user prompt]
UPDATE CODE FROM SHORTHAND 
#file:script.js 
Use #file:index.html:94-99 to see where converted
markdown to html will be parsed `id="a"`.
```

### 代码文件

```js
// script.js
// Parse markdown file, applying HTML to render output.

var file = "file.md";
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
 if (this.readyState == 4 && this.status == 200) {
  let data = this.responseText;
  let a = document.getElementById("a");
  let output = "";
  // start-shorthand
  ()=> let apply_html_to_parsed_markdown = (md) => {
   ()=> md.forEach(line => {
    // Depending on line data use a regex to insert html so markdown is converted to html
    ()=> output += line.replace(/^(regex to add html elements from markdonw line)(.*)$/g, $1$1);
   });
   // Output the converted file from markdown to html.
   return output;
  };
  ()=>a.innerHTML = apply_html_to_parsed_markdown(data);
  // end-shorthand
 }
};
xhttp.open("GET", file, true);
xhttp.send();
```
