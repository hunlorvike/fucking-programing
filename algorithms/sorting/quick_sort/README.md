## **🚀 "GIẢI MÃ" THUẬT TOÁN QUICK SORT: SẮP XẾP NHANH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một trong những thuật toán sắp xếp được yêu thích
nhất: Quick Sort (sắp xếp nhanh). Đây là một thuật toán "chia để trị" cực kỳ hiệu quả, thường được dùng trong các thư
viện sắp xếp chuẩn. Cùng mình "mổ xẻ" nó nhé!

### **I. QUICK SORT LÀ GÌ?**

* **Quick Sort (Sắp xếp nhanh):** Là thuật toán sắp xếp dựa trên kỹ thuật "chia để trị" (divide and conquer), chọn một
  phần tử làm "pivot" rồi phân chia và đệ quy.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn chia một công việc lớn thành các phần nhỏ hơn, giải quyết từng phần rồi kết hợp lại.
* **Ưu điểm:**
    * **Nhanh:** Chạy rất nhanh trong trường hợp trung bình.
    * **Hiệu quả:** Phù hợp với các danh sách lớn.
    * **In-place:** Ít tốn bộ nhớ hơn Merge Sort.
* **Nhược điểm:**
    * **Có thể chậm:** Chạy chậm trong trường hợp xấu nhất (danh sách đã được sắp xếp hoặc gần sắp xếp).
    * **Không ổn định:** Có thể thay đổi thứ tự các phần tử bằng nhau.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Chọn Pivot:**
    * Chọn một phần tử trong danh sách làm "pivot" (phần tử trụ).
    * Có nhiều cách chọn, ví dụ: chọn phần tử giữa, chọn ngẫu nhiên, ...
2. **Phân chia (Partition):**
    * Chia danh sách thành 2 phần:
        * Phần bên trái: Các phần tử nhỏ hơn hoặc bằng `pivot`.
        * Phần bên phải: Các phần tử lớn hơn `pivot`.
3. **Sắp xếp đệ quy:**
    * Gọi đệ quy `quickSort` cho phần bên trái và bên phải.
4. **Kết hợp:**
    * Kết hợp phần bên trái, `pivot` và phần bên phải thành danh sách đã sắp xếp.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĐANG CHƠI GAME**

```
quickSort(arr):
  n = length(arr)

  IF n <= 1:
    RETURN arr  // Dừng khi có 0 hoặc 1 phần tử

  pivot = arr[floor(n / 2)]  // Chọn phần tử giữa làm pivot
  left = [], right = []

  FOR i FROM 0 to n-1:
    IF arr[i] < pivot:
      left.append(arr[i])
    ELSE IF arr[i] > pivot:
      right.append(arr[i])

  RETURN quickSort(left) + [pivot] + quickSort(right) // Kết hợp và đệ quy
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`quickSort(arr)`:** Hàm chính của thuật toán.
* **`n = length(arr)`:** Lấy độ dài của danh sách.
* **`IF n <= 1`:** Nếu danh sách có 0 hoặc 1 phần tử thì đã được sắp xếp, trả về luôn.
* **`pivot = arr[floor(n / 2)]`:** Chọn phần tử giữa làm `pivot`.
* **`left = [], right = []`:** Tạo 2 danh sách con để lưu trữ các phần tử nhỏ hơn và lớn hơn `pivot`.
* **`FOR i FROM 0 to n-1`:** Vòng lặp duyệt qua các phần tử.
* **`IF arr[i] < pivot`:** Nếu phần tử nhỏ hơn `pivot` thì thêm vào danh sách `left`.
* **`ELSE IF arr[i] > pivot`:** Nếu phần tử lớn hơn `pivot` thì thêm vào danh sách `right`.
* **`RETURN quickSort(left) + [pivot] + quickSort(right)`:** Đệ quy sắp xếp danh sách `left` và `right`, kết hợp với
  `pivot` để tạo thành danh sách đã sắp xếp.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ TRỰC QUAN)**

Giả sử ta có danh sách: `[5, 1, 4, 2, 8]` và cần sắp xếp tăng dần.

1. **Chọn pivot và phân chia:**
    * `pivot = 4`.
    * `left = [1, 2]`.
    * `right = [5, 8]`.

2. **Đệ quy (sắp xếp từng nửa):**
    * `quickSort([1, 2])` -> `[1, 2]` (đã sắp xếp).
    * `quickSort([5, 8])` -> `[5, 8]` (đã sắp xếp).

3. **Kết hợp:**
    * `[1, 2] + [4] + [5, 8]` -> `[1, 2, 4, 5, 8]`.

* **Kết quả:** `[1, 2, 4, 5, 8]` (đã sắp xếp).

### **VI. CODE VÍ DỤ BẰNG C#**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class QuickSortExample
{
    public static int[] QuickSort(int[] arr)
    {
        if (arr.Length <= 1)
        {
            return arr;
        }

        int pivot = arr[arr.Length / 2];
        List<int> left = new List<int>();
        List<int> right = new List<int>();

        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] < pivot)
            {
                left.Add(arr[i]);
            }
            else if (arr[i] > pivot)
            {
                right.Add(arr[i]);
            }
        }

        return QuickSort(left.ToArray())
            .Concat(new int[] { pivot })
            .Concat(QuickSort(right.ToArray()))
            .ToArray();
    }

    public static void Main(string[] args)
    {
        int[] arr = { 5, 1, 4, 2, 8 };
        int[] sortedArr = QuickSort(arr);

        Console.WriteLine("Mảng đã sắp xếp: " + string.Join(", ", sortedArr));
        // Output: Mảng đã sắp xếp: 1, 2, 4, 5, 8
    }
}
```

### **VII. ĐỘ PHỨC TẠP (ĐỘ NHANH CHẬM CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:**
    * **Trường hợp tốt nhất:** O(n log n)
    * **Trường hợp trung bình:** O(n log n)
    * **Trường hợp xấu nhất:** O(n²)
* **Độ phức tạp không gian:** O(log n) (do đệ quy).

### **VIII. CẢI TIẾN (MỘT SỐ MẸO)**

* **Chọn pivot thông minh:** Chọn pivot ngẫu nhiên hoặc dùng "median-of-three" để tránh trường hợp xấu nhất.
* **Tối ưu hóa đệ quy:** Sử dụng "tail recursion" để tối ưu đệ quy.

### **IX. LƯU Ý QUAN TRỌNG**

* **Nhanh trong thực tế:** Quick Sort rất nhanh trong trường hợp trung bình.
* **Chọn pivot quan trọng:** Cách chọn `pivot` ảnh hưởng lớn đến hiệu suất.
* **Không ổn định:** Thứ tự các phần tử bằng nhau có thể bị thay đổi.

### **KẾT LUẬN**

Quick Sort là một thuật toán sắp xếp rất quan trọng và được sử dụng rộng rãi trong thực tế. Hy vọng qua bài viết này,
các bạn đã hiểu rõ hơn về cách nó hoạt động. Chúc các bạn code thành công! 😎
