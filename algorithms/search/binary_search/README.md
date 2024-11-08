# Thuật Toán Tìm Kiếm Nhị Phân (Binary Search)

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Binary Search](#mã-giả-của-thuật-toán-binary-search)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán tìm kiếm nhị phân (Binary Search) là một thuật toán tìm kiếm hiệu quả được sử dụng để tìm một phần tử cụ thể trong một danh sách đã được sắp xếp. Nó hoạt động bằng cách liên tục chia danh sách thành hai phần bằng nhau và so sánh phần tử cần tìm với phần tử ở giữa. Nếu phần tử cần tìm nhỏ hơn phần tử ở giữa, thuật toán sẽ tiếp tục tìm kiếm trong nửa đầu danh sách. Ngược lại, nếu phần tử cần tìm lớn hơn phần tử ở giữa, thuật toán sẽ tiếp tục tìm kiếm trong nửa sau danh sách. Quá trình này được lặp lại cho đến khi tìm thấy phần tử cần tìm hoặc danh sách còn lại trống.

## Cách hoạt động

1. **Khởi tạo:** Thuật toán bắt đầu bằng việc đặt hai biến `left` và `right` tương ứng với vị trí của phần tử đầu tiên và phần tử cuối cùng trong danh sách.
2. **Duyệt danh sách:** Điều kiện `left` nhỏ hơn hoặc bằng `right`:
   - Tính vị trí của phần tử ở giữa `mid = (left + right) // 2`.
   - So sánh giá trị cần tìm với giá trị của phần tử ở giữa `arr[mid]`:
     - Nếu `target < arr[mid]`, đặt `right = mid - 1` (tìm kiếm trong nửa đầu).
     - Nếu `target > arr[mid]`, đặt `left = mid + 1` (tìm kiếm trong nửa sau).
     - Nếu `target == arr[mid]`, trả về `mid` (đã tìm thấy phần tử).
3. **Kết quả:**
   - Nếu `left > right`, trả về -1 (phần tử không tồn tại trong danh sách).

## Mã giả của thuật toán Binary Search

```
binary_search(arr, target):
  left = 0
  right = length(arr) - 1

  WHILE left <= right:
    mid = (left + right) // 2
    IF target < arr[mid]:
      right = mid - 1
    ELSE IF target > arr[mid]:
      left = mid + 1
    ELSE:
      RETURN mid
  RETURN -1
```

## Giải thích

- **left = 0, right = length(arr) - 1:** Khởi tạo biến `left` và `right` với vị trí của phần tử đầu tiên và cuối cùng trong danh sách.

- **WHILE left <= right:** Vòng lặp duyệt qua danh sách cho đến khi `left` lớn hơn `right`.

- **mid = (left + right) // 2:** Tính vị trí của phần tử ở giữa.

- **IF target < arr[mid]:** Nếu giá trị cần tìm nhỏ hơn phần tử ở giữa, đặt `right` thành `mid - 1` để tìm kiếm trong nửa đầu danh sách.

- **ELSE IF target > arr[mid]:** Nếu giá trị cần tìm lớn hơn phần tử ở giữa, đặt `left` thành `mid + 1` để tìm kiếm trong nửa sau danh sách.

- **ELSE:** Nếu giá trị cần tìm bằng phần tử ở giữa, trả về `mid` (đã tìm thấy phần tử).

- **RETURN -1:** Nếu duyệt hết danh sách mà không tìm thấy phần tử, trả về -1.

## Ví dụ

Giả sử chúng ta có danh sách đã được sắp xếp: `[1, 2, 4, 5, 8]` và cần tìm phần tử `4`.

**Bước 1:** `left = 0`, `right = 4`, `mid = (0 + 4) // 2 = 2`, `arr[2] = 4`, `target == arr[mid]` -> Tìm thấy! `RETURN 2`.

### Mã ví dụ bằng TypeScript

```typescript
function binarySearch(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid; // Đã tìm thấy phần tử
    } else if (arr[mid] > target) {
      right = mid - 1; // Tìm kiếm trong nửa đầu
    } else {
      left = mid + 1; // Tìm kiếm trong nửa sau
    }
  }

  return -1; // Phần tử không có trong danh sách
}

const arr = [1, 2, 4, 5, 8];
const target = 4;
console.log(binarySearch(arr, target)); // Output: 2
```

## Độ phức tạp

- **Độ phức tạp thời gian:** O(log n), vì thuật toán liên tục chia danh sách thành hai phần bằng nhau cho đến khi tìm thấy phần tử cần tìm.
- **Độ phức tạp không gian:** O(1)

## Lưu ý

- Thuật toán Binary Search chỉ hoạt động trên danh sách đã được sắp xếp.
- Nó có độ phức tạp thời gian logarit, điều này có nghĩa là nó rất hiệu quả cho các danh sách lớn.
- Thuật toán Binary Search thường được sử dụng trong các trường hợp cần tìm kiếm một phần tử cụ thể trong một danh sách đã được sắp xếp, chẳng hạn như tìm kiếm một từ trong từ điển.
