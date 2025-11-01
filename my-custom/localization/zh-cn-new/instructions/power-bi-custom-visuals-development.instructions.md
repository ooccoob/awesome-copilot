---
description: '全面的 Power BI 自定义视觉对象开发指南，涵盖 React、D3.js 集成、TypeScript 模式、测试框架和高级可视化技术。'
applyTo: '**/*.{ts,tsx,js,jsx,json,less,css}'
---

# Power BI 自定义视觉对象开发最佳实践

## 概述
本文档提供了基于 Microsoft 官方指导和社区最佳实践，使用现代 Web 技术包括 React、D3.js、TypeScript 和高级测试框架开发自定义 Power BI 视觉对象的综合指令。

## 开发环境设置

### 1. 项目初始化
```typescript
// 全局安装 Power BI 视觉对象工具
npm install -g powerbi-visuals-tools

// 创建新的视觉对象项目
pbiviz new MyCustomVisual
cd MyCustomVisual

// 启动开发服务器
pbiviz start
```

### 2. TypeScript 配置
```json
{
    "compilerOptions": {
        "jsx": "react",
        "types": ["react", "react-dom"],
        "allowJs": false,
        "emitDecoratorMetadata": true,
        "experimentalDecorators": true,
        "target": "es6",
        "sourceMap": true,
        "outDir": "./.tmp/build/",
        "moduleResolution": "node",
        "declaration": true,
        "lib": [
            "es2015",
            "dom"
        ]
    },
    "files": [
        "./src/visual.ts"
    ]
}
```

## 核心视觉对象开发模式

### 1. 基本视觉对象结构
```typescript
"use strict";
import powerbi from "powerbi-visuals-api";

import DataView = powerbi.DataView;
import VisualConstructorOptions = powerbi.extensibility.visual.VisualConstructorOptions;
import VisualUpdateOptions = powerbi.extensibility.visual.VisualUpdateOptions;
import IVisual = powerbi.extensibility.visual.IVisual;
import IVisualHost = powerbi.extensibility.IVisualHost;

import "./../style/visual.less";

export class Visual implements IVisual {
    private target: HTMLElement;
    private host: IVisualHost;

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
    }

    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView) {
            return;
        }

        // 视觉对象更新逻辑
    }

    public getFormattingModel(): powerbi.visuals.FormattingModel {
        return this.formattingSettingsService.buildFormattingModel(this.formattingSettings);
    }
}
```

### 2. 数据视图处理
```typescript
// 单一数据映射示例
export class Visual implements IVisual {
    private valueText: HTMLParagraphElement;

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
        this.valueText = document.createElement("p");
        this.target.appendChild(this.valueText);
    }

    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView || !dataView.categorical) {
            return;
        }

        const categorical: powerbi.DataViewCategorical = dataView.categorical;
        const category: powerbi.DataViewCategoryColumn = categorical.categories[0];
        const value: powerbi.DataViewValueColumn = categorical.values[0];

        let dataString = "";

        for (let i = 0; i < category.values.length; i++) {
            dataString += `${category.values[i]}: ${value.values[i]}\n`;
        }

        this.valueText.innerText = dataString;
    }
}
```

### 3. 表格式数据处理
```typescript
// 表格式数据映射示例
export class Visual implements IVisual {
    private table: HTMLTableElement;

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
        this.table = document.createElement("table");
        this.target.appendChild(this.table);
    }

    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView || !dataView.table) {
            return;
        }

        const table: powerbi.DataViewTable = dataView.table;
        this.renderTable(table);
    }

    private renderTable(table: powerbi.DataViewTable) {
        this.table.innerHTML = "";

        // 创建表头
        const headerRow = this.table.createTHead().insertRow();
        table.columns.forEach((column, index) => {
            const th = document.createElement("th");
            th.textContent = column.displayName;
            headerRow.appendChild(th);
        });

        // 创建数据行
        const tbody = this.table.createTBody();
        table.rows.forEach((row) => {
            const tr = tbody.insertRow();
            table.columns.forEach((column, index) => {
                const td = tr.insertCell();
                td.textContent = row[index].toString();
            });
        });
    }
}
```

## React 集成

