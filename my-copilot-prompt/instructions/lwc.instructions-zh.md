---
描述：“在 Salesforce Platform 上开发 Lightning Web 组件 (LWC) 的指南和最佳实践。”
applyTo: 'force-app/main/default/lwc/**'
---

# LWC发展

## 一般说明

- 每个 LWC 应驻留在 `force-app/main/default/lwc/` 下自己的文件夹中。
- 文件夹名称应与组件名称匹配（例如，`myComponent` 组件的 `myComponent` 文件夹）。
- 每个组件文件夹应包含以下文件：
    - `myComponent.html`：HTML 模板文件。
    - `myComponent.js`：JavaScript 控制器文件。
    - `myComponent.js-meta.xml`：元数据配置文件。
    - 可选：`myComponent.css` 用于组件特定的样式。
    - 可选：用于 Jest 单元测试的 `myComponent.test.js`。

## 核心原则

### 1. 在 HTML 标签上使用 Lightning 组件
为了一致性、可访问性和面向未来，始终更喜欢 Lightning Web Component 库组件而不是纯 HTML 元素。

#### 推荐方法
```html
<!-- Use Lightning components -->
<lightning-button label="Save" variant="brand" onclick={handleSave}></lightning-button>
<lightning-input type="text" label="Name" value={name} onchange={handleNameChange}></lightning-input>
<lightning-combobox label="Type" options={typeOptions} value={selectedType}></lightning-combobox>
<lightning-radio-group name="duration" label="Duration" options={durationOptions} value={duration} type="radio"></lightning-radio-group>
```

#### 避免纯 HTML
```html
<!-- Avoid these -->
<button onclick={handleSave}>Save</button>
<input type="text" onchange={handleNameChange} />
<select onchange={handleTypeChange}>
    <option value="option1">Option 1</option>
</select>
```

### 2.Lightning组件映射指南

| HTML 元素 |闪电组件|关键属性|
|--------------|-------------------|----------------|
| __代码0__ | __代码1__ | __代码2__、__代码3__、__代码4__ |
| __代码0__ | __代码1__ | __代码2__、__代码3__、__代码4__ |
| __代码0__ | __代码1__ | __代码2__、__代码3__、__代码4__ |
| __代码0__ | __代码1__ | __代码2__，__代码3__ |
| __代码0__ | __代码1__ | __代码2__，__代码3__ |
| __代码0__ | __代码1__ | __代码2__、__代码3__、__代码4__ |
| __代码0__ | __代码1__ | __代码2__，__代码3__ |
|定制药丸| __代码0__ | __代码1__、__代码2__、__代码3__ |
|图标| __代码0__ | __代码1__、__代码2__、__代码3__ |

### 3.闪电设计系统合规性

#### 使用 SLDS 实用程序类
对于现代实施，始终使用带有 `slds-var-` 前缀的 Salesforce Lightning Design System 实用程序类：

```html
<!-- Spacing -->
<div class="slds-var-m-around_medium slds-var-p-top_large">
    <div class="slds-var-m-bottom_small">Content</div>
</div>

<!-- Layout -->
<div class="slds-grid slds-wrap slds-gutters_small">
    <div class="slds-col slds-size_1-of-2 slds-medium-size_1-of-3">
        <!-- Content -->
    </div>
</div>

<!-- Typography -->
<h2 class="slds-text-heading_medium slds-var-m-bottom_small">Section Title</h2>
<p class="slds-text-body_regular">Description text</p>
```

#### SLDS 组件模式
```html
<!-- Card Layout -->
<article class="slds-card slds-var-m-around_medium">
    <header class="slds-card__header">
        <h2 class="slds-text-heading_small">Card Title</h2>
    </header>
    <div class="slds-card__body slds-card__body_inner">
        <!-- Card content -->
    </div>
    <footer class="slds-card__footer">
        <!-- Card actions -->
    </footer>
</article>

<!-- Form Layout -->
<div class="slds-form slds-form_stacked">
    <div class="slds-form-element">
        <lightning-input label="Field Label" value={fieldValue}></lightning-input>
    </div>
</div>
```

