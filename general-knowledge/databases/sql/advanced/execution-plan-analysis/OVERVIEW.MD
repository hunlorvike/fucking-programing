## **🚀 "GIẢI MÃ" EXECUTION PLAN: "BẢN ĐỒ" TRUY VẤN SQL SERVER CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một công cụ cực kỳ mạnh mẽ trong SQL Server: Execution
Plan (Kế hoạch Thực thi). Đây là "bản đồ" chi tiết về cách SQL Server thực thi câu lệnh của bạn, giúp bạn tìm ra các
điểm "nghẽn cổ chai" và tối ưu hóa truy vấn. Cùng mình "mổ xẻ" nó nhé!

### **I. EXECUTION PLAN LÀ GÌ? (NHƯ "BẢN ĐỒ" CHO QUERY)**

- **Execution Plan (Kế hoạch Thực thi):** Là bản đồ chi tiết về các bước mà SQL Server thực hiện để chạy một câu lệnh
  SQL (như `SELECT`, `INSERT`, `UPDATE`, `DELETE`).
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn đi du lịch: Google Maps sẽ chỉ cho bạn đường đi, và Execution Plan cũng vậy, nó chỉ cho bạn con
      đường mà SQL Server đi để lấy/sửa/xóa dữ liệu.
- **Quan trọng vì:**
    - **Hiểu cách query chạy:** Biết SQL Server làm gì bên trong.
    - **Tìm điểm yếu:** Phát hiện các bước chạy chậm, tốn tài nguyên.
    - **Tối ưu:** Cải thiện query để chạy nhanh hơn, hiệu quả hơn.

### **II. CÁC THÀNH PHẦN CHÍNH CỦA EXECUTION PLAN (NHỮNG "ĐỊA DANH" TRÊN BẢN ĐỒ)**

1. **Operators (Toán tử):** Các "cột mốc" trên đường đi, biểu diễn các hành động của SQL Server (ví dụ: `Table Scan`,
   `Index Seek`, `Sort`, `Hash Match`).
2. **Arrows (Mũi tên):** Chỉ thứ tự thực hiện (dòng chảy dữ liệu).
3. **Cost (Chi phí):** Ước tính chi phí của từng toán tử, giúp nhận biết các toán tử tốn tài nguyên.
4. **Cardinality (Bản số):** Ước tính số lượng dòng dữ liệu đi qua mỗi toán tử.
5. **Properties (Thuộc tính):** Thông tin chi tiết về toán tử (bảng, cột, index, ...).

### **III. CÁCH XEM EXECUTION PLAN (CÁCH "MỞ BẢN ĐỒ")**

1. **SQL Server Management Studio (SSMS):**
    - Mở SSMS, viết câu lệnh SQL.
    - Bấm nút "Display Estimated Execution Plan" (Ctrl+L) để xem kế hoạch ước tính.
    - Bấm nút "Display Actual Execution Plan" (Ctrl+M) để xem kế hoạch thực tế.
2. **Azure Data Studio:**
    - Tương tự SSMS, nhưng giao diện khác một chút.

### **IV. CÁC TOÁN TỬ THƯỜNG GẶP (NHỮNG "ĐỊA DANH" QUEN THUỘC)**

1. **`Table Scan`:** Đọc toàn bộ dữ liệu của bảng (như "đi hết cả khu").
    - **Xấu:** Thường chậm, nên tránh với bảng lớn.
2. **`Index Seek`:** Tìm dữ liệu bằng index (như "đi tắt").
    - **Tốt:** Nhanh, dùng khi có index tốt.
3. **`Index Scan`:** Duyệt qua toàn bộ index (như "đi dạo" trong danh sách index).
    - **Không tốt:** Thường không nhanh bằng `Index Seek`.
4. **`Sort`:** Sắp xếp dữ liệu (tốn thời gian và bộ nhớ).
    - **Nên tránh:** Khi không thực sự cần thiết.
5. **`Hash Match`:** Dùng để kết hợp dữ liệu từ 2 bảng (thường dùng trong JOIN).
    - **Có thể chậm:** Với bảng lớn.
6. **`Nested Loops`:** Kết hợp dữ liệu bằng cách loop qua các bản ghi của 2 bảng.
    - **Có thể chậm:** Với bảng lớn.
7. **`Merge Join`:** Kết hợp dữ liệu bằng cách merge các bản ghi đã sắp xếp (nhanh hơn Nested Loops nếu dữ liệu đã sắp
   xếp).
8. **`Clustered Index Scan`:** Duyệt toàn bộ clustered index của bảng.
9. **`Clustered Index Seek`:** Tìm dữ liệu bằng clustered index.
10. **`Key Lookup`:** Sau khi tìm index, cần lookup vào bảng để lấy các cột không có trong index.
    - **Có thể chậm:** Nếu phải lookup nhiều.

### **V. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **5.1. MỘT QUERY ĐƠN GIẢN (KHÔNG INDEX):**

```sql
SELECT *
FROM Employees
WHERE Department = 'HR';
```

- **Execution Plan:** Thường có `Table Scan` (đọc toàn bộ bảng).
- **Lời khuyên:** Nên tạo index trên cột `Department`.

#### **5.2. QUERY DÙNG INDEX:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE EmployeeID = 10;
```

- **Execution Plan:** Có `Index Seek` (truy cập index nhanh).
- **Lời khuyên:** Tạo index trên `EmployeeID` nếu chưa có.

#### **5.3. QUERY DÙNG JOIN:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees AS e
INNER JOIN Departments AS d
ON e.DepartmentID = d.DepartmentID;
```

- **Execution Plan:** Có thể có `Nested Loops`, `Hash Match` hoặc `Merge Join`.
- **Lời khuyên:** Tạo index trên các cột `JOIN`.

### **VI. MỘT SỐ MẸO KHI PHÂN TÍCH EXECUTION PLAN (ĐỂ "ĐỌC BẢN ĐỒ" TỐT HƠN)**

1. **Tìm các toán tử tốn nhiều chi phí:** Toán tử có chi phí cao thường là điểm "nghẽn cổ chai".
2. **Xem cardinality:** Để biết số lượng dòng dữ liệu đi qua từng toán tử.
3. **Đọc từ phải sang trái:** Các toán tử bên phải thường chạy trước (tùy vào plan).
4. **Xem các warnings:** Nếu có cảnh báo, hãy xem xét và khắc phục (thiếu index, ...).
5. **So sánh kế hoạch thực tế và ước tính:** Xem có gì khác nhau không.
6. **Thay đổi code, xem lại plan:** Tối ưu code và kiểm tra lại Execution Plan để thấy hiệu quả.

### **VII. KẾT LUẬN (TỔNG KẾT)**

Execution Plan là "bạn thân" của dân code SQL, giúp bạn hiểu rõ và tối ưu hóa các truy vấn. Hy vọng qua bài viết này,
các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày. Chúc các bạn code thành công! 😎
