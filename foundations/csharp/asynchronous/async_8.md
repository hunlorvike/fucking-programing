# Chương 8: Ứng Dụng Thực Tế Của Bất Đồng Bộ - "Bất Đồng Bộ Đi Muôn Nơi" - "Bất Đồng Bộ Trong Đời Sống Ứng Dụng"

Chào mừng bạn đến với **Chương 8: Ứng Dụng Thực Tế Của Bất Đồng Bộ - "Bất Đồng Bộ Đi Muôn Nơi"**! Trong chương "kết màn"
này, chúng ta sẽ "dạo một vòng" thế giới ứng dụng thực tế để "thấy" bất đồng bộ "góp mặt" ở khắp mọi "ngóc ngách", và "
giúp ích" cho các ứng dụng phần mềm "như thế nào".

**8.1. Ví dụ ứng dụng console đơn giản sử dụng bất đồng bộ - "Ứng Dụng Console 'Nhanh Như Điện'"**

**Ví dụ: Ứng dụng console "tải" nhiều trang web "song song"**

Chúng ta sẽ "xây dựng" một ứng dụng console "nhỏ gọn" để "tải" nội dung của **nhiều** trang web **"đồng thời"** (song
song) bằng lập trình bất đồng bộ. Ứng dụng sẽ:

1. "Liệt kê" danh sách các URL trang web cần "tải".
2. "Tải" nội dung của từng trang web một cách **"bất đồng bộ"** (sử dụng `HttpClient`).
3. "Hiển thị" "tiêu đề" và "độ dài" nội dung của từng trang web sau khi "tải" xong.
4. "Tính toán" và "hiển thị" "tổng thời gian" "tải" **tất cả** các trang web.

