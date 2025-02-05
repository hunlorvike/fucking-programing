# Chương 2: `async` và `await` - "Cặp Đôi Hoàn Hảo" Của Bất Đồng Bộ - "Từ Khóa Ma Thuật" Của C#

Chào mừng bạn trở lại với hành trình bất đồng bộ! Hôm nay, chúng ta sẽ "làm quen" với **`async`** và **`await`** - "cặp
đôi quyền lực" giúp bạn "viết" code bất đồng bộ trong C# một cách "dễ dàng" và "thanh lịch".

**2.1. Giới thiệu về `async` và `await` - "Từ Khóa Ma Thuật" Của C# - "Vũ Khí Bí Mật"**

- **`async` và `await` - "bộ đôi" "tuyệt vời"** được giới thiệu vào C# để "đơn giản hóa" việc lập trình bất đồng bộ.
  Trước khi có chúng, việc viết code bất đồng bộ có thể khá "phức tạp" và "khó đọc". Nhưng với `async` và `await`, mọi
  thứ trở nên "dễ thở" hơn rất nhiều.

- Hãy coi `async` và `await` như **"từ khóa ma thuật"** giúp bạn "biến" code "đồng bộ" (chạy tuần tự) thành code **"bất
  đồng bộ"** (chạy "vừa chờ vừa làm việc khác") một cách "nhanh chóng" và "ít công sức".

- **`async` - "Phù phép" phương thức thành "phương thức bất đồng bộ":**

    - Khi bạn "thêm" từ khóa `async` vào "đầu" một phương thức (ví dụ: `public async Task<string> DoSomethingAsync()`),
      bạn đang "phù phép" phương thức đó thành một **"phương thức bất đồng bộ"**.
    - "Phương thức bất đồng bộ" có "khả năng đặc biệt" là có thể sử dụng từ khóa `await` bên trong nó.
    - "Tên" phương thức bất đồng bộ thường được đặt **kết thúc bằng `Async`** (ví dụ: `DoSomethingAsync`,
      `DownloadDataAsync`) - đây là "thói quen" tốt để "nhận diện" chúng.