### 1. React 视觉对象基础
```typescript
import * as React from 'react';
import * as ReactDOM from 'react-dom';

class ReactVisual implements IVisual {
    private target: HTMLElement;
    private host: IVisualHost;
    private reactRoot: React.ComponentElement<any, any>;

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
    }

    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView) {
            return;
        }

        const props = {
            dataView: dataView,
            host: this.host
        };

        if (!this.reactRoot) {
            this.reactRoot = React.createElement(MyReactComponent, props);
            ReactDOM.render(this.reactRoot, this.target);
        } else {
            // 更新现有组件
            ReactDOM.render(
                React.cloneElement(this.reactRoot, props),
                this.target
            );
        }
    }
}

// React 组件示例
const MyReactComponent: React.FC<{ dataView: DataView, host: IVisualHost }> = ({ dataView, host }) => {
    const [data, setData] = React.useState<any[]>([]);

    React.useEffect(() => {
        if (dataView && dataView.categorical) {
            const categorical = dataView.categorical;
            const processedData = processData(categorical);
            setData(processedData);
        }
    }, [dataView]);

    return (
        <div className="visual-container">
            {data.map((item, index) => (
                <div key={index} className="data-item">
                    <span>{item.category}: {item.value}</span>
                </div>
            ))}
        </div>
    );
};
```

### 2. 高级 React 模式
```typescript
// 使用 React Hooks 的复杂视觉对象
import { useState, useEffect, useCallback, useMemo } from 'react';

interface DataPoint {
    category: string;
    value: number;
    color?: string;
}

const AdvancedReactComponent: React.FC<{
    dataView: DataView;
    host: IVisualHost;
    formattingSettings: FormattingSettings;
}> = ({ dataView, host, formattingSettings }) => {
    const [data, setData] = useState<DataPoint[]>([]);
    const [selectedItem, setSelectedItem] = useState<string | null>(null);
    const [hoveredItem, setHoveredItem] = useState<string | null>(null);

    // 数据处理
    useEffect(() => {
        if (dataView?.categorical) {
            const processedData = processCategoricalData(dataView.categorical);
            setData(processedData);
        }
    }, [dataView]);

    // 交互处理
    const handleItemClick = useCallback((item: DataPoint) => {
        setSelectedItem(item.category);

        // 触发 Power BI 选择
        const selectionId = host.createSelectionIdBuilder()
            .withCategory(dataView.categorical.categories[0], item.index)
            .createSelectionId();

        host.selectionManager.select(selectionId);
    }, [dataView, host]);

    // 计算属性
    const maxValue = useMemo(() => {
        return Math.max(...data.map(d => d.value));
    }, [data]);

    // 渲染逻辑
    return (
        <div className="advanced-visual">
            {data.map((item, index) => (
                <div
                    key={item.category}
                    className={`data-point ${selectedItem === item.category ? 'selected' : ''}`}
                    style={{
                        height: `${(item.value / maxValue) * 100}%`,
                        backgroundColor: hoveredItem === item.category ? '#ff6b6b' : item.color
                    }}
                    onClick={() => handleItemClick(item)}
                    onMouseEnter={() => setHoveredItem(item.category)}
                    onMouseLeave={() => setHoveredItem(null)}
                >
                    <span className="label">{item.category}</span>
                    <span className="value">{item.value}</span>
                </div>
            ))}
        </div>
    );
};
```

## D3.js 集成

### 1. 基本 D3.js 视觉对象
```typescript
import * as d3 from 'd3';

class D3Visual implements IVisual {
    private target: HTMLElement;
    private host: IVisualHost;
    private svg: d3.Selection<SVGSVGElement, unknown, null, undefined>;

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
        this.svg = d3.select(this.target)
            .append('svg')
            .attr('width', '100%')
            .attr('height', '100%');
    }

    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView || !dataView.categorical) {
            return;
        }

        const data = this.processData(dataView.categorical);
        this.renderChart(data);
    }

    private renderChart(data: DataPoint[]) {
        const margin = { top: 20, right: 20, bottom: 30, left: 40 };
        const width = this.target.clientWidth - margin.left - margin.right;
        const height = this.target.clientHeight - margin.top - margin.bottom;

        // 清除现有内容
        this.svg.selectAll('*').remove();

        const g = this.svg
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // 创建比例尺
        const x = d3.scaleBand()
            .domain(data.map(d => d.category))
            .range([0, width])
            .padding(0.1);

        const y = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.value)])
            .range([height, 0]);

        // 创建坐标轴
        g.append('g')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x));

        g.append('g')
            .call(d3.axisLeft(y));

        // 创建柱状图
        g.selectAll('.bar')
            .data(data)
            .enter().append('rect')
            .attr('class', 'bar')
            .attr('x', d => x(d.category))
            .attr('width', x.bandwidth())
            .attr('y', d => y(d.value))
            .attr('height', d => height - y(d.value))
            .attr('fill', '#4CAF50');
    }
}
```

