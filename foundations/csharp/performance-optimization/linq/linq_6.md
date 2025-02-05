## **Chương 6: Parallel LINQ (PLINQ) - "Bơm Ga" Cho Truy Vấn - Tăng Tốc Độ Xử Lý Dữ Liệu**

Chào mừng bạn đến với **Chương 6: Parallel LINQ (PLINQ)**! Trong chương này, chúng ta sẽ "lên đời" cho LINQ, học cách "
bơm ga" cho các truy vấn LINQ để chúng "chạy nhanh như gió" bằng **Parallel LINQ (PLINQ)**. PLINQ sẽ giúp bạn "tận
dụng" "sức mạnh" của bộ vi xử lý "đa nhân" để "xử lý" dữ liệu "siêu tốc".

**Phần 6: Parallel LINQ (PLINQ) - "Bơm Ga" Cho Truy Vấn**

**6.1. Giới thiệu PLINQ: Khi nào nên "bật chế độ" PLINQ? - "Tăng Tốc Khi Nào?"**

- **PLINQ (Parallel Language Integrated Query)**, dịch nôm na là **"LINQ Song Song"**. Nó là một "bản nâng cấp" của
  LINQ, được "thiết kế" để **"chạy" các truy vấn LINQ "song song"** trên nhiều "đường đua" (luồng) khác nhau. Điều này
  có thể giúp **"tăng tốc" "xử lý"** một cách "đáng kể", đặc biệt khi bạn "vật lộn" với **"núi" dữ liệu "khổng lồ"** và
  các "công việc tính toán" "nặng đô" (CPU-bound operations).

- **Khi nào nên "bật chế độ" PLINQ? (Khi nào nên "tăng tốc")**

    - **Khi bạn có CPU "khỏe" (đa nhân):** PLINQ "phát huy" sức mạnh khi máy tính của bạn có nhiều "lõi" CPU (đa nhân).
      Nếu máy bạn có nhiều "lõi", PLINQ có thể "mang lại" "hiệu quả" rõ rệt.
    - **Khi truy vấn "ngốn CPU" (CPU-bound):** Nếu truy vấn LINQ của bạn chủ yếu "xoay quanh" các phép "tính toán" trên
      dữ liệu (ví dụ: "lọc", "biến đổi", "sắp xếp" "phức tạp"), và không bị "nghẽn cổ chai" bởi các "thao tác" "chờ
      đợi" (I/O - ví dụ: "mở/ghi" file, "hỏi han" database), thì PLINQ có thể "giúp" "chạy nhanh hơn".
    - **Khi "núi" dữ liệu "cao ngất ngưởng":** Càng nhiều dữ liệu, "chi phí" "bật chế độ" song song càng được "bù đắp"
      bởi "lợi ích" "tăng tốc". PLINQ thường "làm tốt" nhất với các "rổ" dữ liệu "siêu to khổng lồ".
    - **Khi "tốc độ" là "vấn đề sống còn":** Nếu "thời gian" "chạy" truy vấn là một "nỗi đau", và bạn cần "vắt kiệt" "
      hiệu năng", hãy "nghía" đến PLINQ.

