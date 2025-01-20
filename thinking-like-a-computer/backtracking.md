## **🚀 "GIẢI MÃ" THUẬT TOÁN BACKTRACKING: TÌM KIẾM LÙI CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán cực kỳ thú vị và hữu ích:
Backtracking (tìm kiếm lùi). Đây là một kỹ thuật giải quyết vấn đề dựa trên việc thử và sai, rất hữu ích cho các bài
toán có nhiều khả năng. Cùng mình "mổ xẻ" nó nhé!

### **I. BACKTRACKING LÀ GÌ?**

* **Backtracking (Tìm kiếm lùi):** Là thuật toán giải quyết vấn đề bằng cách "thử" từng bước, nếu "sai đường" thì quay
  lại bước trước để thử hướng khác.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn đi lạc trong mê cung: bạn thử từng ngã rẽ, nếu đi vào đường cụt thì quay lại ngã rẽ trước đó để
      đi đường khác.
* **Ưu điểm:**
    * **Tìm được mọi giải pháp:** Có thể tìm hết tất cả các giải pháp có thể của một bài toán.
    * **Dễ hiểu, dễ cài đặt:** Cấu trúc thường khá đơn giản, dễ code.
* **Nhược điểm:**
    * **Có thể chậm:** Nếu không "khéo" có thể duyệt hết mọi trường hợp (tốn thời gian).
    * **Không đảm bảo tối ưu:** Chỉ tìm các giải pháp, không chắc tìm được giải pháp tốt nhất.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Khởi tạo:** Bắt đầu với một giải pháp ban đầu (thường là rỗng).
2. **Mở rộng giải pháp:** Thêm một lựa chọn vào giải pháp hiện tại.
3. **Kiểm tra tính khả thi:** Kiểm tra xem giải pháp hiện tại có thỏa mãn yêu cầu không.
    * Nếu không thỏa mãn, loại bỏ giải pháp đó và quay lại bước 2 (quay lui).
    * Nếu thỏa mãn, tiếp tục mở rộng giải pháp.
4. **Kiểm tra giải pháp:** Nếu giải pháp hiện tại đã hoàn chỉnh, lưu lại kết quả.
5. **Quay lui:** Nếu không còn lựa chọn nào để thêm, quay lại bước 2 và thử các lựa chọn khác.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĐỌC TRUYỆN TRANH**

```
backtracking(solution, options):
    IF solution is complete:
        add solution to list of solutions
        RETURN

    FOR option in options:
        IF option is valid for current solution:
            add option to solution
            backtracking(solution, options)
            remove option from solution
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHÉ!)**

* **`backtracking(solution, options)`:** Hàm chính của thuật toán, nhận vào giải pháp hiện tại và các lựa chọn.
* **`IF solution is complete`:** Kiểm tra xem giải pháp đã hoàn chỉnh chưa. Nếu rồi, lưu lại kết quả.
* **`FOR option in options`:** Vòng lặp duyệt qua các lựa chọn.
* **`IF option is valid for current solution`:** Kiểm tra xem lựa chọn hiện tại có hợp lệ không.
* **`add option to solution`:** Thêm lựa chọn vào giải pháp.
* **`backtracking(solution, options)`:** Gọi đệ quy để tiếp tục xây dựng giải pháp.
* **`remove option from solution`:** Loại bỏ lựa chọn để thử các hướng khác (quay lui).

### **V. VÍ DỤ MINH HỌA - BÀI TOÁN N-QUEENS (C#)**

```csharp
using System;
using System.Collections.Generic;

public class NQueens
{
    static bool IsSafe(int[,] board, int row, int col, int n)
    {
        // Kiểm tra cột
        for (int i = 0; i < row; i++)
        {
            if (board[i, col] == 1)
                return false;
        }

        // Kiểm tra đường chéo chính
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        {
            if (board[i, j] == 1)
                return false;
        }

        // Kiểm tra đường chéo phụ
        for (int i = row, j = col; i >= 0 && j < n; i--, j++)
        {
            if (board[i, j] == 1)
                return false;
        }

        return true;
    }

    static bool SolveNQueensUtil(int[,] board, int row, int n, List<int[,]> solutions)
    {
        if (row == n)
        {
            // Tìm thấy một giải pháp, thêm vào danh sách
            int[,] solution = new int[n, n];
            Array.Copy(board, solution, n * n);
            solutions.Add(solution);
            return true; // hoặc return false để tìm tất cả các lời giải
        }

        bool res = false;
        for (int col = 0; col < n; col++)
        {
            if (IsSafe(board, row, col, n))
            {
                board[row, col] = 1;
                res = SolveNQueensUtil(board, row + 1, n, solutions) || res;
                board[row, col] = 0; // Quay lui: loại bỏ quân hậu
            }
        }
        return res;
    }

    public static List<int[,]> SolveNQueens(int n)
    {
        int[,] board = new int[n, n];
        List<int[,]> solutions = new List<int[,]>();
        if (SolveNQueensUtil(board, 0, n, solutions) == false)
        {
            Console.WriteLine("No solution exists");
        }
        return solutions;
    }

    static void Main(string[] args)
    {
        int n = 4;
        List<int[,]> solutions = SolveNQueens(n);
        foreach (var solution in solutions)
        {
           PrintBoard(solution, n);
        }
    }
        static void PrintBoard(int[,] board, int n)
    {
          for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.Write(board[i, j] + " ");
                }
                Console.WriteLine();
            }
            Console.WriteLine();
    }
}
```

**Giải thích:**

* **`IsSafe`:** Kiểm tra xem vị trí (`row`, `col`) có an toàn để đặt quân hậu không.
* **`SolveNQueensUtil`:** Hàm đệ quy để đặt quân hậu.
    * Nếu đặt được hết quân hậu (`row == n`), lưu giải pháp.
    * Thử từng cột (`col`) cho mỗi hàng (`row`).
    * Nếu vị trí an toàn: đặt quân hậu (`board[row, col] = 1`), gọi đệ quy, rồi loại bỏ quân hậu (`board[row, col] = 0`)
      khi quay lui.
* **`SolveNQueens`:** Hàm gọi để giải bài toán, khởi tạo bàn cờ và gọi `SolveNQueensUtil`.

### **VI. ƯU ĐIỂM CỦA BACKTRACKING (NHỚ LÀM GÌ CŨNG TỐT)**

* **Tìm hết mọi giải pháp:** Tìm tất cả các cách giải quyết bài toán.
* **Dễ code:** Cấu trúc thường khá đơn giản, dễ hiểu.

### **VII. NHƯỢC ĐIỂM CỦA BACKTRACKING (CẨN THẬN LÀM GÌ CŨNG TỐT)**

* **Có thể chậm:** Với bài toán phức tạp, có thể tốn rất nhiều thời gian.
* **Không chắc tối ưu:** Chỉ tìm các giải pháp, không chắc có giải pháp tốt nhất.

### **VIII. KHI NÀO NÊN DÙNG BACKTRACKING (CHỌN ĐÚNG "VŨ KHÍ")**

* Khi bài toán có nhiều khả năng, nhiều hướng đi.
* Khi cần tìm tất cả các giải pháp thỏa mãn điều kiện.
* Khi không cần tối ưu thời gian quá nhiều (có thể chấp nhận chậm).

### **KẾT LUẬN**

Backtracking là một kỹ thuật giải thuật rất thú vị và hữu ích, giúp bạn giải quyết nhiều bài toán phức tạp. Tuy không
phải lúc nào cũng nhanh nhất, nhưng nó là một "vũ khí" quan trọng trong kho tàng kiến thức của dân code. Chúc các bạn
code thành công! 😎
