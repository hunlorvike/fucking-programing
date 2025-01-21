## **🚀 "GIẢI MÃ" THUẬT TOÁN INSERTION SORT: SẮP XẾP CHÈN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán sắp xếp khá thú vị: Insertion Sort (sắp
xếp chèn). Đây là một thuật toán đơn giản, dễ hiểu và thường được dùng trong nhiều tình huống thực tế. Cùng mình "mổ xẻ"
nó nhé!

### **I. INSERTION SORT LÀ GÌ?**

* **Insertion Sort (Sắp xếp chèn):** Là thuật toán sắp xếp dựa trên việc chèn từng phần tử vào đúng vị trí trong phần đã
  sắp xếp của danh sách.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn sắp xếp bài trên tay: bạn lấy từng lá bài và chèn nó vào đúng vị trí trong các lá bài đã được
      sắp xếp.
* **Ưu điểm:**
    * **Đơn giản:** Thuật toán dễ hiểu và dễ cài đặt.
    * **Hiệu quả cho danh sách nhỏ:** Chạy nhanh trên danh sách nhỏ hoặc gần như đã sắp xếp.
    * **In-place:** Không cần dùng thêm nhiều bộ nhớ.
* **Nhược điểm:**
    * **Chậm cho danh sách lớn:** Không hiệu quả với danh sách lớn.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Chia danh sách:** Xem danh sách như có hai phần:
    * Phần đã sắp xếp (ban đầu chỉ có phần tử đầu tiên).
    * Phần chưa sắp xếp (phần còn lại).

2. **Lấy phần tử:** Lấy phần tử đầu tiên từ phần chưa sắp xếp (`key`).

3. **So sánh và di chuyển:**
    * So sánh `key` với các phần tử trong phần đã sắp xếp, đi từ phải sang trái.
    * Nếu gặp phần tử lớn hơn `key`, thì di chuyển phần tử đó sang phải để tạo chỗ trống.

4. **Chèn:** Chèn `key` vào chỗ trống vừa tạo.

5. **Lặp lại:** Lặp lại bước 2, 3 và 4 cho đến khi tất cả phần tử được chèn vào phần đã sắp xếp.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĂN BÁNH**

```
insertionSort(arr):
  n = length(arr)

  FOR i FROM 1 to n-1:
    key = arr[i]
    j = i - 1

    WHILE j >= 0 AND arr[j] > key:
      arr[j+1] = arr[j]
      j = j - 1

    arr[j+1] = key

  return arr
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`n = length(arr)`:** Lấy độ dài của danh sách.
* **`FOR i FROM 1 to n-1`:** Vòng lặp ngoài, duyệt qua các phần tử (trừ phần tử đầu tiên).
* **`key = arr[i]`:** Lấy phần tử hiện tại để chèn (`key`).
* **`j = i - 1`:** Khởi tạo vị trí so sánh trong phần đã sắp xếp.
* **`WHILE j >= 0 AND arr[j] > key`:** Vòng lặp trong, so sánh và di chuyển phần tử lớn hơn `key` sang phải.
* **`arr[j+1] = arr[j]`:** Di chuyển phần tử sang phải.
* **`j = j - 1`:** Di chuyển vị trí so sánh sang trái.
* **`arr[j+1] = key`:** Chèn `key` vào đúng vị trí.
* **`return arr`:** Trả về danh sách đã được sắp xếp.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ TRỰC QUAN)**

Giả sử ta có danh sách: `[12, 11, 13, 5, 6]` và cần sắp xếp tăng dần.

* **Lần 1 (`i=1`):**
    * `key = 11`, so sánh với `12`.
    * Di chuyển `12` sang phải: `[12, 12, 13, 5, 6]`.
    * Chèn `11`: `[11, 12, 13, 5, 6]`.
* **Lần 2 (`i=2`):**
    * `key = 13`, so sánh với `12` và `11` (không cần di chuyển).
    * Chèn `13`: `[11, 12, 13, 5, 6]`.
* **Lần 3 (`i=3`):**
    * `key = 5`, so sánh với `13`, `12`, `11`.
    * Di chuyển `13`, `12`, `11` sang phải: `[11, 12, 13, 13, 6]`.
    * Chèn `5`: `[5, 11, 12, 13, 6]`.
* **Lần 4 (`i=4`):**
    * `key = 6`, so sánh với `13`, `12`, `11`, `5`.
    * Di chuyển `13`, `12`, `11` sang phải: `[5, 11, 11, 12, 13]`.
    * Chèn `6`: `[5, 6, 11, 12, 13]`.

* **Kết quả:** `[5, 6, 11, 12, 13]` (đã sắp xếp).

### **VI. CODE VÍ DỤ BẰNG C#**

```csharp
using System;

public class InsertionSortExample
{
    public static int[] InsertionSort(int[] arr)
    {
        int n = arr.Length;

        for (int i = 1; i < n; i++)
        {
            int key = arr[i];
            int j = i - 1;

            // So sánh và di chuyển các phần tử lớn hơn key sang phải
            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j--;
            }

            // Chèn key vào vị trí đúng
            arr[j + 1] = key;
        }

        return arr;
    }

    public static void Main(string[] args)
    {
        int[] arr = { 12, 11, 13, 5, 6 };
        int[] sortedArr = InsertionSort(arr);

        Console.WriteLine("Mảng đã sắp xếp: " + string.Join(", ", sortedArr));
        // Output: Mảng đã sắp xếp: 5, 6, 11, 12, 13
    }
}
```

### **VII. ĐỘ PHỨC TẠP (ĐỘ NHANH CHẬM CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:** O(n²) (thường chậm hơn các thuật toán sắp xếp khác).
* **Độ phức tạp không gian:** O(1) (không dùng thêm nhiều bộ nhớ).

### **VIII. LƯU Ý QUAN TRỌNG**

* **Hiệu quả với danh sách nhỏ:** Chạy nhanh với danh sách ít phần tử.
* **Ổn định:** Không thay đổi thứ tự các phần tử bằng nhau.
* **Thích hợp cho dữ liệu gần như đã sắp xếp:** Chạy nhanh khi dữ liệu gần như đã được sắp xếp.
* **Không nên dùng cho danh sách lớn:** Hãy dùng các thuật toán khác như Merge Sort, Quick Sort khi cần sắp xếp danh
  sách lớn.

### **KẾT LUẬN**

Insertion Sort là một thuật toán sắp xếp đơn giản, dễ hiểu và có thể dùng trong nhiều tình huống thực tế. Hy vọng qua
bài viết này, các bạn đã hiểu rõ hơn về nó. Chúc các bạn code thành công! 😎
