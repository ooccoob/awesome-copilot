---
title: HOS 后端代码生成 Prompt
version: 1.0
date_created: 2025-10-20
last_updated: 2025-10-20
owner: hos-datafill-backend团队
tags: [code-generation, prompt, template, specification]
---

# HOS 后端代码生成 Prompt

## 使用说明

本 Prompt 用于指导 GitHub Copilot 根据规范文档 (`spec-*.md`) 自动生成符合 HOS 框架规范的后端代码。

**使用方式**:

```
请按照 hos-backend-code-generate.prompt.md 的要求,根据 spec-xx.md 在 XX 类中生成对应的代码。
```

**示例**:

```
请按照 hos-backend-code-generate.prompt.md 的要求,根据 spec-datafill-model-management.md 在 ModelManagement 类中生成对应的代码。
```

---

## 代码生成规则

### 1. 包路径规范 (参考 DbConnectionManagement 模块)

根据规范文档中的 **业务类名** (例如: `DbConnectionManagement`, `ModelManagement`, `FieldSetting` 等),严格按照以下包路径结构生成代码:

#### 1.1 API 层 (hos-app-datafill-api)

**包路径**: `com.mediway.hos.datafill.api`

**文件名**: `{业务类名}Api.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-api/src/main/java/com/mediway/hos/datafill/api/DbConnectionManagementApi.java`

**职责**:

- 定义 Feign 客户端接口
- 声明所有对外暴露的 API 方法签名
- 添加 `@FeignClient` 注解,指定服务名与请求路径前缀
- 添加 `@ApiOperation` 注解描述接口用途
- 使用 `@RequestBody`, `@RequestParam`, `@GetMapping`, `@PostMapping` 等注解
- 统一返回 `BaseResponse<T>` 格式

**代码模板**:

```java
package com.mediway.hos.datafill.api;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.mediway.hos.base.model.BaseResponse;
import com.mediway.hos.datafill.model.entity.{业务类名};
import com.mediway.hos.datafill.model.vo.{业务类名}VO;
import io.swagger.annotations.ApiOperation;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

/**
 * <p>
 * {模块描述} API接口
 * </p>
 *
 * @author {作者名}
 * @date {日期}
 */
@FeignClient(value = "hos-datafill-server", path = "/datafill/{路径前缀}")
public interface {业务类名}Api {

    /**
     * 分页查询列表
     */
    @ApiOperation("分页查询列表")
    @PostMapping("/selectPageList")
    BaseResponse<IPage<{业务类名}VO>> selectPageList(
            @RequestParam(defaultValue = "1") Long current,
            @RequestParam(defaultValue = "10") Long size,
            // ... 其他查询参数
    );

    /**
     * 根据ID查询详情
     */
    @ApiOperation("根据ID查询详情")
    @GetMapping("/getDetailById")
    BaseResponse<{业务类名}VO> getDetailById(@RequestParam String id);

    /**
     * 新增
     */
    @ApiOperation("新增")
    @PostMapping("/save")
    BaseResponse<Boolean> save(@RequestBody {业务类名} entity, HttpServletRequest request);

    /**
     * 更新
     */
    @ApiOperation("更新")
    @PostMapping("/update")
    BaseResponse<Boolean> update(@RequestBody {业务类名} entity, HttpServletRequest request);

    /**
     * 批量删除
     */
    @ApiOperation("批量删除")
    @PostMapping("/batchDeleteByIds")
    BaseResponse<Boolean> batchDeleteByIds(@RequestBody List<String> ids);
}
```

---

#### 1.2 Controller 层 (hos-app-datafill-controller)

**包路径**: `com.mediway.hos.datafill.controller`

**文件名**: `{业务类名}Controller.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-controller/src/main/java/com/mediway/hos/datafill/controller/DbConnectionManagementController.java`

**职责**:

- 实现 Api 接口
- 处理 HTTP 请求,调用 Service 层业务逻辑
- 添加 `@RestController` 和 `@RequestMapping` 注解
- 添加 `@Api` 和 `@ApiOperation` Swagger 注解
- 统一异常处理与日志记录
- 返回统一 `BaseResponse<T>` 格式

**代码模板**:

