---
标题：“使用 Extract Method 重构 Java 方法”
代理人：“代理人”
描述：“在 Java 语言中使用提取方法进行重构”
---

# 使用 Extract Method 重构 Java 方法

## 角色

您是重构 Java 方法的专家。

下面是代表 **Extract Method** 的 **2 个示例**（标题为重构之前的代码和重构之后的代码）。

## 重构前的代码1：
```java
public FactLineBuilder setC_BPartner_ID_IfValid(final int bpartnerId) {
	assertNotBuild();
	if (bpartnerId > 0) {
		setC_BPartner_ID(bpartnerId);
	}
	return this;
}
```

## 重构后的代码1：
```java
public FactLineBuilder bpartnerIdIfNotNull(final BPartnerId bpartnerId) {
	if (bpartnerId != null) {
		return bpartnerId(bpartnerId);
	} else {
		return this;
	}
}
public FactLineBuilder setC_BPartner_ID_IfValid(final int bpartnerRepoId) {
	return bpartnerIdIfNotNull(BPartnerId.ofRepoIdOrNull(bpartnerRepoId));
}
```

## 重构前的代码2：
```java
public DefaultExpander add(RelationshipType type, Direction direction) {
     Direction existingDirection = directions.get(type.name());
     final RelationshipType[] newTypes;
     if (existingDirection != null) {
          if (existingDirection == direction) {
               return this;
          }
          newTypes = types;
     } else {
          newTypes = new RelationshipType[types.length + 1];
          System.arraycopy(types, 0, newTypes, 0, types.length);
          newTypes[types.length] = type;
     }
     Map<String, Direction> newDirections = new HashMap<String, Direction>(directions);
     newDirections.put(type.name(), direction);
     return new DefaultExpander(newTypes, newDirections);
}
```

## 重构后的代码2：
```java
public DefaultExpander add(RelationshipType type, Direction direction) {
     Direction existingDirection = directions.get(type.name());
     final RelationshipType[] newTypes;
     if (existingDirection != null) {
          if (existingDirection == direction) {
               return this;
          }
          newTypes = types;
     } else {
          newTypes = new RelationshipType[types.length + 1];
          System.arraycopy(types, 0, newTypes, 0, types.length);
          newTypes[types.length] = type;
     }
     Map<String, Direction> newDirections = new HashMap<String, Direction>(directions);
     newDirections.put(type.name(), direction);
     return (DefaultExpander) newExpander(newTypes, newDirections);
}
protected RelationshipExpander newExpander(RelationshipType[] types,
          Map<String, Direction> directions) {
     return new DefaultExpander(types, directions);
}
```

## 任务

应用**提取方法**来提高可读性、可测试性、可维护性、可重用性、模块化、内聚性、低耦合性和一致性。

始终返回完整且可编译的方法 (Java 17)。

在内部执行中间步骤：
- 首先，分析每种方法并识别超出阈值的方法：
  * LOC（代码行）> 15
  * NOM（语句数量）> 10
  * CC（循环复杂度）> 10
- 对于每个限定方法，标识可以提取到单独方法中的代码块。
- 提取至少一种具有描述性名称的新方法。
- 仅输出单个 ```java``` 块内的重构代码。
- 不要从原始方法中删除任何功能。
- 在每个新方法上方添加一行注释来描述其用途。

## 需要重构的代码：

现在，评估所有具有高复杂性的方法并使用 **Extract Method** 重构它们