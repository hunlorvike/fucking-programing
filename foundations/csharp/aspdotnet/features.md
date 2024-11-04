## Các tính năng nổi bật trong C#

Dưới đây là tài liệu tổng hợp các tính năng mới của **C#** từ **phiên bản 1.0** đến **phiên bản 12.0**. Tài liệu cung cấp chi tiết về các tính năng chính được giới thiệu trong từng phiên bản, giúp bạn hiểu rõ hơn về sự phát triển và cải tiến của ngôn ngữ qua từng năm.

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

- **Classes & Objects (Lớp và đối tượng)**: C# hỗ trợ lập trình hướng đối tượng (OOP), cho phép tạo các lớp và đối tượng.

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

- **Iterators**: Hỗ trợ `yield` để tạo các phương thức trả về tuần tự các phần tử mà không cần phải dùng đến các collections.

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

### Phiên bản 6.0 (2015)

- **Auto-Property Initializers**: Cho phép gán giá trị khởi tạo cho thuộc tính ngay trong lúc khai báo.

```csharp
public class Car
{
    public string Make { get; set; } = "Toyota";
}
```

- **Expression-bodied Members**: Rút gọn cú pháp của các phương thức chỉ có một biểu thức.

```csharp
public string Name => "C#";

public void Print() => Console.WriteLine("Hello from C#");
```

- **Null-conditional Operator**: Toán tử `?.` kiểm tra null trước khi truy cập thành phần của đối tượng.

```csharp
string name = person?.Name;
```

- **String Interpolation**: Kết hợp chuỗi và biểu thức trực tiếp trong chuỗi với `$""`.

```csharp
string name = "C#";
Console.WriteLine($"Hello, {name}!");
```

---

### Phiên bản 7.0 (2017)

- **Tuples**: Hỗ trợ kiểu `tuple` giúp nhóm các giá trị lại với nhau mà không cần lớp riêng.

```csharp
var person = (Name: "John", Age: 30);
```

- **Pattern Matching**: Hỗ trợ kiểm tra kiểu và giá trị trong các biểu thức điều kiện.

```csharp
if (person is Person { Age: > 18 })
{
    Console.WriteLine("Adult");
}
```

- **Out Variables**: Biến `out` có thể được khai báo trực tiếp trong phương thức.

```csharp
if (int.TryParse("123", out int result)) { /*...*/ }
```

- **Local Functions**: Cho phép định nghĩa các hàm con bên trong hàm khác.

```csharp
void Local() { /*...*/ }
```

### Phiên bản 7.1, 7.2, 7.3

- **Enhanced Pattern Matching**: Cải thiện tính năng pattern matching với cú pháp mở rộng.

```csharp
public void PrintShape(object shape)
{
    if (shape is Circle { Radius: > 0 })
    {
        Console.WriteLine("This is a circle with a positive radius.");
    }
    else if (shape is Rectangle { Width: > 0, Height: > 0 })
    {
        Console.WriteLine("This is a rectangle with positive dimensions.");
    }
}
```

- **Async Main**: Cho phép phương thức `Main` có thể sử dụng `async`.

```csharp
using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args) // Phương thức Main bất đồng bộ
    {
        await Task.Delay(1000);
        Console.WriteLine("Hello after 1 second delay!");
    }
}
```

- **Default Literals**: Sử dụng từ khóa `default` cho các giá trị mặc định kiểu tổng quát.

```csharp
public void PrintDefaultValue(int x = default)
{
    Console.WriteLine(x); // Hiển thị "0" vì int mặc định là 0
}
```

---

### Phiên bản 8.0 (2019)

- **Nullable Reference Types**: Cải tiến xử lý kiểu nullable, giúp tránh lỗi null reference.

```csharp
string? nullableName = null;
```

- **Async Streams**: Cho phép sử dụng `await foreach` để lặp qua các dữ liệu bất đồng bộ.

```csharp
public async IAsyncEnumerable<int> GetNumbersAsync()
{
    yield return 1;
}
```

- **Indices and Ranges**: Hỗ trợ cú pháp lấy phần tử từ cuối mảng và truy xuất đoạn mảng.

