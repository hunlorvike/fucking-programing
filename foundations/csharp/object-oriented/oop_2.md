# Chương 2: Class và Object - " 'Bản Thiết Kế' " và " 'Sản Phẩm' " Của OOP - " 'Nền Tảng' " Để " 'Xây Dựng' " Code OOP

Chào mừng bạn đến với **Chương 2: Class và Object**! Trong chương này, chúng ta sẽ "đi sâu" vào **Class** và **Object**,
hai "khái niệm" **"nền tảng"** và **"quan trọng nhất"** của OOP. "Hiểu rõ" Class và Object là "bước đầu tiên" để "làm
chủ" OOP và "xây dựng" code OOP "thực thụ".

**Phần 2: Class và Object - " 'Bản Thiết Kế' " và " 'Sản Phẩm' " Của OOP**

**2.1. Class (Lớp) là gì? - " 'Khuôn Mẫu' " Cho Đối Tượng - " 'Bản Vẽ' " Chi Tiết Để " 'Xây Nhà' "**

- **Class (Lớp) - " 'Bản Thiết Kế' " Cho Đối Tượng:**

    - **Class** (Lớp) là một **"khuôn mẫu"** (blueprint), **"bản thiết kế"** (design template), hoặc **"mô tả"** (
      description) cho một **"loại"** (type) **"đối tượng"** (object).
    - Class "xác định" **"các đặc điểm"** (properties/attributes) và **"các hành động"** (behaviors/methods) mà **"tất
      cả"** các **"đối tượng"** thuộc Class đó sẽ có.
    - Class không phải là một "đối tượng" "thực tế". Nó chỉ là **"mô tả"** hoặc **"khuôn mẫu"**. Để có một "đối tượng" "
      thực tế", chúng ta cần "tạo ra" (instantiate) một **"instance"** (thể hiện) của Class.

- **"Ví Dụ 'Dễ Hình Dung' " - Class "Ngôi Nhà" (House):**

    - Tưởng tượng bạn muốn "xây dựng" **"nhiều ngôi nhà"** "cùng một kiểu" (ví dụ: nhà kiểu biệt thự).
    - Bạn sẽ cần một **"bản thiết kế"** (blueprint) chi tiết cho kiểu nhà biệt thự này. "Bản thiết kế" sẽ "mô tả" **"các
      thành phần"** (ví dụ: số phòng, diện tích, vật liệu xây dựng, màu sơn, v.v.) và **"cách xây dựng"** (ví dụ: quy
      trình xây móng, xây tường, lợp mái, v.v.) của ngôi nhà.
    - **Class `House` (Lớp "Ngôi Nhà")** trong OOP "tương tự" như "bản thiết kế" ngôi nhà. Class `House` sẽ "mô tả" **"
      các đặc điểm"** của "ngôi nhà" (ví dụ: `numberOfRooms`, `area`, `buildingMaterial`, `color`) và **"các hành động"
      ** có thể "thực hiện" với "ngôi nhà" (ví dụ: `openDoor`, `closeDoor`, `turnOnLights`, `turnOffLights`).

- **Class "Không Phải" Là Object:**

    - **Class** chỉ là **"khuôn mẫu"**, **"bản thiết kế"**. Nó **"không phải"** là một "ngôi nhà" "thực tế" mà bạn có
      thể "ở" được.
    - Để có một "ngôi nhà" "thực tế", bạn cần **"dùng" "bản thiết kế"** (Class `House`) để **"xây dựng"** (instantiate)
      **"một hoặc nhiều ngôi nhà cụ thể"** (Objects of Class `House`). Mỗi "ngôi nhà cụ thể" sẽ là một **"Object"** "
      riêng biệt", có thể có các "giá trị" "đặc điểm" khác nhau (ví dụ: "ngôi nhà 1" có màu "trắng", "ngôi nhà 2" có
      màu "xanh", nhưng cả hai đều "tuân theo" "bản thiết kế" Class `House`).

