## **🚀 "GIẢI MÃ" TẬP HỢP (SET): CẤU TRÚC DỮ LIỆU "KHÔNG TRÙNG LẶP" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một cấu trúc dữ liệu rất thú vị: Tập hợp (Set). Nghe có vẻ "lạ" nhưng thực ra rất hữu ích khi bạn cần quản lý các phần tử không trùng lặp. Cùng mình "mổ xẻ" nó nhé!

### **I. TẬP HỢP (SET) LÀ GÌ?**

-   **Tập hợp (Set):** Là cấu trúc dữ liệu phi tuyến tính, chứa các phần tử _không trùng lặp_ và không có thứ tự cố định.
-   **Nó hoạt động như thế nào?**
    -   Giống như một túi đựng đồ mà mỗi món đồ chỉ có một cái duy nhất.
-   **Đặc điểm:**
    -   **Phi tuyến tính:** Không có thứ tự cố định giữa các phần tử.
    -   **Không trùng lặp:** Mỗi phần tử chỉ xuất hiện một lần.
    -   **Thao tác tập hợp:** Hỗ trợ các phép hợp, giao, hiệu, ...
    -   **Kiểm tra thuộc tính:** Kiểm tra xem một phần tử có trong tập hợp không.

### **II. ƯU ĐIỂM CỦA TẬP HỢP (NHỮNG ĐIỂM "ĐÁNG YÊU")**

-   **Thao tác tập hợp nhanh:** Hợp, giao, hiệu, kiểm tra thuộc tính thường nhanh (O(1)).
-   **Loại bỏ trùng lặp:** Tự động loại bỏ các phần tử trùng lặp, đảm bảo tính duy nhất.

### **III. NHƯỢC ĐIỂM CỦA TẬP HỢP (NHỮNG ĐIỂM "KHÓ CHỊU")**

-   **Không có thứ tự:** Các phần tử không có thứ tự rõ ràng.
-   **Khó duyệt:** Duyệt qua các phần tử có thể không hiệu quả nếu tập hợp lớn.

### **IV. ỨNG DỤNG CỦA TẬP HỢP (ĐƯỢC DÙNG Ở ĐÂU?)**

-   **Lý thuyết tập hợp:** Tìm giao, hợp, hiệu của các tập hợp số, chữ, ...
-   **Loại bỏ trùng lặp:** Loại bỏ các phần tử trùng lặp trong danh sách, email,...
-   **Kiểm tra thuộc tính:** Kiểm tra xem một phần tử có trong tập hợp không (từ điển, dữ liệu người dùng).

### **V. VÍ DỤ MINH HỌA (C#)**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class SetExample
{
   public class SetCollection<T>
        {
            private HashSet<T> items;

            public SetCollection(IEnumerable<T> initialItems = null)
            {
                items = initialItems == null ? new HashSet<T>() : new HashSet<T>(initialItems);
            }

            // Thêm một phần tử vào tập hợp
            public void Add(T element)
            {
                items.Add(element);
            }

            // Kiểm tra thuộc tính
            public bool Has(T element)
            {
                return items.Contains(element);
            }

            // Hợp của hai tập hợp
            public SetCollection<T> Union(SetCollection<T> otherSet)
            {
                SetCollection<T> unionSet = new SetCollection<T>();
                foreach (var item in items)
                {
                    unionSet.Add(item);
                }
                foreach (var item in otherSet.items)
                {
                  unionSet.Add(item);
                 }
                return unionSet;
            }

             // Giao của hai tập hợp
            public SetCollection<T> Intersection(SetCollection<T> otherSet)
            {
                SetCollection<T> intersectionSet = new SetCollection<T>();
                foreach (var item in items)
                {
                    if (otherSet.Has(item))
                    {
                         intersectionSet.Add(item);
                    }
                }
                 return intersectionSet;
            }

           // Hiệu của hai tập hợp
              public SetCollection<T> Difference(SetCollection<T> otherSet)
            {
                SetCollection<T> differenceSet = new SetCollection<T>();
                   foreach (var item in items)
                {
                    if (!otherSet.Has(item))
                    {
                         differenceSet.Add(item);
                    }
                }
                return differenceSet;
            }
             // Hiển thị tập hợp
            public void Display()
            {
                Console.WriteLine(string.Join(", ", items));
            }
        }
    public static void Main(string[] args)
    {
        SetCollection<int> setA = new SetCollection<int>(new int[] { 1, 2, 3, 4, 5 });
        SetCollection<int> setB = new SetCollection<int>(new int[] { 4, 5, 6, 7, 8 });

        // Hợp của hai tập hợp
        Console.Write("Hợp của hai tập hợp: ");
        SetCollection<int> unionSet = setA.Union(setB);
        unionSet.Display(); // Output: Hợp của hai tập hợp: 1, 2, 3, 4, 5, 6, 7, 8

        // Giao của hai tập hợp
        Console.Write("Giao của hai tập hợp: ");
        SetCollection<int> intersectionSet = setA.Intersection(setB);
        intersectionSet.Display(); // Output: Giao của hai tập hợp: 4, 5

        // Hiệu của hai tập hợp
         Console.Write("Hiệu của hai tập hợp: ");
        SetCollection<int> differenceSet = setA.Difference(setB);
        differenceSet.Display(); // Output: Hiệu của hai tập hợp: 1, 2, 3
    }
}
```

**Giải thích:**

-   **`SetCollection<T>`:** Lớp biểu diễn tập hợp, dùng `HashSet<T>` để lưu các phần tử.
    -   **`Add(T element)`:** Thêm phần tử vào tập hợp.
    -   **`Has(T element)`:** Kiểm tra xem có phần tử trong tập hợp không.
    -   **`Union(SetCollection<T> otherSet)`:** Trả về hợp của 2 tập hợp.
    -   **`Intersection(SetCollection<T> otherSet)`:** Trả về giao của 2 tập hợp.
    -   **`Difference(SetCollection<T> otherSet)`:** Trả về hiệu của 2 tập hợp.
    -   **`Display()`:** In tập hợp.

### **VI. BỔ SUNG (MỘT SỐ ĐIỀU THÚ VỊ)**

-   **`HashSet<T>`:** C# có sẵn class `HashSet<T>` để làm tập hợp, các bạn có thể dùng nó thay vì viết lại.
-   **Thứ tự:** Các phần tử không có thứ tự cố định, nếu cần thứ tự thì hãy dùng các cấu trúc dữ liệu khác.

### **VII. KẾT LUẬN (TỔNG KẾT)**

Tập hợp là một cấu trúc dữ liệu rất hữu ích, giúp bạn quản lý các phần tử không trùng lặp một cách hiệu quả. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể dùng nó trong nhiều tình huống thực tế. Chúc các bạn code thành công! 😎