```java
package com.mediway.hos.datafill.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.mediway.hos.base.model.BaseResponse;
import com.mediway.hos.datafill.api.{业务类名}Api;
import com.mediway.hos.datafill.model.entity.{业务类名};
import com.mediway.hos.datafill.model.vo.{业务类名}VO;
import com.mediway.hos.datafill.service.{业务类名}Service;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

/**
 * <p>
 * {模块描述} 前端控制器
 * </p>
 *
 * @author {作者名}
 * @date {日期}
 */
@Api(tags = "{模块名称}")
@RestController
@RequestMapping("/datafill/{路径前缀}")
public class {业务类名}Controller implements {业务类名}Api {

    private static final Logger log = LoggerFactory.getLogger({业务类名}Controller.class);

    @Autowired
    private {业务类名}Service {业务实例名}Service;

    @Override
    @ApiOperation("分页查询列表")
    @PostMapping("/selectPageList")
    public BaseResponse<IPage<{业务类名}VO>> selectPageList(
            @RequestParam(defaultValue = "1") Long current,
            @RequestParam(defaultValue = "10") Long size,
            // ... 其他参数
    ) {
        try {
            log.info("分页查询 - current={}, size={}", current, size);
            IPage<{业务类名}VO> page = {业务实例名}Service.selectPageList(current, size, ...);
            return BaseResponse.success(page);
        } catch (Exception e) {
            log.error("分页查询失败", e);
            return BaseResponse.error("查询失败: " + e.getMessage());
        }
    }

    @Override
    @ApiOperation("根据ID查询详情")
    @GetMapping("/getDetailById")
    public BaseResponse<{业务类名}VO> getDetailById(@RequestParam String id) {
        try {
            log.info("查询详情 - id={}", id);
            {业务类名}VO vo = {业务实例名}Service.getDetailById(id);
            if (vo == null) {
                return BaseResponse.error("记录不存在");
            }
            return BaseResponse.success(vo);
        } catch (Exception e) {
            log.error("查询详情失败 - id={}", id, e);
            return BaseResponse.error("查询失败: " + e.getMessage());
        }
    }

    @Override
    @ApiOperation("新增")
    @PostMapping("/save")
    public BaseResponse<Boolean> save(@RequestBody {业务类名} entity, HttpServletRequest request) {
        try {
            log.info("新增 - entity={}", entity);
            boolean success = {业务实例名}Service.save{业务类名}(entity);
            return success ? BaseResponse.success(true) : BaseResponse.error("新增失败");
        } catch (Exception e) {
            log.error("新增失败", e);
            return BaseResponse.error("新增失败: " + e.getMessage());
        }
    }

    @Override
    @ApiOperation("更新")
    @PostMapping("/update")
    public BaseResponse<Boolean> update(@RequestBody {业务类名} entity, HttpServletRequest request) {
        try {
            log.info("更新 - entity={}", entity);
            boolean success = {业务实例名}Service.update{业务类名}(entity);
            return success ? BaseResponse.success(true) : BaseResponse.error("更新失败");
        } catch (Exception e) {
            log.error("更新失败", e);
            return BaseResponse.error("更新失败: " + e.getMessage());
        }
    }

    @Override
    @ApiOperation("批量删除")
    @PostMapping("/batchDeleteByIds")
    public BaseResponse<Boolean> batchDeleteByIds(@RequestBody List<String> ids) {
        try {
            log.info("批量删除 - ids={}", ids);
            if (ids == null || ids.isEmpty()) {
                return BaseResponse.error("删除ID列表不能为空");
            }
            boolean success = {业务实例名}Service.batchDeleteByIds(ids);
            return success ? BaseResponse.success(true) : BaseResponse.error("删除失败");
        } catch (Exception e) {
            log.error("批量删除失败 - ids={}", ids, e);
            return BaseResponse.error("删除失败: " + e.getMessage());
        }
    }
}
```

---

#### 1.3 Model 层 (hos-app-datafill-model)

##### 1.3.1 Entity 实体类

**包路径**: `com.mediway.hos.datafill.model.entity`

**文件名**: `{业务类名}.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-model/src/main/java/com/mediway/hos/datafill/model/entity/DbConnectionManagement.java`

**职责**:

- 映射数据库表结构
- 继承 `BaseEntity` (包含 id, createTime, updateTime 等审计字段)
- 使用 MyBatis-Plus 注解: `@TableName`, `@TableField`, `@TableLogic`
- 添加 Swagger 注解: `@ApiModel`, `@ApiModelProperty`
- 使用 Lombok: `@Data`, `@EqualsAndHashCode(callSuper = true)`

**代码模板**:

