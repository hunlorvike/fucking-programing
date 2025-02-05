## **2.4. Các Toán Tử Kiểm Tra (Element Operators) - "Chiêu" Kiểm Tra Và "Bắt" Phần Tử**

Chào mừng bạn đến với phần tiếp theo của **Chương 2: LINQ to Objects**! Hôm nay, chúng ta sẽ khám phá nhóm toán tử **Kiểm Tra (Element Operators)**. Những "chiêu" này giúp bạn **"kiểm tra"** xem "rổ" dữ liệu có "đúng ý" bạn không, và **"bắt"** ra một hoặc một vài "món đồ" cụ thể từ "rổ" đó.

Hãy cùng nhau tìm hiểu các "chiêu" kiểm tra dữ liệu này nhé!

\*\*2.4.1. `First`, `FirstOrDefault` - "Chiêu" Bắt "Món Đồ" Đầu Tiên - Nhanh Tay Lấy Ngay

-   **"Tuyệt chiêu" này dùng để làm gì?**

    -   `First`: "Tóm" lấy **"món đồ" đầu tiên** trong "rổ" dữ liệu. Nếu "rổ" **rỗng** (không có "món đồ" nào), hoặc **không có "món đồ" nào "đạt tiêu chuẩn"** (nếu bạn có thêm "tiêu chuẩn"), thì `First` sẽ **"nổi giận"** và **ném ra lỗi** (`InvalidOperationException`).
    -   `FirstOrDefault`: Cũng "tóm" lấy **"món đồ" đầu tiên**, nhưng "hiền lành" hơn. Nếu "rổ" **rỗng**, hoặc **không có "món đồ" nào "đạt tiêu chuẩn"**, thì `FirstOrDefault` sẽ **"lặng lẽ"** trả về **"món đồ mặc định"** (ví dụ: số 0 cho số, `null` cho chuỗi hoặc đối tượng). **Không "nổi giận"** (không ném lỗi).

