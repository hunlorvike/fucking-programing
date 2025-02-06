# Chương 5: Polymorphism (Tính Đa Hình) - " 'Một Hình Hài' " "Nhiều Công Dụng' " - " 'Vạn Biến Hình' " Của Đối Tượng Để Code "Linh Hoạt"

Chào mừng bạn đến với **Chương 5: Polymorphism (Tính Đa Hình)**! Trong chương này, chúng ta sẽ "khám phá" **Polymorphism**, một "khái niệm" **"đỉnh cao"** của OOP, được "xây dựng" trên "nền tảng" Inheritance, giúp code OOP trở nên **"linh hoạt"**, **"mạnh mẽ"**, và **"dễ mở rộng"** hơn bao giờ hết.

**Phần 5: Polymorphism (Tính Đa Hình) - " 'Một Hình Hài' " "Nhiều Công Dụng' "**

**5.1. Polymorphism là gì? - " 'Vạn Biến Hình' " Của Đối Tượng - " 'Cùng Một Hành Động', 'Muôn Vàn Cách Thể Hiện' "**

-   **Polymorphism (Tính Đa Hình) - " 'Nhiều Hình Dạng' " Trong OOP:**

    -   **Polymorphism** (Tính Đa Hình) là một "khái niệm" "chủ chốt" của OOP, "cho phép" các **Đối Tượng** của các **Class "khác nhau"** (nhưng có "quan hệ" "kế thừa" với nhau) có thể được **"xem"** và **"xử lý"** như các **Đối Tượng** của **"cùng một Class"** (Base Class/Interface).
    -   Polymorphism "cho phép" bạn **"gọi" "cùng một 'hành động' "** (method) trên các Đối Tượng "khác nhau", nhưng **"mỗi Đối Tượng"** sẽ **"thực hiện" "hành động" đó theo "cách 'riêng' " của mình**. "Cùng một "tên gọi", "muôn vàn cách thể hiện".
    -   Hãy tưởng tượng Polymorphism như **"khả năng 'vạn biến hình' " của các Đối Tượng**. Một Đối Tượng có thể "xuất hiện" và "hành xử" theo "nhiều "hình dạng' " khác nhau, tùy thuộc vào "ngữ cảnh" và "kiểu" của nó.

-   **"Ví Dụ 'Minh Họa' " - "Hành Động 'Phát Ra Âm Thanh' " (MakeSound) Của "Động Vật":**

    -   Trong ví dụ "Gia Đình" Class "Động Vật" (Animal) ở Chương 4, chúng ta đã "định nghĩa" method `MakeSound()` trong Base Class `Animal` và "ghi đè" (override) method `MakeSound()` này trong các Derived Classes `Dog`, `Cat`, `Bird`, `Fish`.
    -   **Polymorphism "cho phép" chúng ta "xử lý" một "danh sách" các Đối Tượng "Động Vật" "khác nhau"** (Dog, Cat, Bird, Fish) **"một cách 'thống nhất' "** thông qua "tham chiếu" đến Base Class `Animal`.
    -   Khi chúng ta "gọi" method `MakeSound()` trên **từng Đối Tượng** trong "danh sách" "Động Vật", **"mỗi Đối Tượng"** sẽ **"phát ra âm thanh" "đặc trưng"** của **"loại" "động vật" đó** (Dog sủa "Woof!", Cat kêu "Meow!", Bird hót "Tweet!", Fish im lặng). **"Cùng một hành động" `MakeSound()`, nhưng "kết quả" "khác nhau"** tùy theo "kiểu" Đối Tượng.

    ```csharp
    // (Tiếp tục ví dụ Class Animal, Dog, Cat từ Chương 4)

    public class PolymorphismExample
    {
        public static void Main(string[] args)
        {
            // "Tạo" danh sách các Đối Tượng "Động Vật" "khác nhau" (Dog, Cat)
            List<Animal> animals = new List<Animal>
            {
                new Dog { Name = "Lucky", Age = 3, Breed = "Golden Retriever" },
                new Cat { Name = "Whiskers", Age = 2, FurColor = "Gray" },
                new Dog { Name = "Buddy", Age = 5, Breed = "Labrador" },
                new Cat { Name = "Garfield", Age = 7, FurColor = "Orange" }
            };

            // "Duyệt qua" danh sách "Động Vật" và "gọi" method MakeSound() trên từng Đối Tượng
            foreach (Animal animal in animals) // "Dùng" "tham chiếu" kiểu Base Class "Animal" để "xử lý" các Đối Tượng "khác nhau"
            {
                Console.WriteLine($"{animal.Name} says:");
                animal.MakeSound(); // "Gọi" method "đa hình" MakeSound() - "cùng một lệnh gọi", "kết quả" "khác nhau" tùy theo "kiểu" Đối Tượng
                Console.WriteLine();
            }
        }
    }
    ```

