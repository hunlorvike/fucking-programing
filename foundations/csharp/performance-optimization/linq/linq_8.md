## **Chương 8: LINQ Trong Thực Tế - Ứng Dụng Vào Đời Sống - "LINQ Đi Muôn Nơi"**

Chào mừng bạn đến với **Chương 8: Ứng Dụng Thực Tế của LINQ**! Trong chương "cuối cùng" này, chúng ta sẽ cùng nhau "dạo
quanh" một vài ví dụ "thực tế" để "thấy tận mắt" LINQ "tung hoành" trong các dự án phần mềm "muôn màu muôn vẻ". Chúng ta
sẽ "tham quan" các ví dụ "ứng dụng" LINQ to Objects, LINQ to XML, và LINQ to Entities, "minh họa" cách LINQ "giúp sức" "
giải quyết" các "bài toán" lập trình "hàng ngày" một cách "gọn gàng" và "thông minh".

**Phần 8: Ứng Dụng Thực Tế của LINQ - "LINQ Đi Muôn Nơi"**

**8.1. Ví dụ dự án nhỏ sử dụng LINQ to Objects - Ứng Dụng Console "Nhỏ Mà Có Võ"**

**Ví dụ: Ứng dụng "quản lý danh sách công việc" (To-Do List) "tí hon" trên console**

Chúng ta sẽ "xây" một ứng dụng console "đơn giản" giúp người dùng "quản lý" "danh sách" "việc cần làm" của mình. Ứng
dụng sẽ có các "chức năng":

- "Thêm" "việc" mới.
- "Xem" "danh sách" "tất cả" các "việc".
- "Xem" "danh sách" các "việc" "chưa xong".
- "Đánh dấu" "việc" là "xong".
- "Xóa" "việc".
- "Tìm kiếm" "việc" theo "tên".

Chúng ta sẽ "dùng" `List<TodoItem>` để "giữ" "danh sách" "việc" trong "bộ nhớ" ("chơi" LINQ to Objects).

