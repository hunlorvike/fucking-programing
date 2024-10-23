## Thuật toán Selection Sort: Sắp xếp chọn

### Giới thiệu

Thuật toán Selection Sort (hay còn gọi là sắp xếp chọn) là một thuật toán sắp xếp đơn giản, hoạt động dựa trên việc tìm phần tử nhỏ nhất (hoặc lớn nhất) trong danh sách và hoán đổi nó với phần tử đầu tiên của danh sách. Quá trình này được lặp lại cho đến khi toàn bộ danh sách được sắp xếp.

### Cách hoạt động

1. **Tìm phần tử nhỏ nhất:** Thuật toán bắt đầu bằng việc duyệt qua danh sách và tìm phần tử nhỏ nhất.
2. **Hoán đổi:** Phần tử nhỏ nhất được hoán đổi với phần tử đầu tiên của danh sách.
3. **Lặp lại:** Bước 1 và 2 được lặp lại cho phần còn lại của danh sách, bắt đầu từ phần tử thứ hai, cho đến khi danh sách được sắp xếp hoàn toàn.

### Mã giả của thuật toán Selection Sort

```
selection_sort(arr):
  n = length(arr)

  FOR i FROM 0 to n - 1:
      min_index = i # Giả sử phần tử đầu tiên là nhỏ nhất
      FOR j FROM i + 1 to n - 1: # Duyệt phần chưa được sắp xếp
          IF arr[j] < arr[min_index]: # Tìm phần tử nhỏ hơn
            min_index = j # Cập nhật chỉ số phần tử nhỏ nhất

      IF min_index != i: # Nếu tìm thấy phần tử nhỏ hơn
          swap arr[i] AND arr[min_index] # Hoán đổi
```

### Giải thích

- n = length(arr): Lấy độ dài của mảng arr.

- for i from 0 to n - 1 do: Vòng lặp ngoài duyệt qua từng phần tử trong mảng (n lần).

- min_index = i: Khởi tạo biến min_index với giá trị i, giả sử phần tử đầu tiên là nhỏ nhất.

- for j from i + 1 to n - 1 do: Vòng lặp trong để tìm phần tử nhỏ nhất trong phần còn lại của mảng (trừ phần tử đầu).

- if arr[j] < arr[min_index] then min_index = j: So sánh phần tử hiện tại (arr[j]) với phần tử nhỏ nhất hiện tại (arr[min_index]). Nếu arr[j] nhỏ hơn, cập nhật min_index với j.

- if min_index != i then swap arr[i] and arr[min_index]: Nếu phần tử nhỏ nhất không phải là phần tử đầu tiên (min_index != i), hoán đổi hai phần tử.

### Ví dụ

Giả sử chúng ta có danh sách cần sắp xếp tăng dần: `64, 25, 12, 22, 11`

**Lần lặp 1:**

- i = 0
  - min_index = 0
  - j = 1: **25 < 64**, min_index = 1
  - j = 2: **12 < 25**, min_index = 2
  - j = 3: 22 < 12, min_index vẫn giữ là 2 (sai - không thay đổi)
  - j = 4: **11 < 12**, min_index = 4
  - Hoán đổi: `11, 25, 12, 22, 64`

**Lần lặp 2:**

- i = 1
  - min_index = 1
  - j = 2: **12 < 25**, min_index = 2
  - j = 3: 22 < 12, min_index vẫn giữ là 2 (sai - không thay đổi)
  - j = 4: 64 < 12, min_index vẫn giữ là 3 (sai - không thay đổi)
  - Hoán đổi: `11, 12, 25, 22, 64`

**Lần lặp 3:**

- i = 2
  - min_index = 2
  - j = 3: **22 < 25**, min_index = 3
  - j = 4: **64 < 22**, min_index vẫn giữ là 3 (sai - không thay đổi)
  - Hoán đổi: `11, 12, 22, 25, 64`

**Lần lặp 4:**

- i = 3
  - min_index = 3
  - j = 4: **64 < 25**, min_index vẫn giữ là 3 (sai - không thay đổi)
  - Hoán đổi: `11, 12, 22, 25, 64`

**Kết quả:** Danh sách đã được sắp xếp: `11, 12, 22, 25, 64`

### Độ phức tạp

- **Độ phức tạp thời gian:** O(n²)
- **Độ phức tạp không gian:** O(1)

### Lưu ý

- **Tìm phần tử nhỏ nhất (hoặc lớn nhất):** Thuật toán duyệt qua danh sách và tìm phần tử nhỏ nhất (hoặc lớn nhất) trong phần chưa được sắp xếp.

- **Hoán đổi vị trí:** Phần tử nhỏ nhất (hoặc lớn nhất) được hoán đổi vị trí với phần tử đầu tiên của phần chưa được sắp xếp.

- **Lặp lại:** Quá trình tìm và hoán đổi được lặp lại cho phần còn lại của danh sách, mỗi lần thu hẹp phần chưa được sắp xếp.