### 2. 高级 D3.js 动画和交互
```typescript
class AdvancedD3Visual implements IVisual {
    private svg: d3.Selection<SVGSVGElement, unknown, null, undefined>;
    private simulation: d3.Simulation<any, undefined>;

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
        this.svg = d3.select(this.target).append('svg');
    }

    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView) {
            return;
        }

        const data = this.processData(dataView);
        this.renderForceDirectedGraph(data);
    }

    private renderForceDirectedGraph(nodes: any[]) {
        const width = this.target.clientWidth;
        const height = this.target.clientHeight;

        this.svg.selectAll('*').remove();

        // 创建力模拟
        this.simulation = d3.forceSimulation(nodes)
            .force('charge', d3.forceManyBody().strength(-100))
            .force('center', d3.forceCenter(width / 2, height / 2))
            .force('collision', d3.forceCollide().radius(20));

        // 创建节点
        const node = this.svg.selectAll('.node')
            .data(nodes)
            .enter().append('circle')
            .attr('class', 'node')
            .attr('r', d => Math.sqrt(d.value) * 2)
            .attr('fill', (d, i) => d3.schemeCategory10[i % 10])
            .call(d3.drag<SVGCircleElement, any>()
                .on('start', dragstarted)
                .on('drag', dragged)
                .on('end', dragended));

        // 添加标签
        const label = this.svg.selectAll('.label')
            .data(nodes)
            .enter().append('text')
            .attr('class', 'label')
            .text(d => d.category)
            .attr('font-size', '12px')
            .attr('dx', 12)
            .attr('dy', 4);

        // 更新位置
        this.simulation.on('tick', () => {
            node.attr('cx', d => d.x)
                .attr('cy', d => d.y);

            label.attr('x', d => d.x)
                .attr('y', d => d.y);
        });

        // 拖拽函数
        function dragstarted(event: any, d: any) {
            if (!event.active) this.simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event: any, d: any) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragended(event: any, d: any) {
            if (!event.active) this.simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }
    }
}
```

## 格式化和属性窗格

### 1. 基本格式化设置
```typescript
import { FormattingSettingsService } from "powerbi-visuals-utils-formattingmodel";

// 定义格式化接口
interface VisualFormattingSettingsModel {
    general: GeneralSettings;
    colors: ColorSettings;
    labels: LabelSettings;
}

interface GeneralSettings {
    showTitle: boolean;
    titleText: string;
}

interface ColorSettings {
    primaryColor: string;
    secondaryColor: string;
    useGradient: boolean;
}

interface LabelSettings {
    showLabels: boolean;
    labelSize: number;
    labelColor: string;
}

// 格式化设置类
class FormattingSettings {
    private _general: GeneralSettings;
    private _colors: ColorSettings;
    private _labels: LabelSettings;

    constructor() {
        this._general = new GeneralSettings();
        this._colors = new ColorSettings();
        this._labels = new LabelSettings();
    }

    get general(): GeneralSettings {
        return this._general;
    }

    get colors(): ColorSettings {
        return this._colors;
    }

    get labels(): LabelSettings {
        return this._labels;
    }
}

// 实现格式化模型
export class Visual implements IVisual {
    private formattingSettings: FormattingSettings;
    private formattingSettingsService: FormattingSettingsService;

    constructor(options: VisualConstructorOptions) {
        this.formattingSettings = new FormattingSettings();
        this.formattingSettingsService = new FormattingSettingsService();
    }

    public getFormattingModel(): powerbi.visuals.FormattingModel {
        return this.formattingSettingsService.buildFormattingModel(this.formattingSettings);
    }

    public update(options: VisualUpdateOptions) {
        // 使用格式化设置
        if (this.formattingSettings.general.showTitle) {
            // 显示标题
        }

        const primaryColor = this.formattingSettings.colors.primaryColor;
        // 使用颜色设置
    }
}
```

