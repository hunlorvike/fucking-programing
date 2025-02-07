# Chương 3: Nguyên Tắc SOLID Số 2: OCP - Open/Closed Principle (Nguyên Tắc Đóng Mở) - "Mở Rộng Dễ, Sửa Đổi Khó" - "Thiết Kế" Để "Mở Rộng" Thay Vì "Sửa Đổi"

Chào mừng bạn đến với **Chương 3: Nguyên Tắc SOLID Số 2: OCP - Open/Closed Principle (Nguyên Tắc Đóng Mở)**! Trong
chương này, chúng ta sẽ "khám phá" "nguyên tắc" SOLID thứ hai - OCP - một "kim chỉ nam" "quan trọng" để "thiết kế" các
class **"linh hoạt"**, **"dễ mở rộng"**, nhưng **"hạn chế"** việc **"sửa đổi"** code "cốt lõi", giúp code của bạn trở
nên **"vững chắc"** và **"ít rủi ro"** hơn khi có "thay đổi" yêu cầu.

**Phần 3: Nguyên Tắc SOLID Số 2: OCP - Open/Closed Principle (Nguyên Tắc Đóng Mở) - "Mở Rộng Dễ, Sửa Đổi Khó"**

**3.1. OCP là gì? (Giải thích "dễ hiểu" và "ví dụ minh họa") - "Mở" Cho "Mở Rộng", "Đóng" Cho "Sửa Đổi" - "Linh Hoạt"
và "Ổn Định"**

- **OCP - Open/Closed Principle (Nguyên Tắc Đóng Mở) - "Tuyên Ngôn" "Mở Rộng" và "Ổn Định":**

    - **"Các thực thể phần mềm (classes, modules, functions, v.v.) nên 'mở' cho 'mở rộng', nhưng 'đóng' cho 'sửa đổi' "
      **. Đây là "tuyên ngôn" "đầy triết lý" và "sâu sắc" của OCP.
    - Nói một cách "dễ hiểu" hơn:
        - **"Mở" cho "mở rộng" (Open for extension):** Class của bạn nên được "thiết kế" để có thể **"dễ dàng" "thêm"
          các "chức năng" mới** khi có yêu cầu "mới" phát sinh.
        - **"Đóng" cho "sửa đổi" (Closed for modification):** Khi bạn "thêm" "chức năng" mới, bạn nên **"hạn chế tối đa"
          việc "sửa đổi" code "hiện có"** của class. Thay vào đó, hãy "mở rộng" class bằng cách "thêm" code mới, **"
          không 'đụng chạm' "** vào code đã "hoạt động ổn định".

- **"Vi phạm" OCP - "Sửa Code 'Tùm Lum' " Khi Thêm "Chức Năng Mới" - "Rối Rắm" và "Dễ Gãy":**

    - Hãy tưởng tượng bạn có một class `HinhDang` (Shape) để "vẽ" các hình dạng khác nhau (hình tròn, hình vuông, hình
      tam giác, ...):

      ```csharp
      public class HinhDang // Class "vẽ" hình dạng
      {
          public string LoaiHinhDang { get; set; } // "Loại" hình dạng (ví dụ: "Tron", "Vuong", "TamGiac")

          public void Ve() // Phương thức "vẽ" hình dạng
          {
              if (LoaiHinhDang == "Tron")
              {
                  // Code "vẽ" hình tròn
                  Console.WriteLine("Vẽ hình tròn");
              }
              else if (LoaiHinhDang == "Vuong")
              {
                  // Code "vẽ" hình vuông
                  Console.WriteLine("Vẽ hình vuông");
              }
              else if (LoaiHinhDang == "TamGiac")
              {
                  // Code "vẽ" hình tam giác
                  Console.WriteLine("Vẽ hình tam giác");
              }
              // ... (thêm code "vẽ" các loại hình dạng khác vào đây) ...
          }
      }
      ```

    - Class `HinhDang` này "vi phạm" OCP vì:

        - **"Khó" "mở rộng"** để "hỗ trợ" thêm loại hình dạng mới (ví dụ: hình chữ nhật). Bạn phải **"sửa đổi"** code "
          hiện có" của phương thức `Ve()` (thêm `else if` hoặc `switch case`) - "vi phạm" "nguyên tắc 'mở' cho 'mở
          rộng' ".
        - Khi bạn "sửa đổi" phương thức `Ve()` để "thêm" "chức năng" mới, bạn có thể **"vô tình" "gây ra" các lỗi "không
          mong muốn"** ở các "chức năng" "vẽ" hình dạng cũ (vì bạn đang "đụng chạm" vào code đã "hoạt động ổn định") - "
          vi phạm" "nguyên tắc 'đóng' cho 'sửa đổi' ".

