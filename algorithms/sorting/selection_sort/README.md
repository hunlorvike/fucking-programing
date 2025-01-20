## **🚀 "GIẢI MÃ" THUẬT TOÁN SELECTION SORT: SẮP XẾP CHỌN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán sắp xếp đơn giản mà hiệu quả: Selection
Sort (sắp xếp chọn). Tuy không phải là thuật toán nhanh nhất, nhưng nó lại rất dễ hiểu và là nền tảng cho nhiều thuật
toán khác. Cùng mình "mổ xẻ" nó nhé!

### **I. SELECTION SORT LÀ GÌ?**

* **Selection Sort (Sắp xếp chọn):** Là thuật toán sắp xếp bằng cách tìm phần tử nhỏ nhất (hoặc lớn nhất) trong danh
  sách chưa sắp xếp, rồi hoán đổi nó với phần tử đầu tiên của danh sách chưa sắp xếp.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn đang chọn ra người thấp nhất (hoặc cao nhất) trong một hàng, rồi đưa người đó lên đầu hàng, và
      tiếp tục chọn người thấp nhất trong những người còn lại.
* **Ưu điểm:**
    * **Đơn giản:** Dễ hiểu và dễ cài đặt.
    * **In-place:** Không cần dùng thêm nhiều bộ nhớ.
* **Nhược điểm:**
    * **Chậm:** Không hiệu quả với danh sách lớn.
    * **Luôn duyệt toàn bộ:** Luôn phải duyệt hết các phần tử, không dừng sớm được.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Tìm phần tử nhỏ nhất (hoặc lớn nhất):** Duyệt qua danh sách chưa sắp xếp, tìm phần tử nhỏ nhất (hoặc lớn nhất).
2. **Hoán đổi:** Hoán đổi phần tử nhỏ nhất (hoặc lớn nhất) tìm được với phần tử đầu tiên của danh sách chưa sắp xếp.
3. **Lặp lại:** Lặp lại bước 1 và 2 cho phần còn lại của danh sách, mỗi lần bỏ qua các phần tử đã sắp xếp.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĂN KẸO**

```
selectionSort(arr):
  n = length(arr)

  FOR i FROM 0 to n-2:
    minIndex = i
    FOR j FROM i+1 to n-1:
      IF arr[j] < arr[minIndex]:
        minIndex = j
    IF minIndex != i:
      swap(arr[i], arr[minIndex])
  RETURN arr
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`n = length(arr)`:** Lấy số lượng phần tử của danh sách.
* **`FOR i FROM 0 to n-2`:** Vòng lặp ngoài, duyệt qua từng phần tử (trừ phần tử cuối cùng).
* **`minIndex = i`:** Giả sử phần tử hiện tại (tại vị trí `i`) là nhỏ nhất.
* **`FOR j FROM i+1 to n-1`:** Vòng lặp trong, tìm phần tử nhỏ nhất trong phần còn lại của danh sách.
* **`IF arr[j] < arr[minIndex]`:** Nếu tìm thấy phần tử nhỏ hơn, cập nhật `minIndex`.
* **`IF minIndex != i`:** Nếu phần tử nhỏ nhất không phải là phần tử hiện tại, hoán đổi chúng.
* **`RETURN arr`:** Trả về danh sách đã sắp xếp.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ TRỰC QUAN)**

Giả sử ta có danh sách: `[64, 25, 12, 22, 11]` và cần sắp xếp tăng dần.

* **Lần 1 (`i=0`):**
    * Tìm min: `11` tại vị trí `4`.
    * Hoán đổi: `[11, 25, 12, 22, 64]`.
* **Lần 2 (`i=1`):**
    * Tìm min (từ vị trí 1): `12` tại vị trí `2`.
    * Hoán đổi: `[11, 12, 25, 22, 64]`.
* **Lần 3 (`i=2`):**
    * Tìm min (từ vị trí 2): `22` tại vị trí `3`.
    * Hoán đổi: `[11, 12, 22, 25, 64]`.
* **Lần 4 (`i=3`):**
    * Tìm min (từ vị trí 3): `25` tại vị trí `3`.
    * Hoán đổi: `[11, 12, 22, 25, 64]`.

* **Kết quả:** `[11, 12, 22, 25, 64]` (đã sắp xếp).

### **VI. CODE VÍ DỤ BẰNG C#**

```csharp
using System;

public class SelectionSortExample
{
    public static int[] SelectionSort(int[] arr)
    {
        int n = arr.Length;

        for (int i = 0; i < n - 1; i++)
        {
            int minIndex = i;
            for (int j = i + 1; j < n; j++)
            {
                if (arr[j] < arr[minIndex])
                {
                    minIndex = j;
                }
            }

            // Hoán đổi nếu tìm thấy phần tử nhỏ hơn
            if (minIndex != i)
            {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }

        return arr;
    }

    public static void Main(string[] args)
    {
        int[] arr = { 64, 25, 12, 22, 11 };
        int[] sortedArr = SelectionSort(arr);

        Console.WriteLine("Mảng đã sắp xếp: " + string.Join(", ", sortedArr));
        // Output: Mảng đã sắp xếp: 11, 12, 22, 25, 64
    }
}
```

### **VII. ĐỘ PHỨC TẠP (ĐỘ NHANH CHẬM CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:** O(n²) (luôn phải duyệt hết các phần tử).
* **Độ phức tạp không gian:** O(1) (không dùng thêm bộ nhớ).

### **VIII. LƯU Ý QUAN TRỌNG**

* **Đơn giản nhưng không nhanh:** Selection Sort dễ hiểu, dễ cài đặt nhưng không hiệu quả với danh sách lớn.
* **Không có trường hợp tốt nhất:** Luôn duyệt hết các phần tử dù danh sách đã được sắp xếp gần như hoàn chỉnh.
* **In-place:** Không cần dùng thêm nhiều bộ nhớ.
* **Không ổn định:** Thứ tự của các phần tử bằng nhau có thể bị thay đổi.
* **Không nên dùng cho danh sách lớn:** Hãy dùng các thuật toán khác như Merge Sort, Quick Sort khi cần sắp xếp danh
  sách lớn.

### **KẾT LUẬN**

Selection Sort là một thuật toán sắp xếp rất cơ bản, giúp bạn hiểu rõ hơn về cách các thuật toán sắp xếp hoạt động. Tuy
không phải là thuật toán nhanh nhất, nhưng nó là một bước quan trọng để bạn tiến xa hơn trong thế giới thuật toán. Chúc
các bạn code thành công! 😎