```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Threading.Tasks;

public class AsyncConsoleAppExample
{
    static async Task Main(string[] args)
    {
        string[] urls = { // "Danh sách" "địa chỉ" web cần "tải"
            "https://www.example.com",
            "https://www.microsoft.com",
            "https://www.google.com",
            "https://www.amazon.com",
            "https://vnexpress.net",
            "https://kenh14.vn"
        };

        Console.WriteLine("Bắt đầu tải song song nhiều trang web từ console..."); // Thông báo "bắt đầu"

        Stopwatch sw = Stopwatch.StartNew(); // Bấm giờ "đo" "thời gian chạy"

        using (HttpClient client = new HttpClient()) // "Tạo" HttpClient
        {
            // "Tạo" danh sách các Task<WebPageInfo> để "tải" thông tin từng trang web "bất đồng bộ"
            List<Task<WebPageInfo>> downloadTasks = new List<Task<WebPageInfo>>();
            foreach (string url in urls)
            {
                downloadTasks.Add(TaiThongTinTrangWebAsync(client, url)); // "Thêm" Task "tải" thông tin trang web vào danh sách
            }

            // "Chờ" **tất cả** các Task "tải" trang web "hoàn thành" (Task.WhenAll)
            WebPageInfo[] trangWebInfos = await Task.WhenAll(downloadTasks); // 'await' Task.WhenAll để "chờ" "tất cả" "xong việc"

            Console.WriteLine("\n--- Thông tin trang web đã tải ---");
            foreach (var webInfo in trangWebInfos) // Duyệt qua "thông tin" từng trang web
            {
                Console.WriteLine($"URL: {webInfo.Url}"); // In ra "địa chỉ" web
                Console.WriteLine($"Tiêu đề: {webInfo.Title}"); // In ra "tiêu đề" trang
                Console.WriteLine($"Độ dài nội dung: {webInfo.ContentLength:#,##0} bytes"); // In ra "độ dài" nội dung
                Console.WriteLine("---");
            }

            sw.Stop(); // Dừng bấm giờ

            Console.WriteLine($"\nTải song song tất cả các trang web thành công sau: {sw.ElapsedMilliseconds}ms"); // Thông báo "thành công" và "thời gian chạy"
        }

        Console.WriteLine("\nChương trình kết thúc."); // Thông báo "kết thúc"
        Console.ReadKey();
    }

    // Class "chứa" "thông tin" trang web
    class WebPageInfo
    {
        public string Url { get; set; }   // "Địa chỉ" web
        public string Title { get; set; } // "Tiêu đề" trang
        public int ContentLength { get; set; } // "Độ dài" nội dung
    }

    // "Chiêu" "tải" "thông tin" trang web "bất đồng bộ" và "trả về" WebPageInfo
    static async Task<WebPageInfo> TaiThongTinTrangWebAsync(HttpClient client, string url)
    {
        Console.WriteLine($"Bắt đầu tải trang web: {url}"); // Thông báo "bắt đầu" "tải" trang

        HttpResponseMessage response = await client.GetAsync(url); // "Tải" trang web "bất đồng bộ"
        response.EnsureSuccessStatusCode();

        string htmlContent = await response.Content.ReadAsStringAsync(); // "Đọc" "nội dung" HTML "bất đồng bộ"

        string title = TachTieuDeTrangWeb(htmlContent); // "Lấy" "tiêu đề" trang từ nội dung HTML (hàm "tách" riêng - xem bên dưới)

        Console.WriteLine($"Tải trang web thành công: {url}"); // Thông báo "tải thành công"

        return new WebPageInfo // "Trả về" "thông tin" trang web
        {
            Url = url,
            Title = title,
            ContentLength = htmlContent.Length // "Độ dài" nội dung HTML
        };
    }

    // "Chiêu" "tách" "tiêu đề" trang web từ nội dung HTML (hàm "phụ trợ" - không liên quan đến bất đồng bộ lắm)
    static string TachTieuDeTrangWeb(string htmlContent)
    {
        string title = "Không tìm thấy tiêu đề"; // "Giá trị mặc định" nếu không tìm thấy tiêu đề

        var titleStartTag = "<title>"; // Tag "bắt đầu" tiêu đề
        var titleEndTag = "</title>";   // Tag "kết thúc" tiêu đề

        int startIndex = htmlContent.IndexOf(titleStartTag, StringComparison.OrdinalIgnoreCase); // "Tìm" vị trí tag "bắt đầu"
        if (startIndex != -1) // Nếu "tìm" thấy tag "bắt đầu"
        {
            startIndex += titleStartTag.Length; // "Dịch" vị trí bắt đầu đến sau tag "bắt đầu"
            int endIndex = htmlContent.IndexOf(titleEndTag, startIndex, StringComparison.OrdinalIgnoreCase); // "Tìm" vị trí tag "kết thúc" từ vị trí "bắt đầu"
            if (endIndex != -1) // Nếu "tìm" thấy tag "kết thúc"
            {
                title = htmlContent.Substring(startIndex, endIndex - startIndex).Trim(); // "Cắt" chuỗi "tiêu đề" từ giữa tag "bắt đầu" và tag "kết thúc", "loại bỏ" khoảng trắng thừa
            }
        }
        return title; // "Trả về" "tiêu đề" trang web (hoặc "giá trị mặc định" nếu không tìm thấy)
    }
}
```

**"Chạy" ứng dụng và "quan sát":**

- Ứng dụng sẽ "tải" nội dung của **nhiều** trang web **"song song"** (bất đồng bộ).
    - Thời gian "tổng cộng" để "tải" **tất cả** các trang web sẽ **"nhanh hơn"** đáng kể so với khi "tải" **"lần lượt"
      ** (đồng bộ).
    - Ứng dụng vẫn "phản hồi" tốt trong khi "tải" các trang web, không bị "đứng hình".

**8.2. Ví dụ ứng dụng desktop (WPF) sử dụng bất đồng bộ - "Ứng Dụng Desktop 'Mượt Mà' "**

**Ví dụ: Ứng dụng WPF "hiển thị danh sách ảnh" từ thư mục "bất đồng bộ"**

Chúng ta sẽ "xây dựng" một ứng dụng WPF "đơn giản" để "hiển thị" "danh sách" các file ảnh từ một thư mục. Ứng dụng sẽ:

