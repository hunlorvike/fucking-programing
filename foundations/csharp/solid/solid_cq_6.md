# Chương 6: Nguyên Tắc SOLID Số 5: DIP - Dependency Inversion Principle (Nguyên Tắc Đảo Ngược Phụ Thuộc) - "Phụ Thuộc Vào 'Trừu Tượng' , Không Phụ Thuộc Vào 'Cụ Thể' "\*\* - "Đảo Ngược" "Quyền Lực" Phụ Thuộc, "Trao Quyền" Cho "Trừu Tượng"

Chào mừng bạn đến với **Chương 6: Nguyên Tắc SOLID Số 5: DIP - Dependency Inversion Principle (Nguyên Tắc Đảo Ngược Phụ
Thuộc)**! Trong chương "kết màn" "bộ 5" SOLID này, chúng ta sẽ "khám phá" "nguyên tắc" DIP - một "kim chỉ nam" "cao cấp"
và "quan trọng" để "thiết kế" code **"mềm dẻo"**, **"dễ kiểm thử"**, **"dễ thay thế"**, và **"dễ tái sử dụng"**, bằng
cách "đảo ngược" "quyền lực" phụ thuộc và "trao quyền" cho "trừu tượng".

**Phần 6: Nguyên Tắc SOLID Số 5: DIP - Dependency Inversion Principle (Nguyên Tắc Đảo Ngược Phụ Thuộc) - "Phụ Thuộc
Vào 'Trừu Tượng' , Không Phụ Thuộc Vào 'Cụ Thể' "**

**6.1. DIP là gì? (Giải thích "dễ hiểu" và "ví dụ minh họa") - "Phụ Thuộc Vào 'Hợp Đồng' ", Không "Phụ Thuộc Vào 'Chi
Tiết' "**

- **DIP - Dependency Inversion Principle (Nguyên Tắc Đảo Ngược Phụ Thuộc) - "Tuyên Ngôn" "Đảo Ngược" "Quyền Lực" Phụ
  Thuộc:**

    - DIP có hai "vế" "tuyên ngôn" "quan trọng":

        1. **"Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào abstraction (trừu
           tượng) "**.
        2. **"Abstractions không nên phụ thuộc vào details (chi tiết). Details nên phụ thuộc vào abstractions"**.

    - Nói một cách "dễ hiểu" hơn:

        1. **"Class 'cấp cao' (High-level modules) - class 'chính', 'quan trọng' trong ứng dụng"** (ví dụ: class
           `QuanLyDonHang` - quản lý đơn hàng, class `ThanhToanService` - dịch vụ thanh toán) **"không nên" "phụ thuộc
           trực tiếp" vào class "cấp thấp" (Low-level modules) - class "phụ trợ", "chi tiết"** (ví dụ: class
           `SqlServerDatabase`, class `EmailSender`). Thay vào đó, **cả hai nên "phụ thuộc" vào "trừu tượng" (
           abstractions)** - Interfaces hoặc Abstract Classes.
        2. **"Interfaces" (trừu tượng) không nên "phụ thuộc" vào "chi tiết"**. Interfaces nên "định nghĩa" các "hợp
           đồng" (contracts) "chung chung", "không quan tâm" đến "cách thức" "hiện thực hóa" "cụ thể". **"Các class 'cụ
           thể' " (details) (ví dụ: `SqlServerDatabase`, `EmailSender`) nên "implement" Interfaces** - "tuân thủ" "hợp
           đồng" mà Interfaces "định nghĩa".

