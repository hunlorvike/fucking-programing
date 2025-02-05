# Chương 3: `Task` - "Viên Gạch Nền Tảng" Của Bất Đồng Bộ - "Phiếu Giao Việc" Cho Công Việc "Ngầm"

Chào mừng bạn đến với **Chương 3: `Task` - "Viên Gạch Nền Tảng" Của Bất Đồng Bộ**! Trong chương này, chúng ta sẽ "khám
phá" **`Task`** và **`Task<T>`** - hai "nhân vật chính" đóng vai trò "cốt lõi" trong lập trình bất đồng bộ C#.

**3.1. `Task` và `Task<T>` là gì? - "Phiếu Giao Việc" Cho Công Việc "Ngầm"**

- **`Task` và `Task<T>` - "đại diện" cho "công việc bất đồng bộ":**

    - Trong lập trình bất đồng bộ, bạn thường muốn "giao" một "công việc" nào đó cho hệ thống "thực hiện" **"ngầm"** (
      background), **"song song"** với các "công việc" khác, hoặc **"trong khi chờ đợi"** một "thao tác" I/O "chậm
      chạp" (ví dụ: mạng, file).
    - **`Task` và `Task<T>`** chính là "công cụ" để bạn "đại diện" cho những "công việc bất đồng bộ" này. Hãy coi chúng
      như **"phiếu giao việc"** - bạn "ghi" "công việc" cần làm vào "phiếu", "giao" "phiếu" cho "hệ thống", và hệ thống
      sẽ "tự động" "thực hiện" "công việc" đó "ngầm" cho bạn.

- **`Task` - "Phiếu giao việc" không cần "trả kết quả":**

    - `Task` (không có chữ `<T>`) đại diện cho một "công việc bất đồng bộ" mà **"không cần" "trả về" kết quả** (hoặc kết
      quả là `void` - "không có gì"). Nó giống như bạn "giao" cho ai đó một "việc vặt" (ví dụ: "in báo cáo", "ghi log")
      mà không cần "mong đợi" "nhận lại" "hàng hóa" cụ thể.

