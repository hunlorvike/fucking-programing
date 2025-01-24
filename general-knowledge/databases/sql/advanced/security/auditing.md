## **🚀 "GIẢI MÃ" AUDITING TRONG SQL SERVER: "MẮT THẦN" THEO DÕI DATABASE CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một tính năng rất quan trọng trong SQL Server:
Auditing (Kiểm toán). Nghe có vẻ "khó hiểu" nhưng thực ra nó là một cách để bạn "ghi lại nhật ký" hoạt động của
database, biết được ai đã làm gì, khi nào. Cùng mình "mổ xẻ" nó nhé!

### **I. AUDITING LÀ GÌ? (NHƯ "NHẬT KÝ" HOẠT ĐỘNG)**

- **Auditing (Kiểm toán):** Là tính năng trong SQL Server giúp _ghi lại_ các thao tác trên database (ai đã làm gì, khi
  nào, trên bảng nào, ...).
- **Nó hoạt động như thế nào?**
    - Giống như bạn ghi nhật ký hàng ngày: bạn ghi lại tất cả những việc bạn đã làm trong ngày (đọc sách, học bài, xem
      phim,...).
- **Quan trọng vì:**
    - **Theo dõi:** Biết được ai đã làm gì trên database.
    - **Phát hiện lỗi:** Dễ dàng phát hiện các hành vi bất thường.
    - **Bảo mật:** Phát hiện các cuộc tấn công, xâm nhập trái phép.
    - **Kiểm toán:** Cung cấp bằng chứng cho việc kiểm toán.

### **II. CÁCH HOẠT ĐỘNG CỦA AUDITING (GHI "NHẬT KÝ" NHƯ THẾ NÀO?)**

1. **Chọn đối tượng:** Chọn database hoặc bảng cần theo dõi.
2. **Chọn hành động:** Chọn các hành động cần ghi log (SELECT, INSERT, UPDATE, DELETE, ...).
3. **Tạo Audit:** Tạo đối tượng audit để ghi log.
4. **Xem log:** Xem nhật ký các hoạt động.

### **III. CÚ PHÁP CƠ BẢN (CÁCH DÙNG AUDITING)**

#### **3.1. TẠO SERVER AUDIT (TẠO "NHẬT KÝ" CHUNG)**

```sql
CREATE SERVER AUDIT audit_name
TO FILE (FILEPATH = 'C:\AuditLogs\AuditLog.sqlaudit');
```

- **`CREATE SERVER AUDIT audit_name`:** Tạo audit trên server với tên `audit_name`.
- **`TO FILE (FILEPATH = ...)`:** Lưu log vào file.

#### **3.2. TẠO DATABASE AUDIT SPECIFICATION (TẠO "NHẬT KÝ" CHO DATABASE)**

```sql
CREATE DATABASE AUDIT SPECIFICATION database_audit_name
FOR SERVER AUDIT audit_name
ADD (SELECT, INSERT, UPDATE, DELETE ON dbo.table_name)
WITH (STATE = ON);
```

- **`CREATE DATABASE AUDIT SPECIFICATION database_audit_name`:** Tạo audit specification (mô tả các hành động ghi log)
  cho database với tên `database_audit_name`.
- **`FOR SERVER AUDIT audit_name`:** Liên kết với server audit.
- **`ADD (SELECT, INSERT, UPDATE, DELETE ON dbo.table_name)`:** Chọn các hành động cần ghi log cho bảng
  `dbo.table_name`.
- **`WITH (STATE = ON)`:** Bật audit specification.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **Tạo server audit:**

```sql
CREATE SERVER AUDIT EmployeeAudit
TO FILE (FILEPATH = 'C:\AuditLogs\EmployeeAudit.sqlaudit');
```

2. **Tạo database audit specification cho bảng `Employees`:**

```sql
CREATE DATABASE AUDIT SPECIFICATION EmployeeAuditSpecification
FOR SERVER AUDIT EmployeeAudit
ADD (SELECT, INSERT, UPDATE, DELETE ON dbo.Employees)
WITH (STATE = ON);
```

- **Giải thích:** Ghi log các thao tác `SELECT`, `INSERT`, `UPDATE`, `DELETE` trên bảng `Employees`.

3. **Bật audit cho database:**

```sql
ALTER SERVER AUDIT EmployeeAudit WITH (STATE = ON);
```

### **V. CÁC THAO TÁC VỚI AUDIT (LÀM GÌ VỚI "NHẬT KÝ")**

1. **Xem nhật ký:** Dùng SQL Server Management Studio hoặc các câu truy vấn để xem các file log.
2. **Lọc nhật ký:** Lọc theo thời gian, người dùng, hành động, ...
3. **Tắt/bật:** Bật/tắt audit khi cần thiết.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Chọn hành động:** Chọn các hành động cần log (đừng log quá nhiều, tốn tài nguyên).
- **Vị trí lưu:** Nên lưu log vào nơi an toàn (ổ cứng riêng, ...).
- **Quản lý file log:** Cần có kế hoạch quản lý, lưu trữ, xoay vòng file log (tránh đầy ổ cứng).
- **Quyền:** Cần quyền để tạo, quản lý audit.
- **Hiệu suất:** Log có thể ảnh hưởng đến hiệu suất database, nên tối ưu khi dùng.

### **VII. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Phát hiện xâm nhập:** Tìm ra các truy vấn bất thường, hành vi đáng ngờ.
- **Kiểm toán:** Cung cấp bằng chứng cho kiểm toán.
- **Tuân thủ:** Đáp ứng các tiêu chuẩn bảo mật.
- **Gỡ lỗi:** Tìm ra nguyên nhân lỗi từ các thao tác trên database.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Auditing là một tính năng bảo mật rất quan trọng trong SQL Server, giúp bạn theo dõi và kiểm soát các hoạt động trên
database của mình. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào các ứng dụng của mình.
Chúc các bạn code thành công! 😎