### 4. 避免自定义 CSS

#### 使用 SLDS 类
```html
<!-- Color and theming -->
<div class="slds-theme_success slds-text-color_inverse slds-var-p-around_small">
    Success message
</div>

<div class="slds-theme_error slds-text-color_inverse slds-var-p-around_small">
    Error message
</div>

<div class="slds-theme_warning slds-text-color_inverse slds-var-p-around_small">
    Warning message
</div>
```

#### 避免自定义 CSS（反模式）
```css
/* Don't create custom styles that override SLDS */
.custom-button {
    background-color: red;
    padding: 10px;
}

.my-special-layout {
    display: flex;
    justify-content: center;
}
```

#### 当需要自定义 CSS 时
如果您必须使用自定义 CSS，请遵循以下准则：
- 尽可能使用 CSS 自定义属性（设计标记）
- 为自定义类添加前缀以避免冲突
- 切勿覆盖 SLDS 基类

```css
/* Custom CSS example */
.my-component-special {
    border-radius: var(--lwc-borderRadiusMedium);
    box-shadow: var(--lwc-shadowButton);
}
```

### 5. 组件架构最佳实践

#### 反应性质
```javascript
import { LightningElement, track, api } from 'lwc';

export default class MyComponent extends LightningElement {
    // Use @api for public properties
    @api recordId;
    @api title;

    // Primitive properties (string, number, boolean) are automatically reactive
    // No decorator needed - reassignment triggers re-render
    simpleValue = 'initial';
    count = 0;

    // Computed properties
    get displayName() {
        return this.name ? `Hello, ${this.name}` : 'Hello, Guest';
    }

    // @track is NOT needed for simple property reassignment
    // This will trigger reactivity automatically:
    handleUpdate() {
        this.simpleValue = 'updated'; // Reactive without @track
        this.count++; // Reactive without @track
    }

    // @track IS needed when mutating nested properties without reassignment
    @track complexData = {
        user: {
            name: 'John',
            preferences: {
                theme: 'dark'
            }
        }
    };

    handleDeepUpdate() {
        // Requires @track because we're mutating a nested property
        this.complexData.user.preferences.theme = 'light';
    }

    // BETTER: Avoid @track by using immutable patterns
    regularData = {
        user: {
            name: 'John',
            preferences: {
                theme: 'dark'
            }
        }
    };

    handleImmutableUpdate() {
      // No @track needed - we're creating a new object reference
      this.regularData = {
        ...this.regularData,
        user: {
          ...this.regularData.user,
          preferences: {
            ...this.regularData.user.preferences,
            theme: 'light'
          }
        }
      };
    }

    // Arrays: @track is needed only for mutating methods
    @track items = ['a', 'b', 'c'];

    handleArrayMutation() {
      // Requires @track
      this.items.push('d');
      this.items[0] = 'z';
    }

    // BETTER: Use immutable array operations
    regularItems = ['a', 'b', 'c'];

    handleImmutableArray() {
      // No @track needed
      this.regularItems = [...this.regularItems, 'd'];
      this.regularItems = this.regularItems.map((item, idx) =>
        idx === 0 ? 'z' : item
      );
    }

    // Use @track only for complex objects/arrays when you mutate nested properties.
    // For example, updating complexObject.details.status without reassigning complexObject.
    @track complexObject = {
      details: {
        status: 'new'
      }
    };
}
```

#### 事件处理模式
```javascript
// Custom event dispatch
handleSave() {
    const saveEvent = new CustomEvent('save', {
        detail: {
            recordData: this.recordData,
            timestamp: new Date()
        }
    });
    this.dispatchEvent(saveEvent);
}

// Lightning component event handling
handleInputChange(event) {
    const fieldName = event.target.name;
    const fieldValue = event.target.value;

    // For lightning-input, lightning-combobox, etc.
    this[fieldName] = fieldValue;
}

handleRadioChange(event) {
    // For lightning-radio-group
    this.selectedValue = event.detail.value;
}

handleToggleChange(event) {
    // For lightning-input type="toggle"
    this.isToggled = event.detail.checked;
}
```

