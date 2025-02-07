# Chương 3: Encapsulation (Tính Đóng Gói) - " 'Bảo Vệ' " Dữ Liệu Bên Trong Đối Tượng - " 'Tạo Vỏ Bọc' " An Toàn Cho Dữ Liệu OOP

Chào mừng bạn đến với **Chương 3: Encapsulation (Tính Đóng Gói)**! Trong chương này, chúng ta sẽ "khám phá" *
*Encapsulation**, một trong những "khái niệm" **"quan trọng"** nhất của OOP, giúp bạn **"bảo vệ"** dữ liệu bên trong Đối
Tượng, "tăng" **"tính 'toàn vẹn' "**, **"tính 'bảo mật' "**, và **"tính 'mô-đun' "** của code OOP.

**Phần 3: Encapsulation (Tính Đóng Gói) - " 'Bảo Vệ' " Dữ Liệu Bên Trong Đối Tượng**

**3.1. Encapsulation là gì? - " 'Gói Gém' " Dữ Liệu và " 'Hành Vi' " - " 'Bí Mật' " Bên Trong " 'Hộp Đen' "**

- **Encapsulation (Tính Đóng Gói) - " 'Gói Gém' " và " 'Che Giấu' ":**

    - **Encapsulation** (Tính Đóng Gói) là một "nguyên tắc" "cốt lõi" của OOP, "liên quan" đến việc **"gói gém"** (
      bundle) **"dữ liệu"** (data/properties) và **"hành vi"** (behavior/methods) "liên quan" đến dữ liệu đó **"trong
      cùng một đơn vị"** (Class/Object).
    - Encapsulation cũng "bao gồm" việc **"che giấu"** (hide) **"chi tiết" "thực hiện"** "bên trong" (implementation
      details) và chỉ "cung cấp" **"giao diện" "công khai"** (public interface) để "tương tác" với Đối Tượng.
    - Hãy tưởng tượng Encapsulation như việc "đặt" các "thành phần" "bên trong" của một "Đối Tượng" vào một **" 'hộp
      đen' "**. "Bên ngoài" chỉ có thể "tương tác" với "Đối Tượng" thông qua các **" 'cổng' " "công khai"** (public
      interface) được "cung cấp" trên " 'hộp đen' ", "không thể" "truy cập" "trực tiếp" vào các "thành phần" "bên
      trong".

- **"Ví Dụ 'Dễ Hình Dung' " - "Động Cơ Xe Hơi" - " 'Hộp Đen' " Encapsulation:**

    - **"Động cơ xe hơi" (Car Engine)** là một "ví dụ" "điển hình" về Encapsulation trong thế giới thực.
    - "Người lái xe" (bên ngoài "Động cơ xe hơi") chỉ cần "quan tâm" đến **"giao diện" "công khai"** của "Động cơ xe
      hơi" (ví dụ: "chân ga", "vô lăng", "hộp số"). "Người lái xe" **"không cần"** và **"không nên"** "can thiệp" "trực
      tiếp" vào các "chi tiết" "phức tạp" "bên trong" "Động cơ xe hơi" (ví dụ: "cơ chế đốt cháy nhiên liệu", "hệ thống
      bôi trơn", "hệ thống làm mát", v.v.).
    - **"Encapsulation 'che giấu' " "chi tiết" "phức tạp" "bên trong" "Động cơ xe hơi"** và chỉ "cung cấp" "giao diện" "
      đơn giản" để "điều khiển" "Động cơ xe hơi". Điều này giúp "người lái xe" "dùng" xe "dễ dàng" hơn, "an toàn" hơn,
      và "không cần" "hiểu" "quá sâu" về "cấu tạo" "Động cơ xe hơi".

