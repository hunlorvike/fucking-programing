# Chương 7: Bất Đồng Bộ Nâng Cao (Tùy Chọn) - "Lên Trình" Chuyên Gia Bất Đồng Bộ - "Bí Kíp" "Cao Thủ"

Chào mừng bạn đến với **Chương 7: Bất Đồng Bộ Nâng Cao (Tùy Chọn)**! Trong chương này, chúng ta sẽ "mở rộng" "tầm mắt"
và "nâng cấp" "kỹ năng" bất đồng bộ của bạn lên một "đẳng cấp" mới với các "chiêu thức" "cao cấp" hơn.

**7.1. `ConfigureAwait(false)` - "Bí Ẩn" Về "Ngữ Cảnh" (Context) - "Hiểu Sâu" Bên Trong `async`/`await`**

- **"Ngữ cảnh" (Context) trong `async`/`await` - "Sân Khấu" Cho "Công Việc" Bất Đồng Bộ:**

    - Khi bạn "chạy" code "đồng bộ" thông thường, code thường "chạy" trên một **"ngữ cảnh"** nhất định. "Ngữ cảnh" này
      có thể là "ngữ cảnh" của **luồng giao diện người dùng (UI thread)** trong ứng dụng GUI (WPF, WinForms, ASP.NET Web
      Forms), hoặc "ngữ cảnh" của **luồng ASP.NET request** trong ứng dụng web ASP.NET MVC/Core.
    - "Ngữ cảnh" này có thể cung cấp một số "tiện ích" đặc biệt, ví dụ: "đồng bộ hóa" với luồng UI, "quản lý" "trạng
      thái" request trong web app.

- **`await` và "ngữ cảnh" - "Trở Về 'Sân Khấu' Quen Thuộc" Sau "Chờ Đợi":**

    - "Mặc định", khi bạn dùng `await` để "chờ đợi" một "công việc bất đồng bộ" trong một "phương thức `async` ", sau
      khi "công việc" đó "hoàn thành", "phần code" "tiếp theo" sau `await` sẽ **"tự động 'nhảy' về 'chạy tiếp' trên 'ngữ
      cảnh' ban đầu"** (ngữ cảnh mà phương thức `async` được "gọi" đến).
    - Điều này thường **"hữu ích"** trong các ứng dụng GUI, vì nó "đảm bảo" rằng code "cập nhật giao diện người dùng" (
      ví dụ: `txtBox.Text = "Hello"`) sẽ được "chạy" trên **luồng UI**, "tránh" các lỗi "xung đột" luồng.

- **`ConfigureAwait(false)` - "Giải Phóng" Khỏi "Ngữ Cảnh" - "Chạy Tự Do" Hơn:**

    - `Task.ConfigureAwait(bool configureAwait)` là một "chiêu" giúp bạn **"điều khiển"** hành vi "trở về" "ngữ cảnh"
      sau `await`.
    - `ConfigureAwait(true)` (mặc định): "Ép" `await` phải "trở về" "ngữ cảnh" ban đầu sau khi "chờ đợi" xong.
    - `ConfigureAwait(false)`: **"Ra lệnh"** cho `await` là **"không cần 'trở về' " "ngữ cảnh" ban đầu"**. Thay vào
      đó, "phần code" "tiếp theo" sau `await` có thể được "chạy" trên **bất kỳ luồng nào "rảnh rỗi"** (thường là một
      luồng từ Thread Pool).

