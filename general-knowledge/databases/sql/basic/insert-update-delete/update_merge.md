# UPDATE MERGE trong SQL Server

## Mục Lục

1. [Tổng quan về câu lệnh UPDATE MERGE](#1-tổng-quan-về-câu-lệnh-update-merge)
   - [UPDATE MERGE là gì?](#update-merge-là-gì)
   - [Lợi ích của câu lệnh UPDATE MERGE](#lợi-ích-của-câu-lệnh-update-merge)
   - [Câu lệnh UPDATE MERGE hoạt động như thế nào?](#câu-lệnh-update-merge-hoạt-động-như-thế-nào)
2. [Cú pháp cơ bản của câu lệnh UPDATE MERGE](#2-cú-pháp-cơ-bản-của-câu-lệnh-update-merge)
   - [Cập nhật bản ghi khi có sự khớp dữ liệu](#cập-nhật-bản-ghi-khi-có-sự-khớp-dữ-liệu)
   - [Cập nhật bản ghi khi không có sự khớp dữ liệu](#cập-nhật-bản-ghi-khi-không-có-sự-khớp-dữ-liệu)
3. [Các tùy chọn mở rộng của câu lệnh UPDATE MERGE](#3-các-tùy-chọn-mở-rộng-của-câu-lệnh-update-merge)
   - [WHEN MATCHED](#when-matched)
   - [WHEN NOT MATCHED](#when-not-matched)
4. [Các ví dụ thực tế với UPDATE MERGE](#4-các-ví-dụ-thực-tế-với-update-merge)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về câu lệnh UPDATE MERGE

#### UPDATE MERGE là gì?

Câu lệnh `UPDATE MERGE` trong SQL Server là một cách để đồng bộ hóa dữ liệu giữa hai bảng. Câu lệnh này cho phép bạn kết hợp các bản ghi từ bảng nguồn vào bảng đích và thực hiện các thao tác cập nhật, chèn (INSERT), hoặc xóa (DELETE) tùy thuộc vào sự khớp dữ liệu giữa các bảng. `UPDATE MERGE` chủ yếu được sử dụng khi bạn cần cập nhật bảng đích dựa trên các thay đổi trong bảng nguồn.

#### Lợi ích của câu lệnh UPDATE MERGE

- **Đồng bộ hóa dữ liệu**: Giúp bạn dễ dàng đồng bộ hóa bảng nguồn và bảng đích, thực hiện các thao tác cập nhật hoặc thêm mới mà không cần nhiều câu lệnh riêng biệt.
- **Cải thiện hiệu suất**: Thay vì sử dụng nhiều câu lệnh `UPDATE`, `INSERT`, và `DELETE` riêng biệt, `UPDATE MERGE` giúp hợp nhất tất cả các thao tác này vào một câu lệnh duy nhất.
- **Tính linh hoạt cao**: Có thể áp dụng các điều kiện khác nhau cho từng loại thao tác (cập nhật, thêm mới, xóa) tùy vào sự khớp dữ liệu.

#### Câu lệnh UPDATE MERGE hoạt động như thế nào?

Câu lệnh `UPDATE MERGE` thực hiện các thao tác sau:

1. **Xác định sự khớp**: SQL Server sẽ tìm kiếm các bản ghi khớp giữa bảng nguồn và bảng đích dựa trên điều kiện `ON`.
2. **Cập nhật dữ liệu (WHEN MATCHED)**: Nếu một bản ghi trong bảng đích khớp với một bản ghi trong bảng nguồn, câu lệnh sẽ thực hiện các thao tác cập nhật.
3. **Thêm mới dữ liệu (WHEN NOT MATCHED)**: Nếu không có sự khớp, bạn có thể chọn thêm bản ghi mới vào bảng đích.
4. **Xóa dữ liệu (WHEN MATCHED AND DELETE)**: Bạn cũng có thể chỉ định xóa các bản ghi trong bảng đích nếu không còn khớp với các bản ghi trong bảng nguồn.

---

### 2. Cú pháp cơ bản của câu lệnh UPDATE MERGE

#### Cập nhật bản ghi khi có sự khớp dữ liệu

Khi có sự khớp dữ liệu giữa bảng đích và bảng nguồn, bạn có thể thực hiện các thao tác cập nhật với dữ liệu trong bảng đích.

**Cú pháp**:

```sql
MERGE INTO target_table AS target
USING source_table AS source
ON target.column = source.column
WHEN MATCHED THEN
    UPDATE SET target.column1 = source.column1, target.column2 = source.column2;
```

**Ví dụ**:

```sql
MERGE INTO employees AS target
USING temp_employees AS source
ON target.employee_id = source.employee_id
WHEN MATCHED THEN
    UPDATE SET target.salary = source.salary;
```

Trong ví dụ trên, nếu có sự khớp giữa `employee_id` của bảng `employees` và bảng `temp_employees`, lương của nhân viên trong bảng `employees` sẽ được cập nhật theo giá trị trong bảng `temp_employees`.

#### Cập nhật bản ghi khi không có sự khớp dữ liệu

Khi không có sự khớp, bạn có thể quyết định hành động khác như thêm mới bản ghi hoặc giữ nguyên.

**Cú pháp**:

```sql
MERGE INTO target_table AS target
USING source_table AS source
ON target.column = source.column
WHEN NOT MATCHED THEN
    INSERT (column1, column2) VALUES (source.column1, source.column2);
```

**Ví dụ**:

```sql
MERGE INTO employees AS target
USING new_employees AS source
ON target.employee_id = source.employee_id
WHEN NOT MATCHED THEN
    INSERT (employee_id, first_name, last_name, salary)
    VALUES (source.employee_id, source.first_name, source.last_name, source.salary);
```

Ví dụ này sẽ thêm các bản ghi mới từ bảng `new_employees` vào bảng `employees` nếu không tìm thấy sự khớp theo `employee_id`.

---

### 3. Các tùy chọn mở rộng của câu lệnh UPDATE MERGE

#### WHEN MATCHED

`WHEN MATCHED` được sử dụng để xác định hành động khi có sự khớp dữ liệu giữa bảng đích và bảng nguồn. Bạn có thể thực hiện các thao tác như `UPDATE` hoặc `DELETE` đối với các bản ghi khớp.

**Cú pháp**:

```sql
WHEN MATCHED THEN
    UPDATE SET column1 = value1, column2 = value2;
```

Hoặc nếu muốn xóa các bản ghi khớp:

```sql
WHEN MATCHED AND condition THEN
    DELETE;
```

**Ví dụ**:

```sql
MERGE INTO employees AS target
USING temp_employees AS source
ON target.employee_id = source.employee_id
WHEN MATCHED THEN
    UPDATE SET target.salary = source.salary;
```

#### WHEN NOT MATCHED

`WHEN NOT MATCHED` sẽ thực hiện thao tác khi không có sự khớp giữa các bản ghi trong bảng đích và bảng nguồn. Thường sử dụng để thêm mới bản ghi.

**Cú pháp**:

```sql
WHEN NOT MATCHED THEN
    INSERT (column1, column2)
    VALUES (value1, value2);
```

**Ví dụ**:

```sql
MERGE INTO employees AS target
USING new_employees AS source
ON target.employee_id = source.employee_id
WHEN NOT MATCHED THEN
    INSERT (employee_id, first_name, last_name, salary)
    VALUES (source.employee_id, source.first_name, source.last_name, source.salary);
```

---

### 4. Các ví dụ thực tế với UPDATE MERGE

#### Cập nhật lương của nhân viên từ bảng nguồn

**Câu lệnh SQL**:

```sql
MERGE INTO employees AS target
USING temp_employees AS source
ON target.employee_id = source.employee_id
WHEN MATCHED THEN
    UPDATE SET target.salary = source.salary;
```

**Giải thích**:

- Cập nhật lương của các nhân viên trong bảng `employees` từ bảng `temp_employees` nếu có sự khớp về `employee_id`.

---

#### Thêm mới nhân viên vào bảng nếu không có sự khớp

**Câu lệnh SQL**:

```sql
MERGE INTO employees AS target
USING new_employees AS source
ON target.employee_id = source.employee_id
WHEN NOT MATCHED THEN
    INSERT (employee_id, first_name, last_name, salary)
    VALUES (source.employee_id, source.first_name, source.last_name, source.salary);
```

**Giải thích**:

- Nếu không có sự khớp về `employee_id`, các bản ghi từ bảng `new_employees` sẽ được thêm mới vào bảng `employees`.

---

#### Xóa nhân viên khỏi bảng nếu không có sự khớp

**Câu lệnh SQL**:

```sql
MERGE INTO employees AS target
USING temp_employees AS source
ON target.employee_id = source.employee_id
WHEN MATCHED AND source.status = 'Inactive' THEN
    DELETE;
```

**Giải thích**:

- Nếu một nhân viên trong bảng `employees` có `employee_id` khớp với bảng `temp_employees` và có trạng thái là `'Inactive'`, bản ghi đó sẽ bị xóa khỏi bảng `employees`.

---

### 5. Lưu ý và thực hành tốt

- **Kiểm tra sự khớp dữ liệu**: Trước khi thực thi câu lệnh `UPDATE MERGE`, luôn đảm bảo rằng điều kiện `ON` chính xác để tránh việc cập

nhật sai dữ liệu.

- **Sử dụng giao dịch (Transactions)**: Khi thực hiện các thao tác quan trọng, sử dụng giao dịch để đảm bảo tính toàn vẹn của dữ liệu và khả năng khôi phục khi cần thiết.
- **Hiệu suất**: Việc sử dụng `MERGE` để đồng bộ hóa dữ liệu có thể ảnh hưởng đến hiệu suất nếu bảng quá lớn. Hãy kiểm tra và tối ưu hóa khi cần.
- **Thử nghiệm trên môi trường phát triển**: Trước khi áp dụng câu lệnh `UPDATE MERGE` trên môi trường sản xuất, hãy thử nghiệm trên môi trường phát triển để đảm bảo rằng không có thay đổi không mong muốn.
