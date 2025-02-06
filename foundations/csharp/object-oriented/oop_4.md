# Chương 4: Inheritance (Tính Kế Thừa) - " 'Tái Sử Dụng' " Code và " 'Xây Dựng' " "Cây Gia Phả" Class - " 'Mượn Sức Mạnh' " Từ " 'Cha Ông' " Để " 'Phát Triển' " "Đời Sau"

Chào mừng bạn đến với **Chương 4: Inheritance (Tính Kế Thừa)**! Trong chương này, chúng ta sẽ "khám phá" **Inheritance**, một "khái niệm" **"quyền năng"** của OOP, giúp bạn **"tái sử dụng"** code, **"mở rộng"** "chức năng", và **"xây dựng"** các "hệ thống phân cấp" Class **"linh hoạt"** và **"dễ bảo trì"**.

**Phần 4: Inheritance (Tính Kế Thừa) - " 'Tái Sử Dụng' " Code và " 'Xây Dựng' " "Cây Gia Phả" Class**

**4.1. Inheritance là gì? - " 'Con Cháu' " "Thừa Hưởng" "Gia Tài" Từ " 'Cha Ông' " - " 'Kế Thừa' " "Đặc Điểm" và " 'Hành Vi' "**

-   **Inheritance (Tính Kế Thừa) - " 'Cha Truyền Con Nối' " Trong Thế Giới OOP:**

    -   **Inheritance** (Tính Kế Thừa) là một "cơ chế" "quan trọng" của OOP, "cho phép" một **Class mới** (Derived Class/Subclass - Lớp Dẫn Xuất/Lớp Con) **"thừa hưởng"** (inherit) các **"đặc điểm"** (properties) và **"hành động"** (methods) từ một **Class đã có** (Base Class/Superclass - Lớp Cơ Sở/Lớp Cha).
    -   Hãy tưởng tượng Inheritance như **"quan hệ 'cha truyền con nối' " trong gia đình**. "Con cháu" (Derived Class) **"thừa hưởng"** "gia tài" (properties, methods) từ "cha ông" (Base Class). "Con cháu" có thể **"dùng lại"** "gia tài" đã "thừa hưởng" và **"thêm vào"** "những thứ của riêng mình"\*\* (thêm properties, methods mới, hoặc "thay đổi" "cách dùng" "gia tài" - method overriding).

-   **"Ví Dụ 'Dễ Hiểu' " - "Gia Đình" Class "Động Vật" (Animal):**

    -   Tưởng tượng bạn muốn "xây dựng" ứng dụng "quản lý" các loại "động vật" (animals). Có nhiều loại "động vật" khác nhau (ví dụ: "chó" - Dog, "mèo" - Cat, "chim" - Bird, "cá" - Fish, v.v.).
    -   **"Class `Animal` (Lớp "Động Vật")"** có thể là **"Lớp Cơ Sở"** (Base Class). Class `Animal` sẽ "mô tả" các **"đặc điểm 'chung' "** của "tất cả" các loại "động vật" (ví dụ: `Name` - Tên, `Age` - Tuổi, `Weight` - Cân Nặng, `Color` - Màu Sắc) và **"các hành động 'chung' "** (ví dụ: `Eat()` - Ăn, `Sleep()` - Ngủ, `MakeSound()` - Phát Ra Âm Thanh).
    -   **"Class `Dog` (Lớp "Chó")", `Cat` (Lớp "Mèo")", `Bird` (Lớp "Chim")", `Fish` (Lớp "Cá")"** có thể là **"Các Lớp Dẫn Xuất"** (Derived Classes). Các Class này sẽ **"kế thừa"** (inherit) các **"đặc điểm"** và **"hành động"** "chung" từ Class `Animal` (ví dụ: `Name`, `Age`, `Eat()`, `Sleep()`).
    -   **"Các Lớp Dẫn Xuất"** có thể **"thêm vào"** các **"đặc điểm"** và **"hành động" "riêng"** "đặc trưng" cho từng loại "động vật" (ví dụ: Class `Dog` có thêm method `Bark()` - Sủa, Class `Bird` có thêm method `Fly()` - Bay, Class `Fish` có thêm method `Swim()` - Bơi).
    -   **"Cây Gia Phả" Class "Động Vật":** Class `Animal` là "Lớp Cha" (Base Class), các Class `Dog`, `Cat`, `Bird`, `Fish` là "Các Lớp Con" (Derived Classes). Tạo ra một **"hệ thống phân cấp" Class** (class hierarchy) hoặc **"cây gia phả" Class**.