- **Khi nào nên "dùng" `ConfigureAwait(false)`? - "Tối Ưu Hiệu Năng" và "Tránh 'Khóa Chết' "**

    - **"Thư viện" và "code backend" "không liên quan" đến UI:** Trong các thư viện class library, các dự án backend,
      hoặc code "không trực tiếp" "cập nhật giao diện người dùng", bạn thường **"không cần"** "trở về" "ngữ cảnh" UI. "
      Dùng" `ConfigureAwait(false)` trong trường hợp này có thể mang lại một số "lợi ích":
        - **"Tăng" "hiệu năng" một chút:** "Tránh" "chi phí" "chuyển đổi" "ngữ cảnh" không cần thiết.
        - **"Ngăn chặn" "khóa chết" (deadlocks) tiềm ẩn:** Trong một số trường hợp "phức tạp" liên quan đến "ngữ cảnh"
          và "đồng bộ hóa", việc "dùng" `ConfigureAwait(false)` có thể giúp "tránh" "khóa chết".

    - **"Ứng dụng GUI" và "code 'cập nhật giao diện người dùng' ":** Trong các ứng dụng GUI, nếu bạn có code **"cập nhật
      giao diện người dùng"** (ví dụ: `txtBox.Text = "Hello"`) **"ngay sau"** `await`, bạn **"không nên"** "dùng"
      `ConfigureAwait(false)`. Hãy **"để mặc định"** (hoặc dùng `ConfigureAwait(true)` một cách "rõ ràng") để "đảm bảo"
      code "cập nhật UI" được "chạy" trên **luồng UI**.

- **Ví dụ: "Tải" trang web và "dùng" `ConfigureAwait(false)` để "giải phóng" khỏi "ngữ cảnh":**

  ```csharp
  using System;
  using System.Net.Http;
  using System.Threading.Tasks;

  public class ConfigureAwaitExample
  {
      static async Task Main(string[] args)
      {
          string url = "https://www.example.com"; // "Địa chỉ" trang web

          Console.WriteLine($"Bắt đầu tải trang web bất đồng bộ (ConfigureAwait(false)) từ: {url}"); // Thông báo "bắt đầu"

          using (HttpClient client = new HttpClient()) // "Tạo" HttpClient
          {
              try // "Bắt đầu" "thử" "tải" trang web
              {
                  // "Dùng" ConfigureAwait(false) - "ra lệnh" "không cần" "trở về" "ngữ cảnh"
                  HttpResponseMessage response = await client.GetAsync(url).ConfigureAwait(false); // Thêm '.ConfigureAwait(false)' vào sau 'await'
                  response.EnsureSuccessStatusCode();
                  string htmlContent = await response.Content.ReadAsStringAsync().ConfigureAwait(false); // Thêm '.ConfigureAwait(false)' vào sau 'await'

                  Console.WriteLine($"\nNội dung trang web (rút gọn):\n{htmlContent.Substring(0, 500)}..."); // In ra "nội dung"
                  Console.WriteLine($"\nTải trang web bất đồng bộ (ConfigureAwait(false)) thành công từ: {url}"); // Thông báo "thành công"
              }
              catch (HttpRequestException ex) // "Bắt" lỗi
              {
                  Console.WriteLine($"\nLỗi tải trang web: {ex.Message}"); // Thông báo "lỗi"
              }
          }

          Console.WriteLine("\nChương trình tiếp tục chạy sau khi tải trang web (ConfigureAwait(false))."); // Thông báo "tiếp tục"
          Console.ReadKey();
      }
  }
  ```

- **"Giải mã" `ConfigureAwait(false)`:**

    - `await client.GetAsync(url).ConfigureAwait(false);`: "Thêm" `.ConfigureAwait(false)` vào sau
      `await client.GetAsync(url)`. Điều này "ra lệnh" cho `await` là **"không cần 'trở về' " "ngữ cảnh" ban đầu** sau
      khi `GetAsync()` "xong việc". "Phần code" "tiếp theo" (sau `await`) có thể được "chạy" trên **bất kỳ luồng nào**.

**7.2. "Chạy song song" các "công việc" bất đồng bộ (`Task.WhenAll`, `Task.WhenAny`) - "Đa Nhiệm" "Siêu Đẳng"**