```csharp
using System;
using System.Collections.Generic;
using System.Linq; // "Nhập" LINQ

public class TodoItem // "Khuôn mẫu" cho "việc cần làm"
{
    public int Id { get; set; } // "Mã số" "việc"
    public string Title { get; set; } // "Tên" "việc"
    public bool IsCompleted { get; set; } // "Trạng thái": đã "xong" hay "chưa"

    public override string ToString() // "Biến" "việc" thành chuỗi để "in ra" màn hình
    {
        return $"[{ (IsCompleted ? "X" : " ") }] ID: {Id}, Title: {Title}"; // Hiển thị "trạng thái", "mã số", và "tên" "việc"
    }
}

public class TodoApp // Class "chính" của ứng dụng To-Do List
{
    private static List<TodoItem> _todoList = new List<TodoItem>(); // "Rổ" "việc cần làm" - dùng List<TodoItem>
    private static int _nextId = 1; // Biến đếm để "tạo" "mã số" "việc" mới

    public static void Main(string[] args) // "Cổng" chính của ứng dụng
    {
        while (true) // Vòng lặp "vô tận" - ứng dụng "chạy" liên tục cho đến khi người dùng "thoát"
        {
            Console.WriteLine("\n--- To-Do List App ---"); // "Tiêu đề" ứng dụng
            Console.WriteLine("1. Thêm công việc"); // "Menu" chức năng
            Console.WriteLine("2. Hiển thị tất cả công việc");
            Console.WriteLine("3. Hiển thị công việc chưa hoàn thành");
            Console.WriteLine("4. Đánh dấu hoàn thành");
            Console.WriteLine("5. Xóa công việc");
            Console.WriteLine("6. Tìm kiếm công việc");
            Console.WriteLine("7. Thoát");
            Console.Write("Chọn chức năng: "); // "Hỏi" người dùng "chọn" chức năng

            string choice = Console.ReadLine(); // "Đọc" lựa chọn của người dùng

            switch (choice) // "Phân tích" lựa chọn và "thực hiện" chức năng tương ứng
            {
                case "1": AddTodo(); break; // Thêm việc
                case "2": ShowAllTodos(); break; // Xem tất cả việc
                case "3": ShowIncompleteTodos(); break; // Xem việc chưa xong
                case "4": MarkAsCompleted(); break; // Đánh dấu xong
                case "5": DeleteTodo(); break; // Xóa việc
                case "6": SearchTodos(); break; // Tìm kiếm việc
                case "7": return; // Thoát ứng dụng
                default: Console.WriteLine("Lựa chọn không hợp lệ."); break; // Báo lỗi nếu chọn không đúng
            }
        }
    }

    static void AddTodo() // Chức năng "thêm việc"
    {
        Console.Write("Nhập tiêu đề công việc: "); // "Hỏi" người dùng "nhập" tên việc
        string title = Console.ReadLine(); // "Đọc" tên việc từ người dùng
        _todoList.Add(new TodoItem { Id = _nextId++, Title = title, IsCompleted = false }); // "Thêm" "việc" mới vào "rổ" _todoList, "tạo" "mã số" tự tăng, "trạng thái" "chưa xong"
        Console.WriteLine("Công việc đã được thêm."); // Thông báo "thêm thành công"
    }

    static void ShowAllTodos() // Chức năng "xem tất cả việc"
    {
        if (!_todoList.Any()) // "Kiểm tra" xem "rổ" _todoList có "rỗng" không? (dùng "chiêu" Any của LINQ)
        {
            Console.WriteLine("Danh sách công việc trống."); // Thông báo "rổ" rỗng
            return; // "Thoát" khỏi chức năng
        }
        Console.WriteLine("--- Tất cả công việc ---"); // "Tiêu đề" danh sách việc
        foreach (var todo in _todoList) // Duyệt qua từng "việc" trong "rổ" _todoList
        {
            Console.WriteLine(todo); // "In ra" thông tin "việc" (dùng ToString() đã "chế biến" ở trên)
        }
    }

    static void ShowIncompleteTodos() // Chức năng "xem việc chưa xong"
    {
        var incompleteTodos = _todoList.Where(todo => !todo.IsCompleted); // "Lọc" "rổ" _todoList để "lấy" các "việc" "chưa xong" (dùng "chiêu" Where của LINQ)
        if (!incompleteTodos.Any()) // "Kiểm tra" xem "rổ" "việc chưa xong" có "rỗng" không? (dùng "chiêu" Any của LINQ)
        {
            Console.WriteLine("Không có công việc chưa hoàn thành."); // Thông báo "không có việc chưa xong"
            return; // "Thoát" khỏi chức năng
        }
        Console.WriteLine("--- Công việc chưa hoàn thành ---"); // "Tiêu đề" danh sách "việc chưa xong"
        foreach (var todo in incompleteTodos) // Duyệt qua "rổ" "việc chưa xong"
        {
            Console.WriteLine(todo); // "In ra" thông tin "việc"
        }
    }

    static void MarkAsCompleted() // Chức năng "đánh dấu xong việc"
    {
        Console.Write("Nhập ID công việc muốn đánh dấu hoàn thành: "); // "Hỏi" người dùng "nhập" "mã số" "việc"
        if (int.TryParse(Console.ReadLine(), out int id)) // "Đọc" "mã số" và "kiểm tra" xem có phải số không
        {
            var todo = _todoList.FirstOrDefault(t => t.Id == id); // "Tìm" "việc" có "mã số" trùng khớp trong "rổ" _todoList (dùng "chiêu" FirstOrDefault của LINQ)
            if (todo != null) // Nếu "tìm" thấy "việc"
            {
                todo.IsCompleted = true; // "Đánh dấu" "trạng thái" "việc" là "xong"
                Console.WriteLine($"Công việc ID {id} đã được đánh dấu hoàn thành."); // Thông báo "đánh dấu thành công"
            }
            else
            {
                Console.WriteLine($"Không tìm thấy công việc với ID {id}."); // Thông báo "không tìm thấy"
            }
        }
        else
        {
            Console.WriteLine("ID không hợp lệ."); // Thông báo "mã số" không hợp lệ
        }
    }

    static void DeleteTodo() // Chức năng "xóa việc"
    {
        Console.Write("Nhập ID công việc muốn xóa: "); // "Hỏi" người dùng "nhập" "mã số" "việc"
        if (int.TryParse(Console.ReadLine(), out int id)) // "Đọc" "mã số" và "kiểm tra" xem có phải số không
        {
            var todo = _todoList.FirstOrDefault(t => t.Id == id); // "Tìm" "việc" có "mã số" trùng khớp trong "rổ" _todoList (dùng "chiêu" FirstOrDefault của LINQ)
            if (todo != null) // Nếu "tìm" thấy "việc"
            {
                _todoList.Remove(todo); // "Xóa" "việc" khỏi "rổ" _todoList
                Console.WriteLine($"Công việc ID {id} đã được xóa."); // Thông báo "xóa thành công"
            }
            else
            {
                Console.WriteLine($"Không tìm thấy công việc với ID {id}."); // Thông báo "không tìm thấy"
            }
        }
        else
        {
            Console.WriteLine("ID không hợp lệ."); // Thông báo "mã số" không hợp lệ
        }
    }

    static void SearchTodos() // Chức năng "tìm kiếm việc" theo "tên"
    {
        Console.Write("Nhập từ khóa tìm kiếm: "); // "Hỏi" người dùng "nhập" "từ khóa"
        string keyword = Console.ReadLine(); // "Đọc" "từ khóa" từ người dùng
        if (string.IsNullOrWhiteSpace(keyword)) // "Kiểm tra" xem "từ khóa" có "rỗng" không
        {
            Console.WriteLine("Từ khóa tìm kiếm không được để trống."); // Thông báo "từ khóa" không được rỗng
            return; // "Thoát" khỏi chức năng
        }
        var searchResults = _todoList.Where(todo => todo.Title.Contains(keyword, StringComparison.OrdinalIgnoreCase)); // "Lọc" "rổ" _todoList để "lấy" các "việc" có "tên" chứa "từ khóa" (dùng "chiêu" Where và Contains của LINQ, "tìm kiếm" "không phân biệt" chữ hoa chữ thường)
        if (!searchResults.Any()) // "Kiểm tra" xem "rổ" "kết quả tìm kiếm" có "rỗng" không? (dùng "chiêu" Any của LINQ)
        {
            Console.WriteLine($"Không tìm thấy công việc nào chứa từ khóa '{keyword}'."); // Thông báo "không tìm thấy"
            return; // "Thoát" khỏi chức năng
        }
        Console.WriteLine($"--- Kết quả tìm kiếm cho '{keyword}' ---"); // "Tiêu đề" danh sách "kết quả tìm kiếm"
        foreach (var todo in searchResults) // Duyệt qua "rổ" "kết quả tìm kiếm"
        {
            Console.WriteLine(todo); // "In ra" thông tin "việc"
        }
    }
}
```

