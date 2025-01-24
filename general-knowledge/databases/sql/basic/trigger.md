## **🚀 "GIẢI MÃ" TRIGGERS TRONG SQL SERVER: "CẢNH BÁO" DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong SQL Server:
Triggers (Bộ kích hoạt). Đây là một "vũ khí" lợi hại giúp bạn tự động thực thi code khi có sự thay đổi trên database,
giúp quản lý và duy trì dữ liệu một cách hiệu quả. Cùng mình "mổ xẻ" nó nhé!

### **I. TRIGGERS LÀ GÌ? (NHƯ "CHUÔNG BÁO" TRONG DATABASE)**

- **Triggers (Bộ kích hoạt):** Là các đối tượng trong SQL Server, dùng để _tự động thực thi code SQL_ khi có sự kiện xảy
  ra trên database (ví dụ: INSERT, UPDATE, DELETE).
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn cài báo thức: khi đến giờ báo thức, nó sẽ tự động reo.
- **Quan trọng vì:**
    - **Tự động:** Thực hiện các hành động tự động (không cần can thiệp của người dùng).
    - **Toàn vẹn dữ liệu:** Đảm bảo tính toàn vẹn và nhất quán của dữ liệu.
    - **Kiểm toán:** Theo dõi các thay đổi trên database (ghi log).
    - **Bảo mật:** Kiểm tra, ngăn chặn các thao tác không hợp lệ.

### **II. CÁC LOẠI TRIGGERS (CÁC LOẠI "CHUÔNG BÁO")**

1. **`DML Triggers` (Data Manipulation Language Triggers):**
    - Kích hoạt khi có các thao tác `INSERT`, `UPDATE`, `DELETE`.
    - Có thể chạy `AFTER` (sau khi thao tác) hoặc `INSTEAD OF` (thay vì thao tác).
2. **`DDL Triggers` (Data Definition Language Triggers):**
    - Kích hoạt khi có thay đổi cấu trúc database (`CREATE`, `ALTER`, `DROP`).
    - Dùng để theo dõi các thay đổi database.
3. **`Logon Triggers`:**
    - Kích hoạt khi có người login vào SQL Server.
    - Dùng để kiểm soát quyền truy cập, log login.

### **III. CÚ PHÁP CƠ BẢN (CÁCH DÙNG TRIGGERS)**

#### **3.1. TẠO DML TRIGGER (BÁO KHI THÊM, SỬA, XÓA DỮ LIỆU)**

```sql
CREATE TRIGGER trigger_name
ON table_name
AFTER/INSTEAD OF INSERT/UPDATE/DELETE
AS
BEGIN
    -- Câu lệnh SQL
END;
```

- **`CREATE TRIGGER trigger_name`:** Tạo trigger với tên `trigger_name`.
- **`ON table_name`:** Chọn bảng trigger sẽ kích hoạt.
- **`AFTER/INSTEAD OF INSERT/UPDATE/DELETE`:** Chọn sự kiện kích hoạt trigger.
- **`AS BEGIN ... END`:** Khối code SQL cần thực hiện khi trigger kích hoạt.

#### **3.2. TẠO DDL TRIGGER (BÁO KHI THAY ĐỔI CẤU TRÚC)**

```sql
CREATE TRIGGER trigger_name
ON DATABASE / ALL SERVER
FOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
AS
BEGIN
    -- Câu lệnh SQL
END;
```

- **`ON DATABASE / ALL SERVER`:** Chọn database hoặc server để kích hoạt trigger.
- **`FOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE`:** Chọn các sự kiện (create, alter, drop) để kích hoạt trigger.

#### **3.3. TẠO LOGON TRIGGER (BÁO KHI AI ĐĂNG NHẬP)**

```sql
CREATE TRIGGER trigger_name
ON ALL SERVER
FOR LOGON
AS
BEGIN
    -- Câu lệnh SQL
END;
```

- **`ON ALL SERVER`:** Kích hoạt trigger trên toàn server.
- **`FOR LOGON`:** Kích hoạt khi có người đăng nhập.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **1. DML TRIGGER (GHI LOG KHI THÊM MỚI NHÂN VIÊN):**

