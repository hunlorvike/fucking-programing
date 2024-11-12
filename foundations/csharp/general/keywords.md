# **Từ khóa trong C#**

Trong C#, từ khóa (keywords) là những từ được sử dụng để xây dựng cấu trúc của chương trình, biểu diễn các kiểu dữ liệu, thực hiện các thao tác điều khiển, khai báo phương thức và class, v.v. Dưới đây là danh sách các từ khóa phổ biến trong C# được phân loại theo chức năng.

### **1. Từ khóa Kiểu dữ liệu (Data Types)**

#### **Kiểu giá trị (Value Types):**

Các kiểu giá trị lưu trữ dữ liệu trực tiếp và không phụ thuộc vào địa chỉ bộ nhớ ngoài.

```csharp
bool    // True/False, kích thước 1 byte
byte    // 0 đến 255, kích thước 1 byte
char    // Ký tự Unicode, kích thước 2 byte
decimal // -7.9 x 10^28 đến 7.9 x 10^28, kích thước 16 byte
double  // ±5.0 × 10^−324 đến ±1.7 × 10^308, kích thước 8 byte
float   // -3.4 × 10^38 đến +3.4 × 10^38, kích thước 4 byte
int     // -2,147,483,648 đến 2,147,483,647, kích thước 4 byte
long    // -9,223,372,036,854,775,808 đến 9,223,372,036,854,775,807, kích thước 8 byte
sbyte   // -128 đến 127, kích thước 1 byte
short   // -32,768 đến 32,767, kích thước 2 byte
uint    // 0 đến 4,294,967,295, kích thước 4 byte
ulong   // 0 đến 18,446,744,073,709,551,615, kích thước 8 byte
ushort  // 0 đến 65,535, kích thước 2 byte
```

#### **Kiểu tham chiếu (Reference Types):**

Các kiểu tham chiếu lưu trữ địa chỉ bộ nhớ của dữ liệu thay vì lưu trữ dữ liệu trực tiếp.

```csharp
object  // Là kiểu cơ sở cho tất cả các kiểu trong .NET, có thể chứa bất kỳ kiểu dữ liệu nào.
string  // Chuỗi ký tự Unicode
dynamic // Kiểu động, kiểu của nó xác định tại runtime.
```

#### **Kiểu cấu trúc và liệt kê:**

```csharp
struct  // Định nghĩa kiểu cấu trúc (value type), lưu trữ các giá trị và có thể chứa các trường và phương thức.
enum    // Định nghĩa kiểu liệt kê, dùng để khai báo các giá trị hằng.
```

### **2. Từ khóa Điều khiển Luồng**

#### **Rẽ nhánh:**

```csharp
if      // Câu lệnh điều kiện
else    // Thực hiện nếu điều kiện if sai
switch  // Câu lệnh chuyển hướng đa nhánh
case    // Định nghĩa một trường hợp trong switch
default // Trường hợp mặc định trong switch
```

#### **Vòng lặp:**

```csharp
for     // Vòng lặp có bộ đếm
foreach // Vòng lặp qua các phần tử trong collection
while   // Vòng lặp kiểm tra điều kiện trước
do      // Vòng lặp kiểm tra điều kiện sau
break   // Thoát khỏi vòng lặp
continue// Bỏ qua phần còn lại của vòng lặp hiện tại
```

#### **Xử lý ngoại lệ:**

```csharp
try     // Khối mã có thể gây ra ngoại lệ
catch   // Bắt và xử lý ngoại lệ
finally // Mã sẽ luôn được thực thi, dù có ngoại lệ hay không
throw   // Ném một ngoại lệ
```

### **3. Từ khóa Sửa đổi Truy cập**

```csharp
public          // Có thể truy cập từ bất kỳ đâu
private         // Chỉ truy cập được trong cùng class
protected       // Truy cập được trong class và các class kế thừa
internal        // Truy cập được trong cùng assembly
protected internal // Truy cập trong cùng assembly và class kế thừa
private protected // Truy cập trong cùng assembly và các class kế thừa
```

### **4. Từ khóa Phương thức và Hàm**

#### **Tham số phương thức:**

```csharp
ref     // Tham chiếu đến biến (có thể thay đổi giá trị của biến tại phương thức gọi)
out     // Tham số đầu ra, phải được gán giá trị trong phương thức
in      // Tham số chỉ đọc (không thể thay đổi giá trị trong phương thức)
params  // Mảng tham số có độ dài thay đổi (có thể truyền vào số lượng tham số bất kỳ)
```

Dưới đây là các ví dụ cụ thể để minh họa cách sử dụng **`ref`**, **`out`**, **`in`**, và **`params`** trong C#.

### 1. `ref` - Tham chiếu đến biến

Sử dụng `ref` để truyền tham chiếu đến biến, cho phép thay đổi giá trị của biến tại phương thức gọi.

```csharp
using System;

class Program {
    static void Main() {
        int number = 5;
        Increment(ref number);
        Console.WriteLine(number); // Output: 6
    }

    static void Increment(ref int x) {
        x++; // Thay đổi giá trị biến gốc `number` trong Main
    }
}
```

