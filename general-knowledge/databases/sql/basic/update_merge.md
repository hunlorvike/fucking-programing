## **🚀 "GIẢI MÃ" UPDATE MERGE TRONG SQL SERVER: "ĐỒNG BỘ" DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cực kỳ mạnh mẽ trong SQL Server:
`UPDATE MERGE`. Đây là câu lệnh giúp bạn đồng bộ dữ liệu giữa các bảng, rất hữu ích khi cần cập nhật, thêm mới hoặc xóa
dữ liệu dựa trên sự so sánh. Cùng mình "mổ xẻ" nó nhé!

### **I. UPDATE MERGE LÀ GÌ? (ĐỒNG BỘ DỮ LIỆU KIỂU GÌ?)**

* **`UPDATE MERGE`:** Là câu lệnh SQL giúp bạn *đồng bộ dữ liệu* giữa 2 bảng:
    * Cập nhật dữ liệu cũ.
    * Thêm dữ liệu mới.
    * Xóa dữ liệu không cần thiết.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn cập nhật danh bạ điện thoại:
        * Nếu số điện thoại đã có trong danh bạ, thì cập nhật thông tin.
        * Nếu số điện thoại chưa có, thì thêm vào danh bạ.
        * Nếu số điện thoại không còn tồn tại, thì xóa khỏi danh bạ.
* **Quan trọng vì:**
    * **Đồng bộ dữ liệu:** Giúp 2 bảng luôn giống nhau.
    * **Hiệu suất:** Thay thế cho nhiều lệnh `INSERT`, `UPDATE`, `DELETE`.
    * **Linh hoạt:** Có thể dùng nhiều điều kiện khác nhau.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG UPDATE MERGE)**

```sql
MERGE INTO target_table AS target
USING source_table AS source
ON target.column = source.column
WHEN MATCHED THEN
    -- UPDATE statement
WHEN NOT MATCHED THEN
    -- INSERT statement
WHEN MATCHED AND condition THEN
   -- DELETE statement
```

* **`MERGE INTO target_table AS target`:** Chọn bảng đích để cập nhật.
* **`USING source_table AS source`:** Chọn bảng nguồn chứa dữ liệu mới.
* **`ON target.column = source.column`:** Điều kiện để so sánh dữ liệu giữa hai bảng (điều kiện khớp).
* **`WHEN MATCHED THEN ...`:** Làm gì khi tìm thấy bản ghi khớp.
    * Có thể dùng `UPDATE` (cập nhật) hoặc `DELETE` (xóa).
* **`WHEN NOT MATCHED THEN ...`:** Làm gì khi không tìm thấy bản ghi khớp.
    * Thường dùng `INSERT` (thêm mới).

### **III. CÁC TÙY CHỌN MỞ RỘNG (CÁC "CHIÊU" NÂNG CAO)**

1. **`WHEN MATCHED`:** Xử lý khi có bản ghi khớp.
    * **Cập nhật:**
      ```sql
      WHEN MATCHED THEN
           UPDATE SET target.column1 = source.column1, target.column2 = source.column2
      ```
    * **Xóa:**
      ```sql
      WHEN MATCHED AND condition THEN
           DELETE
      ```
2. **`WHEN NOT MATCHED`:** Xử lý khi không có bản ghi khớp (thường là thêm mới).

```sql
WHEN NOT MATCHED THEN
    INSERT (column1, column2)
    VALUES (source.column1, source.column2);
```

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Cập nhật lương nhân viên (WHEN MATCHED):**

```sql
MERGE INTO Employees AS target
USING TempEmployees AS source
ON target.EmployeeID = source.EmployeeID
WHEN MATCHED THEN
    UPDATE SET target.Salary = source.Salary;
```

2. **Thêm mới nhân viên (WHEN NOT MATCHED):**

```sql
MERGE INTO Employees AS target
USING NewEmployees AS source
ON target.EmployeeID = source.EmployeeID
WHEN NOT MATCHED THEN
    INSERT (EmployeeID, FirstName, LastName, Salary)
    VALUES (source.EmployeeID, source.FirstName, source.LastName, source.Salary);
```

3. **Xóa nhân viên không hoạt động (WHEN MATCHED AND DELETE):**

```sql
MERGE INTO Employees AS target
USING TempEmployees AS source
ON target.EmployeeID = source.EmployeeID
WHEN MATCHED AND source.Status = 'Inactive' THEN
    DELETE;
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

* **`ON` cẩn thận:** Điều kiện `ON` phải chính xác, để tránh cập nhật sai.
* **Transactions:** Dùng `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK` khi update quan trọng (như đã nói ở bài trước về
  UPDATE).
* **Hiệu suất:** Nếu bảng quá lớn, có thể ảnh hưởng đến hiệu suất.
* **Thử nghiệm:** Thử trên môi trường phát triển trước khi chạy trên production.

### **VI. KẾT LUẬN (TỔNG KẾT)**

`UPDATE MERGE` là một câu lệnh mạnh mẽ, giúp bạn đồng bộ dữ liệu giữa các bảng một cách hiệu quả. Hy vọng qua bài viết
này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách "ngon lành". Chúc các bạn code thành công! 😎