```sql
CREATE TRIGGER trg_employees_insert
ON Employees
AFTER INSERT
AS
BEGIN
    INSERT INTO Employees_Log (EmployeeID, LogMessage, LogTime)
    SELECT EmployeeID, 'New Employee Added', GETDATE()
    FROM INSERTED;
END;
```

- **Giải thích:**
    - Tạo trigger `trg_employees_insert` trên bảng `Employees`.
    - Kích hoạt `AFTER INSERT` (sau khi thêm mới nhân viên).
    - Thêm log vào bảng `Employees_Log`.
    - `INSERTED`: Bảng ảo chứa các bản ghi vừa được thêm mới.

#### **2. DDL TRIGGER (GHI LOG KHI THAY ĐỔI BẢNG):**

```sql
CREATE TRIGGER trg_database_change
ON DATABASE
FOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
AS
BEGIN
    INSERT INTO Database_Log (Event, EventTime, LoginName)
    SELECT EVENTDATA().value('(/EVENT_INSTANCE/EventType)[1]', 'nvarchar(100)'),
           GETDATE(),
           SUSER_SNAME();
END;
```

- **Giải thích:**
    - Tạo trigger `trg_database_change` trên database.
    - Kích hoạt khi tạo, sửa, xóa bảng.
    - Ghi log vào bảng `Database_Log`.
    - `EVENTDATA()`: Hàm trả về thông tin về sự kiện.

#### **3. LOGON TRIGGER (GHI LOG KHI AI ĐĂNG NHẬP):**

```sql
CREATE TRIGGER trg_logon_event
ON ALL SERVER
FOR LOGON
AS
BEGIN
    INSERT INTO Logon_Log (LoginName, LoginTime)
    VALUES (SUSER_SNAME(), GETDATE());
END;
```

- **Giải thích:**
    - Tạo trigger `trg_logon_event` trên toàn server.
    - Kích hoạt khi có người đăng nhập.
    - Ghi log vào bảng `Logon_Log`.
    - `SUSER_SNAME()`: Hàm trả về username.

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Nên dùng `AFTER` hơn `INSTEAD OF`:** Vì `INSTEAD OF` có thể làm ảnh hưởng đến logic của các thao tác.
- **Tránh dùng nhiều trigger:** Có thể làm chậm database (cần tối ưu).
- **Code đơn giản:** Code trong trigger nên ngắn gọn, dễ hiểu, tránh các phép toán phức tạp.
- **Kiểm tra kỹ:** Kiểm tra kỹ lưỡng trước khi dùng trong production.
- **Không thay thế hoàn toàn các biện pháp bảo mật:** Cần dùng kết hợp với các biện pháp bảo mật khác (phân quyền, xác
  thực,...).
- **Tránh vòng lặp:** Không nên có trigger gọi lẫn nhau (gây vòng lặp).

### **VI. ƯU ĐIỂM CỦA TRIGGERS (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Tự động hóa:** Thực hiện các thao tác tự động (không cần code bên ngoài).
- **Toàn vẹn dữ liệu:** Đảm bảo dữ liệu luôn đúng, hợp lệ.
- **Kiểm toán:** Theo dõi các thay đổi, dễ kiểm toán.

### **VII. NHƯỢC ĐIỂM CỦA TRIGGERS (ĐIỂM "KHÓ CHỊU")**

- **Có thể chậm:** Nếu code trigger quá phức tạp.
- **Khó debug:** Có thể khó tìm lỗi trong trigger.
- **Khó bảo trì:** Cần thận trọng khi thay đổi trigger (có thể ảnh hưởng đến hệ thống).

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Triggers là một công cụ mạnh mẽ trong SQL Server, giúp bạn tự động thực thi code khi có sự kiện xảy ra trên database.
Hãy sử dụng chúng một cách cẩn thận và hợp lý để đảm bảo tính toàn vẹn, bảo mật và dễ quản lý dữ liệu. Chúc các bạn code
thành công! 😎
