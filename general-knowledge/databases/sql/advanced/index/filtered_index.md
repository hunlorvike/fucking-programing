## **🚀 "GIẢI MÃ" FILTERED INDEX: "CHỈ MỤC" THÔNG MINH CHO DỮ LIỆU CÓ ĐIỀU KIỆN TRONG SQL SERVER 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một loại index khá đặc biệt trong SQL Server: Filtered Index (Chỉ mục lọc). Đây là một "chiêu thức" lợi hại giúp bạn tăng tốc độ truy vấn trên các tập dữ liệu mà bạn thường xuyên lọc theo một điều kiện nào đó. Cùng mình "mổ xẻ" nó nhé!

### **I. FILTERED INDEX LÀ GÌ? (INDEX CÓ "ĐIỀU KIỆN")**

-   **Filtered Index (Chỉ mục lọc):** Là một loại index _nonclustered_ đặc biệt, được tạo ra trên một tập hợp các dòng dữ liệu thỏa mãn một _điều kiện nhất định_.
-   **Nó hoạt động như thế nào?**
    -   Giống như bạn tạo một "mục lục" riêng cho những trang sách có nội dung đặc biệt, giúp bạn tìm nhanh hơn khi chỉ cần tìm những trang đó (thay vì tìm trong cả cuốn sách).
-   **Quan trọng vì:**
    -   **Tối ưu hiệu suất:** Giúp truy vấn nhanh hơn khi có điều kiện lọc.
    -   **Giảm kích thước index:** Index nhỏ hơn, truy vấn nhanh hơn.
    -   **Linh hoạt:** Tạo index phù hợp với từng trường hợp cụ thể.

### **II. CÁCH HOẠT ĐỘNG CỦA FILTERED INDEX (TÌM DỮ LIỆU "THÔNG MINH" HƠN)**

1.  **Điều kiện lọc:** Filtered index được tạo dựa trên một điều kiện `WHERE`.
2.  **Index nhỏ hơn:** Chỉ mục chỉ lưu trữ các dòng thỏa mãn điều kiện lọc.
3.  **Truy cập nhanh:** Khi truy vấn dùng đúng điều kiện lọc, SQL Server sẽ dùng index này để tìm dữ liệu nhanh hơn.
4.  **Tránh `Key Lookup`:** Nếu index có đủ cột, không cần phải `Key Lookup` (đọc thêm dữ liệu từ bảng gốc).

### **III. CÁCH TẠO FILTERED INDEX (CÁCH "VẼ" MỤC LỤC CÓ ĐIỀU KIỆN)**

```sql
CREATE NONCLUSTERED INDEX index_name
ON table_name (column1 [ASC|DESC], column2 [ASC|DESC], ...)
WHERE filter_condition;
```

-   **`CREATE NONCLUSTERED INDEX index_name`:** Tạo nonclustered index với tên `index_name`.
-   **`ON table_name (column1 [ASC|DESC], ...)`:** Tạo index trên các cột `column1`, `column2`,... (có thể chỉ định thứ tự sắp xếp).
-   **`WHERE filter_condition`:** Điều kiện lọc dữ liệu.
-   **Ví dụ:**

```sql
CREATE NONCLUSTERED INDEX idx_active_employees
ON Employees (LastName, FirstName)
WHERE IsActive = 1;
```

### **IV. KHI NÀO NÊN DÙNG FILTERED INDEX (KHI NÀO "CẦN" LỌC?)**

1.  **Khi có điều kiện `WHERE` cố định:** Khi truy vấn thường xuyên có một điều kiện `WHERE` cụ thể (ví dụ: `IsActive = 1`).
2.  **Khi dữ liệu phân bố không đều:** Khi một số giá trị có nhiều dòng hơn các giá trị khác.
3.  **Khi muốn giảm kích thước index:** Khi bạn không muốn index tất cả các dòng trong bảng, mà chỉ một số dòng thỏa mãn điều kiện.
4.  **Khi index kết hợp với các cột include**: Thêm cột không tìm kiếm vào index để tránh key lookup (Bài trước về nonclustered index).
5.  **Chú ý:** Dữ liệu thay đổi nhiều sẽ làm index trở nên không hiệu quả, nên cân nhắc kỹ.

