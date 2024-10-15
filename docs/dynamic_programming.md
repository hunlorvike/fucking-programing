## Thuật toán Lập trình động (Dynamic Programming)

**Khái niệm:**

Thuật toán lập trình động là một kỹ thuật giải quyết các bài toán bằng cách chia nhỏ chúng thành các bài toán con, lưu trữ các kết quả trung gian để tránh tính toán lại. Nói cách khác, lập trình động dựa trên nguyên tắc "ghi nhớ" các kết quả đã tính toán trước đó, sử dụng lại chúng để giải quyết các bài toán con tương tự, giúp tối ưu hóa hiệu suất.

**Cách thức hoạt động:**

1. **Xác định các bài toán con:** Chia bài toán gốc thành các bài toán con nhỏ hơn, có cùng loại với bài toán gốc.
2. **Lưu trữ kết quả trung gian:** Tạo một bảng hoặc cấu trúc dữ liệu để lưu trữ kết quả của các bài toán con đã được tính toán.
3. **Sử dụng kết quả đã lưu:** Khi cần giải quyết một bài toán con, kiểm tra xem kết quả của bài toán con này đã được tính toán và lưu trữ chưa. Nếu đã có, sử dụng lại kết quả đó, không cần tính toán lại. Nếu chưa, tính toán kết quả và lưu trữ nó vào bảng.
4. **Kết hợp kết quả:** Kết hợp các kết quả của các bài toán con để tạo ra giải pháp cho bài toán gốc.

**Ưu điểm:**

- **Hiệu quả:** Lập trình động giúp cải thiện hiệu suất của các thuật toán, đặc biệt khi giải quyết các bài toán có tính chất đệ quy hoặc có nhiều trường hợp trùng lặp.
- **Dễ hiểu và triển khai:** Việc triển khai lập trình động thường đơn giản hơn so với các thuật toán đệ quy truyền thống, do việc lưu trữ kết quả trung gian giúp tránh tính toán lại.
- **Tái sử dụng:** Các bảng kết quả có thể được sử dụng lại cho các bài toán tương tự khác, giúp giảm thời gian tính toán.

**Nhược điểm:**

- **Bộ nhớ bổ sung:** Việc lưu trữ kết quả trung gian có thể yêu cầu bộ nhớ bổ sung.
- **Không phù hợp với tất cả các vấn đề:** Lập trình động không phù hợp với các vấn đề có nhiều trường hợp rất khác biệt, hoặc khi chi phí lưu trữ kết quả trung gian quá cao.

**Ví dụ:**

**Bài toán Fibonacci:**

```python
def fibonacci_dp(n):
    """
    Tính số Fibonacci thứ n bằng lập trình động.
    """
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Ví dụ sử dụng
n = 10
fib_num = fibonacci_dp(n)
print(fib_num)  # Output: 55
```

**Giải thích:**

- **Xác định các bài toán con:** Bài toán con là tính số Fibonacci cho các giá trị nhỏ hơn n.
- **Lưu trữ kết quả trung gian:** Tạo một mảng dp để lưu trữ các số Fibonacci đã được tính toán.
- **Sử dụng kết quả đã lưu:** Trong vòng lặp, tính toán số Fibonacci thứ i bằng cách sử dụng kết quả đã lưu trữ của hai số Fibonacci trước đó.
- **Kết hợp kết quả:** Kết quả cuối cùng được trả về là dp[n].

**Ví dụ khác:**

- **Bài toán ba lô:** Tìm cách chọn các đồ vật để đưa vào ba lô sao cho tổng giá trị của các đồ vật được chọn là lớn nhất, đồng thời tổng trọng lượng không vượt quá trọng lượng tối đa của ba lô.
- **Bài toán tối ưu hóa đường đi:** Tìm đường đi ngắn nhất từ điểm A đến điểm B trong một đồ thị.
- **Bài toán chỉnh sửa chuỗi:** Tìm số lượng thao tác cần thiết để biến đổi một chuỗi thành một chuỗi khác.

**Kết luận:**

Lập trình động là một kỹ thuật hữu ích để giải quyết các vấn đề đệ quy và các vấn đề có tính chất tối ưu hóa. Nó giúp cải thiện hiệu suất của thuật toán bằng cách tránh tính toán lại các kết quả trung gian.
