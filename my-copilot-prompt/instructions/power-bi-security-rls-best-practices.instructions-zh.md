---
描述：“全面的 Power BI 行级安全性 (RLS) 和高级安全模式实施指南，包括动态安全性、最佳实践和治理策略。”
applyTo: '**/*.{pbix,dax,md,txt,json,csharp,powershell}'
---

# Power BI 安全和行级安全最佳实践

## 概述
本文档提供了在 Power BI 中实现强大安全模式的全面说明，重点关注行级安全性 (RLS)、动态安全性和基于 Microsoft 官方指南的治理最佳实践。

## 行级安全基础知识

### 1. RLS基本实现
```dax
// Simple user-based filtering
[EmailAddress] = USERNAME()

// Role-based filtering with improved security
IF(
    USERNAME() = "Worker",
    [Type] = "Internal",
    IF(
        USERNAME() = "Manager",
        TRUE(),
        FALSE()  // Deny access to unexpected users
    )
)
```

### 2. 具有自定义数据的动态 RLS
```dax
// Using CUSTOMDATA() for dynamic filtering
VAR UserRole = CUSTOMDATA()
RETURN
    SWITCH(
        UserRole,
        "SalesPersonA", [SalesTerritory] = "West",
        "SalesPersonB", [SalesTerritory] = "East",
        "Manager", TRUE(),
        FALSE()  // Default deny
    )
```

### 3. 高级安全模式
```dax
// Hierarchical security with territory lookups
=DimSalesTerritory[SalesTerritoryKey]=LOOKUPVALUE(
    DimUserSecurity[SalesTerritoryID], 
    DimUserSecurity[UserName], USERNAME(), 
    DimUserSecurity[SalesTerritoryID], DimSalesTerritory[SalesTerritoryKey]
)

// Multiple condition security
VAR UserTerritories = 
    FILTER(
        UserSecurity,
        UserSecurity[UserName] = USERNAME()
    )
VAR AllowedTerritories = SELECTCOLUMNS(UserTerritories, "Territory", UserSecurity[Territory])
RETURN
    [Territory] IN AllowedTerritories
```

## 嵌入式分析安全

### 1. 静态RLS实现
```csharp
// Static RLS with fixed roles
var rlsidentity = new EffectiveIdentity(
    username: "username@contoso.com", 
    roles: new List<string>{ "MyRole" },
    datasets: new List<string>{ datasetId.ToString()}
);
```

### 2. 具有自定义数据的动态 RLS
```csharp
// Dynamic RLS with custom data
var rlsidentity = new EffectiveIdentity(
    username: "username@contoso.com",
    roles: new List<string>{ "MyRoleWithCustomData" },
    customData: "SalesPersonA",
    datasets: new List<string>{ datasetId.ToString()}
);
```

### 3. 多数据集安全
```json
{
    "accessLevel": "View",
    "identities": [
        {
            "username": "France",
            "roles": [ "CountryDynamic"],
            "datasets": [ "fe0a1aeb-f6a4-4b27-a2d3-b5df3bb28bdc" ]
        }
    ]
}
```

## 数据库级安全集成

### 1. SQL Server RLS 集成
```sql
-- Creating security schema and predicate function
CREATE SCHEMA Security;
GO

CREATE FUNCTION Security.tvf_securitypredicate(@SalesRep AS nvarchar(50))
    RETURNS TABLE
WITH SCHEMABINDING
AS
    RETURN SELECT 1 AS tvf_securitypredicate_result
WHERE @SalesRep = USER_NAME() OR USER_NAME() = 'Manager';
GO

-- Applying security policy
CREATE SECURITY POLICY SalesFilter
ADD FILTER PREDICATE Security.tvf_securitypredicate(SalesRep)
ON sales.Orders
WITH (STATE = ON);
GO
```

