## **🚀 "GIẢI MÃ" THUẬT TOÁN TÌM KIẾM NHỊ PHÂN: DÀNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay mình sẽ cùng nhau "khám phá" thuật toán tìm kiếm nhị phân (Binary Search). Đây là một
thuật toán cực kỳ quan trọng, giúp bạn tìm kiếm dữ liệu "nhanh như chớp" trong một danh sách đã được sắp xếp. Bắt đầu
thôi!

### **I. TÌM KIẾM NHỊ PHÂN LÀ GÌ?**

* **Tìm kiếm nhị phân (Binary Search):** Là thuật toán tìm kiếm một phần tử trong danh sách đã được sắp xếp bằng cách
  chia đôi danh sách liên tục.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn tìm một từ trong từ điển:
        * Bạn mở trang giữa, nếu từ đó nằm ở trang trước thì bạn tiếp tục mở trang giữa của trang trước.
        * Nếu từ đó ở trang sau thì bạn mở trang giữa của trang sau.
        * Cứ tiếp tục như vậy cho đến khi tìm thấy từ đó.
* **Ưu điểm:**
    * **Nhanh:** Tìm kiếm cực nhanh trên danh sách đã được sắp xếp.
    * **Hiệu quả:** Đặc biệt hiệu quả với danh sách lớn.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Khởi tạo:**
    * Đặt `left` (biến bên trái) ở vị trí đầu tiên của danh sách (index 0).
    * Đặt `right` (biến bên phải) ở vị trí cuối cùng của danh sách.

2. **Lặp:**
    * **Tính `mid` (vị trí ở giữa):** `mid = (left + right) // 2` (lấy phần nguyên).
    * **So sánh:**
        * Nếu giá trị cần tìm (`target`) **nhỏ hơn** giá trị ở giữa (`arr[mid]`): Tìm tiếp ở nửa đầu của danh sách.
            * Đặt `right = mid - 1`.
        * Nếu giá trị cần tìm (`target`) **lớn hơn** giá trị ở giữa (`arr[mid]`): Tìm tiếp ở nửa sau của danh sách.
            * Đặt `left = mid + 1`.
        * Nếu giá trị cần tìm (`target`) **bằng** giá trị ở giữa (`arr[mid]`): Tìm thấy rồi! Trả về `mid`.

3. **Kết thúc:**
    * Nếu `left > right`: Tìm hết rồi mà không thấy => Trả về `-1` (không có phần tử trong danh sách).

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĐỌC TRUYỆN**

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

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`left = 0, right = length(arr) - 1`:** Khởi tạo `left` ở đầu, `right` ở cuối danh sách.
* **`WHILE left <= right`:** Vòng lặp sẽ chạy đến khi nào `left` lớn hơn `right` thì tức là đã tìm hết danh sách rồi.
* **`mid = (left + right) // 2`:** Tính vị trí phần tử ở giữa (chia 2 lấy phần nguyên).
* **`IF target < arr[mid]`:** Nếu giá trị cần tìm nhỏ hơn giá trị ở giữa thì mình sẽ tìm trong nửa đầu.
* **`ELSE IF target > arr[mid]`:** Nếu giá trị cần tìm lớn hơn giá trị ở giữa thì mình sẽ tìm trong nửa sau.
* **`ELSE`:** Nếu giá trị cần tìm bằng giá trị ở giữa thì mình đã tìm thấy rồi, trả về vị trí giữa (`mid`).
* **`RETURN -1`:** Nếu chạy hết vòng lặp mà không tìm thấy thì trả về `-1`.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ DỄ HIỂU)**

Giả sử ta có danh sách đã sắp xếp: `[1, 2, 4, 5, 8]` và cần tìm số `4`.

* **Bước 1:** `left = 0`, `right = 4`, `mid = (0 + 4) // 2 = 2`, `arr[2] = 4`, `target == arr[mid]` (tìm thấy!).
* **Kết quả:** Trả về vị trí `2`.

### **VI. CODE VÍ DỤ BẰNG TYPESCRIPT**

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

### **VII. ĐỘ PHỨC TẠP (ĐỘ NHANH CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:** `O(log n)`.
    * Nghĩa là thời gian tìm kiếm tăng rất chậm khi danh sách lớn lên (n là số phần tử).
    * Rất nhanh đối với danh sách lớn.
* **Độ phức tạp không gian:** `O(1)`.
    * Nghĩa là thuật toán dùng rất ít bộ nhớ (không phụ thuộc vào số lượng phần tử).

### **VIII. LƯU Ý QUAN TRỌNG**

* **Yêu cầu:** Danh sách **phải được sắp xếp** thì thuật toán mới hoạt động đúng.
* **Ứng dụng:** Thường dùng khi cần tìm kiếm nhanh trong danh sách lớn (ví dụ: tìm kiếm từ trong từ điển, tìm kiếm số
  điện thoại trong danh bạ).

### **KẾT LUẬN**

Thuật toán tìm kiếm nhị phân là một "vũ khí" lợi hại trong kho tàng kiến thức của dân code. Hy vọng bài viết này đã giúp
các bạn hiểu rõ hơn về nó. Chúc các bạn thành công! 😎
