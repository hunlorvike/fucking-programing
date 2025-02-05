## **2.3. Các Toán Tử Phân Vùng (Partitioning Operators) - "Chiêu" Chia Nhỏ Và Cắt Bớt Dữ Liệu**

Chào mừng bạn trở lại với **Chương 2: LINQ to Objects**! Hôm nay, chúng ta sẽ "bỏ túi" nhóm toán tử **Phân Vùng (Partitioning Operators)**. Những "chiêu" này giúp bạn **"chia nhỏ"** hoặc **"cắt bớt"** một phần dữ liệu từ "rổ" dữ liệu gốc, giống như bạn đang "chia bánh" hoặc "cắt tỉa" cây cảnh vậy!

Hãy cùng nhau khám phá các "chiêu" phân vùng dữ liệu này nhé!

\*\*2.3.1. `Take` - "Chiêu" Lấy Vài "Món" Đầu Tiên - "Nếm Thử" Một Ít

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Take` dùng để **"lấy"** ra một số lượng **"ấn định"** các "món đồ" **đầu tiên** từ "rổ" dữ liệu. Nó giống như bạn chỉ muốn "nếm thử" một vài "món" đầu tiên trong một "hàng dài" các món ăn.

-   **"Thần chú" (Cú pháp) của `Take` (chỉ có Method Syntax):** `source.Take(count)`

    Trong đó:

    -   `source`: "Rổ" dữ liệu gốc của bạn.
    -   `count`: Số lượng "món đồ" **muốn lấy** từ **đầu** "rổ".
        -   Nếu `count` **lớn hơn** số "món đồ" trong "rổ", `Take` sẽ trả về **tất cả** các "món đồ" trong "rổ".
        -   Nếu `count` **nhỏ hơn hoặc bằng 0**, `Take` sẽ trả về một "rổ" **rỗng** (không có "món đồ" nào).

-   **Ví dụ "thực tế":** Lấy 3 số đầu tiên từ danh sách số:

    ```csharp
    List<int> numbers = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }; // "Rổ" số

    // Lấy 3 số đầu tiên
    var first3Numbers = numbers.Take(3); // "Lấy" 3 "món" đầu tiên

    Console.WriteLine("3 số đầu tiên:");
    foreach (var num in first3Numbers)
    {
        Console.WriteLine(num); // Kết quả: 1 2 3 (chỉ 3 số đầu tiên được lấy)
    }
    ```

-   **"Giải mã" ví dụ:**
    -   `Take(3)` "lấy" 3 "món đồ" đầu tiên từ danh sách `numbers`.
    -   `Take` trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) chứa các "món đồ" đã lấy. Nó là "chiêu" **thực thi trì hoãn (deferred execution)**.

\*\*2.3.2. `Skip` - "Chiêu" Bỏ Qua Vài "Món" Đầu Tiên - "Nhường Nhịn" Phần Đầu

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `Skip` dùng để **"bỏ qua"** một số lượng **"ấn định"** các "món đồ" **đầu tiên** từ "rổ" dữ liệu, và sau đó trả về các "món đồ" **còn lại**. Nó giống như bạn "nhường" phần "đầu" của "hàng" cho người khác, và chỉ lấy phần **"sau"** thôi.

-   **"Thần chú" (Cú pháp) của `Skip` (chỉ có Method Syntax):** `source.Skip(count)`

    Trong đó:

    -   `source`: "Rổ" dữ liệu gốc.
    -   `count`: Số lượng "món đồ" **muốn bỏ qua** từ **đầu** "rổ".
        -   Nếu `count` **lớn hơn hoặc bằng** số "món đồ" trong "rổ", `Skip` sẽ trả về một "rổ" **rỗng**.
        -   Nếu `count` **nhỏ hơn 0**, `Skip` sẽ **không bỏ qua** "món đồ" nào, và trả về **toàn bộ** "rổ" dữ liệu gốc.

-   **Ví dụ "thực tế":** Bỏ qua 5 số đầu tiên và lấy các số còn lại từ danh sách số:

    ```csharp
    List<int> numbers = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }; // "Rổ" số

    // Bỏ qua 5 số đầu tiên
    var remainingNumbers = numbers.Skip(5); // "Bỏ qua" 5 "món" đầu tiên

    Console.WriteLine("Các số sau khi bỏ qua 5 số đầu:");
    foreach (var num in remainingNumbers)
    {
        Console.WriteLine(num); // Kết quả: 6 7 8 9 10 (5 số đầu tiên đã bị "bỏ qua", chỉ còn lại phần "sau")
    }
    ```

-   **"Giải mã" ví dụ:**
    -   `Skip(5)` "bỏ qua" 5 "món đồ" đầu tiên và trả về các "món đồ" từ vị trí thứ 6 trở đi.
    -   `Skip` trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) chứa các "món đồ" còn lại. Nó cũng là "chiêu" **thực thi trì hoãn (deferred execution)**.

\*\*2.3.3. `TakeWhile` - "Chiêu" Lấy "Món Đồ" Đến Khi "Hết Hứng" - Lấy Đến Khi Điều Kiện Sai

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `TakeWhile` dùng để **"lấy"** các "món đồ" từ **đầu** "rổ" dữ liệu **cho đến khi gặp một "món đồ" mà bạn "hết hứng"** (không còn "đạt tiêu chuẩn" - điều kiện sai). Khi bạn "hết hứng" lần đầu tiên, `TakeWhile` sẽ **dừng lại** và không lấy các "món đồ" còn lại, kể cả khi các "món đồ" sau đó có thể lại "đạt tiêu chuẩn".

-   **"Thần chú" (Cú pháp) của `TakeWhile` (chỉ có Method Syntax):** `source.TakeWhile(predicate)` hoặc `source.TakeWhile((element, index) => predicate)` (có thêm "số thứ tự")

    Trong đó:

    -   `source`: "Rổ" dữ liệu gốc.
    -   `predicate`: **"Tiêu chuẩn"** để "hứng thú". Nó là một biểu thức lambda (ví dụ: `num => num < 5`) chỉ định điều kiện. `TakeWhile` sẽ tiếp tục "lấy" "món đồ" khi `predicate` trả về `true` (còn "hứng thú").

-   **Ví dụ "thực tế":** Lấy các số từ đầu danh sách cho đến khi gặp số lớn hơn hoặc bằng 5 (lúc đó "hết hứng"):

    ```csharp
    List<int> numbers = new List<int>() { 1, 3, 2, 4, 5, 6, 1, 2 }; // "Rổ" số

    // Lấy các số nhỏ hơn 5 từ đầu "rổ" (còn "hứng thú" với số nhỏ hơn 5)
    var numbersLessThan5 = numbers.TakeWhile(num => num < 5); // "Lấy" trong khi số còn nhỏ hơn 5

    Console.WriteLine("Các số nhỏ hơn 5 từ đầu 'rổ':");
    foreach (var num in numbersLessThan5)
    {
        Console.WriteLine(num); // Kết quả: 1 3 2 4 (dừng lại khi gặp số 5, vì 5 không nhỏ hơn 5)
    }
    ```

-   **"Giải mã" ví dụ:**
    -   `TakeWhile(num => num < 5)` lấy các số từ đầu danh sách `numbers` cho đến khi gặp số 5 (số 5 không thỏa mãn `num < 5`, nên "hết hứng"). Các số 6, 1, 2 phía sau số 5 cũng không được lấy, dù chúng nhỏ hơn 5.
    -   `TakeWhile` trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) chứa các "món đồ" đã lấy. Nó là "chiêu" **thực thi trì hoãn (deferred execution)**.

\*\*2.3.4. `SkipWhile` - "Chiêu" Bỏ Qua "Món Đồ" Đến Khi "Hết Chán" - Bỏ Qua Đến Khi Điều Kiện Sai

-   **"Tuyệt chiêu" này dùng để làm gì?** Toán tử `SkipWhile` dùng để **"bỏ qua"** các "món đồ" từ **đầu** "rổ" dữ liệu **cho đến khi gặp một "món đồ" mà bạn "hết chán"** (không còn "chán ghét" - điều kiện sai). Khi bạn "hết chán" lần đầu tiên, `SkipWhile` sẽ **dừng bỏ qua** và trả về **tất cả các "món đồ" còn lại**, bắt đầu từ "món đồ" **không còn "chán"** đó, và bao gồm cả các "món đồ" sau đó dù chúng có thể lại "gây chán".

-   **"Thần chú" (Cú pháp) của `SkipWhile` (chỉ có Method Syntax):** `source.SkipWhile(predicate)` hoặc `source.SkipWhile((element, index) => predicate)` (có thêm "số thứ tự")

    Trong đó:

    -   `source`: "Rổ" dữ liệu gốc.
    -   `predicate`: **"Tiêu chuẩn"** để "chán ghét". Nó là một biểu thức lambda (ví dụ: `num => num < 5`) chỉ định điều kiện. `SkipWhile` sẽ tiếp tục "bỏ qua" "món đồ" khi `predicate` trả về `true` (còn "chán ghét").

-   **Ví dụ "thực tế":** Bỏ qua các số từ đầu danh sách cho đến khi gặp số lớn hơn hoặc bằng 5 (lúc đó "hết chán"), và lấy các số còn lại:

    ```csharp
    List<int> numbers = new List<int>() { 1, 3, 2, 4, 5, 6, 1, 2 }; // "Rổ" số

    // Bỏ qua các số nhỏ hơn 5 từ đầu "rổ" (còn "chán ghét" số nhỏ hơn 5)
    var numbersGreaterThanOrEqual5 = numbers.SkipWhile(num => num < 5); // "Bỏ qua" trong khi số còn nhỏ hơn 5

    Console.WriteLine("Các số sau khi bỏ qua các số nhỏ hơn 5 từ đầu 'rổ':");
    foreach (var num in numbersGreaterThanOrEqual5)
    {
        Console.WriteLine(num); // Kết quả: 5 6 1 2 (bắt đầu từ số 5, vì 5 không nhỏ hơn 5)
    }
    ```

-   **"Giải mã" ví dụ:**
    -   `SkipWhile(num => num < 5)` bỏ qua các số 1, 3, 2, 4 (vì chúng nhỏ hơn 5, còn "chán"). Khi gặp số 5 (không nhỏ hơn 5, "hết chán"), `SkipWhile` dừng bỏ qua và bắt đầu trả về từ số 5 trở đi, bao gồm cả số 6, 1, 2 phía sau, dù số 1 và 2 nhỏ hơn 5.
    -   `SkipWhile` trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) chứa các "món đồ" còn lại. Nó cũng là "chiêu" **thực thi trì hoãn (deferred execution)**.

**Phân Biệt `TakeWhile` và `SkipWhile` - "Hết Hứng" vs "Hết Chán":**

-   **`TakeWhile`**: "Lấy" các "món đồ" **trong khi** bạn còn "hứng thú" (điều kiện đúng). Dừng lại khi "hết hứng" (điều kiện sai) lần đầu.
-   **`SkipWhile`**: "Bỏ qua" các "món đồ" **trong khi** bạn còn "chán ghét" (điều kiện đúng). Bắt đầu "lấy" các "món đồ" khi "hết chán" (điều kiện sai) lần đầu và lấy tất cả các "món đồ" còn lại.

**Tổng Kết Các "Chiêu" Phân Vùng:**

-   `Take(count)`: "Lấy" `count` "món đồ" đầu tiên.
-   `Skip(count)`: "Bỏ qua" `count` "món đồ" đầu tiên và lấy phần còn lại.
-   `TakeWhile(predicate)`: "Lấy" các "món đồ" từ đầu "rổ" cho đến khi `predicate` sai (hết "hứng").
-   `SkipWhile(predicate)`: "Bỏ qua" các "món đồ" từ đầu "rổ" cho đến khi `predicate` sai (hết "chán"), và lấy phần còn lại.

Các "chiêu" phân vùng rất hữu ích khi bạn muốn làm việc với một "miếng bánh" nhỏ của "rổ" dữ liệu lớn, ví dụ: chia dữ liệu thành "trang" (phân trang), xử lý một đoạn "đầu" hoặc "cuối" của dữ liệu, hoặc xử lý dữ liệu theo một "luật lệ" nào đó cho đến một "điểm dừng" nhất định.

**Bài Tập "Thử Tay Nghề":**

1.  Cho một danh sách số nguyên (tưởng tượng như "hàng bánh kẹo").
2.  Sử dụng `Take` để lấy 5 cái "bánh" đầu tiên.
3.  Sử dụng `Skip` để bỏ qua 3 cái "kẹo" đầu tiên và lấy phần "kẹo" còn lại.
4.  Sử dụng `TakeWhile` để lấy các "món ăn" từ đầu "hàng" cho đến khi gặp "món" đầu tiên là "bánh ngọt" (giả sử bạn không thích bánh ngọt lắm).
5.  Sử dụng `SkipWhile` để bỏ qua các "món mặn" từ đầu "hàng" và lấy phần "còn lại" (giả sử bạn chỉ thích ăn đồ ngọt sau khi ăn mặn).
6.  "Kết hợp" `Skip` và `Take` để lấy một "trang" dữ liệu từ danh sách (ví dụ: trang thứ 2, mỗi trang 5 phần tử). Tưởng tượng như bạn đang xem một cuốn sách và muốn "lật" đến trang thứ 2, mỗi trang có 5 dòng.

**Bước Tiếp Theo:**

Chúng ta sẽ "tiến quân" đến **Phần 2.4: Các Toán Tử Kiểm Tra (Element Operators)** như `First`, `FirstOrDefault`, `Last`, `LastOrDefault`, `Single`, `SingleOrDefault`, `ElementAt`, `ElementAtOrDefault`, `Any`, `All`, `Contains`, `SequenceEqual`.

Bạn có câu hỏi nào về các "chiêu" phân vùng này không? Hãy cứ "hỏi han" nhé!
