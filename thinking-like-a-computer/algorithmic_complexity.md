# **Độ Phức Tạp Thuật Toán: Big-O, Big-Theta, Big-Omega**

**Mục lục**

1. **Giới thiệu**
    * 1.1. Tại sao cần đánh giá độ phức tạp thuật toán?
    * 1.2. Mục tiêu của việc sử dụng ký hiệu Big-O, Big-Theta, Big-Omega
2. **Các Khái Niệm Cơ Bản**
    * 2.1. Độ phức tạp thời gian (Time Complexity)
    * 2.2. Độ phức tạp không gian (Space Complexity)
3. **Big-O (O): Giới Hạn Trên**
    * 3.1. Định nghĩa
    * 3.2. Cách diễn đạt
    * 3.3. Ý nghĩa và ứng dụng
    * 3.4. Ví dụ minh họa
4. **Big-Theta (Θ): Giới Hạn Chính Xác**
    * 4.1. Định nghĩa
    * 4.2. Cách diễn đạt
    * 4.3. Ý nghĩa và ứng dụng
    * 4.4. Ví dụ minh họa
5. **Big-Omega (Ω): Giới Hạn Dưới**
    * 5.1. Định nghĩa
    * 5.2. Cách diễn đạt
    * 5.3. Ý nghĩa và ứng dụng
    * 5.4. Ví dụ minh họa
6. **So Sánh Big-O, Big-Theta và Big-Omega**
    * 6.1. Mối quan hệ giữa ba ký hiệu
    * 6.2. Khi nào nên sử dụng Big-O, Big-Theta và Big-Omega?
7. **Các Lớp Độ Phức Tạp Thường Gặp**
    * 7.1. Bảng tóm tắt các lớp độ phức tạp
    * 7.2. Giải thích chi tiết từng lớp độ phức tạp
8. **Ví Dụ Tính Toán Độ Phức Tạp**
    * 8.1. Tìm kiếm tuyến tính (Linear Search)
    * 8.2. Sắp xếp nổi bọt (Bubble Sort)
    * 8.3. Tìm kiếm nhị phân (Binary Search)
    * 8.4. Các ví dụ khác (nếu có)
9. **Lưu Ý Quan Trọng**
    * 9.1. Bỏ qua hằng số và tập trung vào thuật ngữ chính
    * 9.2. Độ phức tạp là tốc độ tăng trưởng, không phải thời gian thực tế
    * 9.3. Các yếu tố khác ngoài độ phức tạp thời gian
10. **Ứng Dụng của Độ Phức Tạp Thuật Toán**
    * 10.1. Lựa chọn thuật toán
    * 10.2. Tối ưu hóa code
    * 10.3. Nền tảng kiến thức cơ bản
11. **Kết luận**

---

### **1. Giới thiệu**

#### 1.1. Tại sao cần đánh giá độ phức tạp thuật toán?

Đánh giá độ phức tạp thuật toán là một bước quan trọng trong quá trình thiết kế và phát triển phần mềm. Khi làm việc với
các thuật toán, chúng ta không chỉ quan tâm đến việc thuật toán đó có chạy đúng hay không, mà còn quan tâm đến hiệu suất
của nó. Cụ thể:

* **Hiệu suất:** Đánh giá giúp chúng ta biết được thuật toán đó sẽ chạy nhanh như thế nào, đặc biệt khi xử lý dữ liệu
  lớn.
* **So sánh:** Cho phép so sánh hiệu quả của các thuật toán khác nhau để chọn ra thuật toán tốt nhất cho bài toán cụ
  thể.
* **Dự đoán:** Giúp dự đoán tài nguyên (thời gian, bộ nhớ) mà thuật toán sẽ tiêu thụ khi kích thước đầu vào thay đổi.
* **Tối ưu hóa:** Là cơ sở để tìm ra các điểm yếu của thuật toán và tối ưu hóa nó.

#### 1.2. Mục tiêu của việc sử dụng ký hiệu Big-O, Big-Theta, Big-Omega

Các ký hiệu Big-O, Big-Theta, Big-Omega cung cấp một cách chuẩn hóa để mô tả và so sánh hiệu suất của các thuật toán.
Chúng giúp:

