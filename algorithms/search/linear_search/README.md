# Thuật Toán Tìm kiếm Tuyến Tính (Linear Search)

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Linear Search](#mã-giả-của-thuật-toán-linear-search)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán tìm kiếm tuyến tính (Linear Search) là một thuật toán tìm kiếm đơn giản, được sử dụng để tìm một phần tử cụ thể trong một danh sách. Nó hoạt động bằng cách duyệt qua từng phần tử trong danh sách theo thứ tự, so sánh mỗi phần tử với giá trị cần tìm. Nếu phần tử được tìm thấy, thuật toán trả về vị trí của nó trong danh sách; ngược lại, thuật toán trả về -1 để báo hiệu rằng phần tử không tồn tại trong danh sách.

## Cách hoạt động

1. **Khởi tạo:** Thuật toán bắt đầu bằng việc khởi tạo một biến `index` với giá trị 0, đại diện cho vị trí của phần tử đầu tiên trong danh sách.
2. **Duyệt danh sách:** Thuật toán sẽ duyệt qua từng phần tử trong danh sách, từ phần tử đầu tiên đến phần tử cuối cùng.
3. **So sánh:** Tại mỗi bước, thuật toán sẽ so sánh giá trị của phần tử hiện tại với giá trị cần tìm.
4. **Kết quả:**
   - Nếu phần tử hiện tại bằng giá trị cần tìm, thuật toán trả về `index` (vị trí của phần tử trong danh sách).
   - Nếu duyệt hết danh sách mà không tìm thấy phần tử cần tìm, thuật toán trả về -1.

## Mã giả của thuật toán Linear Search

```
linear_search(arr, target):
  n = length(arr)

  FOR i FROM 0 to n-1:
    IF arr[i] == target:
      RETURN i

  RETURN -1
```

## Giải thích

- **n = length(arr):** Lấy độ dài của mảng arr.
- **FOR i FROM 0 to n-1:** Vòng lặp duyệt qua từng phần tử trong mảng (n lần).
- **IF arr[i] == target:** So sánh phần tử hiện tại (arr[i]) với giá trị cần tìm (target).
- **RETURN i:** Nếu phần tử được tìm thấy, trả về vị trí của nó trong mảng (i).
- **RETURN -1:** Nếu duyệt hết danh sách mà không tìm thấy phần tử, trả về -1.

## Ví dụ

Giả sử chúng ta có danh sách: `5, 1, 4, 2, 8` và cần tìm phần tử `2`.

**Bước 1:** `index = 0`, `arr[0] = 5`, `5 != 2` -> Tiếp tục.

**Bước 2:** `index = 1`, `arr[1] = 1`, `1 != 2` -> Tiếp tục.

**Bước 3:** `index = 2`, `arr[2] = 4`, `4 != 2` -> Tiếp tục.

**Bước 4:** `index = 3`, `arr[3] = 2`, `2 == 2` -> Tìm thấy! `RETURN 3`.

## Độ phức tạp

- **Độ phức tạp thời gian:**
  - Trường hợp xấu nhất: O(n), khi phần tử cần tìm nằm ở vị trí cuối cùng hoặc không tồn tại trong danh sách.
  - Trường hợp tốt nhất: O(1), khi phần tử cần tìm là phần tử đầu tiên trong danh sách.
- **Độ phức tạp không gian:** O(1)

## Lưu ý

- Thuật toán Linear Search rất đơn giản và dễ triển khai.
- Tuy nhiên, nó có độ phức tạp thời gian tuyến tính, điều này có nghĩa là thời gian thực hiện của thuật toán tăng tuyến tính theo số lượng phần tử trong danh sách.
- Do đó, thuật toán Linear Search không phù hợp cho các danh sách lớn, đặc biệt là khi hiệu suất là yếu tố quan trọng.
- Với danh sách lớn, các thuật toán tìm kiếm hiệu quả hơn như Binary Search nên được sử dụng.

---

## Code ví dụ (TypeScript)

Dưới đây là phiên bản TypeScript của mã giả thuật toán Linear Search:

```typescript
function linearSearch(arr: number[], target: number): number {
  const n = arr.length;

  // Duyệt qua tất cả các phần tử trong mảng
  for (let i = 0; i < n; i++) {
    if (arr[i] === target) {
      return i; // Trả về chỉ số nếu tìm thấy
    }
  }

  return -1; // Nếu không tìm thấy phần tử, trả về -1
}
```
