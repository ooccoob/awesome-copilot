---
applyTo: '**/*.{cs,ts,java}'
description: Enforces Object Calisthenics principles for business domain code to ensure clean, maintainable, and robust code
---
# 物体健美操规则

> ⚠️ **警告：** 该文件包含 9 条原始的物体健美操规则。不得添加任何其他规则，并且不得替换或删除这些规则。
> 如果需要，可以稍后添加示例。

## 目的
此规则强制执行对象体操原则，以确保后端代码干净、可维护且健壮，**主要针对业务领域代码**。

## 范围及应用
- **主要焦点**：业务领域类（聚合、实体、值对象、领域服务）
- **次要焦点**：应用程序层服务和用例处理程序
- **豁免**： 
  - DTO（数据传输对象）
  - API模型/合约
  - 配置类
  - 没有业务逻辑的简单数据容器
  - 需要灵活性的基础设施代码

## 关键原则


1. **每个方法一级缩进**：
   - 确保方法简单且缩进不超过一级。

   ```csharp
   // Bad Example - this method has multiple levels of indentation
   public void SendNewsletter() {
         foreach (var user in users) {
            if (user.IsActive) {
               // Do something
               mailer.Send(user.Email);
            }
         }
   }
   // Good Example - Extracted method to reduce indentation
   public void SendNewsletter() {
       foreach (var user in users) {
           SendEmail(user);
       }
   }
   private void SendEmail(User user) {
       if (user.IsActive) {
           mailer.Send(user.Email);
       }
   }

   // Good Example - Filtering users before sending emails
   public void SendNewsletter() {
       var activeUsers = users.Where(user => user.IsActive);

       foreach (var user in activeUsers) {
           mailer.Send(user.Email);
       }
   }
   ```
2. **不要使用 ELSE 关键字**：

   - 避免使用 `else` 关键字以降低复杂性并提高可读性。
   - 使用提前返回来处理情况。
   - 使用快速失败原则
   - 使用保护子句来验证方法开头的输入和条件。

   ```csharp
   // Bad Example - Using else
   public void ProcessOrder(Order order) {
       if (order.IsValid) {
           // Process order
       } else {
           // Handle invalid order
       }
   }
   // Good Example - Avoiding else
   public void ProcessOrder(Order order) {
       if (!order.IsValid) return;
       // Process order
   }
   ```

   样品快速失败原理：
   ```csharp
   public void ProcessOrder(Order order) {
       if (order == null) throw new ArgumentNullException(nameof(order));
       if (!order.IsValid) throw new InvalidOperationException("Invalid order");
       // Process order
   }
   ```

3. **包装所有原语和字符串**：
   - 避免直接在代码中使用原始类型。
   - 将它们包装在类中以提供有意义的上下文和行为。

   ```csharp
   // Bad Example - Using primitive types directly
   public class User {
       public string Name { get; set; }
       public int Age { get; set; }
   }
   // Good Example - Wrapping primitives
   public class User {
       private string name;
       private Age age;
       public User(string name, Age age) {
           this.name = name;
           this.age = age;
       }
   }
   public class Age {
       private int value;
       public Age(int value) {
           if (value < 0) throw new ArgumentOutOfRangeException(nameof(value), "Age cannot be negative");
           this.value = value;
       }
   }
   ```   

4. **一流收藏**：
   - 使用集合来封装数据和行为，而不是暴露原始数据结构。
第一类集合：包含数组作为属性的类不应包含任何其他属性

```csharp
   // Bad Example - Exposing raw collection
   public class Group {
      public int Id { get; private set; }
      public string Name { get; private set; }
      public List<User> Users { get; private set; }

      public int GetNumberOfUsersIsActive() {
         return Users
            .Where(user => user.IsActive)
            .Count();
      }
   }

   // Good Example - Encapsulating collection behavior
   public class Group {
      public int Id { get; private set; }
      public string Name { get; private set; }

      public GroupUserCollection userCollection { get; private set; } // The list of users is encapsulated in a class

      public int GetNumberOfUsersIsActive() {
         return userCollection
            .GetActiveUsers()
            .Count();
      }
   }
   ```

5. **每行一个点**：
   - 每行只有一个点，避免违反德米特定律。

   ```csharp
   // Bad Example - Multiple dots in a single line
   public void ProcessOrder(Order order) {
       var userEmail = order.User.GetEmail().ToUpper().Trim();
       // Do something with userEmail
   }
   // Good Example - One dot per line
   public class User {
     public NormalizedEmail GetEmail() {
       return NormalizedEmail.Create(/*...*/);       
     }
   }
   public class Order {
     /*...*/
     public NormalizedEmail ConfirmationEmail() {
       return User.GetEmail();         
     }
   }
   public void ProcessOrder(Order order) {
       var confirmationEmail = order.ConfirmationEmail();
       // Do something with confirmationEmail
   }
   ```