- **Class "Định Nghĩa" "Kiểu Dữ Liệu" "Mới":**

    - Class "định nghĩa" một **"kiểu dữ liệu" "mới"** (user-defined type) trong chương trình của bạn.
    - Giống như các "kiểu dữ liệu" "có sẵn" (built-in types) trong C# (ví dụ: `int`, `string`, `bool`, `DateTime`), bạn
      có thể "khai báo" **"biến"** có **"kiểu"** là **Class** (ví dụ: `House myHouse;`, `Person person1;`).
    - "Biến" có "kiểu" Class sẽ "lưu trữ" **"tham chiếu"** (reference) đến một **"Object"** của Class đó (hoặc `null`
      nếu "chưa có" Object nào được "gán").

**2.2. Object (Đối Tượng) là gì? - " 'Thực Thể' " Của Class - " 'Ngôi Nhà' " "Thực Tế" Được " 'Xây' " Từ " 'Bản Thiết
Kế' "**

- **Object (Đối Tượng) - " 'Sản Phẩm' " Được " 'Xây' " Từ Class:**

    - **Object** (Đối Tượng) là một **"thể hiện"** (instance), **"thực thể"** (entity), hoặc **"hiện thân"** (
      embodiment) của một **Class**.
    - Object là **"bản sao"** của Class, được "tạo ra" (instantiated) từ Class. Mỗi Object có **"bộ nhớ" "riêng biệt"**
      để "lưu trữ" **"dữ liệu"** (giá trị của các properties) và **"có thể 'thực hiện' " các "hành động"** (methods)
      được "định nghĩa" trong Class.

- **"Ví Dụ 'Dễ Hiểu' " - Object "Ngôi Nhà Cụ Thể":**

    - **Object `myVilla` (Đối Tượng "Ngôi Nhà Biệt Thự Của Tôi")** là một "ngôi nhà" "thực tế" được "xây dựng" dựa
      trên "bản thiết kế" Class `House`.
    - `myVilla` sẽ có **"các đặc điểm"** "thực tế" (ví dụ: `myVilla.numberOfRooms = 5;`, `myVilla.area = 200;`,
      `myVilla.color = "White";`) và **"có thể 'thực hiện' " các "hành động"** (ví dụ: `myVilla.openDoor();`,
      `myVilla.turnOnLights();`).
    - Bạn có thể "tạo ra" **"nhiều Objects"** (nhiều "ngôi nhà cụ thể") từ **"một Class"** (một "bản thiết kế"). Mỗi
      Object sẽ là một "thực thể" "riêng biệt", có thể có các "giá trị" "đặc điểm" khác nhau, nhưng đều "chia sẻ" "
      chung" "khuôn mẫu" và "hành vi" được "định nghĩa" trong Class.

- **Object "Chiếm Bộ Nhớ" - " 'Ngôi Nhà' " "Chiếm Đất" ":**

    - Khi bạn "tạo ra" một Object, hệ thống sẽ **"cấp phát bộ nhớ"** (allocate memory) để "lưu trữ" **"dữ liệu"** (giá
      trị của các properties) của Object đó.
    - Mỗi Object sẽ "chiếm" một "vùng nhớ" "riêng biệt". Các Objects "khác nhau" (dù cùng Class) sẽ "không 'chia sẻ' "
      bộ nhớ dữ liệu.
    - Khi bạn "không còn 'dùng' " Object nữa (ví dụ: Object "không còn được 'tham chiếu' " bởi bất kỳ biến nào), hệ
      thống sẽ **"giải phóng bộ nhớ"** (garbage collection) mà Object đó "chiếm giữ".

**2.3. Class Members (Thành Viên Class): Fields, Properties, Methods, Constructors - " 'Nguyên Liệu' " và " 'Công Cụ' "
Của Class - " 'Xây Nên' " "Bản Thiết Kế" "Hoàn Chỉnh"**

