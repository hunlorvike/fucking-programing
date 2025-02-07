# Chương 5: Nguyên Tắc SOLID Số 4: ISP - Interface Segregation Principle (Nguyên Tắc Phân Tách Interface) - "Interface 'Vừa Vặn' "** - "Không 'Ép' Class 'Làm' Những Gì Không Cần"

Chào mừng bạn đến với **Chương 5: Nguyên Tắc SOLID Số 4: ISP - Interface Segregation Principle (Nguyên Tắc Phân Tách
Interface)**! Trong chương này, chúng ta sẽ "khám phá" "nguyên tắc" SOLID thứ tư - ISP - một "kim chỉ nam" "quan trọng"
để "thiết kế" **Interfaces** **"tinh gọn"**, **"vừa vặn"** với "nhu cầu" của client (class "dùng" interface), "tránh" "
ép" client phải "phụ thuộc" vào các "phương thức" "không cần thiết".

**Phần 5: Nguyên Tắc SOLID Số 4: ISP - Interface Segregation Principle (Nguyên Tắc Phân Tách Interface) - "Interface '
Vừa Vặn' "**

**5.1. ISP là gì? (Giải thích "dễ hiểu" và "ví dụ minh họa") - "Interface 'Vừa Vặn' " - "Không 'Ép' 'Khách Hàng' Dùng
Đồ 'Thừa' "**

- **ISP - Interface Segregation Principle (Nguyên Tắc Phân Tách Interface) - "Tuyên Ngôn" "Interface 'Vừa Vặn' ":**

    - **"Không nên ép client (class 'dùng' interface) phải phụ thuộc vào các phương thức (methods) mà nó không sử dụng"
      **. Đây là "tuyên ngôn" "đanh thép" và "chính xác" của ISP.
    - Nói một cách "dễ hiểu" hơn: **"Thay vì 'nhồi nhét' quá nhiều 'phương thức' vào một interface 'to bự', hãy 'chia
      nhỏ' interface đó thành nhiều interface 'nhỏ gọn' hơn, 'chuyên biệt' hơn"**. Mỗi interface "nhỏ" chỉ "chứa" các "
      phương thức" "thực sự" "cần thiết" cho một "nhóm" client cụ thể.

