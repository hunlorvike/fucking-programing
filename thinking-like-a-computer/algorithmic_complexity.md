## **🚀 "GIẢI MÃ" ĐỘ PHỨC TẠP THUẬT TOÁN: BIG-O, BIG-THETA, BIG-OMEGA CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một chủ đề cực kỳ quan trọng trong thuật toán: Độ phức
tạp (complexity). Nghe có vẻ "hack não" nhưng thực ra rất dễ hiểu nếu mình "mổ xẻ" nó ra. Mình sẽ cố gắng giải thích dễ
hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé!

### **I. TẠI SAO PHẢI QUAN TÂM ĐẾN ĐỘ PHỨC TẠP?**

* **Độ phức tạp:** Là thước đo hiệu suất của thuật toán, cho biết thuật toán chạy nhanh hay chậm.
* **Quan trọng vì:**
    * **Biết thuật toán chạy nhanh hay chậm:** Khi xử lý dữ liệu lớn.
    * **So sánh thuật toán:** Chọn thuật toán tốt nhất cho bài toán.
    * **Dự đoán:** Dự đoán tài nguyên (thời gian, bộ nhớ) mà thuật toán cần.
    * **Tối ưu:** Tìm điểm yếu và cải thiện thuật toán.

### **II. KÝ HIỆU BIG-O, BIG-THETA, BIG-OMEGA (NHƯNG CÁI "MÁC" CHO THUẬT TOÁN)**

* **Big-O (O):** Giới hạn trên, tốc độ *tồi tệ nhất* của thuật toán.
* **Big-Theta (Θ):** Giới hạn chính xác, tốc độ *trung bình* của thuật toán.
* **Big-Omega (Ω):** Giới hạn dưới, tốc độ *tốt nhất* của thuật toán.

### **III. ĐỘ PHỨC TẠP THỜI GIAN VÀ KHÔNG GIAN (NHỮNG GÌ THUẬT TOÁN CẦN)**

* **Độ phức tạp thời gian:** Thời gian chạy của thuật toán (theo kích thước đầu vào).
* **Độ phức tạp không gian:** Lượng bộ nhớ mà thuật toán cần (theo kích thước đầu vào).

### **IV. BIG-O (O) - "TỐI TỆ NHƯNG KHÔNG THỂ TỆ HƠN"**

* **Ý nghĩa:** Cho biết tốc độ *tối đa* của thuật toán, không quan tâm trường hợp tốt nhất.
* **Cách diễn đạt:** `f(n) = O(g(n))` nghĩa là `f(n)` tăng chậm hơn hoặc bằng `g(n)`.
* **Ứng dụng:**
    * Mô tả trường hợp tồi tệ nhất của thuật toán.
    * Đánh giá hiệu suất tối đa của thuật toán.
* **Ví dụ:**
    * `O(1)`: Thời gian không đổi (truy cập phần tử trong mảng).
    * `O(log n)`: Thời gian tăng theo logarit (tìm kiếm nhị phân).
    * `O(n)`: Thời gian tăng tuyến tính (tìm kiếm tuyến tính).
    * `O(n log n)`: Thời gian tăng theo n log n (merge sort).
    * `O(n^2)`: Thời gian tăng theo bình phương (bubble sort).
    * `O(2^n)`: Thời gian tăng theo hàm mũ (vét cạn).

### **V. BIG-THETA (Θ) - "VỪA ĐỦ, KHÔNG THỪA, KHÔNG THIẾU"**

* **Ý nghĩa:** Cho biết tốc độ *chính xác* của thuật toán, cả trường hợp tốt nhất và tồi tệ nhất.
* **Cách diễn đạt:** `f(n) = Θ(g(n))` nghĩa là `f(n)` tăng tương tự như `g(n)`.
* **Ứng dụng:**
    * Mô tả chính xác tốc độ tăng trưởng của thuật toán.
    * Đánh giá hiệu suất thuật toán một cách chính xác.
* **Ví dụ:**
    * `Θ(n)`: Duyệt mảng 1 lần.
    * `Θ(log n)`: Tìm kiếm nhị phân.
    * `Θ(n log n)`: Merge sort.
    * `Θ(n^2)`: Insertion sort.

### **VI. BIG-OMEGA (Ω) - "TỐT NHẤT MÀ THÔI"**

* **Ý nghĩa:** Cho biết tốc độ *tối thiểu* của thuật toán, không quan tâm trường hợp tồi tệ nhất.
* **Cách diễn đạt:** `f(n) = Ω(g(n))` nghĩa là `f(n)` tăng nhanh hơn hoặc bằng `g(n)`.
* **Ứng dụng:**
    * Mô tả trường hợp tốt nhất của thuật toán.
    * Đánh giá hiệu suất tối thiểu của thuật toán.
