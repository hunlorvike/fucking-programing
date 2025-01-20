## **🚀 "GIẢI MÃ" LẬP TRÌNH ĐỘNG (DYNAMIC PROGRAMMING): "BÍ KÍP" TỐI ƯU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một kỹ thuật cực kỳ quan trọng và mạnh mẽ trong lập
trình: Dynamic Programming (Quy hoạch động). Nghe có vẻ "cao siêu" nhưng thực ra rất dễ hiểu nếu mình "mổ xẻ" nó ra.
Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. DYNAMIC PROGRAMMING LÀ GÌ?**

* **Dynamic Programming (Lập trình động - DP):** Là kỹ thuật giải quyết bài toán bằng cách chia nhỏ bài toán lớn thành
  các bài toán con nhỏ hơn, giải các bài toán con rồi lưu lại kết quả để dùng tiếp, không cần phải tính lại.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn làm một bài toán phức tạp: bạn chia nó thành các bài toán nhỏ, giải quyết từng bài, rồi ghép các
      kết quả lại.
* **Ưu điểm:**
    * **Tối ưu:** Giải quyết bài toán tối ưu (tìm max, min, ...).
    * **Hiệu quả:** Giảm thời gian chạy bằng cách tránh tính toán lại.
* **Nhược điểm:**
    * **Có thể phức tạp:** Đòi hỏi phải xác định các bài toán con và công thức.
    * **Tốn bộ nhớ:** Cần bộ nhớ để lưu kết quả các bài toán con.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Xác định tính chất:** Kiểm tra xem bài toán có 2 tính chất:
    * **Bài toán con lặp (Overlapping Subproblems):** Có các bài toán con bị lặp lại nhiều lần.
    * **Cấu trúc tối ưu (Optimal Substructure):** Giải pháp của bài toán lớn được xây dựng từ giải pháp của các bài toán
      con.
2. **Xây dựng bảng DP:** Tạo một bảng (hoặc cấu trúc dữ liệu) để lưu kết quả các bài toán con.
3. **Tính toán từ dưới lên (Bottom-up) hoặc từ trên xuống (Top-down):**
    * **Bottom-up:** Giải các bài toán con nhỏ trước rồi đến bài lớn hơn (lưu kết quả vào bảng).
    * **Top-down:** Chia bài toán lớn thành bài toán con, nếu chưa giải thì giải, rồi lưu vào bảng.
4. **Sử dụng kết quả đã lưu:** Khi cần kết quả của bài toán con đã giải, chỉ cần lấy trong bảng.
5. **Trả về kết quả:** Kết quả cuối cùng là kết quả của bài toán lớn.

### **III. HAI TÍNH CHẤT QUAN TRỌNG CỦA DP (NHƯ "ĐIỀU KIỆN CẦN" VẬY)**

1. **Bài toán con lặp (Overlapping Subproblems):**
    * Bài toán lớn chứa các bài toán con nhỏ hơn, và các bài toán con này bị lặp lại nhiều lần.
    * **Ví dụ:** Trong Fibonacci, để tính F(5) cần F(4) và F(3), nhưng để tính F(4) cũng cần F(3), F(2). Vậy F(3) bị
      lặp.
2. **Cấu trúc tối ưu (Optimal Substructure):**
    * Giải pháp tối ưu của bài toán lớn được xây dựng từ giải pháp tối ưu của các bài toán con.
    * **Ví dụ:** Trong bài toán đường đi ngắn nhất, đường đi ngắn nhất từ A -> C sẽ đi qua một điểm B, và đường từ A ->
      B và B-> C cũng phải là ngắn nhất.

### **IV. HAI CÁCH TIẾP CẬN: TOP-DOWN VÀ BOTTOM-UP (CHO DỄ HIỂU)**

1. **Top-down (Memoization - Ghi nhớ):**
    * Bắt đầu từ bài toán lớn, chia thành bài toán con.
    * Nếu đã giải bài toán con rồi, thì dùng kết quả đã lưu (không cần tính lại).
    * **Ví dụ:** Tính Fibonacci từ F(n) -> F(n-1), F(n-2), nếu F(n-1) đã tính rồi thì lấy ra dùng.