- **Khi nào "không nên" (hoặc cần "cẩn thận") "bật chế độ" PLINQ? (Khi nào "chạy chậm lại"?)**

    - **Khi truy vấn "nghẽn cổ chai" I/O (I/O-bound):** Nếu truy vấn chủ yếu "đứng hình" "chờ đợi" các "thao tác" I/O (
      ví dụ: "hỏi" database, "đọc" file từ ổ cứng "rùa bò", "gọi" dịch vụ web "chậm như sên"), việc "song song hóa" có
      thể "không ăn thua", thậm chí có thể làm "rùa" hơn do "chi phí" "bật chế độ" song song. Trong trường hợp "nghẽn"
      I/O, các "chiêu" lập trình "bất đồng bộ" (asynchronous programming) có thể "hợp lý" hơn.
    - **Khi truy vấn "nhanh như điện xẹt":** Việc "bật chế độ" song song có "tốn kém" (khởi động và "điều khiển" các "
      đường đua" - luồng). Nếu truy vấn của bạn đã "chạy vèo vèo" (ví dụ: chỉ vài "tích tắc" mili giây), việc "thêm mắm
      dặm muối" PLINQ có thể làm "chậm rì" hơn do "chi phí" này. **Hãy "đo thử" (benchmark)** để "biết chắc" PLINQ có
      thực sự "tăng tốc" trong trường hợp của bạn hay không.
    - **Khi truy vấn có "tác dụng phụ" (side-effects):** Nếu lambda expressions trong truy vấn của bạn có "tác dụng
      phụ" (ví dụ: "thay đổi" "trạng thái" bên ngoài, "ghi nhật ký", "cập nhật" "biến dùng chung"), việc "song song hóa"
      có thể "gây rối loạn" về "thứ tự", "đua xe" dữ liệu (race conditions), và kết quả "khó lường". Cần "cực kỳ cẩn
      thận" khi dùng PLINQ với "tác dụng phụ".
    - **Khi "thứ tự" kết quả là "vàng ngọc":** PLINQ có thể "xáo trộn" "thứ tự" của các "món đồ" trong "rổ" kết quả (trừ
      khi bạn dùng các "tùy chọn" đặc biệt). Nếu "thứ tự" là "mệnh lệnh", bạn cần "cân nhắc" hoặc dùng các "chiêu"
      PLINQ "giữ gìn" "thứ tự" (có thể "giảm nhiệt" "tăng tốc").
    - **Khi "bắt lỗi" trở nên "khó nhằn":** "Bắt lỗi" code "song song" thường "phức tạp" hơn code "tuần tự". Nếu bạn
      chưa "quen tay" với PLINQ, việc "bắt bệnh" có thể "vất vả" hơn.

**6.2. Sử dụng `AsParallel()` để "bật chế độ" song song cho truy vấn LINQ - "Nút Ga" Thần Thánh**

Cách "dễ nhất" để "biến" một truy vấn LINQ "chậm rãi" thành truy vấn PLINQ "siêu tốc" là dùng "chiêu" mở rộng *
*`.AsParallel()`** trên "rổ" dữ liệu gốc.

- **`.AsParallel()`:** "Biến hóa" một `IEnumerable<T>` thành một `ParallelQuery<T>`, "bật đèn xanh" cho các "chiêu" LINQ
  tiếp theo trong "dây chuyền" truy vấn được "chạy" "song song" (nếu có "cơ hội").

**Ví dụ:** Tính tổng bình phương các số chẵn trong một "rổ" số "khổng lồ", dùng PLINQ để "tăng tốc":

```csharp
using System.Diagnostics; // Để "đo giờ"
using System.Linq;      // Để dùng LINQ

List<int> numbers = Enumerable.Range(1, 10000000).ToList(); // "Rổ" 10 triệu số - "khổng lồ"

// Truy vấn LINQ "bình thường" (tuần tự - "chạy" từng bước một)
Stopwatch swSequential = Stopwatch.StartNew(); // Bấm giờ
long sumSquaresSequential = numbers.Where(num => num % 2 == 0) // "Lọc" số chẵn
                                    .Select(num => (long)num * num) // "Bình phương" số chẵn
                                    .Sum(); // "Tính tổng"
swSequential.Stop(); // Dừng bấm giờ
Console.WriteLine($"Tuần tự: Tổng bình phương số chẵn = {sumSquaresSequential}, Thời gian = {swSequential.ElapsedMilliseconds}ms"); // In kết quả và thời gian "chạy"

// Truy vấn PLINQ ("song song" - "chia đường đua")
Stopwatch swParallel = Stopwatch.StartNew(); // Bấm giờ
long sumSquaresParallel = numbers.AsParallel() // "Bật chế độ" PLINQ bằng AsParallel() - "chia đường đua"
                                  .Where(num => num % 2 == 0) // "Lọc" số chẵn (có thể "chạy" song song)
                                  .Select(num => (long)num * num) // "Bình phương" số chẵn (có thể "chạy" song song)
                                  .Sum(); // "Tính tổng" (vẫn "chạy" tuần tự, vì cần "gom" kết quả từ các "đường đua")
swParallel.Stop(); // Dừng bấm giờ
Console.WriteLine($"Song song (PLINQ): Tổng bình phương số chẵn = {sumSquaresParallel}, Thời gian = {swParallel.ElapsedMilliseconds}ms"); // In kết quả và thời gian "chạy" (so sánh với "tuần tự")
```

**"Giải mã" code:**

- `numbers.AsParallel()`: "Biến hóa" `numbers` (kiểu `List<int>`) thành `ParallelQuery<int>`. Từ "thời điểm vàng" này
  trở đi, các "chiêu" LINQ tiếp theo (như `Where`, `Select`, `Sum`) sẽ được "chạy" "song song" (nếu PLINQ "thấy" có "
  lợi").
- **PLINQ "tự quyết định":** "Bộ não" PLINQ sẽ "tự động" "phân tích" truy vấn, dữ liệu, và "sức khỏe" hệ thống để "quyết
  định" **có nên "song song hóa" "chiêu" nào** và **"mạnh tay" song song hóa đến mức nào** (dùng bao nhiêu "đường đua" -
  luồng) để "đạt đỉnh" "hiệu năng".
- **Deferred Execution (vẫn "hiệu lực"):** Ngay cả khi dùng PLINQ, các "chiêu" như `Where`, `Select` vẫn là "lười
  biếng" (deferred execution). Truy vấn chỉ thực sự "hành động" khi bạn "triệu hồi" "chiêu" thực thi ngay lập tức (như
  `Sum`, `ToList`, `ToArray`, v.v.) hoặc khi bạn "xem" kết quả bằng `foreach`.

