## **🚀 "GIẢI MÃ" BACKTRACKING VS DYNAMIC PROGRAMMING: KHI NÀO DÙNG CÁI NÀO CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "mổ xẻ" hai kỹ thuật giải thuật rất quan trọng và hay bị nhầm
lẫn: Backtracking (quay lui) và Dynamic Programming (quy hoạch động). Nghe có vẻ "khoai" nhưng thực ra rất thú vị và hữu
ích đấy. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. BACKTRACKING VS DYNAMIC PROGRAMMING: LÀ GÌ VẬY?**

* **Backtracking (Quay lui):** Là kỹ thuật "thử và sai", đi từng bước, nếu "sai đường" thì quay lại bước trước thử hướng
  khác.
* **Dynamic Programming (Quy hoạch động):** Là kỹ thuật "chia để trị", chia bài toán thành các bài toán nhỏ hơn, giải
  rồi lưu lại kết quả để dùng tiếp, không cần tính lại.
* **Tóm lại:**
    * **Backtracking:** "Thử nghiệm" nhiều hướng, đi đến đâu biết đến đấy.
    * **Dynamic Programming:** "Lập kế hoạch" trước, giải quyết từng phần, tận dụng kết quả cũ.

### **II. BACKTRACKING (QUAY LUI) - "THỬ SAI KHÔNG THÀNH VẤN ĐỀ"**

#### **2.1. ĐỊNH NGHĨA VÀ NGUYÊN LÝ HOẠT ĐỘNG**

* **Backtracking:**
    * Xây dựng giải pháp từng bước một.
    * Nếu gặp "ngõ cụt" (không thỏa mãn điều kiện), quay lại bước trước và thử hướng khác.
    * Tiếp tục cho đến khi tìm thấy giải pháp hoặc đã thử hết các khả năng.
* **Nguyên lý:** Đi từng bước, gặp sai thì quay lại.

#### **2.2. KHI NÀO NÊN DÙNG?**

1. **Không gian giải pháp lớn:** Nhiều khả năng, nhưng không phải cái nào cũng đúng.
2. **Bài toán tổ hợp, hoán vị:** Tạo ra các cách sắp xếp, chọn nhóm.
3. **Kết hợp heuristic:** Có thể dùng thêm các "mẹo" để giảm không gian tìm kiếm.

#### **2.3. CÁC BÀI TOÁN PHÙ HỢP**

1. **Tô màu đồ thị (Graph Coloring):** Tô màu các đỉnh sao cho các đỉnh kề nhau không cùng màu.
2. **N-Queens:** Đặt N quân hậu lên bàn cờ NxN sao cho không quân nào ăn nhau.
3. **Bài toán tổ hợp, hoán vị:** Tạo các tổ hợp, hoán vị của 1 tập hợp.

#### **2.4. ƯU ĐIỂM**

1. **Dễ cài đặt:** Code không quá phức tạp.
2. **Tìm được mọi phương án:** Tìm tất cả các giải pháp có thể.

#### **2.5. NHƯỢC ĐIỂM**

1. **Chậm:** Có thể phải duyệt hết mọi trường hợp (độ phức tạp thời gian cao).
2. **Không nhớ kết quả cũ:** Phải tính toán lại các bước tương tự nhiều lần.

#### **2.6. VÍ DỤ MINH HỌA - BÀI TOÁN N-QUEENS (C#)**

```csharp
using System;

class NQueens
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

    static bool SolveNQueensUtil(int[,] board, int row, int n)
    {
        if (row == n)
        {
            // In bảng kết quả (nếu muốn)
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.Write(board[i, j] + " ");
                }
                Console.WriteLine();
            }
            Console.WriteLine();
            return true; // hoặc return false để tìm tất cả các lời giải
        }

        bool res = false;
        for (int col = 0; col < n; col++)
        {
            if (IsSafe(board, row, col, n))
            {
                board[row, col] = 1;
                res = SolveNQueensUtil(board, row + 1, n) || res;
                board[row, col] = 0;
            }
        }
        return res;
    }

    public static bool SolveNQueens(int n)
    {
        int[,] board = new int[n, n];
        if (SolveNQueensUtil(board, 0, n) == false)
        {
            Console.WriteLine("No solution exists");
            return false;
        }
        return true;
    }

    static void Main(string[] args)
    {
        int n = 4;
        SolveNQueens(n);
    }
}
```

### **III. DYNAMIC PROGRAMMING (QUY HOẠCH ĐỘNG) - "LẬP KẾ HOẠCH TRƯỚC CHO CHẮC ĂN"**

#### **3.1. ĐỊNH NGHĨA VÀ NGUYÊN LÝ HOẠT ĐỘNG**

