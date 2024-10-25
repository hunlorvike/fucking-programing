## Độ phức tạp thuật toán: Big-O, Big-Theta, Big-Omega

Độ phức tạp thuật toán là một cách để đánh giá hiệu suất của một thuật toán khi kích thước đầu vào tăng lên. Nó giúp chúng ta so sánh hiệu suất của các thuật toán khác nhau và dự đoán mức độ tiêu thụ tài nguyên (thời gian, bộ nhớ) khi xử lý dữ liệu lớn.

### 1. Big-O, Big-Theta, Big-Omega: Giải thích chi tiết và ví dụ minh họa

**1.1 Big-O (O): Giới hạn trên**

- **Định nghĩa:** Big-O (O) là một ký hiệu toán học dùng để mô tả **giới hạn trên** của tốc độ tăng trưởng của một hàm. Nói cách khác, nó cho biết tốc độ **tối đa** mà một thuật toán có thể chạy, bất kể đầu vào là gì.

- **Cách diễn đạt:** f(n) = O(g(n)) có nghĩa là tồn tại các hằng số dương c và n0 sao cho với mọi n ≥ n0, ta có f(n) ≤ c.g(n). Điều này nghĩa là f(n) tăng trưởng chậm hơn hoặc bằng g(n) khi n tiến về vô cùng.

- **Ý nghĩa:** Big-O thường được sử dụng để mô tả trường hợp **tồi tệ nhất** của một thuật toán. Ví dụ, nếu một thuật toán có độ phức tạp O(n^2), điều đó có nghĩa là thời gian thực thi của nó sẽ không vượt quá một hằng số nhân với n^2, ngay cả khi đầu vào là xấu nhất.

- **Ví dụ:**
  - **O(1):** Thời gian thực thi không đổi, không phụ thuộc vào kích thước đầu vào. Ví dụ: truy cập một phần tử trong mảng.
  - **O(n):** Thời gian thực thi tỷ lệ thuận với kích thước đầu vào. Ví dụ: tìm kiếm một phần tử trong mảng.
  - **O(n^2):** Thời gian thực thi tăng theo bình phương kích thước đầu vào. Ví dụ: sắp xếp nổi bọt (Bubble Sort).

**1.2 Big-Theta (Θ): Giới hạn chính xác**

- **Định nghĩa:** Big-Theta (Θ) là một ký hiệu toán học dùng để mô tả **giới hạn chính xác** của tốc độ tăng trưởng của một hàm. Nó cho biết tốc độ **trung bình** của một thuật toán, cả trong trường hợp tốt nhất và tồi tệ nhất.

- **Cách diễn đạt:** f(n) = Θ(g(n)) có nghĩa là tồn tại các hằng số dương c1, c2, n0 sao cho với mọi n > n0, ta có c1.g(n) ≤ f(n) ≤ c2.g(n). Điều này nghĩa là f(n) tăng trưởng tương tự như g(n) khi n tiến về vô cùng.

- **Ý nghĩa:** Big-Theta cung cấp một cách chính xác hơn để mô tả tốc độ tăng trưởng của thuật toán so với Big-O. Ví dụ, nếu một thuật toán có độ phức tạp Θ(n log n), điều đó có nghĩa là tốc độ thực thi của nó sẽ tăng theo cả hai bên của n log n trong cả trường hợp tốt nhất và tồi tệ nhất.

- **Ví dụ:**
  - **Θ(n):** Thời gian thực thi tỷ lệ thuận với kích thước đầu vào. Ví dụ: sắp xếp chèn (Insertion Sort).
  - **Θ(log n):** Thời gian thực thi logarit với kích thước đầu vào. Ví dụ: tìm kiếm nhị phân (Binary Search).

**1.3 Big-Omega (Ω): Giới hạn dưới**

- **Định nghĩa:** Big-Omega (Ω) là một ký hiệu toán học dùng để mô tả **giới hạn dưới** của tốc độ tăng trưởng của một hàm. Nó cho biết tốc độ **tối thiểu** mà một thuật toán có thể chạy, bất kể đầu vào là gì.

- **Cách diễn đạt:** f(n) = Ω(g(n)) có nghĩa là tồn tại các hằng số dương c và n0 sao cho với mọi n > n0, ta có f(n) ≥ c.g(n). Điều này nghĩa là f(n) tăng trưởng nhanh hơn hoặc bằng g(n) khi n tiến về vô cùng.

- **Ý nghĩa:** Big-Omega thường được sử dụng để mô tả trường hợp **tốt nhất** của một thuật toán. Ví dụ, nếu một thuật toán có độ phức tạp Ω(n), điều đó có nghĩa là thời gian thực thi của nó sẽ ít nhất là một hằng số nhân với n, ngay cả khi đầu vào là tốt nhất.

- **Ví dụ:**
  - **Ω(n):** Thời gian thực thi ít nhất là tỷ lệ thuận với kích thước đầu vào. Ví dụ: sắp xếp lựa chọn (Selection Sort).
  - **Ω(log n):** Thời gian thực thi ít nhất là logarit với kích thước đầu vào. Ví dụ: tìm kiếm nhị phân (Binary Search).

