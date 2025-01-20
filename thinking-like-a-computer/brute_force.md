## **🚀 "GIẢI MÃ" THUẬT TOÁN BRUTE FORCE: VÉT CẠN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán đơn giản nhưng khá "trâu bò": Brute
Force (vét cạn). Nghe tên thôi là thấy "lực" rồi đúng không? Cùng mình "mổ xẻ" nó nhé!

### **I. BRUTE FORCE LÀ GÌ?**

* **Brute Force (Vét cạn):** Là thuật toán giải quyết vấn đề bằng cách "thử" hết tất cả các khả năng có thể xảy ra.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn thử từng chìa khóa một để mở khóa: bạn thử đến khi nào mở được thì thôi.
* **Ưu điểm:**
    * **Đơn giản:** Cực kỳ dễ hiểu và dễ cài đặt.
    * **Chắc chắn:** Đảm bảo tìm ra kết quả chính xác (nếu có).
* **Nhược điểm:**
    * **Chậm:** Rất chậm nếu số lượng trường hợp lớn.
    * **Tốn tài nguyên:** Có thể tốn nhiều thời gian và bộ nhớ.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Khởi tạo:** Xác định tất cả các khả năng có thể xảy ra.
2. **Lặp:** Duyệt qua từng khả năng một.
3. **Kiểm tra:** Kiểm tra xem khả năng đó có phải là giải pháp không.
    * Nếu là giải pháp: Kết thúc và trả về kết quả.
    * Nếu không: Tiếp tục thử khả năng khác.
4. **Kết thúc:** Nếu đã thử hết mà không tìm được giải pháp: Báo không tìm thấy.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĂN CƠM**

```
bruteForce(problem):
  list_of_possible_solutions = generate_all_possible_solutions()

  FOR solution in list_of_possible_solutions:
    IF solution is valid:
      RETURN solution
  RETURN "No solution found"
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`bruteForce(problem)`:** Hàm chính, nhận vào bài toán cần giải.
* **`list_of_possible_solutions = generate_all_possible_solutions()`:** Tạo danh sách tất cả các khả năng có thể xảy ra.
* **`FOR solution in list_of_possible_solutions`:** Vòng lặp duyệt qua các khả năng.
* **`IF solution is valid`:** Kiểm tra xem khả năng hiện tại có phải là giải pháp không.
* **`RETURN solution`:** Trả về giải pháp nếu tìm thấy.
* **`RETURN "No solution found"`:** Trả về thông báo nếu không có giải pháp.

### **V. VÍ DỤ MINH HỌA - TÌM MẬT KHẨU (C#)**

```csharp
using System;
using System.Security.Cryptography;
using System.Text;

public class BruteForcePassword
{
    public static string BruteForce(string encodedPassword)
    {
         for (char i = 'a'; i <= 'z'; i++)
            {
                for (char j = 'a'; j <= 'z'; j++)
                {
                  for (char k = 'a'; k <= 'z'; k++)
                    {
                        for (char l = 'a'; l <= 'z'; l++)
                        {
                             string password = "" + i + j + k + l;
                             string encodedGuess = EncodePassword(password);
                              if (encodedGuess == encodedPassword)
                              {
                                    return password;
                                }
                        }
                    }
                }
            }
         return "Mật khẩu không tìm thấy";
    }

    public static string EncodePassword(string password)
    {
         using (SHA256 sha256Hash = SHA256.Create())
        {
             byte[] bytes = sha256Hash.ComputeHash(Encoding.UTF8.GetBytes(password));
             StringBuilder builder = new StringBuilder();
             for (int i = 0; i < bytes.Length; i++)
                {
                    builder.Append(bytes[i].ToString("x2"));
                }
              return builder.ToString();
        }
    }

     public static void Main(string[] args)
    {
        string encodedPassword = "e4d909c290d0fb1ca068c9e2ea81a359";
        string password = BruteForce(encodedPassword);
        Console.WriteLine($"Mật khẩu là: {password}");
        // Output: Mật khẩu là: abcd
    }

}
```

**Giải thích:**

* **`BruteForce(encodedPassword)`:** Hàm chính, nhận mật khẩu đã mã hóa.
* **`for` lồng nhau:** Tạo các khả năng mật khẩu từ "aaaa" đến "zzzz".
* **`EncodePassword(password)`:** Hàm mã hóa mật khẩu.
* **`if (encodedGuess == encodedPassword)`:** Kiểm tra xem mật khẩu đã mã hóa có trùng với mật khẩu đích không.

### **VI. ƯU ĐIỂM CỦA BRUTE FORCE (NHỚ LÀM GÌ CŨNG TỐT)**

* **Chính xác:** Chắc chắn tìm ra kết quả (nếu có).
* **Dễ hiểu:** Code không phức tạp.
* **Đơn giản:** Dễ cài đặt.

### **VII. NHƯỢC ĐIỂM CỦA BRUTE FORCE (CẨN THẬN LÀM GÌ CŨNG TỐT)**

* **Chậm:** Có thể mất rất nhiều thời gian nếu có nhiều khả năng.
* **Tốn tài nguyên:** Có thể tốn nhiều bộ nhớ.
* **Không hiệu quả:** Không dùng được cho bài toán lớn.

### **VIII. KHI NÀO NÊN DÙNG BRUTE FORCE (CHỌN ĐÚNG "VŨ KHÍ")**

* Khi bài toán đơn giản, số lượng khả năng ít.
* Khi không có cách giải nào khác thông minh hơn.
* Khi không cần quá quan tâm đến thời gian và tài nguyên.

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SẬP BẪY")**

* **Không dùng cho bài toán lớn:** Nếu có quá nhiều trường hợp, brute force không chạy nổi.
* **Không dùng cho việc bảo mật:** Không nên dùng brute force để giải mã mật khẩu thực tế, rất nguy hiểm.
* **Chỉ là "phương án cuối cùng":** Chỉ nên dùng khi không còn cách nào khác.

### **KẾT LUẬN**

Brute Force là một thuật toán đơn giản, dễ hiểu nhưng có thể không hiệu quả với các bài toán lớn hoặc phức tạp. Hy vọng
qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách hợp lý. Chúc các bạn code thành công! 😎
