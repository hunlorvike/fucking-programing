# Chương 7: "Lắp Ghép" Tất Cả - "OOP Trong Ứng Dụng Thực Tế" - " 'Lego' " Thành " 'Ngôi Nhà' "\*\* - " 'Thực Hành' " OOP Để " 'Hiểu Sâu' "

Chào mừng bạn đến với **Chương 7: "Lắp Ghép" Tất Cả - "OOP Trong Ứng Dụng Thực Tế"**! Trong chương này, chúng ta sẽ **"lắp ghép"** tất cả các **"khái niệm" OOP "cốt lõi"** đã học từ Chương 1 đến Chương 6 (Class, Object, Encapsulation, Inheritance, Polymorphism, Abstraction) và **"xây dựng"** một **"ứng dụng console" "ví dụ"** để **"thấy"** OOP "hoạt động" trong **"thực tế"**. "Thực hành" là "chìa khóa" để "hiểu sâu" và "làm chủ" OOP.

**Phần 7: "Lắp Ghép" Tất Cả - "OOP Trong Ứng Dụng Thực Tế" - " 'Lego' " Thành " 'Ngôi Nhà' "**

**7.1. Ví dụ ứng dụng console đơn giản sử dụng OOP - Ứng Dụng Console "Xây Dựng" Bằng OOP - " 'Thực Hành' " OOP Với "Bài Toán" "Cụ Thể"**

-   **"Bài Toán" Ví Dụ - Ứng Dụng Console "Quản Lý Thư Viện Sách" (Library Management System):**

    -   Chúng ta sẽ "xây dựng" một ứng dụng console "đơn giản" để "quản lý" **"thư viện sách"**. Ứng dụng sẽ có các "chức năng":
        1.  "Thêm" sách mới vào thư viện.
        2.  "Hiển thị" "danh sách" tất cả sách trong thư viện.
        3.  "Tìm kiếm" sách theo "tên sách" hoặc "tác giả".
        4.  "Mượn" sách (borrow book) - "đánh dấu" sách là "đang mượn" và "ghi lại" "thông tin người mượn".
        5.  "Trả" sách (return book) - "đánh dấu" sách là "sẵn sàng" và "xóa" "thông tin người mượn".

-   **"Thiết Kế" OOP Cho Ứng Dụng "Quản Lý Thư Viện Sách":**

    -   **Classes và Objects:**

        -   **`Book` Class (Lớp "Sách"):** "Mô tả" "thông tin" của một "cuốn sách" (tên sách, tác giả, ISBN, trạng thái - "sẵn sàng" hay "đang mượn", thông tin người mượn).
        -   **`Library` Class (Lớp "Thư Viện"):** "Quản lý" "danh sách" các "cuốn sách" (list of `Book` objects), "thực hiện" các "chức năng" "quản lý" thư viện (thêm sách, hiển thị danh sách sách, tìm kiếm sách, mượn sách, trả sách).

    -   **Encapsulation:**

        -   Class `Book`: "Đóng gói" "dữ liệu" (tên sách, tác giả, ISBN, trạng thái, thông tin người mượn) và "hành vi" ("mượn sách", "trả sách") "liên quan" đến "cuốn sách". "Bảo vệ" "dữ liệu" "trạng thái" của sách (trạng thái "sẵn sàng" hay "đang mượn", thông tin người mượn) và chỉ "cho phép" "sửa đổi" thông qua các methods "công khai" (e.g., `BorrowBook()`, `ReturnBook()`).
        -   Class `Library`: "Đóng gói" "danh sách" các "cuốn sách" và "các hành vi" "quản lý" thư viện. "Che giấu" "chi tiết" "lưu trữ" "danh sách" sách (ví dụ: dùng `List<Book>`) và chỉ "cung cấp" "giao diện" "công khai" để "tương tác" với thư viện (thêm sách, hiển thị danh sách, tìm kiếm, mượn, trả).

    -   **Không dùng Inheritance và Polymorphism, Abstraction trong ví dụ "đơn giản" này:** (Để giữ cho ví dụ "đơn giản" và "dễ hiểu" cho người mới bắt đầu. Các chương sau sẽ "ứng dụng" Inheritance, Polymorphism, Abstraction vào các ví dụ "phức tạp" hơn).