-   **"Thần chú" (Cú pháp) của `First`, `FirstOrDefault` (chỉ có Method Syntax):**

    -   `source.First()`: Lấy "món đồ" đầu tiên trong "rổ".
    -   `source.First(predicate)`: Lấy "món đồ" đầu tiên "đạt tiêu chuẩn" (`predicate`).
    -   `source.FirstOrDefault()`: Lấy "món đồ" đầu tiên, hoặc "món đồ mặc định" nếu "rổ" rỗng.
    -   `source.FirstOrDefault(predicate)`: Lấy "món đồ" đầu tiên "đạt tiêu chuẩn", hoặc "món đồ mặc định" nếu không có "món đồ" nào "đạt tiêu chuẩn".

    Trong đó:

    -   `source`: "Rổ" dữ liệu của bạn.
    -   `predicate` (tùy chọn): **"Tiêu chuẩn"** (biểu thức lambda, ví dụ: `num => num % 2 == 0`) để "lọc" "món đồ" đầu tiên.

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> numbers = new List<int>() { 10, 2, 5, 8, 3 }; // "Rổ" số

    // First - "Bắt" "món đồ" đầu tiên
    int firstNumber = numbers.First(); // Kết quả: 10 (số đầu tiên trong danh sách)
    Console.WriteLine($"Phần tử đầu tiên: {firstNumber}");

    int firstEvenNumber = numbers.First(num => num % 2 == 0); // "Bắt" "món đồ" chẵn đầu tiên
    Console.WriteLine($"Phần tử chẵn đầu tiên: {firstEvenNumber}"); // Kết quả: 10 (số chẵn đầu tiên)

    // FirstOrDefault - "Bắt" "món đồ" đầu tiên, hoặc "món đồ mặc định" nếu không có
    int firstOrDefaultNumber = numbers.FirstOrDefault(); // Kết quả: 10 (vẫn là số đầu tiên)
    Console.WriteLine($"FirstOrDefault (rổ không rỗng): {firstOrDefaultNumber}");

    int firstOrDefaultOddNumber = numbers.FirstOrDefault(num => num % 2 != 0); // "Bắt" "món đồ" lẻ đầu tiên, hoặc "mặc định"
    Console.WriteLine($"FirstOrDefault (có 'món đồ' thỏa mãn): {firstOrDefaultOddNumber}"); // Kết quả: 5 (số lẻ đầu tiên)

    List<int> emptyList = new List<int>(); // "Rổ" rỗng

    // Thử với "rổ" rỗng
    // int firstOfEmpty = emptyList.First(); // Lỗi: InvalidOperationException (rổ rỗng mà dùng First là "nổi giận"!)
    int firstOrDefaultOfEmpty = emptyList.FirstOrDefault(); // Kết quả: 0 (món đồ "mặc định" cho kiểu số int là 0)
    Console.WriteLine($"FirstOrDefault (rổ rỗng): {firstOrDefaultOfEmpty}");

    int firstOrDefaultNoMatch = numbers.FirstOrDefault(num => num > 100); // Không có số nào > 100
    Console.WriteLine($"FirstOrDefault (không 'món đồ' nào thỏa mãn): {firstOrDefaultNoMatch}"); // Kết quả: 0 (món đồ "mặc định" cho kiểu số int)
    ```

-   **"Giải mã" ví dụ:**
    -   `First()` và `First(predicate)` cố gắng "tóm" "món đồ" đầu tiên. Nếu không "tóm" được, chúng sẽ "nổi giận" (ném lỗi).
    -   `FirstOrDefault()` và `FirstOrDefault(predicate)` "dễ tính" hơn, trả về "món đồ mặc định" nếu không tìm thấy, tránh gây lỗi.
    -   "Món đồ mặc định" là gì? Tùy thuộc vào kiểu dữ liệu:
        -   Kiểu số (int, double, v.v.): là **0**.
        -   Kiểu đúng/sai (bool): là **`false`**.
        -   Kiểu "tham chiếu" (class, string, v.v.): là **`null`** (giống như "không có gì").
    -   Cả `First` và `FirstOrDefault` đều là "chiêu" **thực thi ngay lập tức (immediate execution)**. Chúng sẽ "xem xét" "rổ" dữ liệu từ đầu đến khi tìm được "món đồ" đầu tiên (hoặc xác định là không có).

\*\*2.4.2. `Last`, `LastOrDefault` - "Chiêu" Bắt "Món Đồ" Cuối Cùng - Để Dành Cái Tốt Nhất Đến Sau

-   **"Tuyệt chiêu" này dùng để làm gì?**

    -   `Last`: "Tóm" lấy **"món đồ" cuối cùng** trong "rổ" dữ liệu. Nếu "rổ" **rỗng**, hoặc **không có "món đồ" nào "đạt tiêu chuẩn"** (nếu có "tiêu chuẩn"), thì `Last` cũng sẽ **"nổi giận"** và **ném ra lỗi** (`InvalidOperationException`).
    -   `LastOrDefault`: Cũng "tóm" lấy **"món đồ" cuối cùng**, nhưng "dịu dàng" hơn. Nếu "rổ" **rỗng**, hoặc **không có "món đồ" nào "đạt tiêu chuẩn"**, thì `LastOrDefault` sẽ **"vui vẻ"** trả về **"món đồ mặc định"**. **Không "nổi đóa"** (không ném lỗi).

-   **"Thần chú" (Cú pháp) của `Last`, `LastOrDefault` (chỉ có Method Syntax):** Giống như `First` và `FirstOrDefault`, chỉ cần thay `First` bằng `Last` và `FirstOrDefault` bằng `LastOrDefault`.

    -   `source.Last()`
    -   `source.Last(predicate)`
    -   `source.LastOrDefault()`
    -   `source.LastOrDefault(predicate)`

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> numbers = new List<int>() { 10, 2, 5, 8, 3 }; // "Rổ" số

    // Last - "Bắt" "món đồ" cuối cùng
    int lastNumber = numbers.Last(); // Kết quả: 3 (số cuối cùng trong danh sách)
    Console.WriteLine($"Phần tử cuối cùng: {lastNumber}");

    int lastEvenNumber = numbers.Last(num => num % 2 == 0); // "Bắt" "món đồ" chẵn cuối cùng
    Console.WriteLine($"Phần tử chẵn cuối cùng: {lastEvenNumber}"); // Kết quả: 8 (số chẵn cuối cùng)

    // LastOrDefault - "Bắt" "món đồ" cuối cùng, hoặc "món đồ mặc định" nếu không có
    int lastOrDefaultNumber = numbers.LastOrDefault(); // Kết quả: 3 (vẫn là số cuối cùng)
    Console.WriteLine($"LastOrDefault (rổ không rỗng): {lastOrDefaultNumber}");

    int lastOrDefaultOddNumber = numbers.LastOrDefault(num => num % 2 != 0); // "Bắt" "món đồ" lẻ cuối cùng, hoặc "mặc định"
    Console.WriteLine($"LastOrDefault (có 'món đồ' thỏa mãn): {lastOrDefaultOddNumber}"); // Kết quả: 3 (số lẻ cuối cùng)

    List<int> emptyList = new List<int>(); // "Rổ" rỗng

    // Thử với "rổ" rỗng
    // int lastOfEmpty = emptyList.Last(); // Lỗi: InvalidOperationException (rổ rỗng mà dùng Last là "giận tím người"!)
    int lastOrDefaultOfEmpty = emptyList.LastOrDefault(); // Kết quả: 0 (món đồ "mặc định" cho kiểu số int)
    Console.WriteLine($"LastOrDefault (rổ rỗng): {lastOrDefaultOfEmpty}");

    int lastOrDefaultNoMatch = numbers.LastOrDefault(num => num > 100); // Không có số nào > 100
    Console.WriteLine($"LastOrDefault (không 'món đồ' nào thỏa mãn): {lastOrDefaultNoMatch}"); // Kết quả: 0 (món đồ "mặc định" cho kiểu số int)
    ```

