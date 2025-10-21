---
description: "PRD文档到前端代码生成指导Prompt"
mode: "agent"
tools: ["edit", "search", "new", "changes", "fetch"]
---

# 🚀 PRD 文档到前端代码生成指导 Prompt

当用户提供 PRD 文档时,请按照以下指导原则和步骤,生成完整的、生产就绪的前端代码。

---

## 📋 任务理解

你将收到一份 PRD 文档(Product Requirements Document),需要将其转换为完整的前端实现代码,包括:

- 页面主组件
- 子组件(表单、详情等)
- API 接口封装
- 路由配置
- README 文档

---

## 🎯 代码生成原则

### 1. **严格遵循 HOS 框架规范**

- 使用 HosUI 组件库(hos-row, hos-col, hos-table, hos-form, hos-dialog 等)
- 遵循 HOS 前端开发规范和命名约定
- 使用`this.$api()`方法调用后端接口
- 表单验证使用 rules 规则
- 统一的错误处理和消息提示

### 2. **完整的功能实现**

- 列表查询(分页、搜索、筛选)
- 新增/编辑/删除操作
- 表单验证(前端实时验证)
- 加载状态和错误处理
- 响应式布局和用户体验优化

### 3. **代码质量标准**

- 清晰的注释和 JSDoc 文档
- 规范的命名(camelCase 变量,PascalCase 组件)
- 合理的代码组织和模块化
- 安全性考虑(XSS 防护、敏感数据处理)
- 性能优化(防抖、节流、虚拟滚动等)

---

## 📂 目录结构模板

```
views/
└── [module-name]/              # 模块名(kebab-case)
    ├── index.vue               # 列表主页面
    ├── components/             # 子组件目录
    │   ├── [Module]Form.vue    # 新增/编辑表单
    │   └── [Module]Detail.vue  # 详情组件(可选)
    └── README.md               # 模块说明文档

api/
└── [module-name].js            # API接口封装
```

---

## 🔧 代码生成步骤

### **Step 1: 分析 PRD 文档**

从 PRD 中提取以下信息:

1. **功能列表**: 所有需要实现的功能点
2. **数据模型**: 实体字段、类型、验证规则
3. **用户故事**: 理解用户操作流程
4. **UI/UX 设计**: 页面布局、交互细节
5. **API 接口**: 接口路径、请求方法、参数结构

### **Step 2: 生成 API 接口封装**

**文件**: `src/biz/api/[module-name].js`

**模板结构**:

```javascript
/**
 * [模块名称] API 接口封装
 * @module api/[module-name]
 */

/**
 * 分页查询列表
 * @param {Object} params - 查询参数
 * @param {number} params.current - 当前页码
 * @param {number} params.size - 每页大小
 * @param {string} [params.xxx] - 其他查询条件
 * @returns {Object} API配置对象
 */
export const selectPageList = (params) => ({
  url: "/[module-path]/selectPageList",
  method: "post",
  params,
});

/**
 * 新增记录
 * @param {Object} data - 记录数据
 * @returns {Object} API配置对象
 */
export const save = (data) => ({
  url: "/[module-path]/save",
  method: "post",
  data,
});

/**
 * 更新记录
 * @param {Object} data - 记录数据(包含id)
 * @returns {Object} API配置对象
 */
export const update = (data) => ({
  url: "/[module-path]/update",
  method: "post",
  data,
});

/**
 * 批量删除
 * @param {Array<string>} ids - ID数组
 * @returns {Object} API配置对象
 */
export const batchDeleteByIds = (ids) => ({
  url: "/[module-path]/batchDeleteByIds",
  method: "post",
  data: ids,
});

/**
 * 根据ID查询详情
 * @param {string} id - 记录ID
 * @returns {Object} API配置对象
 */
export const getDetailById = (id) => ({
  url: "/[module-path]/getDetailById",
  method: "get",
  params: { id },
});

// 根据PRD添加其他接口...
```

**关键点**:

- 使用 JSDoc 完整注释每个接口
- GET 请求使用`params`,POST 请求使用`data`
- 数组参数使用`data`传递到 request body
- 根据 PRD 的接口设计调整路径和参数

### **Step 3: 生成列表主页面**

**文件**: `src/biz/views/[module-name]/index.vue`

**模板结构**:

