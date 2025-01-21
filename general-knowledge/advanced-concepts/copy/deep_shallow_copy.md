## **🚀 "GIẢI MÃ" SHALLOW COPY VS DEEP COPY: SAO CHÉP DỮ LIỆU ĐÚNG CÁCH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai khái niệm rất quan trọng trong lập trình: Shallow
Copy (sao chép nông) và Deep Copy (sao chép sâu). Nghe có vẻ "lý thuyết" nhưng thực ra rất dễ hiểu và cần thiết khi bạn
làm việc với dữ liệu phức tạp. Cùng mình "mổ xẻ" nó nhé!

### **I. SHALLOW COPY VS DEEP COPY LÀ GÌ? (SAO CHÉP KIỂU NÀO?)**

- **Shallow Copy (Sao chép nông):** Tạo bản sao mới của đối tượng, nhưng _chỉ sao chép địa chỉ bộ nhớ_ của các thành
  phần bên trong.
    - Giống như khi bạn photocopy một cuốn sách: bản copy chỉ là "bản sao" của các trang, không phải là "cuốn sách mới".
- **Deep Copy (Sao chép sâu):** Tạo bản sao mới của đối tượng, và _sao chép toàn bộ nội dung_ của các thành phần bên
  trong.
    - Giống như khi bạn in lại một cuốn sách: bạn có một cuốn sách hoàn toàn mới, không liên quan đến cuốn cũ.
- **Tóm lại:**
    - **Shallow copy:** "Sao chép nhanh" nhưng có thể ảnh hưởng đến dữ liệu gốc.
    - **Deep copy:** "Sao chép kỹ" nhưng tốn thời gian và bộ nhớ hơn.

### **II. SHALLOW COPY (SAO CHÉP NÔNG) - "NHANH NHƯNG KHÔNG CHẮC"**

#### **2.1. ĐỊNH NGHĨA (SAO CHÉP KIỂU GÌ?)**

- Tạo bản sao mới, nhưng chỉ copy địa chỉ bộ nhớ của các thành phần bên trong.
- Bản sao và bản gốc "cùng trỏ" đến dữ liệu thật.

#### **2.2. VÍ DỤ MINH HỌA (C#)**

```csharp
using System;
using System.Collections.Generic;

public class MyClass
{
    public List<int> data;

    public MyClass(List<int> data)
    {
        this.data = data;
    }
}

public class ShallowCopyExample
{
    public static void Main(string[] args)
    {
        List<int> originalData = new List<int> { 1, 2, 3 };
        MyClass original = new MyClass(originalData);

        // Shallow Copy
        MyClass shallowCopy = new MyClass(original.data);

        // Thay đổi dữ liệu trong original
        original.data.Add(4);

        Console.WriteLine("Original data: " + string.Join(", ", original.data));   // Output: Original data: 1, 2, 3, 4
        Console.WriteLine("Shallow copy data: " + string.Join(", ", shallowCopy.data)); // Output: Shallow copy data: 1, 2, 3, 4
    }
}
```

**Giải thích:**

- Thay đổi `original.data` thì `shallowCopy.data` cũng bị thay đổi.
- Vì `shallowCopy.data` chỉ tham chiếu đến danh sách của `original.data`.

#### **2.3. ƯU ĐIỂM (ĐIỂM "ĐÁNG YÊU")**

- **Nhanh hơn:** Chỉ copy tham chiếu, không copy toàn bộ dữ liệu.
- **Tiết kiệm bộ nhớ:** Không cần dùng nhiều bộ nhớ.

#### **2.4. NHƯỢC ĐIỂM (ĐIỂM "KHÓ CHỊU")**

- **Ảnh hưởng đến dữ liệu gốc:** Thay đổi bản sao có thể làm thay đổi dữ liệu gốc.
- **Không an toàn:** Với các cấu trúc phức tạp có tham chiếu lồng nhau.

#### **2.5. KHI NÀO NÊN DÙNG (KHI NÀO "NÊN" NHANH?)**

- Khi sao chép đối tượng đơn giản.
- Khi không cần bản sao độc lập, có thể chấp nhận ảnh hưởng đến dữ liệu gốc.

