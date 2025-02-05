# Chương 6: Xử Lý Lỗi và Hủy Bỏ Trong Bất Đồng Bộ - "An Toàn Là Bạn, Tai Nạn Là Thù" - "Bảo Vệ" Ứng Dụng Bất Đồng Bộ Khỏi "Sóng Gió"

Chào mừng bạn đến với **Chương 6: Xử Lý Lỗi và Hủy Bỏ Trong Bất Đồng Bộ**! Trong chương này, chúng ta sẽ "trang bị" cho
code bất đồng bộ của bạn "áo giáp" và "phao cứu sinh" để "vượt qua" mọi "sóng gió" - lỗi và hủy bỏ - một cách "an toàn"
và "vững vàng".

**6.1. Xử lý lỗi trong code `async`/`await` (try-catch blocks) - "Đón Đầu" Và "Dập Tắt" "Ngọn Lửa" Lỗi**

- **Exception Handling (Xử Lý Lỗi) - "Không Thể Thiếu" Trong Lập Trình:**

    - Trong bất kỳ chương trình nào, lỗi (exceptions) là điều "không thể tránh khỏi". Đặc biệt trong lập trình bất đồng
      bộ, khi các "công việc" "chạy" "ngầm" và "song song", việc "xử lý lỗi" một cách "chu đáo" càng trở nên "quan
      trọng" hơn bao giờ hết.
    - Nếu không "đón đầu" và "xử lý" lỗi đúng cách, ứng dụng của bạn có thể bị **"treo"**, **"đóng băng"**, hoặc "gây
      ra" các "hậu quả" "khó lường".

- **`try-catch blocks` - "Vũ Khí" "Bắt Lỗi" "Truyền Thống" Vẫn "Hiệu Quả" Trong `async`/`await`:**

    - Tin vui là, cơ chế **`try-catch blocks`** "quen thuộc" trong C# vẫn hoạt động **"hoàn hảo"** trong code `async`/
      `await`. Bạn có thể dùng `try-catch blocks` để **"bắt"** và **"xử lý"** các exceptions "xảy ra" trong các "phương
      thức bất đồng bộ" một cách "tự nhiên" và "dễ hiểu".

- **"Cách dùng" `try-catch` trong `async`/`await`:**

    - "Đặt" code có thể "gây ra" exception (ví dụ: các "chiêu" `await` "gọi" các "công việc bất đồng bộ" khác) vào bên
      trong khối `try { ... }`.
    - "Đặt" code "xử lý lỗi" (ví dụ: "ghi log", "hiển thị thông báo lỗi", "thực hiện" các "hành động" "khắc phục" lỗi)
      vào bên trong khối `catch (Exception ex) { ... }`.

- **Ví dụ: Xử lý lỗi khi "tải" trang web "bất đồng bộ" bằng `try-catch`:**

  ```csharp
  using System;
  using System.Net.Http;
  using System.Threading.Tasks;

  public class AsyncExceptionHandlingExample
  {
      static async Task Main(string[] args)
      {
          string url = "https://www.example.com"; // "Địa chỉ" trang web (có thể "gây lỗi" nếu không tồn tại hoặc mạng "chập chờn")

          Console.WriteLine($"Bắt đầu tải trang web bất đồng bộ từ: {url}"); // Thông báo "bắt đầu"

          using (HttpClient client = new HttpClient()) // "Tạo" HttpClient
          {
              try // "Bắt đầu" "thử" "tải" trang web (có thể "xảy ra lỗi" mạng)
              {
                  HttpResponseMessage response = await client.GetAsync(url); // "Tải" trang web "bất đồng bộ" - có thể "ném ra" HttpRequestException
                  response.EnsureSuccessStatusCode(); // "Kiểm tra" "mã trạng thái" - có thể "ném ra" HttpRequestException

                  string htmlContent = await response.Content.ReadAsStringAsync(); // "Đọc" "nội dung" HTML - ít khả năng "ném ra" lỗi trong ví dụ này, nhưng vẫn nên "đề phòng"

                  Console.WriteLine($"\nNội dung trang web (rút gọn):\n{htmlContent.Substring(0, 500)}..."); // In ra "nội dung" (nếu "tải" thành công)
                  Console.WriteLine($"\nTải trang web bất đồng bộ thành công từ: {url}"); // Thông báo "thành công"
              }
              catch (HttpRequestException ex) // "Bắt" lỗi "yêu cầu" HTTP (HttpRequestException) - "xử lý" lỗi "tải" trang web
              {
                  Console.WriteLine($"\nLỗi tải trang web (HttpRequestException): {ex.Message}"); // Thông báo "lỗi" "chi tiết"
                  // ... (code "xử lý" lỗi "yêu cầu" web, ví dụ: "ghi log", "thông báo" cho người dùng, "thử lại" sau, v.v.) ...
              }
              catch (Exception ex) // "Bắt" tất cả các loại lỗi khác (Exception) - "xử lý" các lỗi "ngoài dự kiến"
              {
                  Console.WriteLine($"\nLỗi không xác định (Exception): {ex.Message}"); // Thông báo "lỗi" "chung chung"
                  // ... (code "xử lý" lỗi "chung", ví dụ: "ghi log" chi tiết hơn, "thông báo" lỗi "tổng quát" cho người dùng, v.v.) ...
              }
          }

          Console.WriteLine("\nChương trình tiếp tục chạy sau khi xử lý lỗi (hoặc thành công)."); // Thông báo chương trình "tiếp tục" "làm việc khác" dù "thành công" hay "lỗi"
          Console.ReadKey();
      }
  }
  ```

