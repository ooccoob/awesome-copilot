---
name: legacy-circuit-mockups
description: 'Generate breadboard circuit mockups and visual diagrams using HTML5 Canvas drawing techniques. Use when asked to create circuit layouts, visualize electronic component placements, draw breadboard diagrams, mockup 6502 builds, generate retro computer schematics, or design vintage electronics projects. Supports 555 timers, W65C02S microprocessors, 28C256 EEPROMs, W65C22 VIA chips, 7400-series logic gates, LEDs, resistors, capacitors, switches, buttons, crystals, and wires.'
---

# 传统电路模型

为复古计算和电子项目创建面包板电路模型和可视化图表的技能。该技能利用 HTML5 Canvas 绘图机制来渲染交互式电路布局，其中包括 6502 微处理器、555 定时器 IC、EEPROM 和 7400 系列逻辑门等老式组件。

## 何时使用此技能

- 用户要求“创建面包板布局”或“模拟电路”
- 用户希望可视化面包板上的组件放置
- 用户需要构建 6502 计算机的视觉参考
- 用户要求“画电路”或“电子图”
- 用户想要创建教育电子视觉效果
- 用户提到 Ben Eater 教程或复古计算项目
- 用户要求制作 555 定时器电路或 LED 项目的模型
- 用户需要可视化组件之间的接线

## 先决条件

- 从捆绑的参考文件中了解组件引脚排列
- 了解面包板布局约定（行、列、电源轨）

## 支持的组件

### 微处理器和内存

|组件|针脚 |描述 |
|-----------|------|-------------|
| W65C02S | 40 针 DIP |具有 16 位地址总线的 8 位微处理器 |
| 28C256 | 28C256 28 针 DIP | 32KB 并行 EEPROM |
| W65C22 | 40 针 DIP |多功能接口适配器 (VIA) |
| 62256 | 62256 28 针 DIP | 32KB 静态 RAM |

### 逻辑和定时器 IC

|组件|针脚 |描述 |
|-----------|------|-------------|
| NE555 | 8 针 DIP |用于定时和振荡的定时器IC |
| 7400| 14 针 DIP |四路 2 输入与非门 |
| 7402 | 7402 14 针 DIP |四路 2 输入或非门 |
| 7404 | 7404 14 针 DIP |六角反相器（非门）|
| 7408 | 14 针 DIP |四路 2 输入与门 |
| 7432 | 14 针 DIP |四路 2 输入或门 |

### 无源和有源元件

|组件|描述 |
|-----------|-------------|
| LED |发光二极管（各种颜色）|
|电阻|电流限制（可配置值）|
|电容器|过滤和计时（陶瓷/电解）|
|水晶|时钟振荡器|
|开关|拨动开关（锁定）|
|按钮|瞬时按钮|
|电位器|可变电阻|
|光敏电阻|光敏电阻|

### 网格系统

```javascript
// Standard breadboard grid: 20px spacing
const gridSize = 20;
const cellX = Math.floor(x / gridSize) * gridSize;
const cellY = Math.floor(y / gridSize) * gridSize;
```

### 组件渲染模式

```javascript
// All components follow this structure:
{
  type: 'component-type',
  x: gridX,
  y: gridY,
  width: componentWidth,
  height: componentHeight,
  rotation: 0,  // 0, 90, 180, 270
  properties: { /* component-specific data */ }
}
```

### 接线

```javascript
// Wire connection format:
{
  start: { x: startX, y: startY },
  end: { x: endX, y: endY },
  color: '#ff0000'  // Wire color coding
}
```

## 分步工作流程

### 创建基本 LED 电路模型

1. 定义面包板尺寸和网格
2. 放置电源轨连接（+5V 和 GND）
3. 添加具有阳极/阴极方向的 LED 组件
4. 放置限流电阻
5. 绘制组件之间的接线
6. 添加标签和注释

### 创建 555 定时器电路

1. 将 NE555 IC 放置在面包板上（引脚 1-4 左，5-8 右）
2. 将引脚 1 (GND) 连接至接地轨
3. 将引脚 8 (Vcc) 连接到电源轨
4. 添加定时电阻和电容
5. 连线触发和阈值连接
6. 将输出连接至 LED 或其他负载

### 创建 6502 微处理器布局

1. 将 W65C02S 放置在面包板中央
2. 添加28C256 EEPROM用于程序存储
3. 将 W65C22 VIA 用于 I/O
4. 添加 7400 系列地址解码逻辑
5. 连线地址总线 (A0-A15)
6. 有线数据总线（D0-D7）
7. 连接控制信号（R/W、PHI2、RESB）
8. 添加重置按钮和时钟晶体

## 组件引脚排列快速参考

### 555定时器（8针DIP）

|针 |名称 |功能|
|:---:|:-----|:---------|
| 1 |接地 |接地（0V）|
| 2 |触发|触发（< 1/3 Vcc 开始计时）|
| 3 |输出 |输出（拉电流/灌电流 200mA）|
| 4 |重置 |低电平有效复位|
| 5 | CTRL |控制电压（10nF 旁路）|
| 6 | THR |阈值（> 2/3 Vcc 复位）|
| 7 | DIS |放电（集电极开路）|
| 8 |电源电压|电源（+4.5V 至 +16V）|

### W65C02S（40 引脚 DIP）- 关键引脚

