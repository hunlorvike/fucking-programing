## **🚀 "GIẢI MÃ" MEMOIZATION: "BÍ KÍP" TỐI ƯU ĐỆ QUY CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một kỹ thuật rất hữu ích giúp tăng tốc độ code đệ quy:
Memoization (ghi nhớ). Nghe có vẻ "hack não" nhưng thực ra rất đơn giản và dễ cài đặt. Mình sẽ cố gắng giải thích dễ
hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. MEMOIZATION LÀ GÌ?**

* **Memoization (Ghi nhớ):** Là kỹ thuật tối ưu hóa hiệu suất của các hàm đệ quy bằng cách lưu lại kết quả của các lần
  gọi hàm đã được tính toán trước đó.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn làm bài tập: nếu bạn đã làm bài nào rồi, bạn ghi lại đáp án để lần sau không phải làm lại.
* **Ưu điểm:**
    * **Nhanh hơn:** Tránh tính toán lại nhiều lần với cùng một input.
    * **Dễ cài đặt:** Chỉ cần thêm một chút code vào hàm đệ quy là xong.
* **Nhược điểm:**
    * **Tốn bộ nhớ:** Cần bộ nhớ để lưu kết quả (như cuốn sổ ghi đáp án).
    * **Không phải lúc nào cũng cần:** Nếu hàm không bị gọi lại nhiều lần thì không cần.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Tạo "sổ ghi nhớ":** Tạo một bảng (thường dùng Dictionary) để lưu kết quả của các lần gọi hàm.
2. **Kiểm tra "sổ ghi nhớ":** Trước khi tính toán, kiểm tra xem kết quả đã có trong "sổ ghi nhớ" chưa.
    * Nếu có: Lấy kết quả đó luôn (không cần tính).
    * Nếu chưa: Tính toán kết quả.
3. **Lưu kết quả:** Lưu kết quả tính được vào "sổ ghi nhớ".
4. **Trả về kết quả:** Trả về kết quả đã tính hoặc lấy từ "sổ ghi nhớ".

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĐỌC TRUYỆN**

```
memoized_function(input, memo):
  IF input in memo:
    RETURN memo[input]
  ELSE:
    result = recursive_calculation(input)
    memo[input] = result
    RETURN result
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHÉ!)**

* **`memoized_function(input, memo)`:** Hàm chính, nhận vào input và "sổ ghi nhớ" (memo).
* **`IF input in memo`:** Kiểm tra xem input đã có trong "sổ ghi nhớ" chưa.
* **`RETURN memo[input]`:** Nếu có rồi thì trả về kết quả đã lưu.
* **`ELSE`:** Nếu chưa có thì tính toán kết quả.
* **`result = recursive_calculation(input)`:** Tính toán kết quả bằng hàm đệ quy.
* **`memo[input] = result`:** Lưu kết quả vào "sổ ghi nhớ".
* **`RETURN result`:** Trả về kết quả.

### **V. VÍ DỤ MINH HỌA - FIBONACCI (C#)**

```csharp
using System;
using System.Collections.Generic;

public class FibonacciMemoization
{
    static Dictionary<int, int> memo = new Dictionary<int, int>();

    public static int Fibonacci(int n)
    {
        if (memo.ContainsKey(n))
        {
            return memo[n]; // Lấy kết quả từ memo
        }

        if (n <= 1)
        {
            return n;
        }

        int result = Fibonacci(n - 1) + Fibonacci(n - 2);
        memo[n] = result; // Lưu kết quả vào memo
        return result;
    }

    public static void Main(string[] args)
    {
        int n = 10;
        int fib = Fibonacci(n);
        Console.WriteLine($"Fibonacci({n}) = {fib}"); // Output: Fibonacci(10) = 55
    }
}
```

**Giải thích:**

* **`memo`:** Dictionary để lưu kết quả.
* **`if (memo.ContainsKey(n))`:** Kiểm tra xem đã tính Fibonacci(n) chưa.
* **`return memo[n]`:** Nếu tính rồi thì trả kết quả đã lưu.
* **`int result = Fibonacci(n - 1) + Fibonacci(n - 2)`:** Tính Fibonacci bằng đệ quy.
* **`memo[n] = result`:** Lưu kết quả vào memo.

### **VI. ƯU ĐIỂM CỦA MEMOIZATION (NHỚ LÀM GÌ CŨNG TỐT)**

* **Cải thiện tốc độ:** Thuật toán chạy nhanh hơn nhờ tránh tính toán lại.
* **Dễ cài đặt:** Chỉ cần thêm một ít code vào hàm đệ quy.
* **Tối ưu cho đệ quy:** Đặc biệt hữu ích cho các hàm đệ quy có nhiều trường hợp lặp.

### **VII. NHƯỢC ĐIỂM CỦA MEMOIZATION (CẨN THẬN LÀM GÌ CŨNG TỐT)**

* **Tốn bộ nhớ:** Cần bộ nhớ để lưu kết quả (như cuốn sổ ghi đáp án).
* **Không phải lúc nào cũng cần:** Nếu hàm không bị gọi nhiều lần thì không cần.

### **VIII. KHI NÀO NÊN DÙNG MEMOIZATION (CHỌN ĐÚNG "VŨ KHÍ")**

* Khi bạn có hàm đệ quy, và hàm đó có thể được gọi lại nhiều lần với cùng input.
* Khi bạn muốn tăng tốc độ thuật toán.
* Khi không gian bộ nhớ không quá hạn chế.

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SẬP BẪY")**

* **Chỉ dùng cho hàm đệ quy:** Memoization chỉ có ích cho hàm đệ quy.
* **Không phải lúc nào cũng tốt:** Nếu không có trường hợp lặp, memoization sẽ không hiệu quả, thậm chí còn làm chậm hơn
  do cần thêm thời gian để quản lý bộ nhớ.
* **Chú ý bộ nhớ:** Có thể tốn nhiều bộ nhớ nếu có nhiều kết quả cần lưu.

### **KẾT LUẬN**

Memoization là một kỹ thuật rất hữu ích giúp tối ưu hóa các hàm đệ quy. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn
về nó và có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
