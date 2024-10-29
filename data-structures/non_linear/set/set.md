## Tập hợp (Set)

**Đặc điểm:**

- Là một cấu trúc dữ liệu phi tuyến tính, tức là các phần tử không được sắp xếp theo một thứ tự tuyến tính.
- Không cho phép phần tử trùng lặp, nghĩa là mỗi phần tử chỉ xuất hiện một lần trong tập hợp.
- Thường được sử dụng để thực hiện các thao tác trên tập hợp như:
  - **Hợp (Union):** Kết hợp các phần tử của hai tập hợp.
  - **Giao (Intersection):** Tìm các phần tử chung của hai tập hợp.
  - **Hiệu (Difference):** Tìm các phần tử chỉ có trong tập hợp đầu tiên mà không có trong tập hợp thứ hai.
  - **Kiểm tra thuộc tính (Membership):** Kiểm tra xem một phần tử có tồn tại trong tập hợp hay không.

**Ưu điểm:**

- **Thao tác tập hợp nhanh:** Các thao tác như hợp, giao, hiệu, kiểm tra thuộc tính thường có độ phức tạp thời gian rất nhanh (thường là O(1)).
- **Loại bỏ trùng lặp:** Tập hợp tự động loại bỏ các phần tử trùng lặp, giúp đảm bảo tính duy nhất của các phần tử trong tập hợp.

**Nhược điểm:**

- **Không có thứ tự:** Các phần tử trong tập hợp không có thứ tự hoặc chỉ mục rõ ràng, vì vậy bạn không thể truy cập đến một phần tử cụ thể bằng chỉ mục.
- **Khó duyệt:** Việc duyệt qua tất cả các phần tử trong tập hợp có thể tốn kém về hiệu suất.

**Ứng dụng:**

- **Lý thuyết tập hợp:** Tập hợp được sử dụng trong các bài toán liên quan đến lý thuyết tập hợp, chẳng hạn như:
  - Tìm giao của hai tập hợp các số.
  - Tìm hiệu của hai tập hợp các từ.
- **Loại bỏ trùng lặp:** Tập hợp được sử dụng để loại bỏ các phần tử trùng lặp trong danh sách, chẳng hạn như:
  - Loại bỏ các từ trùng lặp trong một văn bản.
  - Loại bỏ các địa chỉ email trùng lặp trong danh sách khách hàng.
- **Kiểm tra thuộc tính:** Tập hợp được sử dụng để kiểm tra xem một phần tử có tồn tại trong một tập hợp hay không, chẳng hạn như:
  - Kiểm tra xem một từ có tồn tại trong từ điển hay không.
  - Kiểm tra xem một người dùng có tồn tại trong cơ sở dữ liệu hay không.

**Ví dụ:**

```python
# Tạo một tập hợp
my_set = {1, 2, 3, 4, 5}

# Thêm một phần tử vào tập hợp
my_set.add(6)

# Kiểm tra thuộc tính
print(1 in my_set)  # Output: True
print(7 in my_set)  # Output: False

# Tạo một tập hợp khác
other_set = {4, 5, 6, 7, 8}

# Hợp của hai tập hợp
print(my_set | other_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Giao của hai tập hợp
print(my_set & other_set)  # Output: {4, 5, 6}

# Hiệu của hai tập hợp
print(my_set - other_set)  # Output: {1, 2, 3}
```

**Bổ sung:**

- Tập hợp là một cấu trúc dữ liệu rất hữu ích trong nhiều trường hợp, đặc biệt khi cần xử lý các thao tác trên tập hợp.
- Trong Python, tập hợp được triển khai bằng cấu trúc dữ liệu `set`, hỗ trợ các thao tác như `add`, `remove`, `union`, `intersection`, `difference`, `issubset`, `issuperset`, `isdisjoint`, v.v.
