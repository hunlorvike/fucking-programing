## **🚀 "GIẢI MÃ" THUẬT TOÁN MERGE SORT: SẮP XẾP TRỘN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán sắp xếp rất mạnh mẽ: Merge Sort (sắp
xếp trộn). Đây là một thuật toán "chia để trị" cực kỳ hiệu quả, thường được dùng trong các ứng dụng thực tế. Cùng mình "
mổ xẻ" nó nhé!

### **I. MERGE SORT LÀ GÌ?**

* **Merge Sort (Sắp xếp trộn):** Là thuật toán sắp xếp dựa trên kỹ thuật "chia để trị" (divide and conquer).
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn chia một công việc lớn thành các công việc nhỏ hơn, giải quyết từng công việc nhỏ rồi "trộn" lại
      kết quả.
* **Ưu điểm:**
    * **Hiệu quả:** Chạy nhanh ngay cả trên danh sách lớn.
    * **Ổn định:** Không làm thay đổi thứ tự các phần tử bằng nhau.
    * **Đảm bảo hiệu suất:** Độ phức tạp thời gian luôn là O(n log n).
* **Nhược điểm:**
    * **Tốn bộ nhớ:** Cần thêm bộ nhớ để lưu các mảng con.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Chia (Divide):**
    * Chia danh sách cần sắp xếp thành hai nửa (trái và phải).
    * Tiếp tục chia đôi đến khi mỗi nửa chỉ còn một phần tử (hoặc rỗng).

2. **Sắp xếp (Conquer):**
    * Các nửa có một phần tử được xem là đã sắp xếp.

3. **Trộn (Merge):**
    * Gộp (merge) hai nửa đã sắp xếp lại thành một mảng lớn hơn bằng cách so sánh và chèn từng phần tử vào đúng vị trí.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĐỌC TRUYỆN**