- **Giải thích**: `ref` yêu cầu biến được khởi tạo trước khi truyền vào phương thức. Biến `number` được thay đổi trong hàm `Increment` và cập nhật giá trị ở `Main`.

### 2. `out` - Tham số đầu ra

Sử dụng `out` khi biến cần được gán giá trị trong phương thức trước khi sử dụng ở nơi khác.

```csharp
using System;

class Program {
    static void Main() {
        int result;
        Multiply(3, 4, out result);
        Console.WriteLine(result); // Output: 12
    }

    static void Multiply(int a, int b, out int product) {
        product = a * b; // Gán giá trị cho `product`
    }
}
```

- **Giải thích**: `out` yêu cầu biến phải được gán giá trị bên trong phương thức `Multiply`. Trong `Main`, biến `result` nhận giá trị từ `Multiply`.

### 3. `in` - Tham số chỉ đọc

Sử dụng `in` để truyền tham số chỉ đọc, đảm bảo giá trị không bị thay đổi trong phương thức.

```csharp
using System;

class Program {
    static void Main() {
        int number = 5;
        PrintDouble(in number);
        Console.WriteLine(number); // Output: 5
    }

    static void PrintDouble(in int x) {
        Console.WriteLine(x * 2); // Output: 10
        // x = x + 1; // Lỗi biên dịch vì `x` là tham số chỉ đọc
    }
}
```

- **Giải thích**: `in` đảm bảo biến `x` trong `PrintDouble` chỉ có thể đọc, không được phép thay đổi. Giá trị `number` trong `Main` không bị ảnh hưởng.

### 4. `params` - Mảng tham số có độ dài thay đổi

Sử dụng `params` để cho phép truyền số lượng tham số bất kỳ vào phương thức dưới dạng mảng.

```csharp
using System;

class Program {
    static void Main() {
        PrintNumbers(1, 2, 3, 4, 5);
        PrintNumbers(10, 20); // In ra 10 và 20
    }

    static void PrintNumbers(params int[] numbers) {
        foreach (int num in numbers) {
            Console.WriteLine(num);
        }
    }
}
```

- **Giải thích**: `params` giúp truyền vào nhiều số nguyên mà không cần khai báo trước số lượng. Các tham số được nhóm thành một mảng `numbers` và được duyệt bằng `foreach`.

### **5. Từ khóa Chỉ định Kiểu**

```csharp
abstract    // Khai báo class hoặc phương thức trừu tượng, class không thể tạo instance
const       // Khai báo hằng số, giá trị không thay đổi trong suốt chương trình
event       // Khai báo sự kiện
extern      // Khai báo phương thức bên ngoài C# (thường trong thư viện ngoài .NET)
override    // Ghi đè phương thức trong class kế thừa
readonly    // Chỉ có thể gán giá trị trong constructor
sealed      // Ngăn chặn kế thừa class
static      // Thuộc về kiểu (class) thay vì instance (object)
unsafe      // Code không an toàn (sử dụng con trỏ)
virtual     // Phương thức có thể bị ghi đè trong class dẫn xuất
volatile    // Chỉ thị rằng trường có thể thay đổi bất cứ lúc nào (chủ yếu trong multi-threading)
```

### **6. Từ khóa Đặc biệt**

```csharp
as          // Chuyển đổi kiểu một cách an toàn
is          // Kiểm tra kiểu của đối tượng
new         // Tạo instance mới của class, hoặc che giấu thành viên của class cha
sizeof      // Lấy kích thước của kiểu dữ liệu
typeof      // Lấy đối tượng Type của kiểu dữ liệu
nameof      // Trả về tên của biến hoặc kiểu như một chuỗi
stackalloc  // Cấp phát bộ nhớ trên stack (không phải heap)
checked     // Kiểm tra tràn số khi thực hiện phép toán
unchecked   // Không kiểm tra tràn số khi thực hiện phép toán
```

### **7. Từ khóa Lập trình Bất đồng bộ**

```csharp
async   // Đánh dấu phương thức là bất đồng bộ, trả về Task hoặc Task<T>
await   // Đợi cho Task bất đồng bộ hoàn thành
Task    // Đại diện cho một tác vụ bất đồng bộ
```

### **8. Từ khóa Pattern Matching (C# 9.0+)**

```csharp
when    // Thêm điều kiện vào một pattern
and     // Kết hợp các pattern với điều kiện và
or      // Kết hợp các pattern với điều kiện hoặc
not     // Phủ định của một pattern
```

### **9. Records (C# 9.0+)**

```csharp
record          // Định nghĩa kiểu record bất biến
record struct   // Định nghĩa record dưới dạng kiểu giá trị (value type)
init            // Thuộc tính chỉ có thể được khởi tạo trong constructor hoặc với từ khóa init
```

### **10. Từ khóa Liên quan đến Nullable**

```csharp
null        // Giá trị null, có thể gán cho các kiểu tham chiếu
nullable    // Kiểu có thể nhận giá trị null (ví dụ: int? cho phép int là null)
notnull     // Kiểu không thể null (mới trong C# 8.0+)
```
