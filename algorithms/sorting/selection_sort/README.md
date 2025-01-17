# Thuật toán Selection Sort: Sắp xếp chọn

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Selection Sort](#mã-giả-của-thuật-toán-selection-sort)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán Selection Sort (hay còn gọi là sắp xếp chọn) là một thuật toán sắp xếp đơn giản, hoạt động dựa trên việc tìm
phần tử nhỏ nhất (hoặc lớn nhất) trong danh sách và hoán đổi nó với phần tử đầu tiên của danh sách. Quá trình này được
lặp lại cho đến khi toàn bộ danh sách được sắp xếp.

## Cách hoạt động

1. **Tìm phần tử nhỏ nhất:** Thuật toán bắt đầu bằng việc duyệt qua danh sách và tìm phần tử nhỏ nhất.
2. **Hoán đổi:** Phần tử nhỏ nhất được hoán đổi với phần tử đầu tiên của danh sách.
3. **Lặp lại:** Bước 1 và 2 được lặp lại cho phần còn lại của danh sách, bắt đầu từ phần tử thứ hai, cho đến khi danh
   sách được sắp xếp hoàn toàn.

## Mã giả của thuật toán Selection Sort

```typescript
function selectionSort(arr: number[]): number[] {
  const n = arr.length;

  for (let i = 0; i < n - 1; i++) {
    let minIndex = i; // Giả sử phần tử đầu tiên là nhỏ nhất
    for (let j = i + 1; j < n; j++) {
      // Duyệt phần chưa được sắp xếp
      if (arr[j] < arr[minIndex]) {
        // Tìm phần tử nhỏ hơn
        minIndex = j; // Cập nhật chỉ số phần tử nhỏ nhất
      }
    }

    // Hoán đổi nếu tìm thấy phần tử nhỏ hơn
    if (minIndex !== i) {
      [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
  }

  return arr;
}
```

## Giải thích

- **n = arr.length:** Lấy độ dài của mảng arr.
- **for i from 0 to n - 1 do:** Vòng lặp ngoài duyệt qua từng phần tử trong mảng (n lần).
- **minIndex = i:** Khởi tạo biến minIndex với giá trị i, giả sử phần tử đầu tiên là nhỏ nhất.
- **for j from i + 1 to n do:** Vòng lặp trong để tìm phần tử nhỏ nhất trong phần còn lại của mảng (trừ phần tử đầu).
- **if (arr[j] < arr[minIndex]) then minIndex = j:** So sánh phần tử hiện tại (arr[j]) với phần tử nhỏ nhất hiện tại (
  arr[minIndex]). Nếu arr[j] nhỏ hơn, cập nhật minIndex với j.
- **if (minIndex !== i) then swap arr[i] and arr[minIndex]:** Nếu phần tử nhỏ nhất không phải là phần tử đầu tiên (
  minIndex !== i), hoán đổi hai phần tử.

## Ví dụ

Giả sử chúng ta có danh sách cần sắp xếp tăng dần: `64, 25, 12, 22, 11`

### Lần lặp 1:

- i = 0
    - minIndex = 0
    - j = 1: **25 < 64**, minIndex = 1
    - j = 2: **12 < 25**, minIndex = 2
    - j = 3: 22 < 12, minIndex vẫn giữ là 2
    - j = 4: **11 < 12**, minIndex = 4
    - Hoán đổi: `11, 25, 12, 22, 64`

### Lần lặp 2:

- i = 1
    - minIndex = 1
    - j = 2: **12 < 25**, minIndex = 2
    - j = 3: 22 < 12, minIndex vẫn giữ là 2
    - j = 4: 64 < 12, minIndex vẫn giữ là 3
    - Hoán đổi: `11, 12, 25, 22, 64`

### Lần lặp 3:

- i = 2
    - minIndex = 2
    - j = 3: **22 < 25**, minIndex = 3
    - j = 4: **64 < 22**, minIndex vẫn giữ là 3
    - Hoán đổi: `11, 12, 22, 25, 64`

### Lần lặp 4:

- i = 3
    - minIndex = 3
    - j = 4: 64 < 25, minIndex vẫn giữ là 3
    - Hoán đổi: `11, 12, 22, 25, 64`

**Kết quả:** Danh sách đã được sắp xếp: `11, 12, 22, 25, 64`

## Độ phức tạp

- **Độ phức tạp thời gian:** O(n²)
- **Độ phức tạp không gian:** O(1)

## Lưu ý

- **Tìm phần tử nhỏ nhất (hoặc lớn nhất):** Thuật toán duyệt qua danh sách và tìm phần tử nhỏ nhất (hoặc lớn nhất) trong
  phần chưa được sắp xếp.
- **Hoán đổi vị trí:** Phần tử nhỏ nhất (hoặc lớn nhất) được hoán đổi vị trí với phần tử đầu tiên của phần chưa được sắp
  xếp.
- **Lặp lại:** Quá trình tìm và hoán đổi được lặp lại cho phần còn lại của danh sách, mỗi lần thu hẹp phần chưa được sắp
  xếp.