```
mergeSort(arr):
  n = length(arr)

  IF n <= 1:
    RETURN arr  // Dừng khi có 0 hoặc 1 phần tử

  mid = floor(n / 2)
  leftHalf = arr[0...mid]
  rightHalf = arr[mid...n]

  leftSorted = mergeSort(leftHalf)
  rightSorted = mergeSort(rightHalf)

  RETURN merge(leftSorted, rightSorted)

merge(left, right):
  i = 0, j = 0, result = []

  WHILE i < length(left) AND j < length(right):
    IF left[i] < right[j]:
      result.append(left[i])
      i = i + 1
    ELSE:
      result.append(right[j])
      j = j + 1

  result.append(left[i...])
  result.append(right[j...])
  RETURN result
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`mergeSort(arr)`:** Hàm chính của thuật toán.
* **`n = length(arr)`:** Lấy độ dài danh sách.
* **`IF n <= 1`:** Nếu danh sách có 0 hoặc 1 phần tử thì đã được sắp xếp, trả về luôn.
* **`mid = floor(n / 2)`:** Tìm vị trí giữa danh sách.
* **`leftHalf = arr[0...mid]`:** Tách danh sách thành nửa trái.
* **`rightHalf = arr[mid...n]`:** Tách danh sách thành nửa phải.
* **`leftSorted = mergeSort(leftHalf)`:** Đệ quy sắp xếp nửa trái.
* **`rightSorted = mergeSort(rightHalf)`:** Đệ quy sắp xếp nửa phải.
* **`RETURN merge(leftSorted, rightSorted)`:** Trộn hai nửa đã sắp xếp.
* **`merge(left, right)`:** Hàm trộn hai danh sách đã sắp xếp.
* **`i = 0, j = 0, result = []`:** Khởi tạo các biến.
* **`WHILE i < length(left) AND j < length(right)`:** Vòng lặp so sánh các phần tử từ hai danh sách.
* **`IF left[i] < right[j]`:** Nếu phần tử trái nhỏ hơn, chèn vào `result`.
* **`ELSE`:** Nếu phần tử phải nhỏ hơn, chèn vào `result`.
* **`result.append(left[i...])`:** Chèn các phần tử còn lại của nửa trái vào `result`.
* **`result.append(right[j...])`:** Chèn các phần tử còn lại của nửa phải vào `result`.
* **`RETURN result`:** Trả về mảng kết quả.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ TRỰC QUAN)**

Giả sử ta có danh sách: `[5, 1, 4, 2, 8]` và cần sắp xếp tăng dần.

1. **Chia:**
    * `[5, 1, 4, 2, 8]` -> `[5, 1], [4, 2, 8]`
    * `[5, 1]` -> `[5], [1]`
    * `[4, 2, 8]` -> `[4], [2, 8]`
    * `[2, 8]` -> `[2], [8]`
2. **Sắp xếp (đệ quy):** Các mảng có một phần tử đã được sắp xếp.
3. **Trộn:**
    * `[5], [1]` -> `[1, 5]`
    * `[4], [2]` -> `[2, 4]`
    * `[2, 4], [8]` -> `[2, 4, 8]`
    * `[1, 5], [2, 4, 8]` -> `[1, 2, 4, 5, 8]`

* **Kết quả:** `[1, 2, 4, 5, 8]` (đã sắp xếp).

### **VI. CODE VÍ DỤ BẰNG C# (DÀNH CHO DÂN .NET)**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class MergeSortExample
{
    public static int[] MergeSort(int[] arr)
    {
        if (arr.Length <= 1)
        {
            return arr;
        }

        int mid = arr.Length / 2;
        int[] leftHalf = arr.Take(mid).ToArray();
        int[] rightHalf = arr.Skip(mid).ToArray();

        return Merge(MergeSort(leftHalf), MergeSort(rightHalf));
    }

    public static int[] Merge(int[] left, int[] right)
    {
        List<int> result = new List<int>();
        int i = 0, j = 0;

        while (i < left.Length && j < right.Length)
        {
            if (left[i] < right[j])
            {
                result.Add(left[i++]);
            }
            else
            {
                result.Add(right[j++]);
            }
        }

        result.AddRange(left.Skip(i));
        result.AddRange(right.Skip(j));
        return result.ToArray();
    }

    public static void Main(string[] args)
    {
        int[] arr = { 5, 1, 4, 2, 8 };
        int[] sortedArr = MergeSort(arr);

        Console.WriteLine("Mảng đã sắp xếp: " + string.Join(", ", sortedArr));
        // Output: Mảng đã sắp xếp: 1, 2, 4, 5, 8
    }
}
```

### **VII. ĐỘ PHỨC TẠP (ĐỘ NHANH CHẬM CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:** O(n log n) (cho mọi trường hợp).
* **Độ phức tạp không gian:** O(n) (cần bộ nhớ để lưu các mảng con).

### **VIII. CẢI TIẾN (MỘT SỐ MẸO)**

* **Bộ nhớ bổ sung:** Cố gắng tái sử dụng bộ nhớ thay vì tạo mới trong mỗi lần đệ quy.
* **Tối ưu hóa trộn:** Sử dụng các thuật toán khác để trộn nếu danh sách nhỏ.

### **IX. LƯU Ý QUAN TRỌNG**

* **Thuật toán mạnh mẽ:** Merge Sort rất hiệu quả và thường được sử dụng trong các ứng dụng thực tế.
* **Thích hợp cho danh sách lớn:** Chạy tốt khi danh sách có nhiều phần tử.
* **Ổn định:** Không thay đổi thứ tự của các phần tử bằng nhau.
* **Không "in-place":** Cần thêm bộ nhớ để lưu các mảng con.

### **KẾT LUẬN**

Merge Sort là một thuật toán sắp xếp rất quan trọng, thường được sử dụng trong nhiều tình huống thực tế. Hy vọng qua bài
viết này, các bạn đã hiểu rõ hơn về cách nó hoạt động. Chúc các bạn thành công! 😎