```java
package com.mediway.hos.datafill.model.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableLogic;
import com.mediway.hos.database.model.BaseEntity;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;

/**
 * <p>
 * {表描述}
 * </p>
 *
 * @author {作者名}
 * @date {日期}
 */
@Data
@EqualsAndHashCode(callSuper = true)
@ApiModel(value="{业务类名}对象", description="{表描述}")
@TableName(value = "{表名}", autoResultMap = true)
public class {业务类名} extends BaseEntity {
    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "{字段描述}")
    @TableField("{字段名}")
    private String fieldName;

    @ApiModelProperty(value = "是否启用:0-禁用,1-启用")
    @TableField("is_enabled")
    private Integer isEnabled;

    @ApiModelProperty(value = "是否删除:0-否,1-是")
    @TableField("is_deleted")
    @TableLogic(value = "0", delval = "1")
    private Integer isDeleted;

    @ApiModelProperty(value = "创建人")
    @TableField("create_by")
    private String createBy;

    @ApiModelProperty(value = "更新人")
    @TableField("update_by")
    private String updateBy;

    // Backwards-compatible accessors for isEnabled (compatible with Lombok)
    public Integer getEnabled() {
        return this.isEnabled;
    }

    public void setEnabled(Integer enabled) {
        this.isEnabled = enabled;
    }

    public Integer getIsEnabled() {
        return this.isEnabled;
    }

    public void setIsEnabled(Integer isEnabled) {
        this.isEnabled = isEnabled;
    }

    // isDeleted accessors
    public Integer getIsDeleted() {
        return this.isDeleted;
    }

    public void setIsDeleted(Integer isDeleted) {
        this.isDeleted = isDeleted;
    }
}
```

**注意事项**:

- **必须继承 `BaseEntity`** (包含 id, createTime, updateTime)
- **布尔字段命名**: 使用 `isXxx` 格式 (如 `isEnabled`, `isDeleted`)
- **软删除**: 使用 `@TableLogic` 注解标记 `isDeleted` 字段
- **Lombok 兼容性**: 为 `isEnabled` 等字段提供 `getEnabled()/setEnabled()` 和 `getIsEnabled()/setIsEnabled()` 双重访问器

##### 1.3.2 VO 视图对象

**包路径**: `com.mediway.hos.datafill.model.vo`

**文件名**: `{业务类名}VO.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-model/src/main/java/com/mediway/hos/datafill/model/vo/DbConnectionManagementVO.java`

**职责**:

- 继承 Entity,用于接口返回
- 添加前端需要的扩展字段 (如状态文本、关联对象名称等)
- 使用 Lombok: `@Data`, `@EqualsAndHashCode(callSuper = true)`

**代码模板**:

```java
package com.mediway.hos.datafill.model.vo;

import com.mediway.hos.datafill.model.entity.{业务类名};
import lombok.Data;
import lombok.EqualsAndHashCode;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * {模块描述} 视图对象
 *
 * @author {作者名}
 * @date {日期}
 */
@Data
@EqualsAndHashCode(callSuper = true)
@ApiModel(value="{业务类名}VO对象", description="{模块描述} 视图对象")
public class {业务类名}VO extends {业务类名} {

    @ApiModelProperty(value = "状态文本")
    private String statusText;

    @ApiModelProperty(value = "创建人名称")
    private String createByName;

    @ApiModelProperty(value = "修改人名称")
    private String updateByName;

    // 其他扩展字段...
}
```

---

#### 1.4 Service 层 (hos-app-datafill-service)

##### 1.4.1 Service 接口

**包路径**: `com.mediway.hos.datafill.service`

**文件名**: `{业务类名}Service.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-service/src/main/java/com/mediway/hos/datafill/service/DbConnectionManagementService.java`

**职责**:

- 继承 `BaseService<Entity>`
- 声明业务方法签名
- 添加完整的 Javadoc 注释

**代码模板**:

```java
package com.mediway.hos.datafill.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.mediway.hos.database.service.BaseService;
import com.mediway.hos.datafill.model.entity.{业务类名};
import com.mediway.hos.datafill.model.vo.{业务类名}VO;

import java.util.List;

/**
 * <p>
 * {模块描述} 服务接口
 * </p>
 *
 * @author {作者名}
 * @date {日期}
 */
public interface {业务类名}Service extends BaseService<{业务类名}> {

    /**
     * 分页查询列表
     *
     * @param current 当前页
     * @param size 每页大小
     * @param ... 查询条件
     * @return 分页列表
     */
    IPage<{业务类名}VO> selectPageList(Long current, Long size, ...);

    /**
     * 根据ID查询详情
     *
     * @param id 主键ID
     * @return 详情VO
     */
    {业务类名}VO getDetailById(String id);

    /**
     * 新增
     *
     * @param entity 实体对象
     * @return 保存结果
     */
    boolean save{业务类名}({业务类名} entity);

    /**
     * 更新
     *
     * @param entity 实体对象
     * @return 更新结果
     */
    boolean update{业务类名}({业务类名} entity);

    /**
     * 批量删除(逻辑删除)
     *
     * @param ids ID列表
     * @return 删除结果
     */
    boolean batchDeleteByIds(List<String> ids);
}
```