* **Ví dụ:**
    * `Ω(1)`: Truy cập phần tử đầu tiên của mảng.
    * `Ω(log n)`: Tìm kiếm nhị phân trong trường hợp tốt nhất.
    * `Ω(n)`: Duyệt mảng trong trường hợp tốt nhất.
    * `Ω(n^2)`: Một số thuật toán sắp xếp khi dữ liệu gần như đã sắp xếp.

### **VII. SO SÁNH BIG-O, BIG-THETA, BIG-OMEGA (NHƯNG "CÁC MẶT" CỦA MỘT VẤN ĐỀ)**

* **Big-O:** Giới hạn trên (tệ nhất).
* **Big-Theta:** Giới hạn chính xác (trung bình).
* **Big-Omega:** Giới hạn dưới (tốt nhất).
* **Quan hệ:** Nếu một thuật toán có độ phức tạp `Θ(g(n))`, thì nó cũng có `O(g(n))` và `Ω(g(n))`.

### **VIII. CÁC LỚP ĐỘ PHỨC TẠP THƯỜNG GẶP (NHỮNG "MỨC ĐỘ" CHẠY CỦA THUẬT TOÁN)**

| Lớp phức tạp | Tên gọi     | Ý nghĩa                                                   |
|--------------|-------------|-----------------------------------------------------------|
| O(1)         | Constant    | Chạy nhanh như chớp, không phụ thuộc dữ liệu              |
| O(log n)     | Logarithmic | Chạy nhanh, phù hợp với dữ liệu lớn                       |
| O(n)         | Linear      | Chạy tỷ lệ với dữ liệu, không quá chậm                    |
| O(n log n)   | Loglinear   | Chạy tương đối nhanh, thường gặp ở thuật toán chia để trị |
| O(n^2)       | Quadratic   | Chạy chậm, không nên dùng cho dữ liệu lớn                 |
| O(2^n)       | Exponential | Chạy rất chậm, chỉ dùng khi dữ liệu rất nhỏ               |

### **IX. VÍ DỤ THỰC TẾ (NHÌN VÀO LÀ HIỂU LIỀN)**

* **Tìm kiếm tuyến tính (Linear Search):**
    * **Big-O:** O(n)
    * **Big-Theta:** Θ(n)
    * **Big-Omega:** Ω(1)
* **Sắp xếp nổi bọt (Bubble Sort):**
    * **Big-O:** O(n^2)
    * **Big-Theta:** Θ(n^2)
    * **Big-Omega:** Ω(n) (có thể tốt hơn trong trường hợp đã sắp xếp)
* **Tìm kiếm nhị phân (Binary Search):**
    * **Big-O:** O(log n)
    * **Big-Theta:** Θ(log n)
    * **Big-Omega:** Ω(1)
* **Merge Sort:**
    * **Big-O:** O(n log n)
    * **Big-Theta:** Θ(n log n)
    * **Big-Omega:** Ω(n log n)
* **Quick Sort:**
    * **Big-O:** O(n^2) (trường hợp xấu nhất)
    * **Big-Theta:** Θ(n log n) (trường hợp trung bình)
    * **Big-Omega:** Ω(n log n) (trường hợp tốt nhất)

### **X. LƯU Ý QUAN TRỌNG (NHỚ ĐỂ KHÔNG BỊ "LÚ")**

* **Bỏ qua hằng số:** O(2n) cũng là O(n).
* **Tốc độ tăng trưởng:** Độ phức tạp mô tả tốc độ tăng, không phải thời gian thực tế.
* **Nhiều yếu tố khác:** Không chỉ có độ phức tạp thời gian, còn có độ phức tạp không gian, cache, ...

### **XI. ỨNG DỤNG (BIẾT ĐỂ MÀ DÙNG)**

* **Chọn thuật toán:** Dùng độ phức tạp để chọn thuật toán phù hợp.
* **Tối ưu code:** Tìm các đoạn code chạy chậm và cải thiện.
* **Nền tảng kiến thức:** Giúp hiểu rõ hơn về thuật toán.

### **KẾT LUẬN**

Độ phức tạp thuật toán là một công cụ mạnh mẽ, giúp chúng ta hiểu rõ và đánh giá hiệu quả của thuật toán. Hy vọng qua
bài viết này, các bạn đã nắm vững kiến thức về Big-O, Big-Theta, Big-Omega và có thể tự tin phân tích độ phức tạp của
các thuật toán. Chúc các bạn code thành công! 😎
