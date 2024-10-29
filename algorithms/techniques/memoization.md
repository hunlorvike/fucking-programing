## Brute Force (Vét Cạn)

**Khái niệm:**

Brute force (vét cạn) là một phương pháp giải quyết vấn đề bằng cách thử tất cả các giả định có thể xảy ra. Phương pháp này thường được sử dụng khi không có cách giải quyết thông minh hoặc tối ưu hơn cho một vấn đề cụ thể.

**Ứng dụng:** Brute force có thể áp dụng cho nhiều bài toán khác nhau, từ:

- Tìm kiếm chuỗi con trong một chuỗi lớn
- Tìm kiếm từ khoá trong một văn bản
- Giải mã mật khẩu
- Tìm kiếm lời giải cho một bài toán tối ưu hoá

**Ưu điểm:**

- **Độ chính xác cao:** Brute force kiểm tra tất cả các khả năng có thể, do đó, đảm bảo tìm ra kết quả chính xác nếu tồn tại.
- **Dễ hiểu và triển khai:** Vì phương pháp này không yêu cầu kiến thức toán học phức tạp hay thuật toán phức hợp, nên nó dễ hiểu và triển khai trong thực tế.
- **Đảm bảo tìm được kết quả:** Brute force không bỏ sót bất kỳ trường hợp nào, đảm bảo rằng không có giải pháp nào được bỏ qua.

**Nhược điểm:**

- **Tốn thời gian và tài nguyên:** Vì brute force kiểm tra tất cả các khả năng có thể, nên nó có thể tốn nhiều thời gian và tài nguyên tính toán khi bài toán có quá nhiều khả năng.
- **Không hiệu quả với bài toán lớn:** Khi số lượng khả năng cần kiểm tra quá lớn, brute force trở nên không khả thi vì yêu cầu một lượng lớn thời gian và tài nguyên để hoàn thành.

**Kết luận:** Brute force là một phương pháp đơn giản và dễ hiểu, nhưng không hiệu quả với các bài toán lớn hoặc có nhiều khả năng. Nó có thể được sử dụng như một phương pháp cuối cùng khi không có giải pháp tối ưu nào khác.

## Ví dụ Brute Force trong Giải Thuật: Tìm Kiếm Mật Khẩu

Giả sử chúng ta có một mật khẩu được mã hóa và muốn tìm ra mật khẩu gốc.

**Giả định:**

- Mật khẩu chỉ bao gồm các chữ cái thường từ a đến z.
- Chiều dài mật khẩu tối đa là 4 ký tự.

**Thuật toán Brute Force:**

1. **Khởi tạo:** Tạo một danh sách tất cả các khả năng có thể cho mật khẩu, từ "aaaa" đến "zzzz".
2. **Lặp lại:** Duyệt qua từng khả năng trong danh sách:
   - Mã hóa khả năng hiện tại.
   - So sánh kết quả mã hóa với mật khẩu được mã hóa.
   - Nếu kết quả trùng khớp, thì khả năng hiện tại là mật khẩu gốc.
3. **Kết thúc:** Nếu đã duyệt hết danh sách mà không tìm được mật khẩu gốc, thì mật khẩu không nằm trong danh sách khả năng.

**Mã ví dụ (Python):**

```python
import hashlib

def brute_force_password(encoded_password):
  for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
      for k in range(ord('a'), ord('z') + 1):
        for l in range(ord('a'), ord('z') + 1):
          password = chr(i) + chr(j) + chr(k) + chr(l)
          encoded_guess = hashlib.sha256(password.encode()).hexdigest()
          if encoded_guess == encoded_password:
            return password
  return "Mật khẩu không tìm thấy"

encoded_password = "e4d909c290d0fb1ca068c9e2ea81a359"
password = brute_force_password(encoded_password)
print(f"Mật khẩu là: {password}")
```

**Lưu ý:**

