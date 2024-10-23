## Thuật toán Bubble Sort: Sắp xếp nổi bọt

### Giới thiệu

Thuật toán Bubble Sort (hay còn gọi là sắp xếp nổi bọt) là một thuật toán sắp xếp đơn giản dựa trên việc so sánh cặp các phần tử liền kề và hoán đổi chúng nếu chúng không theo đúng thứ tự (lớn hơn hoặc nhỏ hơn tùy thuộc vào thứ tự cần sắp xếp). Quá trình này được lặp lại cho đến khi không còn sự hoán đổi nào xảy ra, khi đó dãy đã được sắp xếp.

### Cách hoạt động

1. **Duyệt qua danh sách:** Thuật toán bắt đầu bằng việc duyệt qua danh sách từ đầu đến cuối.
2. **So sánh cặp phần tử:** Tại mỗi bước, thuật toán so sánh hai phần tử liền kề.
3. **Hoán đổi:** Nếu hai phần tử không theo thứ tự mong muốn (ví dụ, nếu cần sắp xếp tăng dần và phần tử trước lớn hơn phần tử sau), chúng sẽ được hoán đổi.
4. **Lặp lại:** Quá trình duyệt, so sánh và hoán đổi được lặp lại cho đến khi không còn sự hoán đổi nào xảy ra, nghĩa là danh sách đã được sắp xếp.

### Mã giả của thuật toán Bubble Sort

```
bubble_sort(arr):
  n = length(arr)

  FOR i FROM 0 to n-1:
      swapped = false
      FOR j FROM 0 to n-i-1:
          IF arr[j] > arr[j+1]: # Hoán đổi nếu phần tử trước lớn hơn phần tử sau
              swap arr[j] AND arr[j+1]
              swapped = true
      IF not swapped:
        break;
```

### Giải thích

- **n = length(arr):** Lấy độ dài của mảng arr.

- **FOR i FROM 0 to n-1:** Vòng lặp ngoài duyệt qua từng phần tử trong mảng (n lần).

- **swapped = false:** Đặt biến swapped để theo dõi việc hoán đổi. Nếu không có phần tử nào được hoán đổi trong vòng lặp, điều đó có nghĩa là mảng đã được sắp xếp và ta có thể dừng sớm.

- **FOR j FROM 0 to n-i-1:** Vòng lặp trong để so sánh và hoán đổi các phần tử liền kề. Duyệt từ phần tử đầu đến phần tử thứ n-i-1 vì sau mỗi lần duyệt, phần tử lớn nhất (hoặc nhỏ nhất) sẽ "nổi" lên vị trí cuối cùng, không cần kiểm tra lại.

- **IF arr[j] > arr[j+1]:** So sánh hai phần tử liền kề. Nếu phần tử trước lớn hơn phần tử sau, chúng sẽ bị hoán đổi.

- **swap arr[j] AND arr[j+1]:** Hoán đổi hai phần tử.

- **swapped = true:** Đặt cờ swapped thành true để báo hiệu đã có hoán đổi.

- **IF not swapped:** Nếu không có hoán đổi nào diễn ra trong vòng lặp hiện tại, điều đó có nghĩa là mảng đã được sắp xếp hoàn toàn, và vòng lặp ngoài sẽ dừng sớm.

### Ví dụ

Giả sử chúng ta có danh sách cần sắp xếp tăng dần: `5, 1, 4, 2, 8`

**Lần lặp 1:**

- i = 0
  - j = 0: 5 > 1, hoán đổi -> [1, 5, 4, 2, 8]
  - j = 1: 5 > 4, hoán đổi -> [1, 4, 5, 2, 8]
  - j = 2: 5 > 2, hoán đổi -> [1, 4, 2, 5, 8]
  - j = 3: 5 > 8, không hoán đổi -> [1, 4, 2, 5, 8]

**Lần lặp 2:**

- i = 1
  - j = 0: 1 > 4, không hoán đổi -> [1, 4, 2, 5, 8]
  - j = 1: 4 > 2, hoán đổi -> [1, 2, 4, 5, 8]
  - j = 2: 4 > 5, không hoán đổi -> [1, 2, 4, 5, 8]

**Lần lặp 3:**

- i = 2
  - j = 0: 1 > 2, không hoán đổi -> [1, 2, 4, 5, 8]
  - j = 1: 2 > 4, không hoán đổi -> [1, 2, 4, 5, 8]

**Lần lặp 4:**

- i = 3
  - j = 0: 1 > 2, không hoán đổi -> [1, 2, 4, 5, 8]

**Kết quả:** Danh sách đã được sắp xếp: `1, 2, 4, 5, 8`

### Độ phức tạp

- **Độ phức tạp thời gian:**
  - Trường hợp xấu nhất: O(n²), khi mảng ngược chiều.
  - Trường hợp tốt nhất: O(n), khi mảng đã được sắp xếp (với tối ưu dừng sớm).
- **Độ phức tạp không gian:** O(1)

### Cải tiến

- **Cờ hoán đổi:** Thêm một cờ để kiểm tra xem có sự hoán đổi nào trong vòng lặp hay không. Nếu không có sự hoán đổi, danh sách đã được sắp xếp và có thể dừng thuật toán.
- **Sắp xếp một phần:** Chỉ duyệt qua phần chưa được sắp xếp của danh sách trong mỗi vòng lặp.

### Lưu ý

- Trong mỗi lần lặp của vòng lặp ngoài (i), thuật toán sẽ duyệt qua các phần tử liền kề và hoán đổi chúng nếu chúng không theo thứ tự mong muốn. Điều này sẽ khiến phần tử lớn nhất (hoặc nhỏ nhất) "nổi" lên vị trí cuối cùng của mảng.

- Sau khi phần tử lớn nhất (hoặc nhỏ nhất) đã ở đúng vị trí, thuật toán sẽ không cần kiểm tra lại phần tử đó nữa trong các lần lặp tiếp theo. Vòng lặp trong (j) được tối ưu hóa để chỉ duyệt qua phần còn lại của mảng, loại trừ phần tử đã được sắp xếp.

- Ví dụ: nếu bạn cần sắp xếp danh sách tăng dần, sau lần lặp đầu tiên, phần tử lớn nhất sẽ được đẩy xuống cuối mảng. Trong lần lặp thứ hai, bạn không cần kiểm tra phần tử ở cuối mảng nữa vì nó đã được sắp xếp.

- Cơ chế này giúp thuật toán Bubble Sort hiệu quả hơn, đặc biệt là khi danh sách đã sắp xếp gần như hoàn toàn.