##### 1.4.2 Service 实现类

**包路径**: `com.mediway.hos.datafill.service.impl`

**文件名**: `{业务类名}ServiceImpl.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-service/src/main/java/com/mediway/hos/datafill/service/impl/DbConnectionManagementServiceImpl.java`

**职责**:

- 继承 `BaseServiceImpl<Mapper, Entity>`
- 实现 Service 接口
- 实现具体业务逻辑
- 添加 `@Service` 注解
- 添加 `@Transactional` 注解标记事务方法
- 使用 SLF4J 记录日志

**代码模板**:

```java
package com.mediway.hos.datafill.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.mediway.hos.database.service.impl.BaseServiceImpl;
import com.mediway.hos.datafill.mapper.{业务类名}Mapper;
import com.mediway.hos.datafill.model.entity.{业务类名};
import com.mediway.hos.datafill.model.vo.{业务类名}VO;
import com.mediway.hos.datafill.service.{业务类名}Service;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

/**
 * <p>
 * {模块描述} 服务实现类
 * </p>
 *
 * @author {作者名}
 * @date {日期}
 */
@Service
public class {业务类名}ServiceImpl extends BaseServiceImpl<{业务类名}Mapper, {业务类名}>
        implements {业务类名}Service {

    private static final Logger log = LoggerFactory.getLogger({业务类名}ServiceImpl.class);

    @Autowired
    private {业务类名}Mapper {业务实例名}Mapper;

    @Override
    public IPage<{业务类名}VO> selectPageList(Long current, Long size, ...) {
        Page<{业务类名}> page = new Page<>(current, size);
        QueryWrapper<{业务类名}> wrapper = new QueryWrapper<>();

        // 构建查询条件
        // if (StringUtils.isNotBlank(name)) {
        //     wrapper.like("name", name);
        // }

        IPage<{业务类名}> result = page(page, wrapper);

        // 转换为 VO
        IPage<{业务类名}VO> voPage = result.convert(entity -> {
            {业务类名}VO vo = new {业务类名}VO();
            BeanUtils.copyProperties(entity, vo);
            // 填充扩展字段
            return vo;
        });

        return voPage;
    }

    @Override
    public {业务类名}VO getDetailById(String id) {
        if (StringUtils.isBlank(id)) {
            throw new IllegalArgumentException("ID不能为空");
        }

        {业务类名} entity = getById(id);
        if (entity == null) {
            return null;
        }

        {业务类名}VO vo = new {业务类名}VO();
        BeanUtils.copyProperties(entity, vo);
        // 填充扩展字段

        return vo;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public boolean save{业务类名}({业务类名} entity) {
        // 参数校验
        validateEntity(entity);

        // 业务逻辑
        // ...

        return save(entity);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public boolean update{业务类名}({业务类名} entity) {
        if (StringUtils.isBlank(entity.getId())) {
            throw new IllegalArgumentException("ID不能为空");
        }

        // 参数校验
        validateEntity(entity);

        // 业务逻辑
        // ...

        return updateById(entity);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public boolean batchDeleteByIds(List<String> ids) {
        if (ids == null || ids.isEmpty()) {
            throw new IllegalArgumentException("删除ID列表不能为空");
        }

        // 关联检查 (如需要)
        // ...

        return removeByIds(ids);
    }

    /**
     * 校验实体必填字段
     */
    private void validateEntity({业务类名} entity) {
        if (entity == null) {
            throw new IllegalArgumentException("实体对象不能为空");
        }
        // 具体校验逻辑
        // ...
    }
}
```

---

#### 1.5 Mapper 层 (hos-app-datafill-service)

**包路径**: `com.mediway.hos.datafill.mapper`

**文件名**: `{业务类名}Mapper.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-service/src/main/java/com/mediway/hos/datafill/mapper/DbConnectionManagementMapper.java`

**职责**:

