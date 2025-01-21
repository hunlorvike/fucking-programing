## **🚀 "GIẢI MÃ" NGĂN XẾP (STACK): CẤU TRÚC DỮ LIỆU "XẾP CHỒNG" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một cấu trúc dữ liệu cực kỳ quan trọng và thú vị: Ngăn
xếp (Stack). Đây là một "người bạn" rất hữu ích khi bạn cần quản lý dữ liệu theo thứ tự vào sau ra trước. Cùng mình "mổ
xẻ" nó nhé!

### **I. NGĂN XẾP (STACK) LÀ GÌ?**

- **Ngăn xếp (Stack):** Là cấu trúc dữ liệu tuyến tính mà các phần tử được sắp xếp và truy cập theo nguyên tắc LIFO (
  Last In, First Out): phần tử vào sau ra trước.
- **Nó hoạt động như thế nào?**
    - Giống như một chồng đĩa: bạn để đĩa vào sau cùng, và lấy ra cũng từ trên xuống.
- **Đặc điểm:**
    - **Tuyến tính:** Các phần tử được sắp xếp theo một thứ tự nhất định.
    - **LIFO (Last In, First Out):** Phần tử vào sau ra trước.
    - **Push:** Thêm phần tử vào "đỉnh" ngăn xếp.
    - **Pop:** Lấy phần tử ra từ "đỉnh" ngăn xếp.

### **II. ƯU ĐIỂM CỦA NGĂN XẾP (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Quản lý lịch sử:** Lưu lại các bước thao tác (undo/redo).
- **Dễ cài đặt:** Triển khai bằng mảng hoặc danh sách liên kết đều dễ.
- **Kiểm soát luồng:** Quản lý bộ nhớ và luồng thực thi.

### **III. NHƯỢC ĐIỂM CỦA NGĂN XẾP (NHỮNG ĐIỂM "KHÓ CHỊU")**

- **Truy cập hạn chế:** Chỉ có thể thao tác với phần tử trên đỉnh, không truy cập trực tiếp các phần tử khác.
- **Khó tìm kiếm:** Tìm một phần tử cụ thể thì cần duyệt qua ngăn xếp, có độ phức tạp O(n).

### **IV. ỨNG DỤNG CỦA NGĂN XẾP (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Quản lý bộ nhớ:** Trong các ngôn ngữ lập trình.
- **Kiểm tra biểu thức:** Kiểm tra tính đúng đắn của các dấu ngoặc.
- **Giải thuật quay lui:** Lưu trạng thái trong các thuật toán quay lui.
- **Lập trình hướng đối tượng:** Quản lý các đối tượng.

### **V. VÍ DỤ MINH HỌA (C#)**

```csharp
using System;
using System.Collections.Generic;

public class StackExample
{
    public static void Main(string[] args)
    {
        Stack<int> myStack = new Stack<int>();

        // Thêm các phần tử vào ngăn xếp
        myStack.Push(1);
        myStack.Push(2);
        myStack.Push(3);

        // Lấy ra phần tử ở đỉnh ngăn xếp
        Console.WriteLine("Phần tử ở đỉnh: " + myStack.Pop());  // Output: Phần tử ở đỉnh: 3

        // Xem phần tử ở đỉnh ngăn xếp
        Console.WriteLine("Phần tử ở đỉnh: " + myStack.Peek());  // Output: Phần tử ở đỉnh: 2

        // Kiểm tra xem ngăn xếp có rỗng không
        Console.WriteLine("Ngăn xếp có rỗng không? " + myStack.Count);   // Output: Ngăn xếp có rỗng không? 2
    }
}
```

**Giải thích:**

- **`Stack<int>`:** Tạo ngăn xếp chứa số nguyên.
- **`Push(int)`:** Thêm phần tử vào đỉnh ngăn xếp.
- **`Pop()`:** Lấy ra phần tử ở đỉnh ngăn xếp.
- **`Peek()`:** Xem phần tử ở đỉnh ngăn xếp mà không lấy ra.
- **`Count`:** Xem số lượng phần tử trong ngăn xếp.

### **VI. BỔ SUNG (MỘT SỐ ĐIỀU THÚ VỊ)**

- **Triển khai:** Ngăn xếp có thể cài đặt bằng mảng hoặc danh sách liên kết.
- **Mảng:** Cài đặt ngăn xếp bằng mảng thì đơn giản, dễ code, nhưng nếu phải đẩy nhiều lần có thể tốn thời gian dời các
  phần tử phía sau.
- **Danh sách liên kết:** Cài đặt ngăn xếp bằng danh sách liên kết thì sẽ dễ dàng hơn, chỉ cần insert vào đầu và delete
  ở đầu.
- **Call Stack:** Ngăn xếp được sử dụng để quản lý các hàm được gọi trong chương trình (call stack).

### **VII. KẾT LUẬN (TỔNG KẾT)**

Ngăn xếp là một cấu trúc dữ liệu rất cơ bản, và rất hữu ích khi bạn cần xử lý dữ liệu theo nguyên tắc vào sau ra trước.
Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó. Chúc các bạn code thành công! 😎