-   **Code Ứng Dụng Console "Quản Lý Thư Viện Sách" (OOP):**

    **(File: `Book.cs` - Class `Book`):**

    ```csharp
    public class Book // Class "Sách"
    {
        public string Title { get; set; }    // Property "Tên sách"
        public string Author { get; set; }   // Property "Tác giả"
        public string ISBN { get; set; }     // Property "ISBN"
        public bool IsBorrowed { get; private set; } // Property "Trạng thái mượn" - "private set" để "kiểm soát" việc "sửa đổi" từ bên ngoài
        public string BorrowerName { get; private set; } // Property "Tên người mượn" - "private set"

        public Book(string title, string author, string isbn) // Constructor
        {
            Title = title;
            Author = author;
            ISBN = isbn;
            IsBorrowed = false; // Mặc định sách "sẵn sàng" khi "tạo mới"
            BorrowerName = null;  // Mặc định "không có" người mượn
        }

        public void BorrowBook(string borrowerName) // Method "Mượn sách"
        {
            if (IsBorrowed)
            {
                Console.WriteLine($"Sách '{Title}' đã được mượn bởi {BorrowerName}.");
                return;
            }
            IsBorrowed = true;      // "Cập nhật" trạng thái sách thành "đang mượn"
            BorrowerName = borrowerName; // "Lưu" "tên người mượn"
            Console.WriteLine($"Sách '{Title}' đã được mượn bởi {borrowerName}.");
        }

        public void ReturnBook() // Method "Trả sách"
        {
            if (!IsBorrowed)
            {
                Console.WriteLine($"Sách '{Title}' hiện đang không được mượn.");
                return;
            }
            IsBorrowed = false;     // "Cập nhật" trạng thái sách thành "sẵn sàng"
            BorrowerName = null;      // "Xóa" "thông tin người mượn"
            Console.WriteLine($"Sách '{Title}' đã được trả lại thư viện.");
        }

        public override string ToString() // Override method ToString() để "hiển thị" thông tin sách "đẹp" hơn
        {
            string status = IsBorrowed ? $"Đang mượn bởi: {BorrowerName}" : "Sẵn sàng";
            return $"Tên sách: {Title}, Tác giả: {Author}, ISBN: {ISBN}, Trạng thái: {status}";
        }
    }
    ```

    **(File: `Library.cs` - Class `Library`):**

    ```csharp
    public class Library // Class "Thư Viện"
    {
        private List<Book> _books; // Field "private" - "Danh sách" sách (ẩn chi tiết "lưu trữ")

        public Library() // Constructor
        {
            _books = new List<Book>(); // "Khởi tạo" "danh sách" sách "rỗng" khi "tạo mới" "Thư Viện"
        }

        public void AddBook(Book book) // Method "Thêm sách"
        {
            _books.Add(book); // "Thêm" sách vào "danh sách" sách "bên trong" "Thư Viện"
            Console.WriteLine($"Đã thêm sách '{book.Title}' vào thư viện.");
        }

        public void DisplayAllBooks() // Method "Hiển thị tất cả sách"
        {
            if (_books.Count == 0)
            {
                Console.WriteLine("Thư viện hiện đang không có sách nào.");
                return;
            }
            Console.WriteLine("--- Danh sách sách trong thư viện ---");
            foreach (var book in _books) // Duyệt qua "danh sách" sách "bên trong" "Thư Viện"
            {
                Console.WriteLine(book); // "Gọi" method ToString() của Object Book để "hiển thị" thông tin sách
            }
        }

        public Book FindBookByTitle(string title) // Method "Tìm sách theo tên"
        {
            return _books.Find(book => book.Title.ToLower().Contains(title.ToLower())); // "Tìm" sách trong "danh sách" sách "bên trong" "Thư Viện" theo "tên sách" (không phân biệt hoa thường)
        }

        public List<Book> FindBooksByAuthor(string author) // Method "Tìm sách theo tác giả"
        {
            return _books.FindAll(book => book.Author.ToLower().Contains(author.ToLower())); // "Tìm" danh sách sách trong "danh sách" sách "bên trong" "Thư Viện" theo "tác giả" (không phân biệt hoa thường)
        }

        public void BorrowBook(string bookTitle, string borrowerName) // Method "Mượn sách"
        {
            Book book = FindBookByTitle(bookTitle); // "Tìm" sách theo tên
            if (book == null)
            {
                Console.WriteLine($"Không tìm thấy sách '{bookTitle}' trong thư viện.");
                return;
            }
            book.BorrowBook(borrowerName); // "Gọi" method "BorrowBook" của Object Book để "mượn sách" (thực hiện "hành động" trên Object Book)
        }

        public void ReturnBook(string bookTitle) // Method "Trả sách"
        {
            Book book = FindBookByTitle(bookTitle); // "Tìm" sách theo tên
            if (book == null)
            {
                Console.WriteLine($"Không tìm thấy sách '{bookTitle}' trong thư viện.");
                return;
            }
            book.ReturnBook(); // "Gọi" method "ReturnBook" của Object Book để "trả sách" (thực hiện "hành động" trên Object Book)
        }
    }
    ```

    **(File: `Program.cs` - Code "Chạy" Ứng Dụng Console):**

    ```csharp
    using System;
    using System.Collections.Generic;

    public class Program // Class "Program" - chứa method Main()
    {
        public static void Main(string[] args) // Method Main() - "điểm bắt đầu" ứng dụng console
        {
            Library library = new Library(); // "Tạo" Object "Thư Viện"

            // "Thêm" sách vào thư viện (dùng Object Library và method AddBook())
            library.AddBook(new Book("Lập trình C#", "Nguyễn Văn A", "978-1234567890"));
            library.AddBook(new Book("OOP với C#", "Trần Thị B", "978-0987654321"));
            library.AddBook(new Book("Design Patterns", "Erich Gamma", "978-1111222233"));

            while (true) // Vòng lặp "menu" ứng dụng
            {
                Console.WriteLine("\n--- Ứng Dụng Quản Lý Thư Viện Sách (Console OOP) ---"); // "Tiêu đề" ứng dụng
                Console.WriteLine("1. Xem danh sách sách"); // "Menu" chức năng
                Console.WriteLine("2. Thêm sách mới");
                Console.WriteLine("3. Tìm sách theo tên");
                Console.WriteLine("4. Tìm sách theo tác giả");
                Console.WriteLine("5. Mượn sách");
                Console.WriteLine("6. Trả sách");
                Console.WriteLine("7. Thoát");
                Console.Write("Chọn chức năng: "); // "Hỏi" người dùng "chọn" chức năng

                string choice = Console.ReadLine(); // "Đọc" lựa chọn

                switch (choice) // "Phân tích" lựa chọn và "thực hiện" chức năng tương ứng
                {
                    case "1": library.DisplayAllBooks(); break; // Xem danh sách sách
                    case "2": ThemSachMoi(library); break; // Thêm sách mới
                    case "3": TimSachTheoTen(library); break; // Tìm sách theo tên
                    case "4": TimSachTheoTacGia(library); break; // Tìm sách theo tác giả
                    case "5": MuonSach(library); break; // Mượn sách
                    case "6": TraSach(library); break; // Trả sách
                    case "7": return; // Thoát ứng dụng
                    default: Console.WriteLine("Lựa chọn không hợp lệ."); break; // Báo lỗi nếu chọn không đúng
                }
            }
        }

        // Các "phương thức" "hỗ trợ" "thực hiện" các "chức năng" ứng dụng (ví dụ: "hỏi" thông tin sách từ người dùng, "gọi" methods của Object Library để "thực hiện" chức năng)
        static void ThemSachMoi(Library library)
        {
            Console.Write("Nhập tên sách: ");
            string title = Console.ReadLine();
            Console.Write("Nhập tên tác giả: ");
            string author = Console.ReadLine();
            Console.Write("Nhập ISBN: ");
            string isbn = Console.ReadLine();

            Book newBook = new Book(title, author, isbn); // "Tạo" Object Book mới
            library.AddBook(newBook); // "Gọi" method AddBook() của Object Library để "thêm" sách vào thư viện
        }

        static void TimSachTheoTen(Library library)
        {
            Console.Write("Nhập tên sách muốn tìm: ");
            string titleToFind = Console.ReadLine();
            Book foundBook = library.FindBookByTitle(titleToFind); // "Gọi" method FindBookByTitle() của Object Library để "tìm" sách theo tên

            if (foundBook != null)
            {
                Console.WriteLine("\n--- Sách tìm thấy ---");
                Console.WriteLine(foundBook); // "Hiển thị" thông tin sách "tìm thấy"
            }
            else
            {
                Console.WriteLine($"Không tìm thấy sách nào có tên '{titleToFind}'.");
            }
        }

        static void TimSachTheoTacGia(Library library)
        {
            Console.Write("Nhập tên tác giả muốn tìm: ");
            string authorToFind = Console.ReadLine();
            List<Book> foundBooks = library.FindBooksByAuthor(authorToFind); // "Gọi" method FindBooksByAuthor() của Object Library để "tìm" danh sách sách theo tác giả

            if (foundBooks.Count > 0)
            {
                Console.WriteLine($"\n--- Sách của tác giả '{authorToFind}' ---");
                foreach (var book in foundBooks) // Duyệt qua danh sách sách "tìm thấy"
                {
                    Console.WriteLine(book); // "Hiển thị" thông tin từng cuốn sách
                }
            }
            else
            {
                Console.WriteLine($"Không tìm thấy sách nào của tác giả '{authorToFind}'.");
            }
        }

        static void MuonSach(Library library)
        {
            Console.Write("Nhập tên sách muốn mượn: ");
            string bookTitleToBorrow = Console.ReadLine();
            Console.Write("Nhập tên người mượn: ");
            string borrowerName = Console.ReadLine();
            library.BorrowBook(bookTitleToBorrow, borrowerName); // "Gọi" method BorrowBook() của Object Library để "mượn sách"
        }

        static void TraSach(Library library)
        {
            Console.Write("Nhập tên sách muốn trả: ");
            string bookTitleToReturn = Console.ReadLine();
            library.ReturnBook(bookTitleToReturn); // "Gọi" method ReturnBook() của Object Library để "trả sách"
        }
    }
    ```