```vue
<template>
  <div class="[module-name]-management">
    <!-- 搜索区域 -->
    <hos-row :gutter="10" class="search-area">
      <hos-form ref="searchForm" :model="searchForm" label-width="100px">
        <!-- 根据PRD生成搜索字段 -->
        <hos-col :span="8">
          <hos-form-item label="[字段名]">
            <hos-input v-model="searchForm.[fieldName]" placeholder="请输入[字段名]" clearable />
          </hos-form-item>
        </hos-col>

        <!-- 操作按钮 -->
        <hos-col :span="8">
          <hos-form-item label=" ">
            <hos-button type="primary" @click="handleSearch">查询</hos-button>
            <hos-button @click="handleReset">重置</hos-button>
          </hos-form-item>
        </hos-col>
      </hos-form>
    </hos-row>

    <!-- 操作按钮区 -->
    <hos-row :gutter="10" class="button-area">
      <hos-col :span="24">
        <hos-button type="primary" icon="el-icon-plus" @click="handleAdd"> 新增 </hos-button>
      </hos-col>
    </hos-row>

    <!-- 表格区域 -->
    <hos-row :gutter="10">
      <hos-col :span="24">
        <hos-table v-loading="tableLoading" :data="tableData" :height="tableHeight" border highlight-current-row style="width: 100%">
          <hos-table-column type="index" label="序号" width="60" align="center" />

          <!-- 根据PRD生成表格列 -->
          <hos-table-column prop="[fieldName]" label="[字段标签]" min-width="120" show-overflow-tooltip />

          <!-- 操作列 -->
          <hos-table-column label="操作" width="200" fixed="right" align="center">
            <template slot-scope="{ row }">
              <hos-button type="text" size="small" @click="handleEdit(row)"> 编辑 </hos-button>
              <hos-button type="text" size="small" @click="handleDelete(row)"> 删除 </hos-button>
              <!-- 根据PRD添加其他操作按钮 -->
            </template>
          </hos-table-column>
        </hos-table>
      </hos-col>
    </hos-row>

    <!-- 分页组件 -->
    <hos-row :gutter="10" class="pagination-area">
      <hos-col :span="24">
        <hos-pagination :current-page="pagination.current" :page-sizes="[10, 20, 30, 50]" :page-size="pagination.size" :total="pagination.total" layout="total, sizes, prev, pager, next, jumper" @size-change="handleSizeChange" @current-change="handleCurrentChange" />
      </hos-col>
    </hos-row>

    <!-- 新增/编辑对话框 -->
    <module-form v-if="formDialogVisible" :visible.sync="formDialogVisible" :form-data="currentFormData" :is-edit="isEditMode" @success="handleFormSuccess" />
  </div>
</template>

<script>
import ModuleForm from "./components/ModuleForm.vue";

export default {
  name: "[ModuleName]Management",
  components: {
    ModuleForm,
  },
  data() {
    return {
      // 搜索表单
      searchForm: {
        // 根据PRD生成搜索字段
      },
      // 表格数据
      tableData: [],
      tableLoading: false,
      tableHeight: window.innerHeight - 250,
      // 分页
      pagination: {
        current: 1,
        size: 10,
        total: 0,
      },
      // 对话框
      formDialogVisible: false,
      isEditMode: false,
      currentFormData: null,
    };
  },
  mounted() {
    this.loadTableData();
    window.addEventListener("resize", this.handleResize);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    /**
     * 加载表格数据
     */
    async loadTableData() {
      this.tableLoading = true;
      try {
        const params = {
          current: this.pagination.current,
          size: this.pagination.size,
          ...this.searchForm,
        };
        const res = await this.$api("[module].selectPageList", params);

        if (res.code == 200 && res.data) {
          this.tableData = res.data.records || [];
          this.pagination.total = res.data.total || 0;
          this.pagination.current = res.data.current || 1;
          this.pagination.size = res.data.size || 10;
        } else {
          this.$message.error(res.msg || "查询失败");
        }
      } catch (error) {
        console.error("查询列表失败:", error);
        this.$message.error("查询失败,请稍后重试");
      } finally {
        this.tableLoading = false;
      }
    },

    /**
     * 搜索
     */
    handleSearch() {
      this.pagination.current = 1;
      this.loadTableData();
    },

    /**
     * 重置搜索
     */
    handleReset() {
      this.searchForm = {}; // 根据实际字段重置
      this.handleSearch();
    },

    /**
     * 新增
     */
    handleAdd() {
      this.isEditMode = false;
      this.currentFormData = null;
      this.formDialogVisible = true;
    },

    /**
     * 编辑
     */
    handleEdit(row) {
      this.isEditMode = true;
      this.currentFormData = { ...row };
      this.formDialogVisible = true;
    },

    /**
     * 删除
     */
    async handleDelete(row) {
      try {
        const confirm = await this.$confirm(`确定要删除"${row.name}"吗?`, "提示", { type: "warning" }).catch(() => false);

        if (!confirm) return;

        const res = await this.$api("[module].batchDeleteByIds", [row.id]);
        if (res.code === 200) {
          this.$message.success("删除成功");
          this.loadTableData();
        } else {
          this.$message.error(res.msg || "删除失败");
        }
      } catch (error) {
        console.error("删除失败:", error);
        this.$message.error("删除失败,请稍后重试");
      }
    },

    /**
     * 表单提交成功
     */
    handleFormSuccess() {
      this.formDialogVisible = false;
      this.loadTableData();
    },

    /**
     * 分页大小变化
     */
    handleSizeChange(size) {
      this.pagination.size = size;
      this.pagination.current = 1;
      this.loadTableData();
    },

    /**
     * 页码变化
     */
    handleCurrentChange(current) {
      this.pagination.current = current;
      this.loadTableData();
    },

    /**
     * 窗口大小变化
     */
    handleResize() {
      this.tableHeight = window.innerHeight - 250;
    },
  },
};
</script>

<style scoped lang="scss">
.[module-name]-management {
  padding: 20px;
  background: #fff;
  min-height: calc(100vh - 100px);

  .search-area {
    margin-bottom: 10px;
  }

  .button-area {
    margin-bottom: 15px;
  }

  .pagination-area {
    margin-top: 15px;
    text-align: right;
  }
}
</style>
```