### 2. 面料仓库安全
```sql
-- Creating schema for Security
CREATE SCHEMA Security;
GO

-- Creating a function for the SalesRep evaluation
CREATE FUNCTION Security.tvf_securitypredicate(@UserName AS varchar(50))
    RETURNS TABLE
WITH SCHEMABINDING
AS
    RETURN SELECT 1 AS tvf_securitypredicate_result
WHERE @UserName = USER_NAME()
OR USER_NAME() = 'BatchProcess@contoso.com';
GO

-- Using the function to create a Security Policy
CREATE SECURITY POLICY YourSecurityPolicy
ADD FILTER PREDICATE Security.tvf_securitypredicate(UserName_column)
ON sampleschema.sampletable
WITH (STATE = ON);
GO
```

## 高级安全模式

### 1. 分页报告安全性
```json
{
    "format": "PDF",
    "paginatedReportConfiguration":{
        "identities": [
            {"username": "john@contoso.com"}
        ]
    }
}
```

### 2. 电源页面集成
```html
{% powerbi authentication_type:"powerbiembedded" path:"https://app.powerbi.com/groups/00000000-0000-0000-0000-000000000000/reports/00000000-0000-0000-0000-000000000001/ReportSection" roles:"pagesuser" %}
```

### 3. 多租户安全
```json
{
  "datasets": [
    {
      "id": "fff1a505-xxxx-xxxx-xxxx-e69f81e5b974",
    }
  ],
  "reports": [
    {
      "allowEdit": false,
      "id": "10ce71df-xxxx-xxxx-xxxx-814a916b700d"
    }
  ],
  "identities": [
    {
      "username": "YourUsername",
      "datasets": [
        "fff1a505-xxxx-xxxx-xxxx-e69f81e5b974"
      ],
      "roles": [
        "YourRole"
      ]
    }
  ],
  "datasourceIdentities": [
    {
      "identityBlob": "eyJ…",
      "datasources": [
        {
          "datasourceType": "Sql",
          "connectionDetails": {
            "server": "YourServerName.database.windows.net",
            "database": "YourDataBaseName"
          }
        }
      ]
    }
  ]
}
```

## 安全设计模式

### 1. 部分RLS实现
```dax
// Create summary table for partial RLS
SalesRevenueSummary =
SUMMARIZECOLUMNS(
    Sales[OrderDate],
    "RevenueAllRegion", SUM(Sales[Revenue])
)

// Apply RLS only to detail level
Salesperson Filter = [EmailAddress] = USERNAME()
```

### 2. 分级安全
```dax
// Manager can see all, others see their own
VAR CurrentUser = USERNAME()
VAR UserRole = LOOKUPVALUE(
    UserRoles[Role], 
    UserRoles[Email], CurrentUser
)
RETURN
    SWITCH(
        UserRole,
        "Manager", TRUE(),
        "Salesperson", [SalespersonEmail] = CurrentUser,
        "Regional Manager", [Region] IN (
            SELECTCOLUMNS(
                FILTER(UserRegions, UserRegions[Email] = CurrentUser),
                "Region", UserRegions[Region]
            )
        ),
        FALSE()
    )
```

### 3. 基于时间的安全性
```dax
// Restrict access to recent data based on role
VAR UserRole = LOOKUPVALUE(UserRoles[Role], UserRoles[Email], USERNAME())
VAR CutoffDate = 
    SWITCH(
        UserRole,
        "Executive", DATE(1900,1,1),  // All historical data
        "Manager", TODAY() - 365,     // Last year
        "Analyst", TODAY() - 90,      // Last 90 days
        TODAY()                       // Current day only
    )
RETURN
    [Date] >= CutoffDate
```

## 安全验证和测试

### 1. 角色验证模式
```dax
// Security testing measure
Security Test = 
VAR CurrentUsername = USERNAME()
VAR ExpectedRole = "TestRole"
VAR TestResult = 
    IF(
        HASONEVALUE(SecurityRoles[Role]) && 
        VALUES(SecurityRoles[Role]) = ExpectedRole,
        "PASS: Role applied correctly",
        "FAIL: Incorrect role or multiple roles"
    )
RETURN
    "User: " & CurrentUsername & " | " & TestResult
```