- Mã ví dụ trên chỉ là minh họa đơn giản. Trong thực tế, brute force có thể tốn rất nhiều thời gian cho các mật khẩu dài hoặc có nhiều ký tự hơn.
- Brute force không phải là giải pháp tối ưu cho việc giải mã mật khẩu. Nên sử dụng các phương pháp bảo mật tốt hơn như sử dụng mật khẩu mạnh và lưu trữ mật khẩu an toàn.

**Kết luận:**

Brute force là một thuật toán đơn giản nhưng có thể tốn nhiều thời gian để tìm ra kết quả. Nó thường được sử dụng trong các trường hợp đơn giản hoặc khi không có phương pháp tối ưu nào khác.

---

## Thuật toán Memoization (Ghi nhớ)

**Khái niệm:**

Memoization là một kỹ thuật tối ưu hóa hiệu suất của các hàm đệ quy bằng cách lưu trữ kết quả của các cuộc gọi hàm đã được tính toán trước đó. Khi một hàm được gọi lại với cùng một tập hợp các tham số đầu vào, kết quả được lưu trữ sẽ được sử dụng trực tiếp, tránh tính toán lại.

**Cách thức hoạt động:**

1. **Tạo bảng lưu trữ:** Tạo một bảng (thường là một dictionary) để lưu trữ kết quả của các cuộc gọi hàm đã được tính toán.
2. **Kiểm tra bảng lưu trữ:** Trước khi tính toán kết quả của một cuộc gọi hàm, kiểm tra xem kết quả đã được lưu trữ trong bảng chưa.
   - Nếu đã có, trả về kết quả đã lưu trữ.
   - Nếu chưa, tính toán kết quả và lưu trữ nó vào bảng.
3. **Trả về kết quả:** Trả về kết quả được tính toán hoặc kết quả đã lưu trữ.

**Ưu điểm:**

- **Cải thiện hiệu suất:** Memoization có thể giúp cải thiện hiệu suất của các hàm đệ quy, đặc biệt là khi hàm được gọi nhiều lần với cùng một tập hợp các tham số đầu vào.
- **Dễ triển khai:** Memoization thường dễ dàng triển khai bằng cách sử dụng một dictionary hoặc một bảng lưu trữ.

**Nhược điểm:**

- **Bộ nhớ bổ sung:** Memoization yêu cầu bộ nhớ bổ sung để lưu trữ kết quả của các cuộc gọi hàm.
- **Không phù hợp với tất cả các vấn đề:** Memoization không phù hợp với các hàm không có tính chất đệ quy hoặc có nhiều trường hợp rất khác biệt.

**Ví dụ:**

**Bài toán Fibonacci:**

```python
def fibonacci_memo(n, memo={}):
  """
  Tính số Fibonacci thứ n bằng memoization.
  """
  if n in memo:
    return memo[n]
  if n <= 1:
    return n
  else:
    result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    memo[n] = result
    return result

# Ví dụ sử dụng
n = 10
fib_num = fibonacci_memo(n)
print(fib_num)  # Output: 55
```

**Giải thích:**

- **Tạo bảng lưu trữ:** Sử dụng dictionary `memo` để lưu trữ kết quả của các cuộc gọi hàm đã được tính toán.
- **Kiểm tra bảng lưu trữ:** Kiểm tra xem `n` có tồn tại trong `memo` không. Nếu có, trả về giá trị đã lưu trữ.
- **Tính toán và lưu trữ:** Nếu `n` không tồn tại trong `memo`, tính toán kết quả và lưu trữ nó vào `memo`.
- **Trả về kết quả:** Trả về kết quả được tính toán hoặc kết quả đã lưu trữ.

**Kết luận:**

Memoization là một kỹ thuật tối ưu hóa hiệu suất rất hiệu quả cho các hàm đệ quy. Nó có thể giúp cải thiện tốc độ của các hàm đệ quy bằng cách tránh tính toán lại các kết quả đã được tính toán trước đó.