- **Class Members (Thành Viên Class) - " 'Thành Phần' " Của " 'Bản Thiết Kế' ":**

    - **Class Members** (Thành Viên Class) là các **"thành phần"** "cấu tạo" nên một **Class**. Class Members "định
      nghĩa" **"cấu trúc"** và **"hành vi"** của các **Objects** được "tạo ra" từ Class đó.
    - Các loại Class Members "phổ biến" nhất trong C# OOP bao gồm:
        - **Fields (Trường Dữ Liệu):** "Biến" (variables) được "khai báo" **"bên trong" Class**, dùng để "lưu trữ" **"dữ
          liệu"** (trạng thái, đặc điểm) của các Objects.
        - **Properties (Thuộc Tính):** "Cơ chế" đặc biệt để **"truy cập"** (đọc và ghi) **"dữ liệu"** của Objects một
          cách **"có kiểm soát"**. Properties "ẩn giấu" "chi tiết" "lưu trữ" dữ liệu (fields) và "cung cấp" "giao
          diện" "trừu tượng" hơn để "tương tác" với dữ liệu.
        - **Methods (Phương Thức):** "Hàm" (functions) được "định nghĩa" **"bên trong" Class**, dùng để "thực hiện" **"
          hành động"** (behaviors) trên các Objects. Methods "thao tác" với "dữ liệu" (fields, properties) của Objects
          và "thực hiện" các "tác vụ" "liên quan" đến Objects.
        - **Constructors (Hàm Tạo):** "Phương thức" "đặc biệt" được "gọi" **"tự động"** khi **"tạo mới"** một Object (
          instantiation). Constructors dùng để **"khởi tạo"** (initialize) "trạng thái ban đầu" của Object (ví dụ: "gán"
          giá trị ban đầu cho các fields, properties).

- **Fields (Trường Dữ Liệu) - " 'Nguyên Liệu' " Để " 'Xây Nhà' ":**

    - **Fields** là "biến" (variables) được "khai báo" **"trực tiếp" "bên trong" Class**, **"ngay dưới" "khai báo" Class
      **.
    - Fields "lưu trữ" **"dữ liệu"** (trạng thái, đặc điểm, thuộc tính) của các Objects. Mỗi Object có **"bản sao" "
      riêng biệt"** của các fields.
    - "Quy ước" đặt tên field thường dùng **`camelCase`** và bắt đầu bằng **`_`** (ví dụ: `_name`, `_age`, `_color`).

  ```csharp
  public class House
  {
      private int _numberOfRooms; // Field "private" - chỉ "truy cập" được từ bên trong Class House
      public string BuildingMaterial; // Field "public" - "truy cập" được từ "bên ngoài" Class House
      public string Color;        // Field "public"

      // ... (các thành viên khác) ...
  }
  ```

- **Properties (Thuộc Tính) - " 'Cổng' " "Truy Cập" Dữ Liệu "Có Kiểm Soát" ":**

    - **Properties** là "cơ chế" đặc biệt để **"truy cập"** (đọc và ghi) **"dữ liệu"** của Objects một cách **"có kiểm
      soát"**. Properties "ẩn giấu" "chi tiết" "lưu trữ" dữ liệu (fields) và "cung cấp" "giao diện" "trừu tượng" hơn
      để "tương tác" với dữ liệu.
    - Properties bao gồm **"get accessor"** (để "đọc" giá trị property) và **"set accessor"** (để "ghi" giá trị
      property). Bạn có thể "định nghĩa" "logic" (code) "tùy chỉnh" bên trong get và set accessors để "kiểm soát" "cách"
      dữ liệu được "truy cập" và "sửa đổi".
    - "Quy ước" đặt tên property thường dùng **`PascalCase`** (ví dụ: `NumberOfRooms`, `BuildingMaterial`, `Color`).

  ```csharp
  public class House
  {
      private int _numberOfRooms; // Field "private" để "lưu trữ" "số phòng"

      public int NumberOfRooms // Property "public" để "truy cập" "số phòng" "có kiểm soát"
      {
          get // get accessor - "đọc" giá trị property
          {
              return _numberOfRooms; // "Trả về" giá trị của field _numberOfRooms
          }
          set // set accessor - "ghi" giá trị property
          {
              if (value >= 1 && value <= 20) // "Kiểm tra" giá trị "hợp lệ" (ví dụ: số phòng phải từ 1 đến 20)
              {
                  _numberOfRooms = value; // "Gán" giá trị mới cho field _numberOfRooms nếu "hợp lệ"
              }
              else
              {
                  // "Xử lý" lỗi nếu giá trị "không hợp lệ" (ví dụ: throw Exception, log lỗi, v.v.)
                  Console.WriteLine("Số phòng không hợp lệ. Phải từ 1 đến 20.");
              }
          }
      }

      public string BuildingMaterial { get; set; } // Auto-implemented property - "đơn giản" hơn khi không cần "logic" "tùy chỉnh" get/set
      public string Color { get; set; }

      // ... (các thành viên khác) ...
  }
  ```

