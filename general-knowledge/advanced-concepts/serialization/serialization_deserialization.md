## **🚀 "GIẢI MÃ" SERIALIZATION VÀ DESERIALIZATION: BIẾN DỮ LIỆU THÀNH "HÀNH LÝ" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai khái niệm cực kỳ quan trọng: Serialization (Tuần
tự hóa) và Deserialization (Giải tuần tự hóa). Nghe có vẻ "cao siêu" nhưng thực ra rất gần gũi và cần thiết khi bạn làm
việc với dữ liệu. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé!
Let's go!

### **I. SERIALIZATION VÀ DESERIALIZATION LÀ GÌ? (BIẾN DỮ LIỆU THÀNH GÌ?)**

- **Serialization (Tuần tự hóa):** Là quá trình biến một _đối tượng_ (object) phức tạp thành một chuỗi byte hoặc định
  dạng khác (JSON, XML, ...) để có thể lưu trữ hoặc truyền tải.
    - Giống như bạn "đóng gói" đồ đạc vào vali để mang đi.
- **Deserialization (Giải tuần tự hóa):** Là quá trình ngược lại: biến chuỗi byte hoặc định dạng đã lưu về lại thành
  _đối tượng_ ban đầu để dùng.
    - Giống như bạn "mở vali" ra và lấy đồ đạc ra dùng.
- **Tóm lại:**
    - **Serialization:** Biến object -> chuỗi/byte.
    - **Deserialization:** Biến chuỗi/byte -> object.

### **II. TẠI SAO CẦN SERIALIZATION VÀ DESERIALIZATION? (VÌ MÁY TÍNH CHỈ HIỂU "BYTE"!)**

- **Hệ thống mạng chỉ hiểu byte/chuỗi:** Khi gửi dữ liệu qua mạng, cần phải biến dữ liệu thành byte hoặc chuỗi.
- **Serialization:** Biến object phức tạp thành chuỗi/byte để gửi đi.
- **Deserialization:** Biến chuỗi/byte nhận được thành object để dùng.
- **Ví dụ:**
    - Một object chứa thông tin người dùng (tên, tuổi, địa chỉ) cần được gửi đi.
    - Serialization sẽ biến object thành chuỗi JSON để gửi qua mạng.
    - Deserialization sẽ biến chuỗi JSON nhận được thành object để chương trình dùng.

### **III. CÁC ĐỊNH DẠNG PHỔ BIẾN (CÁC KIỂU "HÀNH LÝ")**

1. **JSON (JavaScript Object Notation):** Đơn giản, dễ đọc, dùng nhiều trong web API.
2. **XML (Extensible Markup Language):** Dùng cho các hệ thống lớn, phức tạp.
3. **YAML (YAML Ain't Markup Language):** Cấu trúc rõ ràng, dùng cho cấu hình.
4. **Binary (Nhị phân):** Dùng khi cần tốc độ cao, dung lượng nhỏ.

### **IV. SERIALIZATION VÀ DESERIALIZATION HOẠT ĐỘNG NHƯ THẾ NÀO (CÁCH "ĐÓNG GÓI" VÀ "MỞ GÓI")**

- **Serialization:**
    1. **Mã hóa (Encoding):** Chuyển dữ liệu thành chuỗi byte.
    2. **Tạo định dạng (Formatting):** Chuyển byte thành định dạng cụ thể (JSON, XML, ...).
- **Deserialization:**
    1. **Giải mã (Decoding):** Tách chuỗi byte thành thông tin có nghĩa.
    2. **Xây dựng lại (Reconstruction):** Tạo lại object từ thông tin đó.

### **V. VÍ DỤ MINH HỌA (C# - JSON)**

```csharp
using System;
using System.IO;
using System.Text.Json;
using System.Text.Json.Serialization;

public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string City { get; set; }
}

public class SerializationExample
{
    public static void Main(string[] args)
    {
        // Đối tượng cần serialize
        Person person = new Person
        {
            Name = "Alice",
            Age = 25,
            City = "New York"
        };

        // Serialization (chuyển đối tượng thành chuỗi JSON)
        string jsonString = JsonSerializer.Serialize(person);
        Console.WriteLine($"Serialized JSON: {jsonString}");
        // Output: Serialized JSON: {"Name":"Alice","Age":25,"City":"New York"}

        // Deserialization (chuyển đổi chuỗi JSON thành đối tượng)
        Person personObj = JsonSerializer.Deserialize<Person>(jsonString);

        Console.WriteLine($"Deserialized Object:");
        Console.WriteLine($"Name: {personObj.Name}");  // Output: Deserialized Object: Name: Alice
        Console.WriteLine($"Age: {personObj.Age}"); // Output: Age: 25
        Console.WriteLine($"City: {personObj.City}");  // Output: City: New York
    }
}
```

**Giải thích:**

- **`JsonSerializer.Serialize(person)`:** Chuyển object `person` thành chuỗi JSON.
- **`JsonSerializer.Deserialize<Person>(jsonString)`:** Chuyển chuỗi JSON về object `Person`.

### **VI. LƯU Ý QUAN TRỌNG (ĐỪNG QUÊN NHÉ!)**

- **Bảo mật:** Dữ liệu serialized có thể bị đánh cắp, nên cần mã hóa khi truyền tải.
- **Tương thích:** Các hệ thống có thể dùng định dạng khác nhau, nên cần thống nhất format (ví dụ: JSON).
- **Kích thước:** Dữ liệu serialized có thể lớn hơn object, cần tối ưu khi cần tiết kiệm dung lượng (dùng nhị phân).

### **VII. KẾT LUẬN (TỔNG KẾT)**

Serialization và Deserialization là quá trình quan trọng để biến dữ liệu thành dạng có thể truyền tải và lưu trữ. Hy
vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày của mình. Chúc các bạn
code thành công! 😎
