## **🚀 "GIẢI MÃ" JSON TRONG SQL SERVER: "LÀM VIỆC" VỚI DỮ LIỆU KHÔNG CẤU TRÚC CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một chủ đề cực kỳ quan trọng và "hot" hiện nay: JSON
trong SQL Server. Nghe có vẻ "lạ lẫm" nhưng thực ra nó là một cách để bạn làm việc với dữ liệu không có cấu trúc cố
định (như kiểu data từ API) một cách dễ dàng. Cùng mình "mổ xẻ" nó nhé!

### **I. JSON TRONG SQL SERVER LÀ GÌ? (LÀM GÌ VỚI DỮ LIỆU "KHÔNG CÓ KHUÔN")**

- **JSON (JavaScript Object Notation):** Là một định dạng dữ liệu _dạng văn bản_, thường được dùng để trao đổi dữ liệu
  giữa các hệ thống.
- **JSON trong SQL Server:** SQL Server hỗ trợ lưu trữ và truy vấn dữ liệu dạng JSON.
- **Quan trọng vì:**
    - **Linh hoạt:** Lưu trữ dữ liệu _không có cấu trúc_ (dữ liệu từ API, dữ liệu cấu hình,...).
    - **Truy vấn:** Truy vấn dữ liệu JSON bằng SQL.
    - **Trao đổi:** Trao đổi dữ liệu giữa các ứng dụng dễ dàng hơn.

### **II. CÁCH LƯU TRỮ DỮ LIỆU JSON (CÁCH "CẤT" DỮ LIỆU JSON)**

- Dùng kiểu dữ liệu `NVARCHAR` hoặc `TEXT` để lưu chuỗi JSON.
- Dùng cột computed (tính toán) để lấy các giá trị từ JSON.

```sql
CREATE TABLE Settings (
    SettingID INT PRIMARY KEY,
    SettingName VARCHAR(100),
    SettingValue NVARCHAR(MAX)
);
```

### **III. CÁC HÀM JSON PHỔ BIẾN (NHỮNG "CHIÊU" XỬ LÝ JSON)**

1. **`JSON_VALUE()`:** Lấy giá trị _đơn_ từ JSON.
2. **`JSON_QUERY()`:** Lấy _đối tượng JSON_ hoặc _mảng JSON_.
3. **`JSON_MODIFY()`:** Sửa đổi giá trị trong JSON.
4. **`ISJSON()`:** Kiểm tra xem chuỗi có phải JSON hợp lệ không.
5. **`OPENJSON()`:** Chuyển đổi JSON thành _dạng bảng_.
6. **`FOR JSON AUTO`**: Chuyển đổi kết quả truy vấn thành chuỗi JSON.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **1. LƯU DỮ LIỆU CẤU HÌNH DẠNG JSON:**

```sql
INSERT INTO Settings (SettingID, SettingName, SettingValue)
VALUES (1, 'AppConfig', '{"Theme": "Dark", "FontSize": 14}');
```

#### **2. LẤY GIÁ TRỊ TỪ JSON (DÙNG `JSON_VALUE`)**

```sql
SELECT
    SettingName,
    JSON_VALUE(SettingValue, '$.Theme') AS Theme,
    JSON_VALUE(SettingValue, '$.FontSize') AS FontSize
FROM Settings
WHERE SettingID = 1;
```

- **Giải thích:**
    - Lấy `SettingName`, `Theme`, `FontSize` từ JSON trong cột `SettingValue`.
    - `JSON_VALUE(SettingValue, '$.Theme')`: Lấy giá trị của key `Theme` trong JSON.
- **Kết quả:**

| SettingName | Theme | FontSize |
|-------------|-------|----------|
| AppConfig   | Dark  | 14       |

#### **3. LẤY MỘT PHẦN JSON (DÙNG `JSON_QUERY`)**

```sql
SELECT
  SettingName,
  JSON_QUERY(SettingValue, '$.items') AS Items
    FROM Settings
WHERE SettingID = 2;
```

- **Giải thích:**
    - Lấy `SettingName`, và phần `items` ở dạng JSON
- **Kết quả:**
  | SettingName | Items |
  |--------------|--------|
  | AppConfig2 | [{"product": "keyboard","quantity":1},{"product": "mouse","quantity":2},] |

#### **4. CHUYỂN JSON SANG DẠNG BẢNG (DÙNG `OPENJSON`)**

```sql
 SELECT value
 FROM OPENJSON('["a","b","c"]')
```

- **Giải thích:** Chuyển đổi JSON array thành dạng bảng.
- **Output:**

```
value
-----
a
b
c
```

```sql
SELECT Key, value
FROM OPENJSON('{"name":"John", "age": 30}')
```

- **Giải thích:** Chuyển đổi JSON object thành dạng bảng.
- **Output:**

```
Key      value
--------  ---
name      John
age       30
```

```sql
SELECT *
FROM OPENJSON(
    '
    [
        {"name":"John", "age": 30},
        {"name":"Alice", "age": 25}
    ]'
) WITH(name VARCHAR(10), age int);
```

- **Giải thích:** Chuyển đổi JSON array chứa các object thành dạng bảng với các cột tương ứng.
- **Output:**

| name  | age |
|-------|-----|
| John  | 30  |
| Alice | 25  |

#### **5. CHUYỂN KẾT QUẢ TRUY VẤN SANG JSON (DÙNG `FOR JSON AUTO`)**

```sql
    SELECT
      OrderID,
      OrderDate,
      CustomerID
        FROM Orders
     FOR JSON AUTO;
```

- **Giải thích:** Chuyển đổi kết quả truy vấn thành một chuỗi JSON.
- **Output:**

```
[{"OrderID":1,"OrderDate":"2024-01-10","CustomerID":1},{"OrderID":2,"OrderDate":"2024-01-15","CustomerID":2}]
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Kiểu JSON hợp lệ:** Chuỗi phải là JSON hợp lệ (nếu không sẽ bị lỗi).
- **`$` là root:** Dấu `$` là "gốc" của JSON (ví dụ: `'$.name'`, `'$.items[0]'`).
- **`OPENJSON` có `WITH` clause:** Để xác định kiểu dữ liệu của các cột khi chuyển đổi.
- **Performance:** Nếu JSON quá lớn hoặc phức tạp, truy vấn có thể chậm.
- **Kiểm tra lỗi:** Xử lý lỗi khi JSON không có các giá trị cần thiết.

### **VI. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Lưu cấu hình:** Lưu cấu hình ứng dụng (như setting, option,...).
- **Lưu dữ liệu linh hoạt:** Lưu các dữ liệu không có cấu trúc cố định (từ API, ...).
- **Trao đổi dữ liệu:** Trao đổi dữ liệu giữa các hệ thống dễ dàng.

### **VII. KẾT LUẬN (TỔNG KẾT)**

JSON trong SQL Server giúp bạn làm việc với dữ liệu không có cấu trúc một cách linh hoạt và hiệu quả. Hãy sử dụng các
hàm JSON để khai thác tối đa tiềm năng của dữ liệu dạng này. Chúc các bạn code thành công! 😎