**7.2. "Phân Tích" Ví Dụ OOP - " 'Mổ Xẻ' " Code OOP "Thực Tế" - " 'Giải Mã' " "Ưu Điểm" OOP**

-   **"Code 'Gọn Gàng' và 'Dễ Đọc' " (Readability):** Code OOP được "tổ chức" thành các Class `Book` và `Library` "rõ ràng", "mỗi Class" "chịu trách nhiệm" cho một "phần" "logic" "riêng" của ứng dụng. Code trong mỗi Class "gọn gàng" và "dễ đọc" hơn so với code thủ tục "dài dòng" và "rối rắm".

-   **"Tính 'Mô-đun' " (Modularity):** Class `Book` và `Library` là các "module" "độc lập", "tách biệt" nhau. Bạn có thể "thay đổi" code bên trong một Class mà "ít ảnh hưởng" đến Class khác. "Tăng" "tính 'mô-đun' " và " 'dễ bảo trì' " của code.

-   **"Encapsulation" - " 'Bảo Vệ' " Dữ Liệu và " 'Kiểm Soát' " "Hành Vi":** Class `Book` "đóng gói" "dữ liệu" (tên sách, tác giả, ISBN, trạng thái mượn, người mượn) và "hành vi" ("mượn sách", "trả sách"). Các properties `IsBorrowed` và `BorrowerName` được "bảo vệ" bằng `private set`, chỉ có thể "sửa đổi" thông qua các methods "công khai" `BorrowBook()` và `ReturnBook()`. "Đảm bảo" "tính 'toàn vẹn' " của dữ liệu và "kiểm soát" "cách" dữ liệu được "sửa đổi".