2. **Bottom-up (Tabulation - Lập bảng):**
    * Bắt đầu từ bài toán con nhỏ nhất, rồi tính đến bài lớn hơn.
    * Lưu kết quả vào bảng để dùng lại.
    * **Ví dụ:** Tính Fibonacci từ F(0), F(1), F(2), ... rồi đến F(n).

### **V. VÍ DỤ THỰC TẾ - BÀI TOÁN FIBONACCI (C#)**

1. **Top-down (Memoization):**

```csharp
using System;
using System.Collections.Generic;

public class FibonacciMemo
{
    static Dictionary<int, int> memo = new Dictionary<int, int>();

    public static int Fibonacci(int n)
    {
        if (memo.ContainsKey(n))
        {
            return memo[n];
        }

        if (n <= 1)
        {
            return n;
        }

        memo[n] = Fibonacci(n - 1) + Fibonacci(n - 2);
        return memo[n];
    }

    public static void Main(string[] args)
    {
        int n = 6;
        Console.WriteLine($"Fibonacci({n}) = {Fibonacci(n)}"); // Output: Fibonacci(6) = 8
    }
}
```

2. **Bottom-up (Tabulation):**

```csharp
using System;

public class FibonacciTabulation
{
    public static int Fibonacci(int n)
    {
        if (n <= 1)
        {
            return n;
        }

        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public static void Main(string[] args)
    {
        int n = 6;
        Console.WriteLine($"Fibonacci({n}) = {Fibonacci(n)}"); // Output: Fibonacci(6) = 8
    }
}
```

### **VI. MỘT SỐ BÀI TOÁN KINH ĐIỂN (CÓ THỂ GẶP)**

1. **Bài toán ba lô (Knapsack):** Chọn vật phẩm sao cho tổng giá trị lớn nhất mà không vượt quá trọng lượng.
2. **Đường đi ngắn nhất:** Tìm đường đi ngắn nhất giữa các điểm (Dijkstra, Floyd-Warshall).
3. **Cắt thanh (Rod Cutting):** Cắt thanh thành các đoạn nhỏ để có tổng giá trị lớn nhất.
4. **Chuỗi con chung dài nhất (LCS):** Tìm chuỗi con chung dài nhất của 2 chuỗi.

### **VII. CÁC BƯỚC GIẢI BÀI TOÁN DP (TỪ TỪ LÀM THEO)**

1. **Xác định bài toán con:** Tìm các bài toán con bị lặp.
2. **Xác định công thức:** Viết công thức để tính bài toán lớn từ bài toán con.
3. **Chọn Top-down hoặc Bottom-up:** Chọn cách tiếp cận phù hợp.
4. **Tối ưu bộ nhớ:** Nếu cần, tối ưu bộ nhớ để tránh lãng phí.

### **VIII. ƯU ĐIỂM CỦA DYNAMIC PROGRAMMING (ĐIỂM MẠNH)**

* **Tối ưu thời gian:** Tránh tính toán lại, chạy nhanh hơn.
* **Hiệu quả:** Giải quyết các bài toán tối ưu một cách chính xác.

### **IX. NHƯỢC ĐIỂM CỦA DYNAMIC PROGRAMMING (ĐIỂM YẾU)**

* **Tốn bộ nhớ:** Cần bộ nhớ để lưu bảng DP.
* **Khó hiểu:** Đòi hỏi tư duy logic để xác định bài toán con và công thức.

### **X. LƯU Ý QUAN TRỌNG (ĐỪNG QUÊN)**

* DP là kỹ thuật mạnh, nhưng không phải "vạn năng".
* Cần xác định đúng bài toán con và công thức truy hồi.
* Có thể cần tối ưu bộ nhớ để không tốn quá nhiều.

### **KẾT LUẬN**

Dynamic Programming là một kỹ thuật cực kỳ quan trọng trong lập trình, giúp bạn giải quyết nhiều bài toán phức tạp một
cách tối ưu. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó. Chúc các bạn code thành công! 😎
