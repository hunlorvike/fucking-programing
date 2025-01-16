# Tổng Quan về Reflection và Attributes trong C# .NET

## Mục Lục

1. [Giới thiệu về Reflection và Attributes](#1-giới-thiệu-về-reflection-và-attributes)
   - [Reflection là gì?](#reflection-là-gì)
   - [Attributes là gì?](#attributes-là-gì)
   - [Ứng dụng của Reflection và Attributes](#ứng-dụng-của-reflection-và-attributes)
2. [Sử dụng Reflection trong C#](#2-sử-dụng-reflection-trong-c)
   - [Lấy thông tin về kiểu dữ liệu](#lấy-thông-tin-về-kiểu-dữ-liệu)
   - [Thao tác với đối tượng bằng Reflection](#thao-tác-với-đối-tượng-bằng-reflection)
   - [Tạo đối tượng động bằng Reflection](#tạo-đối-tượng-động-bằng-reflection)
3. [Attributes trong C#](#3-attributes-trong-c)
   - [Các loại Attributes](#các-loại-attributes)
   - [Tự tạo Attribute tùy chỉnh](#tự-tạo-attribute-tùy-chỉnh)
   - [Sử dụng Attributes với Reflection](#sử-dụng-attributes-với-reflection)
4. [Ưu và Nhược điểm của Reflection và Attributes](#4-ưu-và-nhược-điểm-của-reflection-và-attributes)
   - [Ưu điểm](#ưu-điểm)
   - [Nhược điểm](#nhược-điểm)
5. [Ví dụ thực tế của Reflection và Attributes](#5-ví-dụ-thực-tế-của-reflection-và-attributes)
6. [Kết luận](#6-kết-luận)

---

### 1. Giới thiệu về Reflection và Attributes

#### Reflection là gì?

Reflection trong C# là cơ chế cho phép truy cập thông tin về cấu trúc của mã nguồn tại runtime. Nó cung cấp khả năng kiểm tra và thao tác với các kiểu dữ liệu, phương thức, thuộc tính, trường, và event của các đối tượng hoặc assembly tại thời điểm thực thi.

#### Attributes là gì?

Attributes trong C# là các chú thích (metadata) được gắn kèm vào các phần tử của chương trình như lớp, phương thức, thuộc tính, hoặc toàn bộ assembly. Các Attribute cung cấp thông tin bổ sung mà chương trình có thể truy cập thông qua Reflection.

#### Ứng dụng của Reflection và Attributes

- **Reflection**:
  - Xây dựng các công cụ phát triển (IDE, debugger).
  - Nạp các assembly và sử dụng các thành phần của chúng động.
  - Kiểm tra hoặc thao tác các đối tượng không xác định trước (như Dependency Injection).
  
- **Attributes**:
  - Gắn thông tin metadata vào các thành phần chương trình.
  - Áp dụng trong serialization, logging, kiểm tra quyền hạn, và unit testing.

---

### 2. Sử dụng Reflection trong C#

#### Lấy thông tin về kiểu dữ liệu

Sử dụng `Type` để lấy thông tin về cấu trúc của một đối tượng hoặc lớp.

```csharp
Type type = typeof(string);

// Lấy tên lớp
Console.WriteLine($"Type Name: {type.Name}");

// Lấy các phương thức
var methods = type.GetMethods();
foreach (var method in methods)
{
    Console.WriteLine($"Method: {method.Name}");
}
```

#### Thao tác với đối tượng bằng Reflection

Reflection cho phép bạn gọi các phương thức, đọc hoặc gán giá trị cho các thuộc tính, và truy cập trường dữ liệu của một đối tượng.

```csharp
Type type = typeof(DateTime);
var now = DateTime.Now;

// Gọi phương thức "AddDays" bằng Reflection
var addDaysMethod = type.GetMethod("AddDays");
var newDate = addDaysMethod.Invoke(now, new object[] { 5 });
Console.WriteLine($"Date after 5 days: {newDate}");
```

#### Tạo đối tượng động bằng Reflection

Sử dụng `Activator.CreateInstance` để tạo đối tượng tại runtime.

```csharp
Type type = typeof(StringBuilder);
var stringBuilder = Activator.CreateInstance(type) as StringBuilder;

// Thao tác trên đối tượng
stringBuilder?.Append("Hello Reflection!");
Console.WriteLine(stringBuilder?.ToString());
```

---

### 3. Attributes trong C#

#### Các loại Attributes

1. **Built-in Attributes (Attributes tích hợp sẵn)**:
   - `[Obsolete]`: Đánh dấu một thành phần là không nên sử dụng.
   ```csharp
   [Obsolete("Use NewMethod instead.")]
   public void OldMethod() { }
   ```

   - `[Serializable]`: Đánh dấu lớp có thể được serializable.
   ```csharp
   [Serializable]
   public class MyClass { }
   ```

   - `[Conditional]`: Chỉ thực thi phương thức khi một điều kiện biên dịch được thỏa mãn.
   ```csharp
   [Conditional("DEBUG")]
   public void LogDebug(string message) { }
   ```

2. **Custom Attributes (Attributes tùy chỉnh)**:
   Người dùng có thể tạo Attribute của riêng mình để cung cấp metadata.

#### Tự tạo Attribute tùy chỉnh

Tạo một Attribute tùy chỉnh bằng cách kế thừa từ lớp `System.Attribute`.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = false)]
public class MyCustomAttribute : Attribute
{
    public string Description { get; }
    public MyCustomAttribute(string description)
    {
        Description = description;
    }
}

// Sử dụng Attribute tùy chỉnh
[MyCustomAttribute("This is a sample class.")]
public class SampleClass
{
    [MyCustomAttribute("This is a sample method.")]
    public void SampleMethod() { }
}
```

#### Sử dụng Attributes với Reflection

Reflection có thể được sử dụng để đọc metadata từ các Attributes.

```csharp
Type type = typeof(SampleClass);
var attributes = type.GetCustomAttributes(false);

foreach (var attribute in attributes)
{
    if (attribute is MyCustomAttribute myAttr)
    {
        Console.WriteLine($"Class Attribute Description: {myAttr.Description}");
    }
}
```

---

### 4. Ưu và Nhược điểm của Reflection và Attributes

#### Ưu điểm

- **Reflection**:
  - Cung cấp khả năng linh hoạt để làm việc với các đối tượng và kiểu dữ liệu tại runtime.
  - Hỗ trợ phát triển các công cụ mạnh mẽ như IDE và ORM.

- **Attributes**:
  - Cho phép gắn metadata vào mã nguồn, giúp tăng tính mô tả và dễ dàng truy xuất thông tin.
  - Dễ dàng mở rộng chức năng mà không cần sửa đổi cấu trúc chính của chương trình.

#### Nhược điểm

- **Reflection**:
  - Hiệu suất thấp hơn vì thao tác tại runtime.
  - Dễ bị lỗi nếu không kiểm tra cẩn thận kiểu dữ liệu và phương thức.

- **Attributes**:
  - Có thể làm mã nguồn phức tạp hơn khi sử dụng không hợp lý.
  - Một số Attributes tích hợp sẵn không đủ linh hoạt cho các trường hợp đặc biệt.

---

### 5. Ví dụ thực tế của Reflection và Attributes

#### 1. Kiểm tra và ghi log bằng Attributes

```csharp
[AttributeUsage(AttributeTargets.Method)]
public class LogAttribute : Attribute { }

public class Logger
{
    [Log]
    public void DoSomething()
    {
        Console.WriteLine("Doing something...");
    }
}

public class Program
{
    public static void Main()
    {
        var logger = new Logger();
        var methods = typeof(Logger).GetMethods();

        foreach (var method in methods)
        {
            if (method.GetCustomAttributes(typeof(LogAttribute), false).Length > 0)
            {
                Console.WriteLine($"Executing method: {method.Name}");
                method.Invoke(logger, null);
            }
        }
    }
}
```

#### 2. Dependency Injection (DI) sử dụng Reflection

Reflection giúp nạp và khởi tạo các thành phần phụ thuộc động trong một hệ thống DI.

---

### 6. Kết luận

Reflection và Attributes là những công cụ mạnh mẽ trong C# giúp tăng tính linh hoạt và khả năng mở rộng của ứng dụng. Reflection cho phép thao tác với các đối tượng tại runtime, trong khi Attributes giúp gắn thêm metadata để mô tả hành vi và cấu trúc của chương trình. Tuy nhiên, cần sử dụng một cách hợp lý để tránh làm giảm hiệu suất hoặc tăng độ phức tạp của mã nguồn.