- **"Vi phạm" DIP - "Phụ Thuộc Trực Tiếp" Vào Class "Cụ Thể" - Code "Cứng Nhắc" và "Khó Thay Thế":**

    - Hãy tưởng tượng bạn có một class `QuanLySanPham` (ProductManager) "phụ thuộc trực tiếp" vào class
      `SqlServerDatabase` (để "lưu trữ" dữ liệu sản phẩm vào SQL Server):

      ```csharp
      public class SqlServerDatabase // Class "cấp thấp" - "cụ thể" - "quản lý" kết nối SQL Server
      {
          public void LuuSanPham(SanPham sanPham) // Phương thức "lưu" sản phẩm vào SQL Server
          {
              // Code "lưu" sản phẩm vào SQL Server database "cụ thể"
              Console.WriteLine($"Lưu sản phẩm '{sanPham.TenSanPham}' vào SQL Server database");
          }
      }

      public class QuanLySanPham // Class "cấp cao" - "chính" - "quản lý" nghiệp vụ sản phẩm
      {
          private SqlServerDatabase _database; // "Phụ thuộc trực tiếp" vào class "cụ thể" SqlServerDatabase

          public QuanLySanPham()
          {
              _database = new SqlServerDatabase(); // "Khởi tạo" "trực tiếp" SqlServerDatabase
          }

          public void ThemSanPham(SanPham sanPham) // Phương thức "thêm" sản phẩm
          {
              // ... (code "kiểm tra" nghiệp vụ sản phẩm) ...

              _database.LuuSanPham(sanPham); // "Phụ thuộc trực tiếp" vào phương thức "LuuSanPham" của SqlServerDatabase
          }
      }

      public class Program
      {
          static void Main(string[] args)
          {
              QuanLySanPham quanLySanPham = new QuanLySanPham(); // Tạo đối tượng QuanLySanPham
              SanPham sanPham = new SanPham { TenSanPham = "Bàn phím cơ", Gia = 150000 }; // Tạo đối tượng SanPham

              quanLySanPham.ThemSanPham(sanPham); // "Thêm" sản phẩm (và "lưu" vào SQL Server database)

              Console.ReadKey();
          }
      }
      ```

    - Class `QuanLySanPham` "vi phạm" DIP vì:

        - **"Phụ thuộc trực tiếp" vào class "cụ thể" `SqlServerDatabase`**: Class `QuanLySanPham` "khởi tạo" và "dùng"
          `SqlServerDatabase` **"trực tiếp"** bên trong code của nó.
        - **Code trở nên "cứng nhắc"**: Nếu bạn muốn "thay đổi" database từ SQL Server sang MySQL, bạn phải **"sửa đổi"
          code của class `QuanLySanPham`** (thay `SqlServerDatabase` bằng `MySqlDatabase`) - "vi phạm" "nguyên tắc '
          đóng' cho 'sửa đổi' " (OCP).
        - **"Khó kiểm thử" (Unit Test)**: "Khó khăn" khi viết unit tests cho class `QuanLySanPham`, vì bạn phải "phụ
          thuộc" vào `SqlServerDatabase` (database "thật" hoặc "giả lập" phức tạp) trong unit tests. "Khó" "cô lập" và "
          kiểm thử" "đơn vị" class `QuanLySanPham` một cách "độc lập".
        - **"Khó tái sử dụng"**: Class `QuanLySanPham` trở nên "gắn chặt" với SQL Server database, "khó" "tái sử dụng" ở
          các "ngữ cảnh" khác nhau (ví dụ: ứng dụng "không dùng" SQL Server).

- **"Tuân Thủ" DIP - "Phụ Thuộc Vào 'Trừu Tượng' " (Interface) - "Mềm Dẻo" và "Dễ Thay Thế":**

    - "Giải pháp" DIP là **"đảo ngược" "quyền lực" phụ thuộc**, "không cho phép" class "cấp cao" "phụ thuộc trực tiếp"
      vào class "cấp thấp", mà "phụ thuộc" vào **"trừu tượng" (Interface)**.
    - "Tạo" một **interface `IDatabase`** để "định nghĩa" "hợp đồng" "chung" cho các "thao tác" database (ví dụ: phương
      thức `LuuSanPham()`).
    - Class `SqlServerDatabase` và các class "database khác" (ví dụ: `MySqlDatabase`, `PostgreSqlDatabase`, ...) sẽ "
      implement" interface `IDatabase` để "hiện thực hóa" các "thao tác" database "cụ thể" cho từng loại database.
    - Class `QuanLySanPham` sẽ **"không"** "phụ thuộc trực tiếp" vào class "cụ thể" `SqlServerDatabase` (hay bất kỳ
      class "database cụ thể" nào), mà **"phụ thuộc" vào interface `IDatabase`**.
    - "Tiêm" (inject) "sự phụ thuộc" `IDatabase` vào `QuanLySanPham` thông qua **Constructor Injection** (hoặc Property
      Injection, Method Injection) - một kỹ thuật **Dependency Injection (DI)** "phổ biến".