**6.3. Các "nút tùy chỉnh" cho PLINQ (`WithDegreeOfParallelism`, `WithCancellation`, `WithMergeOptions`) - "Chỉnh PLINQ
Theo Ý Mình"**

PLINQ "mở lòng" cho bạn "tùy chỉnh" cách "song song hóa" truy vấn bằng một vài "chiêu" đặc biệt, giúp bạn "nắn nót" "
hiệu năng" và "điều khiển" "hành vi" của PLINQ.

- **`.WithDegreeOfParallelism(degree)`:** **"Điều chỉnh" "số lượng đường đua" tối đa** mà PLINQ có thể "dùng" để "chạy"
  truy vấn.

    - `degree`: "Số lượng đường đua" tối đa (số luồng tối đa). Nếu bạn "đặt" `degree = 1`, PLINQ sẽ "chạy" "một mình một
      ngựa" (tuần tự - giống như không dùng `AsParallel()`).
    - "Mặc định", PLINQ sẽ "tự động" "chọn" "số lượng đường đua" "tối ưu" (thường là "số lõi CPU"). Bạn có thể dùng
      `WithDegreeOfParallelism` để **"hạn chế" "số lượng đường đua"** nếu "cảm thấy" cần (ví dụ: để "giảm tải" cho hệ
      thống, hoặc khi truy vấn có "chờ đợi" I/O và bạn không muốn "mở" quá nhiều "đường đua" cùng lúc).

  ```csharp
  // "Hạn chế" PLINQ chỉ "dùng" tối đa 2 "đường đua" (luồng)
  long sumSquaresParallelLimitedThreads = numbers.AsParallel() // "Bật chế độ" PLINQ
                                                .WithDegreeOfParallelism(2) // "Giới hạn" chỉ dùng 2 luồng
                                                .Where(num => num % 2 == 0) // "Lọc" số chẵn
                                                .Select(num => (long)num * num) // "Bình phương"
                                                .Sum(); // "Tính tổng"
  ```