-   **"Giải mã" ví dụ:** Tương tự như `First` và `FirstOrDefault`, nhưng "soi" vào **"món đồ" cuối cùng** của "rổ" dữ liệu. Cũng là "chiêu" **thực thi ngay lập tức**.

\*\*2.4.3. `Single`, `SingleOrDefault` - "Chiêu" Bắt "Món Đồ" Duy Nhất - Chỉ Một Và Không Hai

-   **"Tuyệt chiêu" này dùng để làm gì?**

    -   `Single`: "Tóm" lấy **"món đồ duy nhất"** trong "rổ" dữ liệu. Nếu "rổ" **rỗng**, hoặc **có nhiều hơn một "món đồ"**, hoặc **không có "món đồ" nào "đạt tiêu chuẩn"** (nếu có "tiêu chuẩn"), hoặc **có nhiều hơn một "món đồ" "đạt tiêu chuẩn"**, thì `Single` sẽ **"nổi trận lôi đình"** và **ném ra lỗi** (`InvalidOperationException`). Tóm lại, `Single` chỉ "chấp nhận" khi **chính xác có một "món đồ"** (hoặc một "món đồ" thỏa mãn điều kiện).
    -   `SingleOrDefault`: "Hiền lành" hơn `Single`. Trả về **"món đồ duy nhất"**, hoặc **"món đồ mặc định"** nếu "rổ" **rỗng**, hoặc **không có "món đồ" nào "đạt tiêu chuẩn"**. Nhưng nếu **có nhiều hơn một "món đồ"**, hoặc **nhiều hơn một "món đồ" "đạt tiêu chuẩn"**, thì `SingleOrDefault` vẫn sẽ **"bực bội"** và **ném ra lỗi** (`InvalidOperationException`). Tức là, `SingleOrDefault` chỉ "chấp nhận" khi có **tối đa một "món đồ"** (hoặc tối đa một "món đồ" thỏa mãn điều kiện).