-   **"Lợi Ích" Của Polymorphism - "Code 'Linh Hoạt' " và " 'Dễ Mở Rộng' " - "OOP 'Mạnh Mẽ' và 'Uyển Chuyển' "**

    -   **"Code 'Linh Hoạt' " (Flexibility):** Polymorphism "cho phép" bạn "viết code" "tổng quát" có thể **"làm việc"** với **"nhiều 'loại' Đối Tượng" "khác nhau"** một cách **"thống nhất"** (thông qua "tham chiếu" Base Class/Interface). "Không cần" phải "viết code" "riêng biệt" cho từng "loại" Đối Tượng.
    -   **"Code 'Dễ Mở Rộng' " (Extensibility):** Dễ dàng "thêm" các **"loại Đối Tượng" "mới"** (Derived Classes mới) vào hệ thống mà **"không cần" "sửa đổi"** code "cốt lõi" đã có. Code "tự động" "thích nghi" với các "loại Đối Tượng" "mới" nhờ Polymorphism. "Mở rộng" ứng dụng OOP một cách "linh hoạt" và "dễ dàng".
    -   **"Code 'Dễ Bảo Trì' " (Maintainability):** Code OOP "dùng" Polymorphism thường "gọn gàng" hơn, "dễ đọc" hơn, và "dễ bảo trì" hơn. "Giảm" code "lặp đi lặp lại" và "tăng" "tính 'mô-đun' " của code.
    -   **"Code 'Tái Sử Dụng' " (Code Reusability):** Polymorphism "tái sử dụng" code "logic" "chung" thông qua Base Classes/Interfaces và "cho phép" các Derived Classes "tùy chỉnh" "hành vi" "đặc biệt" của mình.

**5.2. Method Overriding (Ghi Đè Phương Thức) - `virtual` và `override` Keywords - " 'Con' " "Thay Đổi" "Cách Làm" Của " 'Cha' " - " 'Tùy Biến' " "Hành Vi" "Kế Thừa"**

-   **Method Overriding (Ghi Đè Phương Thức) - " 'Con' " "Thay Đổi" "Hành Động" Của " 'Cha' "**:

    -   **Method Overriding** (Ghi Đè Phương Thức) là một "cơ chế" của OOP, "cho phép" **Derived Classes** (Lớp Dẫn Xuất) **"thay đổi"** (override) **"cách 'thực hiện' "** (implementation) của một **Method** đã được "định nghĩa" trong **Base Class** (Lớp Cơ Sở).
    -   Method Overriding "cho phép" Derived Classes **"tùy biến"** (customize) **"hành vi"** "kế thừa" từ Base Class, "thực hiện" "cùng một 'hành động' "\*\* (method) theo "cách "riêng' " của mình.
    -   Method Overriding là "yếu tố" "quan trọng" để "thực hiện" **Polymorphism**.