### 2. Các lớp độ phức tạp thường gặp:

| Lớp độ phức tạp | Biểu diễn   | Ý nghĩa                                                         |
| --------------- | ----------- | --------------------------------------------------------------- |
| O(1)            | Constant    | Thời gian chạy không phụ thuộc vào kích thước đầu vào           |
| O(log n)        | Logarithmic | Thời gian chạy tăng logarit theo kích thước đầu vào             |
| O(n)            | Linear      | Thời gian chạy tăng tuyến tính theo kích thước đầu vào          |
| O(n log n)      | Loglinear   | Thời gian chạy tăng logarit tuyến tính theo kích thước đầu vào  |
| O(n^2)          | Quadratic   | Thời gian chạy tăng bậc hai theo kích thước đầu vào             |
| O(n^k)          | Polynomial  | Thời gian chạy tăng bậc k theo kích thước đầu vào               |
| O(2^n)          | Exponential | Thời gian chạy tăng theo lũy thừa của 2 theo kích thước đầu vào |

### 3. Ví dụ tính toán độ phức tạp:

**3.1 Tìm kiếm tuyến tính (Linear Search):**

- Thuật toán: Duyệt qua từng phần tử trong mảng để tìm kiếm mục tiêu.
- Độ phức tạp:
  - Trường hợp tốt nhất (mục tiêu ở vị trí đầu tiên): O(1)
  - Trường hợp trung bình và xấu nhất (mục tiêu ở cuối mảng hoặc không tồn tại): O(n)
  - **Big-O:** O(n)
  - **Big-Theta:** Θ(n)
  - **Big-Omega:** Ω(1)

**3.2 Sắp xếp nổi bọt (Bubble Sort):**

- Thuật toán: So sánh các phần tử kề nhau và hoán đổi chúng cho đến khi mảng được sắp xếp.
- Độ phức tạp:
  - Luôn phải duyệt qua tất cả các phần tử n lần.
  - Độ phức tạp thời gian: O(n^2) cho cả trường hợp tốt nhất, trung bình và xấu nhất.
  - **Big-O:** O(n^2)
  - **Big-Theta:** Θ(n^2)
  - **Big-Omega:** Ω(n^2)

**3.3 Tìm kiếm nhị phân (Binary Search):**

- Thuật toán: Chia mảng đã được sắp xếp thành hai nửa, loại bỏ nửa không chứa mục tiêu và lặp lại quy trình cho đến khi tìm thấy mục tiêu hoặc không còn phần tử nào để kiểm tra.
- Độ phức tạp:
  - Mỗi lần lặp, kích thước mảng giảm đi một nửa.
  - Số lần lặp tối đa là log2(n).
  - **Big-O:** O(log n)
  - **Big-Theta:** Θ(log n)
  - **Big-Omega:** Ω(1)

### 4. Lưu ý:

- Khi phân tích độ phức tạp, chúng ta thường bỏ qua các hằng số và chỉ tập trung vào thuật ngữ chính.
- Độ phức tạp được thể hiện dưới dạng "tốc độ tăng trưởng" của thời gian chạy khi kích thước đầu vào tăng lên.
- Độ phức tạp thời gian chỉ là một trong những yếu tố đánh giá hiệu suất của thuật toán. Ngoài ra còn có độ phức tạp không gian (để đo lượng bộ nhớ sử dụng), độ phức tạp truyền thông (để đo lượng dữ liệu truyền đi), v.v.

### 5. Ứng dụng:

- **Lựa chọn thuật toán:** Độ phức tạp giúp chúng ta lựa chọn thuật toán phù hợp nhất cho một bài toán cụ thể, dựa trên kích thước đầu vào và yêu cầu hiệu suất.
- **Tối ưu hóa code:** Hiểu rõ độ phức tạp giúp chúng ta cải thiện hiệu suất của code bằng cách loại bỏ các vòng lặp không cần thiết hoặc sử dụng các cấu trúc dữ liệu phù hợp.
- **Kiến thức cơ bản về khoa học máy tính:** Độ phức tạp là một kiến thức cơ bản về khoa học máy tính, giúp chúng ta hiểu sâu hơn về cách hoạt động của các thuật toán và cách đánh giá hiệu suất của chúng.

**Lưu ý:**

- Big-O, Big-Theta và Big-Omega là các ký hiệu toán học được sử dụng để mô tả tốc độ tăng trưởng của thuật toán.
- Big-O mô tả giới hạn trên, Big-Theta mô tả giới hạn chính xác và Big-Omega mô tả giới hạn dưới.
- Các ký hiệu này giúp chúng ta so sánh hiệu quả của các thuật toán khác nhau và chọn thuật toán phù hợp nhất cho một bài toán cụ thể.

**Kết luận:**

Độ phức tạp thuật toán là một công cụ quan trọng để đánh giá hiệu suất của các thuật toán. Hiểu rõ các khái niệm Big-O, Big-Theta, và Big-Omega giúp chúng ta lựa chọn thuật toán phù hợp, tối ưu hóa code và nâng cao kiến thức về khoa học máy tính.