### 2. 数据暴露审计
```dax
// Audit measure to track data access
Data Access Audit = 
VAR AccessibleRows = COUNTROWS(FactTable)
VAR TotalRows = CALCULATE(COUNTROWS(FactTable), ALL(FactTable))
VAR AccessPercentage = DIVIDE(AccessibleRows, TotalRows) * 100
RETURN
    "User: " & USERNAME() & 
    " | Accessible: " & FORMAT(AccessibleRows, "#,0") & 
    " | Total: " & FORMAT(TotalRows, "#,0") & 
    " | Access: " & FORMAT(AccessPercentage, "0.00") & "%"
```

## 治理与行政

### 1. 自动化安全组管理
```powershell
# Add security group to Power BI workspace
# Sign in to Power BI
Login-PowerBI

# Set up the security group object ID
$SGObjectID = "<security-group-object-ID>"

# Get the workspace
$pbiWorkspace = Get-PowerBIWorkspace -Filter "name eq '<workspace-name>'"

# Add the security group to the workspace
Add-PowerBIWorkspaceUser -Id $($pbiWorkspace.Id) -AccessRight Member -PrincipalType Group -Identifier $($SGObjectID)
```

### 2、安全监控
```powershell
# Monitor Power BI access patterns
$workspaces = Get-PowerBIWorkspace
foreach ($workspace in $workspaces) {
    $users = Get-PowerBIWorkspaceUser -Id $workspace.Id
    Write-Host "Workspace: $($workspace.Name)"
    foreach ($user in $users) {
        Write-Host "  User: $($user.UserPrincipalName) - Access: $($user.AccessRight)"
    }
}
```

### 3. 合规报告
```dax
// Compliance dashboard measures
Users with Data Access = 
CALCULATE(
    DISTINCTCOUNT(AuditLog[Username]),
    AuditLog[AccessType] = "DataAccess",
    AuditLog[Date] >= TODAY() - 30
)

High Privilege Users = 
CALCULATE(
    DISTINCTCOUNT(UserRoles[Email]),
    UserRoles[Role] IN {"Admin", "Manager", "Executive"}
)

Security Violations = 
CALCULATE(
    COUNTROWS(AuditLog),
    AuditLog[EventType] = "SecurityViolation",
    AuditLog[Date] >= TODAY() - 7
)
```

## 最佳实践和反模式

### ✅ 安全最佳实践

#### 1. 最小特权原则
```dax
// Always default to restrictive access
Default Security = 
VAR UserPermissions = 
    FILTER(
        UserAccess,
        UserAccess[Email] = USERNAME()
    )
RETURN
    IF(
        COUNTROWS(UserPermissions) > 0,
        [Territory] IN SELECTCOLUMNS(UserPermissions, "Territory", UserAccess[Territory]),
        FALSE()  // No access if not explicitly granted
    )
```

#### 2. 显式角色验证
```dax
// Validate expected roles explicitly
Role-Based Filter = 
VAR UserRole = LOOKUPVALUE(UserRoles[Role], UserRoles[Email], USERNAME())
VAR AllowedRoles = {"Analyst", "Manager", "Executive"}
RETURN
    IF(
        UserRole IN AllowedRoles,
        SWITCH(
            UserRole,
            "Analyst", [Department] = LOOKUPVALUE(UserDepartments[Department], UserDepartments[Email], USERNAME()),
            "Manager", [Region] = LOOKUPVALUE(UserRegions[Region], UserRegions[Email], USERNAME()),
            "Executive", TRUE()
        ),
        FALSE()  // Deny access for unexpected roles
    )
```

### ❌ 要避免的安全反模式

#### 1. 过于宽松的默认设置
```dax
// ❌ AVOID: This grants full access to unexpected users
Bad Security Filter = 
IF(
    USERNAME() = "SpecificUser",
    [Type] = "Internal",
    TRUE()  // Dangerous default
)
```