- 继承 `BaseMapper<Entity>`
- 声明自定义 SQL 方法
- 添加 `@Mapper` 注解
- 参数使用 `@Param` 注解

**代码模板**:

```java
package com.mediway.hos.datafill.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mediway.hos.datafill.model.entity.{业务类名};
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import java.util.List;

/**
 * <p>
 * {模块描述} Mapper 接口
 * </p>
 *
 * @author {作者名}
 * @date {日期}
 */
@Mapper
public interface {业务类名}Mapper extends BaseMapper<{业务类名}> {

    /**
     * 自定义查询方法示例
     *
     * @param param1 参数1
     * @param param2 参数2
     * @return 查询结果
     */
    List<{业务类名}> customQuery(@Param("param1") String param1, @Param("param2") String param2);
}
```

**Mapper XML** (如需要):

**文件路径**: `hos-app-datafill/hos-app-datafill-service/src/main/resources/{模块名}/{业务类名}Mapper.xml`

**示例**: `hos-app-datafill/hos-app-datafill-service/src/main/resources/datafill/DbConnectionManagementMapper.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.mediway.hos.datafill.mapper.{业务类名}Mapper">

    <!-- 自定义查询 -->
    <select id="customQuery" resultType="com.mediway.hos.datafill.model.entity.{业务类名}">
        SELECT * FROM {表名}
        WHERE is_deleted = 0
        <if test="param1 != null and param1 != ''">
            AND column1 = #{param1}
        </if>
        <if test="param2 != null and param2 != ''">
            AND column2 LIKE CONCAT('%', #{param2}, '%')
        </if>
    </select>

</mapper>
```

---

#### 1.6 单元测试 (hos-app-datafill-controller & hos-app-datafill-service)

##### 1.6.1 Controller 测试

**包路径**: `com.mediway.hos.datafill.controller` (test 目录)

**文件名**: `{业务类名}ControllerTest.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-controller/src/test/java/com/mediway/hos/datafill/controller/DbConnectionManagementControllerTest.java`

**代码模板**:

```java
package com.mediway.hos.datafill.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.mediway.hos.base.model.BaseResponse;
import com.mediway.hos.datafill.model.entity.{业务类名};
import com.mediway.hos.datafill.model.vo.{业务类名}VO;
import com.mediway.hos.datafill.service.{业务类名}Service;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

/**
 * {业务类名}Controller层单元测试
 *
 * @author GitHub Copilot
 * @date {日期}
 */
@ExtendWith(MockitoExtension.class)
@DisplayName("{业务类名}Controller测试")
public class {业务类名}ControllerTest {

    @Mock
    private {业务类名}Service {业务实例名}Service;

    @Mock
    private HttpServletRequest request;

    @InjectMocks
    private {业务类名}Controller controller;

    private {业务类名} testEntity;
    private {业务类名}VO testVO;

    @BeforeEach
    void setUp() {
        // 准备测试数据
        testEntity = new {业务类名}();
        testEntity.setId("test-id-001");
        // ...

        testVO = new {业务类名}VO();
        testVO.setId("test-id-001");
        // ...
    }

    @Test
    @DisplayName("UT-C-001: 分页查询API-成功")
    void testSelectPageListSuccess() {
        // Given
        Page<{业务类名}VO> mockPage = new Page<>(1, 10);
        mockPage.setRecords(Collections.singletonList(testVO));
        mockPage.setTotal(1);
        when({业务实例名}Service.selectPageList(anyLong(), anyLong(), ...)).thenReturn(mockPage);

        // When
        BaseResponse<IPage<{业务类名}VO>> response = controller.selectPageList(1L, 10L, ...);

        // Then
        assertThat(response.getCode()).isEqualTo(200);
        assertThat(response.getData().getRecords()).hasSize(1);
        verify({业务实例名}Service).selectPageList(anyLong(), anyLong(), ...);
    }

    @Test
    @DisplayName("UT-C-002: 查询详情API-成功")
    void testGetDetailByIdSuccess() {
        // Given
        when({业务实例名}Service.getDetailById("test-id-001")).thenReturn(testVO);

        // When
        BaseResponse<{业务类名}VO> response = controller.getDetailById("test-id-001");

        // Then
        assertThat(response.getCode()).isEqualTo(200);
        assertThat(response.getData()).isNotNull();
        assertThat(response.getData().getId()).isEqualTo("test-id-001");
    }

    @Test
    @DisplayName("UT-C-003: 新增API-成功")
    void testSaveSuccess() {
        // Given
        when({业务实例名}Service.save{业务类名}(any({业务类名}.class))).thenReturn(true);

        // When
        BaseResponse<Boolean> response = controller.save(testEntity, request);

        // Then
        assertThat(response.getCode()).isEqualTo(200);
        assertThat(response.getData()).isTrue();
    }

    @Test
    @DisplayName("UT-C-004: 批量删除API-成功")
    void testBatchDeleteByIdsSuccess() {
        // Given
        List<String> ids = Arrays.asList("id1", "id2");
        when({业务实例名}Service.batchDeleteByIds(ids)).thenReturn(true);

        // When
        BaseResponse<Boolean> response = controller.batchDeleteByIds(ids);

        // Then
        assertThat(response.getCode()).isEqualTo(200);
        assertThat(response.getData()).isTrue();
    }
}
```

