## **🚀 "GIẢI MÃ" CẤU TRÚC DỮ LIỆU: TUYẾN TÍNH VS PHI TUYẾN TÍNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai loại cấu trúc dữ liệu chính: Tuyến tính (Linear)
và Phi tuyến tính (Non-linear). Đây là hai "phe" đối đầu nhau, nhưng mỗi "phe" lại có những ưu điểm riêng. Cùng mình "mổ
xẻ" nó nhé!

### **I. CẤU TRÚC DỮ LIỆU: TUYẾN TÍNH VS PHI TUYẾN TÍNH LÀ GÌ?**

- **Cấu trúc dữ liệu tuyến tính:** Các phần tử được sắp xếp theo một thứ tự _tuyến tính_ (như kiểu hàng ngang).
- **Cấu trúc dữ liệu phi tuyến tính:** Các phần tử không có thứ tự cố định, mà liên kết với nhau theo các mối quan hệ
  phức tạp hơn.
- **Tóm lại:**
    - **Tuyến tính:** Xếp hàng một, dễ duyệt.
    - **Phi tuyến tính:** Xếp không theo hàng lối, có nhiều mối liên kết.

### **II. CẤU TRÚC DỮ LIỆU TUYẾN TÍNH (NHƯ "HÀNG NGANG")**

1. **Mảng (Array):**
    - Các phần tử cùng kiểu, lưu liên tiếp trong bộ nhớ.
    - **Ưu:** Truy cập nhanh bằng index.
    - **Nhược:** Kích thước cố định, thêm/xóa khó.
    - **Ví dụ:** `[1, 2, 3, 4, 5]` (như một dãy số).
2. **Danh sách liên kết (Linked List):**
    - Các phần tử (node) liên kết với nhau bằng con trỏ.
    - **Ưu:** Linh hoạt, thêm/xóa dễ.
    - **Nhược:** Truy cập chậm hơn, cần thêm bộ nhớ cho con trỏ.
    - **Ví dụ:** Như một đoàn tàu, các toa liên kết với nhau.
3. **Ngăn xếp (Stack):**
    - LIFO (Last-In, First-Out): vào sau ra trước (như chồng đĩa).
    - **Ưu:** Dùng trong đệ quy, quản lý bộ nhớ.
    - **Nhược:** Chỉ thao tác ở đỉnh.
4. **Hàng đợi (Queue):**
    - FIFO (First-In, First-Out): vào trước ra trước (như hàng đợi mua vé).
    - **Ưu:** Dùng trong hệ thống xử lý, quản lý tác vụ.
    - **Nhược:** Chỉ thao tác ở đầu và cuối.

### **III. CẤU TRÚC DỮ LIỆU PHI TUYẾN TÍNH (KHÔNG "HÀNG NGANG")**

1. **Cây (Tree):**
    - Các phần tử liên kết theo kiểu phân cấp (như sơ đồ tổ chức).
    - **Ưu:** Tìm kiếm, sắp xếp nhanh.
    - **Nhược:** Cài đặt phức tạp hơn.
    - **Ví dụ:** Cây thư mục, cây nhị phân, ...
2. **Đồ thị (Graph):**
    - Các phần tử liên kết phức tạp (như mạng lưới).
    - **Ưu:** Biểu diễn mối quan hệ phức tạp.
    - **Nhược:** Khó cài đặt hơn.
    - **Ví dụ:** Bản đồ đường đi, mạng xã hội, ...
3. **Bảng băm (Hash Table):**
    - Ánh xạ "khóa" (key) vào "vị trí" (hash value).
    - **Ưu:** Tìm kiếm nhanh.
    - **Nhược:** Có thể xung đột, không duyệt tuần tự.
4. **Tập hợp (Set):**
    - Lưu trữ các phần tử duy nhất, không có thứ tự.

### **IV. SO SÁNH CHI TIẾT (NHÌN VÀO LÀ HIỂU)**

| Đặc điểm         | Tuyến tính                                                  | Phi tuyến tính                                                              |
|------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Cấu trúc**     | Dữ liệu sắp xếp tuần tự, theo một trình tự nhất định.       | Dữ liệu không sắp xếp tuần tự, quan hệ phức tạp hơn.                        |
| **Mối quan hệ**  | Liên kết 1-1 (mỗi phần tử liên kết với trước/sau).          | Liên kết 1-n hoặc n-n (mỗi phần tử có thể liên kết với nhiều phần tử khác). |
| **Truy cập**     | Dễ dàng truy cập phần tử bằng index hoặc thứ tự.            | Truy cập phức tạp hơn, cần dùng thuật toán.                                 |
| **Ví dụ**        | Mảng, danh sách liên kết, ngăn xếp, hàng đợi.               | Cây, đồ thị, bảng băm, ...                                                  |
| **Tính tuần tự** | Các phần tử được duyệt tuần tự, dễ dàng.                    | Các phần tử không có thứ tự rõ ràng.                                        |
| **Kích thước**   | Có thể cố định (mảng), hoặc linh hoạt (danh sách liên kết). | Kích thước thường linh hoạt, dễ thêm/xóa phần tử.                           |
| **Ứng dụng**     | Bài toán đơn giản, dữ liệu có mối quan hệ tuyến tính.       | Bài toán phức tạp, dữ liệu có cấu trúc phân cấp hoặc không cố định.         |
| **Độ phức tạp**  | Thường O(1) hoặc O(n) cho các thao tác.                     | Thường O(log n) đến O(n²) hoặc hơn cho các thao tác trên cây/đồ thị.        |

### **V. VÍ DỤ MINH HỌA (CHO DỄ HÌNH DUNG)**

1. **Tuyến tính:**
    - **Mảng:** Dãy số nhà trên đường (1, 2, 3, ...).
    - **Danh sách liên kết:** Đoàn tàu (các toa nối nhau).
    - **Ngăn xếp:** Chồng đĩa (đĩa mới đặt lên trên).
    - **Hàng đợi:** Hàng người xếp hàng mua vé (ai đến trước thì được mua trước).
2. **Phi tuyến tính:**
    - **Cây:** Cây gia đình, sơ đồ tổ chức.
    - **Đồ thị:** Bản đồ đường đi, mạng xã hội.
    - **Bảng băm:** Từ điển (tra từ theo "khóa").

### **VI. KẾT LUẬN (TỔNG KẾT)**

Cấu trúc dữ liệu tuyến tính và phi tuyến tính đều có những ưu điểm và nhược điểm riêng. Việc lựa chọn cấu trúc dữ liệu
nào tùy thuộc vào từng bài toán và yêu cầu cụ thể. Hy vọng qua bài viết này, các bạn đã có cái nhìn tổng quan và hiểu rõ
hơn về chúng. Chúc các bạn code thành công! 😎