* **Đơn giản hóa:** Bỏ qua các chi tiết nhỏ và tập trung vào tốc độ tăng trưởng của thuật toán khi kích thước đầu vào
  tăng lên.
* **Chung:** Cung cấp một ngôn ngữ chung để các nhà khoa học máy tính, lập trình viên có thể dễ dàng trao đổi và hiểu về
  hiệu suất của thuật toán.
* **Trừu tượng:** Mô tả hiệu suất ở mức độ trừu tượng, không phụ thuộc vào ngôn ngữ lập trình, phần cứng hoặc môi trường
  thực thi cụ thể.

### **2. Các Khái Niệm Cơ Bản**

#### 2.1. Độ phức tạp thời gian (Time Complexity)

Độ phức tạp thời gian là một thước đo về thời gian mà một thuật toán cần để hoàn thành, tính theo kích thước đầu vào. Nó
thường được biểu diễn bằng các hàm toán học và sử dụng các ký hiệu Big-O, Big-Theta, Big-Omega.

#### 2.2. Độ phức tạp không gian (Space Complexity)

Độ phức tạp không gian là một thước đo về lượng bộ nhớ mà một thuật toán cần sử dụng, tính theo kích thước đầu vào.
Tương tự như độ phức tạp thời gian, nó cũng thường được biểu diễn bằng các hàm toán học và các ký hiệu tương ứng.

### **3. Big-O (O): Giới Hạn Trên**

#### 3.1. Định nghĩa

Big-O (O) là một ký hiệu toán học mô tả giới hạn trên của tốc độ tăng trưởng của một hàm. Nói cách khác, nó cho biết tốc
độ **tối đa** mà một thuật toán có thể chạy, không quan tâm đến trường hợp tốt nhất.

#### 3.2. Cách diễn đạt

f(n) = O(g(n)) có nghĩa là tồn tại các hằng số dương c và n0 sao cho với mọi n ≥ n0, ta có f(n) ≤ c.g(n). Điều này có
nghĩa là f(n) tăng trưởng chậm hơn hoặc bằng g(n) khi n tiến về vô cùng.

#### 3.3. Ý nghĩa và ứng dụng

* Big-O thường được sử dụng để mô tả trường hợp **tồi tệ nhất** của một thuật toán.
* Ví dụ, O(n^2) có nghĩa là thời gian thực thi của thuật toán không vượt quá một hằng số nhân với n^2, ngay cả trong
  trường hợp đầu vào xấu nhất.
* Big-O hữu ích trong việc đánh giá hiệu suất tối đa của một thuật toán, giúp chúng ta dự đoán được giới hạn thời gian
  thực thi.

#### 3.4. Ví dụ minh họa

* **O(1):** Thời gian không đổi, không phụ thuộc vào kích thước đầu vào. Ví dụ: truy cập một phần tử trong mảng (index).
* **O(log n):** Thời gian tăng theo logarit của kích thước đầu vào. Ví dụ: tìm kiếm nhị phân (binary search).
* **O(n):** Thời gian tăng tuyến tính với kích thước đầu vào. Ví dụ: tìm kiếm tuyến tính (linear search).
* **O(n log n):** Thời gian tăng theo n nhân với logarit của n. Ví dụ: các thuật toán sắp xếp hiệu quả như merge sort.
* **O(n^2):** Thời gian tăng theo bình phương kích thước đầu vào. Ví dụ: sắp xếp nổi bọt (bubble sort).
* **O(2^n):** Thời gian tăng theo hàm mũ của kích thước đầu vào. Ví dụ: một số thuật toán vét cạn.

### **4. Big-Theta (Θ): Giới Hạn Chính Xác**

#### 4.1. Định nghĩa

Big-Theta (Θ) là một ký hiệu toán học mô tả giới hạn chính xác của tốc độ tăng trưởng của một hàm. Nó cho biết tốc độ *
*trung bình** của một thuật toán, cả trong trường hợp tốt nhất và tồi tệ nhất.

#### 4.2. Cách diễn đạt

f(n) = Θ(g(n)) có nghĩa là tồn tại các hằng số dương c1, c2 và n0 sao cho với mọi n > n0, ta có c1.g(n) ≤ f(n) ≤ c2.g(
n). Điều này nghĩa là f(n) tăng trưởng tương tự như g(n) khi n tiến về vô cùng.

#### 4.3. Ý nghĩa và ứng dụng

