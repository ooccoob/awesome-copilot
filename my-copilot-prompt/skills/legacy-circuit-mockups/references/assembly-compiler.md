# 6502 SBC 汇编编译和 ROM 构建规范

## 概述

本文档定义了**为单板计算机编译 6502 汇编语言**的完整规范，其中包括：

* **MOS 6502 CPU**
* **MOS 6522 过孔**
* **AS6C62256（32 KB SRAM）**
* **AT28C256（32 KB EEPROM / ROM）**
* **DFRobot FIT0127（兼容 HD44780 的 16x2 LCD）**

重点是**工具链行为、内存布局、ROM 构造和固件约定**，而不是电气布线。

---

## 目标系统架构

### 内存映射（规范）

```
$0000-$00FF  Zero Page (RAM)
$0100-$01FF  Stack (RAM)
$0200-$7FFF  General RAM (AS6C62256)
$8000-$8FFF  6522 VIA I/O space
$9000-$FFFF  ROM (AT28C256)
```

> 地址解码可以镜像设备；汇编器采用这种规范布局。

---

## ROM组织（AT28C256）

|地址 |目的|
| ----------- | -------------------- |
| $9000-$FFEF |程序代码+数据|
| $FFF0-$FFF9 |可选系统数据|
| $FFFA-$FFFB | NMI矢量|
| $FFFC-$FFFD |重置矢量|
| $FFFE-$FFFF | IRQ/BRK向量|

ROM 映像大小：**32,768 字节**

---

## 重置和启动约定

复位时：

1. CPU 在 `$FFFC` 处获取 RESET 向量
2. 代码初始化堆栈指针
3. 初始化零页变量
4. 威盛配置
5. 液晶显示屏初始化
6. 主程序进入

---

## 汇编器要求

汇编器**必须**支持：

* `.org` 绝对寻址
* 象征性标签
* 二进制输出（`.bin`）
* 小尾数字发射
* 零页面优化

推荐的组装商：

* **ca65**（cc65 工具链）
* **vasm6502**
* **64塔斯**

---

## 汇编源结构

```asm
;---------------------------
; Reset Vector Entry Point
;---------------------------
        .org $9000
RESET:
        sei
        cld
        ldx #$FF
        txs
        jsr init_via
        jsr init_lcd
MAIN:
        jsr lcd_print
        jmp MAIN
```

---

## 向量表定义

```asm
        .org $FFFA
        .word nmi_handler
        .word RESET
        .word irq_handler
```

---

## 6522 VIA 编程模型

### 注册地图（基础 = $8000）

|偏移|注册 |
| ------ | -------- |
| 0 美元 | ORB |
| 1 美元 |欧拉 |
| 2 美元 | DDRB |
| 3 美元 | DDRA |
| 4 美元 | T1CL |
| 5 美元 | T1CH |
| 6 美元 | T1LL |
| 7 美元 | T1LH |
| 8 美元 | T2CL |
| 9 美元 | T2CH |
| $B | ACR |
| $C |聚合酶链反应 |
| $D |仪表飞行规则 |
| $E | IER |

---

## LCD接口约定

### LCD 接线假设

|液晶显示器|威盛|
| ----- | ------- |
| D4-D7 | PB4-PB7 |
| RS | PA0 |
|电子| PA1 |
|读/写 |接地 |

假定为 4 位模式。

---

## LCD 初始化顺序

```asm
lcd_init:
        lda #$33
        jsr lcd_cmd
        lda #$32
        jsr lcd_cmd
        lda #$28
        jsr lcd_cmd
        lda #$0C
        jsr lcd_cmd
        lda #$06
        jsr lcd_cmd
        lda #$01
        jsr lcd_cmd
        rts
```

---

## LCD命令/数据接口

|运营| RS |数据|
| --------- | -- | --------------- |
|命令 | 0 |说明 |
|数据| 1 | ASCII 字符 |

---

## 零页使用约定

|地址 |目的|
| ------- | ------------ |
| $00-$0F |刮刮|
| $10-$1F |液晶例程|
| $20-$2F |威盛状态|
| $30-$FF |用户定义 |

---

## RAM 使用情况 (AS6C62256)

* 堆栈使用页 `$01`
* 所有 RAM 均假定为易失性
* 无 ROM 阴影

---

## 建设管道

### 第 1 步：组装

```bash
ca65 main.asm -o main.o
```

### 第 2 步：链接

```bash
ld65 -C rom.cfg main.o -o rom.bin
```

### 步骤3：垫ROM

确保 `rom.bin` 恰好是 **32768 字节**。

---

## EEPROM编程

* 目标设备：**AT28C256**
* 编程器：**MiniPro / T48**
* 写入后验证

---

## 模拟器期望

模拟器必须：

* 在 `$9000-$FFFF` 加载 ROM
* 模拟 VIA I/O 副作用
* 渲染 LCD 输出
* 荣誉重置矢量

---

## 测试清单

* 重置向量执行
* VIA 寄存器写入
* LCD 显示正确的文字
* 堆栈操作有效
* ROM 映像正确映射

---

## 参考文献

* [MOS 6502 编程手册](http://archive.6502.org/datasheets/synertek_programming_manual.pdf)
* [MOS 6522 VIA 数据表](http://archive.6502.org/datasheets/mos_6522_preliminary_nov_1977.pdf)
* [AT28C256 数据表](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT28C256-Industrial-Grade-256-Kbit-Paged-Parallel-EEPROM-Data-Sheet-DS20006386.pdf)
* [HD44780 LCD 数据表](https://www.futurlec.com/LED/LCD16X2BLa.shtml)
* [cc65 工具链文档](https://cc65.github.io/doc/cc65.html)

---

## 注释

该规范有意实现**端到端**：从汇编源代码到 EEPROM 映像，再到运行的硬件或仿真器。它定义了一个稳定的合约，因此 ROM、模拟器和真实的 SBC 的行为相同。
