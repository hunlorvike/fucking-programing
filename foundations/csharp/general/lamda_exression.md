# Lambda Expressions trong C# .NET

## Mục Lục

1. [Tổng Quan về Lambda Expressions](#1-tổng-quan-về-lambda-expressions)
2. [Mục Đích và Lợi Ích của Lambda Expressions](#2-mục-đích-và-lợi-ích-của-lambda-expressions)
3. [Cú Pháp Lambda Expressions](#3-cú-pháp-lambda-expressions)
4. [Lambda Expressions với Các Delegate](#4-lambda-expressions-với-các-delegate)
5. [Lambda Expressions với LINQ](#5-lambda-expressions-với-linq)
6. [Lambda Expressions và Expression Trees](#6-lambda-expressions-và-expression-trees)
7. [Sử Dụng Lambda trong Các Phương Thức Anon](#7-sử-dụng-lambda-trong-các-phương-thức-anonymous)
8. [Các Hạn Chế và Lưu Ý Khi Sử Dụng Lambda Expressions](#8-các-hạn-chế-và-lưu-ý-khi-sử-dụng-lambda-expressions)
9. [Tóm Tắt](#9-tóm-tắt)
10. [So Sánh Lambda Expressions và Các Phương Pháp Khác](#10-so-sánh-lambda-expressions-và-các-phương-pháp-khác)

## 1. Tổng Quan về Lambda Expressions

**Lambda Expressions** trong C# là một cách viết ngắn gọn để định nghĩa các hàm vô danh (anonymous functions) nhằm truyền hành vi của hàm dưới dạng các biểu thức ngắn gọn. Lambda Expressions rất hữu ích khi bạn muốn tạo ra các hàm nhanh chóng và gọn nhẹ cho các thao tác như lọc, sắp xếp, hoặc xử lý danh sách dữ liệu trong LINQ.

## 2. Mục Đích và Lợi Ích của Lambda Expressions

- **Đơn giản hóa cú pháp**: Lambda Expressions giúp giảm thiểu số lượng mã cần viết, làm cho mã ngắn gọn và dễ đọc hơn.
- **Lập trình chức năng (Functional Programming)**: Cho phép xử lý dữ liệu bằng cách truyền các hàm, tạo ra các đoạn mã có tính modular và tái sử dụng cao.
- **LINQ và Data Processing**: Hỗ trợ LINQ và các thao tác xử lý dữ liệu với danh sách, tập hợp dữ liệu một cách hiệu quả.

## 3. Cú Pháp Lambda Expressions

Lambda Expressions có hai phần: danh sách tham số và biểu thức.

```csharp
(parameters) => expression
```

- **Một biểu thức đơn giản**: Đối với các thao tác ngắn gọn.

  ```csharp
  x => x * x
  ```

- **Khối mã nhiều dòng**: Đối với các biểu thức phức tạp hơn.

  ```csharp
  (x, y) =>
  {
      int result = x + y;
      return result;
  }
  ```

**Ví dụ:**

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
var evenNumbers = numbers.Where(n => n % 2 == 0).ToList(); // Lọc số chẵn
```

## 4. Lambda Expressions với Các Delegate

Lambda Expressions có thể gán trực tiếp cho các delegate như `Func`, `Action`, và `Predicate`.

- **`Func`**: Delegate có trả về giá trị.
- **`Action`**: Delegate không trả về giá trị.
- **`Predicate`**: Delegate nhận vào một tham số và trả về `bool`.

**Ví dụ:**

```csharp
Func<int, int, int> add = (a, b) => a + b;
Action<string> printMessage = message => Console.WriteLine(message);
Predicate<int> isEven = num => num % 2 == 0;

Console.WriteLine(add(2, 3)); // Output: 5
printMessage("Hello, Lambda!"); // Output: Hello, Lambda!
Console.WriteLine(isEven(4)); // Output: True
```

## 5. Lambda Expressions với LINQ

Lambda Expressions được sử dụng phổ biến trong LINQ (Language Integrated Query) để xử lý và truy vấn dữ liệu trong các tập hợp.

**Ví dụ:**

```csharp
var numbers = new List<int> { 1, 2, 3, 4, 5 };
var squaredNumbers = numbers.Select(n => n * n).ToList();
```

- **`Select`**: Biến đổi từng phần tử trong tập hợp.
- **`Where`**: Lọc phần tử dựa trên điều kiện.
- **`OrderBy` và `OrderByDescending`**: Sắp xếp tập hợp.

## 6. Lambda Expressions và Expression Trees

Expression Trees cho phép biểu diễn các Lambda Expressions dưới dạng cây biểu thức (`Expression<Func<T, TResult>>`). Điều này rất hữu ích khi làm việc với Entity Framework hoặc các thư viện yêu cầu cấu trúc của biểu thức thay vì kết quả trả về.

**Ví dụ:**

```csharp
Expression<Func<int, bool>> isGreaterThanFive = num => num > 5;
```

Expression Trees cho phép C# dịch Lambda Expressions thành cây biểu thức, nhờ đó có thể phân tích và biên dịch biểu thức khi truy vấn dữ liệu, như với Entity Framework.

## 7. Sử Dụng Lambda trong Các Phương Thức Anonymous

Lambda Expressions có thể được sử dụng trong các phương thức vô danh hoặc inline. Điều này rất hữu ích trong các sự kiện hoặc callback.

**Ví dụ:**

```csharp
Button myButton = new Button();
myButton.Click += (sender, e) =>
{
    Console.WriteLine("Button clicked!");
};
```

Trong ví dụ này, Lambda Expression `(sender, e) => { ... }` được dùng để định nghĩa một hàm xử lý sự kiện `Click`.

## 8. Các Hạn Chế và Lưu Ý Khi Sử Dụng Lambda Expressions

- **Khó hiểu với mã phức tạp**: Nếu Lambda Expression chứa quá nhiều logic, mã có thể khó đọc và khó bảo trì.
- **Không có khai báo kiểu rõ ràng**: Lambda tự suy luận kiểu dữ liệu, điều này có thể gây nhầm lẫn khi phân tích mã.
- **Expression Trees có giới hạn**: Expression Trees chỉ hỗ trợ một tập hợp hạn chế các thao tác (vì vậy các biểu thức quá phức tạp có thể không được hỗ trợ).

## 9. Tóm Tắt

1. **Cú pháp Lambda Expression**:
   - Cú pháp ngắn gọn, dễ hiểu, phù hợp với các thao tác nhỏ, đơn giản.
2. **Delegate**:
   - Có thể gán Lambda Expressions cho các delegate `Func`, `Action`, và `Predicate`.
3. **LINQ**:
   - Lambda Expressions rất hữu ích cho LINQ trong việc xử lý và truy vấn dữ liệu.
4. **Expression Trees**:
   - Biểu diễn Lambda Expressions dưới dạng cây biểu thức, hữu ích khi tương tác với các thư viện như Entity Framework.

## 10. So Sánh Lambda Expressions và Các Phương Pháp Khác

### 1. Delegate vs Lambda Expressions

| Tiêu chí                 | Delegate                              | Lambda Expressions                 |
| ------------------------ | ------------------------------------- | ---------------------------------- |
| **Cú pháp**              | Phức tạp hơn                          | Ngắn gọn và dễ hiểu                |
| **Khả năng tái sử dụng** | Tốt hơn trong các trường hợp phức tạp | Dễ dàng nhưng nên giới hạn mã ngắn |
| **Tương thích với LINQ** | Không phổ biến                        | Rất phổ biến                       |

### 2. Phương thức truyền thống vs Lambda Expressions

| Tiêu chí              | Phương thức truyền thống         | Lambda Expressions             |
| --------------------- | -------------------------------- | ------------------------------ |
| **Cú pháp**           | Chi tiết, đầy đủ                 | Ngắn gọn và dễ viết            |
| **Độ rõ ràng**        | Rõ ràng cho các đoạn mã phức tạp | Có thể khó đọc với mã phức tạp |
| **Ứng dụng với LINQ** | Khó sử dụng                      | Phổ biến và dễ tích hợp        |

### 3. Kết Luận

Lambda Expressions giúp mã ngắn gọn và dễ hiểu trong các trường hợp đơn giản. Với các thao tác phức tạp hoặc yêu cầu tính rõ ràng cao, nên cân nhắc sử dụng các phương pháp khác để dễ dàng kiểm soát mã nguồn.

Lambda Expressions đặc biệt hiệu quả trong lập trình LINQ, xử lý dữ liệu và callback, giúp tăng khả năng đọc và bảo trì mã trong C# .NET.