- **`Task<T>` - "Phiếu giao việc" có "hẹn trả kết quả":**

    - `Task<T>` (có chữ `<T>`) đại diện cho một "công việc bất đồng bộ" mà **"hứa hẹn"** sẽ "trả về" một **"kết quả"**
      có kiểu `T` sau khi "hoàn thành". Nó giống như bạn "đặt hàng" ai đó "làm" một "món đồ" (ví dụ: "tải dữ liệu", "
      tính toán giá trị") và "mong đợi" "nhận lại" "món đồ" đó (kết quả) sau khi "xong việc".

**3.2. "Tạo" và "khởi động" `Task` - "Giao Việc" Cho Hệ Thống - "Viết Phiếu Giao Việc"**

- Có nhiều cách để "tạo" và "khởi động" một `Task`, dưới đây là một số cách phổ biến:

    - **`Task.Run()` - "Giao" "công việc" cho Thread Pool "thực hiện":**

        - `Task.Run(Action)`: Tạo và "khởi động" một `Task` để "thực thi" một "hành động" (delegate `Action` - không trả
          về giá trị).
        - `Task.Run(Func<TResult>)`: Tạo và "khởi động" một `Task<TResult>` để "thực thi" một "hàm" (delegate
          `Func<TResult>` - trả về giá trị kiểu `TResult`).

      ```csharp
      // Tạo và "khởi động" Task để "thực hiện" một "hành động" (không trả về gì)
      Task taskKhongKetQua = Task.Run(() => {
          Console.WriteLine("Task không trả kết quả: Bắt đầu công việc...");
          Thread.Sleep(2000); // "Giả vờ" "làm việc" mất 2 giây
          Console.WriteLine("Task không trả kết quả: Hoàn thành công việc.");
      });

      // Tạo và "khởi động" Task<string> để "thực hiện" một "hàm" và "trả về" string
      Task<string> taskCoKetQua = Task.Run(() => {
          Console.WriteLine("Task có trả kết quả: Bắt đầu tính toán...");
          Thread.Sleep(3000); // "Giả vờ" "tính toán" mất 3 giây
          Console.WriteLine("Task có trả kết quả: Tính toán xong.");
          return "Kết quả tính toán"; // "Trả về" kết quả kiểu string
      });
      ```

    - **`Task.Factory.StartNew()` - Tương tự `Task.Run()`, nhưng có thêm "tùy chọn" cấu hình:**

        - `Task.Factory.StartNew(Action)`
        - `Task.Factory.StartNew(Func<TResult>)`
        - ... và nhiều "tùy chọn" khác để "cấu hình" `Task` (ví dụ: `TaskCreationOptions`, `TaskScheduler`).

      ```csharp
      // Tạo và "khởi động" Task bằng Task.Factory.StartNew (tương tự Task.Run)
      Task taskFactory = Task.Factory.StartNew(() => {
          Console.WriteLine("Task Factory: Bắt đầu công việc...");
          Thread.Sleep(1500); // "Giả vờ" "làm việc" mất 1.5 giây
          Console.WriteLine("Task Factory: Hoàn thành công việc.");
      });
      ```

    - **`new Task()` và `.Start()` - "Tự tay" "điều khiển" "vòng đời" `Task`:**

        - `Task task = new Task(Action)`: Tạo một `Task` **"chưa khởi động"**.
        - `task.Start()`: **"Khởi động"** `Task` (bắt đầu "thực thi" "công việc").

      ```csharp
      // Tạo Task "chưa khởi động"
      Task taskManualStart = new Task(() => {
          Console.WriteLine("Task Manual Start: Bắt đầu công việc...");
          Thread.Sleep(2500); // "Giả vờ" "làm việc" mất 2.5 giây
          Console.WriteLine("Task Manual Start: Hoàn thành công việc.");
      });

      // "Khởi động" Task "bằng tay"
      taskManualStart.Start(); // "Lệnh" Task "bắt đầu" "thực thi"
      ```

- **"Lựa chọn" cách "tạo" và "khởi động" `Task`:**

    - **`Task.Run()`:**  Cách "dễ dàng" và "phổ biến" nhất để "tạo" và "khởi động" `Task`. Thường "đủ dùng" cho hầu hết
      các trường hợp.
    - **`Task.Factory.StartNew()`:**  "Linh hoạt" hơn `Task.Run()`, cho phép bạn "tùy chỉnh" thêm các "thiết lập" cho
      `Task` (nếu cần).
    - **`new Task()` và `.Start()`:**  Cho phép bạn "kiểm soát" "toàn diện" "vòng đời" `Task`, nhưng thường "rườm rà"
      hơn và ít khi cần dùng trực tiếp (trừ khi có yêu cầu "đặc biệt").

**3.3. "Lấy" kết quả từ "công việc bất đồng bộ" (`Task<T>`) - "Thu Thập" "Chiến Lợi Phẩm"**

- Khi bạn "giao việc" bằng `Task<T>`, bạn "mong đợi" "nhận lại" một "kết quả" sau khi "công việc" "hoàn tất". Để "lấy" "
  kết quả" này, bạn có thể dùng property **`.Result`** của `Task<T>`.

- **"Cách dùng" `.Result`:**

    - Gọi `.Result` trên một `Task<T>` **sau khi** `Task` đã **"hoàn thành"**.
    - `.Result` sẽ **"trả về"** "kết quả" (kiểu `T`) mà `Task<T>` "hứa hẹn".
    - Nếu `Task` **chưa "hoàn thành"** khi bạn gọi `.Result`, luồng (thread) hiện tại sẽ bị **"chặn lại"** (blocking) và
      **"chờ đợi"** cho đến khi `Task` "xong việc" và có kết quả.

- **Ví dụ:** "Lấy" kết quả từ `Task<string>` đã "tạo" ở ví dụ trước:

  ```csharp
  async Task Main(string[] args)
  {
      // Tạo và "khởi động" Task<string> (như ví dụ trước)
      Task<string> taskCoKetQua = Task.Run(() => {
          Console.WriteLine("Task có trả kết quả: Bắt đầu tính toán...");
          Thread.Sleep(3000);
          Console.WriteLine("Task có trả kết quả: Tính toán xong.");
          return "Kết quả tính toán";
      });

      Console.WriteLine("Chờ Task hoàn thành và lấy kết quả...");

      string ketQua = taskCoKetQua.Result; // "Lấy" kết quả từ Task<string> bằng .Result - luồng "chặn lại" ở đây cho đến khi Task "xong việc"

      Console.WriteLine($"Kết quả Task: {ketQua}"); // In ra "kết quả" "thu được"
      Console.WriteLine("Chương trình tiếp tục chạy sau khi lấy kết quả Task.");

      Console.ReadKey();
  }
  ```

- **"Lưu ý quan trọng" về `.Result`:**

    - `.Result` là "chiêu" **"đồng bộ"** để "lấy" kết quả từ `Task<T>`. Nó sẽ **"chặn"** luồng hiện tại và "chờ đợi"
      `Task` "xong việc".
    - **"Tránh" dùng `.Result` trong code "bất đồng bộ"** (ví dụ: trong phương thức `async`). Vì nó sẽ "phá hỏng" tính "
      bất đồng bộ" và có thể gây ra "đứng hình" ứng dụng.
    - Trong code "bất đồng bộ", hãy "ưu tiên" dùng **`await`** để "chờ đợi" `Task` và "lấy" kết quả (như chúng ta sẽ
      thấy ở phần sau).

**3.4. "Chờ" `Task` hoàn thành (`await` và `.Wait()`) - "Kiên Nhẫn Chờ Đợi" "Phiếu Giao Việc"**

- Đôi khi, bạn cần **"đảm bảo"** rằng một `Task` (hoặc nhiều `Task`) đã **"hoàn thành"** trước khi "tiếp tục" "làm việc
  khác". Có hai cách chính để "chờ đợi" `Task` "xong việc":

    - **`await` (trong code "bất đồng bộ" - "Chờ Đợi Thông Minh"):**

        - Như đã thấy ở Chương 2, `await` là "chiêu" **"bất đồng bộ"** để "chờ đợi" `Task`. Nó không làm "đứng hình"
          luồng hiện tại, mà chỉ làm cho phương thức `async` hiện tại "tạm dừng" cho đến khi `Task` "xong việc".

      ```csharp
      async Task Main(string[] args)
      {
          Task taskChoHoanThanh = Task.Run(() => { // Tạo Task "chạy" một "công việc" "giả lập"
              Console.WriteLine("Task chờ hoàn thành: Bắt đầu công việc...");
              Thread.Sleep(4000); // "Giả vờ" "làm việc" mất 4 giây
              Console.WriteLine("Task chờ hoàn thành: Hoàn thành công việc.");
          });

          Console.WriteLine("Chờ Task hoàn thành (dùng 'await')...");

          await taskChoHoanThanh; // "Chờ" Task "hoàn thành" (không "đứng hình" luồng) - dùng 'await'

          Console.WriteLine("Task đã hoàn thành. Chương trình tiếp tục.");

          Console.ReadKey();
      }
      ```

    - **`.Wait()` (trong code "đồng bộ" - "Chờ Đợi 'Cứng Nhắc' "):**

        - `.Wait()` là "chiêu" **"đồng bộ"** để "chờ đợi" `Task`. Nó sẽ **"chặn"** luồng hiện tại và **"ép"** luồng
          phải "đứng im" "chờ" cho đến khi `Task` "hoàn thành".

      ```csharp
      void Main_DongBo(string[] args) // Main method "đồng bộ" (không async)
      {
          Task taskChoHoanThanh = Task.Run(() => { // Tạo Task (tương tự như trên)
              Console.WriteLine("Task chờ hoàn thành: Bắt đầu công việc...");
              Thread.Sleep(4000);
              Console.WriteLine("Task chờ hoàn thành: Hoàn thành công việc.");
          });

          Console.WriteLine("Chờ Task hoàn thành (dùng '.Wait()')...");

          taskChoHoanThanh.Wait(); // "Chờ" Task "hoàn thành" (luồng "đứng hình" hoàn toàn) - dùng '.Wait()'

          Console.WriteLine("Task đã hoàn thành. Chương trình tiếp tục.");

          Console.ReadKey();
      }
      ```

- **"So sánh" `await` và `.Wait()`:**

    - **`await` (bất đồng bộ):** "Chờ đợi thông minh", không làm "đứng hình" luồng, "giữ" ứng dụng "nhanh nhẹn". **"Ưu
      tiên" dùng `await` trong code "bất đồng bộ"**.
    - **`.Wait()` (đồng bộ):** "Chờ đợi cứng nhắc", làm "đứng hình" luồng, "làm chậm" ứng dụng. **"Hạn chế"
      dùng `.Wait()`**, chỉ dùng khi **"bắt buộc"** phải "chờ đợi" trong code "đồng bộ" (ví dụ: trong `Main` method "
      đồng bộ" - như ví dụ trên, hoặc trong các tình huống "hiếm gặp" khác).

**Tổng Kết Chương 3:**

- Bạn đã "hiểu rõ" về **`Task`** và **`Task<T>`** - "viên gạch" cơ bản của lập trình bất đồng bộ C#.
    - Biết cách "tạo" và "khởi động" `Task` bằng `Task.Run()`, `Task.Factory.StartNew()`, `new Task()` và `.Start()`.
    - Học cách "lấy" kết quả từ `Task<T>` bằng property `.Result` (nhưng cần "cẩn thận" khi dùng).
    - Nắm vững cách "chờ đợi" `Task` "hoàn thành" bằng `await` ("thông minh") và `.Wait()` ("cứng nhắc"), và "thời
      điểm" "phù hợp" để dùng từng "chiêu".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: `async void` vs `async Task`/`async Task<T>` - "Chọn Mặt Gửi Vàng" Kiểu Trả Về**.
Chúng ta sẽ "phân tích" các kiểu trả về khác nhau của "phương thức bất đồng bộ" và "biết" khi nào nên "chọn" kiểu trả về
nào để code "chuẩn chỉnh" và "hiệu quả".

Nếu bạn có bất kỳ câu hỏi nào về `Task` và `Task<T>`