### 2. 高级格式化选项
```typescript
import {
    DataColorPalette,
    DataColorPaletteHelper,
    IColorPalette
} from "powerbi-visuals-utils-colorutils";

interface AdvancedFormattingSettings {
    dataColors: DataColorSettings;
    axis: AxisSettings;
    tooltips: TooltipSettings;
    animations: AnimationSettings;
}

interface DataColorSettings {
    showDataLabels: boolean;
    colorPalette: IColorPalette;
    singleColor: string;
}

interface AxisSettings {
    showXAxis: boolean;
    showYAxis: boolean;
    axisColor: string;
    axisWidth: number;
    showGridlines: boolean;
}

interface TooltipSettings {
    showTooltips: boolean;
    backgroundColor: string;
    textColor: string;
    fontSize: number;
}

interface AnimationSettings {
    enableAnimations: boolean;
    animationDuration: number;
    animationEasing: string;
}

// 在视觉对象中使用高级格式化
export class Visual implements IVisual {
    private updateColors(data: any[]) {
        const colorPalette = this.formattingSettings.dataColors.colorPalette;

        if (colorPalette && colorPalette.isHighContrast) {
            // 高对比度模式
            return data.map((d, i) => ({
                ...d,
                color: colorPalette.getColor(i.toString())
            }));
        } else {
            // 正常模式
            return data.map((d, i) => ({
                ...d,
                color: this.formattingSettings.dataColors.singleColor ||
                        colorPalette.getColor(i.toString())
            }));
        }
    }

    private renderChart(data: any[]) {
        const coloredData = this.updateColors(data);

        if (this.formattingSettings.animations.enableAnimations) {
            this.animateChart(coloredData);
        } else {
            this.renderChartStatic(coloredData);
        }
    }

    private animateChart(data: any[]) {
        const duration = this.formattingSettings.animations.animationDuration;
        const easing = this.formattingSettings.animations.animationEasing;

        // D3.js 动画实现
        this.svg.selectAll('.bar')
            .data(data)
            .transition()
            .duration(duration)
            .ease(d3.ease(easing as any))
            .attr('height', d => d.height)
            .attr('y', d => d.y);
    }
}
```

## 数据绑定和选择

### 1. 数据选择管理
```typescript
import {
    ISelectionIdBuilder,
    ISelectionManager
} from "powerbi-visuals-utils-interactivityutils";

export class Visual implements IVisual {
    private selectionIdBuilder: ISelectionIdBuilder;
    private selectionManager: ISelectionManager;
    private selectedIds: powerbi.visuals.ISelectionId[];

    constructor(options: VisualConstructorOptions) {
        this.host = options.host;
        this.selectionIdBuilder = this.host.createSelectionIdBuilder();
        this.selectionManager = this.host.selectionManager;
        this.selectedIds = [];
    }

    private createSelectionId(index: number): powerbi.visuals.ISelectionId {
        return this.selectionIdBuilder
            .withCategory(this.dataView.categorical.categories[0], index)
            .createSelectionId();
    }

    private handleDataPointClick(dataPoint: any, index: number) {
        const selectionId = this.createSelectionId(index);

        // 检查是否已选择
        const isSelected = this.selectedIds.some(id =>
            id.equals(selectionId)
        );

        if (isSelected) {
            // 取消选择
            this.selectedIds = this.selectedIds.filter(id =>
                !id.equals(selectionId)
            );
        } else {
            // 添加选择
            this.selectedIds.push(selectionId);
        }

        // 应用选择
        this.selectionManager.select(this.selectedIds);
    }

    public update(options: VisualUpdateOptions) {
        // 处理选择状态
        if (options && options.selectionIds) {
            this.selectedIds = options.selectionIds;
            this.updateSelectionVisuals();
        }
    }

    private updateSelectionVisuals() {
        // 更新视觉选择状态
        this.svg.selectAll('.data-point')
            .style('opacity', (d, i) => {
                const selectionId = this.createSelectionId(i);
                const isSelected = this.selectedIds.some(id =>
                    id.equals(selectionId)
                );
                return isSelected ? 1 : 0.5;
            });
    }
}
```

