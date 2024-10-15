## Brute Force (Vét Cạn)

**Khái niệm:** Brute force (vét cạn) là một phương pháp giải quyết vấn đề bằng cách thử tất cả các giả định có thể xảy ra. Phương pháp này thường được sử dụng khi không có cách giải quyết thông minh hoặc tối ưu hơn cho một vấn đề cụ thể.

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