- **"Mục Đích" Của Encapsulation - " 'Bảo Vệ' ", " 'Kiểm Soát' ", và " 'Đơn Giản Hóa' ":**

    - **"Bảo Vệ" "Dữ Liệu" (Data Protection):** "Ngăn chặn" "truy cập" và "sửa đổi" "trực tiếp" "dữ liệu" "bên trong"
      Đối Tượng từ "bên ngoài" Class. "Đảm bảo" "tính 'toàn vẹn' " và " 'bảo mật' " của dữ liệu.
    - **"Kiểm Soát" "Truy Cập" Dữ Liệu (Access Control):** "Quy định" "cách thức" "hợp lệ" để "truy cập" và "sửa đổi" "
      dữ liệu" thông qua các "phương thức" và "thuộc tính" "công khai" (public methods and properties) được "cung cấp"
      bởi Class. "Cho phép" "thêm" "logic" "kiểm tra" và "xác thực" dữ liệu khi "truy cập" và "sửa đổi".
    - **"Đơn Giản Hóa" Việc "Sử Dụng" Đối Tượng (Simplicity):** "Che giấu" "chi tiết" "phức tạp" "bên trong" và chỉ "
      cung cấp" "giao diện" "đơn giản" và "dễ dùng" để "tương tác" với Đối Tượng. "Giảm" "độ phức tạp" và "tăng" "tính '
      dễ hiểu' " của code.
    - **"Thay Đổi" "Thực Hiện" "Bên Trong" "Không Ảnh Hưởng" Đến "Bên Ngoài" (Flexibility and Maintainability):** "Cho
      phép" "thay đổi" "chi tiết" "thực hiện" "bên trong" Class (ví dụ: "cách" dữ liệu được "lưu trữ", "cách" methods
      được "thực hiện") mà **"không làm 'hỏng' " code "bên ngoài"** đang "sử dụng" Class, miễn là "giao diện" "công
      khai" (public interface) của Class **"không thay đổi"**. "Tăng" "tính 'linh hoạt' " và " 'dễ bảo trì' " của code.

**3.2. Access Modifiers (public, private, protected, internal) - " 'Hàng Rào' " "Bảo Vệ" Dữ Liệu - " 'Quy Định' " "Ai
Được 'Phép' " "Truy Cập' " Phần Nào**

- **Access Modifiers (Bộ Sửa Đổi Truy Cập) - " 'Hàng Rào' " "Phân Quyền" Truy Cập:**

    - **Access Modifiers** (Bộ Sửa Đổi Truy Cập) là các từ khóa trong C# (và nhiều ngôn ngữ OOP khác) được "dùng" để **"
      kiểm soát" "mức độ 'truy cập' "** (access level) của các **Class Members** (fields, properties, methods,
      constructors) từ **"bên ngoài" Class**.
    - Access Modifiers "định nghĩa" **" 'hàng rào' " "bảo vệ"** xung quanh các Class Members, "quy định" **"ai"** (phần
      code nào) được "phép" **"truy cập"** (đọc, ghi, gọi) các Class Members đó.
    - Access Modifiers "đóng vai trò" "quan trọng" trong việc "thực hiện" **Encapsulation**.