-   **"Lợi Ích" Của Inheritance - " 'Tái Sử Dụng' ", " 'Mở Rộng' ", và " 'Dễ Bảo Trì' ":**

    -   **"Tái Sử Dụng" Code (Code Reusability):** "Tránh" "lặp đi lặp lại" code. Các Lớp Dẫn Xuất "thừa hưởng" code từ Lớp Cơ Sở, "không cần" phải "viết lại" code "chung" (properties, methods "chung"). "Tiết kiệm" thời gian và công sức lập trình.
    -   **"Mở Rộng" "Chức Năng" (Extensibility):** Các Lớp Dẫn Xuất có thể "thêm vào" "chức năng" "riêng" của mình (thêm properties, methods mới) mà "không làm 'ảnh hưởng' " đến Lớp Cơ Sở và các Lớp Dẫn Xuất khác. "Dễ dàng" "mở rộng" ứng dụng bằng cách "thêm" các Lớp Dẫn Xuất mới.
    -   **"Dễ Bảo Trì" (Maintainability):** Khi "sửa đổi" code "chung" trong Lớp Cơ Sở, các "thay đổi" sẽ được **"tự động" "áp dụng"** cho **"tất cả"** các Lớp Dẫn Xuất "kế thừa" từ Lớp Cơ Sở. "Đơn giản hóa" việc "bảo trì" và "cập nhật" code "chung".
    -   **"Tính 'Mô-đun' " (Modularity):** Inheritance giúp "tổ chức" code thành các "module" "phân cấp" (Lớp Cơ Sở và Các Lớp Dẫn Xuất), "tăng" "tính 'mô-đun' " và " 'dễ quản lý' " của code.
    -   **"Tính 'Đa Hình' " (Polymorphism) (sẽ "khám phá" ở Chương 5):** Inheritance là "nền tảng" cho **Polymorphism**. "Cho phép" "xử lý" các Đối Tượng của các Class "khác nhau" (nhưng có "quan hệ" "kế thừa") một cách "thống nhất" thông qua "tham chiếu" đến Lớp Cơ Sở.

**4.2. Base Class (Lớp Cơ Sở) và Derived Class (Lớp Dẫn Xuất) - " 'Cha' " và " 'Con' " Trong "Gia Đình" Class - " 'Quan Hệ' " "Kế Thừa"**

-   **Base Class (Lớp Cơ Sở) / Superclass (Siêu Lớp) / Parent Class (Lớp Cha): " 'Người Cha' " "Gốc" Của "Gia Đình" Class:**

    -   **Base Class** (Lớp Cơ Sở), còn gọi là **Superclass** (Siêu Lớp) hoặc **Parent Class** (Lớp Cha), là Class **"được 'kế thừa' '** bởi một hoặc nhiều **Derived Classes**.
    -   Base Class "cung cấp" các **"đặc điểm"** và **"hành động" "chung"** cho các Derived Classes "kế thừa".
    -   Base Class thường "mô tả" một "khái niệm" **"tổng quát"** hoặc **"chung chung"**. (Ví dụ: Class `Animal` là Base Class "tổng quát" cho các loại "động vật").

