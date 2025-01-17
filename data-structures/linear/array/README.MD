# Mảng (Array)

## Mục lục

1. [Đặc điểm](#Đặc-điểm)
2. [Ưu điểm](#Ưu-điểm)
3. [Nhược điểm](#Nhược-điểm)
4. [Ứng dụng](#Ứng-dụng)
5. [Ví dụ](#Ví-dụ)
6. [Bổ sung](#Bổ-sung)

---

## Đặc điểm

- **Tuyến tính**: Mảng là một cấu trúc dữ liệu tuyến tính, tức là các phần tử được sắp xếp theo một thứ tự liên tiếp.
- **Cùng kiểu dữ liệu**: Tất cả các phần tử trong mảng phải thuộc cùng một kiểu dữ liệu, ví dụ: tất cả là số nguyên hoặc
  tất cả là chuỗi.
- **Lưu trữ liên tiếp**: Các phần tử trong mảng được lưu trữ liên tiếp trong bộ nhớ, cho phép truy cập nhanh đến bất kỳ
  phần tử nào bằng chỉ số.
- **Truy cập bằng chỉ số**: Mỗi phần tử trong mảng có thể được truy cập thông qua chỉ số (index), bắt đầu từ 0 đối với
  hầu hết các ngôn ngữ lập trình.
- **Kích thước cố định**: Khi mảng được khai báo, kích thước của nó thường cố định và khó thay đổi sau đó, tức là không
  thể mở rộng hay thu nhỏ mà không cần tạo mảng mới.

## Ưu điểm

- **Truy cập nhanh**: Do các phần tử được lưu trữ liên tiếp trong bộ nhớ, nên việc truy cập vào phần tử bất kỳ bằng chỉ
  số có độ phức tạp thời gian là O(1), nghĩa là cực kỳ nhanh chóng.
- **Đơn giản**: Mảng là một trong những cấu trúc dữ liệu cơ bản và dễ hiểu nhất, phù hợp cho những tình huống cần lưu
  trữ tập hợp dữ liệu nhỏ hoặc cố định.

## Nhược điểm

- **Kích thước cố định**: Một nhược điểm lớn của mảng là kích thước của nó không thể thay đổi sau khi khai báo. Nếu cần
  thay đổi kích thước, bạn sẽ phải tạo mảng mới và sao chép dữ liệu, điều này có thể tốn tài nguyên.
- **Chèn và xóa phần tử chậm**: Khi chèn hoặc xóa phần tử ở giữa mảng, cần di chuyển tất cả các phần tử phía sau, khiến
  độ phức tạp thời gian của thao tác này là O(n), trong đó n là số lượng phần tử trong mảng.

## Ứng dụng

- **Lưu trữ dữ liệu**: Mảng thường được sử dụng để lưu trữ các danh sách tĩnh, chẳng hạn như danh sách học sinh, sản
  phẩm, hoặc điểm số.
- **Cấu trúc nền tảng**: Mảng là nền tảng để triển khai các cấu trúc dữ liệu khác như stack, queue, và hash table.
- **Thuật toán**: Mảng được sử dụng trong nhiều thuật toán, chẳng hạn như:
    - Thuật toán sắp xếp (Sorting Algorithms): Bubble Sort, Insertion Sort, Selection Sort.
    - Thuật toán tìm kiếm (Searching Algorithms): Linear Search, Binary Search.

## Ví dụ

```python
# Khai báo một mảng số nguyên
numbers = [1, 2, 3, 4, 5]

# Truy cập phần tử thứ 3 trong mảng
print(numbers[2])  # Output: 3

# Thay đổi giá trị của phần tử thứ 2
numbers[1] = 10

# In mảng
print(numbers)  # Output: [1, 10, 3, 4, 5]
```

## Bổ sung

- **Mảng đa chiều**: Ngoài mảng một chiều, còn có mảng đa chiều, chẳng hạn như mảng hai chiều (ma trận), được sử dụng để
  biểu diễn các cấu trúc phức tạp hơn như bảng, đồ thị, hoặc các phép tính toán học.

  ```python
  # Ví dụ về mảng hai chiều:
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]

  # Truy cập phần tử ở hàng thứ 2, cột thứ 3
  print(matrix[1][2])  # Output: 6
  ```

- **Dynamic Arrays (Mảng động)**: Một số ngôn ngữ như Python, JavaScript sử dụng mảng động (dynamic array), cho phép
  thay đổi kích thước tự động khi thêm hoặc xóa phần tử. Ví dụ, trong Python, list là một mảng động có thể thay đổi kích
  thước.