**Trong ví dụ này, chúng ta đã "dùng" LINQ to Objects để:**

- **`_todoList.Where(todo => !todo.IsCompleted)`:** "Lọc" "rổ" "việc cần làm" để "lấy" các "việc" "chưa xong".
    - **`!_todoList.Any()`:** "Kiểm tra" xem "rổ" "việc cần làm" có "rỗng" không.
    - **`_todoList.FirstOrDefault(t => t.Id == id)`:** "Tìm" "việc" "đầu tiên" có "mã số" "trùng khớp" (hoặc "không có
      gì" nếu "không tìm thấy").
    - **`_todoList.Where(todo => todo.Title.Contains(keyword, StringComparison.OrdinalIgnoreCase))`:** "Tìm kiếm" "việc"
      theo "tên", "không quan tâm" chữ hoa chữ thường.

Ví dụ này "minh họa" cách LINQ to Objects giúp "thao tác" và "hỏi han" dữ liệu trong "bộ nhớ" một cách "gọn gàng" và "dễ
hiểu", làm cho code ứng dụng trở nên "đơn giản" và "dễ bảo trì" hơn.

**8.2. Ví dụ ứng dụng LINQ to XML để xử lý cấu hình hoặc dữ liệu XML - "Làm Việc" Với XML "Nhẹ Nhàng"**

**Ví dụ: "Đọc" "cài đặt" ứng dụng từ file XML "cấu hình"**

Giả sử chúng ta có một file "cấu hình" XML (`appsettings.xml`) chứa các "thông tin" "cài đặt" ứng dụng:

```xml
<?xml version="1.0" encoding="utf-8"?>
<appSettings>
  <applicationName>My Application</applicationName>
  <logLevel>Information</logLevel>
  <database>
    <connectionString>Server=.;Database=MyAppDB;Trusted_Connection=True;</connectionString>
    <provider>SqlServer</provider>
  </database>
</appSettings>
```

Chúng ta có thể "dùng" LINQ to XML để "đọc" file "cấu hình" này và "lấy" các "giá trị" "cài đặt" một cách "dễ thở":

```csharp
using System;
using System.Xml.Linq; // "Nhập" LINQ to XML

public class AppConfigReader // Class "đọc" "cài đặt" ứng dụng
{
    public static void Main(string[] args) // "Cổng" chính
    {
        string configFilePath = "appsettings.xml"; // "Đường đi" đến file "cấu hình" XML

        try // "Bắt đầu" "thử" "đọc" file "cấu hình" (có thể "xảy ra sự cố")
        {
            XDocument configDoc = XDocument.Load(configFilePath); // "Mở" file XML "cấu hình" (dùng LINQ to XML)

            // "Lấy" "giá trị" "cài đặt" bằng LINQ to XML - "hỏi han" XML bằng LINQ
            string appName = configDoc.Root.Element("applicationName").Value; // "Lấy" "nội dung" của "phần tử" <applicationName>
            string logLevel = configDoc.Root.Element("logLevel").Value;       // "Lấy" "nội dung" của "phần tử" <logLevel>
            string connectionString = configDoc.Root.Element("database").Element("connectionString").Value; // "Lấy" "nội dung" của <connectionString> bên trong <database>
            string dbProvider = configDoc.Root.Element("database").Element("provider").Value;             // "Lấy" "nội dung" của <provider> bên trong <database>

            Console.WriteLine("--- App Settings ---"); // "Tiêu đề" "thông tin" "cài đặt"
            Console.WriteLine($"Application Name: {appName}"); // In ra "tên ứng dụng"
            Console.WriteLine($"Log Level: {logLevel}");       // In ra "mức độ nhật ký"
            Console.WriteLine($"Connection String: {connectionString}"); // In ra "chuỗi kết nối database"
            Console.WriteLine($"Database Provider: {dbProvider}");     // In ra "nhà cung cấp database"

        }
        catch (Exception ex) // Nếu có "sự cố" khi "đọc" file "cấu hình"
        {
            Console.WriteLine($"Lỗi khi đọc file cấu hình: {ex.Message}"); // Thông báo "lỗi"
        }
    }
}
```

Trong ví dụ này, LINQ to XML "giúp sức" chúng ta:

- **`XDocument.Load(configFilePath)`:** "Mở" file XML "cấu hình".
    - **`configDoc.Root.Element("applicationName").Value`:** "Tiếp cận" các "phần tử" XML bằng "tên" và "lấy" "giá trị"
      của chúng.

LINQ to XML "trao tay" bạn một "cách" "trực quan" và "dễ dàng" để "thao tác" với dữ liệu "cấu hình" XML hoặc bất kỳ dữ
liệu XML nào khác trong ứng dụng của bạn.

**8.3. Ví dụ ứng dụng LINQ to Entities trong ứng dụng web hoặc desktop với cơ sở dữ liệu - "Web và Desktop 'Bắt Tay'
Database Với LINQ"**

**Ví dụ: Ứng dụng web ASP.NET Core "trình diễn" danh sách sản phẩm từ database**

Trong một ứng dụng web ASP.NET Core, chúng ta thường "nhờ cậy" Entity Framework Core để "giao tiếp" với cơ sở dữ liệu.
LINQ to Entities là "trợ thủ đắc lực" để "hỏi han" dữ liệu trong EF Core.

Giả sử chúng ta có một ứng dụng web ASP.NET Core MVC với một `DbContext` (`CuaHangDbContext`) và các entities (
`SanPham`) như đã "dựng" ở Chương 5. Chúng ta có thể "xây" một controller và action để "trình bày" "danh sách" sản phẩm
trên "mặt tiền" trang web:

```csharp
using Microsoft.AspNetCore.Mvc; // Để "dựng" Controller
using Microsoft.EntityFrameworkCore; // Để dùng EF Core
using System.Linq;              // Để dùng LINQ
using System.Threading.Tasks;     // Để dùng Task (bất đồng bộ)

public class SanPhamController : Controller // Class Controller "quản lý" sản phẩm
{
    private readonly CuaHangDbContext _dbContext; // "Trạm trung chuyển" DbContext (đã "chuẩn bị" ở Chương 5)

    public SanPhamController(CuaHangDbContext dbContext) // "Nhận" DbContext từ "bên ngoài" (Dependency Injection)
    {
        _dbContext = dbContext; // "Giữ" DbContext lại để dùng sau
    }

    public async Task<IActionResult> Index() // Action "trình diễn" "danh sách" sản phẩm trên trang web
    {
        // "Dùng" LINQ to Entities để "lấy" "danh sách" sản phẩm từ database - "hỏi han" database bằng LINQ
        var danhSachSanPham = await _dbContext.SanPhams // "Kho" sản phẩm (DbSet<SanPham> - bảng SanPhams trong database)
                                              .OrderBy(sp => sp.TenSanPham) // "Sắp xếp" theo "tên sản phẩm"
                                              .ToListAsync(); // "Ép" truy vấn "chạy" và "đổ" kết quả vào List<SanPham> ("lấy" kết quả "bất đồng bộ")

        return View(danhSachSanPham); // "Trao tay" "danh sách" sản phẩm cho "mặt tiền" (View) để "trình diễn"
    }

    // ... có thể "xây" thêm các actions khác ("Thêm", "Sửa", "Xóa", "Xem chi tiết", v.v.) ở đây
}
```

**Trong controller action `Index()`:**

- **`_dbContext.SanPhams.OrderBy(sp => sp.TenSanPham).ToListAsync()`:** "Dùng" LINQ to Entities để:

    - "Tiếp cận" `DbSet<SanPham>` (`_dbContext.SanPhams`).
    - "Sắp xếp" "danh sách" sản phẩm theo "tên" (`OrderBy`).
    - "Ép" truy vấn "ra quân" và "trao tay" `List<SanPham>` bằng `ToListAsync()` ("chạy" truy vấn "bất đồng bộ").

- **`return View(danhSachSanPham)`:** "Gửi" "danh sách" sản phẩm "lấy" từ database cho "mặt tiền" (View) để "trình diễn"
  trên trang web.

Trong "mặt tiền" (View - ví dụ: `Index.cshtml`), bạn có thể "dạo" qua `Model` ("danh sách" sản phẩm) và "trình bày" "
thông tin" sản phẩm:

```cshtml
@model List<SanPham> // "Khai báo" View này sẽ "nhận" dữ liệu kiểu List<SanPham>

@{
    ViewData["Title"] = "Danh sách sản phẩm"; // "Đặt tên" "tiêu đề" trang web
}

<h1>@ViewData["Title"]</h1> // "Hiển thị" "tiêu đề"

<table class="table"> // "Bảng" HTML để "trình bày" dữ liệu
    <thead> // "Đầu bảng"
        <tr>
            <th>Tên sản phẩm</th> // "Cột" "tên sản phẩm"
            <th>Giá</th>            // "Cột" "giá"
            <th>Danh mục</th>       // "Cột" "danh mục"
        </tr>
    </thead>
    <tbody> // "Thân bảng" - dữ liệu sản phẩm sẽ "hiển thị" ở đây
        @foreach (var sanPham in Model) // "Dạo" qua từng "sản phẩm" trong "rổ" Model (danh sách sản phẩm)
        {
            <tr>
                <td>@sanPham.TenSanPham</td> // "Hiển thị" "tên sản phẩm"
                <td>@sanPham.Gia</td>           // "Hiển thị" "giá"
                <td>@sanPham.DanhMucSanPham</td>      // "Hiển thị" "danh mục"
            </tr>
        }
    </tbody>
</table>
```

Ví dụ này "cho thấy" cách LINQ to Entities "kết hợp" "ăn ý" với EF Core và ASP.NET Core để "xây dựng" các ứng dụng web "
tương tác" với database một cách "mượt mà". LINQ giúp "hỏi han" dữ liệu từ database "dễ dàng" và "an toàn" về kiểu dữ
liệu, làm cho code backend trở nên "gọn" và "dễ bảo trì". Tương tự, LINQ to Entities cũng được "trọng dụng" trong các
ứng dụng desktop (WPF, WinForms) để "tiếp cận" và "thao tác" dữ liệu database.

**Tổng Kết Chương 8:**

- Chúng ta đã "chiêm ngưỡng" các ví dụ "ứng dụng" "thực tế" của LINQ trong:
    - Ứng dụng console "nhỏ xinh" (To-Do List) dùng LINQ to Objects.
    - "Xử lý" file "cấu hình" XML dùng LINQ to XML.
    - Ứng dụng web ASP.NET Core với database dùng LINQ to Entities.

Các ví dụ này chỉ là "phần nổi của tảng băng chìm" trong "vũ trụ" ứng dụng của LINQ. LINQ là một "công cụ" "đa năng" có
thể "góp mặt" trong hầu hết mọi "loại hình" ứng dụng .NET, giúp bạn "làm chủ" dữ liệu một cách "hiệu quả", "dễ dàng", và
viết code C# "thanh lịch" hơn.

**"Lời Chúc" "Kết Hành Trình":**

Chúc mừng bạn đã "vượt qua" "hành trình" "khám phá" LINQ từ "vạch xuất phát" đến "vạch đích" "chuyên nghiệp"!

Bạn đã "băng qua" một "quãng đường dài",