### **III. DEEP COPY (SAO CHÉP SÂU) - "CHẬM MÀ CHẮC"**

#### **3.1. ĐỊNH NGHĨA (SAO CHÉP KIỂU GÌ?)**

- Tạo bản sao mới, và copy toàn bộ dữ liệu bên trong.
- Bản sao và bản gốc hoàn toàn độc lập, không chia sẻ dữ liệu.

#### **3.2. VÍ DỤ MINH HỌA (C#)**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class MyClass
{
    public List<int> data;

    public MyClass(List<int> data)
    {
        this.data = data.ToList(); // Tạo bản sao mới của danh sách
    }
}

public class DeepCopyExample
{
    public static void Main(string[] args)
    {
        List<int> originalData = new List<int> { 1, 2, 3 };
        MyClass original = new MyClass(originalData);

        // Deep Copy (bằng cách sao chép list)
        MyClass deepCopy = new MyClass(original.data);

        // Thay đổi dữ liệu trong original
        original.data.Add(4);

        Console.WriteLine("Original data: " + string.Join(", ", original.data));   // Output: Original data: 1, 2, 3, 4
        Console.WriteLine("Deep copy data: " + string.Join(", ", deepCopy.data));  // Output: Deep copy data: 1, 2, 3
    }
}
```

**Giải thích:**

- Thay đổi `original.data` _không_ ảnh hưởng đến `deepCopy.data`.
- Vì `deepCopy.data` đã có bản sao dữ liệu riêng.
- Cách copy ở đây là dùng `ToList()` để tạo list mới.

#### **3.3. ƯU ĐIỂM (ĐIỂM "ĐÁNG YÊU")**

- **An toàn:** Thay đổi bản sao không ảnh hưởng đến dữ liệu gốc.
- **Độc lập:** Tạo ra bản sao hoàn toàn riêng biệt.

#### **3.4. NHƯỢC ĐIỂM (ĐIỂM "KHÓ CHỊU")**

- **Chậm hơn:** Phải copy hết dữ liệu.
- **Tốn bộ nhớ:** Dùng nhiều bộ nhớ hơn.

#### **3.5. KHI NÀO NÊN DÙNG (KHI NÀO "NÊN" KỸ?)**

- Khi cần bản sao độc lập, không ảnh hưởng đến dữ liệu gốc.
- Khi dùng cấu trúc phức tạp có tham chiếu lồng nhau.

### **IV. VÍ DỤ THỰC TẾ (SO SÁNH SHALLOW VÀ DEEP COPY)**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

 public class Example
        {
            public static void Main(string[] args)
            {
                 // Shallow copy
               List<int> originalList = new List<int>{1, 2, 3};
                List<int> shallowCopiedList = originalList;
                originalList.Add(4);
                Console.WriteLine("Shallow Copy: ");
                 Console.WriteLine("Original: "+string.Join(", ", originalList));  // Output: Original: 1, 2, 3, 4
                Console.WriteLine("Shallow Copy: "+string.Join(", ", shallowCopiedList)); // Output: Shallow Copy: 1, 2, 3, 4
                // Deep copy
                originalList = new List<int>{1, 2, 3};
                List<int> deepCopiedList = originalList.ToList(); // Tạo bản copy mới
                originalList.Add(4);
                 Console.WriteLine("Deep Copy: ");
                 Console.WriteLine("Original: "+string.Join(", ", originalList));  // Output: Original: 1, 2, 3, 4
                Console.WriteLine("Deep Copy: "+string.Join(", ", deepCopiedList)); // Output: Deep Copy: 1, 2, 3
            }
        }
```

### **V. KẾT LUẬN (TỔNG KẾT)**

- **Shallow Copy:** Nhanh nhưng có thể gây lỗi khi dùng với cấu trúc dữ liệu phức tạp.
- **Deep Copy:** Chậm hơn nhưng an toàn, không ảnh hưởng đến dữ liệu gốc.
- **Chọn loại copy phù hợp:** Dựa vào tình huống cụ thể để chọn cho phù hợp.

Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về shallow copy và deep copy. Chúc các bạn code thành công! 😎