- **Methods (Phương Thức) - " 'Công Cụ' " Để " 'Thực Hiện' " "Hành Động" Trên Đối Tượng:**

    - **Methods** là "hàm" (functions) được "định nghĩa" **"bên trong" Class**, dùng để "thực hiện" **"hành động"** (
      behaviors) trên các Objects.
    - Methods "thao tác" với "dữ liệu" (fields, properties) của Objects và "thực hiện" các "tác vụ" "liên quan" đến
      Objects (ví dụ: tính toán, xử lý dữ liệu, tương tác với bên ngoài, v.v.).
    - "Quy ước" đặt tên method thường dùng **`PascalCase`** và thường bắt đầu bằng **"động từ"** (ví dụ: `OpenDoor()`,
      `CalculateArea()`, `DisplayInfo()`).

  ```csharp
  public class House
  {
      // ... (fields, properties) ...

      public void OpenDoor() // Method "public" để "mở cửa" ngôi nhà
      {
          Console.WriteLine("Cửa nhà đã mở.");
          // (Code để "thực hiện" "hành động" "mở cửa" - ví dụ: thay đổi trạng thái Object, tương tác với hệ thống khác, v.v.)
      }

      public decimal CalculateArea() // Method "public" để "tính diện tích" ngôi nhà
      {
          decimal area = NumberOfRooms * 30; // "Giả sử" mỗi phòng rộng 30 mét vuông
          return area; // "Trả về" "diện tích"
      }

      // ... (các thành viên khác) ...
  }
  ```

- **Constructors (Hàm Tạo) - " 'Thợ Xây' " "Khởi Tạo" Object:**

    - **Constructors** là "phương thức" "đặc biệt" có **"cùng tên" với Class**, và **"không có kiểu trả về"** (không có
      `void`, `int`, `string`, v.v.).
    - Constructors được "gọi" **"tự động"** khi bạn **"tạo mới"** một Object (instantiation) bằng từ khóa `new`.
    - Constructors dùng để **"khởi tạo"** (initialize) "trạng thái ban đầu" của Object (ví dụ: "gán" giá trị ban đầu cho
      các fields, properties, "thực hiện" các "tác vụ" "khởi tạo" cần thiết).
    - Một Class có thể có **"nhiều Constructors"** (method overloading) với các "tham số" "khác nhau", cho phép bạn "
      tạo" Object với các "cách khởi tạo" "khác nhau". Nếu bạn "không định nghĩa" Constructor nào trong Class, C# sẽ "tự
      động" "tạo" một **"default constructor"** (hàm tạo mặc định) "không tham số".

  ```csharp
  public class House
  {
      // ... (fields, properties) ...

      public House() // Constructor "không tham số" (default constructor)
      {
          _numberOfRooms = 3; // "Khởi tạo" "số phòng" mặc định là 3
          BuildingMaterial = "Gạch"; // "Khởi tạo" "vật liệu xây dựng" mặc định là "Gạch"
          Color = "Trắng";       // "Khởi tạo" "màu sắc" mặc định là "Trắng"
          Console.WriteLine("Constructor House() được gọi."); // Thông báo constructor được gọi
      }

      public House(int numberOfRooms, string buildingMaterial, string color) // Constructor "có tham số"
      {
          NumberOfRooms = numberOfRooms;     // "Khởi tạo" "số phòng" theo tham số truyền vào (dùng property NumberOfRooms để "kiểm tra" giá trị)
          BuildingMaterial = buildingMaterial; // "Khởi tạo" "vật liệu xây dựng" theo tham số
          Color = color;                   // "Khởi tạo" "màu sắc" theo tham số
          Console.WriteLine("Constructor House(int, string, string) được gọi."); // Thông báo constructor được gọi
      }

      // ... (methods) ...
  }
  ```