-   **"Thần chú" (Cú pháp) của `Single`, `SingleOrDefault` (chỉ có Method Syntax):** Tương tự `First` và `FirstOrDefault`, chỉ thay bằng `Single` và `SingleOrDefault`.

    -   `source.Single()`
    -   `source.Single(predicate)`
    -   `source.SingleOrDefault()`
    -   `source.SingleOrDefault(predicate)`

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> numbers1 = new List<int>() { 5 }; // "Rổ" chỉ có 1 "món đồ"
    List<int> numbers2 = new List<int>() { 10, 5, 2 }; // "Rổ" có nhiều hơn 1 "món đồ"
    List<int> emptyList = new List<int>(); // "Rổ" rỗng

    // Single - "Bắt" "món đồ" duy nhất
    int singleNumber1 = numbers1.Single(); // Kết quả: 5 (vì chỉ có một số 5)
    Console.WriteLine($"Single (rổ 1 'món đồ'): {singleNumber1}");

    // int singleNumber2 = numbers2.Single(); // Lỗi: InvalidOperationException (rổ > 1 'món đồ' - "không chịu"!)
    // int singleOfEmpty = emptyList.Single(); // Lỗi: InvalidOperationException (rổ rỗng - cũng "không ưng"!)

    // SingleOrDefault - "Bắt" "món đồ" duy nhất, hoặc "mặc định" nếu không có, nhưng vẫn "giận" nếu có nhiều hơn 1
    int singleOrDefaultNumber1 = numbers1.SingleOrDefault(); // Kết quả: 5 (vẫn là số 5)
    Console.WriteLine($"SingleOrDefault (rổ 1 'món đồ'): {singleOrDefaultNumber1}");

    int singleOrDefaultOfEmpty = emptyList.SingleOrDefault(); // Kết quả: 0 (món đồ "mặc định" cho kiểu số int)
    Console.WriteLine($"SingleOrDefault (rổ rỗng): {singleOrDefaultOfEmpty}");

    // int singleOrDefaultNumber2 = numbers2.SingleOrDefault(); // Lỗi: InvalidOperationException (rổ > 1 'món đồ' - vẫn "giận"!)

    // Single với "tiêu chuẩn"
    List<SinhVien> danhSachSinhVien = new List<SinhVien>() // "Rổ" SinhVien
    {
        new SinhVien { Ten = "An", Tuoi = 20 }, // Chỉ có một sinh viên 20 tuổi (trong ví dụ này)
        // new SinhVien { Ten = "Binh", Tuoi = 22 }, // Bỏ comment để thử lỗi nếu có nhiều hơn 1 sinh viên >= 20 tuổi
        new SinhVien { Ten = "Lan", Tuoi = 21 }
    };

    SinhVien singleSinhVien20Tuoi = danhSachSinhVien.Single(sv => sv.Tuoi == 20); // Kết quả: SinhVien { Ten = "An", Tuoi = 20 } (vì chỉ có một sinh viên 20 tuổi)
    Console.WriteLine($"Single (tiêu chuẩn, 1 kết quả): {singleSinhVien20Tuoi.Ten}");

    // SinhVien singleOrDefaultSinhVien20Tuoi_Multiple = danhSachSinhVien.SingleOrDefault(sv => sv.Tuoi >= 20); // Lỗi: InvalidOperationException (nhiều hơn 1 sinh viên >= 20 tuổi nếu có Binh - vẫn "giận"!)
    SinhVien singleOrDefaultSinhVien25Tuoi = danhSachSinhVien.SingleOrDefault(sv => sv.Tuoi == 25); // Không có sinh viên 25 tuổi
    Console.WriteLine($"SingleOrDefault (tiêu chuẩn, không kết quả): {(singleOrDefaultSinhVien25Tuoi == null ? "null" : singleOrDefaultSinhVien25Tuoi.Ten)}"); // Kết quả: null (món đồ "mặc định" cho kiểu SinhVien là null)
    ```

-   **"Giải mã" ví dụ:**
    -   `Single` và `SingleOrDefault` dùng khi bạn **"chắc chắn"** rằng "rổ" dữ liệu phải chứa **chính xác một "món đồ"** (hoặc không có "món đồ" nào trong trường hợp `SingleOrDefault` và rổ rỗng/không thỏa mãn điều kiện).
    -   Chúng rất "khó tính": nếu không đúng "1 và chỉ 1", chúng sẽ "giận dữ" (ném lỗi), ngoại trừ `SingleOrDefault` trong trường hợp "rổ" rỗng hoặc không thỏa mãn điều kiện (trả về "món đồ mặc định" thay vì lỗi).
    -   Cũng là "chiêu" **thực thi ngay lập tức**.

\*\*2.4.4. `ElementAt`, `ElementAtOrDefault` - "Chiêu" Bắt "Món Đồ" Theo Vị Trí - Lấy Đúng "Chỗ" Mình Muốn

-   **"Tuyệt chiêu" này dùng để làm gì?**

    -   `ElementAt`: Trả về "món đồ" ở **"vị trí" (index)** mà bạn "chỉ định" trong "rổ" dữ liệu. Nếu "vị trí" bạn "chỉ định" **"không có thật"** trong "rổ" (vị trí quá nhỏ - nhỏ hơn 0, hoặc quá lớn - lớn hơn hoặc bằng số "món đồ"), thì `ElementAt` sẽ **"bực mình"** và **ném ra lỗi** (`ArgumentOutOfRangeException`).
    -   `ElementAtOrDefault`: Trả về "món đồ" ở "vị trí" "chỉ định", hoặc **"món đồ mặc định"** nếu "vị trí" **"không có thật"**. **Không "cáu gắt"** (không ném lỗi).

-   **"Thần chú" (Cú pháp) của `ElementAt`, `ElementAtOrDefault` (chỉ có Method Syntax):**

    -   `source.ElementAt(index)`
    -   `source.ElementAtOrDefault(index)`

    Trong đó:

    -   `source`: "Rổ" dữ liệu của bạn.
    -   `index`: **"Vị trí"** (số thứ tự) của "món đồ" bạn muốn lấy (bắt đầu đếm từ 0).

-   **Ví dụ "thực tế":**

    ```csharp
    List<string> colors = new List<string>() { "Red", "Green", "Blue" }; // "Rổ" màu sắc

    // ElementAt - "Bắt" "món đồ" ở vị trí chỉ định
    string colorAtIndex1 = colors.ElementAt(1); // Kết quả: "Green" (vị trí 1 là "món đồ" thứ 2, vì đếm từ 0)
    Console.WriteLine($"Phần tử tại vị trí 1: {colorAtIndex1}");

    // string colorAtIndex3 = colors.ElementAt(3); // Lỗi: ArgumentOutOfRangeException (vị trí 3 "vượt quá giới hạn" - "rổ" chỉ có 3 "món đồ", vị trí 0, 1, 2)

    // ElementAtOrDefault - "Bắt" "món đồ" ở vị trí chỉ định, hoặc "món đồ mặc định" nếu vị trí không có
    string colorAtIndex1OrDefault = colors.ElementAtOrDefault(1); // Kết quả: "Green" (vẫn là "món đồ" ở vị trí 1)
    Console.WriteLine($"ElementAtOrDefault (vị trí hợp lệ): {colorAtIndex1OrDefault}");

    string colorAtIndex4OrDefault = colors.ElementAtOrDefault(4); // Vị trí 4 "không có thật" (vượt quá giới hạn)
    Console.WriteLine($"ElementAtOrDefault (vị trí ngoài giới hạn): {(colorAtIndex4OrDefault == null ? "null" : colorAtIndex4OrDefault)}"); // Kết quả: null (món đồ "mặc định" cho kiểu string là null)
    ```

-   **"Giải mã" ví dụ:**
    -   `ElementAt` và `ElementAtOrDefault` giúp bạn "chỉ thẳng mặt" vào một "món đồ" trong "rổ" theo "số thứ tự" của nó, giống như bạn "gọi tên" một phần tử trong mảng hay danh sách bằng `[]`.
    -   `ElementAt` "nổi nóng" nếu "số thứ tự" không hợp lệ, còn `ElementAtOrDefault` thì "nhẹ nhàng" trả về "món đồ mặc định".
    -   Cả hai đều là "chiêu" **thực thi ngay lập tức**.

\*\*2.4.5. `Any` - "Chiêu" Hỏi "Có Không?" - Kiểm Tra Xem Có "Món Đồ" Nào "Đạt Tiêu Chuẩn" Không

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Any` dùng để **"hỏi"** xem trong "rổ" dữ liệu **"có ít nhất một "món đồ" nào đó"** "đạt tiêu chuẩn" (predicate) hay không. Nó trả lời **`true` (Có)** nếu có, và **`false` (Không)** nếu không. Nếu bạn không đưa ra "tiêu chuẩn" nào, `Any` chỉ đơn giản là **"hỏi"** xem "rổ" có **"rỗng"** hay không (trả lời `true` nếu không rỗng, `false` nếu rỗng).

