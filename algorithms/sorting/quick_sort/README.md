# Thuật toán Quick Sort: Sắp xếp nhanh

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Quick Sort](#mã-giả-của-thuật-toán-quick-sort)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Cải tiến](#cải-tiến)
8. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán Quick Sort (hay còn gọi là sắp xếp nhanh) là một thuật toán sắp xếp chia để trị (divide and conquer) rất hiệu quả và được sử dụng rộng rãi trong lập trình. Nó hoạt động bằng cách chọn một phần tử làm "pivot" (trụ) và chia danh sách thành hai phần: các phần tử nhỏ hơn pivot và các phần tử lớn hơn pivot. Sau đó, nó đệ quy sắp xếp hai phần này cho đến khi danh sách được sắp xếp hoàn toàn.

## Cách hoạt động

1. **Chọn pivot:** Chọn một phần tử từ danh sách để làm pivot. Có nhiều cách chọn pivot, ví dụ như:
   - Lấy phần tử đầu tiên hoặc cuối cùng.
   - Lấy phần tử ở giữa danh sách.
   - Chọn ngẫu nhiên một phần tử.
2. **Phân chia:** Tạo hai danh sách con:
   - Danh sách con trái: chứa các phần tử nhỏ hơn hoặc bằng pivot.
   - Danh sách con phải: chứa các phần tử lớn hơn pivot.
3. **Sắp xếp đệ quy:** Gọi đệ quy hàm sắp xếp nhanh cho danh sách con trái và danh sách con phải.
4. **Kết hợp:** Kết hợp danh sách con trái, pivot, và danh sách con phải để tạo thành danh sách đã sắp xếp.

## Mã giả của thuật toán Quick Sort

```typescript
function quickSort(arr: number[]): number[] {
  const n = arr.length;

  if (n <= 1) {
    return arr;
  }

  const pivot = arr[Math.floor(n / 2)];
  const left: number[] = [];
  const right: number[] = [];

  for (let i = 0; i < n; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else if (arr[i] > pivot) {
      right.push(arr[i]);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}
```

## Giải thích

- **n = arr.length:** Lấy độ dài của mảng arr.
- **IF n <= 1:** Nếu mảng có độ dài nhỏ hơn hoặc bằng 1, mảng đã được sắp xếp và trả về trực tiếp.
- **pivot = arr[Math.floor(n / 2)]:** Chọn phần tử ở giữa mảng làm pivot.
- **left: number[] = [], right: number[] = []:** Khởi tạo hai danh sách con trống để lưu trữ các phần tử nhỏ hơn và lớn hơn pivot.
- **for (let i = 0; i < n; i++):** Vòng lặp duyệt qua từng phần tử trong mảng.
- **if (arr[i] < pivot):** Nếu phần tử nhỏ hơn pivot, thêm vào danh sách con trái.
- **else if (arr[i] > pivot):** Nếu phần tử lớn hơn pivot, thêm vào danh sách con phải.
- **return [...quickSort(left), pivot, ...quickSort(right)]:** Gọi đệ quy hàm `quickSort` cho danh sách con trái và danh sách con phải, sau đó kết hợp chúng với pivot để tạo thành danh sách đã sắp xếp.

## Ví dụ

Giả sử chúng ta có danh sách cần sắp xếp tăng dần: `5, 1, 4, 2, 8`

### Bước 1: Chọn pivot và phân chia

- Pivot = 4 (phần tử giữa).
- Danh sách trái: [1, 2]
- Danh sách phải: [5, 8]

### Bước 2: Sắp xếp đệ quy

- Gọi `quickSort` cho danh sách trái: `1, 2`
  - Pivot = 1
  - Danh sách trái: []
  - Danh sách phải: [2]
  - Kết quả: [1, 2]
- Gọi `quickSort` cho danh sách phải: `5, 8`
  - Pivot = 5
  - Danh sách trái: []
  - Danh sách phải: [8]
  - Kết quả: [5, 8]

### Bước 3: Kết hợp

- Kết hợp danh sách trái, pivot và danh sách phải: `1, 2` + `4` + `5, 8` -> `1, 2, 4, 5, 8`

**Kết quả:** Danh sách đã được sắp xếp: `1, 2, 4, 5, 8`

## Độ phức tạp

- **Độ phức tạp thời gian:**
  - Trường hợp xấu nhất: O(n²), khi mảng đã được sắp xếp hoặc gần như đã sắp xếp.
  - Trường hợp tốt nhất: O(n log n), khi pivot được chọn một cách hiệu quả.
  - Trường hợp trung bình: O(n log n).
- **Độ phức tạp không gian:** O(log n), do việc đệ quy.

## Cải tiến

- **Chọn pivot:** Chọn pivot một cách thông minh (ví dụ, bằng cách sử dụng phương pháp "median-of-three") để tránh trường hợp xấu nhất.
- **Tối ưu hóa đệ quy:** Sử dụng kỹ thuật "tail recursion" để tối ưu hóa đệ quy.

## Lưu ý

- Thuật toán Quick Sort rất hiệu quả trong trường hợp trung bình, nhưng có thể gặp phải trường hợp xấu nhất với độ phức tạp thời gian O(n²).
- Chọn pivot một cách hợp lý là rất quan trọng để tối ưu hóa hiệu suất của thuật toán.
- Thuật toán Quick Sort có thể được tối ưu hóa bằng cách sử dụng kỹ thuật "tail recursion" để loại bỏ đệ quy và cải thiện hiệu suất.
