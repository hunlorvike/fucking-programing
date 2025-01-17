# Thuật Toán Tìm kiếm Nhảy (Jump Search)

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Jump Search](#mã-giả-của-thuật-toán-jump-search)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán tìm kiếm nhảy (Jump Search) là một thuật toán tìm kiếm hiệu quả được sử dụng để tìm một phần tử cụ thể trong
một danh sách đã được sắp xếp. Nó hoạt động bằng cách nhảy qua danh sách với bước nhảy cố định, sau đó tìm kiếm tuyến
tính trong khoảng nhảy cuối cùng. Thuật toán này kết hợp lợi ích của tìm kiếm tuyến tính (đơn giản) và tìm kiếm nhị
phân (hiệu quả).

## Cách hoạt động

1. **Khởi tạo:** Thuật toán bắt đầu bằng việc tính toán bước nhảy `step = √n` (căn bậc hai của số lượng phần tử trong
   danh sách).
2. **Nhảy:** Thuật toán sẽ nhảy qua danh sách với bước nhảy `step`, so sánh phần tử ở vị trí nhảy hiện tại với giá trị
   cần tìm.
    - Nếu giá trị cần tìm nhỏ hơn phần tử ở vị trí nhảy hiện tại, thuật toán sẽ tìm kiếm tuyến tính trong khoảng nhảy
      trước đó (từ vị trí nhảy trước đến vị trí nhảy hiện tại).
    - Nếu giá trị cần tìm lớn hơn phần tử ở vị trí nhảy hiện tại, thuật toán sẽ tiếp tục nhảy qua danh sách với bước
      nhảy `step`.
3. **Tìm kiếm tuyến tính:** Sau khi tìm thấy khoảng nhảy phù hợp, thuật toán sẽ tìm kiếm tuyến tính trong khoảng đó (từ
   vị trí nhảy trước đến vị trí nhảy hiện tại) để tìm phần tử cần tìm.

## Mã giả của thuật toán Jump Search

```
jump_search(arr, target):
  n = length(arr)
  step = int(sqrt(n))

  # Nhảy qua danh sách
  prev = 0
  while arr[min(step, n) - 1] < target:
    prev = step
    step += int(sqrt(n))
    if prev >= n:
      return -1

  # Tìm kiếm tuyến tính trong khoảng nhảy
  while arr[prev] < target:
    prev += 1
    if prev == min(step, n):
      return -1

  # Kiểm tra nếu phần tử được tìm thấy
  if arr[prev] == target:
    return prev
  else:
    return -1
```

## Giải thích

- **n = length(arr), step = int(sqrt(n)):** Khởi tạo biến `n` (số lượng phần tử) và `step` (bước nhảy) với giá trị căn
  bậc hai của số lượng phần tử.

- **while arr[min(step, n) - 1] < target:** Vòng lặp này nhảy qua danh sách cho đến khi tìm thấy phần tử lớn hơn hoặc
  bằng giá trị cần tìm.

    - `min(step, n)-1` đảm bảo rằng vị trí nhảy không vượt quá giới hạn của danh sách.

- **prev = step, step += int(sqrt(n)):** Cập nhật vị trí nhảy trước và vị trí nhảy hiện tại.

    - prev: Biến này lưu trữ vị trí nhảy trước đó.

    - n: Biến này là số lượng phần tử trong danh sách.

    - Khi prev >= n, điều đó có nghĩa là vị trí nhảy trước đó đã vượt quá giới hạn của danh sách. Nói cách khác, thuật
      toán đã nhảy qua toàn bộ danh sách mà vẫn chưa tìm thấy phần tử cần tìm.

- **if prev >= n:** Nếu vị trí nhảy trước lớn hơn hoặc bằng số lượng phần tử, điều đó có nghĩa là phần tử cần tìm không
  tồn tại trong danh sách, trả về -1.

- **while arr[prev] < target:** Vòng lặp này thực hiện tìm kiếm tuyến tính trong khoảng nhảy phù hợp.

- **prev += 1:** Cập nhật vị trí hiện tại trong khoảng nhảy.

- **if prev == min(step, n):** Nếu vị trí hiện tại vượt quá giới hạn của khoảng nhảy, điều đó có nghĩa là phần tử cần
  tìm không tồn tại trong danh sách, trả về -1.

- **if arr[prev] == target:** Nếu phần tử ở vị trí hiện tại bằng giá trị cần tìm, trả về vị trí `prev` (đã tìm thấy phần
  tử).

- **else:** Nếu phần tử ở vị trí hiện tại không bằng giá trị cần tìm, trả về -1 (phần tử không tồn tại trong danh sách).

## Ví dụ

Giả sử chúng ta có danh sách đã được sắp xếp: `1, 3, 5, 7, 9, 11, 13, 15, 17, 19` và cần tìm phần tử `13`.

- **Bước 1:** Khởi tạo:

    - n = 10 (số lượng phần tử trong danh sách).
    - step = int(sqrt(10)) = 3 (bước nhảy).

- **Bước 2:** Nhảy qua danh sách:

    - arr[2] = 5: Nhảy đến vị trí thứ 3 (vì step = 3) và so sánh giá trị 5 với giá trị cần tìm 13.

    - arr[5] = 11: Nhảy thêm 3 bước (vì step = 3) đến vị trí thứ 6 và so sánh giá trị 11 với giá trị cần tìm 13.

    - arr[8] = 17: Nhảy thêm 3 bước đến vị trí thứ 9 và so sánh giá trị 17 với giá trị cần tìm 13.

        - Bởi vì 13 nhỏ hơn 17, chúng ta biết rằng phần tử cần tìm nằm trong khoảng nhảy giữa vị trí thứ 6 và vị trí thứ
            9.

**Sơ đồ minh họa:**

```
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
              ^       ^       ^       ^
              |       |       |       |
              3       6       9       12
            (step = 3)
```

- **Bước 3:** Tìm kiếm tuyến tính:
    - arr[6] = 13: Kiểm tra phần tử ở vị trí thứ 6 (vì prev = 6).

## Độ phức tạp

- **Độ phức tạp thời gian:** O(√n), vì thuật toán nhảy qua danh sách với bước nhảy √n và sau đó tìm kiếm tuyến tính
  trong khoảng nhảy.

- **Độ phức tạp không gian:** O(1)

## Lưu ý

- Thuật toán Jump Search chỉ hoạt động trên danh sách đã được sắp xếp.
- Nó có độ phức tạp thời gian cận tuyến tính, hiệu quả hơn Linear Search nhưng kém hiệu quả hơn Binary Search.
- Thuật toán Jump Search phù hợp cho các danh sách lớn khi không thể sử dụng Binary Search (ví dụ: danh sách quá lớn để
  lưu trữ trong bộ nhớ).

---

## Code ví dụ (TypeScript)

Dưới đây là phiên bản TypeScript của mã giả thuật toán Jump Search:

```typescript
function jumpSearch(arr: number[], target: number): number {
  const n = arr.length;
  const step = Math.floor(Math.sqrt(n)); // Bước nhảy

  let prev = 0;

  // Nhảy qua danh sách
  while (arr[Math.min(step, n) - 1] < target) {
    prev = step;
    step += Math.floor(Math.sqrt(n));
    if (prev >= n) {
      return -1; // Nếu vị trí nhảy vượt quá số lượng phần tử
    }
  }

  // Tìm kiếm tuyến tính trong khoảng nhảy
  while (arr[prev] < target) {
    prev += 1;
    if (prev === Math.min(step, n)) {
      return -1; // Nếu không tìm thấy phần tử
    }
  }

  // Kiểm tra nếu phần tử được tìm thấy
  if (arr[prev] === target) {
    return prev; // Phần tử tìm thấy
  }

  return -1; // Phần tử không tìm thấy
}
```