##### 1.6.2 Service 测试

**包路径**: `com.mediway.hos.datafill.service` (test 目录)

**文件名**: `{业务类名}ServiceTest.java`

**示例**:

- 业务类名: `DbConnectionManagement`
- 完整路径: `hos-app-datafill/hos-app-datafill-service/src/test/java/com/mediway/hos/datafill/service/DbConnectionManagementServiceTest.java`

**代码模板**:

```java
package com.mediway.hos.datafill.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.mediway.hos.datafill.mapper.{业务类名}Mapper;
import com.mediway.hos.datafill.model.entity.{业务类名};
import com.mediway.hos.datafill.model.vo.{业务类名}VO;
import com.mediway.hos.datafill.service.impl.{业务类名}ServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("{业务类名}Service测试")
class {业务类名}ServiceTest {

    @Mock
    private {业务类名}Mapper mapper;

    @InjectMocks
    private {业务类名}ServiceImpl service;

    private {业务类名} testEntity;

    @BeforeEach
    void setUp() {
        testEntity = new {业务类名}();
        testEntity.setId("test-id-001");
        // ...
    }

    @Test
    @DisplayName("UT-S-001: 新增-成功")
    void testSaveSuccess() {
        // Given
        when(mapper.insert(any())).thenReturn(1);

        // When
        boolean result = service.save{业务类名}(testEntity);

        // Then
        assertThat(result).isTrue();
        verify(mapper).insert(any());
    }

    @Test
    @DisplayName("UT-S-002: 新增-参数校验失败")
    void testSaveValidationFailed() {
        // Given
        {业务类名} invalidEntity = new {业务类名}();

        // When & Then
        assertThatThrownBy(() -> service.save{业务类名}(invalidEntity))
                .isInstanceOf(IllegalArgumentException.class);
    }

    @Test
    @DisplayName("UT-S-003: 根据ID查询-成功")
    void testGetDetailByIdSuccess() {
        // Given
        when(mapper.selectById("test-id-001")).thenReturn(testEntity);

        // When
        {业务类名}VO result = service.getDetailById("test-id-001");

        // Then
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo("test-id-001");
    }

    @Test
    @DisplayName("UT-S-004: 批量删除-成功")
    void testBatchDeleteByIdsSuccess() {
        // Given
        List<String> ids = Arrays.asList("id1", "id2");

        // When
        boolean result = service.batchDeleteByIds(ids);

        // Then
        assertThat(result).isTrue();
    }
}
```

---

### 2. 代码生成流程

#### 步骤 1: 解析规范文档

从 `spec-*.md` 规范文档中提取以下信息:

1. **业务类名** (例如: `DbConnectionManagement`, `ModelManagement`)
2. **表名** (例如: `t_df_db_connection`, `t_df_model`)
3. **表字段列表** (字段名、类型、注释、是否必填等)
4. **API 接口列表** (接口路径、方法、参数、返回值)
5. **业务逻辑描述** (特殊校验、关联查询、业务规则等)

#### 步骤 2: 检查现有代码

1. **如果对应类不存在**: 创建新文件,严格按照包路径规范生成完整代码
2. **如果对应类已存在**:
   - 在现有类中添加缺失的方法
   - 修改不符合规范的代码
   - 保留现有的业务逻辑与注释

#### 步骤 3: 验证与更正规范文档

如果用户提供的类名与规范文档中的业务类名不一致:

1. **优先使用规范文档中的业务类名**
2. **提示用户**: "规范文档中定义的业务类名为 `{业务类名}`,您提供的类名为 `{用户类名}`,已按规范文档生成代码"
3. **如需更正规范**: 在 `spec-*.md` 文档的 `## Introduction` 章节更新 **业务类名** 字段