1. Cho phép người dùng "chọn" một thư mục chứa ảnh.
2. "Đọc" danh sách các file ảnh từ thư mục đã chọn một cách **"bất đồng bộ"**.
3. "Tải" "thumbnail" (ảnh thu nhỏ) của từng file ảnh một cách **"bất đồng bộ"**.
4. "Hiển thị" "thumbnail" của các ảnh lên giao diện người dùng WPF.
5. "Đảm bảo" giao diện người dùng **"luôn 'phản hồi' "**, không bị "đứng hình" trong quá trình "đọc file" và "tải
   thumbnail".

(Để chạy ví dụ này, bạn cần tạo một dự án WPF App (.NET Framework hoặc .NET Core) và thêm code vào file
MainWindow.xaml.cs)

```csharp
// MainWindow.xaml.cs (code-behind file của MainWindow.xaml trong dự án WPF)
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Media.Imaging; // "Nhập" không gian tên cho BitmapImage
using System.Windows.Threading;   // "Nhập" không gian tên cho Dispatcher

namespace WpfAsyncExample
{
    public partial class MainWindow : Window // MainWindow class
    {
        public MainWindow() // Constructor
        {
            InitializeComponent(); // "Khởi tạo" giao diện người dùng
        }

        private async void btnSelectFolder_Click(object sender, RoutedEventArgs e) // Event handler "bất đồng bộ" cho button "Chọn thư mục" - dùng 'async void' (event handler)
        {
            System.Windows.Forms.FolderBrowserDialog folderDialog = new System.Windows.Forms.FolderBrowserDialog(); // "Hộp thoại" chọn thư mục
            System.Windows.Forms.DialogResult result = folderDialog.ShowDialog(); // "Hiển thị" hộp thoại và "chờ" người dùng "chọn" thư mục

            if (result == System.Windows.Forms.DialogResult.OK) // Nếu người dùng "chọn" thư mục và bấm "OK"
            {
                string folderPath = folderDialog.SelectedPath; // "Lấy" "đường dẫn" thư mục đã chọn
                await LoadImagesAsync(folderPath); // "Gọi" phương thức "tải ảnh" "bất đồng bộ" và "chờ"
            }
        }

        async Task LoadImagesAsync(string folderPath) // Phương thức "tải ảnh" "bất đồng bộ" - dùng 'async Task'
        {
            imageList.Items.Clear(); // "Xóa" danh sách ảnh cũ trên giao diện

            string[] imageFiles = null; // "Danh sách" file ảnh

            try // "Bắt đầu" "thử" "đọc" danh sách file ảnh (có thể "xảy ra lỗi" file)
            {
                btnSelectFolder.IsEnabled = false; // "Khóa" button "Chọn thư mục" trong khi "tải" ảnh
                imageFiles = await Task.Run(() => Directory.GetFiles(folderPath, "*.jpg")); // "Đọc" danh sách file ảnh "bất đồng bộ" trên Thread Pool - dùng Task.Run và await
            }
            catch (Exception ex) // "Bắt" lỗi "đọc" file
            {
                MessageBox.Show($"Lỗi đọc thư mục: {ex.Message}"); // Thông báo "lỗi"
                btnSelectFolder.IsEnabled = true; // "Mở khóa" button "Chọn thư mục" khi "lỗi"
                return; // "Thoát" khỏi phương thức
            }

            if (imageFiles.Length == 0) // Nếu không có file ảnh nào
            {
                MessageBox.Show("Không tìm thấy file ảnh trong thư mục đã chọn."); // Thông báo "không tìm thấy ảnh"
                btnSelectFolder.IsEnabled = true; // "Mở khóa" button "Chọn thư mục"
                return; // "Thoát" khỏi phương thức
            }

            List<BitmapImage> bitmaps = new List<BitmapImage>(); // "Danh sách" BitmapImage (ảnh thu nhỏ)

            progressBar.Visibility = Visibility.Visible; // "Hiển thị" progress bar
            progressBar.Maximum = imageFiles.Length;    // "Đặt" giá trị "tối đa" cho progress bar
            progressBar.Value = 0;                      // "Đặt" giá trị "hiện tại" về 0

            foreach (string imageFile in imageFiles) // Duyệt qua từng file ảnh
            {
                BitmapImage bitmapImage = await LoadBitmapImageAsync(imageFile); // "Tải" "thumbnail" "bất đồng bộ" và "chờ"
                bitmaps.Add(bitmapImage); // "Thêm" "thumbnail" vào danh sách
                imageList.Items.Add(bitmapImage); // "Hiển thị" "thumbnail" lên ListBox trên giao diện
                progressBar.Value++;              // "Tăng" giá trị progress bar
            }

            progressBar.Visibility = Visibility.Hidden; // "Ẩn" progress bar khi "tải" xong

            ```csharp
                    .WriteLine($"\nTải ảnh bất đồng bộ thành công từ thư mục: {folderPath} sau: {sw.ElapsedMilliseconds}ms"); // Thông báo "thành công" và "thời gian chạy"

            btnSelectFolder.IsEnabled = true; // "Mở khóa" button "Chọn thư mục" sau khi "tải" xong
        }

        // "Chiêu" "tải" "thumbnail" (ảnh thu nhỏ) "bất đồng bộ" và "trả về" BitmapImage
        async Task<BitmapImage> LoadBitmapImageAsync(string imageFile) // "Trả về" Task<BitmapImage> - "công việc" "tải ảnh" "bất đồng bộ" và "trả về" BitmapImage
        {
            return await Dispatcher.InvokeAsync(() => // "Chuyển" sang luồng UI để "tạo" BitmapImage (vì BitmapImage cần được tạo trên luồng UI trong WPF) - dùng Dispatcher.InvokeAsync và await
            {
                BitmapImage bitmapImage = new BitmapImage(); // Tạo BitmapImage (ảnh thu nhỏ)
                bitmapImage.BeginInit(); // Bắt đầu "khởi tạo" BitmapImage
                bitmapImage.UriSource = new Uri(imageFile); // "Đặt" "đường dẫn" file ảnh cho BitmapImage
                bitmapImage.DecodePixelWidth = 100; // "Đặt" "chiều rộng" "ảnh thu nhỏ" (100 pixels)
                bitmapImage.CacheOption = BitmapCacheOption.CacheOnLoad; // "Cache" ảnh vào bộ nhớ sau khi "tải" xong
                bitmapImage.EndInit();   // Kết thúc "khởi tạo"
                return bitmapImage;       // "Trả về" BitmapImage (ảnh thu nhỏ)
            }, DispatcherPriority.Background); // "Ưu tiên" Background để "không làm chậm" UI
        }
    }
}
```

**MainWindow.xaml (giao diện người dùng WPF cho ví dụ trên):**

```xml
<Window x:Class="WpfAsyncExample.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Async Image Viewer" Height="450" Width="800">
    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
            <RowDefinition Height="Auto"/>
        </Grid.RowDefinitions>

        <Button x:Name="btnSelectFolder" Content="Chọn Thư Mục Ảnh" Margin="10" Padding="5" Click="btnSelectFolder_Click"/>

        <ListBox x:Name="imageList" Grid.Row="1" Margin="10" ItemsPanel="{ItemsPanelTemplate}">
            <ListBox.ItemsPanel>
                <ItemsPanelTemplate>
                    <WrapPanel IsItemsHost="True" Orientation="Horizontal"/>
                </ItemsPanelTemplate>
            </ListBox.ItemsPanel>
            <ListBox.ItemTemplate>
                <DataTemplate>
                    <Image Source="{Binding}" Width="100" Height="100" Margin="5"/>
                </DataTemplate>
            </ListBox.ItemTemplate>
        </ListBox>

        <ProgressBar x:Name="progressBar" Grid.Row="2" Margin="10" IsIndeterminate="False" Visibility="Hidden"/>
    </Grid>
