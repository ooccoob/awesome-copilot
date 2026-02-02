# 带 AT28C256 EEPROM 的 6502 汇编语言

用于编写 **6502/65C02 汇编语言程序** 的实用规范，旨在存储在单板计算机 (SBC) 和复古系统中的 **AT28C256 (32 KB) 并行 EEPROM** 中并从中执行。

---

## 1. 范围和假设

本文档假设：

* **6502 系列 CPU**（6502、65C02 或兼容）
* 程序代码存储在 **AT28C256 (32K x 8) EEPROM** 中
* 内存映射 I/O（例如 6522 VIA）
* 复位和中断向量位于 EEPROM 中
* 映射到其他地方的外部 RAM（例如 62256 SRAM）

---

## 2. AT28C256 EEPROM 概述

|参数|价值|
| -------------- | ------------------- |
|产能 | 32 KB（32768 字节）|
|地址行| A0-A14 |
|数据线| D0-D7 |
|访问时间 | ~150 纳秒 |
|电源电压| 5V|
|套餐 | DIP-28/PLCC|

### 典型内存映射用法

|地址范围|用途 |
| ------------- | ----------------------- |
| __代码0__ | EEPROM（代码+向量）|
| __代码0__ |中断向量|

---

## 3. 6502内存映射示例

```
$0000-$00FF  Zero Page (RAM)
$0100-$01FF  Stack
$0200-$7FFF  RAM / I/O
$8000-$FFFF  AT28C256 EEPROM
```

---

## 4. 复位和中断向量

6502 从 **内存顶部** 读取向量：

|矢量|地址 |描述 |
| ------- | ------------- | ---------------------- |
|纳米医学| __代码0__ |不可屏蔽中断|
|重置| __代码0__ |重置入口点 |
| IRQ/BRK | __代码0__ |可屏蔽中断|

### 向量定义示例

```asm
        .org $FFFA
        .word nmi_handler
        .word reset
        .word irq_handler
```

---

## 5. 汇编程序结构

### 典型布局

```asm
        .org $8000

reset:
        sei             ; Disable IRQs
        cld             ; Clear decimal mode
        ldx #$FF
        txs             ; Initialize stack

main:
        jmp main
```

---

## 6. 6502 基本说明

### 寄存器

|注册 |目的|
| -------- | ---------------- |
|一个 |蓄能器|
| X，Y |索引寄存器|
| SP |堆栈指针|
|电脑|程序计数器|
|普 |处理器状态 |

### 常用说明

|说明 |功能|
| ----------- | ---------------------- |
| LDA/STA |加载/存储累加器 |
| LDX/LDY|加载索引寄存器|
| JMP/JSR |跳转/子程序|
|即时战略|从子程序返回 |
| BEQ/BNE |条件分支 |
| SEI/CLI |禁用/启用 IRQ |

---

## 7. 寻址方式（常用）

|模式|示例|笔记|
| --------- | ------------- | ------------ |
|立即 | __代码0__ |恒定|
|零页| __代码0__ |快|
|绝对| __代码0__ |完整地址 |
|索引| __代码0__ |桌子|
|间接 | __代码0__ |向量|

---

## 8. 编写 EEPROM 执行代码

### 关键考虑因素

* 代码**在运行时是只读的**
* 不推荐自行修改代码
* 将跳转表和常量放入 EEPROM 中
* 将 RAM 用于变量和堆栈

### 零页变量示例

```asm
counter = $00

        lda #$00
        sta counter
```

---

## 9. 时间和表现

* EEPROM 访问时间必须满足 CPU 时钟要求
* AT28C256 轻松支持 ~1 MHz
* 更快的时钟可能需要等待状态或 ROM 屏蔽

---

## 10. 示例：简单 LED 切换（内存映射 I/O）

```asm
PORTB = $6000
DDRB  = $6002

        .org $8000
reset:
        sei
        ldx #$FF
        txs

        lda #$FF
        sta DDRB

loop:
        lda #$FF
        sta PORTB
        jsr delay
        lda #$00
        sta PORTB
        jsr delay
        jmp loop
```

---

## 11. 组装和编程工作流程

1. 写入源代码 (`.asm`)
2. 汇编成二进制
3. 填充或重新定位到 `$8000`
4. 通过 T48 / minipro 编程 AT28C256
5. 插入EEPROM并重置CPU

---

## 12. 汇编指令（通用）

|指令|目的|
| ---------- | --------------------------- |
| __代码0__ |设置程序原点|
| __代码0__ |定义字节|
| __代码0__ |定义单词（小端）|
| __代码0__ |包含文件 |
| __代码0__ |常数定义 |

---

## 13. 常见错误

|问题 |结果 |
| -------------------------- | ------------------ |
|缺失向量 | CPU 在复位时挂起 |
|错误 `.org` |代码未执行 |
|在 ROM 中使用 RAM 地址 |崩溃 |
|堆栈未初始化|未定义的行为 |

---

## 14. 参考链接

* [https://www.masswerk.at/6502/6502_instruction_set.html](https://www.masswerk.at/6502/6502_instruction_set.html)
* [https://www.nesdev.org/wiki/6502](https://www.nesdev.org/wiki/6502)
* [https://www.westerndesigncenter.com/wdc/documentation](https://www.westerndesigncenter.com/wdc/documentation)
* [https://en.wikipedia.org/wiki/MOS_Technology_6502](https://en.wikipedia.org/wiki/MOS_Technology_6502)

---

**文档范围：** 存储在 AT28C256 EEPROM 中的 6502 组件
**受众：** 复古计算、SBC 设计师、嵌入式爱好者
**状态：** 稳定参考