-   **Derived Class (Lớp Dẫn Xuất) / Subclass (Lớp Con) / Child Class (Lớp Con): " 'Con Cháu' " "Kế Thừa" "Gia Tài" Từ " 'Cha' "**:

    -   **Derived Class** (Lớp Dẫn Xuất), còn gọi là **Subclass** (Lớp Con) hoặc **Child Class** (Lớp Con), là Class **"kế thừa"** từ một **Base Class**.
    -   Derived Class **"thừa hưởng"** các **"đặc điểm"** và **"hành động"** (không phải tất cả - xem Access Modifiers) từ Base Class.
    -   Derived Class có thể **"thêm vào"** các **"đặc điểm"** và **"hành động" "riêng"** của mình.
    -   Derived Class thường "mô tả" một "khái niệm" **"cụ thể"** hoặc **"đặc biệt"** hơn so với Base Class. (Ví dụ: Class `Dog`, `Cat`, `Bird`, `Fish` là Derived Classes "cụ thể" của Base Class `Animal`).

-   **"Quan Hệ" "Kế Thừa" - " `class DerivedClass : BaseClass` ":**

    -   Trong C#, bạn "dùng" cú pháp **`class DerivedClass : BaseClass`** để "khai báo" một Derived Class **`DerivedClass`** "kế thừa" từ một Base Class **`BaseClass`**.
    -   Dấu **`:`** (hai chấm) và **tên Base Class** sau tên Derived Class "biểu thị" "quan hệ" "kế thừa".

    ```csharp
    // "Khai báo" Base Class "Animal" (ví dụ)
    public class Animal // Base Class - Lớp Cơ Sở
    {
        public string Name { get; set; } // Property "public" - Tên
        public int Age { get; set; }     // Property "public" - Tuổi

        public virtual void MakeSound() // Method "public" "virtual" - Phát ra âm thanh (có thể được "ghi đè" - overridden)
        {
            Console.WriteLine("Animal makes a sound."); // Hành động "mặc định" - Động vật phát ra âm thanh
        }

        public void Eat() // Method "public" - Ăn
        {
            Console.WriteLine("Animal is eating."); // Hành động "chung" - Động vật đang ăn
        }
    }

    // "Khai báo" Derived Class "Dog" "kế thừa" từ Base Class "Animal"
    public class Dog : Animal // Derived Class - Lớp Dẫn Xuất "kế thừa" từ Animal
    {
        public string Breed { get; set; } // Property "public" - Giống chó (đặc điểm "riêng" của Dog)

        public void Bark() // Method "public" - Sủa (hành động "riêng" của Dog)
        {
            Console.WriteLine("Woof! Woof!"); // Hành động "sủa"
        }

        public override void MakeSound() // "Ghi đè" (override) method "MakeSound" từ Base Class "Animal"
        {
            Console.WriteLine("Dog barks: Woof!"); // Hành động "phát ra âm thanh" "đặc biệt" cho Dog - "sủa"
        }
    }

    // "Khai báo" Derived Class "Cat" "kế thừa" từ Base Class "Animal"
    public class Cat : Animal // Derived Class - Lớp Dẫn Xuất "kế thừa" từ Animal
    {
        public string FurColor { get; set; } // Property "public" - Màu lông mèo (đặc điểm "riêng" của Cat)

        public void Meow() // Method "public" - Kêu meo meo (hành động "riêng" của Cat)
        {
            Console.WriteLine("Meow! Meow!"); // Hành động "kêu meo meo"
        }

        public override void MakeSound() // "Ghi đè" (override) method "MakeSound" từ Base Class "Animal"
        {
            Console.WriteLine("Cat meows: Meow!"); // Hành động "phát ra âm thanh" "đặc biệt" cho Cat - "meo meo"
        }
    }
    ```

**4.3. `base` Keyword - " 'Gọi' " Đến " 'Cha' " Để " 'Xin' " "Trợ Giúp' " - " 'Truy Cập' " Thành Viên Của Lớp Cơ Sở**

