# Phần 2.2: Các Toán Tử Tổng Hợp (Aggregation Operators) - "Chiêu" Tính Toán Nhanh Trên Dữ Liệu

Chào mừng bạn đến với phần tiếp theo của **Chương 2: LINQ to Objects**! Hôm nay, chúng ta sẽ học về các **Toán Tử Tổng Hợp (Aggregation Operators)**. Nghe tên có vẻ "hàn lâm", nhưng thực chất chúng là những "chiêu" rất hữu ích để **"tóm tắt"** một "rổ" dữ liệu thành một **giá trị duy nhất**.

Ví dụ, bạn có thể dùng chúng để **đếm** số lượng "món đồ", **tính tổng** giá trị, **tính trung bình**, hoặc **tìm "món đồ" nhỏ nhất, lớn nhất** trong "rổ" dữ liệu của mình. Hãy cùng nhau khám phá những "chiêu" này nhé!

---

## 2.2.1. `Count` – "Chiêu" Đếm Số Lượng - Xem Có Bao Nhiêu "Món"

-   **"Tuyệt chiêu" này dùng để làm gì?**  
    `Count` dùng để **"đếm"** xem có bao nhiêu "món đồ" (phần tử) trong một "rổ" dữ liệu, hoặc **đếm** số "món đồ" **"đạt tiêu chuẩn"** (thỏa mãn điều kiện) mà bạn đặt ra.

-   **"Thần chú" (Cú pháp) của `Count`:**

    -   **Đếm tất cả "món đồ":**
        ```csharp
        source.Count();
        ```
    -   **Đếm "món đồ" "đạt tiêu chuẩn":**
        ```csharp
        source.Count(predicate);
        ```
        Trong đó:
    -   `source`: "Rổ" dữ liệu của bạn (ví dụ: `List<int>`, `IEnumerable<T>`, v.v.).
    -   `predicate`: **"Tiêu chuẩn"** để đếm. Nó là một biểu thức lambda (ví dụ: `num => num % 2 == 0`) giúp bạn xác định "món đồ" nào được tính là "đạt tiêu chuẩn".

-   **Ví dụ "thực tế":**

    ```csharp
    List<int> numbers = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }; // "Rổ" số

    // Đếm tổng số "món đồ" trong "rổ"
    int totalCount = numbers.Count(); // Kết quả: 10 (có 10 số trong danh sách)
    Console.WriteLine($"Tổng số phần tử: {totalCount}");

    // Đếm số "món đồ" "đạt tiêu chuẩn" - số chẵn
    int evenCount = numbers.Count(num => num % 2 == 0); // Kết quả: 5 (có 5 số chẵn)
    Console.WriteLine($"Số phần tử chẵn: {evenCount}");
    ```

-   **"Giải mã" ví dụ:**
    -   `Count()` "trơn" (không có gì bên trong) chỉ đơn giản là đếm tất cả "món đồ" trong "rổ".
    -   `Count(predicate)` sẽ "duyệt" qua từng "món đồ", và chỉ đếm những "món đồ" nào "vượt qua bài kiểm tra" (điều kiện trong `predicate` trả về `true`).
    -   Lưu ý: `Count` là "chiêu" **thực thi ngay lập tức (immediate execution)**, tức là nó sẽ "xem xét" hết cả "rổ" dữ liệu ngay khi bạn gọi nó.

---

## 2.2.2. `Sum` – "Chiêu" Tính Tổng - Cộng Hết Giá Trị Lại

-   **"Tuyệt chiêu" này dùng để làm gì?**  
    `Sum` được dùng để **"tính tổng"** tất cả các **giá trị số** trong một "rổ" dữ liệu.