-   **`virtual` và `override` Keywords - " 'Từ Khóa Ma Thuật' " Cho Method Overriding:**

    -   Để "cho phép" method trong Base Class có thể được "ghi đè" (overridden) trong Derived Classes, bạn cần "khai báo" method đó là **`virtual`** (ảo) trong Base Class.
    -   Để "thực sự" "ghi đè" method `virtual` từ Base Class trong Derived Class, bạn cần "khai báo" method "ghi đè" đó là **`override`** (ghi đè) trong Derived Class.

    ```csharp
    public class Animal
    {
        // ... (các thành viên khác) ...

        public virtual void MakeSound() // Method "virtual" - "cho phép" "ghi đè" trong Derived Classes
        {
            Console.WriteLine("Animal makes a sound."); // "Thực hiện" "mặc định" của method "MakeSound" trong Base Class
        }
    }

    public class Dog : Animal
    {
        // ... (các thành viên khác) ...

        public override void MakeSound() // Method "override" - "ghi đè" method "MakeSound" của Base Class
        {
            Console.WriteLine("Dog barks: Woof!"); // "Thực hiện" "ghi đè" của method "MakeSound" trong Derived Class "Dog"
        }
    }

    public class Cat : Animal
    {
        // ... (các thành viên khác) ...

        public override void MakeSound() // Method "override" - "ghi đè" method "MakeSound" của Base Class
        {
            Console.WriteLine("Cat meows: Meow!"); // "Thực hiện" "ghi đè" của method "MakeSound" trong Derived Class "Cat"
        }
    }
    ```

-   **"Quy Tắc" Method Overriding:**

    -   Method "ghi đè" (override method) trong Derived Class phải có **"cùng tên"**, **"cùng kiểu trả về"**, và **"cùng danh sách tham số"** (signature) với method `virtual` trong Base Class mà nó "ghi đè".
    -   Method "ghi đè" phải được "khai báo" với từ khóa **`override`**.
    -   Method `virtual` trong Base Class "có thể" có "thực hiện" (implementation) "mặc định" (như ví dụ `MakeSound()` trong Class `Animal`). Các Derived Classes có thể "ghi đè" method `virtual` để "thay đổi" hoặc "mở rộng" "thực hiện" này.
    -   Method `virtual` trong Base Class cũng có thể **"không có" "thực hiện" "mặc định"** (abstract method - sẽ "học" ở Chương 6 về Abstraction). Trong trường hợp này, **"bắt buộc"** các Derived Classes **"phải" "ghi đè"** method `abstract` đó và "cung cấp" "thực hiện" "cụ thể".

**5.3. Method Overloading (Nạp Chồng Phương Thức) - " 'Cùng Tên' " Nhưng " 'Khác Nhau' " - " 'Linh Hoạt' " Trong "Cách Gọi" Phương Thức**

-   **Method Overloading (Nạp Chồng Phương Thức) - " 'Cùng Tên', 'Nhiều Phiên Bản' ":**

    -   **Method Overloading** (Nạp Chồng Phương Thức) là một "tính năng" của C# (và nhiều ngôn ngữ lập trình khác), "cho phép" bạn "định nghĩa" **"nhiều methods" "cùng tên"** trong **"cùng một Class"**, nhưng phải có **"danh sách tham số" "khác nhau"** (khác nhau về **"số lượng"**, **"kiểu dữ liệu"**, hoặc **"thứ tự"** của tham số).
    -   Method Overloading "cho phép" bạn "cung cấp" **"nhiều 'phiên bản' "** của **"cùng một 'hành động' "** (method) với các "đầu vào" (tham số) "khác nhau", "tăng" "tính 'linh hoạt' " trong "cách gọi" method.

