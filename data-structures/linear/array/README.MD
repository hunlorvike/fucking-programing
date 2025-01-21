## **🚀 "GIẢI MÃ" MẢNG (ARRAY): CẤU TRÚC DỮ LIỆU CƠ BẢN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "mổ xẻ" một cấu trúc dữ liệu cực kỳ cơ bản và quan trọng: Mảng (Array). Đây là một trong những "viên gạch" đầu tiên khi bạn học lập trình. Cùng mình khám phá nhé!

### **I. MẢNG (ARRAY) LÀ GÌ?**

-   **Mảng (Array):** Là một dãy các phần tử có cùng kiểu dữ liệu, được lưu trữ liên tiếp trong bộ nhớ.
-   **Nó hoạt động như thế nào?**
    -   Giống như một dãy số nhà trên một con đường: các nhà đều có số thứ tự (index) và nằm cạnh nhau.
-   **Đặc điểm:**
    -   **Tuyến tính:** Các phần tử được sắp xếp theo một thứ tự nhất định.
    -   **Cùng kiểu dữ liệu:** Tất cả phần tử phải cùng kiểu (ví dụ: toàn số nguyên hoặc toàn chữ).
    -   **Liên tiếp:** Các phần tử được lưu trữ liên tiếp nhau trong bộ nhớ.
    -   **Index:** Truy cập phần tử bằng index (số thứ tự), bắt đầu từ 0.
    -   **Kích thước cố định:** Kích thước thường không thay đổi sau khi khai báo (nhưng có một số ngôn ngữ dùng mảng động).

### **II. ƯU ĐIỂM CỦA MẢNG (NHỮNG ĐIỂM "ĐÁNG YÊU")**

-   **Truy cập nhanh:** Truy cập phần tử bằng index cực nhanh (độ phức tạp O(1)).
-   **Đơn giản:** Dễ hiểu, dễ dùng.

### **III. NHƯỢC ĐIỂM CỦA MẢNG (NHỮNG ĐIỂM "KHÓ CHỊU")**

-   **Kích thước cố định:** Khó thay đổi kích thước sau khi khai báo.
-   **Chèn/xóa chậm:** Chèn hoặc xóa ở giữa mảng thì cần di chuyển nhiều phần tử (độ phức tạp O(n)).

### **IV. ỨNG DỤNG CỦA MẢNG (ĐƯỢC DÙNG Ở ĐÂU?)**

-   **Lưu dữ liệu:** Lưu danh sách, bảng điểm, danh sách sản phẩm, ...
-   **Nền tảng:** Dùng để xây các cấu trúc khác (stack, queue, hash table, ...).
-   **Thuật toán:** Dùng trong nhiều thuật toán (sắp xếp, tìm kiếm).

### **V. VÍ DỤ MINH HỌA (C#)**

```csharp
using System;

public class ArrayExample
{
    public static void Main(string[] args)
    {
        // Khai báo một mảng số nguyên
        int[] numbers = { 1, 2, 3, 4, 5 };

        // Truy cập phần tử thứ 3 (index 2)
        Console.WriteLine($"Phần tử thứ 3 là: {numbers[2]}"); // Output: Phần tử thứ 3 là: 3

        // Thay đổi giá trị phần tử thứ 2 (index 1)
        numbers[1] = 10;

        // In mảng
        Console.Write("Mảng sau khi thay đổi: ");
        foreach (int num in numbers)
        {
            Console.Write(num + " ");
        }
         // Output: Mảng sau khi thay đổi: 1 10 3 4 5
    }
}
```

### **VI. MỘT SỐ ĐIỀU BỔ SUNG (ĐỂ HIỂU RÕ HƠN)**

1.  **Mảng đa chiều:**
    -   Mảng 2 chiều (ma trận), 3 chiều,... dùng để biểu diễn dữ liệu phức tạp hơn.
    -   **Ví dụ (mảng 2 chiều):**

```csharp
  using System;
    public class Array2D
    {
       public static void Main(string[] args)
        {
           int[,] matrix = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
           };

           Console.WriteLine($"Phần tử ở hàng 2, cột 3: {matrix[1, 2]}"); // Output: Phần tử ở hàng 2, cột 3: 6
        }
    }
```

2.  **Mảng động:**
    -   Một số ngôn ngữ (như C#, Java, Python) có "mảng động" (dynamic array) - có thể thay đổi kích thước tự động.
    -   **Ví dụ (C# dùng List):**

```csharp
  using System;
    using System.Collections.Generic;

        public class DynamicArray
        {
           public static void Main(string[] args)
             {
                   List<int> numbers = new List<int> { 1, 2, 3 };
                    numbers.Add(4);
                    Console.Write("Mảng động: ");
                    foreach (int num in numbers)
                     {
                          Console.Write(num + " ");
                     } // Output: Mảng động: 1 2 3 4
            }
        }
```

### **VII. KẾT LUẬN (TỔNG KẾT)**

Mảng là cấu trúc dữ liệu cơ bản, dễ hiểu và rất quan trọng trong lập trình. Nắm vững kiến thức về mảng sẽ giúp bạn xây dựng nền tảng vững chắc để học các cấu trúc dữ liệu khác. Chúc các bạn code thành công! 😎