-   **"Thần chú" (Cú pháp) của `Sum`:**

    -   **Tính tổng trực tiếp trên "rổ" số:**
        ```csharp
        source.Sum();
        ```
    -   **Tính tổng "gián tiếp" qua "công thức" (selector):**
        ```csharp
        source.Sum(selector);
        ```
        Trong đó:
    -   `source`: "Rổ" dữ liệu chứa các giá trị số, hoặc chứa các "món đồ" có **thuộc tính kiểu số**.
    -   `selector`: Là **"công thức"** để "lấy ra" giá trị số từ mỗi "món đồ". Nó là một biểu thức lambda (ví dụ: `sv => sv.Tuoi`) giúp bạn "chỉ định" thuộc tính nào (kiểu số) cần được cộng lại.

-   **Ví dụ "thực tế" 1: Tính tổng các số trong danh sách:**

    ```csharp
    List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 }; // "Rổ" số

    // Tính tổng tất cả các số trong "rổ"
    int sumOfNumbers = numbers.Sum(); // Kết quả: 15 (1 + 2 + 3 + 4 + 5 = 15)
    Console.WriteLine($"Tổng các số: {sumOfNumbers}");
    ```

-   **Ví dụ "thực tế" 2: Tính tổng tuổi của các sinh viên (dùng "công thức" selector):**

    ```csharp
    // Giả sử có danh sách sinh viên như ví dụ trước: danhSachSinhVien

    // Tính tổng "tuổi" của tất cả sinh viên
    int sumOfAges = danhSachSinhVien.Sum(sv => sv.Tuoi); // "Công thức": lấy thuộc tính "Tuoi"
    Console.WriteLine($"Tổng tuổi sinh viên: {sumOfAges}"); // Kết quả: 63 (20 + 22 + 21 = 63)
    ```

-   **"Giải mã" ví dụ:**
    -   `Sum()` "trơn" sẽ cộng trực tiếp các giá trị số trong "rổ".
    -   Khi dùng `Sum(selector)`, bạn "ra lệnh" cho LINQ là "hãy lấy thuộc tính 'Tuoi' từ mỗi sinh viên, rồi cộng tất cả các giá trị 'Tuoi' đó lại".
    -   Kết quả của `Sum` sẽ là một giá trị số (kiểu dữ liệu tùy thuộc vào dữ liệu đầu vào), và nó cũng là "chiêu" thực thi ngay lập tức.

---

## 2.2.3. `Average` – "Chiêu" Tính Trung Bình - Tìm Giá Trị "Đại Diện"

-   **"Tuyệt chiêu" này dùng để làm gì?**  
    `Average` giúp bạn **"tính giá trị trung bình"** của các giá trị số trong một "rổ" dữ liệu.

-   **"Thần chú" (Cú pháp) của `Average`:**

    -   **Tính trung bình trực tiếp:**
        ```csharp
        source.Average();
        ```
    -   **Tính trung bình "gián tiếp" qua "công thức" (selector):**
        ```csharp
        source.Average(selector);
        ```
        Trong đó:
    -   `source`: "Rổ" dữ liệu số hoặc "rổ" chứa "món đồ" có thuộc tính số.
    -   `selector`: "Công thức" để "lấy ra" giá trị số cần tính trung bình (giống như trong `Sum`).

-   **Ví dụ "thực tế" 1: Tính trung bình các số trong danh sách:**

    ```csharp
    List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 }; // "Rổ" số

    // Tính trung bình của các số trong "rổ"
    double averageOfNumbers = numbers.Average(); // Kết quả: 3 (kiểu double, vì trung bình có thể là số thập phân)
    Console.WriteLine($"Trung bình các số: {averageOfNumbers}");
    ```

-   **Ví dụ "thực tế" 2: Tính tuổi trung bình của sinh viên (dùng "công thức" selector):**

    ```csharp
    // Sử dụng danhSachSinhVien đã định nghĩa trước đó

    // Tính tuổi trung bình của sinh viên
    double averageAge = danhSachSinhVien.Average(sv => sv.Tuoi); // "Công thức": lấy thuộc tính "Tuoi"
    Console.WriteLine($"Tuổi trung bình sinh viên: {averageAge}"); // Kết quả: 21 (kiểu double)
    ```

