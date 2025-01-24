## **🚀 "GIẢI MÃ" DYNAMIC DATA MASKING: "LÀM MỜ" DỮ LIỆU NHẠY CẢM TRONG SQL SERVER CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một tính năng rất thú vị trong SQL Server: Dynamic
Data Masking (DDM). Nghe có vẻ "ảo diệu" nhưng thực ra nó là một cách để bạn "làm mờ" dữ liệu nhạy cảm, bảo vệ thông tin
quan trọng mà không ảnh hưởng đến dữ liệu gốc. Cùng mình "mổ xẻ" nó nhé!

### **I. DYNAMIC DATA MASKING (DDM) LÀ GÌ? (LÀM MỜ DỮ LIỆU KIỂU GÌ?)**

- **Dynamic Data Masking (DDM):** Là một tính năng trong SQL Server giúp _ẩn_ hoặc _làm mờ_ dữ liệu nhạy cảm (ví dụ: số
  thẻ tín dụng, số điện thoại, email) khi người dùng truy vấn.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn xem phim có cảnh "mờ": bạn vẫn thấy có người, nhưng không thấy rõ mặt.
- **Quan trọng vì:**
    - **Bảo mật:** Ẩn thông tin nhạy cảm khỏi những người không có quyền xem.
    - **Dễ sử dụng:** Không cần thay đổi dữ liệu gốc.
    - **Linh hoạt:** Có nhiều cách để làm mờ dữ liệu.
    - **Thực thi theo thời gian thực:** Dữ liệu được làm mờ ngay khi truy vấn.

### **II. CÁCH HOẠT ĐỘNG CỦA DDM (LÀM MỜ DỮ LIỆU NHƯ THẾ NÀO?)**

1. **Định nghĩa Mask:** Bạn chọn cột cần làm mờ và cách làm mờ (ví dụ: thay số bằng `X`, che email, ...).
2. **Tạo Mask:** Tạo Dynamic Data Masking cho cột đó (không thay đổi dữ liệu gốc).
3. **Khi truy vấn:** Khi người dùng truy vấn dữ liệu, SQL Server sẽ tự động làm mờ dữ liệu dựa trên Mask đã định nghĩa (
   đối với những user không có quyền xem dữ liệu gốc).
4. **Quyền:** Người dùng với quyền đặc biệt có thể thấy dữ liệu gốc.

### **III. CÁC KIỂU LÀM MỜ PHỔ BIẾN (CÁC CÁCH "CHE MẶT")**

1. **`default()`:** Thay thế các ký tự bằng `x` hoặc các ký tự khác.
    - **Ví dụ:** Che số điện thoại thành `xxx-xxx-xxxx`.
2. **`email()`:** Làm mờ email bằng cách thay thế một phần của email bằng ký tự `x`.
    - **Ví dụ:** Làm mờ email thành `xx@xx.com`.
3. **`partial(prefix,[padding],suffix)`:** Làm mờ một phần chuỗi, dùng prefix (đầu), padding (số ký tự được thay bằng
   chữ x) và suffix (cuối).

- **Ví dụ:** Làm mờ credit card thành `XXXX-XXXX-XXXX-1234`.

4. **`random()`:** Tạo một số ngẫu nhiên, hữu ích cho những giá trị như số điện thoại.
    - **Ví dụ**: Tạo các số điện thoại ngẫu nhiên thay thế cho số điện thoại thật.
5. **`datetime`**: Chuyển ngày tháng về một giá trị cố định.

### **IV. CÚ PHÁP CƠ BẢN (CÁCH DÙNG DDM)**

```sql
ALTER TABLE table_name
ALTER COLUMN column_name ADD MASKED WITH (FUNCTION = 'masking_function()');
```

- **`ALTER TABLE table_name ALTER COLUMN column_name`:** Chọn bảng và cột cần làm mờ.
- **`ADD MASKED WITH (FUNCTION = 'masking_function()')`:** Chọn cách làm mờ (`default()`, `email()`, `partial()`, ...).

### **V. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có bảng `Customers`:

- **(CustomerID, FirstName, LastName, Email, PhoneNumber, CreditCardNumber)**

1. **Làm mờ email (email()):**

```sql
ALTER TABLE Customers
ALTER COLUMN Email ADD MASKED WITH (FUNCTION = 'email()');
```

- **Giải thích:** Làm mờ cột `Email` bằng hàm `email()`.

2. **Làm mờ số điện thoại (partial):**

```sql
ALTER TABLE Customers
ALTER COLUMN PhoneNumber ADD MASKED WITH (FUNCTION = 'partial(0,"XXX-XXX-", 4)');
```

- **Giải thích:** Làm mờ cột `PhoneNumber` bằng hàm `partial` để chỉ hiển thị 4 số cuối.

3. **Làm mờ số thẻ tín dụng (partial):**

```sql
ALTER TABLE Customers
ALTER COLUMN CreditCardNumber ADD MASKED WITH (FUNCTION = 'partial(0,"XXXX-XXXX-XXXX-",4)');
```

- **Giải thích**: Làm mờ cột `CreditCardNumber` bằng hàm `partial` để chỉ hiển thị 4 số cuối của thẻ tín dụng.

4. **Làm mờ một giá trị số ngẫu nhiên:**

```sql
ALTER TABLE Customers
ALTER COLUMN CustomerID ADD MASKED WITH (FUNCTION = 'random(1, 1000)');
```

- **Giải thích:** Làm mờ cột `CustomerID` bằng một số ngẫu nhiên từ 1 đến 1000.

5. **Làm mờ giá trị ngày tháng:**

```sql
ALTER TABLE Orders
ALTER COLUMN OrderDate ADD MASKED WITH (FUNCTION = 'datetime(01/01/2024)')
```

- **Giải thích**: Chuyển đổi tất cả các ngày sang một giá trị ngày tháng cố định.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Không thay đổi dữ liệu gốc:** DDM _không_ thay đổi dữ liệu thật trong database.
- **Chỉ cho người không có quyền:** Chỉ người dùng _không có quyền_ mới thấy dữ liệu đã làm mờ.
- **Không mã hóa:** Không dùng để mã hóa dữ liệu, chỉ là làm mờ.
- **Không thay thế RLS:** Không thay thế Row-Level Security (bài trước).
- **Hiệu suất:** DDM có thể làm chậm truy vấn, nên cân nhắc kỹ.
- **Kiểm tra kỹ:** Sau khi thiết lập, cần test xem có đúng không.
- **`UNMASK`:** Dùng `UNMASK` permission để thấy dữ liệu thật (cần cấp quyền).

### **VII. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Bảo mật dữ liệu:** Ẩn thông tin nhạy cảm trong ứng dụng.
- **Phát triển/Test:** Tạo dữ liệu test an toàn, không lộ thông tin thật.
- **Báo cáo:** Hiển thị dữ liệu đã làm mờ cho các đối tượng không được quyền xem.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Dynamic Data Masking là một công cụ mạnh mẽ giúp bạn bảo vệ dữ liệu nhạy cảm trong SQL Server. Hy vọng qua bài viết này,
các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào các ứng dụng của mình. Chúc các bạn code thành công! 😎
