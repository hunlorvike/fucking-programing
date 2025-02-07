# Chương 4: `async void` vs `async Task`/

`async Task<T>` - "Chọn Mặt Gửi Vàng" Kiểu Trả Về - "Quyết Định" Đúng Đắn Cho Phương Thức Bất Đồng Bộ

Chào mừng bạn trở lại với **Chương 4: `async void` vs `async Task`/`async Task<T>`**! Trong chương này, chúng ta sẽ "soi
kỹ" các kiểu trả về khác nhau của "phương thức bất đồng bộ" (`async` methods) và "học cách" "chọn mặt gửi vàng" - chọn
kiểu trả về nào cho "phương thức bất đồng bộ" của bạn để code vừa "chuẩn", vừa "ngon", vừa "ít lỗi".

**4.1. "Mổ Xẻ" `async void`, `async Task`, và `async Task<T>` - "Ba Chàng Lính Ngự Lâm" Kiểu Trả Về**

Khi bạn "phù phép" một phương thức thành "phương thức bất đồng bộ" bằng từ khóa `async`, bạn cần "chọn" một trong ba
kiểu trả về sau:

- **`async void` - "Kiểu trả về 'Vô Diện' " (ít dùng, cẩn thận):**

    - `async void` được dùng cho các "phương thức bất đồng bộ" mà **"không trả về giá trị"** và **"không thể 'await'
      được một cách trực tiếp' từ bên ngoài"**.
    - Nó thường được dùng **"duy nhất"** cho **event handlers** (các phương thức "xử lý sự kiện" - ví dụ: button click
      event trong giao diện người dùng).
    - **"Cực kỳ cẩn thận" khi dùng `async void` ở những nơi khác ngoài event handlers!** Vì nó có thể gây ra các vấn
      đề "khó lường" về xử lý lỗi và luồng.

- **`async Task` - "Kiểu trả về 'Nhiệm Vụ Hoàn Thành' " (phổ biến):**

    - `async Task` được dùng cho các "phương thức bất đồng bộ" mà **"không trả về giá trị cụ thể"** (tương tự như `void`
      trong phương thức "đồng bộ"), nhưng **"cho phép 'await' từ bên ngoài' "** và **"hỗ trợ xử lý lỗi chuẩn mực"**.
    - Đây là kiểu trả về **"phổ biến nhất"** cho các "phương thức bất đồng bộ" thực hiện các "công việc" mà bạn muốn "
      chờ đợi" chúng "hoàn thành", nhưng không quan tâm đến "kết quả" cụ thể (ví dụ: "tải file", "gửi email", "ghi
      log").