-   **"Code 'Tái Sử Dụng' " (Code Reusability):** Class `Book` và `Library` có thể được "tái sử dụng" trong các ứng dụng "quản lý thư viện" khác hoặc các ứng dụng "quản lý" "danh mục" (catalogs) "nói chung".

-   **"Code 'Dễ Mở Rộng' " (Extensibility):** Dễ dàng "mở rộng" "chức năng" ứng dụng bằng cách "thêm" các Class mới hoặc "sửa đổi" các Class hiện có. Ví dụ: "thêm" Class `Member` (thành viên thư viện), "thêm" chức năng "gia hạn" sách, "thêm" chức năng "thống kê" sách, v.v. Code OOP "dễ mở rộng" hơn so với code thủ tục "khó thay đổi" và "khó mở rộng".

**7.3. "Mở Rộng" Ví Dụ OOP - " 'Nâng Cấp' " Ứng Dụng OOP "Lên Tầm Cao Mới" - " 'Thêm' " Tính Năng và " 'Ứng Dụng' " OOP "Nâng Cao"**

-   **"Ý Tưởng" "Mở Rộng" Ứng Dụng "Quản Lý Thư Viện Sách":**

    -   **"Thêm" Class `Member` (Thành Viên Thư Viện):** "Quản lý" "thông tin" của "thành viên" thư viện (tên, mã số thẻ, địa chỉ, số điện thoại, v.v.). "Liên kết" `Member` với `Book` (quan hệ "mượn-trả sách").
    -   **"Thêm" "phân loại" sách (Genre):** "Phân loại" sách theo "thể loại" (ví dụ: "tiểu thuyết", "khoa học viễn tưởng", "kinh dị", v.v.). "Thêm" property `Genre` vào Class `Book` và "cho phép" "tìm kiếm" sách theo "thể loại".
    -   **"Thêm" "chức năng" "gia hạn" sách (Renew Book):** "Cho phép" thành viên "gia hạn" thời gian "mượn sách" (nếu sách chưa bị "đặt trước" - reserved).
    -   **"Thêm" "chức năng" "đặt trước" sách (Reserve Book):** "Cho phép" thành viên "đặt trước" sách (nếu sách đang "được mượn" hoặc "chưa có" trong thư viện).
    -   **"Ứng dụng" Inheritance và Polymorphism:**
        -   "Tạo" Base Class `LibraryItem` (Lớp Cơ Sở "Vật Phẩm Thư Viện") để "mô tả" "đặc điểm" và "hành vi" "chung" của "mọi vật phẩm" trong thư viện (sách, báo, tạp chí, DVD, v.v.).
        -   "Tạo" Derived Classes `Book`, `Magazine`, `DVD` "kế thừa" từ Base Class `LibraryItem`. "Ứng dụng" Polymorphism để "xử lý" các "vật phẩm thư viện" "khác nhau" một cách "thống nhất" thông qua "tham chiếu" đến Base Class `LibraryItem`.
        -   "Ứng dụng" Abstraction: "Dùng" Abstract Classes hoặc Interfaces để "định nghĩa" "giao diện" "chung" cho các "hành động" "quản lý" thư viện (ví dụ: Interface `IBorrowable` cho các vật phẩm "có thể mượn được", Interface `IReservable` cho các vật phẩm "có thể đặt trước được").