- **"Bài toán": "Chạy nhiều 'công việc bất đồng bộ' " "cùng lúc" và "chờ đợi" "tất cả" hoặc "một trong số" chúng "hoàn
  thành":**

    - Trong nhiều ứng dụng, bạn có thể muốn "thực hiện" **nhiều** "công việc bất đồng bộ" **"song song"** để "tăng
      tốc" "xử lý". Ví dụ: "tải" nhiều file từ internet "đồng thời", "gọi" nhiều API "cùng lúc", "xử lý" nhiều "yêu cầu"
      đồng thời trong web server.
    - Bạn có thể muốn **"chờ đợi"** cho đến khi **"tất cả"** các "công việc" "hoàn thành", hoặc chỉ cần **"chờ đợi"**
      cho đến khi **"một trong số"** các "công việc" "xong việc" (ví dụ: "lấy" kết quả "nhanh nhất" từ nhiều nguồn).

- **`Task.WhenAll(tasks)` - "Chờ Đợi" "Tất Cả Cùng Về Đích":**

    - `Task.WhenAll(Task[])`: "Nhận" vào một "mảng" các `Task` (hoặc `Task<T>`).
    - "Trả về" một `Task` **mới** sẽ "hoàn thành" **chỉ khi** **tất cả** các `Task` trong "mảng" **đã "hoàn thành"**.
    - Nếu các `Task` trong "mảng" là `Task<T>`, `Task.WhenAll` sẽ "trả về" `Task<T[]>`, chứa một "mảng" các "kết quả" từ
      các `Task` "con".
    - "Dùng" `await Task.WhenAll(...)` để "chờ đợi" "tất cả" các `Task` "hoàn thành" một cách **"bất đồng bộ"**.

- **`Task.WhenAny(tasks)` - "Chờ Đợi" "Ai Về Đích Trước":**

    - `Task.WhenAny(Task[])`: "Nhận" vào một "mảng" các `Task` (hoặc `Task<T>`).
    - "Trả về" một `Task<Task>` **mới** sẽ "hoàn thành" **ngay khi** **bất kỳ** `Task` nào trong "mảng" **"hoàn thành" "
      đầu tiên"**.
    - "Dùng" `await Task.WhenAny(...)` để "chờ đợi" **"món đồ" `Task` "xong việc" "nhanh nhất"** một cách **"bất đồng
      bộ"**.

