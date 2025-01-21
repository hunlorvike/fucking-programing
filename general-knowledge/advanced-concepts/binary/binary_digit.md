## **🚀 "GIẢI MÃ" BIT TRONG LẬP TRÌNH: "VIÊN GẠCH" CƠ BẢN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong lập trình và máy
tính: Bit. Nghe có vẻ "hàn lâm" nhưng thực ra rất gần gũi và hữu ích cho dân code chúng mình đấy. Cùng mình "mổ xẻ" nó
nhé!

### **I. BIT LÀ GÌ? (ĐƠN GIẢN NHƯ ĂN KẸO)**

- **Bit:** Là đơn vị nhỏ nhất của dữ liệu trong máy tính.
- **Nó hoạt động như thế nào?**
    - Giống như một công tắc: hoặc là BẬT (1), hoặc là TẮT (0).
- **Đặc điểm:**
    - Có hai giá trị: 0 hoặc 1 (nhị phân).
    - Là nền tảng của mọi dữ liệu trong máy tính.

### **II. TẠI SAO BIT LẠI QUAN TRỌNG?**

- **Cơ sở của mọi dữ liệu:** Tất cả dữ liệu (số, chữ, ảnh, video,...) đều được mã hóa thành các chuỗi bit.
- **Công nghệ điện tử:** Máy tính hoạt động dựa trên tín hiệu điện (có điện/không điện), dễ dàng biểu diễn bằng bit.

### **III. CÁC ĐƠN VỊ DỮ LIỆU (BIT LÀ GỐC, CÁI KHÁC LÀ "CÂY")**

- **Byte:** 1 byte = 8 bits.
- **Kilobyte (KB):** 1 KB = 1024 bytes.
- **Megabyte (MB):** 1 MB = 1024 KB.
- **Gigabyte (GB):** 1 GB = 1024 MB.
- **Terabyte (TB):** 1 TB = 1024 GB.

### **IV. BIT TRONG LẬP TRÌNH (LÀM GÌ VỚI BIT?)**

- **Biểu diễn số:** Dùng bit để biểu diễn số nguyên, số thực.
- **Phép toán bitwise:** Các phép toán trên bit:
    - **AND (&):** Chỉ trả về 1 nếu cả hai bit đều là 1.
    - **OR (|):** Trả về 1 nếu ít nhất một bit là 1.
    - **XOR (^):** Trả về 1 nếu hai bit khác nhau.
    - **NOT (~):** Đảo ngược giá trị bit (0 -> 1, 1 -> 0).
    - **Shift Left (<<):** Di chuyển bit sang trái (nhân 2).
    - **Shift Right (>>):** Di chuyển bit sang phải (chia 2).

### **V. ỨNG DỤNG CỦA BIT (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Lưu trữ dữ liệu:** Lưu trữ dữ liệu trên đĩa, RAM,...
- **Mã hóa:** Mã hóa dữ liệu, bảo mật thông tin.
- **Truyền thông:** Mã hóa tín hiệu trong truyền dữ liệu.

### **VI. VÍ DỤ THỰC TẾ (CODE C# CHO DỄ HÌNH DUNG)**

```csharp
using System;

public class BitExample
{
    public static void Main(string[] args)
    {
        byte a = 5;  // 00000101 trong nhị phân
        byte b = 3;  // 00000011 trong nhị phân
        byte result;

        result = (byte)(a & b);   // Phép AND: 00000101 & 00000011 = 00000001 (1)
        Console.WriteLine($"AND: {result}");   // Output: AND: 1

        result = (byte)(a | b);   // Phép OR: 00000101 | 00000011 = 00000111 (7)
        Console.WriteLine($"OR: {result}");   // Output: OR: 7

        result = (byte)(a ^ b);   // Phép XOR: 00000101 ^ 00000011 = 00000110 (6)
        Console.WriteLine($"XOR: {result}");   // Output: XOR: 6

        result = (byte)~a;        // Phép NOT: ~00000101 = 11111010 (250 trong số không dấu)
        Console.WriteLine($"NOT: {result}");   // Output: NOT: 250

        result = (byte)(a << 1);  // Shift trái: 00000101 << 1 = 00001010 (10)
        Console.WriteLine($"Shift Left: {result}"); // Output: Shift Left: 10

        result = (byte)(a >> 1);  // Shift phải: 00000101 >> 1 = 00000010 (2)
        Console.WriteLine($"Shift Right: {result}");  // Output: Shift Right: 2
    }
}
```

### **VII. CÁCH TÍNH BIT CẦN THIẾT (ĐỂ KHÔNG BỊ "THỪA")**

- **Công thức:** Số bit = Kích thước (byte) \* 8.
- **Ví dụ:**
    - `byte`: 1 byte = 8 bit.
    - `int`: 4 byte = 32 bit.
    - `long`: 8 byte = 64 bit.

### **VIII. CHUYỂN ĐỔI GIỮA CÁC HỆ THỐNG SỐ (NHỊ PHÂN, THẬP PHÂN, THẬP LỤC PHÂN)**

- **Nhị phân -> Thập phân:** `1011` = 1\*2³ + 0\*2² + 1\*2¹ + 1\*2⁰ = 8 + 0 + 2 + 1 = 11.
- **Thập phân -> Nhị phân:** Chia liên tục cho 2 và ghi lại số dư.
    - Ví dụ: `13` -> 13/2=6 dư 1, 6/2=3 dư 0, 3/2=1 dư 1, 1/2=0 dư 1. Vậy là `1101`.
- **Nhị phân <-> Thập lục phân:** Nhóm 4 bit thành 1 chữ số thập lục phân.
    - Ví dụ: `1010 1100` -> `A C`.

### **IX. CÁC PHÉP TOÁN BITWISE (CÁCH "CHƠI" VỚI BIT)**

- **AND (&):**
  ```
  5: 0101
  3: 0011
  ----
  &: 0001 (1)
  ```
- **OR (|):**
  ```
  5: 0101
  3: 0011
  ----
  |: 0111 (7)
  ```
- **XOR (^):**
  ```
  5: 0101
  3: 0011
  ----
  ^: 0110 (6)
  ```
- **NOT (~):**
  ```
  5: 0101
  ~: 1010 (250 nếu là byte)
  ```
- **Shift Left (<<):**
  ```
  5: 0101
  <<1: 1010 (10)
  ```
- **Shift Right (>>):**
  ```
  5: 0101
  >>1: 0010 (2)
  ```

### **X. KẾT LUẬN (TỔNG KẾT)**

Bit là khái niệm cơ bản nhưng rất quan trọng trong lập trình. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và
có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