-   **"Thần chú" (Cú pháp) của `Any` (chỉ có Method Syntax):**

    -   `source.Any()`: Hỏi xem "rổ" có rỗng không?
    -   `source.Any(predicate)`: Hỏi xem có "món đồ" nào "đạt tiêu chuẩn" không?

    Trong đó:

    -   `source`: "Rổ" dữ liệu của bạn.
    -   `predicate` (tùy chọn): **"Tiêu chuẩn"** (biểu thức lambda, ví dụ: `num => num % 2 == 0`) để kiểm tra.

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 }; // "Rổ" số
    List<int> emptyList = new List<int>(); // "Rổ" rỗng

    // Any - Hỏi xem "rổ" có "món đồ" nào không? (kiểm tra rỗng)
    bool hasAnyNumbers = numbers.Any(); // Kết quả: true (rổ 'numbers' không rỗng, có "món đồ")
    Console.WriteLine($"Rổ có phần tử nào không? {hasAnyNumbers}");

    bool isEmpty = emptyList.Any(); // Kết quả: false (rổ 'emptyList' rỗng, không có "món đồ")
    Console.WriteLine($"Rổ rỗng? {!isEmpty}"); // In ra "Rổ rỗng? true"

    // Any - Hỏi xem "rổ" có "món đồ" chẵn nào không? (kiểm tra điều kiện)
    bool hasEvenNumber = numbers.Any(num => num % 2 == 0); // Kết quả: true (có số 2, 4 là số chẵn)
    Console.WriteLine($"Rổ có số chẵn không? {hasEvenNumber}");

    bool hasNumberGreaterThan10 = numbers.Any(num => num > 10); // Kết quả: false (không có số nào > 10)
    Console.WriteLine($"Rổ có số > 10 không? {hasNumberGreaterThan10}");
    ```

-   **"Giải mã" ví dụ:**
    -   `Any()` "trơn" (không có tiêu chuẩn) chỉ kiểm tra xem "rổ" có "món đồ" nào bên trong không (kiểm tra rỗng).
    -   `Any(predicate)` kiểm tra xem có **ít nhất một** "món đồ" "vượt qua bài kiểm tra" (thỏa mãn điều kiện) hay không.
    -   `Any` trả lời bằng **`true` (Có)** hoặc **`false` (Không)**. Nó là "chiêu" **thực thi ngay lập tức**, nhưng có thể **"đi tắt đón đầu" (short-circuiting)**: nó sẽ dừng "xem xét" "rổ" ngay khi tìm thấy "món đồ" đầu tiên "đạt tiêu chuẩn" (hoặc xác định "rổ" rỗng nếu không có tiêu chuẩn).

\*\*2.4.6. `All` - "Chiêu" Hỏi "Tất Cả Đúng Không?" - Kiểm Tra Xem Tất Cả "Món Đồ" Có "Đạt Tiêu Chuẩn" Không

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `All` dùng để **"hỏi"** xem **"tất cả"** các "món đồ" trong "rổ" dữ liệu **có "đạt tiêu chuẩn"** (predicate) hay không. Nó trả lời **`true` (Đúng)** nếu **tất cả** "món đồ" đều "đạt", và **`false` (Sai)** nếu **chỉ cần một** "món đồ" không "đạt". Nếu "rổ" **rỗng**, `All` sẽ trả lời **`true` (Đúng)** (vì không có "món đồ" nào không "đạt tiêu chuẩn").

-   **"Thần chú" (Cú pháp) của `All` (chỉ có Method Syntax):** `source.All(predicate)`

    Trong đó:

    -   `source`: "Rổ" dữ liệu của bạn.
    -   `predicate`: **"Tiêu chuẩn"** (biểu thức lambda, ví dụ: `num => num % 2 == 0`) để kiểm tra **từng** "món đồ".

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> numbers1 = new List<int>() { 2, 4, 6, 8 }; // "Rổ" toàn số chẵn
    List<int> numbers2 = new List<int>() { 2, 4, 5, 8 }; // "Rổ" có số 5 lẻ
    List<int> emptyList = new List<int>(); // "Rổ" rỗng

    // All - Hỏi xem "tất cả" có phải số chẵn không?
    bool allEven1 = numbers1.All(num => num % 2 == 0); // Kết quả: true (tất cả đều chẵn)
    Console.WriteLine($"Tất cả đều chẵn (rổ 1)? {allEven1}");

    bool allEven2 = numbers2.All(num => num % 2 == 0); // Kết quả: false (có số 5 lẻ, không phải tất cả đều chẵn)
    Console.WriteLine($"Tất cả đều chẵn (rổ 2)? {allEven2}");

    bool allPositiveEmpty = emptyList.All(num => num > 0); // Kết quả: true (rổ rỗng, không có "món đồ" nào không > 0, nên coi như "tất cả đều đúng")
    Console.WriteLine($"Tất cả đều dương (rổ rỗng)? {allPositiveEmpty}");
    ```