- **"Tuân Thủ" OCP - "Mở Rộng" Bằng "Kế Thừa" và "Interface" - "Thêm 'Nhánh Cây' " Thay Vì "Chặt Cây"**

    - "Giải pháp" OCP là **"thiết kế"** class `HinhDang` theo hướng **"mở rộng"** bằng **"kế thừa" (inheritance)** và *
      *"interface"**.
    - **"Tạo" một interface `IHinhDang`** để "định nghĩa" "hợp đồng" chung cho các hình dạng (ví dụ: phương thức
      `Ve()`).
    - "Tạo" các class **"con" "kế thừa"** từ `IHinhDang` (ví dụ: `HinhTron`, `HinhVuong`, `HinhTamGiac`), mỗi class "
      chuyên trị" "vẽ" một loại hình dạng cụ thể.
    - Class `HinhDang` (hoặc interface `IHinhDang`) sẽ **"đóng"** cho "sửa đổi" - bạn **"không cần"** "sửa đổi" code của
      chúng khi "thêm" loại hình dạng mới.
    - Bạn có thể **"dễ dàng" "mở rộng"** ứng dụng để "hỗ trợ" thêm loại hình dạng mới bằng cách **"thêm" các class "con"
      mới** "kế thừa" từ `IHinhDang`, **"không cần" "sửa đổi" code "cốt lõi"** đã có.

- **Ví dụ minh họa "Vi phạm" OCP và "Tuân Thủ" OCP:**

  (Ví dụ code C# minh họa sự khác biệt giữa class "vi phạm" OCP và các class "tuân thủ" OCP - bạn có thể tự viết code ví
  dụ này để "thực hành" và "thấm nhuần" OCP)

**3.2. "Vấn đề" khi class "khó" "mở rộng" và "dễ" "bị phá vỡ" khi sửa đổi - Code "cứng nhắc" và "mong manh" - "Hậu Quả"
Của "Vi Phạm" OCP**

- **Code "Cứng Nhắc" (Rigidity) - "Khó Uốn Nắn" Theo Yêu Cầu Mới:**

    - Class "vi phạm" OCP thường "khó" "mở rộng" để "đáp ứng" các yêu cầu "mới" phát sinh.
    - Bạn phải **"sửa đổi" code "hiện có"** để "thêm" "chức năng" mới, thay vì chỉ "thêm" code mới.
    - Code trở nên **"cứng nhắc"** (rigid) - "khó" "uốn nắn", "khó" "thay đổi" theo "ý muốn".

- **Code "Mong Manh" (Fragility) - "Dễ 'Vỡ' " Khi "Đụng Chạm" - "Sửa Chỗ Này, Hỏng Chỗ Khác":**

    - Khi bạn "sửa đổi" code "hiện có" của class "vi phạm" OCP, bạn có thể **"vô tình" "gây ra" các lỗi "không mong
      muốn"** (side effects) ở các "chức năng" khác của class.
    - Code trở nên **"mong manh"** (fragile) - "dễ 'vỡ' " khi có bất kỳ "thay đổi" nào.
    - Hiệu ứng "domino" - "một thay đổi nhỏ" có thể "gây ra" "hàng loạt" lỗi "khó lường".

- **"Khó Tái Sử Dụng" (Reduced Reusability):**

    - Class "vi phạm" OCP thường "chứa" quá nhiều "logic" "lẫn lộn" với nhau, làm giảm "tính gắn kết" (cohesion) và "
      tăng" "tính phụ thuộc" (coupling) của class.
    - "Khó" "tách rời" các "chức năng" riêng biệt để "tái sử dụng" ở các "ngữ cảnh" khác nhau.
    - Code trở nên "khó" "lắp ghép" và "tái sử dụng" trong các "module" khác.

- **"Khó Kiểm Thử" (Reduced Testability):**

    - Class "phức tạp" và "mong manh" "khó" "viết unit tests" "đầy đủ" và "tin cậy".
    - "Nguy cơ" "bỏ sót" các "trường hợp" "kiểm thử" quan trọng, "giảm" "chất lượng" code.
    - Unit tests trở nên "khó bảo trì" và "kém hiệu quả" trong việc "đảm bảo" "chất lượng" code.

**3.3. "Giải pháp" OCP - "Thiết Kế" Class "Mở" Cho "Mở Rộng", "Đóng" Cho "Sửa Đổi" - "Mở Rộng" Thay Vì "Sửa Code Gốc"**

- **"Trừu Tượng Hóa" (Abstraction) - "Chìa Khóa" Để "Mở Rộng" và "Ổn Định":**

    - "Giải pháp" OCP "cốt lõi" là **"trừu tượng hóa"** các "chức năng" có thể "thay đổi" hoặc "mở rộng" trong tương lai
      bằng cách sử dụng **Interfaces** hoặc **Abstract Classes**.
    - Interfaces và Abstract Classes "định nghĩa" các **"hợp đồng"** (contracts) hoặc **"khung sườn"** (framework) "
      chung" cho các "chức năng" đó.

