## **🚀 "GIẢI MÃ" NONCLUSTERED INDEX: "ĐI TẮT" TRONG DATABASE CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong SQL Server:
Nonclustered Index (Chỉ mục không nhóm cụm). Đây là một "chiêu thức" lợi hại giúp bạn tăng tốc độ tìm kiếm dữ liệu trong
database, như kiểu bạn có "mục lục" giúp bạn tìm đến trang sách cần thiết nhanh hơn vậy. Cùng mình "mổ xẻ" nó nhé!

### **I. NONCLUSTERED INDEX LÀ GÌ? (NHƯ "MỤC LỤC" CỦA DATABASE)**

- **Nonclustered Index (Chỉ mục không nhóm cụm):** Là một loại chỉ mục _tách biệt_ với dữ liệu thật trong bảng, được tạo
  trên một hoặc nhiều cột để tìm kiếm nhanh hơn.
- **Nó hoạt động như thế nào?**
    - Giống như "mục lục" ở cuối sách: bạn tra mục lục để biết trang nào chứa thông tin cần, rồi đến trang đó để xem (
      thay vì đọc hết cả cuốn sách).
- **Quan trọng vì:**
    - **Tăng tốc độ:** Giúp tìm kiếm dữ liệu nhanh hơn.
    - **Linh hoạt:** Có thể tạo nhiều index khác nhau cho nhiều cột.
    - **Không ảnh hưởng đến dữ liệu:** Không thay đổi thứ tự lưu trữ vật lý của dữ liệu.

### **II. CÁCH HOẠT ĐỘNG CỦA NONCLUSTERED INDEX (TÌM DỮ LIỆU NHƯ THẾ NÀO?)**

1. **Index riêng biệt:** Nonclustered index là một cấu trúc _tách biệt_ với bảng dữ liệu.
2. **Bản đồ địa chỉ:** Index chứa các giá trị cột được index và _con trỏ_ (pointer) trỏ đến vị trí dữ liệu thực trong
   bảng.
3. **`Index Seek`:** Nếu query dùng cột index, SQL Server sẽ tìm index trước, rồi đến vị trí dữ liệu.
4. **`Key Lookup`:** Nếu index không chứa đủ cột cần lấy, SQL Server cần phải lookup (tìm thêm) vào bảng dữ liệu (có thể
   làm chậm).

### **III. CÁCH TẠO NONCLUSTERED INDEX (CÁCH "VẼ MỤC LỤC")**

```sql
CREATE [NONCLUSTERED] INDEX index_name
ON table_name (column1 [ASC|DESC], column2 [ASC|DESC], ...);
```

- **`CREATE [NONCLUSTERED] INDEX index_name`:** Tạo nonclustered index với tên `index_name`.
- **`ON table_name (column1 [ASC|DESC], ...)`:** Tạo index trên các cột `column1`, `column2`, ... (có thể chỉ định thứ
  tự sắp xếp).
- **Ví dụ:**

```sql
CREATE NONCLUSTERED INDEX idx_lastname ON Employees (LastName);
```

### **IV. KHI NÀO NÊN DÙNG NONCLUSTERED INDEX (KHI NÀO "CẦN MỤC LỤC")**

1. **Cột thường dùng trong `WHERE`:** Khi cần lọc dữ liệu theo một cột nào đó, cần dùng index trên cột đó.
2. **Cột thường dùng trong `JOIN`:** Dùng cho các cột liên kết trong JOIN.
3. **Cột thường dùng trong `ORDER BY`:** Dùng để sắp xếp dữ liệu.
4. **Composite index:** Khi cần tìm kiếm trên nhiều cột cùng lúc, thì dùng composite index (index trên nhiều cột).
5. **`Unique` constraint:** Khi cần giá trị duy nhất (ví dụ email, sdt), ta có thể dùng unique index (chú ý unique index
   có thể clustered hoặc nonclustered).

### **V. ƯU ĐIỂM CỦA NONCLUSTERED INDEX (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Tăng tốc truy vấn:** Giúp tìm dữ liệu nhanh hơn khi dùng đúng cột index.
- **Linh hoạt:** Tạo nhiều index cho các cột khác nhau.
- **Không thay đổi thứ tự dữ liệu:** Không làm thay đổi thứ tự vật lý của dữ liệu trong bảng.

### **VI. NHƯỢC ĐIỂM CỦA NONCLUSTERED INDEX (ĐIỂM "KHÓ CHỊU")**

- **Tốn bộ nhớ:** Chiếm bộ nhớ để lưu trữ.
- **`Key Lookup`:** Có thể phải lookup vào bảng gốc nếu không có đủ cột (chậm hơn).
- **Chậm khi ghi:** Làm chậm các thao tác ghi (INSERT, UPDATE, DELETE).

### **VII. SO SÁNH VỚI CLUSTERED INDEX (ĐỂ HIỂU RÕ HƠN)**

| Tính chất           | Clustered Index                                                       | Nonclustered Index                                              |
|---------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------|
| **Sắp xếp dữ liệu** | Sắp xếp vật lý dữ liệu trên ổ đĩa                                     | Không sắp xếp vật lý dữ liệu trên ổ đĩa                         |
| **Số lượng**        | Mỗi bảng chỉ có _một_                                                 | Mỗi bảng có thể có _nhiều_                                      |
| **Truy cập**        | Tìm kiếm nhanh nếu dùng đúng cột index, các thao tác tìm theo khoảng. | Tìm kiếm nhanh khi dùng đúng cột index, có thể bị _Key Lookup_. |
| **Lưu trữ**         | Lá index chứa chính dữ liệu                                           | Lá index chỉ chứa con trỏ đến dữ liệu                           |

### **VIII. MỘT SỐ KỸ THUẬT TỐI ƯU NONCLUSTERED INDEX (CHO HIỆU QUẢ CAO HƠN)**

- **Include column:** Thêm các cột không dùng để tìm kiếm vào index, để tránh `Key Lookup`.
    - **Ví dụ:** `CREATE INDEX idx_name ON Employees (LastName) INCLUDE (FirstName, Salary);`
- **Filtered Index:** Tạo index dựa trên điều kiện (`WHERE`), giúp index nhỏ và tối ưu hơn cho các query đặc biệt.
    - **Ví dụ:** `CREATE INDEX idx_active_employee ON Employees (LastName) WHERE IsActive = 1;`.

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Chọn đúng cột:** Chọn cột index cẩn thận, dùng những cột thường xuyên dùng để tìm kiếm, sắp xếp.
- **Không lạm dụng:** Không tạo quá nhiều index, làm chậm các thao tác ghi (INSERT, UPDATE, DELETE).
- **Composite Index:** Dùng khi tìm kiếm trên nhiều cột.
- **Include column:** Dùng khi cần thêm các cột không tìm kiếm vào index.
- **Filtered Index:** Dùng cho các điều kiện lọc đặc biệt.
- **Xem Execution Plan:** Dùng Execution Plan để xem SQL Server có dùng index hay không (bài về execution plan).

### **X. KẾT LUẬN (TỔNG KẾT)**

Nonclustered Index là một công cụ rất mạnh mẽ giúp bạn tăng tốc độ truy vấn trong SQL Server. Hãy sử dụng chúng một cách
thông minh để có được hiệu suất tốt nhất cho ứng dụng của mình. Chúc các bạn code thành công! 😎