-   **`base` Keyword - " 'Cầu Nối' " Đến Lớp Cơ Sở:**

    -   **`base` keyword** trong C# được "dùng" trong **Derived Classes** để **"truy cập"** các **"thành viên"** (members - fields, properties, methods, constructors) của **Base Class**.
    -   `base` keyword "cho phép" Derived Class **"gọi"** các methods của Base Class, **"truy cập"** các properties và fields (nếu có "quyền truy cập" - access modifiers cho phép) của Base Class.
    -   `base` keyword thường được "dùng" trong:
        -   **Constructor của Derived Class:** Để "gọi" **Constructor của Base Class** để "khởi tạo" các "thành phần" "chung" được "kế thừa" từ Base Class.
        -   **Method Overriding (Ghi Đè Phương Thức):** Để "gọi" **"phiên bản" "gốc"** của method trong Base Class (đã bị "ghi đè" - overridden) và "thêm vào" "logic" "riêng" của Derived Class.

-   **"Ví Dụ" Sử Dụng `base` Keyword Trong Constructor Của Derived Class:**

    ```csharp
    public class Animal
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public Animal(string name, int age) // Constructor "có tham số" của Base Class "Animal"
        {
            Name = name;
            Age = age;
            Console.WriteLine($"Constructor Animal(string, int) được gọi. Name: {Name}, Age: {Age}");
        }

        // ... (các thành viên khác) ...
    }

    public class Dog : Animal
    {
        public string Breed { get; set; }

        public Dog(string name, int age, string breed) : base(name, age) // Constructor của Derived Class "Dog" - "gọi" constructor của Base Class "Animal" bằng base(...)
        {
            Breed = breed;
            Console.WriteLine($"Constructor Dog(string, int, string) được gọi. Breed: {Breed}");
        }

        // ... (các thành viên khác) ...
    }
    ```

    -   `public Dog(string name, int age, string breed) : base(name, age)`: Trong constructor của Class `Dog`, **`: base(name, age)` "ra lệnh"** cho C# là **"hãy 'gọi' Constructor của Base Class `Animal` "** (Constructor `Animal(string, int)`) và **"truyền" các tham số `name` và `age`** cho Constructor của Base Class.
    -   Constructor của Base Class sẽ được "thực thi" **"trước"** Constructor của Derived Class. "Đảm bảo" các "thành phần" "chung" được "kế thừa" từ Base Class được **"khởi tạo" "đầu tiên"**.

-   **"Ví Dụ" Sử Dụng `base` Keyword Trong Method Overriding (Ghi Đè Phương Thức):**

    ```csharp
    public class Animal
    {
        // ... (các thành viên khác) ...

        public virtual void MakeSound() // Method "virtual" trong Base Class
        {
            Console.WriteLine("Animal makes a sound.");
        }
    }

    public class Dog : Animal
    {
        // ... (các thành viên khác) ...

        public override void MakeSound() // Method "override" trong Derived Class "Dog" - "ghi đè" method "MakeSound" của Base Class
        {
            base.MakeSound(); // "Gọi" "phiên bản" "gốc" của method "MakeSound" trong Base Class "Animal" bằng base.MakeSound()
            Console.WriteLine("Dog barks: Woof!"); // "Thêm" "logic" "riêng" của Dog - "sủa"
        }
    }
    ```

    -   `base.MakeSound();`: Trong method `MakeSound()` của Class `Dog`, `base.MakeSound()` "gọi" và "thực thi" **"phiên bản" "gốc"** của method `MakeSound()` được "định nghĩa" trong **Base Class `Animal`**.
    -   Cho phép Derived Class **"tái sử dụng"** "logic" "chung" của method trong Base Class và **"mở rộng"** hoặc **"thay đổi"** "hành vi" của method bằng cách "thêm vào" code "riêng" của Derived Class.

**4.4. "Ứng Dụng" Inheritance Trong C# - " 'Xây Dựng' " "Hệ Thống Phân Cấp" và " 'Tái Sử Dụng' " Code "Thông Minh" - "OOP 'Linh Hoạt' và 'Mạnh Mẽ' "**