### 6. 数据处理和有线服务

#### 使用@wire进行数据访问
```javascript
import { getRecord } from 'lightning/uiRecordApi';
import { getObjectInfo } from 'lightning/uiObjectInfoApi';

const FIELDS = ['Account.Name', 'Account.Industry', 'Account.AnnualRevenue'];

export default class MyComponent extends LightningElement {
    @api recordId;

    @wire(getRecord, { recordId: '$recordId', fields: FIELDS })
    record;

    @wire(getObjectInfo, { objectApiName: 'Account' })
    objectInfo;

    get recordData() {
        return this.record.data ? this.record.data.fields : {};
    }
}
```

### 7. 错误处理和用户体验

#### 实施适当的误差边界
```javascript
import { ShowToastEvent } from 'lightning/platformShowToastEvent';

export default class MyComponent extends LightningElement {
    isLoading = false;
    error = null;

    async handleAsyncOperation() {
        this.isLoading = true;
        this.error = null;

        try {
            const result = await this.performOperation();
            this.showSuccessToast();
        } catch (error) {
            this.error = error;
            this.showErrorToast(error.body?.message || 'An error occurred');
        } finally {
            this.isLoading = false;
        }
    }

    performOperation() {
        // Developer-defined async operation
    }

    showSuccessToast() {
        const event = new ShowToastEvent({
            title: 'Success',
            message: 'Operation completed successfully',
            variant: 'success'
        });
        this.dispatchEvent(event);
    }

    showErrorToast(message) {
        const event = new ShowToastEvent({
            title: 'Error',
            message: message,
            variant: 'error',
            mode: 'sticky'
        });
        this.dispatchEvent(event);
    }
}
```

### 8. 性能优化

#### 条件渲染
优先使用 `lwc:if`、`lwc:elseif` 和 `lwc:else` 进行条件渲染 (API v58.0+)。旧版 `if:true` / `if:false` 仍受支持，但在新组件中应避免使用。

```html
<!-- Use template directives for conditional rendering -->
<template lwc:if={isLoading}>
    <lightning-spinner alternative-text="Loading..."></lightning-spinner>
</template>
<template lwc:elseif={error}>
    <div class="slds-theme_error slds-text-color_inverse slds-var-p-around_small">
        {error.message}
    </div>
</template>
<template lwc:else>
    <template for:each={items} for:item="item">
        <div key={item.id} class="slds-var-m-bottom_small">
            {item.name}
        </div>
    </template>
</template>
```

```html
<!-- Legacy approach (avoid in new components) -->
<template if:true={isLoading}>
    <lightning-spinner alternative-text="Loading..."></lightning-spinner>
</template>
<template if:true={error}>
    <div class="slds-theme_error slds-text-color_inverse slds-var-p-around_small">
        {error.message}
    </div>
</template>
<template if:false={isLoading}>
  <template if:false={error}>
    <template for:each={items} for:item="item">
        <div key={item.id} class="slds-var-m-bottom_small">
            {item.name}
        </div>
    </template>
  </template>
</template>
```

### 9. 辅助功能最佳实践

#### 使用正确的 ARIA 标签和语义 HTML
```html
<!-- Use semantic structure -->
<section aria-label="Product Selection">
    <h2 class="slds-text-heading_medium">Products</h2>

    <lightning-input
        type="search"
        label="Search Products"
        placeholder="Enter product name..."
        aria-describedby="search-help">
    </lightning-input>

    <div id="search-help" class="slds-assistive-text">
        Type to filter the product list
    </div>
</section>
```

## 要避免的常见反模式
- **直接 DOM 操作**：切勿使用 `document.querySelector()` 或类似的
- **jQuery 或外部库**：避免非 Lightning 兼容的库
- **内联样式**：使用 SLDS 类而不是 `style` 属性
- **全局 CSS**：所有样式的范围都应限于组件
- **硬编码值**：使用自定义标签、自定义元数据或常量
- **命令式 API 调用**：如果可能，优先使用 `@wire` 而不是命令式 `import` 调用
- **内存泄漏**：始终清理 `disconnectedCallback()` 中的事件侦听器
