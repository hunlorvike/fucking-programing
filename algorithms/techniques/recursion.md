## Đệ quy (Recursion)

**Khái niệm:**

Đệ quy là một kỹ thuật lập trình trong đó một hàm gọi chính nó trong định nghĩa của nó. Nói cách khác, một hàm đệ quy là
một hàm gọi chính nó để giải quyết một vấn đề nhỏ hơn, và tiếp tục gọi chính nó cho đến khi đạt được trường hợp cơ bản.

**Cách thức hoạt động:**

1. **Trường hợp cơ bản:** Một trường hợp cơ bản là một trường hợp đơn giản của vấn đề, có thể được giải quyết trực tiếp
   mà không cần đệ quy.
2. **Bước đệ quy:** Hàm đệ quy chia vấn đề thành các vấn đề con nhỏ hơn, tương tự như vấn đề ban đầu, và gọi chính nó để
   giải quyết các vấn đề con đó.
3. **Kết hợp kết quả:** Hàm đệ quy kết hợp kết quả của các vấn đề con để tạo ra giải pháp cho vấn đề ban đầu.

**Ưu điểm:**

- **Dễ hiểu:** Đệ quy thường cung cấp một cách dễ hiểu và rõ ràng để giải quyết các vấn đề có tính chất đệ quy.
- **Hiệu quả:** Đệ quy có thể rất hiệu quả trong việc giải quyết các vấn đề có cấu trúc đệ quy.
- **Code ngắn gọn:** Đệ quy có thể giúp viết code ngắn gọn và dễ đọc hơn so với các kỹ thuật khác.

**Nhược điểm:**

- **Hiệu suất:** Đệ quy có thể tốn kém về hiệu suất, đặc biệt là khi số lượng lần đệ quy lớn.
- **Khó debug:** Việc debug code đệ quy có thể khó khăn hơn so với code thông thường.
- **Stack overflow:** Nếu số lượng lần đệ quy quá lớn, có thể dẫn đến lỗi stack overflow.

**Ví dụ:**

**Bài toán tính giai thừa:**

```python
def factorial(n):
  """
  Tính giai thừa của n bằng đệ quy.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Ví dụ sử dụng
n = 5
result = factorial(n)
print(result)  # Output: 120
```

**Giải thích:**

- **Trường hợp cơ bản:** Nếu n bằng 0, trả về 1.
- **Bước đệ quy:** Nếu n lớn hơn 0, trả về n nhân với giai thừa của n - 1.
- **Kết hợp kết quả:** Giai thừa của n được tính bằng cách nhân n với giai thừa của n - 1, cho đến khi đạt được trường
  hợp cơ bản.

**Ví dụ khác:**

- **Bài toán Fibonacci:** Tính số Fibonacci thứ n.
- **Bài toán Hanoi:** Di chuyển đĩa từ một cọc sang cọc khác.
- **Tìm kiếm nhị phân:** Tìm kiếm một phần tử trong danh sách đã được sắp xếp.

**Kết luận:**

Đệ quy là một kỹ thuật lập trình mạnh mẽ và hữu ích, nhưng cần được sử dụng một cách cẩn thận. Nó có thể giúp viết code
ngắn gọn và dễ đọc, nhưng có thể gây ra vấn đề về hiệu suất và debug.