* Big-Theta cung cấp một mô tả chính xác hơn về tốc độ tăng trưởng của thuật toán so với Big-O.
* Ví dụ, Θ(n log n) cho biết thời gian thực thi của thuật toán sẽ tăng xấp xỉ theo n log n trong cả trường hợp tốt nhất,
  trung bình và tồi tệ nhất.
* Big-Theta thường được sử dụng khi chúng ta muốn đánh giá chính xác hiệu suất của thuật toán.

#### 4.4. Ví dụ minh họa

* **Θ(n):** Thời gian tăng tuyến tính với kích thước đầu vào. Ví dụ: thuật toán duyệt qua tất cả các phần tử một lần.
* **Θ(log n):** Thời gian tăng theo logarit của kích thước đầu vào. Ví dụ: thuật toán tìm kiếm nhị phân.
* **Θ(n log n):** Thời gian tăng theo n nhân với logarit của n. Ví dụ: merge sort.
* **Θ(n^2):** Thời gian tăng theo bình phương kích thước đầu vào. Ví dụ: sắp xếp chèn (insertion sort).

### **5. Big-Omega (Ω): Giới Hạn Dưới**

#### 5.1. Định nghĩa

Big-Omega (Ω) là một ký hiệu toán học mô tả giới hạn dưới của tốc độ tăng trưởng của một hàm. Nó cho biết tốc độ **tối
thiểu** mà một thuật toán có thể chạy, không quan tâm đến trường hợp xấu nhất.

#### 5.2. Cách diễn đạt

f(n) = Ω(g(n)) có nghĩa là tồn tại các hằng số dương c và n0 sao cho với mọi n > n0, ta có f(n) ≥ c.g(n). Điều này nghĩa
là f(n) tăng trưởng nhanh hơn hoặc bằng g(n) khi n tiến về vô cùng.

#### 5.3. Ý nghĩa và ứng dụng

* Big-Omega thường được sử dụng để mô tả trường hợp **tốt nhất** của một thuật toán.
* Ví dụ, Ω(n) có nghĩa là thời gian thực thi của thuật toán ít nhất là một hằng số nhân với n, ngay cả trong trường hợp
  đầu vào tốt nhất.
* Big-Omega hữu ích trong việc đánh giá hiệu suất tối thiểu của thuật toán, giúp chúng ta biết được giới hạn dưới của
  thời gian thực thi.

#### 5.4. Ví dụ minh họa

* **Ω(1):** Thời gian không đổi. Ví dụ: truy cập một phần tử đầu tiên trong mảng.
* **Ω(log n):** Thời gian tăng theo logarit của kích thước đầu vào. Ví dụ: tìm kiếm nhị phân trong trường hợp tốt nhất.
* **Ω(n):** Thời gian tăng tuyến tính với kích thước đầu vào. Ví dụ: duyệt qua tất cả các phần tử trong trường hợp tốt
  nhất.
* **Ω(n^2):** Thời gian tăng theo bình phương kích thước đầu vào. Ví dụ: một số thuật toán sắp xếp khi đầu vào gần như
  đã được sắp xếp.

### **6. So Sánh Big-O, Big-Theta và Big-Omega**

#### 6.1. Mối quan hệ giữa ba ký hiệu

* **Big-O:** Mô tả giới hạn trên, tức là trường hợp tồi tệ nhất.
* **Big-Theta:** Mô tả giới hạn chính xác, tức là trường hợp trung bình.
* **Big-Omega:** Mô tả giới hạn dưới, tức là trường hợp tốt nhất.

Nếu một thuật toán có độ phức tạp **Θ(g(n))**, thì nó cũng đồng thời có độ phức tạp **O(g(n))** và **Ω(g(n))**. Tuy
nhiên, điều ngược lại không phải lúc nào cũng đúng.

#### 6.2. Khi nào nên sử dụng Big-O, Big-Theta và Big-Omega?

* **Big-O:** Sử dụng khi muốn đánh giá hiệu suất tối đa của thuật toán, trường hợp xấu nhất có thể xảy ra. Đây là ký
  hiệu phổ biến nhất vì nó đảm bảo thời gian chạy của thuật toán không vượt quá một ngưỡng nào đó.