### **Step 4: 生成表单组件**

**文件**: `src/biz/views/[module-name]/components/[Module]Form.vue`

**模板结构**:

```vue
<template>
  <hos-dialog :title="isEdit ? '编辑[模块名]' : '新增[模块名]'" :visible.sync="dialogVisible" :close-on-click-modal="false" width="600px" @close="handleClose">
    <hos-form ref="form" :model="form" :rules="rules" label-width="120px">
      <!-- 根据PRD生成表单字段 -->
      <hos-form-item label="[字段名]" prop="[fieldName]">
        <hos-input v-model="form.[fieldName]" placeholder="请输入[字段名]" maxlength="64" show-word-limit />
      </hos-form-item>

      <!-- 下拉选择示例 -->
      <hos-form-item label="[字段名]" prop="[fieldName]">
        <hos-select v-model="form.[fieldName]" placeholder="请选择[字段名]">
          <hos-option label="选项1" value="VALUE1" />
          <hos-option label="选项2" value="VALUE2" />
        </hos-select>
      </hos-form-item>

      <!-- 日期选择示例 -->
      <hos-form-item label="[字段名]" prop="[fieldName]">
        <hos-date-picker v-model="form.[fieldName]" type="date" placeholder="请选择日期" value-format="yyyy-MM-dd" style="width: 100%;" />
      </hos-form-item>

      <!-- 开关示例 -->
      <hos-form-item label="[字段名]">
        <hos-switch v-model="form.[fieldName]" />
      </hos-form-item>
    </hos-form>

    <div slot="footer" class="dialog-footer">
      <hos-button @click="handleClose">取消</hos-button>
      <hos-button type="primary" @click="handleSubmit" :loading="submitting"> 保存 </hos-button>
    </div>
  </hos-dialog>
</template>

<script>
export default {
  name: "[Module]Form",
  props: {
    visible: {
      type: Boolean,
      required: true,
    },
    formData: {
      type: Object,
      default: null,
    },
    isEdit: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      dialogVisible: this.visible,
      submitting: false,
      form: {
        // 根据PRD生成表单字段
        id: null,
        // ... 其他字段
      },
      rules: {
        // 根据PRD生成验证规则
        [fieldName]: [
          { required: true, message: "请输入[字段名]", trigger: "blur" },
          { min: 2, max: 64, message: "长度在 2 到 64 个字符", trigger: "blur" },
          { pattern: /^[a-zA-Z0-9_-]+$/, message: "仅支持字母、数字、下划线和短横线", trigger: "blur" },
        ],
      },
    };
  },
  watch: {
    visible(val) {
      this.dialogVisible = val;
    },
    dialogVisible(val) {
      this.$emit("update:visible", val);
    },
    formData: {
      handler(val) {
        if (val) {
          this.form = { ...val };
        } else {
          this.resetForm();
        }
      },
      immediate: true,
      deep: true,
    },
  },
  methods: {
    /**
     * 提交表单
     */
    async handleSubmit() {
      try {
        await this.$refs.form.validate();
      } catch (error) {
        this.$message.warning("请检查表单填写是否正确");
        return;
      }

      this.submitting = true;
      try {
        const apiMethod = this.isEdit ? "[module].update" : "[module].save";
        const res = await this.$api(apiMethod, this.form);

        if (res.code === 200) {
          this.$message.success(this.isEdit ? "修改成功" : "新增成功");
          this.$emit("success");
        } else {
          this.$message.error(res.msg || "保存失败");
        }
      } catch (error) {
        console.error("保存失败:", error);
        this.$message.error("保存失败,请稍后重试");
      } finally {
        this.submitting = false;
      }
    },

    /**
     * 关闭对话框
     */
    handleClose() {
      this.dialogVisible = false;
      this.resetForm();
    },

    /**
     * 重置表单
     */
    resetForm() {
      this.$refs.form && this.$refs.form.resetFields();
      this.form = {
        // 重置为初始值
      };
    },
  },
};
</script>

<style scoped lang="scss">
.dialog-footer {
  text-align: right;
}
</style>
```