* **Dynamic Programming:**
    * Chia bài toán lớn thành các bài toán con nhỏ hơn.
    * Giải các bài toán con một lần, lưu lại kết quả (memoization).
    * Sử dụng kết quả đã lưu để giải bài toán lớn.
* **Nguyên lý:** Giải các bài toán nhỏ trước, dùng kết quả đó cho các bài toán lớn hơn.

#### **3.2. KHI NÀO NÊN DÙNG?**

1. **Bài toán tối ưu:** Tìm giá trị lớn nhất, nhỏ nhất, đường đi ngắn nhất,...
2. **Bài toán "chia để trị" có tính chất lặp:** Các bài toán con bị trùng lặp nhau.
3. **Bài toán với cấu trúc bảng:** Các bài toán trên lưới, ...

#### **3.3. CÁC BÀI TOÁN PHÙ HỢP**

1. **Bài toán ba lô (Knapsack):** Chọn vật phẩm để có tổng giá trị lớn nhất mà không vượt quá trọng lượng cho phép.
2. **Chuỗi con chung dài nhất (LCS):** Tìm chuỗi con chung dài nhất của 2 chuỗi.
3. **Fibonacci, tam giác Pascal:** Các bài toán liên quan đến dãy số.
4. **Đường đi ngắn nhất trên lưới:** Tìm đường đi ngắn nhất giữa 2 điểm trên lưới.

#### **3.4. ƯU ĐIỂM**

1. **Tối ưu thời gian:** Nhờ memoization (lưu kết quả), không cần tính toán lại nhiều lần.
2. **Hiệu quả:** Tìm được giải pháp tối ưu.

#### **3.5. NHƯỢC ĐIỂM**

1. **Tốn bộ nhớ:** Cần bộ nhớ để lưu kết quả trung gian.
2. **Khó cài đặt hơn:** Cần xác định bài toán con và công thức truy hồi.

#### **3.6. VÍ DỤ MINH HỌA - BÀI TOÁN FIBONACCI (C#)**

```csharp
using System;

class Fibonacci
{
    public static int FibonacciDP(int n)
    {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        if (n > 0)
        {
            dp[1] = 1;
        }
        for (int i = 2; i <= n; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    static void Main(string[] args)
    {
        int n = 10;
        Console.WriteLine($"Fibonacci({n}) = {FibonacciDP(n)}");
    }
}
```

### **IV. SO SÁNH CHI TIẾT (TỔNG KẾT LẠI)**

| Yếu tố            | Backtracking                | Dynamic Programming         |
|-------------------|-----------------------------|-----------------------------|
| **Cách tiếp cận** | Thử sai, quay lui           | Chia để trị, lưu kết quả    |
| **Tính toán lặp** | Không nhớ, tính lại         | Nhớ kết quả, không tính lại |
| **Bài toán**      | Tổ hợp, hoán vị, tìm tất cả | Tối ưu, có tính lặp         |
| **Thời gian**     | Thường chậm                 | Thường nhanh hơn            |
| **Bộ nhớ**        | Ít hơn                      | Nhiều hơn                   |
| **Cài đặt**       | Thường dễ hơn               | Phức tạp hơn                |
| **Cắt tỉa**       | Dùng heuristic              | Không cần heuristic         |

### **V. KHI NÀO NÊN DÙNG BACKTRACKING?**

* Khi có nhiều hướng đi và không biết hướng nào là đúng.
* Khi cần tìm tất cả các giải pháp có thể.
* Khi không cần tối ưu thời gian và có thể dùng thêm các "mẹo" để cắt tỉa không gian tìm kiếm.

### **VI. KHI NÀO NÊN DÙNG DYNAMIC PROGRAMMING?**

* Khi bài toán có các bài toán con bị trùng lặp (overlapping subproblems).
* Khi bài toán có cấu trúc tối ưu (optimal substructure).
* Khi cần tìm giải pháp tối ưu (nhất, ngắn nhất, ...).
* Khi muốn giảm thời gian chạy bằng cách lưu kết quả.

### **VII. VÍ DỤ CỤ THỂ (ĐỂ CÁC BẠN THẤY RÕ HƠN)**

1. **Tìm kiếm trên cây (Tree Traversal):**
    * **Backtracking:** Để duyệt cây theo các thứ tự (preorder, inorder, postorder).
    * **Dynamic Programming:** Để tính các thông tin từ cây (chiều cao, số node,...).
2. **Bài toán đếm số cách đi cầu thang:**
    * **Dynamic Programming:** Chia thành các bài toán con, lưu kết quả.

```csharp
using System;

class ClimbStairs
{
    public static int CountWaysToClimb(int n)
    {
        int[] dp = new int[n + 1];
