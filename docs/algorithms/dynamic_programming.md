## Thuật toán Lập trình động (Dynamic Programming - DP)

### Giới thiệu

Lập trình động (Dynamic Programming - DP) là một kỹ thuật tối ưu hóa trong lập trình được sử dụng để giải quyết các bài toán có tính chất chồng lặp và con trỏ tối ưu. Ý tưởng chính là chia nhỏ bài toán phức tạp thành những bài toán con đơn giản hơn và lưu trữ kết quả của các bài toán con này để tránh việc tính toán lại nhiều lần.

### Cách hoạt động

1. **Xác định tính chất:** Kiểm tra xem bài toán có hai tính chất quan trọng của lập trình động là con trỏ tối ưu (Optimal Substructure) và tính chất chồng lặp (Overlapping Subproblems) hay không.
2. **Xây dựng bảng DP:** Tạo một bảng DP để lưu trữ kết quả của các bài toán con.
3. **Tính toán từ dưới lên (Bottom-up):** Bắt đầu từ các bài toán con nhỏ nhất và giải dần lên bài toán lớn hơn. Lưu trữ kết quả của mỗi bài toán con vào bảng DP.
4. **Sử dụng kết quả đã lưu:** Khi gặp lại một bài toán con đã được tính toán, thay vì tính toán lại, ta chỉ cần lấy kết quả từ bảng DP.
5. **Trả về kết quả:** Kết quả cuối cùng của bài toán lớn được lưu trữ trong bảng DP.

### Hai tính chất quan trọng:

**1. Con trỏ tối ưu (Optimal Substructure):**

- Lời giải của bài toán lớn có thể được xây dựng từ lời giải của các bài toán con.
- Ví dụ: Trong bài toán tìm đường đi ngắn nhất, đường đi ngắn nhất từ A đến C sẽ bao gồm đường đi ngắn nhất từ A đến B và từ B đến C.

**2. Tính chất chồng lặp (Overlapping Subproblems):**

- Bài toán lớn sẽ có những bài toán con giống nhau và xuất hiện nhiều lần.
- Ví dụ: Trong bài toán Fibonacci, để tính F(5), ta cần tính F(4) và F(3), nhưng để tính F(4), ta lại cần F(3) và F(2), nghĩa là F(3) bị tính lại nhiều lần.

### Cách tiếp cận:

**1. Top-down (Memoization - Ghi nhớ):**

- Bắt đầu từ bài toán lớn nhất và chia nhỏ nó thành các bài toán con.
- Khi gặp một bài toán con, nếu bài toán này đã được giải và kết quả đã được lưu trữ, ta không tính lại mà lấy kết quả từ bộ nhớ (cache).
- Ví dụ: Nếu đã tính F(3) trong bài toán Fibonacci, lần sau gặp lại ta sẽ dùng ngay kết quả mà không tính lại.

**2. Bottom-up (Tabulation - Lập bảng):**

- Bắt đầu từ các bài toán con nhỏ nhất và giải dần lên bài toán lớn hơn.
- Tất cả các kết quả đều được lưu trữ trong một bảng để sử dụng lại.
- Ví dụ: Trong bài toán Fibonacci, thay vì tính ngược từ F(n), ta tính dần từ F(1), F(2), rồi mới đến F(n).

### Ví dụ cụ thể với bài toán Fibonacci:

**Bài toán Fibonacci:** Tính số Fibonacci thứ n, được định nghĩa như sau:

```
F(n) = F(n-1) + F(n-2)
```

Với điều kiện:

```
F(0) = 0, F(1) = 1
```

**3.1. Sử dụng phương pháp Top-down (Memoization):**

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Ví dụ: Tính F(6)
print(fibonacci_memo(6))  # Output: 8
```

**3.2. Sử dụng phương pháp Bottom-up (Tabulation):**

```python
def fibonacci_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)  # Tạo một bảng dp để lưu kết quả
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Ví dụ: Tính F(6)
print(fibonacci_tabulation(6))  # Output: 8
```

### Một số bài toán kinh điển áp dụng lập trình động:

- **Bài toán xếp ba lô (Knapsack Problem):** Tìm cách tối ưu để chọn đồ vật sao cho tổng giá trị tối đa nhưng không vượt quá trọng lượng của ba lô.
- **Bài toán đường đi ngắn nhất:** Tìm đường đi ngắn nhất giữa các điểm trong một đồ thị (ví dụ: Floyd-Warshall, Dijkstra).
- **Bài toán cắt thanh (Rod Cutting Problem):** Cắt một thanh dài thành các đoạn nhỏ sao cho tổng giá trị thu được là lớn nhất.
- **Bài toán con chung dài nhất (Longest Common Subsequence - LCS):** Tìm chuỗi con chung dài nhất giữa hai chuỗi.

### Các bước giải một bài toán lập trình động:

1. **Xác định bài toán con:** Tìm các bài toán con lặp đi lặp lại.
2. **Xác định công thức quy hoạch động (DP formula):** Thiết lập công thức để tính bài toán lớn dựa trên các bài toán con.
3. **Lựa chọn phương pháp:** Xác định bạn muốn sử dụng phương pháp Top-down hay Bottom-up.
4. **Tối ưu hóa bộ nhớ (nếu cần):** Trong một số bài toán, bạn có thể tối ưu hóa bộ nhớ bằng cách chỉ lưu trữ các giá trị cần thiết thay vì lưu toàn bộ bảng (như bài toán Fibonacci chỉ cần lưu hai giá trị trước đó).

### Ưu điểm:

- **Giải quyết các bài toán phức tạp:** Lập trình động có thể giải quyết các bài toán phức tạp bằng cách chia nhỏ chúng thành các bài toán con đơn giản hơn.
- **Tối ưu hóa thời gian:** Bằng cách lưu trữ kết quả của các bài toán con, lập trình động tránh việc tính toán lại nhiều lần, giúp tối ưu hóa thời gian chạy.

### Nhược điểm:

- **Sử dụng nhiều bộ nhớ:** Lập trình động thường yêu cầu nhiều bộ nhớ để lưu trữ bảng DP.
- **Khó hiểu:** Khái niệm lập trình động có thể khó hiểu đối với những người mới bắt đầu.

### Lưu ý:

- Lập trình động là một kỹ thuật mạnh mẽ giúp tối ưu hóa các giải pháp cho nhiều bài toán.
- Hiểu rõ các tính chất của bài toán và lựa chọn phương pháp phù hợp là điều quan trọng để áp dụng lập trình động hiệu quả.
- Việc tối ưu hóa bộ nhớ là một yếu tố cần lưu ý trong một số bài toán để tránh lãng phí tài nguyên.