|针 |名称 |功能|
|:---:|:-----|:---------|
| 8 |电源电压|电源|
| 21 | 21 VSS |地面|
| 37 | 37 PHI2 |系统时钟输入|
| 40 | 40 RESB |低电平有效复位|
| 34 | 34 RWB |读/写信号|
| 9-25 | A0-A15 |地址总线|
| 26-33 | 26-33 D0-D7 |数据总线|

### 28C256 EEPROM（28 引脚 DIP）- 关键引脚

|针 |名称 |功能|
|:---:|:-----|:---------|
| 14 | 14接地 |地面|
| 28 | 28 VCC |电源|
| 20 |欧盟CE |芯片使能（低电平有效）|
| 22 | 22原厂设备 |输出使能（低电平有效）|
| 27 | 27我们|写使能（低电平有效）|
| 1-10、21-26 | A0-A14 |地址输入|
| 11-19 | I/O0-I/O7 |数据总线|

## 公式参考

### 电阻计算

- **欧姆定律：** V = I × R
- **LED 电流：** R = (Vcc - Vled) / Iled
- **功率：** P = V × I = I² × R

### 正常 双线555服 [双线555服]

**不稳定模式：**

- 频率：f = 1.44 / ((R1 + 2×R2) × C)
- 高电平时间：t₁ = 0.693 × (R1 + R2) × C
- 低电平时间：t2 = 0.693 × R2 × C
- 占空比：D=(R1+R2)/(R1+2×R2)×100%

**单稳态模式：**

- 脉冲宽度：T=1.1×R×C

### 电容计算

- 容抗：Xc=1/(2πfC)
- 储存能量：E = ½ × C × V²

## 颜色编码约定

### 电线颜色

|颜色 |目的|
|-------|---------|
|红色| +5V/电源|
|黑色|地面|
|黄色|时钟/计时|
|蓝色|地址总线|
|绿色|数据总线|
|橙色|控制信号|
|白色|通用|

### LED 颜色

|颜色 |正向电压|
|-------|-----------------|
|红色| 1.8V - 2.2V |
|绿色| 2.0V - 2.2V |
|黄色| 2.0V - 2.2V |
|蓝色| 3.0V - 3.5V |
|白色| 3.0V - 3.5V |

## 构建示例

### 构建 1 — 单 LED

**组件：** 红色 LED、220Ω 电阻、跳线、电源

**步骤：**

1. 将黑色跳线从电源 GND 插入 A5 排
2. 将电源 +5V 的红色跳线插入 J5 排
3. 将带有阴极（短腿）的 LED 放置在与 GND 对齐的行中
4. 在电源和 LED 阳极之间放置 220Ω 电阻

### 构建 2 — 555 不稳定信号灯

**组件：** NE555、LED、电阻（10kΩ、100kΩ）、电容（10μF）

**步骤：**

1. 将 555 IC 跨置于中央通道
2. 将引脚 1 连接至 GND，将引脚 8 连接至 +5V
3. 将引脚 4 连接到引脚 8（禁用复位）
4. 在引脚 7 和 +5V 之间连接 10kΩ 导线
5. 在引脚 6 和 7 之间连接 100kΩ 电阻
6. 在引脚 6 和 GND 之间连接 10μF 导线
7. 将引脚 3（输出）连接到 LED 电路

## 故障排除

|问题 |解决方案 |
|-------|----------|
| LED 不亮 |检查极性（阳极为+，阴极为-） |
|电路不通电 |验证电源轨连接 |
|集成电路不工作|检查 VCC 和 GND 引脚连接 |
| 555不振荡|验证阈值/触发电容器接线 |
|微处理器卡住|复位脉冲后检查 RESB 是否为高电平 |

## 参考文献

捆绑的参考文件中提供了详细的组件规格：

- [555.md](references/555-zh.md) - 完整的 555 定时器 IC 规范
- [6502.md](references/6502-zh.md) - MOS 6502 微处理器详细信息
- [6522.md](references/6522-zh.md) - W65C22 VIA 接口适配器
- [28256-eeprom.md](references/28256-eeprom-zh.md) - AT28C256 EEPROM 规范
- [6C62256.md](references/6C62256-zh.md) - 62256 SRAM 详细信息
- [7400-series.md](references/7400-series-zh.md) - TTL 逻辑门引脚排列
- [ assembly-compiler.md](references/assembly-compiler-zh.md) - 汇编编译器规范
- [汇编语言.md](references/assembly-language-zh.md) - 汇编语言规范
- [basic-Electronic-Components.md](references/basic-electronic-components-zh.md) - 电阻器、电容器、开关
- [breadboard.md](references/breadboard-zh.md) - 面包板规格
- [common-breadboard-components.md](references/common-breadboard-components-zh.md) - 综合组件参考
- [connecting-Electronic-Components.md](references/connecting-electronic-components-zh.md) - 分步构建指南
- [emulator-28256-eeprom.md](references/emulator-28256-eeprom-zh.md) - 模拟 28256-eeprom 规范
- [emulator-6502.md](references/emulator-6502-zh.md) - 模拟 6502 规范
- [emulator-6522.md](references/emulator-6522-zh.md) - 模拟 6522 规范
- [emulator-6C62256.md](references/emulator-6C62256-zh.md) - 模拟 6C62256 规范
- [emulator-lcd.md](references/emulator-lcd-zh.md) - 模拟 LCD 规范
- [lcd.md](references/lcd-zh.md) - LCD 显示接口
- [minipro.md](references/minipro-zh.md) - EEPROM 编程器使用
- [t48eeprom-programmer.md](references/t48eeprom-programmer-zh.md) - T48 程序员参考