- **`async Task<T>` - "Kiểu trả về 'Nhiệm Vụ Có Kết Quả' " (phổ biến):**

    - `async Task<T>` được dùng cho các "phương thức bất đồng bộ" mà **"trả về" một "kết quả"** có kiểu `T` (ví dụ:
      `Task<string>`, `Task<int>`, `Task<MyObject>`), và **"cho phép 'await' từ bên ngoài' "** và **"hỗ trợ xử lý lỗi
      chuẩn mực"**.
    - Đây cũng là kiểu trả về **"rất phổ biến"** cho các "phương thức bất đồng bộ" thực hiện các "công việc" mà bạn cần
      **"lấy" "kết quả"** sau khi chúng "xong việc" (ví dụ: "tải dữ liệu từ web" - trả về `Task<string>`, "tính toán giá
      trị" - trả về `Task<int>`).

**4.2. Khi nào nên "dùng" `async void`? - Trường hợp "đặc biệt" (và cảnh báo) - "Dao Hai Lưỡi"**

- **`async void` - "Chỉ dành" cho event handlers:**

    - Như đã nói ở trên, `async void` **"chỉ nên"** được dùng cho **event handlers** trong các ứng dụng giao diện người
      dùng (ví dụ: WPF, WinForms, ASP.NET Web Forms).

    - **Ví dụ:** Button click event handler trong WinForms:

      ```csharp
      private async void btnDownload_Click(object sender, EventArgs e) // Event handler "bất đồng bộ" - dùng 'async void'
      {
          try
          {
              btnDownload.Enabled = false; // "Khóa" button để tránh click nhiều lần

              string duLieu = await TaiDuLieuTuWebAsync("https://www.example.com"); // "Gọi" phương thức "tải" dữ liệu "bất đồng bộ" và "chờ"
              txtDuLieu.Text = duLieu; // "Hiển thị" dữ liệu lên TextBox

              MessageBox.Show("Tải dữ liệu thành công!"); // Thông báo "thành công"
          }
          catch (Exception ex) // "Bắt" lỗi nếu có
          {
              MessageBox.Show($"Lỗi: {ex.Message}"); // Hiển thị thông báo lỗi
          }
          finally
          {
              btnDownload.Enabled = true; // "Mở khóa" button sau khi "xong việc" hoặc "lỗi"
          }
      }
      ```

- **"Cảnh báo" về `async void` - "Con Dao Hai Lưỡi":**

    - **Khó "bắt lỗi" từ bên ngoài:** Các phương thức `async void` **không thể "await" được trực tiếp** từ code gọi
      chúng. Điều này có nghĩa là bạn **khó "kiểm soát"** việc thực thi của chúng và **khó "bắt" "lỗi"** (exceptions) "
      xảy ra" bên trong chúng từ code gọi.

    - **Lỗi "không được báo cáo" có thể "làm ứng dụng 'im lặng' ":** Nếu một exception "xảy ra" trong phương thức
      `async void` mà **không được "bắt" bên trong**, nó có thể làm ứng dụng **"im lặng 'nuốt chửng' " lỗi** (unobserved
      exception), gây ra các vấn đề "khó debug" và "khó lường".

    - **Khó "kết hợp" với các "chiêu" bất đồng bộ khác:** `async void` "khó" "kết hợp" với các "chiêu" lập trình bất
      đồng bộ khác như `Task.WhenAll`, `Task.WhenAny`, `async streams`, v.v.

    - **"Lời khuyên":** **"Hạn chế tối đa"** việc sử dụng `async void` **ngoài event handlers**. Trong mọi trường hợp
      khác, hãy **"ưu tiên"** dùng `async Task` hoặc `async Task<T>`.

**4.3. Khi nào "ưu tiên" `async Task` và `async Task<T>`? - Trường hợp "phổ biến" và "an toàn" - "Lựa Chọn 'Vàng' "**

- **`async Task` và `async Task<T>` - "Lựa chọn 'vàng' " cho hầu hết các trường hợp:**

    - **"Linh hoạt" và "đa năng":** `async Task` và `async Task<T>` là các kiểu trả về **"linh hoạt"** và **"đa dụng"**
      nhất cho các "phương thức bất đồng bộ". Chúng "phù hợp" với hầu hết các tình huống lập trình bất đồng bộ, từ các "
      công việc" đơn giản đến các "luồng" xử lý "phức tạp".

    - **"Dễ dàng 'await' từ bên ngoài' ":** Các phương thức `async Task` và `async Task<T>` có thể được **"await" một
      cách trực tiếp"** từ code gọi chúng. Điều này giúp bạn **"kiểm soát"** "luồng" thực thi, **"chờ đợi"** "công
      việc" "hoàn thành", và **"lấy" "kết quả"** (nếu có) một cách "dễ dàng" và "tự nhiên".

    - **"Xử lý lỗi 'chuẩn mực' ":** Khi một exception "xảy ra" trong phương thức `async Task` hoặc `async Task<T>`,
      exception đó sẽ được "lan truyền" (propagate) đến code "await" phương thức đó, cho phép bạn **"bắt" và "xử lý" lỗi
      ** bằng `try-catch blocks` một cách "quen thuộc" và "hiệu quả".

    - **"Dễ dàng 'kết hợp' " với các "chiêu" bất đồng bộ khác:** `async Task` và `async Task<T>` "kết hợp" rất tốt với
      các "chiêu" lập trình bất đồng bộ khác như `Task.WhenAll`, `Task.WhenAny`, `async streams`, giúp bạn xây dựng
      các "ứng dụng" bất đồng bộ "mạnh mẽ" và "linh hoạt".

- **Khi nào "chọn" `async Task` vs `async Task<T>`?**

    - **`async Task`:** "Chọn" khi "phương thức bất đồng bộ" của bạn **"không cần 'trả về' giá trị cụ thể"**, mà chỉ
      cần "báo hiệu" "hoàn thành" (ví dụ: "tải xong file", "gửi xong email").

    - **`async Task<T>`:** "Chọn" khi "phương thức bất đồng bộ" của bạn **"cần 'trả về' một 'kết quả' "** có kiểu `T`
      sau khi "xong việc" (ví dụ: "tải dữ liệu từ web" - trả về `Task<string>`, "tính toán" và trả về `Task<int>`).

**4.4. "Nguyên tắc vàng" chọn kiểu trả về cho "phương thức bất đồng bộ" - "Chọn Đúng" Để Code "Chuẩn"**

- **"Nguyên tắc vàng":**

    - **"Luôn 'ưu tiên' `async Task` hoặc `async Task<T>` cho các 'phương thức bất đồng bộ' "**, trừ trường hợp **"bắt
      buộc"** phải dùng `async void` (ví dụ: event handlers).

    - **`async Task` khi "không cần 'trả về' giá trị"**.

    - **`async Task<T>` khi "cần 'trả về' kết quả" kiểu `T`**.

    - **`async void` "chỉ dùng" cho event handlers, và "cẩn thận" với những "cạm bẫy" của nó**.

- **"Ví dụ" "tổng kết" các kiểu trả về:**

  ```csharp
  // Phương thức "bất đồng bộ" "không trả về giá trị" - dùng 'async Task' (phổ biến)
  async Task HienThiThongBaoAsync(string thongBao)
  {
      await Task.Delay(1000); // "Giả vờ" "chờ" 1 giây
      MessageBox.Show(thongBao); // "Hiển thị" thông báo (không "trả về" gì thêm)
  }

  // Phương thức "bất đồng bộ" "trả về" "số lượng" byte đã tải - dùng 'async Task<int>' (phổ biến)
  async Task<int> TaiFileAsync(string url, string duongDanLuu)
  {
      // ... (code "tải" file "bất đồng bộ" và "lưu" xuống ổ cứng) ...
      int soByteDaTai = ...; // "Tính toán" "số lượng" byte đã tải
      return soByteDaTai; // "Trả về" "số lượng" byte (kiểu int)
  }

  // Event handler "bất đồng bộ" - dùng 'async void' (trường hợp "đặc biệt" - và cẩn thận)
  private async void btnTaiFile_Click(object sender, EventArgs e)
  {
      try
      {
          int byteDaTai = await TaiFileAsync("https://example.com/file.zip", "C:\\Downloads\\file.zip"); // "Gọi" phương thức "tải file" "bất đồng bộ" và "chờ"
          MessageBox.Show($"Tải file thành công! Đã tải {byteDaTai} bytes."); // Thông báo "tải thành công"
      }
      catch (Exception ex)
      {
          MessageBox.Show($"Lỗi tải file: {ex.Message}"); // Xử lý lỗi
      }
  }
  ```

**Tổng Kết Chương 4:**

- Bạn đã "mổ xẻ" và "so sánh" các kiểu trả về của "phương thức bất đồng bộ": `async void`, `async Task`, và
  `async Task<T>`.
    - Hiểu rõ khi nào nên "dùng" `async void` (chỉ event handlers - và "cẩn thận").
    - "Nắm vững" "ưu điểm" và "ứng dụng" của `async Task` và `async Task<T>` ("lựa chọn 'vàng' " cho hầu hết các trường
      hợp).
    - "Thuộc lòng" "nguyên tắc vàng" chọn kiểu trả về cho "phương thức bất đồng bộ" để code "chuẩn chỉnh" và "ít lỗi".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: Bất Đồng Bộ Trong Thực Tế - "Ứng Dụng Vào Đời Sống"**. Chúng ta sẽ "thấy" cách "ứng
dụng" lập trình bất đồng bộ vào các "tình huống" "thực tế" như "thao tác" I/O (file, mạng, database), "xây dựng" ứng
dụng web "nhanh nhẹn", và nhiều hơn nữa.

Bạn có câu hỏi nào về `async void`, `async Task`, và `async Task<T>` không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn
sàng "giải đáp" và "cùng bạn" "làm chủ" bất đồng bộ.

