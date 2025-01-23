## **🚀 "GIẢI MÃ" CROSS JOIN TRONG SQL SERVER: "PHÉP NHÂN" BẢNG CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh khá đặc biệt trong SQL Server:
`CROSS JOIN`. Nghe có vẻ "lạ" nhưng thực ra nó cũng có những ứng dụng của nó đấy. Cùng mình "mổ xẻ" nó nhé!

![Cross Join](/assets/images/sql-joins-venn-diagrams-cross-join-1.png)

### **I. CROSS JOIN LÀ GÌ? (NHƯ "PHÉP NHÂN" BẢNG)**

- **`CROSS JOIN`:** Là một kiểu kết nối bảng trong SQL, dùng để tạo ra _tất cả các cặp kết hợp_ giữa các bản ghi của 2
  bảng.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn có 2 danh sách: một danh sách đồ ăn và một danh sách đồ uống, `CROSS JOIN` sẽ tạo ra tất cả các
      cặp kết hợp (ví dụ: cơm với trà, cơm với nước ngọt, phở với trà, phở với nước ngọt, ...).
- **Quan trọng vì:**
    - **Tạo dữ liệu mẫu:** Dùng để tạo dữ liệu thử nghiệm, test.
    - **Kết hợp tất cả:** Tạo ra mọi kết hợp giữa các yếu tố.
    - **Phân tích:** Phân tích các kết hợp có thể giữa các dữ liệu.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG CROSS JOIN)**

```sql
SELECT column1, column2, ...
FROM table1
CROSS JOIN table2;
```

- **`SELECT column1, column2, ...`:** Chọn các cột cần lấy từ bảng.
- **`FROM table1 CROSS JOIN table2`:** Kết hợp bảng `table1` và `table2`.
- **Không có điều kiện `ON`:** Vì nó kết hợp tất cả các cặp có thể.

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có 2 bảng:

- **`Products`:** (ProductID, ProductName)
- **`Colors`:** (ColorID, ColorName)

1. **Kết hợp tất cả sản phẩm với màu sắc:**

```sql
SELECT p.ProductName, c.ColorName
FROM Products p
CROSS JOIN Colors c;
```

- **Kết quả:** Liệt kê tất cả các cặp sản phẩm và màu sắc.

2. **Kết hợp có điều kiện (WHERE):**

```sql
SELECT p.ProductName, c.ColorName
FROM Products p
CROSS JOIN Colors c
WHERE c.ColorName = 'Red';
```

- **Kết quả:** Chỉ lấy các kết hợp mà màu sắc là Red

3. **Kết hợp và sắp xếp (ORDER BY):**

```sql
SELECT p.ProductName, c.ColorName
FROM Products p
CROSS JOIN Colors c
ORDER BY p.ProductName, c.ColorName;
```

- **Kết quả:** Kết quả được sắp xếp theo tên sản phẩm và màu sắc.

### **IV. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Hiệu suất:** Có thể tạo ra một bảng kết quả rất lớn, nên cẩn thận với bảng lớn.
- **Dữ liệu nhiều:** Kết quả có thể rất nhiều, cần lọc nếu cần (dùng `WHERE`).
- **Không có điều kiện `ON`:** Khác với các loại `JOIN` khác, `CROSS JOIN` không có `ON`.
- **Ít dùng:** Thường chỉ dùng trong các trường hợp đặc biệt (tạo dữ liệu mẫu, ...).

### **V. KẾT LUẬN (TỔNG KẾT)**

`CROSS JOIN` là một cách kết hợp bảng đặc biệt, tạo ra tất cả các cặp kết hợp có thể. Tuy không thường dùng như các loại
`JOIN` khác, nhưng nó lại rất hữu ích trong một số tình huống nhất định. Hy vọng qua bài viết này, các bạn đã hiểu rõ
hơn về nó và có thể sử dụng nó một cách hợp lý. Chúc các bạn code thành công! 😎
