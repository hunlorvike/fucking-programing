# Delegate trong C# .NET

## Mục Lục

1. [Tổng Quan về Delegate](#1-tổng-quan-về-delegate)
2. [Mục Đích của Delegate](#2-mục-đích-của-delegate)
3. [Các Loại Delegate trong C#](#3-các-loại-delegate-trong-c)
   - 3.1 [Delegate Đơn](#31-delegate-đơn)
   - 3.2 [Multicast Delegate](#32-multicast-delegate)
   - 3.3 [Func và Action Delegate](#33-func-và-action-delegate)
4. [Cú Pháp Khai Báo và Sử Dụng Delegate](#4-cú-pháp-khai-báo-và-sử-dụng-delegate)
5. [Multicast Delegate](#5-multicast-delegate)
6. [Func, Action, và Predicate Delegate](#6-func-action-và-predicate-delegate)
   - 6.1 [Func Delegate](#61-func-delegate)
   - 6.2 [Predicate Delegate](#62-predicate-delegate)
   - 6.3 [Action Delegate](#63-action-delegate)
7. [Anonymous Delegate](#7-anonymous-delegate)
8. [Delegate và Event](#8-delegate-và-event)
9. [Sự Khác Biệt Giữa Delegate và Interface](#9-sự-khác-biệt-giữa-delegate-và-interface)
10. [Tóm Tắt](#10-tóm-tắt)

## Phần nội dung bên dưới mỗi mục lục được liên kết đầy đủ với các mục cụ thể, giúp dễ dàng tra cứu hơn khi đọc tài liệu.

## 1. Tổng Quan về Delegate

**Delegate** trong C# là một kiểu dữ liệu tham chiếu đại diện cho một phương thức, cho phép lưu trữ và gọi các phương thức thông qua các biến delegate. Delegate giúp xử lý các phương thức như một tham số, giúp thực thi phương thức trong thời gian chạy một cách linh hoạt và giúp tăng khả năng mở rộng của mã nguồn.

---

## 2. Mục Đích của Delegate

- **Đại diện cho phương thức**: Delegate có thể chứa một hoặc nhiều phương thức và gọi chúng thông qua biến delegate.
- **Giảm độ phức tạp của mã nguồn**: Cho phép truyền phương thức như một tham số, giúp linh hoạt trong việc thiết kế mã.
- **Dễ dàng quản lý các sự kiện và callback**: Delegate đóng vai trò quan trọng trong việc xử lý sự kiện và callback trong C#.

---

## 3. Các Loại Delegate trong C#

### 3.1 Delegate Đơn

Delegate đơn chỉ chứa một phương thức tại một thời điểm.

### 3.2 Multicast Delegate

Multicast Delegate có thể chứa nhiều phương thức, cho phép gọi tất cả các phương thức đó trong một lần gọi.

### 3.3 Func và Action Delegate

`Func` và `Action` là những delegate tổng quát có sẵn trong .NET, giúp giảm bớt công việc khai báo delegate tùy chỉnh.

---

## 4. Cú Pháp Khai Báo và Sử Dụng Delegate

### Khai Báo Delegate

Delegate được khai báo bằng từ khóa `delegate` và định nghĩa loại trả về và danh sách tham số của nó.

**Ví dụ:**

```csharp
public delegate int Calculate(int x, int y); // Khai báo delegate
```

### Sử Dụng Delegate

```csharp
class Program
{
    public static int Add(int a, int b) => a + b;
    public static int Subtract(int a, int b) => a - b;

    static void Main()
    {
        Calculate calc = Add; // Gán phương thức vào delegate
        Console.WriteLine(calc(5, 3)); // Kết quả: 8

        calc = Subtract; // Thay đổi phương thức của delegate
        Console.WriteLine(calc(5, 3)); // Kết quả: 2
    }
}
```

---

## 5. Multicast Delegate

Multicast Delegate cho phép chứa và gọi nhiều phương thức. Khi delegate gọi một phương thức không trả về giá trị, tất cả các phương thức được thêm vào sẽ thực thi theo thứ tự.

**Ví dụ về Multicast Delegate:**

```csharp
public delegate void ShowMessage();

public static void Hello() => Console.WriteLine("Hello");
public static void Goodbye() => Console.WriteLine("Goodbye");

static void Main()
{
    ShowMessage message = Hello;
    message += Goodbye; // Thêm phương thức vào delegate
    message(); // In ra: Hello và Goodbye
}
```

---

Dưới đây là tài liệu đã được chỉnh sửa và bổ sung thêm các giải thích chi tiết cho từng loại delegate:

---

## 6. `Func`, `Action`, và `Predicate` Delegate trong C#

### 6.1. `Func` Delegate

`Func` là một loại delegate tổng quát (generic delegate) cho phép truyền vào các phương thức với kiểu trả về xác định. `Func` có thể nhận từ 0 đến 16 tham số, trong đó kiểu của tham số cuối cùng luôn là kiểu trả về của phương thức. `Func` là lựa chọn linh hoạt khi cần truyền các phương thức có kiểu trả về khác `void`.

- **Cú pháp:** `Func<T1, T2, ..., TResult>`
  - `T1`, `T2`, ... là các kiểu tham số.
  - `TResult` là kiểu trả về.

**Ví dụ về `Func`:**

```csharp
Func<int, int, int> add = (a, b) => a + b;
Console.WriteLine(add(3, 5)); // Kết quả: 8
```

Trong ví dụ trên:

- `Func<int, int, int>` định nghĩa một delegate nhận hai tham số `int` và trả về một `int`.
- `add` là một biểu thức lambda thực hiện phép cộng.

### 6.2. `Predicate` Delegate

`Predicate` là một dạng đặc biệt của `Func` trong C# được thiết kế để trả về kiểu `bool`. `Predicate` được sử dụng khi cần kiểm tra một điều kiện nào đó và trả về `true` hoặc `false` dựa trên kết quả kiểm tra. Delegate này chỉ nhận một tham số đầu vào, là kiểu dữ liệu cần kiểm tra.

- **Cú pháp:** `Predicate<T>`
  - `T` là kiểu của tham số.

**Ví dụ về `Predicate`:**

```csharp
int[] numbersArray = { 1, 2, 3, 4, 5, 6 };

// Kiểm tra xem có bất kỳ số nào lớn hơn 5 không
Predicate<int> isGreaterThanFive = number => number > 5;

bool exists = Array.Exists(numbersArray, isGreaterThanFive);

Console.WriteLine(exists); // Kết quả: True
```

Trong ví dụ trên:

- `Predicate<int>` định nghĩa một delegate nhận một tham số kiểu `int` và trả về `bool`.
- `isGreaterThanFive` là một biểu thức lambda kiểm tra xem giá trị có lớn hơn 5 không.

### 6.3. `Action` Delegate

`Action` là một loại delegate tổng quát không có kiểu trả về (`void`). `Action` có thể nhận từ 0 đến 16 tham số và thường được sử dụng cho các phương thức thực hiện thao tác nhưng không trả về kết quả.

- **Cú pháp:** `Action<T1, T2, ...>`
  - `T1`, `T2`, ... là các kiểu tham số.

**Ví dụ về `Action`:**

```csharp
Action<string> print = message => Console.WriteLine(message);
print("Hello World"); // Kết quả: Hello World
```

Trong ví dụ trên:

- `Action<string>` định nghĩa một delegate nhận một tham số kiểu `string`.
- `print` là một biểu thức lambda dùng để in chuỗi ra màn hình.

## 7. Anonymous Delegate (Delegate Vô Danh)

**Anonymous Delegate** là một delegate không có tên, được khai báo trực tiếp trong mã mà không cần phải định nghĩa một phương thức riêng. Cách viết này giúp mã ngắn gọn hơn khi không cần sử dụng delegate ở nhiều nơi. Anonymous delegate có thể được khai báo bằng từ khóa `delegate`.

**Ví dụ về Anonymous Delegate:**

```csharp
// Định nghĩa một delegate tên Calculate
delegate int Calculate(int a, int b);

Calculate calc = delegate (int a, int b)
{
    return a + b;
};
Console.WriteLine(calc(3, 4)); // Kết quả: 7
```

Trong ví dụ trên:

- `Calculate` là một delegate nhận hai tham số kiểu `int` và trả về `int`.
- Anonymous delegate được gán vào `calc` để thực hiện phép cộng hai số.

Anonymous delegate cho phép viết mã một cách ngắn gọn khi không cần đặt tên phương thức, đặc biệt hữu ích khi chỉ cần gọi delegate một lần hoặc làm đối số cho một phương thức khác.

---

Các loại delegate như `Func`, `Predicate`, và `Action` giúp mã nguồn linh hoạt và dễ đọc hơn, đồng thời cho phép lập trình viên tận dụng các phương thức như tham số, giúp cải thiện cấu trúc mã và khả năng tái sử dụng trong các ứng dụng C#.

## 8. Delegate và Event

Delegate đóng vai trò nền tảng trong việc khai báo và sử dụng event trong C#. Event là một cơ chế thông báo cho các thành phần khác về các sự kiện xảy ra trong ứng dụng.

**Ví dụ về Event sử dụng Delegate:**

```csharp
public delegate void Notify(); // Khai báo delegate

public class Process
{
    public event Notify ProcessCompleted; // Khai báo event

    public void StartProcess()
    {
        Console.WriteLine("Processing...");
        ProcessCompleted?.Invoke(); // Kích hoạt event
    }
}

public class Program
{
    static void Main()
    {
        Process process = new Process();
        process.ProcessCompleted += () => Console.WriteLine("Process Completed!"); // Đăng ký event
        process.StartProcess();
    }
}
```

---

## 9. Sự Khác Biệt Giữa Delegate và Interface

| Tiêu chí            | Delegate                                     | Interface                                              |
| ------------------- | -------------------------------------------- | ------------------------------------------------------ |
| **Mục đích**        | Đại diện cho một phương thức cụ thể          | Định nghĩa các hành vi mà lớp cần thực hiện            |
| **Linh hoạt**       | Có thể chứa nhiều phương thức                | Yêu cầu lớp triển khai các phương thức được định nghĩa |
| **Sử dụng chính**   | Xử lý callback, event                        | Kế thừa và mở rộng lớp                                 |
| **Tính năng chính** | Cho phép truyền và gọi phương thức linh hoạt | Bắt buộc lớp thực thi các phương thức đã khai báo      |

---

## 10. Tóm Tắt

1. **Delegate**: Là kiểu dữ liệu tham chiếu đại diện cho phương thức, cho phép xử lý phương thức như một đối tượng.
2. **Multicast Delegate**: Cho phép delegate chứa nhiều phương thức, có thể gọi tất cả trong một lần.
3. **Func và Action**: Delegate tổng quát có sẵn trong .NET, giảm bớt việc khai báo delegate tùy chỉnh.
4. **Anonymous Delegate**: Delegate không tên, giúp đơn giản hóa mã nguồn.
5. **Delegate và Event**: Delegate là cơ sở để định nghĩa các event, giúp ứng dụng linh hoạt trong việc xử lý sự kiện.

Delegate là một tính năng mạnh mẽ và linh hoạt trong C#, giúp đơn giản hóa việc gọi các phương thức linh hoạt và xử lý callback, đồng thời đóng vai trò quan trọng trong lập trình sự kiện trong .NET.