- **`await` - "Dừng lại thông minh" - "Chờ Đợi" mà không "Đứng Hình":**

    - Từ khóa `await` chỉ có thể được "dùng" **bên trong** các "phương thức bất đồng bộ" (những phương thức đã được "phù
      phép" bằng `async`).
    - Khi bạn "gặp" từ khóa `await` trước một "công việc bất đồng bộ" (thường là một `Task` hoặc `Task<T>`), nó sẽ làm
      cho phương thức hiện tại **"tạm dừng"** (suspension) việc thực thi tại điểm đó.
    - **"Điều kỳ diệu" là:** Phương thức "tạm dừng" nhưng **"không làm 'đứng hình' luồng hiện tại"**. Luồng (thread)
      hiện tại có thể "rảnh tay" để "làm việc khác" (ví dụ: xử lý giao diện người dùng, thực hiện các "công việc" khác).
    - Khi "công việc bất đồng bộ" mà `await` đang "chờ đợi" **"hoàn thành"**, phương thức "tạm dừng" sẽ **"tự động 'thức
      giấc' "** và **"tiếp tục"** thực thi từ "điểm dừng" đó trở đi, "như chưa hề có cuộc chia ly".

**2.2. `async` - "Biến" phương thức thường thành "phương thức bất đồng bộ" - "Phép Thuật" Biến Hình**

- Để "biến" một phương thức thường thành "phương thức bất đồng bộ", bạn chỉ cần "thêm" từ khóa `async` vào "đầu" "khai
  báo" phương thức.

- **Ví dụ:**

  ```csharp
  // Phương thức "thường" (đồng bộ) - "Chạy" tuần tự, "chờ đợi" "đứng hình"
  string LayDuLieuTuTrangWeb_DongBo(string url)
  {
      Console.WriteLine($"Bắt đầu tải dữ liệu đồng bộ từ: {url}"); // Thông báo "bắt đầu"
      // ... (code "tải" dữ liệu từ trang web một cách "đồng bộ" - "chờ đợi" "đứng hình") ...
      Thread.Sleep(3000); // "Giả vờ" "chờ đợi" 3 giây (mô phỏng "chờ đợi" mạng)
      Console.WriteLine($"Tải dữ liệu đồng bộ xong từ: {url}"); // Thông báo "xong"
      return "Dữ liệu đồng bộ"; // "Trả về" dữ liệu (giả lập)
  }

  // Phương thức "bất đồng bộ" - "Chạy" "vừa chờ vừa làm việc khác", không "đứng hình"
  async Task<string> LayDuLieuTuTrangWeb_BatDongBoAsync(string url) // Thêm 'async' và 'Task<string>'
  {
      Console.WriteLine($"Bắt đầu tải dữ liệu bất đồng bộ từ: {url}"); // Thông báo "bắt đầu"
      // ... (code "tải" dữ liệu từ trang web một cách "bất đồng bộ" - "không 'đứng hình' chờ đợi") ...
      await Task.Delay(3000); // "Tạm dừng" bất đồng bộ 3 giây (mô phỏng "chờ đợi" mạng - "không 'đứng hình' luồng") - dùng 'await' và Task.Delay
      Console.WriteLine($"Tải dữ liệu bất đồng bộ xong từ: {url}"); // Thông báo "xong"
      return "Dữ liệu bất đồng bộ"; // "Trả về" dữ liệu (giả lập)
  }
  ```

- **"Điểm khác biệt" quan trọng:**

    - **`async Task<string>`:** Phương thức `LayDuLieuTuTrangWeb_BatDongBoAsync` có thêm từ khóa `async` và kiểu trả về
      là `Task<string>`. `Task<string>` "báo hiệu" rằng phương thức này là **"bất đồng bộ"** và sẽ "trả về" một `string`
      **"trong tương lai"** (sau khi "công việc" bất đồng bộ "hoàn thành").
    - **`Thread.Sleep(3000)` vs `await Task.Delay(3000)`:**
        - `Thread.Sleep(3000)` trong phương thức **"đồng bộ"** làm cho **toàn bộ luồng (thread) bị "đứng hình"** trong 3
          giây - ứng dụng "đơ".
        - `await Task.Delay(3000)` trong phương thức **"bất đồng bộ"** chỉ làm cho **phương thức hiện tại "tạm dừng"**
          trong 3 giây, **luồng (thread) vẫn "rảnh tay"** để "làm việc khác" - ứng dụng "mượt mà".

**2.3. `await` - "Tạm dừng" mà không "đứng hình" - "Chiêu" "Chờ Đợi Thông Minh"**

- Từ khóa `await` là "linh hồn" của lập trình bất đồng bộ với `async`/`await`. Nó cho phép bạn "tạm dừng" việc thực thi
  của "phương thức bất đồng bộ" một cách "thông minh", mà không làm "đóng băng" toàn bộ ứng dụng.

- **"Cách dùng" `await`:**

    - Đặt `await` **trước** một "công việc bất đồng bộ" (thường là một `Task` hoặc `Task<T>`).
    - "Công việc bất đồng bộ" này thường là một phương thức khác **cũng là "bất đồng bộ"** và "trả về" `Task` hoặc
      `Task<T>`.

- **Ví dụ:** "Gọi" phương thức bất đồng bộ `LayDuLieuTuTrangWeb_BatDongBoAsync` và `await` kết quả:

  ```csharp
  async Task Main(string[] args) // Main method giờ cũng có thể là async!
  {
      Console.WriteLine("Bắt đầu chương trình.");

      // "Gọi" phương thức bất đồng bộ và "chờ đợi" kết quả (không "đứng hình")
      string duLieuWeb = await LayDuLieuTuTrangWeb_BatDongBoAsync("https://www.example.com"); // 'await' "tạm dừng" ở đây cho đến khi 'LayDuLieuTuTrangWeb_BatDongBoAsync' "xong việc"

      Console.WriteLine($"Dữ liệu tải về: {duLieuWeb}"); // "In ra" dữ liệu sau khi đã "tải" xong
      Console.WriteLine("Chương trình tiếp tục chạy sau khi tải dữ liệu.");

      Console.WriteLine("Kết thúc chương trình.");
      Console.ReadKey(); // "Đợi" người dùng "bấm phím" để chương trình "kết thúc"
  }
  ```

- **"Giải mã" `await`:**

    - `string duLieuWeb = await LayDuLieuTuTrangWeb_BatDongBoAsync("https://www.example.com");`
        - `await LayDuLieuTuTrangWeb_BatDongBoAsync(...)`: "Ra lệnh" là "hãy 'chạy' 'công việc bất đồng bộ'
          `LayDuLieuTuTrangWeb_BatDongBoAsync(...)` và **'chờ đợi' cho đến khi nó 'hoàn thành' **".
        - **"Trong thời gian 'chờ đợi' "**, phương thức `Main` **"tạm dừng"** tại dòng code này, nhưng **luồng (
          thread) "không bị 'đứng hình' "**, nó có thể "rảnh tay" để "làm việc khác".
        - Khi `LayDuLieuTuTrangWeb_BatDongBoAsync(...)` **"hoàn thành"** và "trả về" kết quả (kiểu `string`), `await` sẽ
          **"lấy"** kết quả đó và **"gán"** vào biến `duLieuWeb`, sau đó phương thức `Main` **"tự động 'thức giấc' "**
          và **"tiếp tục"** "chạy" các dòng code phía sau `await`.

**2.4. Ví dụ code đơn giản với `async` và `await` - "Thấy Tận Mắt" Bất Đồng Bộ "Hoạt Động"**

Hãy cùng xem một ví dụ "chạy" để "thấy tận mắt" sự khác biệt giữa "đồng bộ" và "bất đồng bộ":

```csharp
using System;
using System.Diagnostics;
using System.Threading;
using System.Threading.Tasks;

public class AsyncAwaitExample
{
    // Phương thức "đồng bộ" - "chờ đợi" "đứng hình"
    static void CongViecDongBo(string tenCongViec)
    {
        Console.WriteLine($"{tenCongViec} (Đồng bộ): Bắt đầu"); // Thông báo "bắt đầu"
        Thread.Sleep(2000); // "Giả vờ" "làm việc" mất 2 giây (luồng "đứng hình" hoàn toàn)
        Console.WriteLine($"{tenCongViec} (Đồng bộ): Hoàn thành"); // Thông báo "hoàn thành"
    }

    // Phương thức "bất đồng bộ" - "vừa chờ vừa làm việc khác", không "đứng hình"
    static async Task CongViecBatDongBoAsync(string tenCongViec) // Thêm 'async' và 'Task'
    {
        Console.WriteLine($"{tenCongViec} (Bất đồng bộ): Bắt đầu"); // Thông báo "bắt đầu"
        await Task.Delay(2000); // "Tạm dừng" bất đồng bộ 2 giây (luồng "không 'đứng hình'") - dùng 'await' và Task.Delay
        Console.WriteLine($"{tenCongViec} (Bất đồng bộ): Hoàn thành"); // Thông báo "hoàn thành"
    }

    static async Task Main(string[] args)
    {
        Console.WriteLine("Chương trình bắt đầu.");

        Stopwatch sw = Stopwatch.StartNew(); // Bấm giờ

        CongViecDongBo("Công việc 1"); // "Chạy" "công việc đồng bộ" 1
        CongViecDongBo("Công việc 2"); // "Chạy" "công việc đồng bộ" 2

        Console.WriteLine("\n--- Chạy song song (bất đồng bộ) ---");

        Task task1 = CongViecBatDongBoAsync("Công việc 3"); // "Khởi động" "công việc bất đồng bộ" 3 (chưa "chờ")
        Task task2 = CongViecBatDongBoAsync("Công việc 4"); // "Khởi động" "công việc bất đồng bộ" 4 (chưa "chờ")

        await Task.WhenAll(task1, task2); // "Chờ" **cả hai** "công việc bất đồng bộ" 3 và 4 "hoàn thành" (không "đứng hình") - dùng Task.WhenAll để "chờ" nhiều Task cùng lúc

        sw.Stop(); // Dừng bấm giờ

        Console.WriteLine($"\nChương trình kết thúc sau: {sw.ElapsedMilliseconds}ms"); // In ra "thời gian chạy"

        Console.ReadKey(); // "Đợi" người dùng "bấm phím"
    }
}
```

**"Chạy" ví dụ và "quan sát" kết quả:**

- **"Công việc đồng bộ" ("Công việc 1" và "Công việc 2") "chạy" "lần lượt"**, tổng thời gian khoảng 4 giây (2 giây + 2
  giây).
- **"Công việc bất đồng bộ" ("Công việc 3" và "Công việc 4") "chạy" "song song"**, tổng thời gian chỉ khoảng 2 giây (
  thời gian của "công việc" "lâu nhất").

**"Giải thích" kết quả:**

- **Đồng bộ:** Các "công việc" "chạy" **"tuần tự"**, "công việc" này "xong" mới đến "công việc" khác, "tốn thời gian" "
  chờ đợi" "lần lượt".
- **Bất đồng bộ:** Các "công việc" "chạy" **"gần như đồng thời"**, "tận dụng" thời gian "chờ đợi" của "công việc" này
  để "làm" "công việc" khác, "tiết kiệm" thời gian "tổng cộng".

---

## Bước Tiếp Theo Trong Hành Trình Bất Đồng Bộ

Chúng ta sẽ chuyển sang **Chương 3: `Task` - "Viên Gạch Nền Tảng" Của Bất Đồng Bộ**. Ở chương này, chúng ta sẽ "mổ xẻ"
sâu hơn về `Task` và `Task<T>`, "hiểu rõ" vai trò "quan trọng" của chúng trong lập trình bất đồng bộ C#.

Nếu bạn có bất kỳ câu hỏi nào về `async` và `await`, đừng "ngại ngần" "hỏi" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng
bạn" "khám phá" thế giới bất đồng bộ.

Chúc bạn học tập thật vui và hiệu quả!

---

Let me know if you'd like me to continue with Chapter 3!