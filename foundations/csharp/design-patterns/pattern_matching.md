# Pattern Matching trong C#

## Mục Lục

1. [Tổng Quan về Pattern Matching](#1-tổng-quan-về-pattern-matching)

    - [Mục Đích](#mục-đích)
    - [Lịch Sử Phát Triển](#lịch-sử-phát-triển)

2. [Các Loại Pattern Matching trong C#](#2-các-loại-pattern-matching-trong-c)

    - [a. Type Pattern](#a-type-pattern)
    - [b. Constant Pattern](#b-constant-pattern)
    - [c. Relational Pattern](#c-relational-pattern)
    - [d. Logical Pattern](#d-logical-pattern)
    - [e. Property Pattern](#e-property-pattern)
    - [f. Positional Pattern](#f-positional-pattern)

3. [Ứng Dụng Pattern Matching](#3-ứng-dụng-pattern-matching)

    - [a. Sử Dụng với Switch Expression](#a-sử-dụng-với-switch-expression)
    - [b. Sử Dụng với Toán Tử `is`](#b-sử-dụng-với-toán-tử-is)

4. [Ưu Điểm và Nhược Điểm](#4-ưu-điểm-và-nhược-điểm)

5. [Tóm Tắt](#5-tóm-tắt)

---

### 1. Tổng Quan về Pattern Matching

**Pattern Matching** là một tính năng trong C# cho phép bạn kiểm tra và xử lý dữ liệu dựa trên hình mẫu (pattern). Nó
giúp mã nguồn ngắn gọn, dễ đọc và giảm thiểu các câu lệnh điều kiện lồng nhau.

#### Mục Đích

- **Đơn Giản Hóa Xử Lý Dữ Liệu**: Giảm thiểu việc sử dụng các câu lệnh `if-else` hoặc `switch` phức tạp.
- **Cải Thiện Tính Bảo Trì**: Giúp mã nguồn dễ hiểu hơn bằng cách tập trung vào các điều kiện cụ thể của dữ liệu.
- **Hỗ Trợ Kiểm Tra Kiểu Dữ Liệu**: Giúp làm việc dễ dàng hơn với các kiểu dữ liệu phức tạp.

#### Lịch Sử Phát Triển

- **C# 7.0**: Giới thiệu các tính năng cơ bản như Type Pattern và Constant Pattern.
- **C# 8.0**: Bổ sung Switch Expression và Property Pattern.
- **C# 9.0**: Thêm Relational Pattern, Logical Pattern và Positional Pattern.

---

### 2. Các Loại Pattern Matching trong C#

Pattern Matching trong C# được phân thành nhiều loại dựa trên cách thức và mục đích sử dụng.

#### a. Type Pattern

Kiểm tra kiểu dữ liệu và gán giá trị nếu đúng kiểu.

```csharp
object obj = "Hello, World!";

if (obj is string str)
{
    Console.WriteLine($"Độ dài chuỗi: {str.Length}");
}
```

#### b. Constant Pattern

So sánh giá trị với một hằng số cụ thể.

```csharp
int number = 42;

if (number is 42)
{
    Console.WriteLine("Giá trị là 42.");
}
```

#### c. Relational Pattern

Kiểm tra mối quan hệ của một giá trị với một ngưỡng nhất định.

```csharp
int age = 25;

if (age is > 18 and < 30)
{
    Console.WriteLine("Độ tuổi trong khoảng 18 đến 30.");
}
```

#### d. Logical Pattern

Kết hợp các điều kiện kiểm tra với các toán tử logic như `and`, `or`, và `not`.

```csharp
int number = 15;

if (number is > 0 and < 20)
{
    Console.WriteLine("Số nằm trong khoảng 0 đến 20.");
}
```

#### e. Property Pattern

Kiểm tra giá trị của các thuộc tính trong một đối tượng.

```csharp
var person = new { Name = "Alice", Age = 25 };

if (person is { Name: "Alice", Age: > 20 })
{
    Console.WriteLine("Alice lớn hơn 20 tuổi.");
}
```

#### f. Positional Pattern

Kiểm tra giá trị của các thành phần trong một đối tượng, đặc biệt hữu ích với các `tuple` hoặc `record`.

```csharp
var point = (X: 1, Y: 2);

if (point is (1, 2))
{
    Console.WriteLine("Điểm nằm tại (1, 2).");
}
```

---

### 3. Ứng Dụng Pattern Matching

#### a. Sử Dụng với Switch Expression

`Switch Expression` là một cách ngắn gọn để thay thế câu lệnh `switch` truyền thống.

```csharp
string GetDayType(int day) => day switch
{
    1 => "Thứ Hai",
    2 => "Thứ Ba",
    3 => "Thứ Tư",
    _ => "Ngày không hợp lệ"
};
```

#### b. Sử Dụng với Toán Tử `is`

Toán tử `is` được sử dụng để kiểm tra và gán kiểu dữ liệu trong cùng một biểu thức.

```csharp
void Print(object obj)
{
    if (obj is string str)
    {
        Console.WriteLine($"Chuỗi: {str}");
    }
    else if (obj is int number)
    {
        Console.WriteLine($"Số: {number}");
    }
}
```

---

### 4. Ưu Điểm và Nhược Điểm

#### Ưu Điểm

- **Ngắn Gọn và Dễ Hiểu**: Mã nguồn trở nên đơn giản hơn khi xử lý các điều kiện phức tạp.
- **Giảm Thiểu Lỗi**: Tăng độ an toàn khi làm việc với các kiểu dữ liệu.
- **Tăng Tính Linh Hoạt**: Hỗ trợ nhiều cách xử lý dữ liệu khác nhau trong cùng một biểu thức.

#### Nhược Điểm

- **Đòi Hỏi Hiểu Biết Sâu**: Người lập trình cần nắm rõ cú pháp và tính năng mới của C#.
- **Không Tương Thích Ngược**: Một số tính năng chỉ hoạt động từ các phiên bản C# mới.

---

### 5. Tóm Tắt

Pattern Matching là một tính năng mạnh mẽ giúp tối ưu hóa mã nguồn trong C#. Nó cung cấp nhiều loại hình mẫu (pattern)
để kiểm tra và xử lý dữ liệu một cách linh hoạt và dễ hiểu.

**Các điểm chính:**

- **Type Pattern và Constant Pattern**: Cơ bản nhất, kiểm tra kiểu và giá trị.
- **Relational và Logical Pattern**: Hỗ trợ điều kiện phức tạp.
- **Property và Positional Pattern**: Tối ưu hóa kiểm tra thuộc tính và cấu trúc dữ liệu.
- **Switch Expression**: Rút gọn và làm rõ logic xử lý.

Sử dụng Pattern Matching đúng cách sẽ cải thiện đáng kể hiệu suất và tính rõ ràng của ứng dụng C#.
