# Thuật Toán Tìm Kiếm Fibonacci (Fibonacci Search)

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Fibonacci Search](#mã-giả-của-thuật-toán-fibonacci-search)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán tìm kiếm Fibonacci (Fibonacci Search) là một thuật toán tìm kiếm hiệu quả được sử dụng để tìm một phần tử cụ
thể trong một danh sách đã được sắp xếp. Nó dựa trên chuỗi Fibonacci, một chuỗi số trong đó mỗi số là tổng của hai số
trước đó (ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21...).

## Cách hoạt động

1. **Khởi tạo:** Thuật toán bắt đầu bằng việc tạo ra một chuỗi Fibonacci có kích thước đủ lớn để bao phủ danh sách.
2. **Tìm vị trí chia:** Thuật toán tìm vị trí chia (offset) trong danh sách, được xác định bởi số Fibonacci gần nhất
   nhưng nhỏ hơn số lượng phần tử trong danh sách.
3. **So sánh:** Thuật toán so sánh phần tử cần tìm với phần tử ở vị trí chia.
    - Nếu phần tử cần tìm bằng với phần tử ở vị trí chia, thuật toán đã tìm thấy phần tử.
    - Nếu phần tử cần tìm nhỏ hơn phần tử ở vị trí chia, thuật toán sẽ tiếp tục tìm kiếm trong nửa trái của danh sách (
      từ đầu danh sách đến vị trí chia).
    - Nếu phần tử cần tìm lớn hơn phần tử ở vị trí chia, thuật toán sẽ tiếp tục tìm kiếm trong nửa phải của danh sách (
      từ vị trí chia đến cuối danh sách).
4. **Lặp lại:** Thuật toán lặp lại bước 2 và 3 trên nửa danh sách được chọn cho đến khi tìm thấy phần tử cần tìm hoặc
   không còn phần tử nào để kiểm tra.

## Mã giả của thuật toán Fibonacci Search

```
fibonacci_search(arr, target):
  n = length(arr)

  # Tạo chuỗi Fibonacci
  fibM_minus_2 = 0
  fibM_minus_1 = 1
  fibM = fibM_minus_1 + fibM_minus_2

  while fibM < n:
    fibM_minus_2 = fibM_minus_1
    fibM_minus_1 = fibM
    fibM = fibM_minus_1 + fibM_minus_2

  # Tìm vị trí chia
  offset = -1

  while fibM > 1:
    i = min(offset + fibM_minus_2, n - 1)

    # So sánh phần tử ở vị trí chia với giá trị cần tìm
    if arr[i] < target:
      fibM = fibM_minus_1
      fibM_minus_1 = fibM_minus_2
      fibM_minus_2 = fibM - fibM_minus_1
      offset = i
    elif arr[i] > target:
      fibM = fibM_minus_2
      fibM_minus_1 = fibM_minus_1 - fibM_minus_2
      fibM_minus_2 = fibM - fibM_minus_1
    else:
      return i

  # Kiểm tra nếu phần tử được tìm thấy trong hai phần tử cuối
  if fibM_minus_1 and arr[offset + 1] == target:
    return offset + 1

  return -1  # Phần tử không được tìm thấy
```

## Giải thích

- **n = length(arr):** Khởi tạo biến `n` (số lượng phần tử) trong danh sách.

- **fibM_minus_2 = 0, fibM_minus_1 = 1, fibM = fibM_minus_1 + fibM_minus_2:** Khởi tạo các biến để tạo chuỗi Fibonacci.

- **while fibM < n:** Vòng lặp này tạo ra chuỗi Fibonacci cho đến khi số Fibonacci lớn nhất nhỏ hơn hoặc bằng số lượng
  phần tử trong danh sách.

- **offset = -1:** Khởi tạo biến `offset` (vị trí chia) ban đầu bằng -1.

- **while fibM > 1:** Vòng lặp này thực hiện tìm kiếm Fibonacci cho đến khi tìm thấy phần tử cần tìm hoặc không còn phần
  tử nào để kiểm tra.

    - **i = min(offset + fibM_minus_2, n - 1):** Tính toán vị trí chia (`i`) dựa trên số Fibonacci `fibM_minus_2` và vị
      trí chia trước đó (`offset`).

    - **if arr[i] < target:** Nếu phần tử ở vị trí chia nhỏ hơn giá trị cần tìm, thuật toán sẽ tiếp tục tìm kiếm trong
      nửa trái của danh sách.

        - Cập nhật các biến Fibonacci để thu hẹp phạm vi tìm kiếm.

        - Cập nhật `offset` bằng `i` để ghi nhớ vị trí chia hiện tại.

    - **elif arr[i] > target:** Nếu phần tử ở vị trí chia lớn hơn giá trị cần tìm, thuật toán sẽ tiếp tục tìm kiếm trong
      nửa phải của danh sách.

        - Cập nhật các biến Fibonacci để thu hẹp phạm vi tìm kiếm.

    - **else:** Nếu phần tử ở vị trí chia bằng giá trị cần tìm, thuật toán đã tìm thấy phần tử, trả về `i` (vị trí của
      phần tử).

- **if fibM_minus_1 and arr[offset + 1] == target:** Kiểm tra nếu phần tử cần tìm nằm ở phần tử tiếp theo sau vị trí
  chia.

- **return -1:** Nếu không tìm thấy phần tử, trả về -1.

## Ví dụ

Giả sử chúng ta có danh sách đã được sắp xếp: `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]` và cần tìm phần tử `13`.

- **Bước 1:** Tạo chuỗi Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...

- **Bước 2:** Tìm vị trí chia: Số Fibonacci gần nhất nhỏ hơn 10 là 8, nên `offset = -1`.

- **Bước 3:** So sánh:

    - `arr[min(-1 + 5, 9)] = arr[4] = 9`: So sánh giá trị 9 với 13.

    - `arr[min(-1 + 3, 9)] = arr[2] = 5`: So sánh giá trị 5 với 13.

    - `arr[min(-1 + 2, 9)] = arr[1] = 3`: So sánh giá trị 3 với 13.

    - `arr[min(-1 + 1, 9)] = arr[0] = 1`: So sánh giá trị 1 với 13.

    - `arr[min(-1 + 0, 9)] = arr[0] = 1`: So sánh giá trị 1 với 13.

    - `arr[min(-1 + 1, 9)] = arr[0] = 1`: So sánh giá trị 1 với 13.

    - `arr[min(-1 + 2, 9)] = arr[1] = 3`: So sánh giá trị 3 với 13.

    - `arr[min(-1 + 3, 9)] = arr[2] = 5`: So sánh giá trị 5 với 13.

    - `arr[min(-1 + 5, 9)] = arr[4] = 9`: So sánh giá trị 9 với 13.

    - `arr[min(-1 + 8, 9)] = arr[7] = 15`: So sánh giá trị 15 với 13.

    - `arr[min(-1 + 5, 9)] = arr[4] = 9`: So sánh giá trị 9 với 13.

    - `arr[min(-1 + 3, 9)] = arr[2] = 5`: So sánh giá trị 5 với 13.

    - `arr[min(-1 + 2, 9)] = arr[1] = 3`: So sánh giá trị 3 với 13.

    - `arr[min(-1 + 1, 9)] = arr[0] = 1`: So sánh giá trị 1 với 13.

    - `arr[min(0, 9)] = arr[0] = 1`: So sánh giá trị 1 với 13.

    - `arr[min(1, 9)] = arr[1] = 3`: So sánh giá trị 3 với 13.

    - `arr[min(2, 9)] = arr[2] = 5`: So sánh giá trị 5 với 13.

    - `arr[min(3, 9)] = arr[3] = 7`: So sánh giá trị 7 với 13.

    - `arr[min(4, 9)] = arr[4

] = 9`: So sánh giá trị 9 với 13.

- `arr[min(5, 9)] = arr[5] = 11`: So sánh giá trị 11 với 13.

- `arr[min(6, 9)] = arr[6] = 13`: Thuật toán đã tìm thấy phần tử cần tìm!

## Độ phức tạp

- **Độ phức tạp thời gian:** O(log n), vì thuật toán chia danh sách thành hai phần bằng nhau trong mỗi bước.
- **Độ phức tạp không gian:** O(1)

## Lưu ý

- Thuật toán Fibonacci Search chỉ hoạt động trên danh sách đã được sắp xếp.
- Nó có độ phức tạp thời gian logarit, hiệu quả hơn Linear Search và Jump Search, nhưng kém hiệu quả hơn Binary Search
  trong trường hợp xấu nhất.
- Thuật toán Fibonacci Search phù hợp cho các danh sách lớn khi không thể sử dụng Binary Search (ví dụ: danh sách quá
  lớn để lưu trữ trong bộ nhớ).

---

## Code ví dụ (TypeScript)

Dưới đây là phiên bản TypeScript của mã giả thuật toán Fibonacci Search:

```typescript
function fibonacciSearch(arr: number[], target: number): number {
  const n = arr.length;

  // Tạo chuỗi Fibonacci
  let fibM_minus_2 = 0;
  let fibM_minus_1 = 1;
  let fibM = fibM_minus_1 + fibM_minus_2;

  while (fibM < n) {
    fibM_minus_2 = fibM_minus_1;
    fibM_minus_1 = fibM;
    fibM = fibM_minus_1 + fibM_minus_2;
  }

  let offset = -1;

  // Tìm kiếm với Fibonacci
  while (fibM > 1) {
    let i = Math.min(offset + fibM_minus_2, n - 1);

    if (arr[i] < target) {
      fibM = fibM_minus_1;
      fibM_minus_1 = fibM_minus_2;
      fibM_minus_2 = fibM - fibM_minus_1;
      offset = i;
    } else if (arr[i] > target) {
      fibM = fibM_minus_2;
      fibM_minus_1 -= fibM_minus_2;
      fibM_minus_2 = fibM - fibM_minus_1;
    } else {
      return i; // Phần tử tìm thấy
    }
  }

  if (fibM_minus_1 && arr[offset + 1] === target) {
    return offset + 1; // Phần tử tìm thấy ở vị trí tiếp theo
  }

  return -1; // Phần tử không được tìm thấy
}
```
