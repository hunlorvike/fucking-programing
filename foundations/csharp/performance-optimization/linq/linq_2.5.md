## **2.5. Các Toán Tử Tạo Chuỗi và Tập Hợp (Generation Operators) - "Chiêu" Tự Sinh Dữ Liệu "Ảo"**

Chào mừng bạn đến với phần cuối của **Chương 2: LINQ to Objects**! Hôm nay, chúng ta sẽ học về nhóm toán tử **Tạo Chuỗi
và Tập Hợp (Generation Operators)**. Những "chiêu" này khá đặc biệt, chúng không làm việc với "rổ" dữ liệu sẵn có, mà
giúp bạn **"tự sinh ra"** những "rổ" dữ liệu **"mới toanh"** từ "hư không" (hoặc từ một vài "mẫu" có sẵn).

Hãy cùng khám phá các "chiêu" tạo dữ liệu "ảo diệu" này nhé!

\*\*2.5.1. `Range` - "Chiêu" Tạo "Dãy Số Đếm" - Đếm Số Liên Tục

- **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Range` dùng để **"tạo ra"** một "rổ" dữ liệu mới chứa một **"dãy số
  đếm"**, tức là các số nguyên liên tiếp nhau, bắt đầu từ một số nào đó và kéo dài trong một khoảng bao nhiêu số. Nó
  giống như bạn đang "đếm số" từ một điểm bắt đầu đến một điểm kết thúc, và "ghi" lại tất cả các số đó vào một "rổ".

- **"Thần chú" (Cú pháp) của `Range` (chỉ có Method Syntax - và hơi đặc biệt):** `Enumerable.Range(start, count)`

  Trong đó:

    - `Enumerable.Range`: Bạn phải gọi `Range` thông qua lớp `Enumerable` (giống như gọi một "hàm đặc biệt" của LINQ).
    - `start`: Số nguyên **bắt đầu** dãy số đếm.
    - `count`: **Số lượng** số nguyên bạn muốn tạo ra trong dãy. Dãy số sẽ chứa `count` số, bắt đầu từ `start`, rồi
      `start + 1`, `start + 2`, ..., cho đến `start + count - 1`. `count` phải là một số **không âm** (0 hoặc lớn hơn).

- **Ví dụ "thực tế":** Tạo một "rổ" số đếm từ 1 đến 10:

  ```csharp
  // Tạo "rổ" số đếm từ 1 đến 10
  var numbersFrom1To10 = Enumerable.Range(1, 10); // Bắt đầu từ 1, tạo ra 10 số liên tiếp

  Console.WriteLine("Dãy số từ 1 đến 10:");
  foreach (var num in numbersFrom1To10)
  {
      Console.WriteLine(num);
      // Kết quả: 1 2 3 4 5 6 7 8 9 10 (dãy số đếm liên tục từ 1 đến 10)
  }
  ```

- **Ví dụ khác:** Tạo dãy số từ -5 đến 5 (tổng cộng 11 số):

  ```csharp
  var numbersFromNegative5To5 = Enumerable.Range(-5, 11); // Bắt đầu từ -5, tạo ra 11 số liên tiếp

  Console.WriteLine("Dãy số từ -5 đến 5:");
  foreach (var num in numbersFromNegative5To5)
  {
      Console.WriteLine(num);
      // Kết quả: -5 -4 -3 -2 -1 0 1 2 3 4 5 (dãy số đếm liên tục từ -5 đến 5)
  }
  ```

- **"Giải mã" ví dụ:**
    - `Enumerable.Range(start, count)` tạo ra một "rổ" dữ liệu mới (`IEnumerable<int>`).
    - Dãy số được tạo ra là **thực thi trì hoãn (deferred execution)**. Các số chỉ thực sự được "sinh ra" khi bạn "xem"
      chúng (ví dụ: bằng vòng lặp `foreach`).

\*\*2.5.2. `Repeat` - "Chiêu" Tạo "Dãy Lặp" - Lặp Đi Lặp Lại Một "Món Đồ"

- **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Repeat` dùng để **"tạo ra"** một "rổ" dữ liệu mới chỉ gồm **một "món
  đồ" duy nhất được lặp đi lặp lại** một số lần nhất định. Nó giống như bạn đang "copy" một "món đồ" nào đó ra nhiều bản
  sao và "xếp" chúng vào một "rổ".