- **"Mở Rộng" Chức Năng Bằng "Kế Thừa" (Inheritance) hoặc "Implement Interface" - "Thêm 'Nhánh Mới' " Cho "Cây" Class:**

    - Để "thêm" "chức năng" mới, bạn **"không cần"** "sửa đổi" code "hiện có" của class "trừu tượng" (interface hoặc
      abstract class).
    - Thay vào đó, bạn chỉ cần **"tạo" các class "con" mới** "kế thừa" từ abstract class hoặc "implement" interface,
      và "hiện thực hóa" các "chức năng" "mới" trong các class "con" này.
    - "Mở rộng" "chức năng" bằng cách "thêm" code mới, **"không 'đụng chạm' "** vào code "cốt lõi" đã "ổn định".

- **Code "Gọi" "Chức Năng" Thông Qua "Trừu Tượng" (Interfaces/Abstract Classes) - "Làm Việc" Với "Hợp Đồng" Thay Vì "Chi
  Tiết":**

    - Code "gọi" "chức năng" (client code) sẽ "phụ thuộc" vào **"trừu tượng"** (interfaces hoặc abstract classes) thay
      vì "phụ thuộc trực tiếp" vào các class "cụ thể".
    - Điều này giúp code "client" trở nên **"độc lập"** với các "thay đổi" trong các class "cụ thể", và "linh hoạt" hơn
      trong việc "thay thế" hoặc "mở rộng" "chức năng".

- **Ví dụ "tái cấu trúc" class `HinhDang` "vi phạm" OCP thành các class "tuân thủ" OCP (dùng Interface):**

  (Ví dụ code C# minh họa quá trình "tái cấu trúc" class `HinhDang` - bạn có thể tự viết code ví dụ này để "thực hành"
  OCP)

**3.4. Lợi ích của OCP - Code "linh hoạt", "mở rộng dễ", "ít rủi ro" khi sửa đổi - "Trái Ngọt" Của "Mở Rộng Thay Vì Sửa
Đổi"**

- **Code "Linh Hoạt" và "Dễ Mở Rộng" (Improved Flexibility and Extensibility):**

    - Class được "thiết kế" "mở" cho "mở rộng", giúp bạn "dễ dàng" "thêm" "chức năng" mới mà không cần "sửa đổi" code "
      cốt lõi".
    - Ứng dụng trở nên **"linh hoạt"** hơn trong việc "đáp ứng" các yêu cầu "thay đổi" và "mở rộng" theo thời gian.
    - "Giảm" "thời gian" và "công sức" "phát triển" các "chức năng" mới.

- **Code "Ổn Định" và "Ít Rủi Ro" Khi Sửa Đổi (Improved Stability and Reduced Risk):**

    - Class được "đóng" cho "sửa đổi", giúp bạn **"hạn chế"** việc "sửa đổi" code "hiện có", "tránh" "gây ra" các lỗi "
      không mong muốn" (side effects).
    - Code trở nên **"ổn định"** hơn (stable) - "ít bị vỡ" khi có "thay đổi".
    - "Giảm" "rủi ro" "thất bại" dự án do code "mong manh" và "khó kiểm soát".

- **Code "Dễ Tái Sử Dụng" (Improved Reusability):**

    - Class "trừu tượng" (interface hoặc abstract class) "định nghĩa" "hợp đồng" "rõ ràng" cho các "chức năng", giúp các
      class "con" (concrete classes) "dễ dàng" "thay thế" lẫn nhau và "tái sử dụng" ở các "ngữ cảnh" khác nhau.
    - Code trở nên **"mô-đun hóa" tốt hơn**, "dễ" "lắp ghép" và "xây dựng" các ứng dụng "lớn mạnh" và "phức tạp".

**Tổng Kết Chương 3:**

- Bạn đã "khám phá" **Nguyên Tắc SOLID Số 2: OCP - Open/Closed Principle (Nguyên Tắc Đóng Mở)** - "kim chỉ nam" cho
  việc "thiết kế" class "linh hoạt" và "ổn định".
    - "Hiểu" được "ý nghĩa" và "tầm quan trọng" của OCP - "mở" cho "mở rộng", "đóng" cho "sửa đổi".
    - "Nhận diện" các "vấn đề" khi class "vi phạm" OCP (code "cứng nhắc", "mong manh", "khó tái sử dụng", "khó kiểm
      thử").
    - Học cách "áp dụng" OCP bằng "trừu tượng hóa" (Interfaces, Abstract Classes) và "kế thừa" để "mở rộng" "chức
      năng" "linh hoạt" mà không "sửa đổi" code "cốt lõi".
    - "Thấy" được các "lợi ích" "vàng mười" của OCP (code "linh hoạt", "dễ mở rộng", "ổn định", "tái sử dụng tốt",
      v.v.).

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Nguyên Tắc SOLID Số 3: LSP - Liskov Substitution Principle (Nguyên Tắc Thay Thế
Liskov) - "Con Trai Ra Con Trai"**. Chúng ta sẽ "mổ xẻ" "nguyên tắc" LSP "thú vị" này, và học cách "thiết kế" "hệ thống
kế thừa" (inheritance hierarchies) "chắc chắn", "tin cậy", và "không gây 'bất ngờ' " khi "thay thế" class cha bằng class
con.

Bạn có câu hỏi nào về Nguyên Tắc OCP này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng bạn" "
làm chủ" SOLID Principles.