-   **"Ví Dụ" Method Overloading - Method `Add` (Cộng) Trong Class `Calculator` (Máy Tính):**

    ```csharp
    public class Calculator
    {
        public int Add(int a, int b) // Method "Add" phiên bản 1: cộng 2 số nguyên
        {
            Console.WriteLine("Add(int, int) được gọi.");
            return a + b;
        }

        public double Add(double a, double b) // Method "Add" phiên bản 2: cộng 2 số thực (double)
        {
            Console.WriteLine("Add(double, double) được gọi.");
            return a + b;
        }

        public decimal Add(decimal a, decimal b, decimal c) // Method "Add" phiên bản 3: cộng 3 số thập phân (decimal)
        {
            Console.WriteLine("Add(decimal, decimal, decimal) được gọi.");
            return a + b + c;
        }
    }
    ```

    -   Class `Calculator` có **"ba phiên bản"** của method `Add`, đều **"cùng tên"** là `Add`, nhưng có **"danh sách tham số" "khác nhau"**:

        -   `Add(int a, int b)`: Nhận vào 2 tham số kiểu `int`.
        -   `Add(double a, double b)`: Nhận vào 2 tham số kiểu `double`.
        -   `Add(decimal a, decimal b, decimal c)`: Nhận vào 3 tham số kiểu `decimal`.

    -   Khi bạn "gọi" method `Add`, **C# compiler sẽ "tự động" "chọn" **"phiên bản" `Add` **"phù hợp"** dựa trên **"kiểu dữ liệu"** và **"số lượng"** **"tham số"** bạn "truyền vào".

    ```csharp
    public class MethodOverloadingExample
    {
        public static void Main(string[] args)
        {
            Calculator calculator = new Calculator();

            int sumInt = calculator.Add(5, 10); // "Gọi" phiên bản Add(int, int)
            Console.WriteLine($"Sum (int): {sumInt}"); // Output: Sum (int): 15

            double sumDouble = calculator.Add(3.14, 2.71); // "Gọi" phiên bản Add(double, double)
            Console.WriteLine($"Sum (double): {sumDouble}"); // Output: Sum (double): 5.85

            decimal sumDecimal = calculator.Add(1.5m, 2.5m, 3.5m); // "Gọi" phiên bản Add(decimal, decimal, decimal)
            Console.WriteLine($"Sum (decimal): {sumDecimal}"); // Output: Sum (decimal): 7.5
        }
    }
    ```

-   **"Lợi Ích" Của Method Overloading - " 'Tiện Lợi' " và " 'Dễ Dùng' " - "Cùng 'Hành Động', 'Gọi' Nhiều Cách":**

    -   **"Tiện Lợi" Cho Người "Sử Dụng" Class:** "Cung cấp" "nhiều "cách gọi' " "cùng một 'hành động' "\*\* (method) với các "đầu vào" (tham số) "khác nhau", "tăng" "tính 'tiện lợi' " và " 'dễ dùng' " cho người "sử dụng" Class. "Không cần" phải "nhớ" nhiều "tên method" "khác nhau" cho các "tình huống" "tương tự".
    -   **"Code 'Dễ Đọc' " Hơn:** "Dùng" "cùng một "tên method' " cho các "hành động" "tương tự" giúp code "dễ đọc" và "dễ hiểu" hơn. "Biểu thị" "mối quan hệ" giữa các "phiên bản" method "khác nhau" (cùng "hành động", chỉ "khác" "đầu vào").
    -   **"Code 'Linh Hoạt' " Hơn:** "Tăng" "tính 'linh hoạt' " của Class. Class có thể "xử lý" các "đầu vào" "đa dạng" hơn và "cung cấp" "chức năng" "đa dạng" hơn với "cùng một "tên method' ".

**5.4. "Ứng Dụng" Polymorphism Trong C# - "Code 'Linh Hoạt' " và " 'Dễ Mở Rộng' " - "OOP 'Thực Chiến' "**