- **"Thần chú" (Cú pháp) của `Repeat` (chỉ có Method Syntax - cũng hơi đặc biệt):** `Enumerable.Repeat(element, count)`

  Trong đó:

    - `Enumerable.Repeat`: Bạn cũng phải gọi `Repeat` thông qua lớp `Enumerable`.
    - `element`: **"Món đồ"** bạn muốn lặp lại trong dãy. Có thể là bất kỳ kiểu dữ liệu nào (số, chuỗi, đối tượng...).
    - `count`: **Số lần** bạn muốn lặp lại "món đồ" `element`. `count` cũng phải là một số **không âm**.

- **Ví dụ "thực tế":** Tạo một "rổ" chứa chuỗi "Hello" lặp lại 5 lần:

  ```csharp
  // Tạo "rổ" chứa "Hello" lặp lại 5 lần
  var helloStrings = Enumerable.Repeat("Hello", 5); // Lặp lại chuỗi "Hello" 5 lần

  Console.WriteLine("Dãy lặp lại 'Hello' 5 lần:");
  foreach (var str in helloStrings)
  {
      Console.WriteLine(str);
      // Kết quả:
      // Hello
      // Hello
      // Hello
      // Hello
      // Hello (chuỗi "Hello" được lặp lại 5 lần trong "rổ")
  }
  ```

- **Ví dụ khác:** Tạo "rổ" chứa số 0 lặp lại 3 lần:

  ```csharp
  var zeroNumbers = Enumerable.Repeat(0, 3); // Lặp lại số 0 3 lần

  Console.WriteLine("Dãy lặp lại số 0 3 lần:");
  foreach (var num in zeroNumbers)
  {
      Console.WriteLine(num);
      // Kết quả:
      // 0
      // 0
      // 0 (số 0 được lặp lại 3 lần trong "rổ")
  }
  ```

- **"Giải mã" ví dụ:**
    - `Enumerable.Repeat(element, count)` tạo ra một "rổ" dữ liệu mới (`IEnumerable<T>`), với kiểu dữ liệu `T` là kiểu
      của "món đồ" `element`.
    - "Rổ" dữ liệu được tạo ra cũng là **thực thi trì hoãn**.

\*\*2.5.3. `Empty` - "Chiêu" Tạo "Rổ Rỗng" - Không Có Gì Bên Trong