6. **不要缩写**：
   - 为类、方法和变量使用有意义的名称。
   - 避免使用可能导致混淆的缩写。

   ```csharp
   // Bad Example - Abbreviated names
   public class U {
       public string N { get; set; }
   }
   // Good Example - Meaningful names
   public class User {
       public string Name { get; set; }
   }
   ```

7. **保持实体较小（类、方法、命名空间或包）**：
   - 限制类和方法的大小以提高代码的可读性和可维护性。
   - 每个类应该有单一的职责并且尽可能小。
   
   限制条件：
   - 每个类最多 10 个方法
   - 每类最多 50 行
   - 每个包或命名空间最多 10 个类

   ```csharp
   // Bad Example - Large class with multiple responsibilities
   public class UserManager {
       public void CreateUser(string name) { /*...*/ }
       public void DeleteUser(int id) { /*...*/ }
       public void SendEmail(string email) { /*...*/ }
   }

   // Good Example - Small classes with single responsibility
   public class UserCreator {
       public void CreateUser(string name) { /*...*/ }
   }
   public class UserDeleter {
       public void DeleteUser(int id) { /*...*/ }
   }

   public class UserUpdater {
       public void UpdateUser(int id, string name) { /*...*/ }
   }
   ```


8. **没有类具有两个以上实例变量**：
   - 通过限制实例变量的数量来鼓励类承担单一责任。
   - 将实例变量的数量限制为两个以保持简单性。
   - 不要将 ILogger 或任何其他记录器计为实例变量。

   ```csharp
   // Bad Example - Class with multiple instance variables
   public class UserCreateCommandHandler {
      // Bad: Too many instance variables
      private readonly IUserRepository userRepository;
      private readonly IEmailService emailService;
      private readonly ILogger logger;
      private readonly ISmsService smsService;

      public UserCreateCommandHandler(IUserRepository userRepository, IEmailService emailService, ILogger logger, ISmsService smsService) {
         this.userRepository = userRepository;
         this.emailService = emailService;
         this.logger = logger;
         this.smsService = smsService;
      }
   }

   // Good: Class with two instance variables
   public class UserCreateCommandHandler {
      private readonly IUserRepository userRepository;
      private readonly INotificationService notificationService;
      private readonly ILogger logger; // This is not counted as instance variable

      public UserCreateCommandHandler(IUserRepository userRepository, INotificationService notificationService, ILogger logger) {
         this.userRepository = userRepository;
         this.notificationService = notificationService;
         this.logger = logger;
      }
   }
   ```

9. **域类中没有 Getter/Setter**：
   - 避免公开域类中属性的设置器。
   - 使用私有构造函数和静态工厂方法来创建对象。
   - **注意**：此规则主要适用于域类，而不是 DTO 或数据传输对象。

   ```csharp
   // Bad Example - Domain class with public setters
   public class User {  // Domain class
       public string Name { get; set; } // Avoid this in domain classes
   }
   
   // Good Example - Domain class with encapsulation
   public class User {  // Domain class
       private string name;
       private User(string name) { this.name = name; }
       public static User Create(string name) => new User(name);
   }
   
   // Acceptable Example - DTO with public setters
   public class UserDto {  // DTO - exemption applies
       public string Name { get; set; } // Acceptable for DTOs
   }
   ```

## 实施指南
- **域类**：
  - 使用私有构造函数和静态工厂方法来创建实例。
  - 避免暴露属性的设置器。
  - 对业务域代码严格应用所有 9 条规则。

- **应用层**：
  - 将这些规则应用于用例处理程序和应用程序服务。
  - 专注于维护单一责任和干净的抽象。

- **DTO 和数据对象**：
  - 对于 DTO，规则 3（包装原语）、规则 8（两个实例变量）和规则 9（无 getter/setter）可能会放宽。
  - 数据传输对象可以接受具有 getter/setter 的公共属性。

- **测试**：
  - 确保测试验证对象的行为而不是其状态。
  - 测试类可能有宽松的可读性和可维护性规则。

- **代码审查**：
  - 在域和应用程序代码的代码审查期间强制执行这些规则。
  - 对于基础设施和 DTO 代码要务实。

## 参考文献
- [物体健美操 - Jeff Bay 原创 9 条规则](https://www.cs.helsinki.fi/u/luontola/tdd-2009/ext/ObjectCalisthenics.pdf)
- [ThoughtWorks - 物体健美操](https://www.thoughtworks.com/insights/blog/object-calisthenics)
- [整洁代码：敏捷软件工艺手册 - Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