-   **"Ví Dụ" "Ứng Dụng" Inheritance - "Hệ Thống" "Thanh Toán Trực Tuyến" (Online Payment System):**

    -   Tưởng tượng bạn "xây dựng" một hệ thống "thanh toán trực tuyến" (online payment system) "hỗ trợ" nhiều "phương thức thanh toán" khác nhau (ví dụ: "thẻ tín dụng" - Credit Card, "ví điện tử" - E-Wallet, "chuyển khoản ngân hàng" - Bank Transfer).
    -   **Inheritance** là "công cụ" "tuyệt vời" để "tổ chức" code hệ thống "thanh toán" một cách "gọn gàng", "linh hoạt", và "dễ mở rộng".

    ```csharp
    // Base Class "PaymentMethod" (Lớp Cơ Sở "Phương Thức Thanh Toán") - "khuôn mẫu" cho mọi phương thức thanh toán
    public abstract class PaymentMethod // "abstract" class - Lớp Trừu Tượng (sẽ học ở Chương 6)
    {
        public string PaymentMethodName { get; protected set; } // Property "protected" - Tên phương thức thanh toán (chỉ Class và Class "kế thừa" có thể "sửa đổi")

        public PaymentMethod(string paymentMethodName) // Constructor của Base Class
        {
            PaymentMethodName = paymentMethodName;
        }

        public abstract bool ProcessPayment(decimal amount); // Method "abstract" - "Xử lý thanh toán" (phải được "ghi đè" - overridden trong Derived Classes)
    }

    // Derived Class "CreditCardPayment" (Lớp Dẫn Xuất "Thanh Toán Bằng Thẻ Tín Dụng") - "kế thừa" từ PaymentMethod
    public class CreditCardPayment : PaymentMethod
    {
        public string CardNumber { get; set; } // Property "public" - Số thẻ tín dụng
        public string ExpiryDate { get; set; } // Property "public" - Ngày hết hạn
        public string CVV { get; set; }        // Property "public" - Mã CVV

        public CreditCardPayment(string cardNumber, string expiryDate, string cvv) : base("Credit Card") // Constructor - "gọi" constructor của Base Class, "truyền" "tên phương thức thanh toán"
        {
            CardNumber = cardNumber;
            ExpiryDate = expiryDate;
            CVV = cvv;
        }

        public override bool ProcessPayment(decimal amount) // "Ghi đè" (override) method "ProcessPayment" - "logic" "xử lý thanh toán" "đặc biệt" cho Credit Card
        {
            Console.WriteLine($"Processing Credit Card Payment of {amount:#,##0} VND using card number: {CardNumber}");
            // (Code để "gọi" API thanh toán thẻ tín dụng, "xử lý" giao dịch, v.v.)
            Console.WriteLine("Credit Card Payment Successful.");
            return true; // Giả sử thanh toán thành công
        }
    }

    // Derived Class "EWalletPayment" (Lớp Dẫn Xuất "Thanh Toán Bằng Ví Điện Tử") - "kế thừa" từ PaymentMethod
    public class EWalletPayment : PaymentMethod
    {
        public string PhoneNumber { get; set; } // Property "public" - Số điện thoại ví điện tử

        public EWalletPayment(string phoneNumber) : base("E-Wallet") // Constructor - "gọi" constructor của Base Class, "truyền" "tên phương thức thanh toán"
        {
            PhoneNumber = phoneNumber;
        }

        public override bool ProcessPayment(decimal amount) // "Ghi đè" (override) method "ProcessPayment" - "logic" "xử lý thanh toán" "đặc biệt" cho E-Wallet
        {
            Console.WriteLine($"Processing E-Wallet Payment of {amount:#,##0} VND using phone number: {PhoneNumber}");
            // (Code để "gọi" API thanh toán ví điện tử, "xử lý" giao dịch, v.v.)
            Console.WriteLine("E-Wallet Payment Successful.");
            return true; // Giả sử thanh toán thành công
        }
    }

    // Derived Class "BankTransferPayment" (Lớp Dẫn Xuất "Thanh Toán Bằng Chuyển Khoản Ngân Hàng") - "kế thừa" từ PaymentMethod
    public class BankTransferPayment : PaymentMethod
    {
        public string BankAccountNumber { get; set; } // Property "public" - Số tài khoản ngân hàng
        public string BankName { get; set; }        // Property "public" - Tên ngân hàng

        public BankTransferPayment(string bankAccountNumber, string bankName) : base("Bank Transfer") // Constructor - "gọi" constructor của Base Class, "truyền" "tên phương thức thanh toán"
        {
            BankAccountNumber = bankAccountNumber;
            BankName = bankName;
        }

        public override bool ProcessPayment(decimal amount) // "Ghi đè" (override) method "ProcessPayment" - "logic" "xử lý thanh toán" "đặc biệt" cho Bank Transfer
        {
            Console.WriteLine($"Processing Bank Transfer Payment of {amount:#,##0} VND to bank account: {BankAccountNumber}, bank: {BankName}");
            // (Code để "gọi" API chuyển khoản ngân hàng, "xử lý" giao dịch, v.v.)
            Console.WriteLine("Bank Transfer Payment Successful.");
            return true; // Giả sử thanh toán thành công
        }
    }
    ```

