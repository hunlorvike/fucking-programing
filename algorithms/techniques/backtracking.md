## Thuật toán Backtracking (Tìm kiếm lùi)

**Khái niệm:**

Thuật toán Backtracking là một kỹ thuật giải quyết vấn đề bằng cách khám phá hệ thống các giải pháp tiềm năng, loại bỏ
các giải pháp không khả thi và quay trở lại để thử các giải pháp khác. Nó thường được sử dụng để tìm kiếm tất cả các
giải pháp hoặc giải pháp tốt nhất cho một vấn đề.

**Cách thức hoạt động:**

1. **Khởi tạo:** Khởi tạo một giải pháp ban đầu (thường là giải pháp rỗng).
2. **Mở rộng giải pháp:** Thêm một lựa chọn vào giải pháp hiện tại.
3. **Kiểm tra tính khả thi:** Kiểm tra xem giải pháp hiện tại có khả thi hay không.
    - Nếu không khả thi, loại bỏ giải pháp này và quay lại bước 2.
    - Nếu khả thi, tiếp tục mở rộng giải pháp.
4. **Kiểm tra giải pháp:** Nếu giải pháp hiện tại là một giải pháp hoàn chỉnh, ghi nhận lại giải pháp này.
5. **Quay lui:** Nếu không còn lựa chọn nào để thêm vào giải pháp, quay lại bước 2 và thử các lựa chọn khác.

**Ưu điểm:**

- **Tìm kiếm tất cả các giải pháp:** Thuật toán Backtracking có thể tìm kiếm tất cả các giải pháp khả thi cho một vấn
  đề.
- **Dễ hiểu và triển khai:** Thuật toán Backtracking thường dễ hiểu và dễ triển khai, đặc biệt là khi sử dụng ngôn ngữ
  lập trình có hỗ trợ đệ quy.

**Nhược điểm:**

- **Hiệu suất:** Thuật toán Backtracking có thể rất tốn kém về hiệu suất, đặc biệt là với các vấn đề có không gian tìm
  kiếm lớn.
- **Không đảm bảo tối ưu:** Thuật toán Backtracking không đảm bảo tìm ra giải pháp tốt nhất cho một vấn đề, nó chỉ tìm
  kiếm tất cả các giải pháp khả thi.

**Ví dụ:**

**Bài toán N-Queen:**

Bài toán đặt N quân hậu trên bàn cờ vua N x N sao cho không có hai quân hậu nào tấn công nhau.

```python
def solve_nqueens(n):
    """
    Giải bài toán N-Queen bằng thuật toán Backtracking.
    """
    board = [[-1] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        """
        Kiểm tra xem vị trí hiện tại có an toàn hay không.
        """
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, n, 1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(row):
        """
        Tìm kiếm lùi để đặt quân hậu cho mỗi hàng.
        """
        if row == n:
            # Tìm được một giải pháp.
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = -1

    solve(0)
    return solutions

# Ví dụ sử dụng
n = 4
solutions = solve_nqueens(n)
print(solutions)
```

**Giải thích:**

- **Khởi tạo:** Khởi tạo một bàn cờ rỗng (board).
- **Mở rộng giải pháp:** Thêm một quân hậu vào một cột của hàng hiện tại (row).
- **Kiểm tra tính khả thi:** Kiểm tra xem vị trí hiện tại có an toàn hay không, tức là không có quân hậu nào tấn công vị
  trí này.
- **Kiểm tra giải pháp:** Nếu tất cả N quân hậu đã được đặt, ghi nhận lại giải pháp.
- **Quay lui:** Nếu không còn cột nào khả thi cho hàng hiện tại, quay lại hàng trước đó và thử các cột khác.

**Kết luận:**

Thuật toán Backtracking là một kỹ thuật giải quyết vấn đề hiệu quả cho các bài toán tìm kiếm tất cả các giải pháp hoặc
giải pháp tốt nhất. Tuy nhiên, nó có thể tốn kém về hiệu suất, đặc biệt là với các vấn đề có không gian tìm kiếm lớn.
