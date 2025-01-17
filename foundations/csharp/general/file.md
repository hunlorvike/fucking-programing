## Làm việc với File trong C#

Làm việc với file là một công việc rất phổ biến trong phát triển ứng dụng C#, đặc biệt khi sử dụng .NET Framework hoặc
.NET Core. Bài viết này sẽ giới thiệu chi tiết các thao tác cơ bản làm việc với file trong C# thông qua namespace
`System.IO`.

### Mục lục

1. [Đọc file](#1-Đọc-file)
    - [Sử dụng `File.ReadAllText`](#Sử-dụng-FileReadAllText)
    - [Sử dụng `StreamReader`](#Sử-dụng-StreamReader)
2. [Ghi file](#2-Ghi-file)
    - [Sử dụng `File.WriteAllText`](#Sử-dụng-FileWriteAllText)
    - [Sử dụng `StreamWriter`](#Sử-dụng-StreamWriter)
3. [Sao chép, di chuyển và xóa file](#3-Sao-chép-di-chuyển-và-xóa-file)
    - [Sao chép file](#Sao-chép-file)
    - [Di chuyển file](#Di-chuyển-file)
    - [Xóa file](#Xóa-file)
4. [Kiểm tra sự tồn tại của file](#4-Kiểm-tra-sự-tồn-tại-của-file)
5. [Đọc và ghi file nhị phân](#5-Đọc-và-ghi-file-nhị-phân)
6. [Đọc và ghi file JSON (sử dụng `System.Text.Json`)](#6-Đọc-và-ghi-file-JSON)

---

### 1. Đọc file

Bạn có thể đọc dữ liệu từ file bằng cách sử dụng các lớp trong namespace `System.IO`, như `File`, `StreamReader`, hoặc
`FileStream`.

#### Sử dụng `File.ReadAllText`

Phương pháp này cho phép đọc toàn bộ nội dung của file vào một chuỗi, đơn giản và nhanh chóng.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "example.txt";
        if (File.Exists(path))
        {
            string content = File.ReadAllText(path);
            Console.WriteLine(content);
        }
        else
        {
            Console.WriteLine("File không tồn tại.");
        }
    }
}
```

- **Ưu điểm**:

    - Dễ sử dụng và phù hợp cho các file nhỏ hoặc vừa.
    - Code ngắn gọn, đọc file nhanh chóng.

- **Nhược điểm**:
    - Nếu file lớn, phương pháp này có thể tiêu tốn bộ nhớ vì đọc toàn bộ nội dung vào một chuỗi.
    - Không linh hoạt cho việc xử lý từng dòng hay các phần nhỏ của file.

#### Sử dụng `StreamReader`

`StreamReader` cho phép đọc từng dòng một từ file, giúp tiết kiệm bộ nhớ và linh hoạt hơn khi xử lý file lớn.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "example.txt";
        using (StreamReader reader = new StreamReader(path))
        {
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine(line);
            }
        }
    }
}
```

- **Ưu điểm**:

    - Linh hoạt và tiết kiệm bộ nhớ cho các file lớn.
    - Dễ dàng xử lý từng dòng hoặc từng phần của file.

- **Nhược điểm**:
    - Phức tạp hơn khi cần đọc toàn bộ file thành chuỗi.
    - Cần phải quản lý `Stream` để đóng đúng cách (có thể dùng `using` như ví dụ trên).

### 2. Ghi file

Có thể ghi dữ liệu vào file bằng các phương thức như `File.WriteAllText`, `StreamWriter`.

#### Sử dụng `File.WriteAllText`

Phương pháp này ghi toàn bộ nội dung từ một chuỗi vào file, ghi đè lên nội dung cũ nếu file đã tồn tại.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "example.txt";
        string content = "Đây là nội dung mới của file.";
        File.WriteAllText(path, content);
        Console.WriteLine("Đã ghi file thành công.");
    }
}
```

- **Ưu điểm**:

    - Đơn giản, phù hợp cho việc ghi nhanh một lượng dữ liệu nhỏ.
    - Dễ hiểu, dễ triển khai cho các tác vụ đơn giản.

- **Nhược điểm**:
    - Ghi đè lên toàn bộ nội dung file, không phù hợp cho việc ghi tiếp hoặc thêm dữ liệu vào file.
    - Hạn chế khi làm việc với dữ liệu lớn.

#### Sử dụng `StreamWriter`

`StreamWriter` giúp ghi từng dòng và có thể ghi tiếp mà không ghi đè.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "example.txt";
        using (StreamWriter writer = new StreamWriter(path, true)) // true để ghi thêm
        {
            writer.WriteLine("Dòng mới trong file.");
        }
        Console.WriteLine("Đã ghi dòng vào file thành công.");
    }
}
```

- **Ưu điểm**:

    - Cho phép ghi thêm vào file mà không ghi đè.
    - Linh hoạt trong việc ghi từng phần, từng dòng của file.

- **Nhược điểm**:
    - Phức tạp hơn `File.WriteAllText`.
    - Cần quản lý `Stream` để tránh lỗi khi xử lý file.

### 3. Sao chép, di chuyển và xóa file

Các thao tác sao chép, di chuyển hoặc xóa file có thể thực hiện dễ dàng với các phương thức có sẵn trong lớp `File`.

#### Sao chép file

```csharp
string sourcePath = "example.txt";
string destinationPath = "copy_example.txt";
File.Copy(sourcePath, destinationPath, true); // true để ghi đè nếu file đích đã tồn tại
Console.WriteLine("Đã sao chép file thành công.");
```

- **Ưu điểm**:

    - Thao tác sao chép nhanh chóng và dễ dàng.
    - Có tùy chọn ghi đè nếu file đích đã tồn tại.

- **Nhược điểm**:
    - Không hỗ trợ sao chép thư mục.

#### Di chuyển file

```csharp
string sourcePath = "example.txt";
string destinationPath = "new_location/example.txt";
File.Move(sourcePath, destinationPath);
Console.WriteLine("Đã di chuyển file thành công.");
```

- **Ưu điểm**:

    - Dễ thực hiện và phù hợp cho việc tổ chức lại dữ liệu.

- **Nhược điểm**:
    - Cần kiểm tra trước xem đường dẫn đích có tồn tại để tránh lỗi.

#### Xóa file

```csharp
string path = "example.txt";
File.Delete(path);
Console.WriteLine("Đã xóa file thành công.");
```

- **Ưu điểm**:

    - Xóa file đơn giản và nhanh chóng.

- **Nhược điểm**:
    - Không có xác nhận khi xóa, cần chắc chắn trước khi thực hiện.

### 4. Kiểm tra sự tồn tại của file

Bạn có thể kiểm tra xem file có tồn tại hay không trước khi thực hiện bất kỳ thao tác nào khác:

```csharp
string path = "example.txt";
if (File.Exists(path))
{
    Console.WriteLine("File tồn tại.");
}
else
{
    Console.WriteLine("File không tồn tại.");
}
```

- **Ưu điểm**:

    - Tránh lỗi khi làm việc với file không tồn tại.

- **Nhược điểm**:
    - Có thể không cần thiết trong một số trường hợp đơn giản.

### 5. Đọc và ghi file nhị phân

Nếu cần thao tác với dữ liệu nhị phân, `FileStream` là lựa chọn tốt.

#### Đọc file nhị phân

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "example.bin";
        using (FileStream fs = new FileStream(path, FileMode.Open, FileAccess.Read))
        {
            byte[] buffer = new byte[fs.Length];
            fs.Read(buffer, 0, buffer.Length);
            Console.WriteLine("Đã đọc file nhị phân thành công.");
        }
    }
}
```

#### Ghi file nhị phân

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "example.bin";
        byte[] data = { 0x0, 0x1, 0x2, 0x3 };
        using (FileStream fs = new FileStream(path, FileMode.Create, FileAccess.Write))
        {
            fs.Write(data, 0, data.Length);
            Console.WriteLine("Đã ghi file nhị phân thành công.");
        }
    }
}
```

- **Ưu điểm**:

    - Phù hợp cho các file nhị phân như hình ảnh, video, hoặc dữ liệu mã hóa.

- **Nhược điểm**:
    - Phức tạp khi xử lý so với file văn bản.
    - Cần quản lý `Stream` cẩn thận.

### 6. Đọc và ghi file

JSON

Với C# .NET, bạn có thể dễ dàng thao tác với dữ liệu JSON bằng cách sử dụng `System.Text.Json`.

#### Đọc JSON

```csharp
using System;
using System.IO;
using System.Text.Json;

class Program
{
    class User
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    static void Main()
    {
        string path = "user.json";
        string jsonString = File.ReadAllText(path);
        User user = JsonSerializer.Deserialize<User>(jsonString);
        Console.WriteLine($"Tên: {user.Name}, Tuổi: {user.Age}");
    }
}
```

#### Ghi JSON

```csharp
using System;
using System.IO;
using System.Text.Json;

class Program
{
    class User
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    static void Main()
    {
        string path = "user.json";
        User user = new User { Name = "Nguyen Van A", Age = 25 };
        string jsonString = JsonSerializer.Serialize(user);
        File.WriteAllText(path, jsonString);
        Console.WriteLine("Đã ghi JSON vào file thành công.");
    }
}
```

- **Ưu điểm**:

    - Dễ sử dụng cho các thao tác JSON, phù hợp với nhiều ứng dụng hiện đại.
    - Cung cấp khả năng chuyển đổi dữ liệu từ và sang đối tượng C# dễ dàng.

- **Nhược điểm**:
    - Yêu cầu phải biết cấu trúc JSON trước khi làm việc.
    - Tốn thời gian xử lý khi làm việc với file JSON lớn.
