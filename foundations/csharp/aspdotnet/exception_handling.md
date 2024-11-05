# Ngoại lệ (Exception) trong C# .NET

## Mục lục

1. [Ngoại lệ (Exception) là gì?](#1-nh-ngoai-l-n-exception-l-g)
2. [Hệ thống cấp bậc của các lớp ngoại lệ trong C# .NET](#2-h-s-th-m-c-p-b-c-c-l-s-ngoai-l-trong-c-net)
3. [Các kịch bản phổ biến nơi ngoại lệ có thể xảy ra](#3-c-k-ch-b-n-ph-phi-n-n-ngoai-l-c-th-s-x-ra)
4. [Xử lý ngoại lệ (Exception Handling) trong C# .NET](#4-x-l-ngoai-l-exception-handling-trong-c-net)
   - [try - catch - finally](#try---catch---finally)
   - [throw - Ném Ngoại Lệ](#throw---n-m-ngoai-l)
   - [Các loại Ngoại Lệ Thông Dụng](#c-loi-ngoai-l-th-ng-d-ng)
   - [Tạo Ngoại Lệ Tùy Chỉnh (Custom Exception)](#t-o-ngoai-l-tuy-ch-n-custom-exception)
   - [Sử dụng when trong catch](#s-d-ng-when-trong-catch)
   - [Global Exception Handling](#global-exception-handling)
   - [Logging](#logging)
5. [Tóm tắt](#5-t-m-t)

### 1. Ngoại lệ (Exception) là gì?

Ngoại lệ là một sự kiện không mong muốn xảy ra trong quá trình thực thi chương trình, khiến mã không thể tiếp tục thực hiện bình thường. Các ngoại lệ thường là lỗi có thể dự đoán trước như lỗi phân chia cho 0, lỗi truy cập chỉ số mảng vượt quá phạm vi, hay lỗi gọi phương thức trên đối tượng `null`. Trong .NET, các ngoại lệ được thể hiện bằng lớp `Exception`.

### 2. Hệ thống cấp bậc của các lớp ngoại lệ trong C# .NET

.NET có hệ thống phân cấp lớp ngoại lệ, với `System.Exception` là lớp cơ sở. Các lớp ngoại lệ con của `Exception` cung cấp các lỗi đặc thù hơn. Cấp bậc này cho phép xử lý ngoại lệ chi tiết hơn:

- **System.Exception**: Lớp cơ sở của tất cả các ngoại lệ.
  - **System.SystemException**: Lớp cơ bản của các ngoại lệ hệ thống như `ArgumentException`, `NullReferenceException`, và `IndexOutOfRangeException`.
  - **System.ApplicationException**: Thường được sử dụng cho các lỗi thuộc về ứng dụng, tuy nhiên ít khi sử dụng trong thực tế.
  - **Ngoại lệ tùy chỉnh (Custom Exceptions)**: Có thể kế thừa từ `Exception` để tạo ra các lớp ngoại lệ riêng biệt cho ứng dụng.

### 3. Các kịch bản phổ biến nơi ngoại lệ có thể xảy ra

Dưới đây là một số kịch bản phổ biến mà ngoại lệ thường xảy ra trong C# .NET:

- **Chia cho 0**: Khi phép chia xảy ra mà mẫu số bằng 0.
- **Tham chiếu null**: Khi gọi phương thức hoặc thuộc tính của một đối tượng `null`.
- **Chỉ số mảng ngoài phạm vi**: Khi truy cập phần tử của mảng bằng chỉ số vượt quá phạm vi.
- **Chuyển đổi kiểu không hợp lệ**: Khi cố chuyển đổi một đối tượng thành kiểu không tương thích.
- **Lỗi kết nối mạng**: Khi không thể kết nối đến cơ sở dữ liệu hoặc dịch vụ web.

### 4. Xử lý ngoại lệ (Exception Handling) trong C# .NET

Xử lý ngoại lệ giúp ứng dụng khắc phục sự cố và tiếp tục hoạt động bình thường hoặc ít nhất là dừng lại một cách an toàn. Trong .NET, cấu trúc `try`, `catch`, `finally`, và `throw` đóng vai trò cốt lõi trong xử lý ngoại lệ.

#### `try` - `catch` - `finally`

Cấu trúc `try-catch-finally` là nền tảng của xử lý ngoại lệ:

- **`try`**: Bao quanh mã có khả năng phát sinh lỗi.
- **`catch`**: Được sử dụng để xử lý ngoại lệ phát sinh trong khối `try`.
- **`finally`**: Luôn được thực thi sau khối `try` hoặc `catch` và thường dùng để giải phóng tài nguyên.

**Ví dụ**:

```csharp
try
{
    int[] arr = new int[3];
    Console.WriteLine(arr[5]); // Lỗi: IndexOutOfRangeException
}
catch (IndexOutOfRangeException ex)
{
    Console.WriteLine("Lỗi: Chỉ số mảng ngoài phạm vi.");
}
catch (Exception ex)
{
    Console.WriteLine("Lỗi chung: " + ex.Message);
}
finally
{
    Console.WriteLine("Khối finally luôn được thực thi.");
}
```

#### `throw` - Ném Ngoại Lệ

Lệnh `throw` giúp ném ngoại lệ khi phát hiện điều kiện lỗi hoặc khi muốn truyền lỗi lên tầng xử lý cao hơn.

**Ví dụ**:

```csharp
void ValidateAge(int age)
{
    if (age < 18)
    {
        throw new ArgumentException("Tuổi phải lớn hơn hoặc bằng 18.");
    }
}
```

#### Các loại Ngoại Lệ Thông Dụng

- **ArgumentException**: Khi đối số không hợp lệ.
- **NullReferenceException**: Khi thao tác trên đối tượng `null`.
- **IndexOutOfRangeException**: Khi truy cập chỉ số mảng ngoài phạm vi.
- **InvalidOperationException**: Khi thực hiện thao tác không hợp lệ với trạng thái của đối tượng.

**Ví dụ**:

```csharp
try
{
    // Code có thể gây lỗi
}
catch (ArgumentException ex)
{
    Console.WriteLine("Đối số không hợp lệ: " + ex.Message);
}
catch (InvalidOperationException ex)
{
    Console.WriteLine("Thao tác không hợp lệ: " + ex.Message);
}
catch (Exception ex)
{
    Console.WriteLine("Lỗi không xác định: " + ex.Message);
}
```

#### Tạo Ngoại Lệ Tùy Chỉnh (Custom Exception)

Nếu ngoại lệ mặc định không đủ để biểu diễn lỗi, có thể tạo ngoại lệ tùy chỉnh bằng cách kế thừa `Exception`.

**Ví dụ**:

```csharp
public class InvalidUserException : Exception
{
    public InvalidUserException() : base("Người dùng không hợp lệ.") { }
    public InvalidUserException(string message) : base(message) { }
    public InvalidUserException(string message, Exception inner) : base(message, inner) { }
}
```

Sử dụng ngoại lệ tùy chỉnh:

```csharp
void CheckUser(string username)
{
    if (username != "Admin")
    {
        throw new InvalidUserException("Tên người dùng không hợp lệ.");
    }
}
```

#### Sử dụng `when` trong `catch`

`when` cho phép thêm điều kiện vào `catch`, giúp lọc ra các ngoại lệ cụ thể hơn.

**Ví dụ**:

```csharp
try
{
    // Code có thể gây lỗi
}
catch (Exception ex) when (ex.Message.Contains("dữ liệu"))
{
    Console.WriteLine("Lỗi liên quan đến dữ liệu: " + ex.Message);
}
```

#### Global Exception Handling

Trong các ứng dụng lớn, xử lý ngoại lệ toàn cục giúp đảm bảo mọi lỗi đều được ghi nhận và xử lý.

- **ASP.NET Core**: Sử dụng `Middleware` hoặc `UseExceptionHandler`.

  ```csharp
  public void Configure(IApplicationBuilder app, IHostingEnvironment env)
  {
      app.UseExceptionHandler("/Home/Error"); // Định tuyến khi có lỗi
  }
  ```

- **Windows Forms**: Sử dụng `Application.ThreadException` để xử lý ngoại lệ xảy ra bất cứ đâu trong ứng dụng.

  ```csharp
  Application.ThreadException += (sender, args) =>
  {
      MessageBox.Show("Đã xảy ra lỗi: " + args.Exception.Message);
  };
  Application.Run(new MainForm());
  ```

#### Logging

Ghi lại các ngoại lệ giúp dễ dàng tìm hiểu và sửa chữa lỗi. Sử dụng thư viện logging như NLog hoặc Serilog giúp lưu lại thông tin lỗi chi tiết, bao gồm stack trace.

### 5. Tóm tắt

- **`try-catch-finally`**: Để xử lý lỗi cục bộ.
- **`throw`**: Để tạo và ném ngoại lệ.
- **Ngoại lệ tùy chỉnh**: Để tạo loại ngoại lệ riêng cho ứng dụng.
- **Global Exception Handling**: Để đảm bảo xử lý tổng quát.
- **Logging**: Để giám sát và bảo trì ứng dụng.

Việc hiểu và vận dụng linh hoạt các thành phần trên sẽ giúp xây dựng ứng dụng .NET ổn định, dễ bảo trì hơn.