- **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Empty` dùng để **"tạo ra"** một "rổ" dữ liệu **"rỗng tuếch"** (không
  chứa bất kỳ "món đồ" nào) nhưng vẫn có **"kiểu dữ liệu"** rõ ràng. "Rổ rỗng" này có thể hữu ích trong một số tình
  huống "đặc biệt", ví dụ như khi bạn muốn trả về một "rổ rỗng" khi không có dữ liệu thực tế, hoặc để "kết hợp" với
  các "chiêu" LINQ khác.

- **"Thần chú" (Cú pháp) của `Empty` (chỉ có Method Syntax - và cần "chỉ định" kiểu dữ liệu):** `Enumerable.Empty<T>()`

  Trong đó:

    - `Enumerable.Empty<T>()`: Bạn cũng phải gọi `Empty` thông qua lớp `Enumerable`, và **phải "chỉ định" kiểu dữ liệu**
      cho "rổ rỗng" bằng cách đặt kiểu dữ liệu đó vào giữa dấu `<` và `>` (ví dụ: `<string>`, `<int>`, `<SinhVien>`,
      v.v.).

- **Ví dụ "thực tế":** Tạo một "rổ rỗng" để chứa chuỗi:

  ```csharp
  // Tạo "rổ rỗng" để chứa chuỗi
  var emptyStringList = Enumerable.Empty<string>(); // "Rổ" rỗng kiểu string

  Console.WriteLine("Rổ rỗng kiểu string:");
  Console.WriteLine($"Số phần tử trong rổ rỗng: {emptyStringList.Count()}"); // Kết quả: 0 (rổ rỗng thì số "món đồ" là 0)
  foreach (var str in emptyStringList) // Vòng lặp này sẽ không chạy lần nào vì "rổ" rỗng
  {
      Console.WriteLine(str); // Không có gì được in ra vì "rổ" rỗng
  }
  ```

- **Ví dụ khác:** Tạo "rổ rỗng" để chứa `SinhVien`:

  ```csharp
  var emptySinhVienList = Enumerable.Empty<SinhVien>(); // "Rổ" rỗng kiểu SinhVien (sử dụng "khuôn mẫu" SinhVien đã định nghĩa trước đó)

  Console.WriteLine("Rổ rỗng kiểu SinhVien:");
  Console.WriteLine($"Số phần tử trong rổ rỗng SinhVien: {emptySinhVienList.Count()}"); // Kết quả: 0 (rổ rỗng SinhVien cũng không có "món đồ" nào)
  ```

- **"Giải mã" ví dụ:**
    - `Enumerable.Empty<T>()` tạo ra một "rổ" dữ liệu mới (`IEnumerable<T>`) hoàn toàn "trống rỗng".
    - "Rổ rỗng" này vẫn có **"nhãn mác" kiểu dữ liệu** rõ ràng (ví dụ: `IEnumerable<string>`, `IEnumerable<int>`,
      `IEnumerable<SinhVien>`, v.v.).
    - `Empty` cũng là **thực thi trì hoãn**.

**Tổng Kết Các "Chiêu" Tạo Dữ Liệu:**

- `Enumerable.Range(start, count)`: Tạo "rổ" "dãy số đếm" trong một khoảng.
    - `Enumerable.Repeat(element, count)`: Tạo "rổ" "dãy lặp" chứa một "món đồ" lặp lại nhiều lần.
    - `Enumerable.Empty<T>()`: Tạo "rổ rỗng" của một kiểu dữ liệu cụ thể.

Các "chiêu" tạo dữ liệu này tuy "nhỏ mà có võ", có thể rất hữu ích trong nhiều tình huống, đặc biệt khi bạn cần "khởi
tạo" dữ liệu ban đầu, tạo dữ liệu "mẫu" để thử nghiệm, hoặc xử lý các trường hợp "không có dữ liệu" một cách linh hoạt.

**Bài Tập "Sáng Tạo" Dữ Liệu:**

1. Sử dụng `Enumerable.Range` để tạo một "rổ" số từ 10 đến 20, sau đó "lọc" ra các số chẵn trong "rổ" đó (dùng "chiêu"
   `Where` và `Select` đã học).
2. Sử dụng `Enumerable.Repeat` để tạo một "rổ" gồm 10 dấu sao ("\*"), sau đó "in ra" "rổ" dấu sao đó (mỗi dấu sao trên
   một dòng).
3. Tạo một "rổ rỗng" để chứa số nguyên, sau đó "kiểm tra" xem nó có phải là "rổ rỗng" thật không bằng cách dùng "chiêu"
   `Any()` (kết quả phải là `false` - "không có món đồ nào").
4. "Kết hợp" `Enumerable.Range` và `Select` để tạo một "rổ" chứa các **"bình phương"** của các số từ 1 đến 5 (ví dụ: 1,
   4, 9, 16, 25).
5. Sử dụng `Enumerable.Range` và `Repeat` (kết hợp) để tạo một "rổ" có dạng: 1, 1, 2, 2, 3, 3, 4, 4, 5, 5 (mỗi số từ 1
   đến 5 lặp lại 2 lần). Gợi ý: có thể dùng "chiêu" `SelectMany` sau khi dùng `Range` và `Repeat`. (Bài tập này hơi "khó
   nhằn" hơn một chút, thử thách khả năng sáng tạo của bạn!)

**Chúc mừng bạn đã hoàn thành **Chương 2: LINQ to Objects - "Vọc Vạch" Dữ Liệu Trong Bộ Nhớ**!**

Trong chương này, chúng ta đã đi qua rất nhiều "chiêu thức" quan trọng của LINQ to Objects, từ các "chiêu" truy vấn cơ
bản, tổng hợp, phân vùng, kiểm tra "món đồ", đến các "chiêu" tạo dữ liệu. Bạn đã có một "nền tảng" khá vững chắc để "làm
chủ" LINQ to Objects rồi đấy!

**Bước Tiếp Theo:**

Chúng ta sẽ "chuyển sang" **Chương 3: Cú Pháp LINQ Chi Tiết - Query Syntax và Method Syntax.** Chúng ta sẽ "mổ xẻ" sâu
hơn về sự khác biệt, ưu nhược điểm, và cách "kết hợp" linh hoạt hai "phong cách" viết lệnh LINQ này.

Bạn có câu hỏi nào về các "chiêu" tạo dữ liệu này, hoặc về bất kỳ phần nào trong LINQ to Objects mà chúng ta đã học
không? Hãy cứ "hỏi thoải mái" nhé!

