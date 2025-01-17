# Extension Methods trong C#

## Mục Lục

1. [Tổng Quan về Extension Methods](#1-tổng-quan-về-extension-methods)

    - [Mục Đích](#mục-đích)
    - [Cách Hoạt Động](#cách-hoạt-động)

2. [Cách Tạo Extension Methods](#2-cách-tạo-extension-methods)

3. [Quy Tắc Viết Extension Methods](#3-quy-tắc-viết-extension-methods)

4. [Ví Dụ Sử Dụng Extension Methods](#4-ví-dụ-sử-dụng-extension-methods)

    - [a. Mở Rộng Kiểu Dữ Liệu Chuỗi](#a-mở-rộng-kiểu-dữ-liệu-chuỗi)
    - [b. Mở Rộng Kiểu Dữ Liệu Số](#b-mở-rộng-kiểu-dữ-liệu-số)
    - [c. Mở Rộng Lớp Người Dùng](#c-mở-rộng-lớp-người-dùng)

5. [Ưu Điểm và Nhược Điểm](#5-ưu-điểm-và-nhược-điểm)

6. [Tóm Tắt](#6-tóm-tắt)

---

### 1. Tổng Quan về Extension Methods

**Extension Methods** (Phương thức mở rộng) là một tính năng trong C# cho phép bạn thêm các phương thức mới vào một lớp
hoặc interface hiện có mà không cần phải sửa đổi mã nguồn của nó hoặc tạo một lớp kế thừa. Điều này giúp bạn mở rộng khả
năng của các lớp hiện có mà không làm ảnh hưởng đến tính toàn vẹn của mã gốc.

#### Mục Đích

- **Tăng Tính Linh Hoạt**: Cho phép thêm các phương thức tiện ích mà không cần thay đổi mã nguồn của lớp gốc.
- **Đơn Giản Hóa Mã Nguồn**: Giảm bớt sự lặp lại bằng cách cung cấp các phương thức tái sử dụng được cho các lớp hiện
  có.
- **Cải Thiện Tính Đọc Hiểu**: Làm cho mã dễ đọc và gần gũi hơn với ngôn ngữ tự nhiên.

#### Cách Hoạt Động

- Extension Methods thực chất là các phương thức tĩnh, nhưng chúng được "gắn" vào các lớp hiện có nhờ từ khóa `this`.
- Khi sử dụng, chúng xuất hiện giống như các phương thức thành viên của lớp đó.

Ví dụ: Thay vì gọi một phương thức như sau:

```csharp
StringHelper.ToUppercase("hello");
```

Bạn có thể gọi trực tiếp trên đối tượng chuỗi:

```csharp
"hello".ToUppercase();
```

---

### 2. Cách Tạo Extension Methods

Extension Methods được khai báo trong một lớp tĩnh (static class). Dưới đây là cú pháp cơ bản:

```csharp
public static class MyExtensions
{
    public static string ToUppercase(this string input)
    {
        return input.ToUpper();
    }
}
```

- **Từ khóa `this`**: Là tham số đầu tiên của phương thức, chỉ định đối tượng mà phương thức sẽ mở rộng.

---

### 3. Quy Tắc Viết Extension Methods

1. **Lớp Chứa Phải Là Static**: Extension Methods phải được khai báo trong một lớp tĩnh.
2. **Phương Thức Phải Là Static**: Phương thức mở rộng phải là phương thức tĩnh.
3. **Tham Số Đầu Tiên Phải Có Từ Khóa `this`**: Tham số đầu tiên xác định lớp hoặc kiểu dữ liệu mà phương thức sẽ mở
   rộng.
4. **Không Thay Thế Được Phương Thức Có Sẵn**: Nếu lớp đã có phương thức trùng tên, phương thức của lớp sẽ được ưu tiên
   sử dụng.

---

### 4. Ví Dụ Sử Dụng Extension Methods

#### a. Mở Rộng Kiểu Dữ Liệu Chuỗi

Thêm phương thức để kiểm tra xem một chuỗi có phải là chuỗi số hay không:

```csharp
public static class StringExtensions
{
    public static bool IsNumeric(this string input)
    {
        return int.TryParse(input, out _);
    }
}

// Sử dụng
string value = "123";
bool isNumeric = value.IsNumeric(); // Kết quả: true
```

#### b. Mở Rộng Kiểu Dữ Liệu Số

Thêm phương thức để tính bình phương của một số:

```csharp
public static class NumberExtensions
{
    public static int Square(this int number)
    {
        return number * number;
    }
}

// Sử dụng
int value = 5;
int squared = value.Square(); // Kết quả: 25
```

#### c. Mở Rộng Lớp Người Dùng

Mở rộng lớp `User` để kiểm tra xem người dùng có phải là quản trị viên hay không:

```csharp
public class User
{
    public string Name { get; set; }
    public bool IsAdmin { get; set; }
}

public static class UserExtensions
{
    public static bool IsAdministrator(this User user)
    {
        return user.IsAdmin;
    }
}

// Sử dụng
User user = new User { Name = "Alice", IsAdmin = true };
bool isAdmin = user.IsAdministrator(); // Kết quả: true
```

---

### 5. Ưu Điểm và Nhược Điểm

#### Ưu Điểm

- **Dễ Sử Dụng**: Tạo các phương thức tiện ích mà không cần thay đổi lớp gốc.
- **Tái Sử Dụng Cao**: Phương thức mở rộng có thể được áp dụng cho bất kỳ kiểu nào, miễn là phù hợp.
- **Không Làm Ảnh Hưởng Đến Mã Nguồn Gốc**: Không cần kế thừa hoặc sửa đổi lớp gốc.

#### Nhược Điểm

- **Khó Theo Dõi**: Với những dự án lớn, việc tìm kiếm các Extension Methods áp dụng cho một lớp cụ thể có thể khó khăn.
- **Ưu Tiên Thấp Hơn Phương Thức Nội Tại**: Nếu lớp gốc đã có phương thức trùng tên, Extension Methods sẽ không được
  gọi.
- **Dễ Lạm Dụng**: Có thể dẫn đến việc thêm quá nhiều Extension Methods không cần thiết, làm mã phức tạp hơn.

---

### 6. Tóm Tắt

Extension Methods là một tính năng mạnh mẽ của C#, giúp mở rộng các lớp và kiểu dữ liệu có sẵn mà không cần thay đổi mã
nguồn gốc. Điều này giúp tăng tính tái sử dụng và đơn giản hóa mã. Tuy nhiên, việc sử dụng Extension Methods cần tuân
thủ các quy tắc và phải cân nhắc để tránh lạm dụng.

**Các điểm chính:**

- Extension Methods phải được khai báo trong một lớp tĩnh.
- Tham số đầu tiên phải được định nghĩa với từ khóa `this`.
- Nên sử dụng Extension Methods để cung cấp các phương thức tiện ích có ý nghĩa cho kiểu dữ liệu hoặc lớp cụ thể.

Extension Methods là công cụ lý tưởng để cải thiện hiệu quả và sự rõ ràng trong phát triển phần mềm với C#.
