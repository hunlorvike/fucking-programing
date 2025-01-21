## **🚀 "GIẢI MÃ" IMMUTABLE VS MUTABLE: "KHIÊN" VÀ "KIẾM" TRONG LẬP TRÌNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai khái niệm quan trọng trong lập trình: Immutable (
bất biến) và Mutable (biến đổi). Nghe có vẻ "triết lý" nhưng thực ra rất gần gũi và cần thiết cho dân code chúng mình
đấy. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. IMMUTABLE VS MUTABLE LÀ GÌ? (DỮ LIỆU "CỨNG" HAY "MỀM"?)**

- **Immutable (Bất biến):** Là các đối tượng mà giá trị của chúng _không thể thay đổi_ sau khi được tạo.
    - Giống như một viên gạch: khi đã tạo ra thì không thể "biến hình" được.
- **Mutable (Biến đổi):** Là các đối tượng mà giá trị của chúng _có thể thay đổi_ sau khi được tạo.
    - Giống như cục đất sét: bạn có thể nhào nặn, thay đổi hình dạng của nó.
- **Tóm lại:**
    - **Immutable:** "Cứng" - không thay đổi.
    - **Mutable:** "Mềm" - có thể thay đổi.

### **II. IMMUTABLE (BẤT BIẾN) - "ĐỨNG YÊN MỘT CHỖ"**

#### **2.1. ĐỊNH NGHĨA (NÓ KHÔNG ĐƯỢC ĐỔI)**

- Giá trị của đối tượng không thay đổi sau khi tạo.
- Nếu muốn thay đổi, phải tạo đối tượng mới.

#### **2.2. VÍ DỤ (C#)**

- **`string`:** Chuỗi ký tự.
- **`int`, `float`, `bool`, ...:** Các kiểu dữ liệu số.
- **`struct`:** Cấu trúc (nếu các field của nó là immutable).

```csharp
using System;

public class ImmutableExample
{
    public static void Main(string[] args)
    {
        string s = "Hello";
        Console.WriteLine($"Địa chỉ của s trước khi thay đổi: {s.GetHashCode()}");  // địa chỉ trước
        s = s + " World!";
        Console.WriteLine($"Địa chỉ của s sau khi thay đổi: {s.GetHashCode()}");  // địa chỉ sau khi thay đổi
        // Kết quả sẽ là 2 địa chỉ khác nhau
    }
}
```

**Giải thích:**

- Dù ta có nối chuỗi, thì bản chất C# đã tạo ra một chuỗi mới, nên địa chỉ ô nhớ của `s` đã thay đổi.

#### **2.3. ƯU ĐIỂM (ĐIỂM "ĐÁNG YÊU")**

- **An toàn:** Dữ liệu không bị thay đổi ngoài ý muốn.
- **Dễ đoán:** Giá trị luôn ổn định, code dễ hiểu.
- **Tối ưu:** Dễ dùng cho cache, đa luồng.

#### **2.4. NHƯỢC ĐIỂM (ĐIỂM "KHÓ CHỊU")**

- **Tốn bộ nhớ:** Phải tạo đối tượng mới khi thay đổi.
- **Có thể chậm:** Tạo đối tượng mới có thể tốn thời gian.

#### **2.5. KHI NÀO NÊN DÙNG? (KHI NÀO "NÊN" CỨNG?)**

- Khi dữ liệu không cần thay đổi sau khi tạo.
- Khi cần sự an toàn, dễ dự đoán.
- Trong môi trường đa luồng để tránh xung đột dữ liệu.

### **III. MUTABLE (BIẾN ĐỔI) - "NHÀO NẶN THOẢI MÁI"**

#### **3.1. ĐỊNH NGHĨA (NÓ ĐƯỢC PHÉP ĐỔI)**

- Giá trị của đối tượng có thể thay đổi trực tiếp.
- Không cần tạo đối tượng mới khi thay đổi.

#### **3.2. VÍ DỤ (C#)**

- **`List<T>`:** Danh sách.
- **`Dictionary<K, V>`:** Từ điển.
- **Class:** Các class tự tạo (nếu các property không immutable).