#### 步骤 4: 生成代码

严格按照以下顺序生成:

1. **Entity** (hos-app-datafill-model/entity)
2. **VO** (hos-app-datafill-model/vo)
3. **Mapper** (hos-app-datafill-service/mapper)
4. **Service 接口** (hos-app-datafill-service)
5. **Service 实现** (hos-app-datafill-service/impl)
6. **Api 接口** (hos-app-datafill-api)
7. **Controller** (hos-app-datafill-controller)
8. **Controller 测试** (hos-app-datafill-controller/test)
9. **Service 测试** (hos-app-datafill-service/test)

#### 步骤 5: 代码质量检查

生成代码后,自动检查:

1. **包路径正确性**: 确保与 `DbConnectionManagement` 示例一致
2. **继承关系正确**: Entity 继承 `BaseEntity`, Service 继承 `BaseService`, Controller 实现 Api 接口
3. **注解完整性**: `@Mapper`, `@Service`, `@RestController`, `@Api`, `@ApiOperation`, `@Transactional` 等
4. **命名规范**: 驼峰命名、类名大写、方法名小写
5. **Javadoc 注释**: 每个类、方法必须有注释
6. **SQL 安全**: 仅使用 `#{}` 占位符,禁止 `${}`

---

### 3. 特殊处理规则

#### 3.1 布尔字段兼容性

对于 `isEnabled`, `isDeleted` 等布尔字段,必须提供双重访问器:

```java
// Entity 类中必须包含:
public Integer getEnabled() {
    return this.isEnabled;
}

public void setEnabled(Integer enabled) {
    this.isEnabled = enabled;
}

public Integer getIsEnabled() {
    return this.isEnabled;
}

public void setIsEnabled(Integer isEnabled) {
    this.isEnabled = isEnabled;
}
```

**原因**: 兼容 Lombok 与 MyBatis-Plus,避免字段映射失败

#### 3.2 软删除字段

所有实体类必须包含 `isDeleted` 字段,并标注 `@TableLogic`:

```java
@ApiModelProperty(value = "是否删除:0-否,1-是")
@TableField("is_deleted")
@TableLogic(value = "0", delval = "1")
private Integer isDeleted;
```

#### 3.3 分页查询

Service 层分页方法必须返回 `IPage<VO>`,并转换 Entity 到 VO:

```java
IPage<{业务类名}> result = page(page, wrapper);
IPage<{业务类名}VO> voPage = result.convert(entity -> {
    {业务类名}VO vo = new {业务类名}VO();
    BeanUtils.copyProperties(entity, vo);
    return vo;
});
```

#### 3.4 密码字段脱敏

如包含密码字段 (如 `password`),查询接口必须脱敏:

```java
// Service 层
if (vo.getPassword() != null) {
    vo.setPassword("******");
}
```

#### 3.5 事务注解

所有修改操作方法 (新增、更新、删除) 必须添加事务注解:

```java
@Transactional(rollbackFor = Exception.class)
public boolean save{业务类名}({业务类名} entity) {
    // ...
}
```

---

### 4. 代码风格规范

#### 4.1 日志规范

- **使用 SLF4J**: `private static final Logger log = LoggerFactory.getLogger(XxxClass.class);`
- **日志级别**: `log.info()` (关键操作), `log.error()` (异常)
- **日志格式**: `log.info("操作描述 - 参数={}", 参数值);`
- **异常日志**: `log.error("操作失败 - 参数={}", 参数值, e);`

#### 4.2 异常处理

- **参数校验**: 使用 `IllegalArgumentException`
- **业务异常**: 使用 HOS 框架的 `BizException`
- **Controller 层**: 捕获所有异常,返回统一错误格式

```java
try {
    // 业务逻辑
    return BaseResponse.success(result);
} catch (Exception e) {
    log.error("操作失败", e);
    return BaseResponse.error("操作失败: " + e.getMessage());
}
```

#### 4.3 注释规范

- **类注释**: 包含 `@author`, `@date`
- **方法注释**: 包含 `@param`, `@return` Javadoc
- **字段注释**: 使用 `@ApiModelProperty` Swagger 注解

#### 4.4 代码格式

- **缩进**: 4 空格
- **大括号**: 与语句同行
- **空行**: 方法间空一行,逻辑块间空一行
- **导入**: 不使用通配符 `*`,按字母排序

---

### 5. 验收标准

生成的代码必须满足:

