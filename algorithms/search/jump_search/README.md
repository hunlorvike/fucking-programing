## **🚀 "GIẢI MÃ" THUẬT TOÁN TÌM KIẾM NHẢY: DÀNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán tìm kiếm thú vị nữa: Tìm kiếm Nhảy (
Jump Search). Đây là một "chiêu" hay giúp bạn tìm kiếm dữ liệu nhanh hơn Linear Search mà lại không quá phức tạp như
Binary Search. Bắt đầu thôi!

### **I. TÌM KIẾM NHẢY LÀ GÌ?**

* **Tìm kiếm nhảy (Jump Search):** Là thuật toán tìm kiếm một phần tử trong danh sách đã được sắp xếp bằng cách "nhảy"
  qua các vị trí, sau đó tìm kiếm tuyến tính trong khoảng nhảy cuối cùng.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn đang leo cầu thang:
        * Bạn không đi từng bậc một mà "nhảy" một số bậc, đến gần vị trí cần tìm thì bạn mới đi từng bậc.
* **Ưu điểm:**
    * **Nhanh hơn Linear Search:** Với danh sách lớn, nó tìm kiếm nhanh hơn rất nhiều.
    * **Đơn giản:** Dễ hiểu và dễ cài đặt hơn Binary Search.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Khởi tạo:**
    * Tính `step` (bước nhảy) bằng căn bậc hai của số phần tử trong danh sách: `step = √n`.
    * Đặt `prev = 0` (vị trí nhảy trước).

2. **Nhảy:**
    * Nhảy qua danh sách với bước nhảy `step`.
    * So sánh giá trị cần tìm (`target`) với giá trị ở vị trí nhảy hiện tại (`arr[i]`).
        * Nếu `target` **nhỏ hơn** `arr[i]`: Dừng lại, tìm kiếm tuyến tính trong khoảng nhảy trước.
        * Nếu `target` **lớn hơn** `arr[i]`: Tiếp tục nhảy (`prev = step`, `step = step + √n`).
        * Nếu vượt quá giới hạn danh sách thì trả về `-1`.

3. **Tìm kiếm tuyến tính:**
    * Tìm kiếm tuyến tính từ vị trí `prev` đến vị trí nhảy hiện tại.

4. **Kết thúc:**
    * Nếu tìm thấy `target` trả về vị trí của `target`, nếu không thì trả về `-1` (không có phần tử trong danh sách).

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ NHƯ ĂN KẸO**

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

  # Kiểm tra nếu tìm thấy
  if arr[prev] == target:
    return prev
  else:
    return -1
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`n = length(arr)`:** Lấy số lượng phần tử của danh sách.
* **`step = int(sqrt(n))`:** Tính bước nhảy (lấy phần nguyên của căn bậc hai).
* **`prev = 0`:** Khởi tạo vị trí nhảy trước bằng 0.
* **`while arr[min(step, n) - 1] < target`:** Vòng lặp nhảy đến khi tìm thấy vị trí có giá trị lớn hơn hoặc bằng
  `target`.
    * `min(step, n) - 1` để đảm bảo không vượt quá giới hạn của danh sách.
* **`prev = step; step += int(sqrt(n))`:** Cập nhật vị trí nhảy trước và vị trí nhảy tiếp theo.
* **`if prev >= n`:** Kiểm tra nếu đã nhảy qua hết danh sách.
* **`while arr[prev] < target`:** Vòng lặp tìm kiếm tuyến tính trong khoảng nhảy.
* **`prev += 1`:** Tăng `prev` lên để đi từng bước trong khoảng nhảy.
* **`if prev == min(step, n)`:** Kiểm tra nếu đã đi hết khoảng nhảy.
* **`if arr[prev] == target`:** Tìm thấy rồi! Trả về `prev`.
* **`else`:** Không tìm thấy, trả về `-1`.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ TRỰC QUAN)**

Giả sử ta có danh sách: `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]` và cần tìm số `13`.

* **Bước 1:** `n = 10`, `step = √10 ≈ 3`, `prev = 0`.
* **Bước 2:** Nhảy:
    * `arr[3-1] = arr[2] = 5` (< 13, tiếp tục nhảy).
    * `arr[6-1] = arr[5] = 11` (< 13, tiếp tục nhảy).
    * `arr[9-1] = arr[8] = 17` (> 13, dừng lại).
* **Bước 3:** Tìm kiếm tuyến tính trong khoảng từ 6 đến 9:
    * `arr[6] = 13` (Tìm thấy!).
* **Kết quả:** Trả về vị trí `6`.

### **VI. ĐỘ PHỨC TẠP (THỜI GIAN VÀ KHÔNG GIAN)**

* **Độ phức tạp thời gian:** O(√n) (căn bậc hai của n).
    * Tức là thuật toán chạy nhanh hơn Linear Search, nhưng chậm hơn Binary Search.
* **Độ phức tạp không gian:** O(1).
    * Dùng rất ít bộ nhớ, không phụ thuộc vào số phần tử.

### **VII. LƯU Ý QUAN TRỌNG**

* **Yêu cầu:** Danh sách **phải được sắp xếp**.
* **Ứng dụng:**
    * Khi cần tìm kiếm nhanh hơn Linear Search, nhưng danh sách quá lớn để dùng Binary Search (vì Binary Search cần truy
      cập dữ liệu ngẫu nhiên, mà truy cập ngẫu nhiên có thể tốn kém).
    * Phù hợp khi truy cập dữ liệu tuần tự.

### **VIII. CODE VÍ DỤ BẰNG TYPESCRIPT**

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

### **KẾT LUẬN**

Tìm kiếm nhảy là một thuật toán tìm kiếm khá thú vị và hữu ích. Hy vọng bài viết này đã giúp các bạn hiểu rõ hơn về nó.
Chúc các bạn code thành công! 😎
