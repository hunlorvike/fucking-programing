## **🚀 "GIẢI MÃ" THUẬT TOÁN TÌM KIẾM TUYẾN TÍNH: DÀNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán tìm kiếm cơ bản nhất: Tìm kiếm tuyến
tính (Linear Search). Tuy đơn giản nhưng nó lại là nền tảng để hiểu các thuật toán phức tạp hơn đấy. Bắt đầu thôi!

### **I. TÌM KIẾM TUYẾN TÍNH LÀ GÌ?**

* **Tìm kiếm tuyến tính (Linear Search):** Là thuật toán tìm kiếm một phần tử trong danh sách bằng cách duyệt qua từng
  phần tử một, từ đầu đến cuối.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn tìm một món đồ trong tủ đồ: bạn phải tìm từ ngăn đầu tiên đến ngăn cuối cùng cho đến khi tìm
      thấy món đồ đó.
* **Ưu điểm:**
    * **Đơn giản:** Cực kỳ dễ hiểu và dễ cài đặt.
    * **Không yêu cầu gì:** Có thể dùng cho cả danh sách đã sắp xếp và chưa sắp xếp.
* **Nhược điểm:**
    * **Chậm:** Khi danh sách lớn, tìm kiếm có thể rất chậm.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Khởi tạo:**
    * Đặt `index = 0` (bắt đầu từ vị trí đầu tiên).

2. **Lặp:**
    * Duyệt qua từng phần tử trong danh sách (từ `index = 0` đến cuối danh sách).

3. **So sánh:**
    * So sánh giá trị của phần tử hiện tại (`arr[index]`) với giá trị cần tìm (`target`).
        * Nếu `arr[index] == target`: Tìm thấy rồi! Trả về `index`.
        * Nếu không bằng thì tiếp tục.

4. **Kết thúc:**
    * Nếu duyệt hết danh sách mà không tìm thấy => Trả về `-1` (không có phần tử trong danh sách).

### **III. MÃ GIẢ (PSEUDOCODE) - SIÊU DỄ HIỂU**

```
linear_search(arr, target):
  n = length(arr)

  FOR i FROM 0 to n-1:
    IF arr[i] == target:
      RETURN i

  RETURN -1
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHÉ!)**

* **`n = length(arr)`:** Lấy độ dài của danh sách.
* **`FOR i FROM 0 to n-1`:** Vòng lặp duyệt qua từng phần tử, từ vị trí 0 đến n-1 (vị trí cuối cùng).
* **`IF arr[i] == target`:** So sánh giá trị tại vị trí i với giá trị cần tìm.
* **`RETURN i`:** Nếu tìm thấy thì trả về vị trí `i`.
* **`RETURN -1`:** Nếu duyệt hết danh sách mà không tìm thấy thì trả về `-1`.

### **V. VÍ DỤ MINH HỌA (THỰC TẾ)**

Giả sử ta có danh sách: `[5, 1, 4, 2, 8]` và cần tìm số `2`.

* **Bước 1:** `index = 0`, `arr[0] = 5`, `5 != 2`.
* **Bước 2:** `index = 1`, `arr[1] = 1`, `1 != 2`.
* **Bước 3:** `index = 2`, `arr[2] = 4`, `4 != 2`.
* **Bước 4:** `index = 3`, `arr[3] = 2`, `2 == 2` (Tìm thấy rồi!).
* **Kết quả:** Trả về vị trí `3`.

### **VI. ĐỘ PHỨC TẠP (ĐỘ NHANH CHẬM CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:**
    * **Trường hợp xấu nhất:** O(n) (duyệt hết danh sách).
    * **Trường hợp tốt nhất:** O(1) (tìm thấy ở đầu danh sách).
* **Độ phức tạp không gian:** O(1) (không cần thêm bộ nhớ).

### **VII. LƯU Ý QUAN TRỌNG**

* **Đơn giản nhưng không hiệu quả:** Linear Search rất dễ nhưng lại chậm khi danh sách lớn.
* **Không cần danh sách sắp xếp:** Có thể dùng cho cả danh sách đã sắp xếp và chưa sắp xếp.
* **Không nên dùng cho danh sách lớn:** Nếu danh sách lớn thì nên dùng các thuật toán khác như Binary Search, Jump
  Search.

### **VIII. CODE VÍ DỤ BẰNG TYPESCRIPT**

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

### **KẾT LUẬN**

Thuật toán tìm kiếm tuyến tính là một thuật toán cơ bản mà mọi sinh viên IT đều cần biết. Tuy nó không phải là thuật
toán nhanh nhất nhưng lại rất dễ hiểu và có thể dùng được trong nhiều trường hợp đơn giản. Chúc các bạn thành công! 😎