### 2. 多重选择和交叉筛选
```typescript
export class Visual implements IVisual {
    private selectedCategories: Set<number> = new Set();
    private selectedSeries: Set<number> = new Set();

    private handleCategoryClick(categoryIndex: number) {
        if (this.selectedCategories.has(categoryIndex)) {
            this.selectedCategories.delete(categoryIndex);
        } else {
            this.selectedCategories.add(categoryIndex);
        }

        this.updateSelection();
    }

    private updateSelection() {
        const selectionIds: powerbi.visuals.ISelectionId[] = [];

        // 创建选择ID
        this.selectedCategories.forEach(categoryIndex => {
            this.selectedSeries.forEach(seriesIndex => {
                const selectionId = this.selectionIdBuilder
                    .withCategory(this.dataView.categorical.categories[categoryIndex], categoryIndex)
                    .withSeries(this.dataView.categorical.values[seriesIndex], seriesIndex)
                    .createSelectionId();

                selectionIds.push(selectionId);
            });
        });

        this.selectionManager.select(selectionIds);
    }
}
```

## 测试框架

### 1. 单元测试设置
```typescript
import { Visual } from '../src/visual';
import { VisualBuilder } from './VisualBuilder';
import { powerbi } from 'powerbi-visuals-api';
import VisualObjectInstance = powerbi.extensibility.IVisual;

describe('Visual', () => {
    let visual: VisualObjectInstance;
    let builder: VisualBuilder;

    beforeEach(() => {
        builder = new VisualBuilder(800, 600);
        visual = builder.visual;
    });

    it('should create visual instance', () => {
        expect(visual).toBeDefined();
    });

    it('should render with data', () => {
        const dataView = builder.createCategoricalDataViewBuilder()
            .withCategories(['A', 'B', 'C'])
            .withValues([10, 20, 30])
            .build();

        builder.update(dataView);

        const elements = builder.rootElement.querySelectorAll('.data-point');
        expect(elements.length).toBe(3);
    });

    it('should handle empty data', () => {
        const dataView = builder.createEmptyDataView();
        builder.update(dataView);

        const elements = builder.rootElement.querySelectorAll('.data-point');
        expect(elements.length).toBe(0);
    });

    it('should update colors on formatting change', () => {
        const dataView = builder.createCategoricalDataViewBuilder()
            .withCategories(['A', 'B'])
            .withValues([10, 20])
            .build();

        builder.update(dataView);

        // 更新格式化
        visual.update({
            dataViews: [dataView],
            type: powerbi.VisualUpdateType.Data,
            viewport: { width: 800, height: 600 }
        });

        // 验证颜色更改
        const firstElement = builder.rootElement.querySelector('.data-point');
        expect(firstElement).toBeDefined();
    });
});
```

### 2. 集成测试
```typescript
import { VisualBuilder } from './VisualBuilder';
import { FormattingSettings } from '../src/settings/formatting-settings';

describe('Visual Integration Tests', () => {
    let builder: VisualBuilder;

    beforeEach(() => {
        builder = new VisualBuilder(800, 600);
    });

    it('should handle selection correctly', () => {
        const dataView = builder.createCategoricalDataViewBuilder()
            .withCategories(['A', 'B', 'C'])
            .withValues([10, 20, 30])
            .build();

        builder.update(dataView);

        // 模拟点击
        const firstElement = builder.rootElement.querySelector('.data-point');
        firstElement.dispatchEvent(new MouseEvent('click'));

        // 验证选择
        const selectionManager = builder.host.selectionService;
        expect(selectionManager.getSelectionIds().length).toBeGreaterThan(0);
    });

    it('should respond to formatting changes', () => {
        const dataView = builder.createCategoricalDataViewBuilder()
            .withCategories(['A', 'B'])
            .withValues([10, 20])
            .build();

        builder.update(dataView);

        // 更新格式化设置
        const formattingSettings = new FormattingSettings();
        formattingSettings.general.showTitle = true;
        formattingSettings.general.titleText = 'Test Title';

        visual.update({
            dataViews: [dataView],
            type: powerbi.VisualUpdateType.Data,
            viewport: { width: 800, height: 600 },
            operations: {
                // 格式化操作
            }
        });

        // 验证标题显示
        const titleElement = builder.rootElement.querySelector('.visual-title');
        expect(titleElement.textContent).toBe('Test Title');
    });
});
```