-   **(Bài tập):** Hãy "mở rộng" ứng dụng console "Quản Lý Thư Viện Sách" bằng cách "thêm" các "tính năng" "mở rộng" và "ứng dụng" Inheritance, Polymorphism, Abstraction như "ý tưởng" trên. "Thử sức" "xây dựng" ứng dụng OOP "phức tạp" hơn và "thực hành" "vận dụng" các "khái niệm" OOP đã học.

**Tổng Kết Chương 7:**

-   Bạn đã "lắp ghép" tất cả các "khái niệm" OOP "cốt lõi" và "xây dựng" thành công một ứng dụng console "ví dụ" "Quản Lý Thư Viện Sách" bằng OOP.
    -   "Thấy" OOP "hoạt động" trong "thực tế" và "hiểu" "ưu điểm" của OOP (code "gọn gàng", "dễ đọc", "dễ bảo trì", "tái sử dụng", "mở rộng").
    -   "Phân tích" và " 'mổ xẻ' " code OOP "thực tế" để "củng cố" "kiến thức" OOP.
    -   "Nhận" "ý tưởng" "mở rộng" ứng dụng OOP và "khuyến khích" "thực hành" "nâng cao" kỹ năng OOP.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: "Tổng Kết Hành Trình OOP" và "Bước Tiếp Theo" - "Trở Thành 'Bậc Thầy' OOP"**. Chúng ta sẽ "ôn lại" "kiến thức" OOP "cốt lõi", "nhận" "lời khuyên" "chân thành" để "tiếp tục" "nâng cao" kỹ năng OOP, và "khám phá" các "tài nguyên" "bổ ích" để "học sâu" hơn về OOP trong C# và "trở thành" "bậc thầy" OOP.

Bạn có câu hỏi nào về ví dụ ứng dụng OOP này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" OOP.

