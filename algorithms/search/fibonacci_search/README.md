## **🚀 "BÍ MẬT" THUẬT TOÁN TÌM KIẾM FIBONACCI: DÀNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán tìm kiếm khá thú vị: Tìm kiếm
Fibonacci. Nghe có vẻ "lạ" nhưng thực ra rất hữu ích đấy. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ
minh họa để các bạn dễ "nuốt" nhé! Let's go!

### **I. TÌM KIẾM FIBONACCI LÀ GÌ?**

* **Tìm kiếm Fibonacci (Fibonacci Search):** Là thuật toán tìm kiếm một phần tử trong danh sách đã được sắp xếp, dựa
  trên chuỗi số Fibonacci.
* **Chuỗi Fibonacci:** Là chuỗi số mà mỗi số là tổng của hai số liền trước (ví dụ: 0, 1, 1, 2, 3, 5, 8, 13...).
* **Điểm khác biệt:** Thay vì chia đôi danh sách như Binary Search, Fibonacci Search sử dụng số Fibonacci để chia danh
  sách.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC)**

1. **Khởi tạo:**
    * Tạo chuỗi Fibonacci đủ lớn để "bao phủ" danh sách.
    * Tìm số Fibonacci gần nhất nhưng nhỏ hơn số lượng phần tử trong danh sách.

2. **Tìm vị trí chia:**
    * Dựa trên số Fibonacci, tìm "vị trí chia" (offset) trong danh sách.

3. **So sánh:**
    * So sánh giá trị cần tìm (`target`) với giá trị ở vị trí chia (`arr[i]`).
        * Nếu `target` **bằng** `arr[i]`: Tìm thấy rồi!
        * Nếu `target` **nhỏ hơn** `arr[i]`: Tìm tiếp ở nửa trái.
        * Nếu `target` **lớn hơn** `arr[i]`: Tìm tiếp ở nửa phải.

4. **Lặp:**
    * Lặp lại bước 2 và 3 trên nửa danh sách được chọn cho đến khi tìm thấy hoặc hết phần tử.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĂN CHUỐI**

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

    # So sánh
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

  # Kiểm tra 2 phần tử cuối
  if fibM_minus_1 and arr[offset + 1] == target:
    return offset + 1

  return -1  # Không tìm thấy
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHÉ!)**

* **`n = length(arr)`:** Lấy số phần tử của danh sách.
* **`# Tạo chuỗi Fibonacci`:** Khởi tạo các biến để tạo chuỗi Fibonacci.
* **`while fibM < n`:** Vòng lặp tạo chuỗi Fibonacci đến khi `fibM` lớn hơn hoặc bằng `n`.
* **`offset = -1`:** Khởi tạo vị trí chia ban đầu.
* **`while fibM > 1`:** Vòng lặp thực hiện tìm kiếm.
    * **`i = min(offset + fibM_minus_2, n - 1)`:** Tính vị trí chia `i`.
    * **`if arr[i] < target`:** Nếu giá trị ở vị trí chia nhỏ hơn giá trị cần tìm => Tìm tiếp bên trái.
        * Cập nhật các số Fibonacci và vị trí `offset`.
    * **`elif arr[i] > target`:** Nếu giá trị ở vị trí chia lớn hơn giá trị cần tìm => Tìm tiếp bên phải.
        * Cập nhật các số Fibonacci.
    * **`else`:** Tìm thấy rồi! Trả về vị trí `i`.
* **`if fibM_minus_1 and arr[offset + 1] == target`:** Kiểm tra phần tử cuối.
* **`return -1`:** Không tìm thấy.

### **V. VÍ DỤ MINH HỌA (XEM LÀ HIỂU LIỀN)**

Giả sử ta có danh sách: `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]` và cần tìm số `13`.

* **Bước 1:** Chuỗi Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
* **Bước 2:** Số Fibonacci gần nhất nhỏ hơn 10 là 8 => `offset = -1`.
* **Bước 3:** So sánh và di chuyển vị trí chia:

    * `arr[min(-1 + 5, 9)] = arr[4] = 9` (< 13, tìm bên phải)
    * `arr[min(4 + 2, 9)] = arr[6] = 13` (== 13, tìm thấy!)

### **VI. ĐỘ PHỨC TẠP (THỜI GIAN VÀ KHÔNG GIAN)**

* **Độ phức tạp thời gian:** O(log n).
* **Độ phức tạp không gian:** O(1).
* **Lưu ý:** Fibonacci Search thường chậm hơn Binary Search một chút trong trường hợp tốt nhất và xấu nhất, nhưng có thể
  nhanh hơn trong một số trường hợp đặc biệt.

### **VII. LƯU Ý QUAN TRỌNG**

* **Yêu cầu:** Danh sách phải được sắp xếp.
* **Ứng dụng:**
    * Khi không thể dùng Binary Search (ví dụ: danh sách quá lớn để lưu trong RAM).
    * Khi truy cập vào bộ nhớ tốn kém (ví dụ: truy cập ổ cứng).

### **VIII. CODE VÍ DỤ BẰNG TYPESCRIPT**

```typescript
function fibonacciSearch(arr: number[], target: number): number {
    const n = arr.length;

    let fibM_minus_2 = 0;
    let fibM_minus_1 = 1;
    let fibM = fibM_minus_1 + fibM_minus_2;

    while (fibM < n) {
        fibM_minus_2 = fibM_minus_1;
        fibM_minus_1 = fibM;
        fibM = fibM_minus_1 + fibM_minus_2;
    }

    let offset = -1;

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
            return i;
        }
    }

    if (fibM_minus_1 && arr[offset + 1] === target) {
        return offset + 1;
    }

    return -1;
}

const arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
const target = 13;
console.log(fibonacciSearch(arr, target)); // Output: 6
```

### **KẾT LUẬN**

Thuật toán tìm kiếm Fibonacci tuy "lạ" nhưng rất hữu ích trong nhiều trường hợp. Hy vọng qua bài viết này, các bạn đã
hiểu rõ hơn về nó và có thêm một "vũ khí" trong kho tàng kiến thức của mình. Chúc các bạn thành công! 💪