-   **"Giải mã" ví dụ:**
    -   `All(predicate)` kiểm tra xem **mọi** "món đồ" trong "rổ" có "vượt qua bài kiểm tra" (thỏa mãn `predicate`) hay không.
    -   `All` trả lời bằng **`true` (Đúng)** hoặc **`false` (Sai)**. Nó là "chiêu" **thực thi ngay lập tức**, và cũng có thể **"đi tắt đón đầu"**: nó sẽ dừng "xem xét" "rổ" ngay khi tìm thấy "món đồ" đầu tiên không "đạt tiêu chuẩn".

\*\*2.4.7. `Contains` - "Chiêu" Hỏi "Có Chứa Không?" - Kiểm Tra Xem "Rổ" Có "Món Đồ" Cụ Thể Không

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Contains` dùng để **"hỏi"** xem "rổ" dữ liệu **có chứa một "món đồ" cụ thể** hay không. Nó trả lời **`true` (Có)** nếu có, và **`false` (Không)** nếu không. Bạn có thể dùng thêm "công cụ so sánh" đặc biệt (comparer) nếu muốn so sánh theo cách riêng.

-   **"Thần chú" (Cú pháp) của `Contains` (chỉ có Method Syntax):**

    -   `source.Contains(value)`: Hỏi xem `source` có chứa `value` không, so sánh "bình thường".
    -   `source.Contains(value, comparer)`: Hỏi xem `source` có chứa `value` không, so sánh bằng "công cụ" `comparer`.

    Trong đó:

    -   `source`: "Rổ" dữ liệu của bạn.
    -   `value`: "Món đồ" bạn muốn "kiểm tra" xem có trong "rổ" không.
    -   `comparer` (tùy chọn): "Công cụ so sánh" đặc biệt (`IEqualityComparer<TSource>`) để bạn "ra lệnh" cho `Contains` so sánh theo ý mình.

-   **Ví dụ "thực tế":**

    ```csharp
    List<string> fruits = new List<string>() { "Apple", "Banana", "Orange" }; // "Rổ" trái cây

    // Contains - Hỏi xem "rổ" có chứa "Banana" không? (so sánh "bình thường")
    bool hasBanana = fruits.Contains("Banana"); // Kết quả: true (có "Banana" trong "rổ")
    Console.WriteLine($"Rổ có chứa 'Banana'? {hasBanana}");

    bool hasGrape = fruits.Contains("Grape"); // Kết quả: false (không có "Grape" trong "rổ")
    Console.WriteLine($"Rổ có chứa 'Grape'? {hasGrape}");

    // Contains - Hỏi xem "rổ" có chứa "apple" không? (so sánh "không quan trọng" chữ hoa chữ thường)
    bool hasAppleIgnoreCase = fruits.Contains("apple", StringComparer.OrdinalIgnoreCase); // Kết quả: true (coi "apple" và "Apple" là giống nhau)
    Console.WriteLine($"Rổ có chứa 'apple' (không phân biệt hoa thường)? {hasAppleIgnoreCase}");
    ```

-   **"Giải mã" ví dụ:**
    -   `Contains(value)` so sánh "món đồ" `value` với các "món đồ" trong "rổ" bằng cách so sánh "bình thường" (ví dụ: so sánh bằng giá trị cho số, so sánh bằng chuỗi cho chuỗi...).
    -   `Contains(value, comparer)` cho phép bạn "chế" lại cách so sánh, ví dụ: so sánh chuỗi "không phân biệt" chữ hoa chữ thường.
    -   `Contains` trả lời bằng **`true` (Có)** hoặc **`false` (Không)**. Nó là "chiêu" **thực thi ngay lập tức**, và cũng có thể **"đi tắt đón đầu"**: nó sẽ dừng "xem xét" "rổ" ngay khi tìm thấy "món đồ" cần tìm.

\*\*2.4.8. `SequenceEqual` - "Chiêu" Hỏi "Giống Nhau Không?" - Kiểm Tra Xem Hai "Rổ" Có "Y Hệt" Nhau Không

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `SequenceEqual` dùng để **"hỏi"** xem **hai "rổ" dữ liệu** có **"y hệt" nhau** hay không. Hai "rổ" được coi là "y hệt" nhau nếu chúng có **cùng số lượng "món đồ"** và các "món đồ" ở **cùng vị trí** trong cả hai "rổ" phải **"giống nhau"** (theo cách so sánh "bình thường" hoặc "công cụ so sánh" tùy chỉnh).

-   **"Thần chú" (Cú pháp) của `SequenceEqual` (chỉ có Method Syntax):**

    -   `source1.SequenceEqual(source2)`: So sánh `source1` và `source2` bằng cách so sánh "bình thường".
    -   `source1.SequenceEqual(source2, comparer)`: So sánh `source1` và `source2` bằng "công cụ so sánh" `comparer`.

    Trong đó:

    -   `source1`, `source2`: Hai "rổ" dữ liệu bạn muốn so sánh.
    -   `comparer` (tùy chọn): "Công cụ so sánh" đặc biệt (`IEqualityComparer<TSource>`) để bạn "chỉ đạo" `SequenceEqual` so sánh theo ý mình.

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> list1 = new List<int>() { 1, 2, 3 }; // "Rổ" số 1
    List<int> list2 = new List<int>() { 1, 2, 3 }; // "Rổ" số 2 (giống hệt "rổ" 1)
    List<int> list3 = new List<int>() { 3, 2, 1 }; // "Rổ" số 3 (cùng "món đồ" nhưng khác thứ tự)
    List<int> list4 = new List<int>() { 1, 2, 3, 4 }; // "Rổ" số 4 (khác số lượng "món đồ")

    // SequenceEqual - So sánh "bình thường"
    bool isEqual1and2 = list1.SequenceEqual(list2); // Kết quả: true ("rổ" 1 và "rổ" 2 "y hệt" nhau)
    Console.WriteLine($"Rổ 1 và rổ 2 bằng nhau? {isEqual1and2}");

    bool isEqual1and3 = list1.SequenceEqual(list3); // Kết quả: false ("rổ" 1 và "rổ" 3 không "y hệt" nhau, dù cùng "món đồ" nhưng khác thứ tự)
    Console.WriteLine($"Rổ 1 và rổ 3 bằng nhau? {isEqual1and3}");

    bool isEqual1and4 = list1.SequenceEqual(list4); // Kết quả: false ("rổ" 1 và "rổ" 4 không "y hệt" nhau, khác số lượng "món đồ")
    Console.WriteLine($"Rổ 1 và rổ 4 bằng nhau? {isEqual1and4}");

    // SequenceEqual - So sánh "rổ" chuỗi
    List<string> names1 = new List<string>() { "Alice", "Bob" }; // "Rổ" tên 1
    List<string> names2 = new List<string>() { "alice", "bob" }; // "Rổ" tên 2 (khác chữ hoa chữ thường)

    bool isEqualNamesDefault = names1.SequenceEqual(names2); // Kết quả: false (so sánh "bình thường" phân biệt hoa thường, nên không "y hệt")
    Console.WriteLine($"Rổ tên 1 và rổ tên 2 bằng nhau (mặc định)? {isEqualNamesDefault}");

    bool isEqualNamesIgnoreCase = names1.SequenceEqual(names2, StringComparer.OrdinalIgnoreCase); // Kết quả: true (so sánh "không phân biệt" hoa thường, nên "y hệt" nhau)
    Console.WriteLine($"Rổ tên 1 và rổ tên 2 bằng nhau (không phân biệt hoa thường)? {isEqualNamesIgnoreCase}");
    ```