* **Big-Theta:** Sử dụng khi muốn đánh giá chính xác hiệu suất của thuật toán, cả trong trường hợp tốt nhất và tồi tệ
  nhất.
* **Big-Omega:** Sử dụng khi muốn đánh giá hiệu suất tối thiểu của thuật toán, trường hợp tốt nhất có thể xảy ra.

### **7. Các Lớp Độ Phức Tạp Thường Gặp**

#### 7.1. Bảng tóm tắt các lớp độ phức tạp

| Lớp độ phức tạp | Biểu diễn   | Ý nghĩa                                                         |
|-----------------|-------------|-----------------------------------------------------------------|
| O(1)            | Constant    | Thời gian chạy không phụ thuộc vào kích thước đầu vào           |
| O(log n)        | Logarithmic | Thời gian chạy tăng logarit theo kích thước đầu vào             |
| O(n)            | Linear      | Thời gian chạy tăng tuyến tính theo kích thước đầu vào          |
| O(n log n)      | Loglinear   | Thời gian chạy tăng logarit tuyến tính theo kích thước đầu vào  |
| O(n^2)          | Quadratic   | Thời gian chạy tăng bậc hai theo kích thước đầu vào             |
| O(n^k)          | Polynomial  | Thời gian chạy tăng bậc k theo kích thước đầu vào               |
| O(2^n)          | Exponential | Thời gian chạy tăng theo lũy thừa của 2 theo kích thước đầu vào |

#### 7.2. Giải thích chi tiết từng lớp độ phức tạp

* **O(1) - Constant:** Thuật toán chạy với thời gian không đổi, không phụ thuộc vào kích thước đầu vào. Ví dụ: truy cập
  một phần tử mảng bằng index, phép gán, phép tính số học đơn giản.
* **O(log n) - Logarithmic:** Thời gian chạy tăng chậm hơn so với kích thước đầu vào. Thuật toán thường chia nhỏ vấn đề
  thành các phần nhỏ hơn. Ví dụ: tìm kiếm nhị phân (binary search), tìm kiếm trong cây nhị phân cân bằng.
* **O(n) - Linear:** Thời gian chạy tăng tuyến tính với kích thước đầu vào. Thuật toán thường duyệt qua tất cả các phần
  tử của đầu vào một lần. Ví dụ: tìm kiếm tuyến tính (linear search), duyệt mảng, tính tổng các phần tử trong mảng.
* **O(n log n) - Loglinear:** Thời gian chạy tăng theo n nhân với logarit của n. Thuật toán thường chia để trị và sắp
  xếp. Ví dụ: merge sort, quick sort (trong trường hợp trung bình).
* **O(n^2) - Quadratic:** Thời gian chạy tăng theo bình phương của kích thước đầu vào. Thuật toán thường có các vòng lặp
  lồng nhau. Ví dụ: bubble sort, insertion sort, selection sort.
* **O(n^k) - Polynomial:** Thời gian chạy tăng theo lũy thừa của kích thước đầu vào (với k là một số nguyên dương). Ví
  dụ: nhân ma trận, một số thuật toán quy hoạch động.
* **O(2^n) - Exponential:** Thời gian chạy tăng theo hàm mũ của kích thước đầu vào. Thuật toán thường tìm kiếm vét cạn.
  Ví dụ: tìm tất cả các tập con của một tập hợp, thuật toán giải bài toán người bán hàng (TSP) bằng vét cạn.

### **8. Ví Dụ Tính Toán Độ Phức Tạp**

#### 8.1. Tìm kiếm tuyến tính (Linear Search)

* **Thuật toán:** Duyệt qua từng phần tử của mảng để tìm kiếm mục tiêu.
* **Độ phức tạp:**
    * Trường hợp tốt nhất (mục tiêu ở vị trí đầu): O(1)
    * Trường hợp trung bình và xấu nhất (mục tiêu ở cuối mảng hoặc không tồn tại): O(n)
    * **Big-O:** O(n)
    * **Big-Theta:** Θ(n)
    * **Big-Omega:** Ω(1)

#### 8.2. Sắp xếp nổi bọt (Bubble Sort)

* **Thuật toán:** So sánh các phần tử kề nhau và hoán đổi chúng cho đến khi mảng được sắp xếp.
* **Độ phức tạp:**
    * Luôn phải duyệt qua tất cả các phần tử n lần trong vòng lặp lồng nhau.
    * **Big-O:** O(n^2)
    * **Big-Theta:** Θ(n^2)
    * **Big-Omega:** Ω(n^2)