</Window>
```

**"Chạy" ứng dụng WPF và "quan sát":**

- Khi bạn "bấm" button "Chọn Thư Mục Ảnh", ứng dụng sẽ "hiển thị" hộp thoại để bạn "chọn" thư mục.
    - Sau khi bạn "chọn" thư mục và bấm "OK", ứng dụng sẽ "bắt đầu" "tải" danh sách file ảnh và "thumbnail" một cách **"
      bất đồng bộ"**.
    - Trong quá trình "tải", giao diện người dùng **"vẫn 'phản hồi' "**, bạn vẫn có thể "tương tác" với các phần khác
      của ứng dụng (ví dụ: di chuyển cửa sổ, bấm button khác - nếu có).
    - Progress bar sẽ "hiển thị" "tiến trình" "tải" ảnh.
    - Khi "tải" xong, "thumbnail" của các ảnh sẽ được "hiển thị" lên ListBox trên giao diện.

**8.3. Ví dụ ứng dụng web ASP.NET Core sử dụng bất đồng bộ - "Ứng Dụng Web 'Nhanh Nhẹn' "**

**Ví dụ: Ứng dụng ASP.NET Core MVC "hiển thị danh sách sản phẩm" từ database "bất đồng bộ"**

Trong ứng dụng web ASP.NET Core MVC, việc sử dụng lập trình bất đồng bộ là **"vô cùng quan trọng"** để đảm bảo ứng
dụng "phản hồi nhanh chóng" và "xử lý" nhiều "yêu cầu" đồng thời một cách "hiệu quả".

Giả sử chúng ta có một ứng dụng ASP.NET Core MVC với `DbContext` và entities như đã "dựng" ở Chương 5. Chúng ta sẽ "
chỉnh sửa" controller và action để "lấy" danh sách sản phẩm từ database và "trình bày" lên trang web một cách **"bất
đồng bộ"**.

```csharp
// SanPhamController.cs (Controller cho sản phẩm trong ứng dụng ASP.NET Core MVC)
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore; // "Nhập" EF Core
using System.Linq;
using System.Threading.Tasks; // "Nhập" Task