- **"Interface 'Quá Béo' " (Vi Phạm ISP) - "Ôm Đồm" Quá Nhiều "Phương Thức" - "Khó Dùng" và "Ít Linh Hoạt":**

    - Hãy tưởng tượng bạn có một interface `IPrintableDocument` (Tài Liệu Có Thể In) "quá béo", "ôm đồm" quá nhiều "
      phương thức" "không liên quan" đến nhau:

      ```csharp
      public interface IPrintableDocument // Interface "Tài Liệu Có Thể In" "quá béo"
      {
          void Print();           // Phương thức "In" tài liệu
          void Scan();            // Phương thức "Scan" tài liệu (??? - không liên quan đến "In")
          void Fax();             // Phương thức "Fax" tài liệu (??? - càng không liên quan đến "In")
          void Copy();            // Phương thức "Copy" tài liệu (??? - lạc quẻ hoàn toàn với "In")
          string GetDocumentContent(); // Phương thức "Lấy nội dung" tài liệu (có vẻ "hợp lý" hơn, nhưng vẫn "không liên quan trực tiếp" đến "In")
      }
      ```

    - Interface `IPrintableDocument` "quá béo" này "vi phạm" ISP vì:

        - **"Ép" các class "implement" interface phải "hiện thực hóa" (implement) các "phương thức" mà chúng "không cần"
          hoặc "không có ý nghĩa"**. Ví dụ: class `BaoCao` (Report) chỉ cần "chức năng" "In" (`Print()`) và "Lấy nội
          dung" (`GetDocumentContent()`), **"không cần"** "chức năng" "Scan", "Fax", "Copy". Nhưng vì
          `IPrintableDocument` "ép" phải implement, class `BaoCao` vẫn phải "cố gắng" "hiện thực hóa" (dù chỉ là "ném
          ra" `NotImplementedException` hoặc "để trống").
        - **"Vi phạm" "nguyên tắc 'ít phụ thuộc' " (minimize dependencies):** Các class "implement"
          `IPrintableDocument` "phụ thuộc" vào interface "quá nhiều" "phương thức" "không cần thiết", làm tăng "độ phức
          tạp" và "khó bảo trì" của code.
        - **"Interface trở nên 'cồng kềnh' " và "khó tái sử dụng":** Interface "quá béo" "khó" "tái sử dụng" ở các "ngữ
          cảnh" khác nhau, vì nó "chứa" quá nhiều "phương thức" "không liên quan".

- **"Interface 'Vừa Vặn' " (Tuân Thủ ISP) - "Phân Tách" Interface "Chuyên Biệt" - "Vừa Đủ" Cho Từng "Vai Trò":**

    - "Giải pháp" ISP là **"chia nhỏ"** interface `IPrintableDocument` "quá béo" thành **nhiều interface "nhỏ gọn" hơn
      **, mỗi interface "chuyên trị" **một "nhóm" "phương thức" "liên quan"** đến một "vai trò" cụ thể:

      ```csharp
      public interface IPrintable // Interface "Có Thể In" - "chuyên trị" "chức năng" "In"
      {
          void Print(); // Chỉ "chứa" phương thức "In"
      }

      public interface IScannable // Interface "Có Thể Scan" - "chuyên trị" "chức năng" "Scan"
      {
          void Scan(); // Chỉ "chứa" phương thức "Scan"
      }

      public interface IFaxable // Interface "Có Thể Fax" - "chuyên trị" "chức năng" "Fax"
      {
          void Fax(); // Chỉ "chứa" phương thức "Fax"
      }

      public interface ICopiable // Interface "Có Thể Copy" - "chuyên trị" "chức năng" "Copy"
      {
          void Copy(); // Chỉ "chứa" phương thức "Copy"
      }

      public interface IDocument // Interface "Tài Liệu" - "chuyên trị" "chức năng" "Lấy nội dung"
      {
          string GetDocumentContent(); // Chỉ "chứa" phương thức "Lấy nội dung"
      }
      ```

    - Bây giờ, các class "tài liệu" (ví dụ: `BaoCao`, `HoaDon`, `CongVan`, ...) có thể "implement" **"chỉ những
      interface mà chúng "thực sự" "cần"**, "không bị 'ép' " "implement" các interface "thừa thãi". Ví dụ:

      ```csharp
      public class BaoCao : IPrintable, IDocument // Class "Báo Cáo" chỉ "implement" IPrintable và IDocument (vì chỉ cần "In" và "Lấy nội dung")
      {
          public void Print() { /* Code "In" báo cáo */ }
          public string GetDocumentContent() { /* Code "Lấy nội dung" báo cáo */ return "Nội dung báo cáo"; }
          // Không cần "implement" Scan, Fax, Copy - vì BaoCao không cần các "chức năng" này
      }

      public class MayScan : IScannable // Class "Máy Scan" chỉ "implement" IScannable (vì chỉ cần "chức năng" "Scan")
      {
          public void Scan() { /* Code "Scan" tài liệu */ }
          // Không cần "implement" Print, Fax, Copy, IDocument - vì MayScan không cần các "chức năng" này
      }
      ```

- **Ví dụ minh họa "Interface 'Quá Béo' " (Vi Phạm ISP) và "Interface 'Vừa Vặn' " (Tuân Thủ ISP):**

  (Ví dụ code C# minh họa sự khác biệt giữa interface "quá béo" và các interface "chuyên biệt" tuân thủ ISP - bạn có thể
  tự viết code ví dụ này để "thực hành" và "thấm nhuần" ISP)

**5.2. "Vấn đề" khi Interface "Quá Béo" - Class "Lãnh Đủ" Các "Phương Thức" "Không Cần Thiết" - "Gánh Nặng" "Không Đáng
Có"**

- **"Ép Buộc" "Implement" Các "Phương Thức" "Không Cần Thiết" (Forced Implementation of Unnecessary Methods):**

    - Interface "quá béo" "ép buộc" các class "implement" interface phải "hiện thực hóa" (implement) **"tất cả"** các "
      phương thức" trong interface, **kể cả những "phương thức" mà class đó "không cần" hoặc "không có ý nghĩa"**.
    - Code "hiện thực hóa" các "phương thức" "thừa thãi" thường trở nên **"vô nghĩa"** (ví dụ: "ném ra"
      `NotImplementedException` hoặc "để trống"), làm code trở nên **"rườm rà"** và **"khó hiểu"**.

- **"Vi Phạm" "Nguyên Tắc 'Ít Phụ Thuộc' " (Violation of Dependency Minimization Principle):**

    - Class "implement" interface "quá béo" phải **"phụ thuộc"** vào **"toàn bộ"** interface, **kể cả các "phương thức"
      mà nó "không sử dụng"**.
    - "Tăng" "độ phụ thuộc" (coupling) "không cần thiết" giữa class và interface.
    - "Giảm" "tính linh hoạt" và "tái sử dụng" của class.

- **"Khó Tái Sử Dụng" Interface (Reduced Interface Reusability):**

    - Interface "quá béo" "chứa" quá nhiều "phương thức" "không liên quan" đến nhau, làm giảm **"tính gắn kết" (
      cohesion)** của interface.
    - "Khó" "tái sử dụng" interface ở các "ngữ cảnh" khác nhau, vì nó "chứa "quá nhiều" "chức năng" "không cần thiết"
      cho các "ngữ cảnh" đó.
    - Interface trở nên "cồng kềnh" và "khó" "mở rộng" một cách "hợp lý".

**5.3. "Giải pháp" ISP - "Phân Tách" Interface, "Tạo" Interface "Vừa Đủ" Cho Từng "Vai Trò" - "Interface 'May Đo' "**

- **"Phân Tách" Interface "Quá Béo" Thành Nhiều Interface "Nhỏ Gọn" Hơn:**

    - "Xác định" các **"nhóm" "phương thức" "liên quan"** với nhau trong interface "quá béo".
    - "Chia nhỏ" interface "quá béo" thành **nhiều interface "nhỏ gọn" hơn**, mỗi interface chỉ "chứa" các "phương thức"
      thuộc về một "nhóm" "liên quan".
    - "Đặt tên" interface "rõ ràng" và "mô tả" đúng "vai trò" hoặc "nhóm" "chức năng" mà interface đó "đại diện".

- **Client "Implement" "Chỉ Những Interface Mà Mình "Cần" ":**

    - Thay vì "ép" client (class "dùng" interface) phải "implement" một interface "quá béo", hãy "cho phép" client **"
      lựa chọn"** và "implement" **"chỉ những interface mà mình "thực sự" "cần"** cho "vai trò" của nó.
    - Client class sẽ "implement" **"vừa đủ"** các interface "nhỏ gọn" "chuyên biệt", **"không bị 'ép' " "implement" các
      interface "thừa thãi"**.

- **"Kết Hợp" Các Interface "Nhỏ Gọn" - "Lắp Ghép" "Chức Năng" "Linh Hoạt":**

    - Để "tạo ra" các "đối tượng" "đa năng" "kết hợp" nhiều "chức năng" khác nhau, bạn có thể "kết hợp" các interface "
      nhỏ gọn" lại với nhau thông qua **"composition" (tập hợp)** hoặc **"dependency injection" (tiêm phụ thuộc)**.
    - Thay vì "kế thừa" một interface "quá béo", class có thể "implement" **nhiều interface "nhỏ gọn"**, và "tập hợp"
      các "đối tượng" "implement" các interface khác nhau để "thực hiện" các "chức năng" "phức tạp" hơn.

- **Ví dụ "tái cấu trúc" interface `IPrintableDocument` "quá béo" thành các interface "chuyên biệt" (tuân thủ ISP):**

  (Ví dụ code C# minh họa quá trình "tái cấu trúc" interface `IPrintableDocument` - bạn có thể tự viết code ví dụ này
  để "thực hành" ISP)

**5.4. Lợi ích của ISP - Code "linh hoạt", "dễ tùy biến", "giảm phụ thuộc" không cần thiết - "Trái Ngọt" Của "
Interface 'Vừa Vặn' "**

- **Code "Linh Hoạt" và "Dễ Tùy Biến" (Improved Flexibility and Adaptability):**

    - "Phân tách" interface giúp class "implement" interface trở nên **"linh hoạt"** hơn, "dễ dàng" "thay đổi" và "tùy
      biến" "chức năng" theo "nhu cầu" cụ thể.
    - Ứng dụng trở nên **"dễ dàng" "thích ứng"** với các yêu cầu "thay đổi" và "mở rộng" "đa dạng" hơn.
    - "Giảm" "thời gian" và "công sức" "tùy biến" và "điều chỉnh" code.

- **"Giảm" "Độ Phụ Thuộc" Không Cần Thiết (Reduced Unnecessary Dependencies):**

    - Client class chỉ "phụ thuộc" vào **"những interface mà mình "thực sự" "cần"**, "không bị 'ép' " "phụ thuộc" vào
      các interface "thừa thãi".
    - "Giảm" **"độ phụ thuộc" (coupling)** giữa các class và interfaces, làm code trở nên **"mô-đun hóa" tốt hơn** và *
      *"dễ bảo trì"** hơn.
    - "Tăng" "khả năng" "tái sử dụng" code, vì các class và interfaces trở nên **"độc lập"** và **"chuyên biệt"** hơn.

- **Code "Dễ Kiểm Thử" (Improved Testability):**

    - Các interface "nhỏ gọn" "dễ dàng" "viết unit tests" hơn, vì mỗi interface chỉ "chứa" một "nhóm" "chức năng" "liên
      quan".
    - Unit tests trở nên **"tập trung"**, **"dễ hiểu"**, và **"dễ bảo trì"** hơn.
    - "Tăng" "độ tin cậy" của code, "đảm bảo" "chất lượng" "cao hơn".

**Tổng Kết Chương 5:**

- Bạn đã "khám phá" **Nguyên Tắc SOLID Số 4: ISP - Interface Segregation Principle (Nguyên Tắc Phân Tách Interface)
  ** - "kim chỉ nam" cho việc "thiết kế" Interfaces "chất lượng cao".
    - "Hiểu" được "ý nghĩa" và "tầm quan trọng" của ISP - "interface 'vừa vặn' ", "không 'ép' client dùng đồ 'thừa' ".
    - "Nhận diện" các "vấn đề" khi interface "quá béo" (class "lãnh đủ" "phương thức" "không cần thiết", "vi phạm" "
      nguyên tắc 'ít phụ thuộc' ", "khó tái sử dụng" interface).
    - Học cách "áp dụng" ISP bằng cách "phân tách" interface "quá béo" thành nhiều interface "nhỏ gọn" hơn, "chuyên
      biệt" hơn, và "cho phép" client "implement" "chỉ những interface mà mình "cần" ".
    - "Thấy" được các "lợi ích" "vàng mười" của ISP (code "linh hoạt", "dễ tùy biến", "giảm phụ thuộc" không cần
      thiết, "dễ kiểm thử", v.v.).

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: Nguyên Tắc SOLID Số 5: DIP - Dependency Inversion Principle (Nguyên Tắc Đảo Ngược
Phụ Thuộc) - "Phụ Thuộc Vào 'Trừu Tượng' , Không Phụ Thuộc Vào 'Cụ Thể' "**. Chúng ta sẽ "mổ xẻ" "nguyên tắc" DIP "cuối
cùng" trong "bộ 5" SOLID, và học cách "áp dụng" DIP để "giảm" "độ phụ thuộc" giữa các class, "tăng" "tính linh hoạt"
và "khả năng kiểm thử" của code.

Bạn có câu hỏi nào về Nguyên Tắc ISP này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng bạn" "
làm chủ" SOLID Principles.

