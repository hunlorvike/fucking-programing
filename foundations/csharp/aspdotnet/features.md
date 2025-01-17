# Tài liệu tổng hợp các tính năng nổi bật trong C#

Dưới đây là tài liệu tổng hợp các tính năng mới của **C#** từ **phiên bản 1.0** đến **phiên bản 12.0**. Tài liệu cung
cấp chi tiết về các tính năng chính được giới thiệu trong từng phiên bản, giúp bạn hiểu rõ hơn về sự phát triển và cải
tiến của ngôn ngữ qua từng năm.

## Mục lục

1. [Phiên bản 1.0 (2002)](#phiên-bản-1-0-2002)
    - Namespace
    - Classes & Objects
    - Interfaces
    - Delegates
    - Properties
2. [Phiên bản 2.0 (2005)](#phiên-bản-2-0-2005)
    - Generics
    - Nullable Types
    - Iterators
    - Partial Classes
    - Anonymous Methods
3. [Phiên bản 3.0 (2007)](#phiên-bản-3-0-2007)
    - LINQ
    - Lambda Expressions
    - Anonymous Types
    - Extension Methods
    - Auto-Implemented Properties
4. [Phiên bản 4.0 (2010)](#phiên-bản-4-0-2010)
    - Dynamic Binding
    - Named and Optional Parameters
    - Covariance và Contravariance
5. [Phiên bản 5.0 (2012)](#phiên-bản-5-0-2012)
    - Async & Await
    - Caller Information
6. [Phiên bản 6.0 (2015)](#phiên-bản-6-0-2015)
    - Auto-Property Initializers
    - Expression-bodied Members
    - Null-conditional Operator
    - String Interpolation
7. [Phiên bản 7.0 (2017)](#phiên-bản-7-0-2017)
    - Tuples
    - Pattern Matching
    - Out Variables
    - Local Functions
8. [Phiên bản 7.1, 7.2, 7.3](#phiên-bản-7-1-7-2-7-3)
    - Enhanced Pattern Matching
    - Async Main
    - Default Literals
9. [Phiên bản 8.0 (2019)](#phiên-bản-8-0-2019)
    - Nullable Reference Types
    - Async Streams
    - Indices and Ranges
    - Switch Expressions
10. [Phiên bản 9.0 (2020)](#phiên-bản-9-0-2020)
    - Record Types
    - Init-only Properties
    - Top-level Statements
    - With Expressions
11. [Phiên bản 10.0 (2021)](#phiên-bản-10-0-2021)
    - Global Using
    - File-scoped Namespaces
    - Constant Interpolated Strings
12. [Phiên bản 11.0 (2022)](#phiên-bản-11-0-2022)
    - Raw String Literals
    - Required Members
    - Generic Attributes
13. [Phiên bản 12.0 (2023)](#phiên-bản-12-0-2023)
    - Primary Constructors
    - Improved Interpolated Strings
    - Collection Expressions
    - Using Aliases
14. [Tóm Tắt](#tóm-tắt)

---

### Phiên bản 1.0 (2002)

- **Namespace (không gian tên)**: Giúp quản lý mã nguồn bằng cách tổ chức các lớp và kiểu dữ liệu theo không gian tên.

```csharp
using System;

namespace MyNamespace
{
    public class MyClass
    {
        public void Print() => Console.WriteLine("Hello from MyNamespace!");
    }
}
```

- **Classes & Objects (Lớp và đối tượng)**: C# hỗ trợ lập trình hướng đối tượng (OOP), cho phép tạo các lớp và đối
  tượng.

```csharp
public class Car
{
    public string Color { get; set; }
    public void Drive() => Console.WriteLine("Driving a " + Color + " car");
}

var myCar = new Car { Color = "red" };
myCar.Drive();
```

- **Interfaces (Giao diện)**: Định nghĩa các giao diện (interface) để thiết kế lập trình hướng giao diện.

```csharp
public interface IVehicle
{
    void Drive();
}

public class Car : IVehicle
{
    public void Drive() => Console.WriteLine("Car is driving");
}
```

- **Delegates**: Cho phép truyền hàm như là đối tượng và là nền tảng cho các sự kiện và xử lý bất đồng bộ.

```csharp
public delegate void Notify();

public class Process
{
    public event Notify OnComplete;
    public void Start() => OnComplete?.Invoke();
}
```

- **Properties (Thuộc tính)**: Cho phép kiểm soát việc truy cập và chỉnh sửa dữ liệu của lớp.

```csharp
public class Person
{
    public string Name { get; set; }
}

var person = new Person { Name = "Alice" };
Console.WriteLine(person.Name);
```

---

### Phiên bản 2.0 (2005)

- **Generics**: Tạo các lớp và phương thức kiểu tổng quát, giúp mã nguồn tái sử dụng linh hoạt hơn.

```csharp
public class GenericList<T>
{
    private T[] items = new T[10];
    public void Add(T item) { /*...*/ }
}

var intList = new GenericList<int>();
```

- **Nullable Types**: Kiểu dữ liệu chấp nhận giá trị `null`, cho phép kiểm tra và xử lý giá trị rỗng.

```csharp
int? age = null;
Console.WriteLine(age.HasValue ? age.Value.ToString() : "Age is unknown");
```

- **Iterators**: Hỗ trợ `yield` để tạo các phương thức trả về tuần tự các phần tử mà không cần phải dùng đến các
  collections.

```csharp
public IEnumerable<int> GetNumbers()
{
    yield return 1;
    yield return 2;
    yield return 3;
}
```

- **Partial Classes**: Cho phép định nghĩa một lớp trong nhiều tệp khác nhau.

```csharp
public partial class Car
{
    public string Model { get; set; }
}

public partial class Car
{
    public string Make { get; set; }
}
```

- **Anonymous Methods**: Hỗ trợ khai báo phương thức ẩn danh trong mã.

```csharp
Func<int, int> square = delegate(int x) { return x * x; };
```

---

### Phiên bản 3.0 (2007)

- **LINQ (Language Integrated Query)**: Cung cấp khả năng truy vấn dữ liệu trực tiếp trong C#.

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
var evenNumbers = numbers.Where(n => n % 2 == 0);
```

- **Lambda Expressions**: Biểu thức lambda giúp viết mã gọn hơn cho các hàm ẩn danh.

```csharp
Func<int, int> square = x => x * x;
```

- **Anonymous Types**: Cho phép tạo các kiểu ẩn danh, thường được dùng cùng với LINQ để lưu trữ dữ liệu tạm thời.

```csharp
var person = new { Name = "John", Age = 30 };
```

- **Extension Methods**: Mở rộng chức năng cho các lớp hiện có mà không cần kế thừa hay sửa đổi mã gốc.

```csharp
public static class StringExtensions
{
    public static bool IsNullOrEmpty(this string str)
    {
        return string.IsNullOrEmpty(str);
    }
}
```

- **Auto-Implemented Properties**: Giúp viết các thuộc tính tự động mà không cần tạo biến riêng.

```csharp
public class Car
{
    public string Make { get; set; }
}
```

---

### Phiên bản 4.0 (2010)

- **Dynamic Binding**: Hỗ trợ từ khóa `dynamic`, cho phép xác định kiểu của đối tượng trong thời gian chạy.

```csharp
dynamic expando = new ExpandoObject();
expando.Name = "Dynamic Name";
```

- **Named and Optional Parameters**: Hỗ trợ các tham số tùy chọn và đặt tên tham số trong lời gọi hàm.

```csharp
public void PrintMessage(string message = "Hello", int repeat = 1) { /*...*/ }
PrintMessage(repeat: 3);
```

- **Covariance và Contravariance**: Cải thiện khả năng sử dụng các kiểu tổng quát với các đối tượng kiểu dẫn xuất.

```csharp
IEnumerable<object> objects = new List<string>();
```

---

### Phiên bản 5.0 (2012)

- **Async & Await**: Giúp viết mã bất đồng bộ một cách dễ dàng và trực quan.

```csharp
public async Task<string> GetMessageAsync()
{
    await Task.Delay(1000);
    return "Hello";
}
```

- **Caller Information**: Thêm khả năng lấy thông tin về hàm gọi để phục vụ cho logging và xử lý lỗi.

```csharp
public void Log(string message, [CallerMemberName] string memberName = "")
{
    Console.WriteLine($"{memberName}: {message}");
}
```

---

### Phiên bản 6.0

(2015)

- **Auto-Property Initializers**: Cho phép khởi tạo thuộc tính tự động trực tiếp tại chỗ.

```csharp
public class Person
{
    public string Name { get; set; } = "Default Name";
}
```

- **Expression-bodied Members**: Cho phép định nghĩa các thành viên lớp chỉ bằng một biểu thức.

```csharp
public string GetName() => Name;
```

- **Null-conditional Operator**: Giúp tránh lỗi NullReferenceException.

```csharp
string name = person?.Name;
```

- **String Interpolation**: Cung cấp cách định dạng chuỗi dễ đọc hơn.

```csharp
Console.WriteLine($"Hello, {name}!");
```

---

### Phiên bản 7.0 (2017)

- **Tuples**: Hỗ trợ kiểu dữ liệu tuple, cho phép nhóm nhiều giá trị.

```csharp
var tuple = (1, "Hello");
Console.WriteLine(tuple.Item2);
```

- **Pattern Matching**: Hỗ trợ các cấu trúc điều kiện dựa trên kiểu và giá trị.

```csharp
if (obj is string s)
{
    Console.WriteLine(s);
}
```

- **Out Variables**: Cho phép khai báo biến trực tiếp trong tham số out.

```csharp
if (int.TryParse(input, out var result))
{
    Console.WriteLine(result);
}
```

- **Local Functions**: Cho phép định nghĩa các hàm địa phương trong phương thức khác.

```csharp
void LocalFunction() { /*...*/ }
```

---

### Phiên bản 7.1, 7.2, 7.3

- **Enhanced Pattern Matching**: Mở rộng khả năng so khớp mẫu.

- **Async Main**: Cho phép phương thức Main là async.

```csharp
public static async Task Main() { /*...*/ }
```

- **Default Literals**: Hỗ trợ sử dụng từ khóa `default` cho các kiểu dữ liệu.

```csharp
int num = default;
```

---

### Phiên bản 8.0 (2019)

- **Nullable Reference Types**: Giúp kiểm soát giá trị null trong các kiểu tham chiếu.

```csharp
#nullable enable
public string? Name { get; set; }
```

- **Async Streams**: Hỗ trợ làm việc với luồng dữ liệu bất đồng bộ.

```csharp
await foreach (var item in asyncEnumerable) { /*...*/ }
```

- **Indices and Ranges**: Cho phép truy cập vào các phần tử của mảng theo chỉ số và khoảng cách.

```csharp
var range = array[1..5];
```

- **Switch Expressions**: Cải tiến cấu trúc switch, cho phép xử lý điều kiện gọn gàng hơn.

```csharp
var result = input switch
{
    1 => "One",
    2 => "Two",
    _ => "Unknown"
};
```

---

### Phiên bản 9.0 (2020)

- **Record Types**: Định nghĩa loại bản ghi, giúp tạo các đối tượng không thay đổi.

```csharp
public record Person(string Name, int Age);
```

- **Init-only Properties**: Thuộc tính chỉ có thể khởi tạo một lần.

```csharp
public class Person
{
    public string Name { get; init; }
}
```

- **Top-level Statements**: Giúp viết mã C# đơn giản hơn mà không cần định nghĩa lớp hay phương thức Main.

```csharp
Console.WriteLine("Hello, World!");
```

- **With Expressions**: Cho phép tạo bản sao với các thuộc tính thay đổi.

```csharp
var newPerson = person with { Age = 30 };
```

---

### Phiên bản 10.0 (2021)

- **Global Using**: Hỗ trợ định nghĩa using toàn cục trong tệp để giảm thiểu lặp lại.

```csharp
global using System;
```

- **File-scoped Namespaces**: Giúp định nghĩa không gian tên cho toàn bộ tệp.

```csharp
namespace MyNamespace;
```

- **Constant Interpolated Strings**: Hỗ trợ chuỗi định dạng hằng.

```csharp
const string greeting = $"Hello, {name}";
```

---

### Phiên bản 11.0 (2022)

- **Raw String Literals**: Hỗ trợ chuỗi thô, cho phép định nghĩa chuỗi mà không cần escape.

```csharp
string rawString = """This is a raw string with "quotes" and new lines""";
```

- **Required Members**: Cho phép định nghĩa các thuộc tính yêu cầu trong lớp.

```csharp
public class Person
{
    public required string Name { get; init; }
}
```

- **Generic Attributes**: Hỗ trợ sử dụng thuộc tính với kiểu tổng quát.

```csharp
[AttributeUsage(AttributeTargets.Class)]
public class MyAttribute<T> : Attribute { }
```

---

### Phiên bản 12.0 (2023)

- **Primary Constructors**: Hỗ trợ khởi tạo trực tiếp trong định nghĩa lớp.

```csharp
public class Person(string name, int age) { /*...*/ }
```

- **Improved Interpolated Strings**: Cải tiến khả năng sử dụng chuỗi định dạng.

```csharp
string message = $"Hello, {person.Name}";
```

- **Collection Expressions**: Hỗ trợ cú pháp mới cho việc khởi tạo danh sách.

```csharp
var list = [1, 2, 3, 4];
```

- **Using Aliases**: Hỗ trợ định nghĩa bí danh cho using.

```csharp
using Project = MyNamespace.MyProject;
```

---

### Tóm Tắt

Ngôn ngữ **C#** đã trải qua nhiều thay đổi và cải tiến từ phiên bản 1.0 đến 12.0, mỗi phiên bản mang lại nhiều tính năng
mạnh mẽ, giúp lập trình viên viết mã hiệu quả và dễ hiểu hơn. Các tính năng như **LINQ**, **Async/Await**, **Nullable
Types**, và **Record Types** đã thay đổi cách mà các ứng dụng được phát triển trong C#.

Với mỗi phiên bản mới, Microsoft không ngừng nâng cao trải nghiệm lập trình và hỗ trợ lập trình viên trong việc xây dựng
ứng dụng hiện đại.