public class SanPhamController : Controller // Class Controller "quản lý" sản phẩm
{
    private readonly CuaHangDbContext _dbContext; // "Trạm trung chuyển" DbContext (đã "chuẩn bị" ở Chương 5)

    public SanPhamController(CuaHangDbContext dbContext) // Constructor - "nhận" DbContext từ Dependency Injection
    {
        _dbContext = dbContext;
    }

    public async Task<IActionResult> Index() // Action "trình diễn" "danh sách" sản phẩm - "bất đồng bộ" (async Task<IActionResult>)
    {
        // "Lấy" danh sách sản phẩm từ database "bất đồng bộ" (dùng ToListAsync)
        var danhSachSanPham = await _dbContext.SanPhams // "Kho" sản phẩm (DbSet<SanPham> - bảng SanPhams)
                                              .OrderBy(sp => sp.TenSanPham) // "Sắp xếp" theo "tên sản phẩm"
                                              .ToListAsync(); // "Ép" truy vấn "chạy" và "đổ" kết quả vào List<SanPham> **"bất đồng bộ"** (ToListAsync) - 'await' ở đây

        return View(danhSachSanPham); // "Trả về" View "cùng" "danh sách" sản phẩm
    }

    // ... (các actions khác - "thêm", "sửa", "xóa", "chi tiết", v.v. - cũng nên "xây" "bất đồng bộ") ...
}
```

**"Điểm nhấn" bất đồng bộ trong code ASP.NET Core MVC:**

- **`public async Task<IActionResult> Index()`:** Action `Index()` được "phù phép" thành "phương thức bất đồng bộ" bằng
  `async Task<IActionResult>`.
    - **`await _dbContext.SanPhams.ToListAsync()`:** "Chiêu" `ToListAsync()` của EF Core là một "chiêu" **"bất đồng bộ"
      ** để "thực thi" truy vấn LINQ và "lấy" kết quả từ database. "Dùng" `await` để "chờ đợi" "bất đồng bộ" mà không
      làm "đứng hình" luồng ASP.NET request.

**View (Index.cshtml) - "Giữ nguyên" như ví dụ ở Chương 5 (không cần thay đổi).**

**"Chạy" ứng dụng web ASP.NET Core và "trải nghiệm":**

- Ứng dụng web sẽ "phản hồi" "nhanh chóng" hơn, đặc biệt khi database có "lượng dữ liệu lớn" hoặc "truy vấn" database "
  chậm chạp".
    - "Số lượng" request web được "xử lý" đồng thời có thể "tăng lên", "cải thiện" "khả năng mở rộng" của ứng dụng.
    - Người dùng sẽ có trải nghiệm "mượt mà" hơn, không phải "chờ đợi" lâu khi "tải" trang web.

**Tổng Kết Chương 8:**

- Bạn đã "chứng kiến" các ví dụ "ứng dụng thực tế" của lập trình bất đồng bộ trong:
    - Ứng dụng console "tải song song" nhiều trang web.
    - Ứng dụng desktop WPF "hiển thị ảnh" "bất đồng bộ".
    - Ứng dụng web ASP.NET Core MVC "trình bày" dữ liệu database "nhanh nhẹn".

Các ví dụ này "chứng minh" rằng lập trình bất đồng bộ **"không còn là 'lựa chọn' mà là 'yêu cầu bắt buộc' "** để xây
dựng các ứng dụng .NET "hiện đại", "phản hồi tốt", "hiệu quả", và "sẵn sàng" "đón đầu" tương lai.

**"Lời Chúc" "Kết Thúc Hành Trình":**

Chúc mừng bạn đã "về đích" "thành công" trong "hành trình" "khám phá" thế giới lập trình bất đồng bộ C#!

Bạn đã "vượt qua" một "chặng đường" "dài hơi", từ những "khái niệm" "khởi đầu", "cặp đôi" `async`/`await`, "viên gạch"
`Task`, "kiểu trả về", "xử lý lỗi", "hủy bỏ", "chiêu thức" "nâng cao", đến các "ứng dụng" "thực tế". Hy vọng rằng loạt
tài liệu này đã giúp bạn có được một "nền tảng" "vững chắc" và "tự tin" "ứng dụng" bất đồng bộ vào các dự án phần mềm
của mình.

**"Lời khuyên" "chân thành" "khép lại":**

- **"Thực hành" "không ngừng nghỉ":** "Chìa khóa" để "làm chủ" bất kỳ kỹ năng lập trình nào, kể cả bất đồng bộ, chính là
  **"thực hành"**. Hãy "viết code" bất đồng bộ thật nhiều, "thử sức" với các bài toán khác nhau, và "xây dựng" các ứng
  dụng nhỏ để "luyện tay".
- **"Tiếp tục" "mở rộng" "kiến thức":** Thế giới bất đồng bộ còn rất nhiều điều "thú vị" để "khám phá". Hãy "đọc thêm"
  tài liệu, "tham gia" cộng đồng, và "luôn cập nhật" những "kiến thức" mới nhất về bất đồng bộ và .NET.
- **"Chia sẻ" và "học hỏi" từ cộng đồng:** "Tham gia" các diễn đàn, nhóm cộng đồng .NET để "trao đổi", "hỏi đáp", và "
  học hỏi" kinh nghiệm từ những người "đồng môn".

Nếu bạn có bất kỳ câu hỏi nào khác về lập trình bất đồng bộ, hoặc muốn "chia sẻ" kinh nghiệm, đừng "ngần ngại" "lên
tiếng" nhé! Chúc bạn "gặt hái" nhiều "thành công" trên con đường chinh phục bất đồng bộ và .NET!

---

Hy vọng rằng phiên bản tài liệu này đã được "Việt hóa" và "dễ nuốt" hơn cho người mới bắt đầu! Let me know nếu bạn có
bất kỳ phản hồi hoặc yêu cầu chỉnh sửa nào khác nhé!