- **"Giải mã" code "xử lý lỗi" bất đồng bộ:**

    - Khối `try { ... }` "bao bọc" các "chiêu" `await` "gọi" `HttpClient.GetAsync()` và
      `response.Content.ReadAsStringAsync()`, vì các "chiêu" này có thể "ném ra" `HttpRequestException` nếu có "sự cố"
      mạng hoặc server.
    - Khối `catch (HttpRequestException ex) { ... }` "bắt" và "xử lý" các lỗi **"đặc biệt"** kiểu
      `HttpRequestException` (lỗi "liên quan" đến "yêu cầu" HTTP).
    - Khối `catch (Exception ex) { ... }` "bắt" và "xử lý" **tất cả các loại lỗi khác** (nếu có lỗi nào "ngoài dự
      kiến" "xảy ra").
    - Khối `finally { ... }` (không có trong ví dụ này, nhưng có thể dùng) sẽ chứa code được "thực thi" **"bất kể"** có
      lỗi hay không (ví dụ: "dọn dẹp tài nguyên", "ghi log" "kết thúc" "công việc").

**6.2. Hủy bỏ "công việc" bất đồng bộ bằng `CancellationToken` - "Dừng Lại" Khi "Không Cần Thiết" - "Nút Dừng Khẩn Cấp"
**

- **Cancellation (Hủy Bỏ) - "Cho Phép" "Dừng" "Công Việc" "Giữa Chừng":**

    - Trong nhiều trường hợp, bạn có thể muốn **"dừng lại"** một "công việc bất đồng bộ" đang "chạy" **"giữa chừng"** (
      ví dụ: người dùng "hủy" "tải file", "dừng" "tìm kiếm", "thoát" ứng dụng).
    - **Cancellation (hủy bỏ)** là cơ chế cho phép bạn "ra lệnh" **"dừng"** một "công việc" bất đồng bộ một cách "an
      toàn" và "có kiểm soát".

- **`CancellationToken` và `CancellationTokenSource` - "Bộ Đôi" "Điều Khiển Hủy Bỏ":**

    - **`CancellationTokenSource`:** "Trạm điều khiển" "hủy bỏ". Bạn tạo một `CancellationTokenSource` instance để "quản
      lý" việc "hủy bỏ".
    - **`CancellationToken`:** "Vé báo hiệu" "hủy bỏ". Bạn "lấy" `CancellationToken` từ `CancellationTokenSource` (
      `cancellationTokenSource.Token`) và "truyền" nó cho "công việc bất đồng bộ" mà bạn muốn có thể "hủy bỏ".
    - Khi bạn muốn "hủy bỏ" "công việc", bạn "gọi" phương thức `Cancel()` của `CancellationTokenSource` (
      `cancellationTokenSource.Cancel()`). "Lệnh hủy bỏ" sẽ được "báo hiệu" thông qua `CancellationToken`.
    - "Công việc bất đồng bộ" cần **"kiểm tra"** định kỳ `CancellationToken.IsCancellationRequested` để "biết" có "lệnh
      hủy bỏ" hay không. Nếu có, nó cần **"tự giác" "dừng lại"** và "ném ra" `OperationCanceledException` (hoặc "xử
      lý" "hủy bỏ" theo cách khác).

- **Ví dụ: "Tải" trang web "bất đồng bộ" có hỗ trợ "hủy bỏ" bằng `CancellationToken`:**

  ```csharp
  using System;
  using System.Net.Http;
  using System.Threading; // "Nhập" không gian tên cho CancellationToken
  using System.Threading.Tasks;

  public class AsyncCancellationExample
  {
      static async Task Main(string[] args)
      {
          string url = "https://www.example.com"; // "Địa chỉ" trang web
          CancellationTokenSource cts = new CancellationTokenSource(); // "Trạm điều khiển" hủy bỏ
          CancellationToken cancellationToken = cts.Token; // "Vé báo hiệu" hủy bỏ

          Console.WriteLine($"Bắt đầu tải trang web bất đồng bộ (có thể hủy bỏ) từ: {url}"); // Thông báo "bắt đầu"

          // "Chạy" "công việc" "tải" trang web trong một Task riêng để có thể "hủy bỏ" từ Task chính
          Task downloadTask = Task.Run(async () => { // Task.Run để "chạy" "công việc" "ngầm"
              using (HttpClient client = new HttpClient()) // "Tạo" HttpClient
              {
                  try // "Bắt đầu" "thử" "tải" trang web (có thể "bị hủy bỏ" hoặc "xảy ra lỗi" mạng)
                  {
                      // "Gửi" "yêu cầu GET" bất đồng bộ và "truyền" 'CancellationToken' vào
                      HttpResponseMessage response = await client.GetAsync(url, cancellationToken); // "Truyền" 'cancellationToken' cho GetAsync
                      response.EnsureSuccessStatusCode();
                      string htmlContent = await response.Content.ReadAsStringAsync();

                      Console.WriteLine($"\nNội dung trang web (rút gọn):\n{htmlContent.Substring(0, 500)}..."); // In ra "nội dung" (nếu "tải" thành công và không bị "hủy bỏ")
                      Console.WriteLine($"\nTải trang web bất đồng bộ thành công từ: {url}"); // Thông báo "tải thành công"
                  }
                  catch (OperationCanceledException) // "Bắt" lỗi OperationCanceledException - "báo hiệu" "công việc" bị "hủy bỏ"
                  {
                      Console.WriteLine("\nTask tải trang web đã bị hủy bỏ."); // Thông báo "bị hủy bỏ"
                  }
                  catch (HttpRequestException ex) // "Bắt" lỗi "yêu cầu" HTTP (HttpRequestException)
                  {
                      Console.WriteLine($"\nLỗi tải trang web (HttpRequestException): {ex.Message}"); // Thông báo "lỗi" "yêu cầu" web
                  }
              }
          }, cancellationToken); // "Truyền" 'cancellationToken' cho Task.Run

          Console.WriteLine("\nNhấn phím bất kỳ để hủy bỏ tải trang web (trong vòng 3 giây)..."); // Hướng dẫn người dùng "hủy bỏ"
          Console.ReadKey(true); // "Đợi" người dùng "bấm phím" (trong vòng 3 giây)

          if (!downloadTask.IsCompleted) // Nếu Task "tải" trang web "chưa xong" (vẫn đang "chạy")
          {
              cts.Cancel(); // "Ra lệnh" "hủy bỏ" Task "tải" trang web - "bấm nút dừng khẩn cấp"
              Console.WriteLine("Đã yêu cầu hủy bỏ Task tải trang web."); // Thông báo "đã yêu cầu hủy bỏ"
          }

          await downloadTask; // "Chờ" Task "tải" trang web "hoàn thành" (hoặc "bị hủy bỏ") - dùng 'await'

          Console.WriteLine("\nChương trình tiếp tục chạy sau khi Task tải trang web (hoặc bị hủy bỏ)."); // Thông báo chương trình "tiếp tục"
          Console.ReadKey();
      }
  }
  ```

- **"Giải mã" code "hủy bỏ" bất đồng bộ:**

    - `CancellationTokenSource cts = new CancellationTokenSource();`: "Tạo" "trạm điều khiển" hủy bỏ.
    - `CancellationToken cancellationToken = cts.Token;`: "Lấy" "vé báo hiệu" hủy bỏ.
    - `await client.GetAsync(url, cancellationToken);`: "Truyền" `cancellationToken` cho "chiêu" `GetAsync()`. Điều
      này "cho phép" `GetAsync()` "nhận biết" được "lệnh hủy bỏ" và "dừng lại" khi cần.
    - `Task.Run(async () => { ... }, cancellationToken);`: "Truyền" `cancellationToken` cho `Task.Run()`. Điều này "cho
      phép" **toàn bộ Task "con"** có thể bị "hủy bỏ" từ bên ngoài.
    - `if (!downloadTask.IsCompleted) { cts.Cancel(); }`: "Kiểm tra" xem Task "tải" trang web đã "xong việc" chưa. Nếu
      chưa, "ra lệnh" "hủy bỏ" bằng `cts.Cancel()`.
    - `catch (OperationCanceledException) { ... }`: "Bắt" lỗi `OperationCanceledException` trong Task "con". Đây là "dấu
      hiệu" cho thấy Task đã bị "hủy bỏ" "tự giác".

**6.4. "Nguyên tắc vàng" xử lý lỗi và hủy bỏ trong bất đồng bộ - Code "Vừa Mạnh Mẽ, Vừa An Toàn"**

- **"Nguyên tắc vàng" xử lý lỗi:**

    - **"Bọc" code `async`/`await` trong `try-catch blocks` để "đón đầu" và "xử lý" exceptions.**
    - "Bắt" các loại exception **"cụ thể"** (ví dụ: `HttpRequestException`, `IOException`) để "xử lý" "chi tiết" từng
      loại lỗi.
    - "Bắt" exception "chung" `Exception` ở "ngoài cùng" để "xử lý" các lỗi "ngoài dự kiến".
    - "Ghi log" lỗi (ví dụ: `Console.WriteLine(ex.ToString())`, "lưu" vào file log, dùng logging framework) để "theo
      dõi" và "debug" lỗi.
    - "Thông báo" lỗi cho người dùng một cách "thân thiện" (ví dụ:
      `MessageBox.Show("Đã xảy ra lỗi. Vui lòng thử lại sau.")`).
    - "Thực hiện" các "hành động" "khắc phục" lỗi (ví dụ: "thử lại" "yêu cầu" sau một khoảng thời gian, "chuyển hướng"
      sang "luồng xử lý" khác).
    - "Dùng" khối `finally` để "dọn dẹp" tài nguyên (ví dụ: "đóng" kết nối, "giải phóng" bộ nhớ) và "đảm bảo" code "luôn
      chạy" "dù có lỗi hay không".

- **"Nguyên tắc vàng" hủy bỏ:**

    - "Sử dụng" `CancellationToken` và `CancellationTokenSource` để "thêm" "khả năng hủy bỏ" cho các "công việc bất đồng
      bộ" "tốn thời gian".
    - "Truyền" `CancellationToken` cho các "chiêu" bất đồng bộ (ví dụ: `HttpClient.GetAsync(..., cancellationToken)`,
      `File.ReadAllTextAsync(..., cancellationToken)`).
    - Trong "công việc bất đồng bộ", "kiểm tra" định kỳ `cancellationToken.IsCancellationRequested`.
    - Nếu `cancellationToken.IsCancellationRequested` là `true`, "dừng lại" "công việc" một cách "tự giác" và "ném ra"
      `OperationCanceledException`.
    - "Bắt" `OperationCanceledException` ở code "gọi" để "xử lý" trường hợp "công việc" bị "hủy bỏ" (ví dụ: "thông báo"
      cho người dùng, "dọn dẹp" tài nguyên).

**Tổng Kết Chương 6:**

- Bạn đã "học" cách "xử lý lỗi" "chuẩn mực" trong code `async`/`await` bằng `try-catch blocks`.
    - "Nắm vững" cách "thêm" "khả năng hủy bỏ" cho "công việc bất đồng bộ" bằng `CancellationToken` và
      `CancellationTokenSource`.
    - "Thuộc lòng" các "nguyên tắc vàng" xử lý lỗi và hủy bỏ trong lập trình bất đồng bộ để code vừa "mạnh mẽ", vừa "an
      toàn".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: Bất Đồng Bộ Nâng Cao (Tùy Chọn) - "Lên Trình" Chuyên Gia Bất Đồng Bộ**. Chúng ta
sẽ "khám phá" các "chiêu" bất đồng bộ "cao cấp" hơn như `ConfigureAwait(false)`, "chạy song song" các `Task`, và "dòng
dữ liệu bất đồng bộ" (`IAsyncEnumerable`).

Bạn có câu hỏi nào về "xử lý lỗi" và "hủy bỏ" trong bất đồng bộ này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn
sàng "giải đáp" và "cùng bạn" "vượt qua" mọi "chướng ngại vật".