- **Ví dụ: "Tải song song" nhiều trang web bằng `Task.WhenAll` và `Task.WhenAny`:**

  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Diagnostics;
  using System.Net.Http;
  using System.Threading.Tasks;

  public class TaskWhenAllWhenAnyExample
  {
      static async Task Main(string[] args)
      {
          string[] urls = { // "Danh sách" "địa chỉ" web muốn "tải"
              "https://www.example.com",
              "https://www.microsoft.com",
              "https://www.google.com",
              "https://www.amazon.com"
          };

          Console.WriteLine("Bắt đầu tải song song nhiều trang web..."); // Thông báo "bắt đầu"

          Stopwatch sw = Stopwatch.StartNew(); // Bấm giờ "đo" "thời gian chạy"

          using (HttpClient client = new HttpClient()) // "Tạo" HttpClient
          {
              // "Tạo" danh sách các Task<string> để "tải" từng trang web "bất đồng bộ"
              List<Task<string>> downloadTasks = new List<Task<string>>();
              foreach (string url in urls)
              {
                  downloadTasks.Add(TaiTrangWebAsync(client, url)); // "Thêm" Task "tải" trang web vào danh sách
              }

              // "Chờ" **tất cả** các Task "tải" trang web "hoàn thành" (Task.WhenAll)
              string[] htmlContents = await Task.WhenAll(downloadTasks); // 'await' Task.WhenAll để "chờ" "tất cả" "xong việc"

              Console.WriteLine($"\n--- Nội dung trang web (rút gọn) ---");
              for (int i = 0; i < urls.Length; i++) // Duyệt qua kết quả "tải"
              {
                  Console.WriteLine($"\n{urls[i]}:\n{htmlContents[i].Substring(0, 200)}..."); // In ra "nội dung" "rút gọn" của từng trang web
              }

              Console.WriteLine($"\nĐã tải song song tất cả các trang web thành công sau: {sw.ElapsedMilliseconds}ms"); // Thông báo "thành công" và "thời gian chạy"

              Console.WriteLine("\n--- Thử nghiệm Task.WhenAny ---");

              sw.Restart(); // "Bấm giờ" lại

              // "Chờ" **bất kỳ** Task "tải" trang web nào "hoàn thành" "đầu tiên" (Task.WhenAny)
              Task<string> firstCompletedTask = await Task.WhenAny(downloadTasks); // 'await' Task.WhenAny để "chờ" "món đồ" "xong việc" "nhanh nhất"

              Console.WriteLine($"\nTrang web tải xong đầu tiên:\n{firstCompletedTask.Result.Substring(0, 500)}..."); // In ra "nội dung" "rút gọn" của trang web "về đích" đầu tiên
              Console.WriteLine($"\nĐã tải xong trang web đầu tiên (Task.WhenAny) sau: {sw.ElapsedMilliseconds}ms"); // Thông báo "thành công" và "thời gian chạy"

          }

          Console.WriteLine("\nChương trình tiếp tục chạy sau khi tải song song (Task.WhenAll và Task.WhenAny)."); // Thông báo "tiếp tục"
          Console.ReadKey();
      }

      // "Chiêu" "tải" trang web "bất đồng bộ" (tái sử dụng từ ví dụ trước)
      static async Task<string> TaiTrangWebAsync(HttpClient client, string url)
      {
          Console.WriteLine($"Bắt đầu tải trang web: {url}"); // Thông báo "bắt đầu"
          HttpResponseMessage response = await client.GetAsync(url);
          response.EnsureSuccessStatusCode();
          string htmlContent = await response.Content.ReadAsStringAsync();
          Console.WriteLine($"Tải trang web thành công: {url}"); // Thông báo "thành công"
          return htmlContent;
      }
  }
  ```

- **"Giải mã" code `Task.WhenAll` và `Task.WhenAny`:**

    - `List<Task<string>> downloadTasks = new List<Task<string>>();`: "Tạo" một "danh sách" để "chứa" các
      `Task<string>` - mỗi `Task` sẽ "tải" một trang web.
    - `foreach (string url in urls) { downloadTasks.Add(TaiTrangWebAsync(client, url)); }`: "Lặp" qua "danh sách"
      `urls`, và cho mỗi `url`, "thêm" một `Task<string>` "tải" trang web tương ứng vào `downloadTasks`. **Lúc này, các
      Task "tải" trang web đã được "khởi động" và đang "chạy song song"**.
    - `string[] htmlContents = await Task.WhenAll(downloadTasks);`: "Chờ đợi" **"tất cả"** các `Task` trong
      `downloadTasks` "hoàn thành" (dùng `Task.WhenAll`). Khi **tất cả** các `Task` "xong việc", `await` sẽ "trả về" một
      **"mảng"** các `string[]` chứa "nội dung" HTML của từng trang web.
    - `Task<string> firstCompletedTask = await Task.WhenAny(downloadTasks);`: "Chờ đợi" **"bất kỳ"** `Task` nào trong
      `downloadTasks` "hoàn thành" **"đầu tiên"** (dùng `Task.WhenAny`). Khi **"một"** `Task` "xong việc", `await` sẽ "
      trả về" chính **"món đồ"** `Task<string>` "xong việc" "nhanh nhất" đó.

**7.3. Dòng dữ liệu bất đồng bộ (`IAsyncEnumerable`) - "Xử Lý" Dữ Liệu "Khổng Lồ" Một Cách "Mượt Mà"**

- **"Bài toán": "Xử lý" dữ liệu "khổng lồ" một cách "bất đồng bộ" và "tiết kiệm bộ nhớ":**

    - Trong một số ứng dụng, bạn có thể phải "xử lý" một "lượng dữ liệu" **"siêu lớn"** (ví dụ: "đọc" file "khổng lồ", "
      truy vấn" database trả về "hàng triệu" bản ghi, "nhận" dữ liệu "liên tục" từ stream).
    - Nếu bạn "tải" **"toàn bộ"** dữ liệu vào "bộ nhớ" để "xử lý" **"đồng bộ"**, ứng dụng có thể bị **"ngốn" quá nhiều
      bộ nhớ**, **"chậm chạp"**, hoặc thậm chí **"treo máy"**.

- **`IAsyncEnumerable<T>` - "Dòng chảy" dữ liệu "bất đồng bộ" - "Xử Lý Dữ Liệu 'Từng Chút Một' ":**

    - `IAsyncEnumerable<T>` là một "giao diện" (interface) mới trong C# 8.0, "đại diện" cho một **"dòng chảy" dữ liệu "
      bất đồng bộ"**. Nó cho phép bạn "xử lý" dữ liệu **"từng chút một"** (streaming) một cách **"bất đồng bộ"**, **"
      không cần" "tải" "toàn bộ" dữ liệu vào "bộ nhớ" cùng một lúc**.
    - `IAsyncEnumerable<T>` "tương tự" như `IEnumerable<T>` (cho dữ liệu "đồng bộ"), nhưng nó "dành riêng" cho dữ liệu "
      bất đồng bộ".

- **"Chiêu" `await foreach` - "Dạo Bước" Trên "Dòng Chảy" Dữ Liệu Bất Đồng Bộ:**

    - C# 8.0 cũng giới thiệu "chiêu" **`await foreach`** để bạn có thể "duyệt" qua các "phần tử" trong
      `IAsyncEnumerable<T>` một cách **"bất đồng bộ"**. Nó "tương tự" như `foreach` (cho `IEnumerable<T>`), nhưng "dành
      riêng" cho `IAsyncEnumerable<T>`.

- **Ví dụ: "Đọc" file "văn bản" "khổng lồ" "từng dòng" một cách "bất đồng bộ" bằng `IAsyncEnumerable<string>`
  và `await foreach`:**

  ```csharp
  using System;
  using System.IO;
  using System.Collections.Generic; // "Nhập" không gian tên cho IAsyncEnumerable
  using System.Threading.Tasks;

  public class AsyncEnumerableExample
  {
      static async Task Main(string[] args)
      {
          string filePath = "large_data.txt"; // "Đường đi" đến file "dữ liệu lớn"

          // "Giả vờ" tạo file "large_data.txt" "khổng lồ" (nếu chưa có) - file này có thể rất lớn, không nên "tải" hết vào bộ nhớ
          if (!File.Exists(filePath))
          {
              using (StreamWriter writer = new StreamWriter(filePath))
              {
                  for (int i = 0; i < 100000; i++) // "Giả vờ" ghi 100,000 dòng vào file
                  {
                      await writer.WriteLineAsync($"Dòng dữ liệu số {i + 1}"); // Ghi "bất đồng bộ" từng dòng
                  }
              }
          }

          Console.WriteLine($"Bắt đầu đọc file 'khổng lồ' bất đồng bộ: {filePath}"); // Thông báo "bắt đầu"

          int lineCount = 0; // "Đếm" số dòng đã đọc

          // "Duyệt" qua file "từng dòng" một cách "bất đồng bộ" (IAsyncEnumerable<string> và await foreach)
          await foreach (string line in ReadLinesAsync(filePath)) // 'await foreach' để "dạo bước" trên "dòng chảy" dữ liệu bất đồng bộ
          {
              if (lineCount < 10) // Chỉ "in ra" 10 dòng đầu tiên để "minh họa"
              {
                  Console.WriteLine($"Dòng {lineCount + 1}: {line.Substring(0, 100)}..."); // In ra "một phần" của dòng
              }
              lineCount++; // "Tăng" "đếm" số dòng
              // ... (code "xử lý" từng dòng dữ liệu ở đây - "xử lý" "từng chút một" mà không cần "tải" hết file vào bộ nhớ) ...
          }

          Console.WriteLine($"\nĐọc file 'khổng lồ' bất đồng bộ thành công từ: {filePath}"); // Thông báo "đọc thành công"
          Console.WriteLine($"Tổng số dòng đã đọc: {lineCount:#,##0}"); // In ra "tổng số dòng" đã đọc

          Console.ReadKey();
      }

      // "Chiêu" "đọc" file "văn bản" "từng dòng" một cách "bất đồng bộ" và "trả về" IAsyncEnumerable<string>
      static async IAsyncEnumerable<string> ReadLinesAsync(string filePath) // "Trả về" IAsyncEnumerable<string> - "dòng chảy" dữ liệu bất đồng bộ
      {
          using (var reader = new StreamReader(filePath)) // "Mở" StreamReader để "đọc" file
          {
              string line;
              while ((line = await reader.ReadLineAsync()) != null) // "Đọc" từng dòng "bất đồng bộ" (await reader.ReadLineAsync)
              {
                  yield return line; // "Trả về" từng dòng (yield return) - tạo ra "dòng chảy" dữ liệu
              }
          }
      }
  }
  ```

- **"Giải mã" code `IAsyncEnumerable` và `await foreach`:**

    - `static async IAsyncEnumerable<string> ReadLinesAsync(string filePath)`: "Phương thức" `ReadLinesAsync` "trả về"
      `IAsyncEnumerable<string>`, "báo hiệu" rằng nó sẽ "trả về" một **"dòng chảy"** các chuỗi (từng dòng file) một cách
      **"bất đồng bộ"**.
    - `yield return line;`: "Chiêu" `yield return` trong C# giúp "tạo ra" một "dòng chảy" dữ liệu. Mỗi lần
      `yield return line;` được gọi, nó sẽ "trả về" giá trị `line` cho "người dùng" "dòng chảy", và "tạm dừng" "thực
      thi" phương thức `ReadLinesAsync` tại đó. Khi "người dùng" "yêu cầu" "dòng dữ liệu" tiếp theo, phương thức
      `ReadLinesAsync` sẽ "tiếp tục" "chạy" từ "điểm dừng" trước đó.
    - `await foreach (string line in ReadLinesAsync(filePath))`: "Vòng lặp" `await foreach` giúp bạn "duyệt" qua các "
      dòng dữ liệu" trong "dòng chảy" `IAsyncEnumerable<string>` một cách **"bất đồng bộ"**. Mỗi lần lặp,
      `await foreach` sẽ "chờ đợi" (không "đứng hình") cho đến khi `ReadLinesAsync` "trả về" "dòng dữ liệu" tiếp theo.

**Tổng Kết Chương 7:**

- Bạn đã "khám phá" các "khái niệm" và "chiêu thức" bất đồng bộ "nâng cao":
    - `ConfigureAwait(false)` và "bí ẩn" về "ngữ cảnh" (context) trong `async`/`await`.
        - Cách "chạy song song" các "công việc bất đồng bộ" bằng `Task.WhenAll` và `Task.WhenAny`.
        - "Sức mạnh" của "dòng dữ liệu bất đồng bộ" (`IAsyncEnumerable`) và cách "xử lý" dữ liệu "khổng lồ" một cách "
          mượt mà" với `await foreach`.

Chương 7 đã "mở rộng" "tầm nhìn" của bạn về lập trình bất đồng bộ, "trang bị" cho bạn những "công cụ" "cao cấp" để xây
dựng các ứng dụng .NET "nhanh nhẹn", "hiệu quả", và "mạnh mẽ" hơn nữa.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: Ứng Dụng Thực Tế Của Bất Đồng Bộ - "Bất Đồng Bộ Đi Muôn Nơi"**. Chúng ta sẽ "xem
xét" một vài ví dụ "ứng dụng" "thực tế" để "thấy" bất đồng bộ được "dùng" như thế nào trong các dự án phần mềm "đa
dạng".

Bạn có câu hỏi nào về các chủ đề bất đồng bộ "nâng cao" này không? Hãy cứ "hỏi thoải mái" nhé! Mình luôn sẵn sàng "chia
sẻ" và "cùng bạn" "lên trình" "cao thủ" bất đồng bộ. 