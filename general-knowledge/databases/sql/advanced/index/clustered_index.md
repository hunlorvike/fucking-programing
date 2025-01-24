## **🚀 "GIẢI MÃ" CLUSTERED INDEX: "SẮP XẾP" DỮ LIỆU TRONG DATABASE CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong SQL Server:
Clustered Index (Chỉ mục nhóm cụm). Nghe có vẻ "lạ tai" nhưng thực ra nó ảnh hưởng rất lớn đến hiệu suất của database
đấy. Cùng mình "mổ xẻ" nó nhé!

### **I. CLUSTERED INDEX LÀ GÌ? (SẮP XẾP DỮ LIỆU KIỂU GÌ?)**

- **Clustered Index (Chỉ mục nhóm cụm):** Là một loại chỉ mục đặc biệt, _quyết định thứ tự vật lý_ của dữ liệu trong
  bảng.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn sắp xếp sách trong thư viện: bạn sắp xếp sách theo mã số, và khi cần, bạn tìm đúng mã số là đến
      đúng sách.
- **Quan trọng vì:**
    - **Sắp xếp dữ liệu:** Dữ liệu trong bảng được sắp xếp theo thứ tự của clustered index.
    - **Hiệu suất:** Giúp truy vấn nhanh hơn khi tìm kiếm theo cột được index.
    - **Chỉ có một:** Mỗi bảng chỉ có _một_ clustered index.

### **II. CÁCH HOẠT ĐỘNG CỦA CLUSTERED INDEX (TẠI SAO LẠI NHANH?)**

1. **Dữ liệu được sắp xếp:** Dữ liệu trong bảng được sắp xếp _vật lý_ theo thứ tự của clustered index.
2. **Truy cập nhanh:** Khi tìm kiếm theo cột clustered index, SQL Server có thể truy cập dữ liệu một cách rất nhanh (vì
   dữ liệu đã được sắp xếp).
3. **Lá của cây index chứa dữ liệu:** Với Clustered Index thì lá của cây index cũng là chính dữ liệu của bảng.

### **III. CÁCH TẠO CLUSTERED INDEX (CÁCH "SẮP XẾP")**

#### **3.1. TẠO CLUSTERED INDEX KHI TẠO BẢNG:**

```sql
CREATE TABLE table_name (
    column1 datatype PRIMARY KEY CLUSTERED,
    column2 datatype,
    ...
);
```

- **`PRIMARY KEY CLUSTERED`:** Tạo clustered index trên cột `column1`, đồng thời đặt nó làm khóa chính (Primary Key).
- **Nếu không chỉ định:** SQL server thường tạo một index clustered ngầm định trên cột primary key.

#### **3.2. TẠO CLUSTERED INDEX SAU KHI TẠO BẢNG:**

```sql
CREATE CLUSTERED INDEX index_name
ON table_name (column1 [ASC|DESC], column2 [ASC|DESC], ...);
```

- **`CREATE CLUSTERED INDEX index_name`:** Tạo clustered index với tên `index_name`.
- **`ON table_name (column1 [ASC|DESC], ...)`:** Tạo index trên các cột `column1`, `column2`,... (có thể chỉ định thứ tự
  sắp xếp).
- **Ví dụ:**

```sql
CREATE CLUSTERED INDEX idx_employeeid ON Employees (EmployeeID);
```

### **IV. KHI NÀO NÊN DÙNG CLUSTERED INDEX (KHI NÀO "NÊN" SẮP XẾP)?**

1. **Cột khóa chính (Primary Key):** Thường nên tạo clustered index trên cột khóa chính (vì nó duy nhất).
2. **Cột thường dùng để tìm kiếm:** Nếu bạn hay tìm kiếm theo một cột, thì nên dùng clustered index trên cột đó.
3. **Cột có thứ tự:** Dùng clustered index cho các cột có thứ tự (ngày tháng, ID, ...).
4. **Cột có tính duy nhất**: Dùng clustered index cho các cột đảm bảo tính duy nhất (ví dụ: số CMND, mã số sinh viên).
5. **Chỉ có 1 clustered index:** Nhớ rằng mỗi bảng chỉ có _một_ clustered index thôi.

### **V. ƯU ĐIỂM CỦA CLUSTERED INDEX (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Truy vấn nhanh:** Khi tìm kiếm theo cột index (vì dữ liệu đã được sắp xếp).
- **Tối ưu hóa:** Tối ưu hóa các thao tác tìm kiếm theo khoảng.
- **Đảm bảo thứ tự:** Dữ liệu trong bảng được sắp xếp theo thứ tự.

### **VI. NHƯỢC ĐIỂM CỦA CLUSTERED INDEX (ĐIỂM "KHÓ CHỊU")**

- **Chậm khi thêm/xóa:** Cần sắp xếp lại dữ liệu khi thêm/xóa.
- **Chỉ có một:** Mỗi bảng chỉ có một clustered index (phải chọn cẩn thận).
- **Tốn bộ nhớ:** Chiếm bộ nhớ để lưu index.

### **VII. SO SÁNH VỚI NONCLUSTERED INDEX (ĐỂ HIỂU RÕ HƠN)**

| Tính chất           | Clustered Index                                  | Nonclustered Index                                                                          |
|---------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Sắp xếp dữ liệu** | Sắp xếp vật lý (dữ liệu trong bảng)              | Không sắp xếp dữ liệu (index tách biệt)                                                     |
| **Số lượng**        | Mỗi bảng có 1                                    | Mỗi bảng có thể có nhiều                                                                    |
| **Lá của index**    | Lá chứa chính dữ liệu của bảng                   | Lá chứa địa chỉ của bản ghi                                                                 |
| **Hiệu suất**       | Tốt khi tìm theo cột index, truy vấn theo khoảng | Tốt khi tìm theo cột index, nhưng có thể chậm hơn clustered index nếu phải lookup vào bảng. |

### **VIII. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Chọn đúng cột:** Chọn cột index cẩn thận, dùng cột nào thường xuyên tìm kiếm, sắp xếp.
- **Không quá nhiều:** Không tạo quá nhiều index, làm chậm các thao tác ghi (INSERT, UPDATE, DELETE).
- **Dùng `WHERE`:** Nếu thường xuyên lọc theo một số cột, thì clustered index sẽ phát huy hiệu quả.
- **Xem Execution Plan:** Dùng Execution Plan để xem SQL Server có dùng index hay không (bài về execution plan).

### **IX. KẾT LUẬN (TỔNG KẾT)**

Clustered Index là "trái tim" của bảng trong SQL Server, giúp dữ liệu được sắp xếp và truy vấn nhanh hơn. Hy vọng qua
bài viết này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
