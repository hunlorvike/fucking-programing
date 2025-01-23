## **🚀 "GIẢI MÃ" CÂU LỆNH DELETE TRONG SQL SERVER: "DỌN DẸP" DỮ LIỆU TRONG "KHO" CỦA BẠN 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cực kỳ quan trọng trong SQL Server:
`DELETE`. Đây là câu lệnh giúp bạn xóa dữ liệu không cần thiết trong cơ sở dữ liệu của mình, rất quan trọng để quản lý
và duy trì "kho" dữ liệu của bạn. Cùng mình "mổ xẻ" nó nhé!

### **I. CÂU LỆNH DELETE LÀ GÌ? (XÓA DỮ LIỆU TRONG "KHO")**

- **`DELETE`:** Là câu lệnh SQL dùng để _xóa dữ liệu_ (một hoặc nhiều bản ghi) khỏi một bảng trong cơ sở dữ liệu.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn dọn dẹp tủ: bạn chọn món đồ không cần nữa và bỏ nó ra.
- **Quan trọng vì:**
    - **Xóa dữ liệu cũ:** Loại bỏ dữ liệu không cần thiết, lỗi thời.
    - **Giảm dung lượng:** Giúp database nhỏ gọn hơn.
    - **Bảo mật:** Xóa các thông tin nhạy cảm không cần lưu trữ.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG DELETE)**

#### **2.1. XÓA MỘT SỐ BẢN GHI (XÓA MỘT SỐ "MÓN ĐỒ")**

```sql
DELETE FROM table_name
WHERE condition;
```

- **`DELETE FROM table_name`:** Chọn bảng cần xóa dữ liệu.
- **`WHERE condition`:** Điều kiện để chọn bản ghi cần xóa.
- **Ví dụ:**

```sql
DELETE FROM Employees
WHERE EmployeeID = 10;
```

#### **2.2. XÓA TẤT CẢ BẢN GHI (XÓA HẾT "ĐỒ" TRONG TỦ)**

```sql
DELETE FROM table_name;
```

- **`DELETE FROM table_name`:** Chọn bảng cần xóa _tất cả_ dữ liệu.
- **Ví dụ:**

```sql
DELETE FROM Employees;
```

### **III. CÁC TÙY CHỌN MỞ RỘNG (CÁC "CHIÊU" NÂNG CAO)**

#### **3.1. `WHERE` (XÓA CÓ "CHỌN LỌC")**

- `WHERE` để chọn các bản ghi cần xóa.
- Nếu _không có `WHERE`_, thì sẽ xóa _toàn bộ_ bảng.

```sql
DELETE FROM table_name
WHERE condition;
```

- **Ví dụ:**

```sql
DELETE FROM Employees
WHERE Department = 'HR';
```

#### **3.2. `TOP` (XÓA MỘT SỐ LƯỢNG NHẤT ĐỊNH)**

- `TOP` để giới hạn số lượng bản ghi cần xóa.

```sql
DELETE TOP (n) FROM table_name
WHERE condition;
```

- **Ví dụ:**

```sql
DELETE TOP (5) FROM Employees
WHERE Department = 'Sales';
```

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Xóa 1 nhân viên:**

```sql
DELETE FROM Employees
WHERE EmployeeID = 101;
```

2. **Xóa tất cả nhân viên trong một phòng ban:**

```sql
DELETE FROM Employees
WHERE Department = 'HR';
```

3. **Xóa 10 nhân viên đầu tiên:**

```sql
DELETE TOP (10) FROM Employees;
```

4. **Xóa tất cả nhân viên:**

```sql
DELETE FROM Employees;
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **`WHERE` cẩn thận:** Nếu không có `WHERE` hoặc dùng sai, sẽ xóa _toàn bộ_ bảng (gây lỗi).
- **Transactions:** Dùng `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK` khi xóa dữ liệu quan trọng (để có thể undo).
- **Kiểm tra trước:** Dùng `SELECT` trước để xem bản ghi nào sẽ bị xóa.
- **Sao lưu:** Nếu xóa nhiều dữ liệu, backup lại database trước.
- **Chỉ mục:** Có thể tạm tắt index để xóa nhanh, bật lại sau (như bài về bulk insert).

### **VI. KẾT LUẬN (TỔNG KẾT)**

`DELETE` là câu lệnh rất quan trọng để xóa dữ liệu không cần thiết trong SQL Server. Hy vọng qua bài viết này, các bạn
đã hiểu rõ hơn về nó và có thể dùng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