-   **"Giải mã" ví dụ:**
    -   `SequenceEqual` "soi" kỹ cả **"nội dung"** và **"thứ tự"** của các "món đồ" trong hai "rổ".
    -   Nó trả lời **`true` (Đúng)** chỉ khi cả hai "rổ" **giống hệt nhau "từng li từng tí"**.
    -   `SequenceEqual` trả lời bằng **`true` (Đúng)** hoặc **`false` (Sai)**. Nó là "chiêu" **thực thi ngay lập tức**, và sẽ "xem xét" lần lượt từng "món đồ" trong cả hai "rổ" để so sánh.

**Tổng Kết Các "Chiêu" Kiểm Tra:**

Chúng ta đã "học lỏm" các "chiêu" kiểm tra quan trọng:

-   `First`, `FirstOrDefault`: "Bắt" "món đồ" đầu tiên.
-   `Last`, `LastOrDefault`: "Bắt" "món đồ" cuối cùng.
-   `Single`, `SingleOrDefault`: "Bắt" "món đồ" duy nhất.
-   `ElementAt`, `ElementAtOrDefault`: "Bắt" "món đồ" theo "số thứ tự".
-   `Any`: Hỏi "Có không?", kiểm tra xem có "món đồ" nào "đạt tiêu chuẩn" không.
-   `All`: Hỏi "Tất cả đúng không?", kiểm tra xem tất cả "món đồ" có "đạt tiêu chuẩn" không.
-   `Contains`: Hỏi "Có chứa không?", kiểm tra xem "rổ" có "món đồ" cụ thể không.
-   `SequenceEqual`: Hỏi "Giống nhau không?", kiểm tra xem hai "rổ" có "y hệt" nhau không.

