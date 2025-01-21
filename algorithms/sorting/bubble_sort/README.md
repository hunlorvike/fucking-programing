## **🚀 "GIẢI MÃ" THUẬT TOÁN BUBBLE SORT: SẮP XẾP NỔI BỌT CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán sắp xếp kinh điển: Bubble Sort (sắp xếp
nổi bọt). Nghe tên có vẻ "mềm mại" nhưng thực ra nó là nền tảng cho nhiều thuật toán sắp xếp phức tạp hơn đấy. Cùng
mình "mổ xẻ" nó nhé!

### **I. BUBBLE SORT LÀ GÌ?**

* **Bubble Sort (Sắp xếp nổi bọt):** Là thuật toán sắp xếp đơn giản, dựa trên việc so sánh và hoán đổi các cặp phần tử
  liền kề.
* **Nó hoạt động như thế nào?**
    * Giống như các bọt khí trong nước: các phần tử lớn (hoặc nhỏ, tùy vào thứ tự sắp xếp) sẽ "nổi" lên dần về cuối danh
      sách.
* **Ưu điểm:**
    * **Dễ hiểu:** Thuật toán rất trực quan, dễ hình dung.
    * **Dễ cài đặt:** Code không quá phức tạp.
* **Nhược điểm:**
    * **Chậm:** Không hiệu quả với danh sách lớn.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Duyệt danh sách:** Bắt đầu từ đầu danh sách.
2. **So sánh cặp phần tử:** So sánh hai phần tử liền kề nhau.
3. **Hoán đổi:** Nếu chúng không đúng thứ tự (ví dụ: phần tử trước lớn hơn phần tử sau khi sắp xếp tăng dần), hoán đổi
   chúng.
4. **Lặp lại:** Duyệt, so sánh, và hoán đổi đến khi không còn hoán đổi nào xảy ra (tức là danh sách đã được sắp xếp).

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĂN CƠM**

```
bubbleSort(arr):
  n = length(arr)

  FOR i FROM 0 to n-1:
    swapped = false
    FOR j FROM 0 to n-i-2:
      IF arr[j] > arr[j+1]:
        swap(arr[j], arr[j+1])
        swapped = true
    IF not swapped:
      break
  return arr
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHA!)**

* **`n = length(arr)`:** Lấy số lượng phần tử trong danh sách.
* **`FOR i FROM 0 to n-1`:** Vòng lặp ngoài, duyệt qua từng phần tử trong danh sách.
* **`swapped = false`:** Biến để kiểm tra xem có hoán đổi nào xảy ra không.
* **`FOR j FROM 0 to n-i-2`:** Vòng lặp trong, so sánh và hoán đổi các phần tử liền kề (duyệt từ đầu đến `n-i-2` vì các
  phần tử ở cuối đã được sắp xếp).
* **`IF arr[j] > arr[j+1]`:** So sánh hai phần tử.
* **`swap(arr[j], arr[j+1])`:** Hoán đổi hai phần tử.
* **`swapped = true`:** Báo hiệu đã có hoán đổi.
* **`IF not swapped`:** Nếu không có hoán đổi nào, danh sách đã được sắp xếp, dừng lại.
* **`return arr`:** Trả về danh sách đã được sắp xếp.

### **V. VÍ DỤ MINH HỌA (CỰC KỲ TRỰC QUAN)**

Giả sử ta có danh sách: `[5, 1, 4, 2, 8]` và cần sắp xếp tăng dần.

* **Lần 1:**
    * `[5, 1, 4, 2, 8]` -> `[1, 5, 4, 2, 8]`
    * `[1, 5, 4, 2, 8]` -> `[1, 4, 5, 2, 8]`
    * `[1, 4, 5, 2, 8]` -> `[1, 4, 2, 5, 8]`
    * `[1, 4, 2, 5, 8]` -> `[1, 4, 2, 5, 8]`
* **Lần 2:**
    * `[1, 4, 2, 5, 8]` -> `[1, 4, 2, 5, 8]`
    * `[1, 4, 2, 5, 8]` -> `[1, 2, 4, 5, 8]`
    * `[1, 2, 4, 5, 8]` -> `[1, 2, 4, 5, 8]`
* **Lần 3:**
    * `[1, 2, 4, 5, 8]` -> `[1, 2, 4, 5, 8]`
    * `[1, 2, 4, 5, 8]` -> `[1, 2, 4, 5, 8]`
* **Lần 4:**
    * `[1, 2, 4, 5, 8]` -> `[1, 2, 4, 5, 8]`

* **Kết quả:** `[1, 2, 4, 5, 8]` (đã sắp xếp).

### **VI. CODE VÍ DỤ BẰNG C#**

```csharp
using System;

public class BubbleSortExample
{
    public static int[] BubbleSort(int[] arr)
    {
        int n = arr.Length;

        for (int i = 0; i < n; i++)
        {
            bool swapped = false;
            for (int j = 0; j < n - i - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    // Hoán đổi
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            if (!swapped) break; // Nếu không có hoán đổi, dừng sớm
        }

        return arr;
    }

    public static void Main(string[] args)
    {
        int[] arr = { 5, 1, 4, 2, 8 };
        int[] sortedArr = BubbleSort(arr);

        Console.WriteLine("Mảng đã sắp xếp: " + string.Join(", ", sortedArr));
        // Output: Mảng đã sắp xếp: 1, 2, 4, 5, 8
    }
}
```

### **VII. ĐỘ PHỨC TẠP (ĐỘ NHANH CHẬM CỦA THUẬT TOÁN)**

* **Độ phức tạp thời gian:**
    * **Trường hợp xấu nhất:** O(n²) (khi danh sách ngược chiều).
    * **Trường hợp tốt nhất:** O(n) (khi danh sách đã sắp xếp, có tối ưu dừng sớm).
* **Độ phức tạp không gian:** O(1) (không dùng thêm nhiều bộ nhớ).

### **VIII. CẢI TIẾN (MỘT SỐ MẸO)**

* **Cờ hoán đổi:** Biến `swapped` giúp dừng sớm thuật toán khi danh sách đã được sắp xếp.
* **Sắp xếp một phần:** Chỉ duyệt qua phần chưa được sắp xếp của danh sách.

### **IX. LƯU Ý QUAN TRỌNG**

* **Đơn giản nhưng không nhanh:** Bubble Sort dễ hiểu nhưng không hiệu quả với danh sách lớn.
* **Dễ cài đặt:** Phù hợp để học các thuật toán sắp xếp cơ bản.
* **Không nên dùng cho danh sách lớn:** Hãy dùng các thuật toán khác như Merge Sort, Quick Sort khi cần sắp xếp danh
  sách lớn.

### **KẾT LUẬN**

Bubble Sort là một thuật toán sắp xếp rất cơ bản, giúp bạn hiểu rõ hơn về cách các thuật toán sắp xếp hoạt động. Tuy
không phải là thuật toán nhanh nhất, nhưng nó là một bước quan trọng để bạn tiến xa hơn trong thế giới thuật toán. Chúc
các bạn học tốt! 😎