```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
var last = numbers[^1];
```

- **Switch Expressions**: Giới thiệu cú pháp `switch` ngắn gọn hơn.

```csharp
string result = x switch { 1 => "One", _ => "Other" };
```

---

### Phiên bản 9.0 (2020)

- **Record Types**: Kiểu dữ liệu bất biến, thường dùng cho lưu trữ dữ liệu.

```csharp
public record Person(string Name, int Age);
```

- **Init-only Properties**: Cho phép thuộc tính chỉ có thể gán giá trị trong khối khởi tạo.

```csharp
public string Name { get; init; }
```

- **Top-level Statements**: Cho phép viết mã mà không cần hàm `Main`.

```csharp
Console.WriteLine("Hello, World!");
```

- **With Expressions**: Tạo bản sao của đối tượng với các thuộc tính được thay đổi.

```csharp
var person1 = new Person("John", 30);
var person2 = person1 with { Age = 31 };
```

---

### Phiên bản 10.0 (2021)

- **Global Using**: Khai báo `using` toàn cục cho toàn bộ mã nguồn.

```csharp
global using System;
```

- **File-scoped Namespaces**: Định nghĩa không gian tên cho toàn bộ tệp mã nguồn mà không cần dấu ngoặc.

```csharp
namespace MyNamespace;
```

- **Constant Interpolated Strings**: Hỗ trợ chuỗi nội suy được dùng làm hằng số.

```csharp
const string name = "World";
const string greeting = $"Hello, {name}!";
```

---

### Phiên bản 11.0 (2022)

- **Raw String Literals**: Cho phép viết chuỗi nhiều dòng mà không cần ký tự thoát.

```csharp
string text = """
    This is a raw
    string literal.
    """;
```

- **Required Members**: Yêu cầu các thuộc tính bắt buộc phải được gán giá trị khi khởi tạo.

```csharp
public class Car
{
    public required string Model { get; init; }
}
```

- **Generic Attributes**: Thuộc tính có thể sử dụng với kiểu tổng quát.

```csharp
[AttributeUsage(AttributeTargets.Class)]
public class MyAttribute<T> : Attribute { }
```

---

### Phiên bản 12.0 (2023)

- **Primary Constructors**: Cung cấp cú pháp gọn hơn cho việc khai báo constructor.

```csharp
public class Car(string model, int year) { }
```

- **Improved Interpolated Strings**: Hỗ trợ định dạng chuỗi nội suy mạnh mẽ hơn.

```csharp
var text = $"Car Model: {car.Model,10} Year: {car.Year}";
```

- **Collection Expressions**: Dễ dàng hơn trong việc khởi tạo các collection.

```csharp
var numbers = [1, 2, 3, 4];
```

- **Using Aliases**: Tăng cường khả năng đặt tên alias cho không gian tên và kiểu phức tạp.

```csharp
using ModelAlias = MyNamespace.Models.Car;
```

---

### Tóm Tắt

| Phiên bản | Các tính năng nổi bật                                 |
| --------- | ----------------------------------------------------- |
| 1.0       | Namespace, Classes, Interfaces, Delegates             |
| 2.0       | Generics, Nullable Types, Iterators                   |
| 3.0       | LINQ, Lambda, Anonymous Types                         |
| 4.0       | Dynamic Binding, Named & Optional Parameters          |
| 5.0       | Async & Await, Caller Information                     |
| 6.0       | Auto-Property Initializers, Expression-bodied Members |
| 7.0       | Tuples, Pattern Matching, Local Functions             |
| 8.0       | Nullable Reference Types, Async Streams               |
| 9.0       | Record Types, Init-only Properties, With Expressions  |
| 10.0      | Global Using, File-scoped Namespaces                  |
| 11.0      | Raw String Literals, Required Members                 |
| 12.0      | Primary Constructors, Improved Interpolated Strings   |

---

Trên đây là toàn bộ tài liệu về các tính năng của C# từ phiên bản 1.0 đến 12.0, hy vọng cung cấp được cái nhìn tổng quan và chi tiết về sự phát triển của ngôn ngữ này!