Các "chiêu" kiểm tra này rất "đa năng" khi bạn cần "xem xét" các "đặc điểm" của dữ liệu, lấy ra những "món đồ" "đặc biệt", hoặc so sánh các "rổ" dữ liệu với nhau.

**Bài Tập "Rèn Luyện" Nhãn Quan:**

1.  Cho một danh sách số nguyên (tưởng tượng như "đoàn tàu" số).
2.  Sử dụng `First` và `FirstOrDefault` để "bắt" số "đầu tàu" và số "đầu tàu" là số chẵn (chú ý xem điều gì xảy ra nếu không có số chẵn nào ở đầu tàu).
3.  Sử dụng `Last` và `LastOrDefault` để "bắt" số "toa tàu" cuối cùng và số "toa tàu" cuối cùng là số lẻ (tương tự, chú ý trường hợp không có số lẻ nào ở cuối).
4.  Tạo một danh sách chỉ có **một** số (ví dụ: "đoàn tàu" chỉ có một "toa"). Sử dụng `Single` và `SingleOrDefault` để "bắt" số đó. Sau đó, thử tạo danh sách **rỗng** và danh sách **nhiều hơn một số** để xem `Single` và `SingleOrDefault` "phản ứng" thế nào.
5.  Sử dụng `ElementAt` và `ElementAtOrDefault` để lấy "toa tàu" ở vị trí thứ 3 (index 2) và vị trí thứ 10 (index 9 - nếu "đoàn tàu" không đủ dài).
6.  Sử dụng `Any` để kiểm tra xem "đoàn tàu" có chứa "toa tàu" số âm nào không, và kiểm tra xem "đoàn tàu" có phải là "đoàn tàu rỗng" không.
7.  Sử dụng `All` để kiểm tra xem **tất cả** các "toa tàu" trong "đoàn tàu" có phải là "toa tàu dương" (số dương) không.
8.  Sử dụng `Contains` để kiểm tra xem "đoàn tàu" có chứa "toa tàu" số 5 hay không.
9.  Tạo hai "đoàn tàu" **giống hệt nhau** và hai "đoàn tàu" **khác nhau**. Sử dụng `SequenceEqual` để so sánh chúng và xem kết quả.

**Bước Tiếp Theo:**

Chúng ta sẽ "bước sang" **Phần 2.5: Các Toán Tử Tạo Chuỗi và Tập Hợp (Generation Operators)** như `Range`, `Repeat`, `Empty`.

Bạn có câu hỏi nào về các "chiêu" kiểm tra này không? Hãy cứ "hỏi tự nhiên" nhé!