-   **"Lợi ích" Inheritance trong ví dụ "Thanh Toán Trực Tuyến":**

    -   **"Tái sử dụng" code "chung":** Các Class `CreditCardPayment`, `EWalletPayment`, `BankTransferPayment` "tái sử dụng" code "chung" từ Class `PaymentMethod` (property `PaymentMethodName`, constructor, method `ProcessPayment` "trừu tượng").
    -   **"Mở rộng" "dễ dàng":** Dễ dàng "thêm" các "phương thức thanh toán" "mới" bằng cách "tạo" các Class Dẫn Xuất mới "kế thừa" từ Class `PaymentMethod` và "ghi đè" method `ProcessPayment` với "logic" "xử lý thanh toán" "riêng" cho phương thức thanh toán mới.
    -   **"Code 'linh hoạt' " và " 'dễ bảo trì' "**: Hệ thống "thanh toán" được "tổ chức" thành các "module" "phân cấp", "dễ hiểu", "dễ bảo trì", và "dễ mở rộng" khi có "yêu cầu" "thay đổi" hoặc "thêm" "phương thức thanh toán" mới.

**Tổng Kết Chương 4:**

-   Bạn đã "khám phá" **Inheritance (Tính Kế Thừa)** và "hiểu" được "sức mạnh" của Inheritance trong OOP. - "Hiểu" **Inheritance là gì** ("kế thừa", "cha truyền con nối"). - "Phân biệt" **Base Class** (Lớp ```markdown
Cơ Sở) và **Derived Class** (Lớp Dẫn Xuất) và "quan hệ" "kế thừa" giữa chúng.
    -   Học cách "dùng" **`base` keyword\*\* để "truy cập" các "thành viên" của Base Class từ Derived Class. - "Ứng dụng" Inheritance để "xây dựng" "hệ thống phân cấp" Class "Thanh Toán Trực Tuyến" và "tái sử dụng" code "thông minh".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: Polymorphism (Tính Đa Hình) - " 'Một Hình Hài' " "Nhiều Công Dụng' "**. Chúng ta sẽ "khám phá" **Polymorphism**, "tính năng" "quyền năng" của OOP được "xây dựng" trên "nền tảng" Inheritance, giúp code OOP trở nên **"linh hoạt"**, **"mạnh mẽ"**, và **"dễ mở rộng"** hơn nữa.

Bạn có câu hỏi nào về Inheritance này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" OOP.

