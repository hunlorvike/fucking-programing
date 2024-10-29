## Thuật toán Insertion Sort: Sắp xếp chèn

### Giới thiệu

Thuật toán Insertion Sort (hay còn gọi là sắp xếp chèn) là một thuật toán sắp xếp đơn giản, hoạt động dựa trên việc chèn từng phần tử vào đúng vị trí của nó trong phần đã sắp xếp của danh sách. Thuật toán này hoạt động tương tự như cách chúng ta sắp xếp bài trong tay: ta chọn từng lá bài và chèn nó vào đúng vị trí trong dãy các lá bài đã được sắp xếp trước đó.

### Cách hoạt động

1. **Chia danh sách:** Danh sách được chia thành hai phần: phần đã sắp xếp và phần chưa sắp xếp. Ban đầu, phần đã sắp xếp chỉ có phần tử đầu tiên, phần còn lại là chưa sắp xếp.

2. **Chọn phần tử:** Lấy phần tử đầu tiên từ phần chưa sắp xếp (gọi là `key`).

3. **So sánh và di chuyển:** So sánh `key` với các phần tử trong phần đã sắp xếp, từ phải sang trái. Nếu gặp phần tử lớn hơn `key`, di chuyển phần tử đó sang phải để tạo khoảng trống cho `key`.

4. **Chèn:** Chèn `key` vào vị trí chính xác trong phần đã sắp xếp.

5. **Lặp lại:** Bước 2 đến 4 được lặp lại cho đến khi tất cả các phần tử trong phần chưa sắp xếp được chèn vào phần đã sắp xếp.

### Mã giả của thuật toán Insertion Sort

```
insertion_sort(arr):
  n = length(arr)

  FOR i FROM 1 to n - 1:
    key = arr[i]
    j = i - 1
    WHILE j >= 0 AND arr[j] > key:
      arr[j + 1] = arr[j]
      j = j - 1
    arr[j + 1] = key
```

### Giải thích

- `i` là chỉ số của phần tử hiện tại được lấy ra từ phần chưa được sắp xếp để chèn vào phần đã sắp xếp. `i` sẽ tăng dần trong mỗi vòng lặp ngoài, và nó luôn cố định trong vòng lặp trong

- `j` là chỉ số của phần tử trong phần đã được sắp xếp mà ta đang so sánh với `key`. `j` sẽ giảm dần trong mỗi vòng lặp (while) để so sánh với `key` theo chiều từ phải -> trái

- n = length(arr): Lấy độ dài của mảng arr.

- for i from 1 to n - 1 do: Vòng lặp ngoài duyệt qua từng phần tử trong mảng (trừ phần tử đầu tiên).

- key = arr[i]: Lấy phần tử hiện tại (arr[i]) làm `key` để chèn.

- j = i - 1: Khởi tạo biến j là chỉ số của phần tử trước `key`.

- while j >= 0 and arr[j] > key do: Vòng lặp trong để so sánh `key` với các phần tử trong phần đã sắp xếp, từ phải sang trái.

- arr[j + 1] = arr[j]: Di chuyển phần tử hiện tại (arr[j]) sang vị trí tiếp theo (arr[j + 1]). (đi từ phải -> trái)

- j = j - 1: Giảm chỉ số j để tiếp tục so sánh với phần tử tiếp theo ở bên trái.

- arr[j + 1] = key: Chèn `key` vào vị trí chính xác trong phần đã sắp xếp.

### Ví dụ

Giả sử chúng ta có danh sách cần sắp xếp tăng dần: `12, 11, 13, 5, 6`

**Lần lặp 1:**

- i = 1
  - key = 11
  - j = 0: 12 > 11, arr[1] = 12, j = -1
  - arr[0] = 11: Chèn 11 vào đầu danh sách. Danh sách hiện tại: `11, 12, 13, 5, 6`

**Lần lặp 2:**

- i = 2
  - key = 13
  - j = 1: 12 <= 13, không cần di chuyển, chèn 13 vào vị trí hiện tại.
  - j = 0: 11 <= 13, không cần di chuyển, chèn 13 vào vị trí hiện tại. Danh sách hiện tại: `11, 12, 13, 5, 6`

**Lần lặp 3:**

- i = 3
  - key = 5
  - j = 2: 13 > 5, arr[3] = 13, j = 1
  - j = 1: 12 > 5, arr[2] = 12, j = 0
  - j = 0: 11 > 5, arr[1] = 11, j = -1
  - arr[0] = 5: Chèn 5 vào đầu danh sách. Danh sách hiện tại: `5, 11, 12, 13, 6`

**Lần lặp 4:**

- i = 4
  - key = 6
  - j = 3: 13 > 6, arr[4] = 13, j = 2
  - j = 2: 12 > 6, arr[3] = 12, j = 1
  - j = 1: 11 > 6, arr[2] = 11, j = 0
  - j = 0: 5 < 6, không cần di chuyển, chèn 6 vào vị trí sau 5. Danh sách hiện tại: `[5, 6, 11, 12, 13]`

**Kết quả:** Danh sách đã được sắp xếp: `[5, 6, 11, 12, 13]`

### Độ phức tạp

- **Độ phức tạp thời gian:** O(n²)
- **Độ phức tạp không gian:** O(1)

### Lưu ý

- **Chèn phần tử:** Thuật toán chèn từng phần tử vào đúng vị trí của nó trong phần đã sắp xếp của danh sách.

- **So sánh và di chuyển:** Phần tử được chèn sẽ được so sánh với các phần tử trong phần đã sắp xếp, từ phải sang trái. Nếu gặp phần tử lớn hơn, phần tử đó được di chuyển sang phải để tạo khoảng trống cho phần tử cần chèn.

- **Lặp lại:** Quá trình chèn và so sánh được lặp lại cho đến khi tất cả các phần tử được chèn vào phần đã sắp xếp.