#### 2. 复杂的安全逻辑
```dax
// ❌ AVOID: Overly complex security that's hard to audit
Overly Complex Security = 
IF(
    OR(
        AND(USERNAME() = "User1", WEEKDAY(TODAY()) <= 5),
        AND(USERNAME() = "User2", HOUR(NOW()) >= 9, HOUR(NOW()) <= 17),
        AND(CONTAINS(VALUES(SpecialUsers[Email]), SpecialUsers[Email], USERNAME()), [Priority] = "High")
    ),
    [Type] IN {"Internal", "Confidential"},
    [Type] = "Public"
)
```

## 安全集成模式

### 1.Azure AD 集成
```csharp
// Generate token with Azure AD user context
var tokenRequest = new GenerateTokenRequestV2(
    reports: new List<GenerateTokenRequestV2Report>() { new GenerateTokenRequestV2Report(reportId) },
    datasets: datasetIds.Select(datasetId => new GenerateTokenRequestV2Dataset(datasetId.ToString())).ToList(),
    targetWorkspaces: targetWorkspaceId != Guid.Empty ? new List<GenerateTokenRequestV2TargetWorkspace>() { new GenerateTokenRequestV2TargetWorkspace(targetWorkspaceId) } : null,
    identities: new List<EffectiveIdentity> { rlsIdentity }
);

var embedToken = pbiClient.EmbedToken.GenerateToken(tokenRequest);
```

### 2. 服务主体认证
```csharp
// Service principal with RLS for embedded scenarios
public EmbedToken GetEmbedToken(Guid reportId, IList<Guid> datasetIds, [Optional] Guid targetWorkspaceId)
{
    PowerBIClient pbiClient = this.GetPowerBIClient();

    var rlsidentity = new EffectiveIdentity(
       username: "username@contoso.com",
       roles: new List<string>{ "MyRole" },
       datasets: new List<string>{ datasetId.ToString()}
    );
    
    var tokenRequest = new GenerateTokenRequestV2(
        reports: new List<GenerateTokenRequestV2Report>() { new GenerateTokenRequestV2Report(reportId) },
        datasets: datasetIds.Select(datasetId => new GenerateTokenRequestV2Dataset(datasetId.ToString())).ToList(),
        targetWorkspaces: targetWorkspaceId != Guid.Empty ? new List<GenerateTokenRequestV2TargetWorkspace>() { new GenerateTokenRequestV2TargetWorkspace(targetWorkspaceId) } : null,
        identities: new List<EffectiveIdentity> { rlsIdentity }
    );

    var embedToken = pbiClient.EmbedToken.GenerateToken(tokenRequest);

    return embedToken;
}
```

## 安全监控与审计

### 1. 访问模式分析
```dax
// Identify unusual access patterns
Unusual Access Pattern = 
VAR UserAccessCount = 
    CALCULATE(
        COUNTROWS(AccessLog),
        AccessLog[Date] >= TODAY() - 7
    )
VAR AvgUserAccess = 
    CALCULATE(
        AVERAGE(AccessLog[AccessCount]),
        ALL(AccessLog[Username]),
        AccessLog[Date] >= TODAY() - 30
    )
RETURN
    IF(
        UserAccessCount > AvgUserAccess * 3,
        "⚠️ High Activity",
        "Normal"
    )
```

### 2. 数据泄露检测
```dax
// Detect potential data exposure
Potential Data Exposure = 
VAR UnexpectedAccess = 
    CALCULATE(
        COUNTROWS(AccessLog),
        AccessLog[AccessResult] = "Denied",
        AccessLog[Date] >= TODAY() - 1
    )
RETURN
    IF(
        UnexpectedAccess > 10,
        "🚨 Multiple Access Denials - Review Required",
        "Normal"
    )
```

请记住：安全是分层的 - 通过适当的身份验证、授权、数据加密、网络安全和全面的审核来实施深度防御。定期审查和测试安全实施，以确保它们满足当前的要求和合规性标准。