-   **"Giải mã" ví dụ:**
    -   `Average()` và `Average(selector)` hoạt động gần giống `Sum`, nhưng thay vì chỉ tính tổng, chúng còn "chia" tổng đó cho số lượng "món đồ" để ra giá trị trung bình.
    -   Kết quả của `Average` luôn là kiểu `double` (số thập phân) để đảm bảo tính chính xác.

---

## 2.2.4. `Min` – "Chiêu" Tìm Giá Trị Nhỏ Nhất - "Món Đồ" Bé Nhất

-   **"Tuyệt chiêu" này dùng để làm gì?**  
    `Min` được dùng để **"tìm ra"** giá trị **nhỏ nhất** trong một "rổ" dữ liệu.

-   **"Thần chú" (Cú pháp) của `Min`:**

    -   **Tìm giá trị nhỏ nhất trực tiếp:**
        ```csharp
        source.Min();
        ```
    -   **Tìm giá trị nhỏ nhất "gián tiếp" qua "công thức" (selector):**
        ```csharp
        source.Min(selector);
        ```
        Trong đó:
    -   `source`: "Rổ" dữ liệu.
    -   `selector`: "Công thức" để "chỉ ra" giá trị cần so sánh (nếu "rổ" không phải là "rổ" số, mà là "rổ" đối tượng).

-   **Ví dụ "thực tế" 1: Tìm số nhỏ nhất trong danh sách số:**

    ```csharp
    List<int> numbers = new List<int>() { 5, 2, 8, 1, 9 }; // "Rổ" số

    // Tìm số nhỏ nhất trong "rổ"
    int minNumber = numbers.Min(); // Kết quả: 1 (số 1 là nhỏ nhất)
    Console.WriteLine($"Số nhỏ nhất: {minNumber}");
    ```

-   **Ví dụ "thực tế" 2: Tìm tuổi nhỏ nhất của sinh viên (dùng "công thức" selector):**

    ```csharp
    // Sử dụng danhSachSinhVien đã định nghĩa trước đó

    // Tìm tuổi nhỏ nhất của sinh viên
    int minAge = danhSachSinhVien.Min(sv => sv.Tuoi); // "Công thức": lấy thuộc tính "Tuoi"
    Console.WriteLine($"Tuổi nhỏ nhất của sinh viên: {minAge}"); // Kết quả: 20 (sinh viên An 20 tuổi là nhỏ nhất)
    ```

-   **"Giải mã" ví dụ:**
    -   `Min()` sẽ tìm giá trị nhỏ nhất dựa trên cách so sánh "mặc định" của kiểu dữ liệu.
    -   Nếu dùng `Min(selector)`, bạn có thể "chỉ định" thuộc tính cụ thể để so sánh (ví dụ: so sánh tuổi thay vì so sánh toàn bộ đối tượng sinh viên).

---

## 2.2.5. `Max` – "Chiêu" Tìm Giá Trị Lớn Nhất - "Món Đồ" To Nhất

-   **"Tuyệt chiêu" này dùng để làm gì?**  
    Tương tự như `Min`, toán tử `Max` dùng để **"tìm ra"** giá trị **lớn nhất** trong "rổ" dữ liệu.

-   **"Thần chú" (Cú pháp) của `Max`:**

    -   **Tìm giá trị lớn nhất trực tiếp:**
        ```csharp
        source.Max();
        ```
    -   **Tìm giá trị lớn nhất "gián tiếp" qua "công thức" (selector):**
        ```csharp
        source.Max(selector);
        ```
        Trong đó:
    -   `source`: "Rổ" dữ liệu.
    -   `selector`: "Công thức" để "chỉ định" giá trị so sánh (tương tự `Min`).

-   **Ví dụ "thực tế" 1: Tìm số lớn nhất trong danh sách số:**

    ```csharp
    List<int> numbers = new List<int>() { 5, 2, 8, 1, 9 }; // "Rổ" số

    // Tìm số lớn nhất trong "rổ"
    int maxNumber = numbers.Max(); // Kết quả: 9 (số 9 là lớn nhất)
    Console.WriteLine($"Số lớn nhất: {maxNumber}");
    ```

