# Nullable Types trong C#

## Mục Lục

1. [Tổng Quan về Nullable Types](#1-tổng-quan-về-nullable-types)

   - [Mục Đích](#mục-đích)
   - [Cách Hoạt Động](#cách-hoạt-động)

2. [Cách Khai Báo Nullable Types](#2-cách-khai-báo-nullable-types)

3. [Kiểm Tra và Sử Dụng Nullable Types](#3-kiểm-tra-và-sử-dụng-nullable-types)

   - [a. Sử Dụng Toán Tử `HasValue` và `Value`](#a-sử-dụng-toán-tử-hasvalue-và-value)
   - [b. Sử Dụng Toán Tử Gộp Null (`??`)](#b-sử-dụng-toán-tử-gộp-null-)
   - [c. Sử Dụng Toán Tử Điều Kiện (`?.` và `??=`)](#c-sử-dụng-toán-tử-điều-kiện--và-)

4. [Nullable Reference Types (C# 8.0+)](#4-nullable-reference-types-c-80)

   - [a. Cách Kích Hoạt Nullable Reference Types](#a-cách-kích-hoạt-nullable-reference-types)
   - [b. Các Cảnh Báo và Kiểm Tra Null](#b-các-cảnh-báo-và-kiểm-tra-null)

5. [Ưu Điểm và Nhược Điểm](#5-ưu-điểm-và-nhược-điểm)

6. [Tóm Tắt](#6-tóm-tắt)

---

### 1. Tổng Quan về Nullable Types

**Nullable Types** (kiểu dữ liệu có thể null) là một tính năng trong C# cho phép các biến kiểu giá trị (value type) có thể lưu trữ giá trị `null`. Mặc định, các kiểu dữ liệu giá trị như `int`, `float`, và `bool` không thể lưu trữ giá trị `null`. Tuy nhiên, với Nullable Types, điều này trở nên khả thi.

#### Mục Đích

- **Xử Lý Dữ Liệu Không Đầy Đủ**: Hỗ trợ các trường hợp khi giá trị không xác định hoặc không tồn tại, chẳng hạn như đọc dữ liệu từ cơ sở dữ liệu hoặc tương tác với API.
- **Tăng Tính Linh Hoạt**: Cho phép các kiểu giá trị thể hiện trạng thái "không có giá trị".

#### Cách Hoạt Động

Nullable Types được triển khai thông qua cấu trúc `System.Nullable<T>`. Bạn có thể sử dụng cú pháp ngắn gọn bằng cách thêm dấu `?` vào sau kiểu dữ liệu.

Ví dụ:

```csharp
int? nullableInt = null; // Khai báo kiểu int có thể null
```

---

### 2. Cách Khai Báo Nullable Types

Nullable Types được khai báo theo hai cách:

1. **Sử Dụng `?`**:

```csharp
int? number = null;
```

2. **Sử Dụng `System.Nullable<T>`**:

```csharp
Nullable<int> number = null;
```

Cả hai cách đều tương đương nhau, nhưng cú pháp `?` được sử dụng phổ biến hơn do tính ngắn gọn.

---

### 3. Kiểm Tra và Sử Dụng Nullable Types

Khi làm việc với Nullable Types, bạn cần kiểm tra xem biến có giá trị hay không trước khi sử dụng.

#### a. Sử Dụng Toán Tử `HasValue` và `Value`

- **`HasValue`**: Trả về `true` nếu biến có giá trị, ngược lại là `false`.
- **`Value`**: Trả về giá trị của biến nếu nó không phải null, nếu không sẽ ném ngoại lệ.

Ví dụ:

```csharp
int? number = 10;

if (number.HasValue)
{
    Console.WriteLine($"Giá trị là: {number.Value}");
}
else
{
    Console.WriteLine("Biến không có giá trị.");
}
```

#### b. Sử Dụng Toán Tử Gộp Null (`??`)

Toán tử `??` cho phép bạn chỉ định giá trị mặc định nếu biến là null.

Ví dụ:

```csharp
int? number = null;
int result = number ?? -1; // Nếu number là null, result sẽ là -1
Console.WriteLine(result); // Kết quả: -1
```

#### c. Sử Dụng Toán Tử Điều Kiện (`?.` và `??=`)

- **Toán tử `?.`**: Dùng để truy cập thuộc tính hoặc phương thức một cách an toàn mà không cần kiểm tra null.
- **Toán tử `??=`**: Gán giá trị mặc định cho biến nếu biến đó là null.

Ví dụ:

```csharp
int? number = null;

// Sử dụng ?. để kiểm tra null trước khi gọi phương thức
int? length = number?.ToString().Length;

// Sử dụng ??= để gán giá trị mặc định nếu là null
number ??= 0;
Console.WriteLine(number); // Kết quả: 0
```

---

### 4. Nullable Reference Types (C# 8.0+)

Từ C# 8.0 trở đi, **Nullable Reference Types** được giới thiệu để quản lý null an toàn hơn với các kiểu tham chiếu (reference types).

#### a. Cách Kích Hoạt Nullable Reference Types

Nullable Reference Types được kích hoạt bằng cách bật tính năng nullable trong tệp `.csproj`:

```xml
<Nullable>enable</Nullable>
```

Hoặc sử dụng chỉ thị trong tệp mã nguồn:

```csharp
#nullable enable
```

#### b. Các Cảnh Báo và Kiểm Tra Null

Với Nullable Reference Types, C# sẽ cảnh báo bạn nếu:

1. Một biến tham chiếu nullable có thể null được sử dụng mà không kiểm tra trước.
2. Bạn cố gắng gán `null` cho một biến tham chiếu không nullable.

Ví dụ:

```csharp
#nullable enable

string? nullableString = null; // Biến nullable
string nonNullableString = "Hello";

// Gây cảnh báo vì nullableString có thể null
Console.WriteLine(nullableString.Length);

// Giải pháp: kiểm tra null trước khi sử dụng
if (nullableString != null)
{
    Console.WriteLine(nullableString.Length);
}
```

---

### 5. Ưu Điểm và Nhược Điểm

#### Ưu Điểm

- **Hỗ Trợ Dữ Liệu Không Đầy Đủ**: Nullable Types rất hữu ích khi làm việc với dữ liệu không đầy đủ hoặc không xác định.
- **Giảm Thiểu Lỗi NullReferenceException**: Nullable Reference Types giúp phát hiện lỗi null sớm trong quá trình biên dịch.
- **Cải Thiện Tính Linh Hoạt**: Cho phép biểu diễn trạng thái "không có giá trị".

#### Nhược Điểm

- **Phức Tạp Hóa Mã Nguồn**: Yêu cầu kiểm tra null thường xuyên hơn.
- **Khả Năng Gây Nhầm Lẫn**: Sự khác biệt giữa Nullable Types và Nullable Reference Types có thể gây nhầm lẫn cho người mới học.

---

### 6. Tóm Tắt

Nullable Types trong C# là một công cụ mạnh mẽ giúp xử lý các giá trị null một cách an toàn và linh hoạt. Chúng cho phép các kiểu giá trị lưu trữ trạng thái "không có giá trị" và giúp giảm thiểu lỗi runtime liên quan đến null.

**Các điểm chính:**

- **Nullable Types**: Cho phép các kiểu giá trị như `int`, `bool` lưu trữ giá trị null.
- **Nullable Reference Types**: Được giới thiệu từ C# 8.0, giúp quản lý null hiệu quả hơn cho các kiểu tham chiếu.
- **Toán Tử Hữu Ích**: `??`, `?.`, và `??=` giúp làm việc với null dễ dàng hơn.

Với việc sử dụng đúng cách, Nullable Types sẽ cải thiện đáng kể độ ổn định và khả năng bảo trì của ứng dụng C#.