- **Các Access Modifiers Phổ Biến Trong C#:**

    - **`public` (Công Khai): " 'Cửa Mở Rộng' " - "Truy Cập" Từ "Mọi Nơi":**

        - Class Members được "khai báo" là **`public`** có thể được **"truy cập"** từ **"bất kỳ đâu"** trong chương
          trình (từ bên trong Class, từ bên ngoài Class, từ các Class khác, từ các namespaces khác, v.v.).
        - `public` là "mức độ 'truy cập' " **"ít hạn chế nhất"**.
        - "Dùng" `public` cho các Class Members mà bạn muốn **"cung cấp"** **"giao diện" "công khai"** để "tương tác"
          với Đối Tượng từ "bên ngoài" (ví dụ: các methods "công khai" để "thực hiện" "chức năng" của Đối Tượng, các
          properties "công khai" để "đọc" hoặc "ghi" dữ liệu "có kiểm soát").

    - **`private` (Riêng Tư): " 'Vùng Cấm' " - "Chỉ Truy Cập" Từ "Bên Trong Class":**

        - Class Members được "khai báo" là **`private`** chỉ có thể được **"truy cập"** từ **"bên trong" Class** mà
          chúng được "khai báo". "Không thể" "truy cập" từ "bên ngoài" Class (kể cả từ các Class "kế thừa" - derived
          classes).
        - `private` là "mức độ 'truy cập' " **"hạn chế nhất"**.
        - "Dùng" `private` cho các Fields **"lưu trữ" "dữ liệu 'bên trong' " Đối Tượng**. "Ẩn giấu" "chi tiết" "thực
          hiện" "bên trong" và "bảo vệ" dữ liệu khỏi bị "truy cập" và "sửa đổi" "trực tiếp" từ "bên ngoài".

    - **`protected` (Bảo Vệ): " 'Cửa Riêng' " Cho " 'Gia Đình' " - "Truy Cập" Từ "Bên Trong Class" và "Class 'Kế
      Thừa' ":**

        - Class Members được "khai báo" là **`protected`** có thể được **"truy cập"** từ **"bên trong" Class** mà chúng
          được "khai báo" và từ **"các Class 'kế thừa' " (derived classes)** của Class đó. "Không thể" "truy cập" từ "
          bên ngoài" Class và các Class "kế thừa".
        - `protected` "mở rộng" "mức độ 'truy cập' " của `private` cho "gia đình" Class (các Class "kế thừa").
        - "Dùng" `protected` cho các Class Members mà bạn muốn **"cho phép" "Class 'kế thừa' " "truy cập"** và **"mở
          rộng"** (ví dụ: các methods "ảo" - virtual methods, các properties "ảo" - virtual properties), nhưng **"không
          muốn" "cho phép" "truy cập" từ "bên ngoài"** Class và các Class "kế thừa".

    - **`internal` (Nội Bộ): " 'Cửa Hàng Xóm' " - "Truy Cập" Từ "Bên Trong Assembly":**

        - Class Members được "khai báo" là **`internal`** có thể được **"truy cập"** từ **"bên trong" cùng **"
          Assembly"\*\* (thư viện .dll hoặc ứng dụng .exe) mà chúng được "khai báo". "Không thể" "truy cập" từ "bên
          ngoài" Assembly.
        - `internal` "giới hạn" "mức độ 'truy cập' " trong "phạm vi" của Assembly hiện tại.
        - "Dùng" `internal` để "ẩn giấu" "chi tiết" "thực hiện" "bên trong" Assembly và "ngăn chặn" "truy cập" từ các
          Assembly khác. "Thường dùng" trong "phát triển" các thư viện (libraries) hoặc components.

    - **`protected internal` (Bảo Vệ Nội Bộ): " 'Kết Hợp' " `protected` và `internal`:**

        - Class Members được "khai báo" là **`protected internal`** có thể được **"truy cập"** từ **"bên trong" Class**,
          **"các Class 'kế thừa' "**, và **"bên trong" cùng **"Assembly"\*\* \*\*.
        - `protected internal` là "kết hợp" giữa `protected` và `internal`, "mở rộng" "mức độ 'truy cập' " cho cả "gia
          đình" Class và "hàng xóm" Assembly.

    - **`private protected` (Riêng Tư Bảo Vệ): " 'Kết Hợp' " `private` và `protected` (C# 7.2 trở lên):**
        - Class Members được "khai báo" là **`private protected`** có thể được **"truy cập"** từ **"bên trong" Class**
          và **"các Class 'kế thừa' "** (nhưng chỉ khi các Class "kế thừa" này **"nằm trong cùng Assembly"**). "Hạn chế"
          hơn `protected internal`.
        - `private protected` là "kết hợp" giữa `private` và `protected`, "hạn chế" "mức độ 'truy cập' " cho "gia đình"
          Class "trong cùng Assembly".

- **"Quy Ước" Sử Dụng Access Modifiers - "Nguyên Tắc 'Ít Đặc Quyền Nhất' " (Least Privilege Principle):**

    - **"Nguyên tắc 'Ít Đặc Quyền Nhất' " (Least Privilege Principle): "Luôn 'dùng' " "mức độ 'truy cập' " "hạn chế
      nhất"** có thể cho Class Members.
    - **"Bắt đầu" với `private` "mặc định"** cho Fields. Chỉ "mở rộng" "mức độ 'truy cập' " khi "thực sự cần thiết".
    - **"Dùng" `public` "cẩn thận"**, chỉ cho các Class Members mà bạn muốn **"cung cấp" "giao diện" "công khai"**.
    - **"Dùng" `protected` khi muốn "cho phép" "Class 'kế thừa' " "mở rộng"** và "tùy chỉnh" "hành vi" của Class "cha".
    - **"Dùng" `internal`** (hoặc `private protected`) khi muốn "ẩn giấu" "chi tiết" "thực hiện" "bên trong" Assembly.

**3.3. Properties (Thuộc Tính) - " 'Cổng' " "Truy Cập" Dữ Liệu "Có Kiểm Soát" - " 'Người Gác Cổng' " Cho Dữ Liệu**

- **Properties (Thuộc Tính) - " 'Giao Diện' " "Trừu Tượng" Để " 'Tương Tác' " Với Dữ Liệu:**

    - **Properties** (Thuộc Tính) là "cơ chế" **"chính"** để "truy cập" (đọc và ghi) **"dữ liệu"** (trạng thái, đặc
      điểm) của Objects trong OOP.
    - Properties "ẩn giấu" "chi tiết" "lưu trữ" dữ liệu (fields) và "cung cấp" **"giao diện" "trừu tượng"** hơn, **"có
      kiểm soát"**, và **"linh hoạt"** hơn để "tương tác" với dữ liệu so với việc "truy cập" "trực tiếp" vào Fields.
    - Properties "thực hiện" **Encapsulation** bằng cách:
        - "Che giấu" Fields (thường khai báo `private`).
        - "Cung cấp" **"get accessor"** (phương thức `get`) để "đọc" giá trị (read-only hoặc read-write).
        - "Cung cấp" **"set accessor"** (phương thức `set`) để "ghi" giá trị (write-only hoặc read-write).
        - Cho phép "thêm" **"logic" "kiểm tra"**, **"xác thực"**, **"tính toán"**, hoặc **"tác dụng phụ"** (side
          effects) bên trong `get` và `set` accessors, "kiểm soát" "cách" dữ liệu được "truy cập" và "sửa đổi".

- **"Cú Pháp" Property Trong C#:**

  ```csharp
  public class House
  {
      private int _numberOfRooms; // Field "private" để "lưu trữ" "số phòng"

      public int NumberOfRooms // Property "public" tên "NumberOfRooms"
      {
          get // get accessor - "đọc" giá trị property
          {
              // (Code để "lấy" giá trị - thường "trả về" giá trị của field "ẩn")
              return _numberOfRooms;
          }
          set // set accessor - "ghi" giá trị property
          {
              // (Code để "xét" giá trị mới - thường "gán" giá trị mới cho field "ẩn")
              _numberOfRooms = value;
          }
      }

      // ... (các thành viên khác) ...
  }
  ```

- **"Auto-Implemented Properties" - "Property 'Tự Động' " - "Code 'Gọn Gàng' Cho Properties 'Đơn Giản' ":**

    - **Auto-Implemented Properties** (Properties "Tự Động Thực Hiện") là một "cú pháp" "ngắn gọn" để "tạo" Properties
      khi bạn **"không cần" "logic" "tùy chỉnh"** trong `get` và `set` accessors.
    - Auto-Implemented Properties "tự động" "tạo ra" một **"field 'ẩn danh' "** (backing field) để "lưu trữ" dữ liệu
      property, và "cung cấp" `get` và `set` accessors "mặc định" để "truy cập" field "ẩn danh" đó.

  ```csharp
  public class House
  {
      public string BuildingMaterial { get; set; } // Auto-implemented property "read-write"
      public string Color { get; } = "Mặc định";     // Auto-implemented property "read-only" (chỉ có get, không có set, và "khởi tạo" giá trị mặc định)

      // ... (các thành viên khác) ...
  }
  ```

- **"Các Loại" Properties:**

    - **Read-Write Properties:** Có cả `get` và `set` accessors, cho phép **"đọc"** và **"ghi"** giá trị property. (Ví
      dụ: `NumberOfRooms`, `BuildingMaterial`).
    - **Read-Only Properties:** Chỉ có `get` accessor, **"chỉ cho phép 'đọc' "**, "không cho phép 'ghi' " giá trị
      property từ "bên ngoài" Class. (Ví dụ: `Area`, `YearBuilt`). Thường dùng để "tính toán" giá trị "dựa trên" các
      properties khác hoặc "trả về" giá trị "không thể" "sửa đổi" từ "bên ngoài".
    - **Write-Only Properties:** Chỉ có `set` accessor, **"chỉ cho phép 'ghi' "**, "không cho phép 'đọc' " giá trị
      property từ "bên ngoài" Class. (Ít phổ biến hơn Read-Write và Read-Only Properties. Có thể dùng để "thiết lập" giá
      trị "nội bộ" mà không muốn "cho phép" "đọc" từ "bên ngoài" vì lý do "bảo mật" hoặc "thiết kế").

**3.4. "Ứng Dụng" Encapsulation Trong C# - " 'Gói Gém' " Code "Gọn Gàng" và "An Toàn" - "Code OOP 'Đúng Chuẩn' "**

- **"Ví Dụ" "Ứng Dụng" Encapsulation - Class `BankAccount` (Tài Khoản Ngân Hàng):**

  ```csharp
  public class BankAccount // Class "Tài Khoản Ngân Hàng"
  {
      private string _accountNumber; // Field "private" - "Số tài khoản" (ẩn chi tiết "lưu trữ")
      private decimal _balance;     // Field "private" - "Số dư" (ẩn chi tiết "lưu trữ")

      public string AccountNumber // Property "public" "read-only" - "Số tài khoản" (chỉ cho phép "đọc" từ "bên ngoài")
      {
          get { return _accountNumber; }
      }

      public decimal Balance // Property "public" "read-only" - "Số dư" (chỉ cho phép "đọc" từ "bên ngoài")
      {
          get { return _balance; }
      }

      public BankAccount(string accountNumber, decimal initialBalance) // Constructor để "khởi tạo" tài khoản
      {
          _accountNumber = accountNumber;
          _balance = initialBalance;
      }

      public void Deposit(decimal amount) // Method "public" "Gửi Tiền"
      {
          if (amount <= 0)
          {
              Console.WriteLine("Số tiền gửi không hợp lệ.");
              return;
          }
          _balance += amount; // "Sửa đổi" "số dư" "bên trong" Object
          Console.WriteLine($"Gửi thành công {amount:#,##0} VND. Số dư mới: {_balance:#,##0} VND.");
      }

      public void Withdraw(decimal amount) // Method "public" "Rút Tiền"
      {
          if (amount <= 0)
          {
              Console.WriteLine("Số tiền rút không hợp lệ.");
              return;
          }
          if (amount > _balance)
          {
              Console.WriteLine("Số dư không đủ để rút.");
              return;
          }
          _balance -= amount; // "Sửa đổi" "số dư" "bên trong" Object
          Console.WriteLine($"Rút thành công {amount:#,##0} VND. Số dư mới: {_balance:#,##0} VND.");
      }
  }
  ```

- **"Giải thích" "ứng dụng" Encapsulation trong Class `BankAccount`:**

    - **Fields `_accountNumber` và `_balance` được khai báo `private`**: "Bảo vệ" "dữ liệu 'nhạy cảm' " (số tài khoản,
      số dư) khỏi bị "truy cập" và "sửa đổi" "trực tiếp" từ "bên ngoài" Class.
    - **Properties `AccountNumber` và `Balance` được khai báo `public` và "read-only" (chỉ có `get` accessor)**: "Cung
      cấp" "giao diện" "công khai" để "đọc" "thông tin" tài khoản (số tài khoản, số dư) từ "bên ngoài", nhưng **"không
      cho phép 'sửa đổi' " "trực tiếp"** "số tài khoản" và "số dư" từ "bên ngoài". "Kiểm soát" "quyền 'ghi' " dữ liệu.
    - **Methods `Deposit()` và `Withdraw()` được khai báo `public`**: "Cung cấp" "giao diện" "công khai" để "thực hiện"
      các "hành động" "giao dịch" (gửi tiền, rút tiền) trên tài khoản. Methods "chứa" "logic" "kiểm tra" và "xác thực"
      giao dịch (ví dụ: "kiểm tra" số tiền gửi/rút có hợp lệ không, "kiểm tra" số dư có đủ để rút không) và **"sửa
      đổi" "dữ liệu" "bên trong" Object** (`_balance`) một cách **"có kiểm soát"**.
    - **Constructor `BankAccount()`**: "Khởi tạo" "trạng thái ban đầu" của tài khoản (số tài khoản, số dư) khi "tạo mới"
      Object.

**Tổng Kết Chương 3:**

- Bạn đã "khám phá" **Encapsulation (Tính Đóng Gói)** và "hiểu" được "tầm quan trọng" của Encapsulation trong OOP.
    - "Hiểu" **Encapsulation là gì** ("gói gém", "che giấu", "bảo vệ").
    - "Nắm vững" **Access Modifiers** (public, private, protected, internal) và "cách" chúng "kiểm soát" "mức độ 'truy
      cập' " Class Members.
    - Học cách "sử dụng" **Properties** để "cung cấp" "giao diện" "trừu tượng" và "có kiểm soát" để "truy cập" dữ liệu.
    - "Ứng dụng" Encapsulation trong Class `BankAccount` để "gói gém" code "gọn gàng" và "an toàn".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Inheritance (Tính Kế Thừa) - " 'Tái Sử Dụng' " Code và " 'Xây Dựng' " "Cây Gia Phả"
Class**. Chúng ta sẽ "học cách" "vận dụng" **Inheritance** để "tái sử dụng" code, "mở rộng" "chức năng", và "xây dựng"
các "hệ thống phân cấp" Class "thông minh".

Bạn có câu hỏi nào về Encapsulation này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành"
cùng bạn trên con đường "chinh phục" OOP.