#### 8.3. Tìm kiếm nhị phân (Binary Search)

* **Thuật toán:** Chia mảng đã được sắp xếp thành hai nửa, loại bỏ nửa không chứa mục tiêu và lặp lại quy trình.
* **Độ phức tạp:**
    * Mỗi lần lặp, kích thước mảng giảm đi một nửa.
    * Số lần lặp tối đa là log2(n).
    * **Big-O:** O(log n)
    * **Big-Theta:** Θ(log n)
    * **Big-Omega:** Ω(1)

#### 8.4. Các ví dụ khác (nếu có)

(Bạn có thể bổ sung thêm các ví dụ khác ở đây, ví dụ như sắp xếp chèn, sắp xếp chọn, quick sort, merge sort, v.v.)

### **9. Lưu Ý Quan Trọng**

#### 9.1. Bỏ qua hằng số và tập trung vào thuật ngữ chính

Khi phân tích độ phức tạp, chúng ta thường bỏ qua các hằng số và chỉ quan tâm đến thuật ngữ chính, vì khi kích thước đầu
vào (n) lớn, hằng số không ảnh hưởng đáng kể đến tốc độ tăng trưởng của hàm. Ví dụ: O(2n) tương đương O(n).

#### 9.2. Độ phức tạp là tốc độ tăng trưởng, không phải thời gian thực tế

Độ phức tạp mô tả tốc độ tăng trưởng của thời gian chạy khi kích thước đầu vào tăng lên, không phải là thời gian thực tế
mà thuật toán chạy. Một thuật toán có độ phức tạp O(n) có thể chạy nhanh hơn một thuật toán O(n^2) với các kích thước
đầu vào nhỏ.

#### 9.3. Các yếu tố khác ngoài độ phức tạp thời gian

Độ phức tạp thời gian chỉ là một trong những yếu tố đánh giá hiệu suất của thuật toán. Các yếu tố khác cần xem xét bao
gồm:

* **Độ phức tạp không gian:** Lượng bộ nhớ thuật toán sử dụng.
* **Độ phức tạp truyền thông:** Lượng dữ liệu cần truyền tải khi thuật toán chạy trên các hệ thống phân tán.
* **Độ phức tạp cache:** Hiệu quả của thuật toán khi sử dụng cache.

### **10. Ứng Dụng của Độ Phức Tạp Thuật Toán**

#### 10.1. Lựa chọn thuật toán

Độ phức tạp là một trong những yếu tố quan trọng để lựa chọn thuật toán phù hợp với một bài toán cụ thể. Khi kích thước
đầu vào lớn, thuật toán có độ phức tạp thấp hơn sẽ có hiệu suất tốt hơn.

#### 10.2. Tối ưu hóa code

Hiểu rõ về độ phức tạp của các đoạn code giúp chúng ta tìm ra các đoạn code chạy chậm và tối ưu hóa chúng. Chúng ta có
thể lựa chọn các thuật toán khác hiệu quả hơn, hoặc thay đổi cấu trúc dữ liệu để giảm độ phức tạp của thuật toán.

#### 10.3. Nền tảng kiến thức cơ bản

Độ phức tạp thuật toán là một kiến thức cơ bản trong khoa học máy tính, giúp chúng ta hiểu rõ hơn về các thuật toán và
cách đánh giá hiệu suất của chúng. Nó là một phần quan trọng trong quá trình học tập và phát triển sự nghiệp trong lĩnh
vực công nghệ thông tin.

### **11. Kết luận**

Độ phức tạp thuật toán là một công cụ mạnh mẽ giúp chúng ta đánh giá hiệu suất của các thuật toán một cách hiệu quả.
Hiểu rõ về Big-O, Big-Theta, Big-Omega, các lớp độ phức tạp thường gặp và cách tính độ phức tạp là vô cùng quan trọng
đối với bất kỳ ai làm việc trong lĩnh vực công nghệ thông tin. Nó giúp chúng ta không chỉ viết được code đúng mà còn có
thể tối ưu hóa code và lựa chọn được thuật toán phù hợp nhất cho mỗi bài toán.