-   **Ví dụ "thực tế" 2: Tìm tuổi lớn nhất của sinh viên (dùng "công thức" selector):**

    ```csharp
    // Sử dụng danhSachSinhVien đã định nghĩa trước đó

    // Tìm tuổi lớn nhất của sinh viên
    int maxAge = danhSachSinhVien.Max(sv => sv.Tuoi); // "Công thức": lấy thuộc tính "Tuoi"
    Console.WriteLine($"Tuổi lớn nhất của sinh viên: {maxAge}"); // Kết quả: 22 (sinh viên Bình 22 tuổi là lớn nhất)
    ```

-   **"Giải mã" ví dụ:**
    -   `Max()` hoạt động giống hệt `Min`, chỉ khác là nó tìm giá trị **lớn nhất** thay vì nhỏ nhất.

---

## 2.2.6. `Aggregate` – "Chiêu" Tổng Hợp "Đa Năng" - Tự "Chế" Phép Tính Tổng Hợp

-   **"Tuyệt chiêu" này dùng để làm gì?**  
    `Aggregate` là "chiêu" tổng hợp **"siêu cấp"**, cho phép bạn thực hiện các phép tính tổng hợp **"tùy biến"** theo ý muốn, không chỉ giới hạn ở tổng, trung bình, min hay max. Nó giúp bạn tự "thiết kế" một **"công thức"** (hàm tích lũy) để "kết hợp" các "món đồ" trong "rổ" lại với nhau và cho ra một kết quả duy nhất.

-   **"Thần chú" (Cú pháp) của `Aggregate`:**

    -   **Không có "món đồ" khởi đầu (seed):**
        ```csharp
        source.Aggregate(func)
        ```
    -   **Có "món đồ" khởi đầu (seed):**
        ```csharp
        source.Aggregate(seed, func)
        ```
    -   **Có "món đồ" khởi đầu và "công thức biến đổi" kết quả cuối cùng:**
        ```csharp
        source.Aggregate(seed, func, resultSelector)
        ```
        Trong đó:
    -   `source`: "Rổ" dữ liệu gốc.
    -   `seed`: "Món đồ" **khởi đầu** (giá trị ban đầu) cho quá trình tích lũy (ví dụ: 0 nếu bạn muốn tính tổng, 1 nếu muốn tính tích, một chuỗi rỗng nếu muốn ghép chuỗi...).
    -   `func`: **"Công thức tích lũy"**. Nó là một hàm (biểu thức lambda) kiểu `Func<TAccumulate, TSource, TAccumulate>`, nhận vào **"giá trị tích lũy hiện tại"** và **"món đồ" hiện tại** đang xét, rồi **"trả về"** "giá trị tích lũy **mới**".
    -   `resultSelector` (tùy chọn): "Công thức biến đổi" **kết quả cuối cùng**. Hàm này (biểu thức lambda) kiểu `Func<TAccumulate, TResult>` dùng để "chỉnh sửa" kết quả tích lũy cuối cùng trước khi trả về.

-   **Ví dụ "thực tế" 1: Tính tích của các số trong danh sách (không có "món đồ" khởi đầu):**

    ```csharp
    List<int> numbers = new List<int>() { 2, 3, 4 }; // "Rổ" số

    // Dùng Aggregate để tính tích (2 * 3 * 4 = 24)
    int product = numbers.Aggregate((accumulator, num) => accumulator * num);
    // "Giải thích":
    // - Lần 1: accumulator = 2 (lấy số đầu tiên làm giá trị khởi đầu), num = 3, kết quả = 6 (2 * 3) -> accumulator mới = 6
    // - Lần 2: accumulator = 6 (giá trị accumulator từ lần trước), num = 4, kết quả = 24 (6 * 4) -> accumulator mới = 24
    Console.WriteLine($"Tích các số: {product}"); // Kết quả: 24
    ```

