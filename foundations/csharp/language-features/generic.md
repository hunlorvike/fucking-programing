# Tổng Quan về Generics và Generic Constraints trong C# .NET

## Mục Lục

1. [Giới thiệu về Generics](#1-giới-thiệu-về-generics)
    - [Generics là gì?](#generics-là-gì)
    - [Lợi ích của Generics](#lợi-ích-của-generics)
2. [Cách sử dụng Generics trong C#](#2-cách-sử-dụng-generics-trong-c)
    - [Lớp Generic](#lớp-generic)
    - [Phương thức Generic](#phương-thức-generic)
    - [Interface Generic](#interface-generic)
3. [Generic Constraints](#3-generic-constraints)
    - [Generic Constraints là gì?](#generic-constraints-là-gì)
    - [Các loại Generic Constraints](#các-loại-generic-constraints)
4. [Sử dụng Generics với Collection](#4-sử-dụng-generics-với-collection)
    - [Các lớp Generic Collection phổ biến](#các-lớp-generic-collection-phổ-biến)
    - [So sánh Generic Collection và Non-Generic Collection](#so-sánh-generic-collection-và-non-generic-collection)
5. [Ưu và Nhược điểm của Generics](#5-ưu-và-nhược-điểm-của-generics)
    - [Ưu điểm](#ưu-điểm)
    - [Nhược điểm](#nhược-điểm)
6. [Kết luận](#6-kết-luận)

---

### 1. Giới thiệu về Generics

#### Generics là gì?

Generics là một tính năng trong C# cho phép bạn định nghĩa các lớp, phương thức, delegate, hoặc interface mà không cần
xác định cụ thể kiểu dữ liệu tại thời điểm thiết kế. Generics cung cấp một cách tiếp cận linh hoạt để tái sử dụng mã
nguồn, giúp giảm lỗi và tối ưu hóa hiệu suất.

Ví dụ cơ bản về Generics:

```csharp
public class GenericClass<T>
{
    public T Value { get; set; }
}
```

#### Lợi ích của Generics

- **Tăng tính tái sử dụng mã**: Viết mã một lần và áp dụng cho nhiều kiểu dữ liệu khác nhau.
- **Giảm lỗi kiểu dữ liệu**: Kiểm tra kiểu dữ liệu tại thời điểm biên dịch thay vì runtime.
- **Hiệu suất cao hơn**: Tránh boxing/unboxing khi làm việc với các kiểu dữ liệu giá trị.
- **Đơn giản hóa mã nguồn**: Tránh phải viết lặp lại mã cho các kiểu dữ liệu khác nhau.

---

### 2. Cách sử dụng Generics trong C#

#### Lớp Generic

Lớp Generic cho phép định nghĩa một lớp mà kiểu dữ liệu có thể được xác định tại thời điểm sử dụng.

```csharp
public class GenericClass<T>
{
    public T Data { get; set; }
    public void Display()
    {
        Console.WriteLine($"Data: {Data}");
    }
}

// Sử dụng lớp Generic
var intInstance = new GenericClass<int> { Data = 10 };
var stringInstance = new GenericClass<string> { Data = "Hello" };
```

#### Phương thức Generic

Phương thức Generic cho phép định nghĩa một phương thức với kiểu dữ liệu được quyết định tại thời điểm gọi.

```csharp
public void Swap<T>(ref T a, ref T b)
{
    T temp = a;
    a = b;
    b = temp;
}

// Sử dụng phương thức Generic
int x = 5, y = 10;
Swap(ref x, ref y);
```

#### Interface Generic

Interface Generic cho phép định nghĩa các giao diện với kiểu dữ liệu không cố định.

```csharp
public interface IRepository<T>
{
    void Add(T item);
    T Get(int id);
}

public class Repository<T> : IRepository<T>
{
    private List<T> items = new List<T>();
    public void Add(T item) => items.Add(item);
    public T Get(int id) => items[id];
}
```

---

### 3. Generic Constraints

#### Generic Constraints là gì?

Generic Constraints (ràng buộc kiểu) được sử dụng để giới hạn các kiểu dữ liệu có thể được sử dụng trong Generics. Điều
này giúp đảm bảo rằng kiểu dữ liệu phù hợp với các yêu cầu của chương trình.

#### Các loại Generic Constraints

1. **`where T : struct`**
    - Ràng buộc kiểu phải là kiểu giá trị (value type).
    - Ví dụ: `int`, `float`, `DateTime`.
   ```csharp
   public void ProcessValue<T>(T value) where T : struct
   {
       Console.WriteLine(value);
   }
   ```

2. **`where T : class`**
    - Ràng buộc kiểu phải là kiểu tham chiếu (reference type).
    - Ví dụ: `string`, `List<T>`.
   ```csharp
   public void ProcessReference<T>(T value) where T : class
   {
       Console.WriteLine(value);
   }
   ```

3. **`where T : new()`**
    - Ràng buộc kiểu phải có constructor không tham số.
   ```csharp
   public T CreateInstance<T>() where T : new()
   {
       return new T();
   }
   ```

4. **`where T : BaseClass`**
    - Ràng buộc kiểu phải kế thừa từ một lớp cụ thể.
   ```csharp
   public void Process<T>(T value) where T : MyBaseClass
   {
       value.Display();
   }
   ```

5. **`where T : Interface`**
    - Ràng buộc kiểu phải triển khai một interface cụ thể.
   ```csharp
   public void Process<T>(T value) where T : IDisposable
   {
       value.Dispose();
   }
   ```

---

### 4. Sử dụng Generics với Collection

#### Các lớp Generic Collection phổ biến

1. **`List<T>`**
    - Danh sách các đối tượng kiểu `T`.
   ```csharp
   List<int> numbers = new List<int> { 1, 2, 3 };
   ```

2. **`Dictionary<TKey, TValue>`**
    - Lưu trữ các cặp khóa-giá trị.
   ```csharp
   Dictionary<int, string> students = new Dictionary<int, string>
   {
       { 1, "John" },
       { 2, "Jane" }
   };
   ```

3. **`Queue<T>` và `Stack<T>`**
    - Lớp Queue: hàng đợi FIFO.
    - Lớp Stack: ngăn xếp LIFO.
   ```csharp
   Queue<string> queue = new Queue<string>();
   queue.Enqueue("Task1");

   Stack<int> stack = new Stack<int>();
   stack.Push(10);
   ```

#### So sánh Generic Collection và Non-Generic Collection

| **Tiêu chí**          | **Generic Collection**                 | **Non-Generic Collection**       |
|-----------------------|----------------------------------------|----------------------------------|
| **Kiểm tra kiểu**     | Thực hiện tại thời điểm biên dịch.     | Thực hiện tại thời điểm runtime. |
| **Hiệu suất**         | Tốt hơn, không cần boxing/unboxing.    | Thấp hơn do boxing/unboxing.     |
| **Tính an toàn kiểu** | Cao hơn, giảm lỗi do sai kiểu dữ liệu. | Thấp hơn, dễ xảy ra lỗi runtime. |

---

### 5. Ưu và Nhược điểm của Generics

#### Ưu điểm

- Tăng khả năng tái sử dụng mã nguồn.
- Cải thiện hiệu suất khi làm việc với kiểu dữ liệu giá trị.
- Giảm lỗi và tăng tính an toàn kiểu trong mã nguồn.
- Đơn giản hóa quá trình quản lý dữ liệu với các collection.

#### Nhược điểm

- Tăng độ phức tạp của mã nguồn đối với người mới học.
- Không hỗ trợ cho các kiểu dữ liệu không tương thích với ràng buộc.

---

### 6. Kết luận

Generics là một công cụ mạnh mẽ trong C#, giúp tăng tính linh hoạt, hiệu suất và an toàn cho mã nguồn. Việc sử dụng đúng
cách Generics và Generic Constraints không chỉ giúp tối ưu hóa hiệu suất mà còn làm cho mã nguồn dễ bảo trì hơn. Tuy
nhiên, lập trình viên cần nắm rõ các khái niệm cơ bản và áp dụng chúng một cách hợp lý trong từng tình huống cụ thể.
