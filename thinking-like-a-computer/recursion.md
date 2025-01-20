## **🚀 "GIẢI MÃ" ĐỆ QUY (RECURSION): HÀM TỰ GỌI MÌNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một kỹ thuật lập trình rất thú vị và mạnh mẽ: Đệ quy (
Recursion). Nghe có vẻ "hack não" nhưng thực ra rất dễ hiểu nếu mình "mổ xẻ" nó ra. Mình sẽ cố gắng giải thích dễ hiểu
nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. ĐỆ QUY LÀ GÌ?**

* **Đệ quy (Recursion):** Là kỹ thuật lập trình mà một hàm tự gọi chính nó để giải quyết một bài toán.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn nhìn vào một tấm gương: bạn thấy ảnh của bạn, rồi trong ảnh đó lại có ảnh của bạn, ...
* **Ưu điểm:**
    * **Dễ hiểu:** Code ngắn gọn, dễ đọc với các bài toán có tính đệ quy.
    * **Hiệu quả:** Giải quyết tốt các bài toán có cấu trúc đệ quy.
* **Nhược điểm:**
    * **Có thể chậm:** Có thể tốn nhiều thời gian nếu số lần đệ quy lớn.
    * **Khó debug:** Có thể khó theo dõi và sửa lỗi.
    * **Stack Overflow:** Có thể bị lỗi tràn bộ nhớ stack nếu đệ quy quá sâu.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Trường hợp cơ bản (Base case):** Xác định trường hợp đơn giản nhất mà không cần đệ quy.
2. **Bước đệ quy (Recursive step):**
    * Chia bài toán lớn thành bài toán con nhỏ hơn (tương tự).
    * Gọi hàm đệ quy để giải bài toán con.
3. **Kết hợp kết quả:** Kết hợp kết quả các bài toán con để được kết quả bài toán lớn.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĂN CHUỐI**

```
recursive_function(problem):
  IF problem is base case:
    return base solution
  ELSE:
    subproblem = reduce_problem(problem)
    subsolution = recursive_function(subproblem)
    result = combine(subsolution, problem)
    return result
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHÉ!)**

* **`recursive_function(problem)`:** Hàm chính, nhận vào bài toán.
* **`IF problem is base case`:** Kiểm tra xem bài toán có phải là trường hợp cơ bản không (không cần đệ quy).
* **`return base solution`:** Nếu là trường hợp cơ bản, trả về kết quả luôn.
* **`subproblem = reduce_problem(problem)`:** Chia bài toán thành bài toán con nhỏ hơn.
* **`subsolution = recursive_function(subproblem)`:** Gọi đệ quy để giải bài toán con.
* **`result = combine(subsolution, problem)`:** Kết hợp kết quả của bài toán con để có kết quả bài toán lớn.
* **`return result`:** Trả về kết quả cuối cùng.

### **V. VÍ DỤ MINH HỌA - TÍNH GIAI THỪA (C#)**

```csharp
using System;

public class FactorialExample
{
    public static int Factorial(int n)
    {
        if (n == 0)
        {
            return 1;  // Trường hợp cơ bản
        }
        else
        {
            return n * Factorial(n - 1); // Bước đệ quy
        }
    }

    public static void Main(string[] args)
    {
        int n = 5;
        int result = Factorial(n);
        Console.WriteLine($"Giai thừa của {n} là: {result}"); // Output: Giai thừa của 5 là: 120
    }
}
```

**Giải thích:**

* **`Factorial(int n)`:** Hàm tính giai thừa.
* **`if (n == 0)`:** Trường hợp cơ bản: giai thừa của 0 là 1.
* **`else`:** Bước đệ quy: giai thừa của `n` là `n` nhân với giai thừa của `n-1`.

### **VI. VÍ DỤ KHÁC (ĐỂ THẤY RÕ HƠN)**

1. **Fibonacci:** Tính số Fibonacci thứ n.
2. **Hanoi:** Bài toán di chuyển đĩa.
3. **Tìm kiếm nhị phân:** Tìm kiếm phần tử trong danh sách đã được sắp xếp.

### **VII. ƯU ĐIỂM CỦA ĐỆ QUY (NHỚ LÀM GÌ CŨNG TỐT)**

* **Dễ hiểu:** Code ngắn gọn, dễ đọc cho các bài toán có tính chất đệ quy.
* **Hiệu quả:** Giải quyết tốt các bài toán có cấu trúc đệ quy (chia nhỏ bài toán).

### **VIII. NHƯỢC ĐIỂM CỦA ĐỆ QUY (CẨN THẬN LÀM GÌ CŨNG TỐT)**

* **Có thể chậm:** Nếu đệ quy quá nhiều có thể tốn thời gian.
* **Khó debug:** Khó theo dõi các bước đệ quy.
* **Stack Overflow:** Nếu đệ quy quá sâu có thể bị tràn stack.

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "LÚ")**

* **Luôn có trường hợp cơ bản:** Nếu không có trường hợp cơ bản, hàm sẽ đệ quy mãi.
* **Đệ quy vừa phải:** Tránh đệ quy quá sâu có thể làm chậm chương trình và gây lỗi tràn stack.
* **Cân nhắc khi dùng:** Không phải lúc nào đệ quy cũng là cách tốt nhất, có thể dùng vòng lặp thay thế.

### **KẾT LUẬN**

Đệ quy là một kỹ thuật lập trình rất hữu ích, giúp bạn giải quyết nhiều bài toán một cách đơn giản và hiệu quả. Tuy
nhiên, cần cẩn thận khi sử dụng nó để tránh các vấn đề về hiệu suất và lỗi. Hy vọng qua bài viết này, các bạn đã hiểu rõ
hơn về nó. Chúc các bạn code thành công! 😎