## 性能优化

### 1. 渲染优化
```typescript
export class Visual implements IVisual {
    private animationFrameId: number;
    private isUpdatePending: boolean;

    public update(options: VisualUpdateOptions) {
        // 取消挂起的更新
        if (this.animationFrameId) {
            cancelAnimationFrame(this.animationFrameId);
        }

        // 批量更新
        this.animationFrameId = requestAnimationFrame(() => {
            this.performUpdate(options);
            this.animationFrameId = null;
        });
    }

    private performUpdate(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        if (!dataView) {
            return;
        }

        // 检查是否需要重新渲染
        if (this.shouldSkipUpdate(dataView)) {
            return;
        }

        this.render(dataView);
    }

    private shouldSkipUpdate(dataView: DataView): boolean {
        // 检查数据是否真的改变了
        if (!this.lastDataView || !this.lastDataView.categorical) {
            return false;
        }

        const currentCategorical = dataView.categorical;
        const lastCategorical = this.lastDataView.categorical;

        // 比较数据
        if (currentCategorical.categories.length !== lastCategorical.categories.length) {
            return false;
        }

        // 检查值是否相同
        for (let i = 0; i < currentCategorical.values.length; i++) {
            const currentValues = currentCategorical.values[i].values;
            const lastValues = lastCategorical.values[i].values;

            if (currentValues.length !== lastValues.length) {
                return false;
            }

            for (let j = 0; j < currentValues.length; j++) {
                if (currentValues[j] !== lastValues[j]) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

### 2. 内存管理
```typescript
export class Visual implements IVisual {
    private eventListeners: Map<string, EventListener> = new Map();

    constructor(options: VisualConstructorOptions) {
        this.target = options.element;
        this.host = options.host;
        this.setupEventListeners();
    }

    private setupEventListeners() {
        const resizeHandler = () => {
            this.handleResize();
        };

        this.eventListeners.set('resize', resizeHandler);
        window.addEventListener('resize', resizeHandler);
    }

    private cleanup() {
        // 清理事件监听器
        this.eventListeners.forEach((listener, event) => {
            window.removeEventListener(event, listener);
        });
        this.eventListeners.clear();

        // 清理 D3 元素
        if (this.svg) {
            this.svg.selectAll('*').remove();
            this.svg.remove();
        }

        // 清理 React 组件
        if (this.reactRoot) {
            ReactDOM.unmountComponentAtNode(this.target);
        }
    }

    public destroy() {
        this.cleanup();
    }
}
```

## 部署和发布

### 1. 构建和打包
```typescript
// pbiviz.json 配置
{
    "visual": {
        "name": "MyCustomVisual",
        "displayName": "My Custom Visual",
        "guid": "12345678-1234-1234-1234-123456789012",
        "visualClassName": "Visual",
        "version": "1.0.0",
        "description": "A custom Power BI visual",
        "supportUrl": "https://github.com/username/my-custom-visual",
        "gitHubUrl": "https://github.com/username/my-custom-visual"
    },
    "apiVersion": "5.3.0",
    "author": {
        "name": "Your Name",
        "email": "your.email@example.com"
    },
    "assets": {
        "icon": "assets/icon.png"
    },
    "externalJS": [
        {
            "url": "https://d3js.org/d3.v7.min.js"
        }
    ],
    "style": "style/visual.less",
    "capabilities": "capabilities.json"
}
```

### 2. 验证和测试
```bash
# 运行测试
npm test

# 运行 linting
npm run lint

# 运行类型检查
npm run type-check

# 打包视觉对象
pbiviz package

# 验证包
pbiviz validate
```

通过遵循这些最佳实践，您可以创建高质量、高性能且功能强大的 Power BI 自定义视觉对象。