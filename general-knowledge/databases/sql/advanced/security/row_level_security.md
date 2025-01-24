## **🚀 "GIẢI MÃ" ROW-LEVEL SECURITY: BẢO MẬT DỮ LIỆU "TỪNG DÒNG" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một tính năng cực kỳ quan trọng trong bảo mật SQL
Server: Row-Level Security (RLS). Nghe có vẻ "bí mật" nhưng thực ra nó là một cách để bạn bảo vệ dữ liệu nhạy cảm của
mình, đảm bảo rằng mỗi người dùng chỉ thấy dữ liệu mà họ được phép xem. Cùng mình "mổ xẻ" nó nhé!

### **I. ROW-LEVEL SECURITY (RLS) LÀ GÌ? (BẢO VỆ DỮ LIỆU KIỂU GÌ?)**

- **Row-Level Security (RLS):** Là tính năng trong SQL Server giúp _kiểm soát quyền truy cập dữ liệu_ ở mức độ _từng
  dòng_ (row), dựa trên điều kiện lọc.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn có một quyển sổ mà chỉ có một số người được phép đọc một số trang nhất định (dựa trên vai trò
      của họ).
- **Quan trọng vì:**
    - **Bảo mật:** Bảo vệ dữ liệu nhạy cảm (không cho người không có quyền xem).
    - **Phân quyền:** Phân quyền truy cập dữ liệu cho từng người dùng hoặc nhóm người dùng.
    - **Linh hoạt:** Cho phép cấu hình nhiều điều kiện lọc phức tạp.

### **II. CÁCH HOẠT ĐỘNG CỦA RLS (LỌC DỮ LIỆU KIỂU GÌ?)**

1. **Tạo hàm lọc (Filter Function):** Viết một hàm (inline table-valued function) để xác định xem người dùng có được
   phép xem dòng dữ liệu đó không.
2. **Tạo chính sách bảo mật (Security Policy):** Tạo security policy, liên kết hàm lọc với bảng cần bảo vệ.
3. **SQL Server áp dụng:** Khi người dùng truy vấn dữ liệu, SQL Server sẽ tự động dùng hàm lọc để loại bỏ các dòng mà
   người dùng không có quyền xem.

### **III. CÚ PHÁP CƠ BẢN (CÁCH DÙNG RLS)**

#### **3.1. TẠO HÀM LỌC (FILTER FUNCTION)**

```sql
CREATE FUNCTION security.fn_securitypredicate(@UserName SYSNAME)
    RETURNS TABLE
WITH SCHEMABINDING
AS
    RETURN SELECT 1 AS fn_securitypredicate_result
            WHERE @UserName = USER_NAME()
```

- **`CREATE FUNCTION security.fn_securitypredicate(...)`:** Tạo hàm lọc với tên `fn_securitypredicate` trong schema
  `security`.
- **`@UserName SYSNAME`:** Tham số đầu vào của hàm (tên người dùng hiện tại).
- **`RETURNS TABLE`:** Hàm trả về một bảng.
- **`WITH SCHEMABINDING`:** Đảm bảo hàm không phụ thuộc vào schema khác.
- **`WHERE @UserName = USER_NAME()`:** Điều kiện lọc (chỉ cho phép người dùng xem dữ liệu của mình).

#### **3.2. TẠO CHÍNH SÁCH BẢO MẬT (SECURITY POLICY)**

```sql
CREATE SECURITY POLICY policy_name
    ADD FILTER PREDICATE security.fn_securitypredicate(UserName)
    ON dbo.table_name
    WITH (STATE = ON);
```

- **`CREATE SECURITY POLICY policy_name`:** Tạo security policy với tên `policy_name`.
- **`ADD FILTER PREDICATE security.fn_securitypredicate(UserName)`:** Liên kết hàm lọc với bảng.
- **`ON dbo.table_name`:** Chọn bảng cần bảo vệ.
- **`WITH (STATE = ON)`:** Bật security policy.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có bảng `Orders` (OrderID, CustomerID, OrderDate, TotalAmount), và muốn:

- Người dùng chỉ được xem đơn hàng của chính mình (dựa trên `CustomerID`).

1. **Tạo hàm lọc:**

```sql
CREATE FUNCTION security.fn_customerpredicate(@CustomerID INT)
    RETURNS TABLE
WITH SCHEMABINDING
AS
    RETURN SELECT 1 AS fn_customerpredicate_result
            WHERE @CustomerID = USER_ID();
```

2. **Tạo security policy:**

```sql
CREATE SECURITY POLICY CustomerSecurityPolicy
    ADD FILTER PREDICATE security.fn_customerpredicate(CustomerID)
    ON dbo.Orders
    WITH (STATE = ON);
```

3. **Khi user có ID là 1 truy vấn:**

```sql
SELECT * FROM Orders;
```

- **Kết quả:** Người dùng có ID 1 chỉ thấy các đơn hàng của chính mình (có `CustomerID = 1`).

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Hàm lọc phải có `SCHEMABINDING`:** Để đảm bảo tính nhất quán, hiệu suất.
- **Điều kiện lọc đúng:** Viết điều kiện lọc cẩn thận, tránh lỗi.
- **Hiệu suất:** Có thể làm chậm query (nhất là với hàm lọc phức tạp).
- **Quyền:** Cần có quyền để tạo hàm, tạo policy, ...
- **Test:** Thử nghiệm kỹ để đảm bảo nó hoạt động đúng.
- **Không dùng cho admin:** Security policy có thể không ảnh hưởng đến user có quyền admin (vì admin có quyền xem tất
  cả).

### **VI. ƯU ĐIỂM CỦA RLS (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Bảo mật:** Dữ liệu được bảo vệ ở mức độ dòng, tránh lộ thông tin nhạy cảm.
- **Phân quyền linh hoạt:** Phân quyền theo nhiều điều kiện phức tạp.
- **Dễ quản lý:** Quản lý tập trung các chính sách bảo mật.

### **VII. NHƯỢC ĐIỂM CỦA RLS (ĐIỂM "KHÓ CHỊU")**

- **Có thể chậm:** Nếu hàm lọc phức tạp, có thể làm chậm query.
- **Khó debug:** Có thể khó kiểm tra logic của security policy.
- **Không thay thế authorization:** Không thay thế được việc phân quyền dựa trên vai trò (RBAC), thường kết hợp với
  RBAC (bài authentication/authorization).

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Row-Level Security (RLS) là một "vũ khí" mạnh mẽ giúp bạn bảo vệ dữ liệu nhạy cảm trong SQL Server, đảm bảo rằng người
dùng chỉ thấy dữ liệu mà họ được phép xem. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào
dự án của mình. Chúc các bạn code thành công! 😎