1. **包路径正确**: 与 `DbConnectionManagement` 示例一致
2. **编译通过**: 无语法错误,依赖正确
3. **单元测试覆盖**: Controller 与 Service 层 ≥75%
4. **代码规范**: 遵循 HOS 框架规范与 Java 编码规范
5. **功能完整**: 实现规范文档中定义的所有功能需求
6. **安全合规**: 密码加密、SQL 参数化、权限校验等

---

### 6. 示例用法

**示例 1**: 根据规范生成全新模块

```
请按照 hos-backend-code-generate.prompt.md 的要求,根据 spec-datafill-model-management.md 生成 ModelManagement 模块的所有代码。
```

**生成结果**:

- `hos-app-datafill-api/src/main/java/com/mediway/hos/datafill/api/ModelManagementApi.java`
- `hos-app-datafill-controller/src/main/java/com/mediway/hos/datafill/controller/ModelManagementController.java`
- `hos-app-datafill-model/src/main/java/com/mediway/hos/datafill/model/entity/ModelManagement.java`
- `hos-app-datafill-model/src/main/java/com/mediway/hos/datafill/model/vo/ModelManagementVO.java`
- `hos-app-datafill-service/src/main/java/com/mediway/hos/datafill/service/ModelManagementService.java`
- `hos-app-datafill-service/src/main/java/com/mediway/hos/datafill/service/impl/ModelManagementServiceImpl.java`
- `hos-app-datafill-service/src/main/java/com/mediway/hos/datafill/mapper/ModelManagementMapper.java`
- 对应的单元测试类

---

**示例 2**: 在现有类中添加方法

```
请按照 hos-backend-code-generate.prompt.md 的要求,根据 spec-datafill-db-connection-management.md 在 DbConnectionManagementService 中添加 `getDatabaseList` 方法。
```

**生成结果**:

- 在 `DbConnectionManagementService.java` 中添加方法签名
- 在 `DbConnectionManagementServiceImpl.java` 中添加方法实现
- 在 `DbConnectionManagementApi.java` 中添加 API 接口
- 在 `DbConnectionManagementController.java` 中添加 Controller 方法

---

**示例 3**: 更正规范文档

```
我希望将 spec-datafill-model-management.md 中的业务类名从 `ModelManagement` 改为 `DataModel`,请帮我更新规范文档并重新生成代码。
```

**处理流程**:

1. 更新 `spec-datafill-model-management.md` 的 `## Introduction` 章节,修改 **业务类名** 为 `DataModel`
2. 按新业务类名重新生成所有代码
3. 提示用户: "已将业务类名从 `ModelManagement` 更新为 `DataModel`,代码已重新生成"

---

## 附录: 常见问题

### Q1: 如果规范文档中缺少某些接口定义怎么办?

**A**: 优先参考 `spec-datafill-db-connection-management.md` 的接口设计,补充常用 CRUD 接口 (selectPageList, getDetailById, save, update, batchDeleteByIds)

### Q2: 如果业务类名与表名不对应怎么办?

**A**: 使用 `@TableName` 注解指定实际表名,类名保持 PascalCase 驼峰命名

### Q3: 如何处理复杂的多表关联查询?

**A**: 在 Mapper XML 中编写自定义 SQL,使用 `resultMap` 映射复杂结果,在 Service 层组装 VO

### Q4: 如何生成 Mapper XML 文件?

**A**: 如需自定义 SQL,在 `hos-app-datafill-service/src/main/resources/{模块名}/` 下创建 `{业务类名}Mapper.xml`,参考 DbConnectionManagement 示例

### Q5: 单元测试命名规范是什么?

**A**:

- 测试类: `{业务类名}ControllerTest`, `{业务类名}ServiceTest`
- 测试方法: `test{方法名}{场景}`,如 `testSelectPageListSuccess`, `testSaveValidationFailed`
- 显示名: `@DisplayName("UT-C-001: 分页查询API-成功")`

---

## 总结

本 Prompt 定义了 HOS 后端代码的生成规范,确保所有模块遵循统一的包路径、命名规范、代码风格与质量标准。生成代码时,务必:

1. **严格遵循包路径规范** (参考 `DbConnectionManagement` 示例)
2. **完整实现规范文档中的功能需求**
3. **保持代码风格一致性** (注解、日志、异常处理等)
4. **提供完整的单元测试覆盖**
5. **如遇歧义,优先以规范文档为准**

**最后**: 如有任何疑问或需要调整规范,请及时反馈并更新本 Prompt 文档!