- **Ví dụ minh họa "Vi phạm" DIP và "Tuân Thủ" DIP:**

  (Ví dụ code C# minh họa sự khác biệt giữa class "vi phạm" DIP và các class "tuân thủ" DIP - bạn có thể tự viết code ví
  dụ này để "thực hành" và "thấm nhuần" DIP)

**6.2. "Vấn đề" khi Class "Phụ Thuộc Trực Tiếp" Vào Class Khác - Code "Khó Kiểm Thử", "Khó Thay Thế", "Khó Tái Sử
Dụng" - "Hậu Quả" Của "Phụ Thuộc 'Cứng Nhắc' "**

- **Code "Cứng Nhắc" (Rigidity) - "Khó Uốn Nắn" Khi "Thay Đổi" "Phụ Thuộc":**

    - Class "phụ thuộc trực tiếp" vào class khác thường trở nên **"cứng nhắc"** - "khó" "thay đổi" "phụ thuộc" khi cần.
    - Nếu bạn muốn "thay thế" class "phụ thuộc" (dependency) bằng một class khác (ví dụ: "thay" `SqlServerDatabase` bằng
      `MySqlDatabase`), bạn phải **"sửa đổi" code của class "phụ thuộc"** (ví dụ: class `QuanLySanPham`).
    - Code trở nên **"khó" "mở rộng"** và **"khó" "thích ứng"** với các "thay đổi" về "yêu cầu" hoặc "công nghệ".

