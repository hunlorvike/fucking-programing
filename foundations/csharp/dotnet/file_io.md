# File I/O trong .NET: Tổng Quan và Hướng Dẫn

## Mục Lục

1. [Khái niệm về File I/O](#khái-niệm-về-file-io)
2. [Các lớp quan trọng trong System.IO](#các-lớp-quan-trọng-trong-systemio)
    - [2.1. File và FileInfo](#21-file-và-fileinfo)
    - [2.2. Directory và DirectoryInfo](#22-directory-và-directoryinfo)
    - [2.3. Path](#23-path)
    - [2.4. FileStream](#24-filestream)
3. [Làm việc với File I/O](#làm-việc-với-file-io)
    - [3.1. Đọc và ghi tệp văn bản](#31-đọc-và-ghi-tệp-văn-bản)
    - [3.2. Đọc và ghi tệp nhị phân](#32-đọc-và-ghi-tệp-nhị-phân)
4. [Làm việc với Streams](#làm-việc-với-streams)
    - [4.1. MemoryStream](#41-memorystream)
    - [4.2. BufferedStream](#42-bufferedstream)
5. [Quản lý File I/O hiệu quả](#quản-lý-file-io-hiệu-quả)
    - [5.1. Sử dụng `using` để giải phóng tài nguyên](#51-sử-dụng-using-để-giải-phóng-tài-nguyên)
    - [5.2. Sử dụng các phương thức bất đồng bộ](#52-sử-dụng-các-phương-thức-bất-đồng-bộ)
6. [Tóm tắt](#tóm-tắt)

---

## 1. Khái niệm về File I/O

**File I/O (Input/Output)** trong .NET đề cập đến việc đọc, ghi, tạo, và quản lý các tệp và thư mục trên hệ thống tệp.
.NET cung cấp namespace `System.IO` với nhiều lớp và phương thức mạnh mẽ, giúp lập trình viên thao tác với dữ liệu trên
đĩa cứng hoặc trong bộ nhớ một cách dễ dàng.

File I/O bao gồm:

- **File operations**: Tạo, mở, đọc, ghi, xóa tệp.
- **Directory operations**: Tạo, liệt kê, xóa thư mục.
- **Stream**: Đọc và ghi dữ liệu tuần tự.

---

## 2. Các lớp quan trọng trong System.IO

### 2.1. File và FileInfo

- **File**: Cung cấp các phương thức tĩnh để thao tác tệp, như tạo, sao chép, di chuyển, xóa và đọc dữ liệu.
- **FileInfo**: Là lớp không tĩnh, cung cấp các phương thức tương tự nhưng làm việc trên một tệp cụ thể.

**Ví dụ**:

```csharp
using System.IO;

// Tạo tệp bằng File
File.WriteAllText("example.txt", "Hello, .NET!");

// Xóa tệp bằng FileInfo
FileInfo fileInfo = new FileInfo("example.txt");
if (fileInfo.Exists)
{
    fileInfo.Delete();
}
```

---

### 2.2. Directory và DirectoryInfo

- **Directory**: Cung cấp các phương thức tĩnh để thao tác thư mục, như tạo, xóa, và liệt kê các tệp/thư mục con.
- **DirectoryInfo**: Là lớp không tĩnh, cung cấp các phương thức tương tự cho một thư mục cụ thể.

**Ví dụ**:

```csharp
using System.IO;

// Tạo thư mục
Directory.CreateDirectory("MyFolder");

// Kiểm tra thư mục có tồn tại
if (Directory.Exists("MyFolder"))
{
    Console.WriteLine("Thư mục đã tồn tại.");
}
```

---

### 2.3. Path

- Cung cấp các phương thức xử lý đường dẫn, như lấy tên tệp, phần mở rộng, hoặc kết hợp các đoạn đường dẫn.

**Ví dụ**:

```csharp
using System.IO;

string path = @"C:\Users\Example\file.txt";
string fileName = Path.GetFileName(path); // "file.txt"
string directory = Path.GetDirectoryName(path); // "C:\Users\Example"
```

---

### 2.4. FileStream

`FileStream` được sử dụng để đọc và ghi dữ liệu tuần tự trong tệp.

**Ví dụ**:

```csharp
using System.IO;

string path = "data.bin";

// Ghi dữ liệu nhị phân
using (FileStream fs = new FileStream(path, FileMode.Create))
{
    byte[] data = { 1, 2, 3, 4, 5 };
    fs.Write(data, 0, data.Length);
}

// Đọc dữ liệu nhị phân
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    byte[] buffer = new byte[fs.Length];
    fs.Read(buffer, 0, buffer.Length);
    Console.WriteLine(string.Join(", ", buffer));
}
```

---

## 3. Làm việc với File I/O

### 3.1. Đọc và ghi tệp văn bản

**Phương thức phổ biến:**

- `File.WriteAllText()`: Ghi chuỗi văn bản vào tệp.
- `File.ReadAllText()`: Đọc toàn bộ nội dung tệp văn bản.

**Ví dụ**:

```csharp
using System.IO;

// Ghi tệp văn bản
File.WriteAllText("example.txt", "Hello, .NET!");

// Đọc tệp văn bản
string content = File.ReadAllText("example.txt");
Console.WriteLine(content);
```

---

### 3.2. Đọc và ghi tệp nhị phân

**Phương thức phổ biến:**

- `File.WriteAllBytes()`: Ghi mảng byte vào tệp.
- `File.ReadAllBytes()`: Đọc toàn bộ dữ liệu nhị phân của tệp.

**Ví dụ**:

```csharp
using System.IO;

// Ghi tệp nhị phân
byte[] data = { 1, 2, 3, 4, 5 };
File.WriteAllBytes("binary.bin", data);

// Đọc tệp nhị phân
byte[] readData = File.ReadAllBytes("binary.bin");
Console.WriteLine(string.Join(", ", readData));
```

---

## 4. Làm việc với Streams

### 4.1. MemoryStream

`MemoryStream` lưu dữ liệu trong bộ nhớ, phù hợp cho xử lý dữ liệu tạm thời.

**Ví dụ**:

```csharp
using System.IO;

using (MemoryStream ms = new MemoryStream())
{
    // Ghi dữ liệu vào MemoryStream
    byte[] data = { 10, 20, 30 };
    ms.Write(data, 0, data.Length);

    // Đọc dữ liệu từ MemoryStream
    ms.Position = 0;
    byte[] buffer = new byte[ms.Length];
    ms.Read(buffer, 0, buffer.Length);
    Console.WriteLine(string.Join(", ", buffer));
}
```

---

### 4.2. BufferedStream

`BufferedStream` cải thiện hiệu suất bằng cách sử dụng bộ nhớ đệm khi đọc/ghi.

**Ví dụ**:

```csharp
using System.IO;

string path = "buffered.bin";

using (FileStream fs = new FileStream(path, FileMode.Create))
using (BufferedStream bs = new BufferedStream(fs))
{
    byte[] data = { 100, 200, 255 };
    bs.Write(data, 0, data.Length);
}
```

---

## 5. Quản lý File I/O hiệu quả

### 5.1. Sử dụng `using` để giải phóng tài nguyên

`using` tự động giải phóng tài nguyên, tránh rò rỉ bộ nhớ.

**Ví dụ**:

```csharp
using (FileStream fs = new FileStream("example.txt", FileMode.Open))
{
    // Đọc hoặc ghi dữ liệu
}
```

---

### 5.2. Sử dụng các phương thức bất đồng bộ

Dùng phương thức async để cải thiện hiệu suất, đặc biệt với dữ liệu lớn.

**Ví dụ**:

```csharp
using System.IO;
using System.Threading.Tasks;

string path = "async.txt";

// Ghi bất đồng bộ
await File.WriteAllTextAsync(path, "Hello, async!");

// Đọc bất đồng bộ
string content = await File.ReadAllTextAsync(path);
Console.WriteLine(content);
```

---

## 6. Tóm tắt

File I/O trong .NET cung cấp một tập hợp các công cụ mạnh mẽ để quản lý dữ liệu trên hệ thống tệp. Các lớp như `File`,
`Directory`, `FileStream`, và `MemoryStream` giúp bạn xử lý các tác vụ từ cơ bản đến nâng cao. Việc sử dụng đúng cách
các phương thức như bất đồng bộ và `using` không chỉ tăng hiệu suất mà còn đảm bảo mã nguồn của bạn an toàn và dễ bảo
trì.
