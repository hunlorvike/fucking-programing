## Bảng băm (Hash Table)

**Khái niệm:**

Bảng băm (Hash Table) là một cấu trúc dữ liệu sử dụng hàm băm (hash function) để ánh xạ dữ liệu sang các vị trí bộ nhớ. Dữ liệu được lưu trữ dưới dạng cặp khóa-giá trị (key-value pairs).

**Cách thức hoạt động:**

1. **Hàm băm:** Hàm băm nhận một khóa (key) bất kỳ và trả về một giá trị số nguyên (hash value), đại diện cho vị trí trong bảng băm mà khóa đó sẽ được lưu trữ.
2. **Xung đột (Collision):** Khi hai khóa khác nhau được ánh xạ đến cùng một vị trí trong bảng băm, xảy ra xung đột. Các phương pháp giải quyết xung đột phổ biến gồm:
   - **Chaining (Liên kết):** Lưu trữ các khóa cùng hash value vào một danh sách liên kết tại vị trí đó.
   - **Open addressing (Địa chỉ mở):** Tìm kiếm các vị trí tiếp theo trong bảng băm cho đến khi tìm được vị trí trống.

**Ưu điểm:**

- **Truy cập rất nhanh:** Tìm kiếm, chèn và xóa các phần tử trong bảng băm thường có độ phức tạp trung bình là O(1), rất nhanh.
- **Phù hợp với các thao tác truy cập ngẫu nhiên:** Bảng băm hiệu quả cho các thao tác truy cập ngẫu nhiên như tìm kiếm, chèn và xóa.

**Nhược điểm:**

- **Xung đột:** Xung đột có thể làm giảm hiệu suất của bảng băm.
- **Không phù hợp với duyệt tuần tự:** Bảng băm không hỗ trợ duyệt các phần tử theo thứ tự.

**Ví dụ:**

**Bài toán lưu trữ thông tin người dùng:**

Giả sử bạn muốn lưu trữ thông tin người dùng, mỗi người dùng được xác định bởi một ID duy nhất. Bạn có thể sử dụng bảng băm để lưu trữ thông tin này:

- **Key:** ID của người dùng.
- **Value:** Thông tin về người dùng (tên, tuổi, địa chỉ...).

**Triển khai Bảng băm trong Python:**

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def __hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.__hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def get(self, key):
        index = self.__hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.__hash(key)
        if self.table[index] is not None:
            original_size = len(self.table[index])
            self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
            if len(self.table[index]) < original_size:
                return True
        return False

# Ví dụ sử dụng
hash_table = HashTable(10)
hash_table.put("name", "John")
hash_table.put("age", 30)

print(hash_table.get("name"))  # Output: John
print(hash_table.get("age"))  # Output: 30

hash_table.delete("name")
print(hash_table.get("name"))  # Output: None
```

**Ứng dụng của Bảng băm:**

- **Tìm kiếm nhanh các phần tử:** Bảng băm được sử dụng trong các thuật toán tìm kiếm nhanh chóng, ví dụ: tìm kiếm từ trong văn bản, tìm kiếm key trong một tập dữ liệu lớn.
- **Bảng tra cứu:** Bảng băm được sử dụng để xây dựng bảng tra cứu (lookup table) cho các dữ liệu được truy cập thường xuyên, ví dụ: bảng mã hóa, bảng giá trị.
- **Bộ nhớ cache:** Bảng băm được sử dụng để quản lý bộ nhớ cache (cache) cho các dữ liệu thường được truy cập, giúp tăng tốc độ truy xuất.

**Kết luận:**

Bảng băm là một cấu trúc dữ liệu hiệu quả và được sử dụng rộng rãi trong các ứng dụng cần tìm kiếm nhanh chóng. Nó cung cấp khả năng truy cập ngẫu nhiên với độ phức tạp trung bình là O(1), phù hợp với các thao tác như tìm kiếm, chèn và xóa.