-   **"Ví Dụ" "Ứng Dụng" Polymorphism - "Hệ Thống" "Thông Báo" (Notification System):**

    -   Tưởng tượng bạn "xây dựng" một hệ thống "thông báo" (notification system) "hỗ trợ" nhiều "kênh thông báo" khác nhau (ví dụ: "email" - Email, "SMS" - SMS, "push notification" - Push Notification).
    -   **Polymorphism** là "công cụ" "mạnh mẽ" để "thiết kế" hệ thống "thông báo" một cách "linh hoạt" và "dễ mở rộng".

    ```csharp
    // Base Class "NotificationChannel" (Lớp Cơ Sở "Kênh Thông Báo") - "khuôn mẫu" cho mọi kênh thông báo
    public abstract class NotificationChannel // "abstract" class - Lớp Trừu Tượng
    {
        public string ChannelName { get; protected set; } // Property "protected" - Tên kênh thông báo

        public NotificationChannel(string channelName) // Constructor của Base Class
        {
            ChannelName = channelName;
        }

        public abstract void SendNotification(string message, string recipient); // Method "abstract" - "Gửi thông báo" (phải được "ghi đè" - overridden trong Derived Classes)
    }

    // Derived Class "EmailChannel" (Lớp Dẫn Xuất "Kênh Email") - "kế thừa" từ NotificationChannel
    public class EmailChannel : NotificationChannel
    {
        public string SmtpServer { get; set; } // Property "public" - SMTP server
        public string SenderEmail { get; set; }  // Property "public" - Email người gửi

        public EmailChannel(string smtpServer, string senderEmail) : base("Email") // Constructor - "gọi" constructor của Base Class, "truyền" "tên kênh thông báo"
        {
            SmtpServer = smtpServer;
            SenderEmail = senderEmail;
        }

        public override void SendNotification(string message, string recipient) // "Ghi đè" (override) method "SendNotification" - "logic" "gửi thông báo" "đặc biệt" cho Email
        {
            Console.WriteLine($"Sending Email Notification via {ChannelName} channel...");
            Console.WriteLine($"To: {recipient}, From: {SenderEmail}, SMTP Server: {SmtpServer}");
            Console.WriteLine($"Message: {message}");
            // (Code để "gửi" email thông qua SMTP server, dùng thư viện email, v.v.)
            Console.WriteLine("Email Notification Sent.");
        }
    }

    // Derived Class "SMSChannel" (Lớp Dẫn Xuất "Kênh SMS") - "kế thừa" từ NotificationChannel
    public class SMSChannel : NotificationChannel
    {
        public string SmsGatewayUrl { get; set; } // Property "public" - SMS gateway URL
        public string ApiKey { get; set; }       // Property "public" - API key SMS gateway

        public SMSChannel(string smsGatewayUrl, string apiKey) : base("SMS") // Constructor - "gọi" constructor của Base Class, "truyền" "tên kênh thông báo"
        {
            SmsGatewayUrl = smsGatewayUrl;
            ApiKey = apiKey;
        }

        public override void SendNotification(string message, string recipient) // "Ghi đè" (override) method "SendNotification" - "logic" "gửi thông báo" "đặc biệt" cho SMS
        {
            Console.WriteLine($"Sending SMS Notification via {ChannelName} channel...");
            Console.WriteLine($"To: {recipient}, SMS Gateway URL: {SmsGatewayUrl}, API Key: {ApiKey}");
            Console.WriteLine($"Message: {message}");
            // (Code để "gửi" SMS thông qua SMS gateway API, dùng thư viện SMS, v.v.)
            Console.WriteLine("SMS Notification Sent.");
        }
    }

    public class PolymorphismAppExample
    {
        public static void Main(string[] args)
        {
            // "Tạo" danh sách các "Kênh Thông Báo" "khác nhau" (Email, SMS)
            List<NotificationChannel> notificationChannels = new List<NotificationChannel>
            {
                new EmailChannel { SmtpServer = "smtp.example.com", SenderEmail = "noreply@example.com" },
                new SMSChannel { SmsGatewayUrl = "https://smsgateway.example.com/api/send", ApiKey = "your_api_key" }
            };

            string messageToSend = "Chào bạn! Đây là thông báo từ hệ thống."; // Thông báo muốn gửi
            string recipientAddress = "user@example.com"; // Địa chỉ người nhận (email hoặc số điện thoại)

            // "Duyệt qua" danh sách "Kênh Thông Báo" và "gửi thông báo" qua từng kênh
            foreach (NotificationChannel channel in notificationChannels) // "Dùng" "tham chiếu" kiểu Base Class "NotificationChannel" để "xử lý" các kênh "khác nhau"
            {
                Console.WriteLine($"Sending notification using {channel.ChannelName} channel:");
                channel.SendNotification(messageToSend, recipientAddress); // "Gọi" method "đa hình" SendNotification() - "cùng một lệnh gọi", "cách gửi" "khác nhau" tùy theo "kênh"
                Console.WriteLine("---");
            }
        }
    }
    ```