- **`.WithCancellation(cancellationToken)`:** "Cho phép" **"dừng cuộc đua"** (cancellation) truy vấn PLINQ "giữa chừng".

    - `cancellationToken`: Một đối tượng `CancellationToken`. Bạn có thể dùng `CancellationTokenSource` để "sinh ra"
      `CancellationToken` và "ra lệnh" "dừng cuộc đua" bằng cách "gọi" `cancellationTokenSource.Cancel()`.
    - Nếu "lệnh dừng" được "ban ra" trong khi truy vấn PLINQ đang "chạy", "lỗi" `OperationCanceledException` sẽ bị "ném"
      ra.

  ```csharp
  CancellationTokenSource cts = new CancellationTokenSource(); // "Trạm điều khiển" dừng cuộc đua
  CancellationToken token = cts.Token; // "Vé" báo hiệu dừng cuộc đua

  // Truy vấn PLINQ có "vé" báo hiệu dừng cuộc đua
  Task.Run(() => { // "Cho" truy vấn "chạy" "ngầm" (background task)
      try
      {
          long sumSquaresCancellable = numbers.AsParallel() // "Bật chế độ" PLINQ
                                              .WithCancellation(token) // "Gắn" "vé" báo hiệu dừng cuộc đua
                                              .Where(num => num % 2 == 0) // "Lọc" số chẵn (có thể bị "dừng" giữa chừng)
                                              .Select(num => (long)num * num) // "Bình phương" (có thể bị "dừng" giữa chừng)
                                              .Sum(); // "Tính tổng" (có thể bị "dừng" giữa chừng)
          Console.WriteLine($"\nPLINQ (có thể dừng): Tổng bình phương số chẵn = {sumSquaresCancellable}"); // In kết quả nếu "về đích" thành công
      }
      catch (OperationCanceledException) // Nếu bị "dừng cuộc đua"
      {
          Console.WriteLine("\nPLINQ query bị hủy bỏ."); // Thông báo "bị dừng cuộc đua"
      }
      catch (Exception ex) // Nếu có "sự cố" khác
      {
          Console.WriteLine($"\nLỗi trong PLINQ query: {ex.Message}"); // Thông báo "sự cố"
      }
  });

  // Sau một "khoảng thời gian", "ra lệnh" "dừng cuộc đua"
  Thread.Sleep(100); // "Giả vờ" truy vấn "chạy" mất thời gian
  cts.Cancel(); // "Ra lệnh" "dừng cuộc đua"

  Console.ReadKey(); // "Đợi" người dùng "bấm phím" để chương trình "kết thúc"
  ```

- **`.WithMergeOptions(mergeOptions)`:** "Điều khiển" cách PLINQ **"gộp" (merge)** kết quả từ các "đường đua" song song
  lại thành "hàng" kết quả "cuối cùng".

    - `mergeOptions`: Giá trị của "bảng chọn" (enum) `ParallelMergeOptions`:
        - `AutoBuffered` (mặc định): PLINQ "tự động" "chọn" cách "đệm" (buffer) kết quả để "cân bằng" giữa "tốc độ" và "
          độ trễ".
        - `DefaultBuffered`: PLINQ "đệm" kết quả từ **từng** "đường đua" trước khi "gộp". Có thể "tăng tốc" cho một số
          truy vấn, nhưng có thể "kéo dài" "thời gian chờ" khi "bắt đầu" "nhận" kết quả.
        - `FullyBuffered`: PLINQ "chờ" **tất cả** các "đường đua" "về đích" và "đệm" **toàn bộ** kết quả trước khi "gộp"
          và "trao tay" kết quả "cuối cùng". "Đảm bảo" "thứ tự" kết quả (nếu dùng `.AsOrdered()`), nhưng có thể "chờ lâu
          hơn" và "tốn" nhiều "bộ nhớ" hơn.
        - `NotBuffered`: PLINQ "trao tay" kết quả **ngay khi có** từ bất kỳ "đường đua" nào, không "đệm". Có thể "
          giảm" "thời gian chờ", nhưng "thứ tự" kết quả "không chắc chắn" (ngay cả khi dùng `.AsOrdered()`).

  ```csharp
  // Dùng MergeOptions.FullyBuffered để "giữ gìn" "thứ tự" (nếu dùng AsOrdered)
  var parallelQueryOrdered = numbers.AsParallel().AsOrdered() // "Bật chế độ" PLINQ và "yêu cầu" "giữ thứ tự"
                                    .WithMergeOptions(ParallelMergeOptions.FullyBuffered) // "Chọn" cách "gộp" kết quả: "đợi" hết rồi "gộp"
                                    .Where(num => num % 2 == 0) // "Lọc" số chẵn
                                    .Select(num => num * num); // "Bình phương"

  Console.WriteLine("\nPLINQ (Ordered, FullyBuffered):");
  foreach (var result in parallelQueryOrdered) // Duyệt qua kết quả, "thứ tự" được "giữ nguyên"
  {
      Console.WriteLine(result);
  }
  ```