### **Step 5: 生成详情组件(可选)**

**文件**: `src/biz/views/[module-name]/components/[Module]Detail.vue`

**模板结构**: 参考 ConnectionDetail.vue 的实现

### **Step 6: 生成 README 文档**

**文件**: `src/biz/views/[module-name]/README.md`

**模板内容**:

```markdown
# [模块名称]模块

## 目录结构

## 功能说明

## API 接口文件

## 路由配置

## 使用说明

## 注意事项

## 后续扩展

## 参考文档
```

---

## 🎨 UI/UX 实现要点

### 1. **表单验证规则映射**

根据 PRD 中的字段要求生成验证规则:

- 必填 → `{ required: true, message: '...', trigger: 'blur' }`
- 长度限制 → `{ min: X, max: Y, message: '...', trigger: 'blur' }`
- 格式限制 → `{ pattern: /.../, message: '...', trigger: 'blur' }`
- 唯一性 → 自定义异步 validator

### 2. **状态管理**

- 列表加载状态: `tableLoading`
- 表单提交状态: `submitting`
- 测试连接状态: `testing`
- 使用 v-loading 指令显示加载动画

### 3. **错误处理**

```javascript
try {
  const res = await this.$api("...");
  if (res.code === 200) {
    // 成功处理
  } else {
    this.$message.error(res.msg || "操作失败");
  }
} catch (error) {
  console.error("操作失败:", error);
  this.$message.error("操作失败,请稍后重试");
}
```

### 4. **安全性考虑**

- 密码字段使用`type="password"`
- 敏感数据显示使用掩码(`******`)
- XSS 防护:默认文本渲染,避免 v-html
- CSRF 防护:依赖后端 token 机制

---

## ✅ 质量检查清单

在生成代码后,确保:

- [ ] 所有 PRD 功能点已实现
- [ ] API 接口路径和参数与后端一致
- [ ] 表单验证规则完整
- [ ] 错误处理和加载状态完整
- [ ] 代码注释清晰完整
- [ ] 命名规范符合 HOS 框架
- [ ] 响应式布局适配
- [ ] 安全性考虑到位
- [ ] 用户体验友好(提示、反馈)
- [ ] README 文档完整

---

## 📝 输出格式

生成代码时,请按以下顺序输出:

1. **API 接口文件** (`src/biz/api/[module-name].js`)
2. **列表主页面** (`src/biz/views/[module-name]/index.vue`)
3. **表单组件** (`src/biz/views/[module-name]/components/[Module]Form.vue`)
4. **详情组件**(如有) (`src/biz/views/[module-name]/components/[Module]Detail.vue`)
5. **README 文档** (`src/biz/views/[module-name]/README.md`)
6. **路由配置代码片段**(添加到 index.js)

每个文件使用代码块分隔,并注明文件路径。

---

## 🚀 开始生成

现在,请阅读用户提供的 PRD 文档,按照以上指导原则和模板,生成完整的前端代码实现。

**记住**:

- 严格遵循 HOS 框架规范
- 代码质量优先于速度
- 用户体验和安全性不可妥协
- 提供完整的注释和文档

开始吧! 🎉

---
