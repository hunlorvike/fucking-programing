# View trong SQL Server

## Mục Lục

1. [Tổng quan về View](#1-tổng-quan-về-view)
   - [View là gì?](#view-là-gì)
   - [Lợi ích và ứng dụng của View](#lợi-ích-và-ứng-dụng-của-view)
   - [Cách hoạt động của View](#cách-hoạt-động-của-view)
2. [Cú pháp và cách sử dụng View](#2-cú-pháp-và-cách-sử-dụng-view)
   - [Tạo View](#tạo-view)
   - [Sử dụng View trong SELECT](#sử-dụng-view-trong-select)
   - [Cập nhật, Xoá, và Thêm dữ liệu với View](#cập-nhật-xoá-và-thêm-dữ-liệu-với-view)
   - [Xem danh sách các View](#xem-danh-sách-các-view)
3. [Các loại View](#3-các-loại-view)
   - [View đơn giản](#view-đơn-giản)
   - [View phức tạp](#view-phức-tạp)
   - [View cập nhật được và không cập nhật được](#view-cập-nhật-được-và-không-cập-nhật-được)
4. [Kết hợp với các mệnh đề khác](#4-kết-hợp-với-các-mệnh-đề-khác)
   - [View với JOIN](#view-với-join)
   - [View với GROUP BY](#view-với-group-by)
   - [View với UNION](#view-với-union)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về View

#### View là gì?

**View** trong SQL Server là một đối tượng cơ sở dữ liệu, thực chất là một câu lệnh SELECT đã được lưu trữ, cho phép bạn tái sử dụng các truy vấn phức tạp mà không cần phải lặp lại mã nguồn. View không lưu trữ dữ liệu mà chỉ lưu trữ câu lệnh truy vấn SQL, khi người dùng truy cập vào View, SQL Server sẽ thực thi câu lệnh đó và trả về kết quả tương ứng. Có thể hiểu View như một alias cho một câu SELECT trong SQL

Ví dụ, một view có thể kết hợp nhiều bảng, thực hiện tính toán hoặc lọc dữ liệu trước khi người dùng truy vấn, giúp đơn giản hóa việc quản lý và truy xuất dữ liệu.

#### Lợi ích và ứng dụng của View

- **Đơn giản hóa truy vấn**: View cho phép bạn tạo ra các truy vấn phức tạp mà không cần phải lặp lại nhiều lần, giúp mã nguồn dễ hiểu và dễ bảo trì.
- **Tăng cường bảo mật**: Bạn có thể tạo view để hạn chế quyền truy cập vào các cột và bảng cụ thể, chỉ cho phép người dùng truy cập dữ liệu cần thiết.
- **Tái sử dụng mã nguồn**: Thay vì phải viết lại các truy vấn giống nhau, bạn chỉ cần viết một lần trong View và sử dụng lại khi cần.
- **Hỗ trợ tính toàn vẹn dữ liệu**: View giúp hiển thị dữ liệu từ nhiều bảng, giúp bạn quản lý dữ liệu một cách hiệu quả hơn.

#### Cách hoạt động của View

View hoạt động như một bảng ảo. Khi một View được truy vấn, SQL Server sẽ tự động thực thi câu lệnh SELECT trong View và trả về kết quả. Do View chỉ lưu trữ câu lệnh truy vấn, nó không làm ảnh hưởng đến dữ liệu gốc trong các bảng.

- **Không lưu trữ dữ liệu**: View không lưu trữ dữ liệu thực tế mà chỉ lưu trữ câu lệnh SQL.
- **Tự động cập nhật**: Khi bạn cập nhật dữ liệu trong bảng, các thay đổi sẽ tự động phản ánh trong View khi truy vấn lại.
- **Có thể sử dụng trong các câu lệnh khác**: View có thể được sử dụng trong câu lệnh SELECT, JOIN, WHERE như một bảng bình thường.

---

### 2. Cú pháp và cách sử dụng View

#### Tạo View

Để tạo một View, bạn sử dụng câu lệnh `CREATE VIEW`. Cú pháp cơ bản như sau:

```sql
CREATE VIEW <view_name> AS
SELECT <columns>
FROM <tables>
WHERE <conditions>;
```

**Ví dụ**:

```sql
CREATE VIEW EmployeeView AS
SELECT employee_id, name, department_id, salary
FROM employees
WHERE salary > 5000;
```

Câu lệnh trên tạo một View có tên `EmployeeView` để hiển thị thông tin của các nhân viên có mức lương lớn hơn 5000.

#### Sử dụng View trong SELECT

Bạn có thể truy vấn từ View giống như khi truy vấn từ bảng.

**Ví dụ**:

```sql
SELECT * FROM EmployeeView;
```

Kết quả sẽ trả về danh sách tất cả nhân viên có lương lớn hơn 5000, như đã định nghĩa trong View.

#### Cập nhật, Xoá, và Thêm dữ liệu với View

Mặc dù View không lưu trữ dữ liệu thực tế, bạn vẫn có thể cập nhật, thêm hoặc xóa dữ liệu thông qua View, nếu View đáp ứng một số điều kiện.

- **Cập nhật dữ liệu**: Nếu View đơn giản (không sử dụng các phép toán như `JOIN`, `GROUP BY`, `DISTINCT`), bạn có thể cập nhật dữ liệu thông qua View.

  ```sql
  UPDATE EmployeeView
  SET salary = 6000
  WHERE employee_id = 1;
  ```

- **Thêm dữ liệu**: Bạn có thể thêm dữ liệu vào bảng thông qua View nếu View không thay đổi cấu trúc của bảng.

  ```sql
  INSERT INTO EmployeeView (employee_id, name, department_id, salary)
  VALUES (4, 'David', 2, 7000);
  ```

- **Xóa dữ liệu**: Bạn cũng có thể xóa dữ liệu thông qua View nếu View không phức tạp.

  ```sql
  DELETE FROM EmployeeView
  WHERE employee_id = 3;
  ```

#### Xem danh sách các View

Để xem danh sách các View trong cơ sở dữ liệu, bạn có thể truy vấn bảng hệ thống `INFORMATION_SCHEMA.VIEWS`.

```sql
SELECT * FROM INFORMATION_SCHEMA.VIEWS;
```

---

### 3. Các loại View

#### View đơn giản

View đơn giản chỉ bao gồm một câu lệnh SELECT mà không sử dụng các phép toán phức tạp. Những View này thường dễ dàng cập nhật, thêm và xóa dữ liệu.

**Ví dụ**:

```sql
CREATE VIEW SimpleView AS
SELECT employee_id, name
FROM employees;
```

#### View phức tạp

View phức tạp có thể bao gồm các phép toán như `JOIN`, `GROUP BY`, `HAVING`, `DISTINCT`, v.v. Những View này có thể không hỗ trợ cập nhật, xóa hoặc thêm dữ liệu trực tiếp.

**Ví dụ**:

```sql
CREATE VIEW ComplexView AS
SELECT e.name, d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 5000;
```

#### View cập nhật được và không cập nhật được

- **View cập nhật được**: Những View đơn giản có thể cập nhật, xóa hoặc thêm dữ liệu trực tiếp. View này không chứa các phép toán phức tạp hoặc các truy vấn con.
- **View không cập nhật được**: Nếu View sử dụng các phép toán phức tạp như `GROUP BY`, `JOIN`, `DISTINCT`, bạn không thể cập nhật dữ liệu trực tiếp thông qua View.

---

### 4. Kết hợp với các mệnh đề khác

#### View với JOIN

Bạn có thể kết hợp View với `JOIN` để hiển thị dữ liệu từ nhiều bảng.

**Ví dụ**:

```sql
CREATE VIEW EmployeeDepartmentView AS
SELECT e.name, e.salary, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```

#### View với GROUP BY

View có thể sử dụng `GROUP BY` để nhóm dữ liệu và thực hiện các phép tính như `SUM()`, `AVG()`, v.v.

**Ví dụ**:

```sql
CREATE VIEW DepartmentSalaryAvg AS
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;
```

#### View với UNION

Bạn có thể sử dụng `UNION` trong View để kết hợp kết quả từ nhiều truy vấn SELECT khác nhau.

**Ví dụ**:

```sql
CREATE VIEW AllEmployees AS
SELECT name, salary FROM employees
UNION
SELECT name, salary FROM contractors;
```

---

### 5. Lưu ý và thực hành tốt

- **Hiệu suất**: Mặc dù View giúp đơn giản hóa các truy vấn, nhưng nếu View chứa quá nhiều phép toán phức tạp, nó có thể ảnh hưởng đến hiệu suất. Cần tối ưu hóa các câu lệnh trong View.
- **Cập nhật và bảo trì**: View có thể giúp tái sử dụng mã nguồn, nhưng bạn cần lưu ý rằng những View phức tạp có thể khó bảo trì và làm tăng độ phức tạp của hệ thống.
- **Sử dụng đúng loại View**: Nên sử dụng View đơn giản khi cần cập nhật dữ liệu dễ dàng và sử dụng View phức tạp

 khi cần xử lý dữ liệu với các phép toán phức tạp.

---

### Tổng kết

View trong SQL Server là một công cụ mạnh mẽ giúp bạn đơn giản hóa các truy vấn phức tạp, tái sử dụng mã nguồn, và tăng cường bảo mật trong cơ sở dữ liệu. Tuy nhiên, việc sử dụng View cần phải cân nhắc kỹ lưỡng, đặc biệt khi View phức tạp, để tránh ảnh hưởng đến hiệu suất và bảo trì mã nguồn.