**"Lưu ý" về `.AsOrdered()`: - "Giữ Gìn" "Thứ Tự" - Đánh Đổi "Tốc Độ"**

- `.AsOrdered()` "ra lệnh" cho PLINQ **"giữ nguyên" "thứ tự"** của các "món đồ" trong "rổ" gốc trong "rổ" kết quả.
    - Việc "giữ gìn" "thứ tự" thường "làm chậm" "tốc độ" "song song hóa" và có thể "giảm" "hiệu năng" so với khi không
      dùng `.AsOrdered()`.
    - Chỉ "dùng" `.AsOrdered()` khi "thứ tự" kết quả thực sự "quan trọng".

**6.4. Lưu ý và cạm bẫy khi sử dụng PLINQ - "Cẩn Thận Kẻo 'Tẩu Hỏa Nhập Ma' "**

Khi "cầm lái" PLINQ, hãy "nhớ kỹ" những "lời khuyên" và "cạm bẫy" sau:

- **"Chi phí" "bật chế độ" song song:** Việc "khởi động" và "điều khiển" "đường đua", "chia việc", và "gộp" kết quả
  cũng "tốn kém" "năng lượng". Đối với các truy vấn "nhỏ xíu" hoặc "nhanh như chớp", "chi phí" này có thể "vượt mặt" "
  lợi ích" "tăng tốc", khiến **PLINQ "chạy" "rùa bò" hơn truy vấn "bình thường"**. **Hãy "đo thử" (benchmark)** "tốc độ"
  cả hai phiên bản để "biết chắc" PLINQ có thực sự "đáng đồng tiền bát gạo" trong trường hợp của bạn hay không.
- **"Thứ tự" kết quả "hên xui" (mặc định):** PLINQ "chạy" "tùm lum tà la" song song, nên "thứ tự" "xử lý" các "món đồ"
  và "thứ tự" kết quả "trả về" **"không ai dám chắc"** giống như "rổ" gốc, trừ khi bạn dùng `.AsOrdered()`. Nếu "thứ tự"
  là "mệnh lệnh", hãy "cân nhắc" dùng `.AsOrdered()` (nhưng có thể "chậm" hơn) hoặc "thiết kế" code của bạn sao cho "
  không phụ thuộc" vào "thứ tự".
- **"Tác dụng phụ" trong lambda expressions - "Họa Vô Đơn Chí":** "Tránh xa" lambda expressions có "tác dụng phụ" (ví
  dụ: "thay đổi" "biến bên ngoài", "thao tác" I/O, "gọi" "hàm" không "an toàn" cho "đa luồng") trong truy vấn PLINQ. Vì
  các lambda expressions có thể được "chạy" "hỗn loạn" đồng thời trên nhiều "đường đua", "tác dụng phụ" có thể "gây ra"
  **"đua xe" dữ liệu (race conditions), "hỏng hóc" dữ liệu, và kết quả "khó đoán"**. Nếu "bắt buộc" phải có "tác dụng
  phụ", hãy "gia cố" chúng bằng "khóa" (locks) hoặc dùng các "rổ" dữ liệu "an toàn" cho "đa luồng", nhưng điều này có
  thể "triệt tiêu" "lợi ích" "tăng tốc" của "song song hóa". "Tốt nhất" là "tống khứ" "tác dụng phụ" hoàn toàn khỏi
  lambda expressions của PLINQ.
