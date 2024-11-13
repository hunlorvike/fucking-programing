Trong SQL, `WHERE` và `HAVING` đều được sử dụng để lọc dữ liệu, nhưng chúng có sự khác biệt quan trọng về cách thức hoạt động và mục đích sử dụng:

### 1. **WHERE**

- **Định nghĩa**: `WHERE` là mệnh đề lọc dữ liệu _trước khi_ nhóm (nếu có) và áp dụng lên từng bản ghi trong bảng. Nó chỉ lọc các bản ghi mà không liên quan đến các hàm tổng hợp.
- **Ứng dụng**: `WHERE` được sử dụng để lọc dữ liệu trong các truy vấn không sử dụng `GROUP BY` hoặc lọc dữ liệu trước khi nhóm.
- **Lọc dữ liệu**: Lọc _các bản ghi đơn lẻ_ từ bảng dựa trên điều kiện bạn chỉ định.

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'HR';
```

Trong ví dụ này, `WHERE` lọc các nhân viên thuộc phòng ban 'HR' trước khi bất kỳ nhóm hay tính toán nào được thực hiện.

### 2. **HAVING**

- **Định nghĩa**: `HAVING` được sử dụng để lọc dữ liệu _sau khi_ dữ liệu đã được nhóm lại bởi mệnh đề `GROUP BY`. Nó cho phép lọc các nhóm dữ liệu, điều này đặc biệt hữu ích khi sử dụng các hàm tổng hợp như `COUNT()`, `SUM()`, `AVG()`, v.v.
- **Ứng dụng**: `HAVING` được dùng khi bạn muốn lọc các nhóm dữ liệu dựa trên các kết quả tổng hợp hoặc khi dữ liệu đã được nhóm lại.
- **Lọc dữ liệu**: Lọc _các nhóm_ dữ liệu sau khi nhóm theo `GROUP BY`.

**Ví dụ**:

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

Truy vấn này nhóm các nhân viên theo phòng ban và lọc các phòng ban có số lượng nhân viên lớn hơn 5.

### Sự khác biệt chính:

1. **Mục đích**:
   - `WHERE` lọc dữ liệu trước khi nhóm.
   - `HAVING` lọc dữ liệu sau khi nhóm.
2. **Sử dụng với các hàm tổng hợp**:

   - `WHERE` không thể sử dụng với các hàm tổng hợp (ví dụ: `COUNT()`, `SUM()`).
   - `HAVING` có thể sử dụng với các hàm tổng hợp để lọc kết quả tính toán.

3. **Thứ tự thực thi**:
   - `WHERE` được thực thi trước `GROUP BY`.
   - `HAVING` được thực thi sau `GROUP BY`.

### Ví dụ về sự kết hợp của cả hai:

```sql
SELECT department, COUNT(*), AVG(salary)
FROM employees
WHERE salary > 3000
GROUP BY department
HAVING COUNT(*) > 5 AND AVG(salary) > 5000;
```

Truy vấn này lọc các nhân viên có lương trên 3000 trước khi nhóm, sau đó nhóm các nhân viên theo phòng ban và chỉ trả về các phòng ban có số lượng nhân viên lớn hơn 5 và mức lương trung bình trên 5000.

### Kết luận:

- **WHERE**: Sử dụng khi bạn muốn lọc dữ liệu trước khi nhóm hoặc khi không sử dụng `GROUP BY`.
- **HAVING**: Sử dụng khi bạn muốn lọc các nhóm dữ liệu đã được nhóm lại, đặc biệt khi có các hàm tổng hợp.