- **"Khó Kiểm Thử" (Testability is Reduced) - "Vật Cản" Cho Unit Testing:**

    - Class "phụ thuộc trực tiếp" vào class khác thường **"khó" "viết unit tests"** một cách "độc lập" và "dễ dàng".
    - Bạn phải "tạo" các **"mocks"** hoặc **"stubs"** "phức tạp" để "giả lập" "hành vi" của class "phụ thuộc", hoặc
      phải "phụ thuộc" vào "implementation" "thật" của class "phụ thuộc" trong unit tests (điều này làm giảm tính "đơn
      vị" và "tốc độ" của unit tests).
    - Code trở nên **"khó kiểm thử"** và **"khó 'đảm bảo' chất lượng"**.

- **"Giảm" "Khả Năng Tái Sử Dụng" (Reduced Reusability):**

    - Class "phụ thuộc trực tiếp" vào class khác thường trở nên **"gắn chặt"** với class "phụ thuộc" đó, làm giảm **"
      tính gắn kết" (cohesion)** và **"tăng" "tính phụ thuộc" (coupling)** của class.
    - "Khó" "tái sử dụng" class ở các "ngữ cảnh" khác nhau, vì nó "kéo theo" "sự phụ thuộc" vào class khác.
    - Code trở nên "kém" "mô-đun hóa" và "khó" "lắp ghép" vào các "module" khác.

**6.3. "Giải pháp" DIP - "Đảo Ngược" Phụ Thuộc, "Phụ Thuộc" Vào Interfaces/Abstract Classes - "Trao Quyền" Cho "Trừu
Tượng"**

- **"Phụ Thuộc Vào 'Trừu Tượng' " (Depend on Abstractions) - "Hướng Đến 'Hợp Đồng' ", Không "Hướng Đến 'Chi Tiết' ":**

    - Thay vì class "cấp cao" "phụ thuộc trực tiếp" vào class "cấp thấp" "cụ thể", hãy "đảo ngược" "chiều" phụ thuộc,
      và "cho phép" **cả hai** "phụ thuộc" vào **"trừu tượng"** (Interfaces hoặc Abstract Classes).
    - Class "cấp cao" sẽ "không quan tâm" đến "chi tiết" "hiện thực hóa" của class "cấp thấp", mà chỉ "quan tâm" đến **"
      hợp đồng"** mà interface hoặc abstract class "định nghĩa".

- **"Dependency Injection (DI) - "Trao" "Phụ Thuộc" Từ "Bên Ngoài" Vào Class - "Không Để" Class "Tự Tạo" "Phụ Thuộc"**:

    - **Dependency Injection (DI)** là một "kỹ thuật" thiết kế phần mềm giúp bạn "hiện thực hóa" "Nguyên Tắc Đảo Ngược
      Phụ Thuộc" (DIP) một cách "hiệu quả".
    - Thay vì class "tự" "khởi tạo" (create) các "phụ thuộc" (dependencies) của nó (ví dụ:
      `_database = new SqlServerDatabase()`), hãy "trao" các "phụ thuộc" này vào class **"từ bên ngoài"** thông qua *
      *Constructor Injection**, **Property Injection**, hoặc **Method Injection**.
    - **Constructor Injection (Tiêm Phụ Thuộc Qua Constructor):** "Truyền" các "phụ thuộc" vào class thông qua *
      *constructor** (hàm khởi tạo) của class. Đây là cách DI "phổ biến" và được "khuyến khích" nhất.

      ```csharp
      public class QuanLySanPham // Class "cấp cao" - "tuân thủ" DIP
      {
          private IDatabase _database; // "Phụ thuộc" vào interface IDatabase (trừu tượng)

          public QuanLySanPham(IDatabase database) // Constructor Injection: "nhận" IDatabase "từ bên ngoài"
          {
              _database = database; // "Gán" "phụ thuộc" được "tiêm" vào
          }

          public void ThemSanPham(SanPham sanPham)
          {
              // ... (code "kiểm tra" nghiệp vụ sản phẩm) ...

              _database.LuuSanPham(sanPham); // "Dùng" interface IDatabase để "lưu" sản phẩm - "không quan tâm" đến class "cụ thể" nào
          }
      }
      ```

    - **Inversion of Control (IoC) Containers - "Trạm Điều Phối" Phụ Thuộc "Tự Động":**

        - **Inversion of Control (IoC) Containers** (hoặc Dependency Injection Containers) là các "thư viện" hoặc "
          frameworks" giúp bạn **"tự động hóa"** quá trình **Dependency Injection**.
        - IoC Containers sẽ "quản lý" việc "tạo" và "tiêm" các "phụ thuộc" vào các class của bạn, giúp bạn "giảm" code "
          boilerplate" và "tập trung" vào "logic" nghiệp vụ chính.
        - Các IoC Containers phổ biến trong .NET: **ASP.NET Core Dependency Injection (built-in)**, Autofac, Ninject,
          Castle Windsor, v.v.

- **Ví dụ "tái cấu trúc" class `QuanLySanPham` "vi phạm" DIP thành "tuân thủ" DIP (dùng Interface và Constructor
  Injection):**

  (Ví dụ code C# minh họa quá trình "tái cấu trúc" class `QuanLySanPham` - bạn có thể tự viết code ví dụ này để "thực
  hành" DIP)

**6.4. Lợi ích của DIP - Code "mềm dẻo", "dễ kiểm thử", "dễ thay thế", "dễ tái sử dụng" - "Trái Ngọt" Của "Đảo Ngược"
Phụ Thuộc**

- **Code "Mềm Dẻo" và "Dễ Thay Thế" (Improved Flexibility and Replaceability):**

    - Class "cấp cao" "phụ thuộc" vào "trừu tượng" (interface), **"không bị 'trói buộc' "** vào class "cấp thấp" "cụ
      thể".
    - Bạn có thể "dễ dàng" "thay thế" class "cấp thấp" "cụ thể" (ví dụ: "thay" `SqlServerDatabase` bằng `MySqlDatabase`)
      mà **"không cần" "sửa đổi" code của class "cấp cao"** (ví dụ: `QuanLySanPham`).
    - Ứng dụng trở nên **"mềm dẻo"** (flexible) - "dễ" "thích ứng" với các "thay đổi" về "công nghệ" hoặc "yêu cầu".

- **Code "Dễ Kiểm Thử" (Improved Testability):**

    - Class "cấp cao" "không còn" "phụ thuộc trực tiếp" vào class "cấp thấp" "cụ thể", giúp bạn "dễ dàng" "viết unit
      tests" cho class "cấp cao" một cách **"độc lập"**.
    - Bạn có thể "dùng" **"mocks"** hoặc **"stubs"** "đơn giản" để "giả lập" "hành vi" của interface "phụ thuộc" trong
      unit tests, **"cô lập"** class "cấp cao" khỏi các "phụ thuộc" "phức tạp".
    - Unit tests trở nên **"nhanh hơn"**, **"ổn định hơn"**, và **"dễ bảo trì"** hơn.

- **Code "Dễ Tái Sử Dụng" (Improved Reusability):**

    - Class "cấp cao" "phụ thuộc" vào "trừu tượng" (interface), **"không bị 'gắn chặt' "** với class "cấp thấp" "cụ
      thể".
    - "Dễ dàng" "tái sử dụng" class "cấp cao" ở các "ngữ cảnh" khác nhau, chỉ cần "cung cấp" các "implementation" khác
      nhau của interface "phụ thuộc".
    - Code trở nên **"mô-đun hóa" tốt hơn**, "dễ" "lắp ghép" và "xây dựng" các ứng dụng "lớn mạnh" và "phức tạp".

**Tổng Kết Chương 6:**

- Bạn đã "khám phá" **Nguyên Tắc SOLID Số 5: DIP - Dependency Inversion Principle (Nguyên Tắc Đảo Ngược Phụ Thuộc)** - "
  kim chỉ nam" "cao cấp" cho việc "thiết kế" code "mềm dẻo" và "dễ kiểm thử".
    - "Hiểu" được "ý nghĩa" và "tầm quan trọng" của DIP - "phụ thuộc vào 'trừu tượng' ", không "phụ thuộc vào 'cụ
      thể' ".
    - "Nhận diện" các "vấn đề" khi class "vi phạm" DIP (code "cứng nhắc", "khó kiểm thử", "kém tái sử dụng").
    - Học cách "áp dụng" DIP bằng "trừu tượng hóa" (Interfaces, Abstract Classes) và "Dependency Injection" để "đảo
      ngược" "quyền lực" phụ thuộc và "trao quyền" cho "trừu tượng".
    - "Thấy" được các "lợi ích" "vàng mười" của DIP (code "mềm dẻo", "dễ thay thế", "dễ kiểm thử", "tái sử dụng tốt",
      v.v.).

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: "Bí Kíp" Code Quality - "Nâng Tầm" Code Lên "Đẳng Cấp"**. Chúng ta sẽ "khám phá"
các "bí kíp" và "thực hành" "code quality" "cụ thể" hơn, từ "phong cách code", "quy ước đặt tên", "code reviews", "unit
testing", đến "tái cấu trúc code" (refactoring), giúp bạn "nâng tầm" code C# của mình lên một "đẳng cấp" "chuyên
nghiệp" "thực thụ".

Bạn có câu hỏi nào về Nguyên Tắc DIP này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn lòng "giải đáp" và "cùng bạn" "
làm chủ" SOLID Principles.