- **"Bắt lỗi" "khó lường":** "Bắt lỗi" code "song song" "gai góc" hơn code "tuần tự". "Dùng" debugger "cẩn thận", và có
  thể "ghi nhật ký" để "theo dấu" "hành trình" của PLINQ.
- **Exception handling - "Đón Đầu" "Sóng Gió":** Khi có "sự cố" (exception) "xảy ra" ở một "đường đua" của PLINQ, PLINQ
  sẽ "gom" hết tất cả các "sự cố" từ mọi "đường đua" và "ném" ra một "quả bom" `AggregateException` chứa đầy các "mảnh
  vỡ" exception con. Hãy "xử lý" `AggregateException` để "bắt" và "dập tắt" các "ngọn lửa" lỗi trong truy vấn song song.

**Tổng Kết Chương 6:**

- Bạn đã được "giới thiệu" về Parallel LINQ (PLINQ) và "thời điểm vàng" để "bật chế độ" PLINQ "tăng tốc" truy vấn.
    - Học cách dùng `.AsParallel()` để "song song hóa" truy vấn LINQ một cách "nhanh gọn lẹ".
    - Biết cách "tùy chỉnh" PLINQ bằng các "nút điều khiển" `.WithDegreeOfParallelism()`, `.WithCancellation()`,
      `.WithMergeOptions()`.
    - "Ghi nhớ" các "lời khuyên" và "cạm bẫy" "chí mạng" khi "cầm cương" PLINQ ("chi phí", "thứ tự", "tác dụng phụ", "
      bắt lỗi").

PLINQ là một "cỗ máy" "tăng tốc" dữ liệu "mạnh mẽ", nhưng cần được "lái" một cách "khéo léo" và "hiểu rõ" về "tính nết"
và "giới hạn" của nó. **Hãy luôn "đo đạc" và "kiểm tra" "hiệu năng"** để "chắc chắn" PLINQ thực sự "mang lại" "lợi ích"
cho ứng dụng của bạn.

**Bài Tập "Tăng Tốc":**

1. Viết một chương trình "thực hiện" một phép "tính toán" "nặng nhọc" (ví dụ: tính toán số Fibonacci, "tìm" số nguyên
   tố "siêu to khổng lồ") trên một "rổ" số "bạt ngàn".
2. "Đọ sức" "thời gian" "chạy" của truy vấn LINQ "bình thường" và truy vấn PLINQ ("dùng" `Stopwatch` để "bấm giờ").
3. "Thử nghiệm" với các "mức độ" khác nhau của `WithDegreeOfParallelism()` để "xem" "ảnh hưởng" đến "tốc độ".
4. "Thêm" "chức năng" "dừng cuộc đua" (cancellation) vào truy vấn PLINQ ("dùng" `CancellationTokenSource`).
5. "Thử nghiệm" với các `ParallelMergeOptions` khác nhau (nếu truy vấn của bạn có "thứ tự" "quan trọng").
6. "Tạo ra" một ví dụ về truy vấn PLINQ có "tác dụng phụ" (ví dụ: "tăng" một "biến đếm" trong lambda expression) và "
   quan sát" các "vấn đề" có thể "nảy sinh". (Bài tập này chỉ để "cảnh báo", "không khuyến khích" "làm theo" trong "thực
   tế").

**Bước Tiếp Theo:**

Chúng ta sẽ "bước vào" **Chương 7: LINQ "Pro" và Tối Ưu Hiệu Năng**. Chúng ta sẽ "khám phá" các "bí kíp" "nâng cao" hơn
như custom query operators ("chiêu thức" LINQ "độ"), expression trees ("bản thiết kế" truy vấn), "tối ưu hóa" "tốc độ"
truy vấn, "bắt bệnh" lỗi, và các "mẫu nhà đẹp" (Design Patterns) thường "gặp" với LINQ.

Bạn có câu hỏi nào về Parallel LINQ (PLINQ) này không? Hãy cứ "hỏi tự nhiên" nhé!