### **V. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có bảng `Employees`:

-   **(EmployeeID, FirstName, LastName, IsActive, Department, Salary)**

1.  **Tạo filtered index cho nhân viên đang hoạt động:**

```sql
CREATE NONCLUSTERED INDEX idx_active_employees
ON Employees (LastName, FirstName)
WHERE IsActive = 1;
```

-   **Giải thích:** Tạo index trên cột `LastName`, `FirstName`, chỉ cho các nhân viên có `IsActive = 1`.

2.  **Truy vấn:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE IsActive = 1 AND Department = 'HR'
```

-   **Kết quả:** Truy vấn này sẽ dùng index `idx_active_employees` vì có `WHERE IsActive = 1`, sau đó có thể lọc tiếp theo `Department`

### **VI. ƯU ĐIỂM CỦA FILTERED INDEX (NHỮNG ĐIỂM "ĐÁNG YÊU")**

-   **Hiệu suất cao:** Truy vấn nhanh hơn khi có điều kiện lọc phù hợp.
-   **Index nhỏ:** Kích thước index nhỏ hơn, truy vấn nhanh hơn, giảm bộ nhớ.
-   **Tối ưu hóa:** Tối ưu cho các tình huống cụ thể.
-   **Tránh `Key Lookup`:** Nếu index có đủ cột, không cần `Key Lookup`.

### **VII. NHƯỢC ĐIỂM CỦA FILTERED INDEX (ĐIỂM "KHÓ CHỊU")**

-   **Ít dùng hơn:** Chỉ phù hợp với một số bài toán cụ thể.
-   **Cần điều kiện:** Không dùng được nếu không có điều kiện `WHERE` phù hợp.
-   **Bảo trì:** Có thể khó quản lý nếu có quá nhiều filtered index.

### **VIII. SO SÁNH VỚI NONCLUSTERED INDEX (ĐỂ HIỂU RÕ HƠN)**

| Tính chất          | Nonclustered Index (thường)             | Filtered Index                            |
| ------------------ | --------------------------------------- | ----------------------------------------- |
| **Lưu trữ**        | Lưu trữ cho _tất cả các dòng_           | Lưu trữ cho các dòng _thỏa mãn điều kiện_ |
| **Kích thước**     | Lớn hơn                                 | Nhỏ hơn                                   |
| **Truy vấn**       | Hiệu quả khi dùng cột index             | Hiệu quả khi dùng cột index và điều kiện  |
| **Tính linh hoạt** | Linh hoạt hơn, dùng được nhiều truy vấn | Ít linh hoạt hơn (cần điều kiện)          |
| **Phức tạp**       | Dễ tạo, dễ quản lý                      | Phức tạp hơn, cần chọn điều kiện hợp lý   |

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

-   **Chọn điều kiện phù hợp:** Chọn điều kiện lọc thường dùng trong `WHERE` để có hiệu quả tốt nhất.
-   **Không lạm dụng:** Không tạo quá nhiều filtered index (chỉ dùng khi cần).
-   **Include column:** Thêm các cột không dùng để tìm kiếm vào index (để tránh `Key Lookup`).
-   **Test kỹ:** Thử nghiệm để xem filtered index có thật sự hiệu quả không.
-   **Dùng Execution Plan:** Xem Execution Plan để biết SQL Server có dùng index hay không (như bài trước).

### **X. KẾT LUẬN (TỔNG KẾT)**

Filtered Index là một công cụ rất mạnh mẽ để tối ưu hóa truy vấn trong SQL Server, đặc biệt khi bạn làm việc với các dữ liệu có điều kiện lọc cụ thể. Hãy sử dụng chúng một cách thông minh để có được hiệu suất tốt nhất cho ứng dụng của bạn. Chúc các bạn code thành công! 😎