-   **"Ứng Dụng" Polymorphism - "Code 'Tổng Quát' " "Làm Việc" Với "Nhiều Loại" Đối Tượng:**

    -   Trong ví dụ "Hệ Thống Thông Báo", code "duyệt qua" danh sách `notificationChannels` và "gọi" method `SendNotification()` trên từng `channel` **"không cần" "biết" "kiểu" "cụ thể"** của từng `channel` (EmailChannel, SMSChannel, v.v.). Code chỉ "làm việc" với các `channel` thông qua **"tham chiếu"** kiểu **Base Class `NotificationChannel`**.
    -   Polymorphism "cho phép" code "tổng quát" (ví dụ: vòng lặp `foreach` trong `PolymorphismAppExample.Main()`) "làm việc" với **"nhiều 'loại' Đối Tượng" "khác nhau"** một cách **"thống nhất"**. "Không cần" phải "kiểm tra" "kiểu" Đối Tượng "rồi mới" "gọi" method "tương ứng". "Code" trở nên **"gọn gàng"**, **"dễ đọc"**, và **"dễ bảo trì"**.
    -   "Dễ dàng" **"thêm" "kênh thông báo" "mới"** (ví dụ: Push Notification, Slack Notification) bằng cách "tạo" các Derived Classes mới "kế thừa" từ Class `NotificationChannel` và "ghi đè" method `SendNotification()` với "logic" "gửi thông báo" "riêng" cho kênh mới. Code "cốt lõi" "không cần" "sửa đổi". "Code" OOP **"dễ mở rộng"** và **"linh hoạt"**.

**Tổng Kết Chương 5:**

-   Bạn đã "khám phá" **Polymorphism (Tính Đa Hình)** và "hiểu" được "sức mạnh" của Polymorphism trong OOP.
    -   "Hiểu" **Polymorphism là gì** ("vạn biến hình", "một hình hài", "nhiều công dụng").
    -   "Nắm vững" **Method Overriding** (`virtual` và `override` keywords) và "cách" "Lớp Con" "thay đổi" "hành động" của "Lớp Cha".
    -   "Phân biệt" **Method Overriding** và **Method Overloading**.
    -   "Ứng dụng" Polymorphism để "xây dựng" "Hệ Thống Thông Báo" "linh hoạt" và "dễ mở rộng".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: Abstraction (Tính Trừu Tượng) - " 'Che Giấu' " Chi Tiết "Phức Tạp", "Tập Trung" Vào " 'Cốt Lõi' "**. Chúng ta sẽ "học cách" "vận dụng" **Abstraction** để "đơn giản hóa" "thế giới phức tạp", "che giấu" "chi tiết" "thực hiện", và "tập trung" vào " 'cái gì' " (what) chứ không phải " 'làm như thế nào' " (how), "tăng" "tính 'dễ hiểu' " và " 'mềm dẻo' " của code OOP.

Bạn có câu hỏi nào về Polymorphism này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" OOP.