```csharp
using System;
using System.Collections.Generic;

 public class MutableExample
    {
        public static void Main(string[] args)
        {
            List<int> myList = new List<int> { 1, 2, 3 };
             Console.WriteLine($"Địa chỉ của mylist trước khi thay đổi: {myList.GetHashCode()}"); // in địa chỉ trước
            myList.Add(4); // Thêm phần tử
             Console.WriteLine($"Địa chỉ của mylist sau khi thay đổi: {myList.GetHashCode()}");  // địa chỉ sau khi thay đổi
             // 2 địa chỉ ô nhớ giống nhau
        }
    }

```

**Giải thích:**

- Ta thêm phần tử vào `myList`, nhưng địa chỉ ô nhớ của `myList` vẫn giữ nguyên.

#### **3.3. ƯU ĐIỂM (ĐIỂM "ĐÁNG YÊU")**

- **Nhanh:** Thay đổi giá trị trực tiếp, không tạo đối tượng mới.
- **Linh hoạt:** Dễ dàng thay đổi dữ liệu.

#### **3.4. NHƯỢC ĐIỂM (ĐIỂM "KHÓ CHỊU")**

- **Dễ gây lỗi:** Dữ liệu dễ bị thay đổi không mong muốn.
- **Khó dự đoán:** Không chắc chắn giá trị sẽ thay đổi như thế nào.
- **Khó dùng trong đa luồng:** Dễ gây ra xung đột dữ liệu.

#### **3.5. KHI NÀO NÊN DÙNG? (KHI NÀO "NÊN" MỀM?)**

- Khi cần thay đổi dữ liệu thường xuyên.
- Khi cần hiệu suất cao khi thay đổi dữ liệu.
- Khi không cần quan tâm nhiều đến tính an toàn của dữ liệu.

### **IV. SO SÁNH IMMUTABLE VÀ MUTABLE (ĐỂ THẤY RÕ SỰ KHÁC BIỆT)**

| Tính chất      | Immutable                               | Mutable                                  |
|----------------|-----------------------------------------|------------------------------------------|
| **Thay đổi**   | Không thể                               | Có thể                                   |
| **Ví dụ**      | string, int, struct                     | List, Dictionary, Class                  |
| **An toàn**    | An toàn, không lo thay đổi ngoài ý muốn | Nguy cơ lỗi khi thay đổi không kiểm soát |
| **Bộ nhớ**     | Tạo đối tượng mới khi thay đổi          | Sửa đổi trực tiếp                        |
| **Hiệu suất**  | Có thể chậm hơn khi thay đổi            | Thường nhanh hơn khi thay đổi            |
| **Dễ sử dụng** | Dễ kiểm tra, dễ đoán                    | Khó dự đoán, dễ lỗi                      |

### **V. LƯU Ý QUAN TRỌNG (ĐỂ TRÁNH "SẬP BẪY")**

- **Ưu tiên Immutable:** Nếu có thể, hãy dùng immutable cho an toàn.
- **Cẩn thận với Mutable:** Khi truyền mutable object vào hàm, hàm có thể thay đổi dữ liệu gốc.
- **Dùng `copy()` để tránh thay đổi gốc:** Khi muốn thay đổi, hãy tạo bản sao rồi thay đổi bản sao.

**Ví dụ (C#):**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Example
{
  static void ModifyList(List<int> listToModify)
        {
            listToModify.Add(4);
        }

    public static void Main(string[] args)
    {
           //Mutable
           List<int> myList = new List<int> { 1, 2, 3 };
           ModifyList(myList);  // Thay đổi trực tiếp danh sách myList
           Console.WriteLine("List mutable: "+string.Join(", ", myList));
           //Output: List mutable: 1, 2, 3, 4

            //Immutable
            List<int> myList2 = new List<int> { 1, 2, 3 };
            List<int> newList = myList2.ToList(); // Tạo bản copy
            ModifyList(newList);
            Console.WriteLine("List immutable: "+string.Join(", ", myList2));
            // Output: List immutable: 1, 2, 3
            Console.WriteLine("New List: "+string.Join(", ", newList));
            //  Output: New List: 1, 2, 3, 4
    }
}
```

### **VI. KẾT LUẬN (TỔNG KẾT)**

Immutable và Mutable là hai khái niệm quan trọng trong lập trình. Việc hiểu rõ chúng sẽ giúp bạn viết code an toàn, hiệu
quả và dễ bảo trì hơn. Chúc các bạn code thành công! 😎