**2.4. "Tạo" Class và Object Trong C# - " 'Vẽ' " "Bản Thiết Kế" và " 'Xây' " "Sản Phẩm" - " 'Bắt Tay' " Vào Code OOP**

- **"Tạo" Class ( " 'Vẽ' " "Bản Thiết Kế" ):**

    - "Dùng" từ khóa **`class`** để "khai báo" một Class.
    - "Đặt tên" Class theo "quy ước" **`PascalCase`** và thường dùng **"danh từ số ít"** (ví dụ: `House`, `Person`,
      `Product`, `Order`).
    - "Khai báo" các **Class Members** (fields, properties, methods, constructors) "bên trong" "khối code" của Class (
      `{ ... }`).

  ```csharp
  // "Khai báo" Class "House" (ví dụ)
  public class House // "public" access modifier - Class "công khai", "truy cập" được từ mọi nơi
  {
      // Class members (fields, properties, methods, constructors) sẽ được "khai báo" ở đây
  }
  ```

- **"Tạo" Object ( " 'Xây' " "Sản Phẩm" ):**

    - "Dùng" từ khóa **`new`** theo sau là **"tên Class"** và **"dấu ngoặc đơn" `()`** để "tạo mới" một Object (
      instantiate class).
    - "Gọi" **Constructor** của Class để "khởi tạo" Object. Nếu Class có nhiều Constructors, bạn có thể "chọn"
      Constructor phù hợp bằng cách "truyền" các "tham số" "tương ứng".
    - "Gán" Object mới tạo cho một **"biến"** có **"kiểu"** là **Class** (ví dụ: `House myHouse = new House();`).

  ```csharp
  // "Tạo" Object "house1" từ Class "House" bằng "default constructor" (không tham số)
  House house1 = new House(); // "Gọi" constructor House() để "khởi tạo" Object house1

  // "Tạo" Object "house2" từ Class "House" bằng constructor "có tham số"
  House house2 = new House(4, "Gỗ", "Xanh lá cây"); // "Gọi" constructor House(int, string, string) để "khởi tạo" Object house2 với "tham số"

  Console.WriteLine($"Ngôi nhà 1 có {house1.NumberOfRooms} phòng, màu {house1.Color}."); // "Truy cập" properties của Object house1
  Console.WriteLine($"Ngôi nhà 2 có {house2.NumberOfRooms} phòng, màu {house2.Color}."); // "Truy cập" properties của Object house2

  house1.OpenDoor(); // "Gọi" method của Object house1
  decimal area_house2 = house2.CalculateArea(); // "Gọi" method của Object house2 và "lấy" giá trị trả về
  Console.WriteLine($"Diện tích ngôi nhà 2: {area_house2} mét vuông.");
  ```

**Tổng Kết Chương 2:**

- Bạn đã "khám phá" **Class** và **Object**, "nền tảng" của OOP, và "học cách" "tạo" Class và Object trong C#.
    - "Hiểu" **Class là gì** ("bản thiết kế") và **Object là gì** ("sản phẩm" "thực tế").
    - "Nắm vững" các **Class Members** (fields, properties, methods, constructors) và "vai trò" của chúng trong Class.
    - Biết cách **"khai báo" Class** và **"tạo" Object** từ Class trong C#.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 3: Encapsulation (Tính Đóng Gói) - " 'Bảo Vệ' " Dữ Liệu Bên Trong Đối Tượng**. Chúng ta
sẽ "học cách" "ứng dụng" **Encapsulation** để "gói gém" và "bảo vệ" dữ liệu bên trong Đối Tượng, "tăng" "tính 'mô-đun' "
và " 'bảo mật' " của code OOP.

Bạn có câu hỏi nào về Class và Object này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành"
cùng bạn trên con đường "chinh phục" OOP.
