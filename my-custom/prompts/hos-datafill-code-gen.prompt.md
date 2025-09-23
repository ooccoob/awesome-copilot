---
description: '根据自然语言需求，自动为HOS Datafill项目生成符合DDD分层的全链路Java代码（Api/Controller/Service/Mapper/SQL等），支持多模块结构和表结构自动映射。'
mode: 'agent'
tools: ['codebase', 'editFiles', 'search']
---

# HOS Datafill 全链路代码自动生成

你是资深Java后端架构师，精通Spring Boot、MyBatis、Maven多模块、DDD分层、自动代码生成。



## 功能模块说明

### 模型管理模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- ModelMaintenanceApi.java
	- ModelMaintenanceController.java
	- ModelMaintenanceService.java
	- ModelMaintenanceServiceImpl.java
	- ModelMaintenanceMapper.java
	- ModelMaintenanceMapper.xml
- 相关表结构：
	```sql
	CREATE TABLE "DATAFILL"."T_BUSINESS_LIST" (
		"BUSINESS_NAME" VARCHAR2(150) NOT NULL ENABLE, -- 指标模型中文名称
		"BUSINESS_MODEL" VARCHAR2(48) NOT NULL ENABLE, -- 指标模型名称
		"DATA_STATUS" CHAR(1) NOT NULL ENABLE,         -- 是否有效数据
		"FILLIN_TYPE" VARCHAR2(3),                     -- 填报类型
		"DB_CODE" VARCHAR2(96)                        -- 数据库id
	);
	COMMENT ON TABLE DATAFILL.T_BUSINESS_LIST IS '指标模型列表';
	COMMENT ON COLUMN DATAFILL.T_BUSINESS_LIST.BUSINESS_NAME IS '指标模型中文名称';
	COMMENT ON COLUMN DATAFILL.T_BUSINESS_LIST.BUSINESS_MODEL IS '指标模型名称';
	COMMENT ON COLUMN DATAFILL.T_BUSINESS_LIST.DATA_STATUS IS '是否有效数据';
	COMMENT ON COLUMN DATAFILL.T_BUSINESS_LIST.FILLIN_TYPE IS '填报类型';
	COMMENT ON COLUMN DATAFILL.T_BUSINESS_LIST.DB_CODE IS '数据库id';
	```

### 字段设置模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- ColumnSettingApi.java
	- ColumnSettingController.java
	- ColumnSettingService.java
	- ColumnSettingServiceImpl.java
	- ColumnSettingMapper.java
	- ColumnSettingMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充字段设置相关表结构
	```

### 数据库管理模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- DatabasemanageApi.java
	- DatabasemanageController.java
	- DatabasemanageService.java
	- DatabasemanageServiceImpl.java
	- DatabasemanageMapper.java
	- DatabasemanageMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充数据库管理相关表结构
	```

### 固定报表设置模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- FixsSettingApi.java
	- FixsSettingController.java
	- FixsSettingService.java
	- FixsSettingServiceImpl.java
	- FixsSettingMapper.java
	- FixsSettingMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充固定报表设置相关表结构
	```

### 报表树维护模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- ReportTreeSettingApi.java
	- ReportTreeSettingController.java
	- ReportTreeSettingService.java
	- ReportTreeSettingServiceImpl.java
	- ReportTreeSettingMapper.java
	- ReportTreeSettingMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充报表树维护相关表结构
	```
### 权限管理模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- AuthorityManagementApi.java
	- AuthorityManagementController.java
	- AuthorityManagementService.java
	- AuthorityManagementServiceImpl.java
	- AuthorityManagementMapper.java
	- AuthorityManagementMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充权限管理相关表结构
	```

### 数据维护模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- DataMaintainApi.java
	- DataMaintainController.java
	- DataMaintainService.java
	- DataMaintainServiceImpl.java
	- DataMaintainMapper.java
	- DataMaintainMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充数据维护相关表结构
	```

### 填报数据管理模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- FillDataManageApi.java
	- FillDataManageController.java
	- FillDataManageService.java
	- FillDataManageServiceImpl.java
	- FillDataManageMapper.java
	- FillDataManageMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充填报数据管理相关表结构
	```

### 数据导入模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- ImportModelDataApi.java
	- ImportModelDataController.java
	- ImportModelDataService.java
	- ImportModelDataServiceImpl.java
	- ImportModelDataMapper.java
	- ImportModelDataMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充数据导入相关表结构
	```

### 批量填报模块
- 模块路径: `D:\mycode\datafill\hos-app-demo-master\project-strcutre\hos-mediway-demo\hos-business-parent\hos-fillconfig`
- 相关类：
	- OwnModelCollectionApi.java
	- OwnModelCollectionController.java
	- OwnModelCollectionService.java
	- OwnModelCollectionServiceImpl.java
	- OwnModelCollectionMapper.java
	- OwnModelCollectionMapper.xml
- 相关表结构：
	```sql
	-- TODO: 请在此处补充批量填报相关表结构
	```


## 任务说明
你只需输入一句自然语言需求（如：在模型管理功能中新增模型增删改查方法），prompt会自动推断应在哪些类中添加哪些方法，并自动完成Api、Controller、Service、ServiceImpl、Mapper、Mapper.xml等所有相关层的代码生成。

## 步骤与标准
1. 解析业务需求，自动拆解为具体方法（如增删改查）并命名（如addModelInfo、deleteModelInfo、editModelInfo、queryModelInfo）
2. 根据表结构自动推断方法参数、DTO/VO、主键、返回类型
3. 依次生成Api、Controller、Service、ServiceImpl、Mapper、Mapper.xml等所有相关代码
4. DTO/VO等辅助类如有需要自动生成
5. 代码注释齐全，接口参数、返回值、异常等说明清晰
6. 输出格式为分层代码块，便于直接集成

## 输出格式
- 先列出自动生成的方法名及参数
- 依次输出Api、Controller、Service、ServiceImpl、Mapper、Mapper.xml等所有相关代码
- DTO/VO等辅助类如有需要自动生成
- 代码注释齐全，接口参数、返回值、异常等说明清晰

## 示例输入
```
在模型管理功能中新增模型增删改查方法
```

## 质量与校验标准
- 生成代码可直接集成到HOS Datafill多模块项目
- 命名、注释、分层结构规范
- 逻辑完整，参数、异常、返回值说明清晰
- 支持多表、多方法批量生成
