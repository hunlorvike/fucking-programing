## **🚀 "GIẢI MÃ" TRANSACTIONS TRONG SQL SERVER: "BẢO HIỂM" DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong SQL Server:
Transactions (Giao dịch). Đây là "vũ khí" giúp bạn đảm bảo tính toàn vẹn và nhất quán của dữ liệu, đặc biệt khi thực
hiện nhiều thao tác cùng lúc. Cùng mình "mổ xẻ" nó nhé!

### **I. TRANSACTION LÀ GÌ? (NHƯ "HỢP ĐỒNG" CHO DATABASE)**

- **Transaction (Giao dịch):** Là một chuỗi các thao tác (query SQL) được thực hiện như một _đơn vị công việc_.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn ký hợp đồng: hoặc là tất cả các điều khoản đều được thực hiện, hoặc là không có gì xảy ra (nếu
      có một điều khoản không được chấp nhận).
- **Quan trọng vì:**
    - **Tính toàn vẹn:** Đảm bảo dữ liệu luôn đúng, không bị "nửa vời".
    - **Nhất quán:** Đảm bảo dữ liệu đồng bộ, không bị xung đột.
    - **Khôi phục lỗi:** Nếu có lỗi, có thể quay lại trạng thái ban đầu.

### **II. CÁC THUỘC TÍNH ACID CỦA TRANSACTION (NHƯ "NGUYÊN TẮC VÀNG")**

- **ACID:** Là 4 thuộc tính quan trọng của transaction:
    1. **Atomicity (Nguyên tử):** Tất cả thao tác phải thành công, hoặc không có gì xảy ra.
    2. **Consistency (Nhất quán):** Dữ liệu phải luôn hợp lệ (tuân thủ các quy tắc).
    3. **Isolation (Độc lập):** Các transaction không được ảnh hưởng lẫn nhau (cô lập).
    4. **Durability (Bền vững):** Dữ liệu đã commit sẽ được lưu vĩnh viễn (kể cả khi có sự cố).

### **III. CÚ PHÁP CƠ BẢN (CÁCH DÙNG TRANSACTION)**

1. **Bắt đầu giao dịch (Start Transaction):**

```sql
BEGIN TRANSACTION;
```

2. **Thực hiện các câu lệnh SQL:**

```sql
INSERT INTO Table1 ...;
UPDATE Table2 ...;
DELETE FROM Table3 ...;
```

3. **Kết thúc giao dịch (Commit/Rollback):**

    - **`COMMIT TRANSACTION:`** Hoàn tất (chấp nhận) giao dịch nếu thành công.
    - **`ROLLBACK TRANSACTION:`** Hủy bỏ giao dịch (quay lại trạng thái trước khi giao dịch bắt đầu) nếu có lỗi.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **Thao tác thành công (COMMIT):**

```sql
BEGIN TRANSACTION;

INSERT INTO Orders (OrderID, CustomerID)
VALUES (100, 1);

UPDATE Products
SET Stock = Stock - 2
WHERE ProductID = 5;

COMMIT TRANSACTION;
```

- **Giải thích:**
    - Bắt đầu transaction.
    - Thêm đơn hàng mới vào bảng `Orders`.
    - Giảm số lượng sản phẩm trong bảng `Products`.
    - Kết thúc transaction (commit) nếu không có lỗi.

2. **Thao tác thất bại (ROLLBACK):**

```sql
BEGIN TRANSACTION;

INSERT INTO Orders (OrderID, CustomerID)
VALUES (101, 2);

UPDATE Products
SET Stock = Stock - 10
WHERE ProductID = 10;
-- Giả sử có lỗi xảy ra ở đây (ví dụ: không đủ số lượng sản phẩm)

ROLLBACK TRANSACTION;
```

- **Giải thích:**
    - Bắt đầu transaction.
    - Thêm đơn hàng mới.
    - Cập nhật số lượng sản phẩm (giả sử có lỗi xảy ra).
    - Hủy bỏ transaction (rollback) vì có lỗi.

### **V. MỘT SỐ LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Dùng `BEGIN TRANSACTION`:** Luôn bắt đầu transaction trước khi thực hiện các thao tác.
- **`COMMIT` hoặc `ROLLBACK`:** Luôn kết thúc transaction bằng `COMMIT` (thành công) hoặc `ROLLBACK` (thất bại).
- **Xử lý lỗi:** Nếu có lỗi xảy ra, dùng `ROLLBACK` để khôi phục dữ liệu.
- **Tối ưu:** Nên dùng transaction khi có nhiều query liên quan đến nhau, để đảm bảo tính toàn vẹn.

### **VI. CÁC MỨC ĐỘ CÔ LẬP (TRANSACTION ISOLATION LEVELS) - (KIỂM SOÁT ĐỘ "CHẶT CHẼ")**

- **Read Uncommitted:** Cho phép đọc các thay đổi chưa commit (có thể đọc dữ liệu chưa chính xác).
- **Read Committed:** Không cho phép đọc các thay đổi chưa commit (chỉ đọc dữ liệu đã commit).
- **Repeatable Read:** Không cho phép đọc dữ liệu bị thay đổi trong transaction khác (tránh đọc dữ liệu không nhất
  quán).
- **Serializable:** Mức độ cô lập cao nhất, đảm bảo dữ liệu hoàn toàn nhất quán (có thể ảnh hưởng đến hiệu suất).
- **Cách chọn mức cô lập:**
    - **`Read Uncommitted`:** Ít dùng, trừ khi không quan trọng độ chính xác.
    - **`Read Committed`:** Phổ biến, cân bằng giữa hiệu suất và độ chính xác.
    - **`Repeatable Read`:** Cho các ứng dụng cần độ chính xác cao, có thể dùng khi có nhiều transaction đọc dữ liệu
      cùng lúc.
    - **`Serializable`:** Cho ứng dụng quan trọng, độ chính xác là ưu tiên hàng đầu, nhưng có thể chậm.

#### **Cú pháp:**

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; -- mức cô lập Read Uncommitted

SET TRANSACTION ISOLATION LEVEL READ COMMITTED; -- mức cô lập Read Committed
```

### **VII. KẾT LUẬN (TỔNG KẾT)**

Transaction là một công cụ rất quan trọng để đảm bảo tính toàn vẹn và nhất quán của dữ liệu trong cơ sở dữ liệu. Hy vọng
qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày. Chúc các bạn code thành công!
😎