-   **Ví dụ "thực tế" 2: Ghép tên sinh viên thành một chuỗi dài, cách nhau bởi dấu phẩy (có "món đồ" khởi đầu và "công thức biến đổi" cuối cùng):**

    ```csharp
    // Sử dụng danhSachSinhVien đã được định nghĩa từ trước

    string danhSachTenSinhVien = danhSachSinhVien.Aggregate(
        "Danh sách sinh viên: ",                      // "Món đồ" khởi đầu: chuỗi "Danh sách sinh viên: "
        (currentString, sv) => currentString + sv.Ten + ", ",  // "Công thức tích lũy": nối tên sinh viên vào chuỗi hiện tại, thêm dấu phẩy và khoảng trắng
        finalString => finalString.TrimEnd(',', ' ')    // "Công thức biến đổi" cuối cùng: loại bỏ dấu phẩy và khoảng trắng thừa ở cuối chuỗi
    );

    Console.WriteLine(danhSachTenSinhVien);
    // Kết quả: Danh sách sinh viên: An, Binh, Lan (chuỗi tên sinh viên, cách nhau bởi dấu phẩy)
    ```

-   **"Giải mã" ví dụ:**
    -   `Aggregate` cho phép bạn tự do "sáng tạo" các phép tính tổng hợp phức tạp.
    -   Nó cũng là "chiêu" **thực thi ngay lập tức**, kết quả được tính toán "tức thì" khi bạn gọi.

---

## Tổng Kết Các "Chiêu" Tổng Hợp

Trong phần này, chúng ta đã "bỏ túi" các toán tử tổng hợp sau:

-   **`Count`**: Đếm số lượng "món đồ" (hoặc "món đồ" "đạt tiêu chuẩn").
-   **`Sum`**: Tính tổng giá trị số.
-   **`Average`**: Tính giá trị trung bình.
    -   **`Min`**: Tìm giá trị nhỏ nhất.
    -   **`Max`**: Tìm giá trị lớn nhất.
    -   **`Aggregate`**: "Chiêu" tổng hợp "đa năng", tùy biến theo ý bạn.

Những "chiêu" này rất "đắc lực" khi bạn cần "rút gọn" một "rổ" dữ liệu thành một giá trị "tóm tắt" duy nhất, để làm báo cáo, thống kê, hoặc xử lý dữ liệu theo nhiều cách khác nhau.

---

## Bài Tập "Luyện Công"

Hãy cùng "luyện tập" với một số bài tập sau để "nâng cao trình độ" nhé:

1.  **Bài Tập 1:**

    -   Cho danh sách sản phẩm (Product) như các bài tập trước.
    -   Dùng `Count` để đếm **tổng số sản phẩm** trong danh sách.

2.  **Bài Tập 2:**

    -   Sử dụng `Sum` để tính **tổng giá trị** của **tất cả** sản phẩm trong danh sách.

3.  **Bài Tập 3:**

    -   Dùng `Average` để tính **giá trung bình** của sản phẩm.

4.  **Bài Tập 4:**

    -   Dùng `Min` và `Max` để tìm **giá sản phẩm thấp nhất** và **giá sản phẩm cao nhất**.

5.  **Bài Tập 5:**
    -   Sử dụng `Aggregate` để tạo một chuỗi **liệt kê tên tất cả sản phẩm**, cách nhau bởi dấu gạch ngang " - ". Ví dụ:  
        `"Sản phẩm A - Sản phẩm B - Sản phẩm C"`.

---

## Bước Tiếp Theo

Chúng ta sẽ tiếp tục "khám phá" **Phần 2.3: Các Toán Tử Phân Vùng (Partitioning Operators)** như `Take`, `Skip`, `TakeWhile`, `SkipWhile`. Trước khi "chuyển sang" phần đó, bạn hãy "thực hành" và đảm bảo đã "nắm chắc" các "chiêu" tổng hợp này nhé!

Nếu bạn có bất kỳ câu hỏi hay "thắc mắc" nào về `Count`, `Sum`, `Average`, `Min`, `Max` hay `Aggregate` thì hãy cứ "chia sẻ", chúng ta sẽ cùng nhau "mổ xẻ" để hiểu sâu hơn!

Chúc bạn học và "luyện công" thật hiệu quả!
