# Chương 2: LINQ to Objects - "Vọc Vạch" Dữ Liệu Trong Bộ Nhớ (Phần 1)

Chào mừng bạn trở lại với hành trình khám phá LINQ! Trong chương này, chúng ta sẽ bắt đầu "vọc vạch" **LINQ to Objects
**, tức là học cách dùng LINQ để làm việc với dữ liệu đang "nằm" trong bộ nhớ máy tính của bạn (ví dụ như các danh sách,
mảng...).

Hôm nay, chúng ta sẽ "làm quen" với nhóm **Toán Tử Truy Vấn Cơ Bản (Query Operators)** - những "chiêu thức" nền tảng
nhưng vô cùng "lợi hại" để "xử lý" dữ liệu. Hãy cùng nhau khám phá nhé!

---

## Phần 2.1. Các Toán Tử Truy Vấn Cơ Bản (Query Operators) - "Vũ Khí" Đầu Tiên Của Bạn

Nhóm toán tử này bao gồm những thao tác "quen thuộc" nhất khi làm việc với dữ liệu: **lọc**, **chọn**, **sắp xếp**, *
*nhóm**, **kết hợp**, và **loại bỏ trùng lặp**. Mỗi toán tử sẽ có "sức mạnh" và cách dùng riêng, chúng ta sẽ "mổ xẻ"
từng toán tử ngay sau đây:

---

### 2.1.1. `Where` – "Chiêu" Lọc Dữ Liệu - Chỉ Lấy Cái Mình Cần

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Toán tử `Where` giúp bạn **"lọc"** ra những "món đồ" (phần tử) từ một "rổ" dữ liệu (danh sách) dựa trên một **"tiêu
  chí"** nào đó. Nói một cách đơn giản, nó giống như bạn đang "soi" từng "món đồ" và chỉ giữ lại những cái **"đạt yêu
  cầu"** của bạn.

- **"Thần chú" (Cú pháp) của `Where`:**

    - **Method Syntax (Kiểu "chấm chấm"):**
      ```csharp
      source.Where(predicate)
      ```
    - **Query Syntax (Kiểu SQL):**
      ```csharp
      from element in source
      where predicate
      select element
      ```

  Trong đó:

    - `source`: Là "rổ" dữ liệu gốc của bạn (ví dụ: `List<T>`, `Array`, hoặc `IEnumerable<T>`).
    - `predicate`: Là **"tiêu chí"** lọc dữ liệu. Nó giống như một câu hỏi **"Đúng hay Sai?"** mà bạn đặt ra cho từng "
      món đồ" trong "rổ". Nếu "món đồ" nào trả lời là **"Đúng"**, nó sẽ được giữ lại, ngược lại sẽ bị "loại".
      `predicate` thường được viết bằng **biểu thức lambda** (ví dụ: `num => num > 5`).

- **Ví dụ "thực tế":** Lọc ra các số lớn hơn 5 từ danh sách số sau:

  ```csharp
  List<int> numbers = new List<int>() { 1, 8, 3, 12, 5, 9, 2 };

  // Method Syntax (Kiểu "chấm chấm")
  var numbersGreaterThan5_Method = numbers.Where(num => num > 5); // "Lọc" số lớn hơn 5

  // Query Syntax (Kiểu SQL)
  var numbersGreaterThan5_Query = from num in numbers // Từ danh sách 'numbers'
                                  where num > 5     // "Lọc" số lớn hơn 5
                                  select num;      // Giữ lại số đó

  Console.WriteLine("Các số lớn hơn 5:");
  foreach (var num in numbersGreaterThan5_Method) // Hoặc dùng numbersGreaterThan5_Query, kết quả như nhau
  {
      Console.WriteLine(num); // Kết quả: 8, 12, 9 (chỉ những số lớn hơn 5 được giữ lại)
  }
  ```

- **"Giải mã" ví dụ:**  
  Biểu thức `num => num > 5` chính là **"tiêu chí"** lọc của chúng ta (predicate). Nó "kiểm tra" từng số (`num`) trong
  danh sách `numbers` và chỉ "bật đèn xanh" (trả về `true`) cho những số nào **lớn hơn 5**. Những số được "bật đèn xanh"
  sẽ được giữ lại trong kết quả. Lưu ý rằng cả hai kiểu viết (Method Syntax và Query Syntax) đều cho ra kết quả giống
  nhau, và truy vấn chỉ thực sự "làm việc" khi bạn "xem" kết quả (nhờ cơ chế **deferred execution** - chúng ta sẽ nói về
  nó sau).

---

### 2.1.2. `Select` – "Chiêu" Chọn Và "Biến Hình" Dữ Liệu - Tạo Ra Dữ Liệu Mới Theo Ý Muốn

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Toán tử `Select` giúp bạn **"chọn"** ra một hoặc nhiều **"đặc điểm"** (thuộc tính) từ mỗi "món đồ" (phần tử) trong "
  rổ" dữ liệu, và có thể **"biến hình"** chúng thành một dạng dữ liệu **mới** (nếu bạn muốn). Nói cách khác, nó tạo ra
  một "rổ" dữ liệu **mới**, chứa những giá trị đã được bạn "chọn lọc" và "biến đổi" từ dữ liệu gốc.

- **"Thần chú" (Cú pháp) của `Select`:**

    - **Method Syntax (Kiểu "chấm chấm"):**
      ```csharp
      source.Select(selector)
      ```
    - **Query Syntax (Kiểu SQL):**
      ```csharp
      from element in source
      select selector
      ```

  Trong đó:

    - `source`: Vẫn là "rổ" dữ liệu gốc của bạn.
    - `selector`: Là **"công thức biến hình"**. Nó là một biểu thức lambda (ví dụ: `sv => sv.Ten`) giúp bạn "lấy ra"
      hoặc "tính toán" giá trị mới từ mỗi "món đồ" gốc.

- **Ví dụ "thực tế" 1: Chỉ chọn tên của sinh viên từ danh sách sinh viên:**

  ```csharp
  public class SinhVien // "Khuôn mẫu" SinhVien
  {
      public string Ten { get; set; } // Thuộc tính "Tên"
      public int Tuoi { get; set; }   // Thuộc tính "Tuổi"
  }

  List<SinhVien> danhSachSinhVien = new List<SinhVien>() // "Rổ" SinhVien
  {
      new SinhVien { Ten = "An", Tuoi = 20 },
      new SinhVien { Ten = "Binh", Tuoi = 22 },
      new SinhVien { Ten = "Lan", Tuoi = 21 }
  };

  // Method Syntax (Kiểu "chấm chấm")
  var tenSinhVien_Method = danhSachSinhVien.Select(sv => sv.Ten); // "Chọn" thuộc tính "Ten"

  // Query Syntax (Kiểu SQL)
  var tenSinhVien_Query = from sv in danhSachSinhVien // Từ danh sách 'danhSachSinhVien'
                          select sv.Ten;             // "Chọn" thuộc tính 'Ten'

  Console.WriteLine("Tên các sinh viên:");
  foreach (var ten in tenSinhVien_Method) // Hoặc dùng tenSinhVien_Query, kết quả như nhau
  {
      Console.WriteLine(ten); // Kết quả: An, Binh, Lan (chỉ còn tên sinh viên)
  }
  ```

- **Ví dụ "thực tế" 2: "Biến hình" dữ liệu - Tạo danh sách thông tin sinh viên dạng chuỗi:**

  ```csharp
  // Method Syntax (Kiểu "chấm chấm")
  var thongTinSinhVien_Method = danhSachSinhVien.Select(sv => $"Tên: {sv.Ten}, Tuổi: {sv.Tuoi}"); // "Biến hình" thành chuỗi

  // Query Syntax (Kiểu SQL)
  var thongTinSinhVien_Query = from sv in danhSachSinhVien // Từ danh sách 'danhSachSinhVien'
                               select $"Tên: {sv.Ten}, Tuổi: {sv.Tuoi}"; // "Biến hình" thành chuỗi

  Console.WriteLine("Thông tin sinh viên:");
  foreach (var thongTin in thongTinSinhVien_Method) // Hoặc dùng thongTinSinhVien_Query
  {
      Console.WriteLine(thongTin);
      // Kết quả:
      // Tên: An, Tuổi: 20
      // Tên: Binh, Tuổi: 22
      // Tên: Lan, Tuổi: 21 (dữ liệu đã được "biến hình" thành chuỗi)
  }
  ```

- **"Giải mã" ví dụ:**  
  `Select` cho phép bạn "chiếu" dữ liệu sang một "hình dạng" mới, có thể khác hoàn toàn so với kiểu dữ liệu gốc. Nó cũng
  trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) và hoạt động theo cơ chế deferred execution.

---

### 2.1.3. `OrderBy`, `OrderByDescending`, `ThenBy`, `ThenByDescending` – "Chiêu" Sắp Xếp Dữ Liệu - Ngăn Nắp Theo Ý Muốn

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Các toán tử này giúp bạn **"sắp xếp"** các "món đồ" trong "rổ" dữ liệu theo một hoặc nhiều **"tiêu chí"**.

    - **`OrderBy`**: Sắp xếp theo thứ tự **tăng dần** (từ nhỏ đến lớn, từ A đến Z).
    - **`OrderByDescending`**: Sắp xếp theo thứ tự **giảm dần** (từ lớn đến nhỏ, từ Z đến A).
    - **`ThenBy`**: Sắp xếp **thứ cấp** (nếu có "món đồ" nào có tiêu chí sắp xếp chính giống nhau), theo thứ tự **tăng
      dần**.
    - **`ThenByDescending`**: Sắp xếp **thứ cấp** theo thứ tự **giảm dần**.

- **"Thần chú" (Cú pháp) của các "chiêu" sắp xếp:**

    - **Method Syntax (Kiểu "chấm chấm"):**
      ```csharp
      source.OrderBy(keySelector);             // Tăng dần
      source.OrderByDescending(keySelector);   // Giảm dần
      source.ThenBy(keySelector);              // Tăng dần thứ cấp (sau OrderBy/OrderByDescending)
      source.ThenByDescending(keySelector);    // Giảm dần thứ cấp (sau OrderBy/OrderByDescending)
      ```
    - **Query Syntax (Kiểu SQL):**
      ```csharp
      orderby keySelector                      // Tăng dần
      orderby keySelector descending          // Giảm dần
      ```
      (Lưu ý: Query Syntax **không hỗ trợ trực tiếp `ThenBy`**. Nếu cần sắp xếp thứ cấp, bạn có thể "kết hợp" với Method
      Syntax.)

  Trong đó:

    - `keySelector`: Là **"tiêu chí sắp xếp"**. Nó là một biểu thức lambda (ví dụ: `sv => sv.Ten`) giúp bạn "chọn ra" *
      *"khóa"** (giá trị) mà bạn muốn dùng để sắp xếp từng "món đồ".

- **Ví dụ "thực tế":** Sắp xếp danh sách sinh viên theo tên (tăng dần), và nếu tên giống nhau thì sắp xếp theo tuổi (
  giảm dần):

  ```csharp
  // Sử dụng danhSachSinhVien đã định nghĩa ở ví dụ trước

  // Method Syntax (Kiểu "chấm chấm")
  var sinhVienDaSapXep_Method = danhSachSinhVien
                                  .OrderBy(sv => sv.Ten)          // Sắp xếp chính: theo tên (tăng dần)
                                  .ThenByDescending(sv => sv.Tuoi); // Sắp xếp thứ cấp: theo tuổi (giảm dần)

  // Query Syntax (Kiểu SQL) - Chỉ sắp xếp theo tên (tăng dần)
  var sinhVienDaSapXep_Query = from sv in danhSachSinhVien // Từ danh sách 'danhSachSinhVien'
                               orderby sv.Ten             // Sắp xếp theo tên (tăng dần)
                               select sv;                // Giữ lại sinh viên đó

  Console.WriteLine("Sinh viên đã sắp xếp:");
  foreach (var sv in sinhVienDaSapXep_Method) // Hoặc dùng sinhVienDaSapXep_Query (nếu chỉ sắp xếp theo tên)
  {
      Console.WriteLine($"Tên: {sv.Ten}, Tuổi: {sv.Tuoi}");
  }
  // Ví dụ kết quả (sắp xếp theo tên, rồi theo tuổi giảm dần nếu tên trùng):
  // Tên: An, Tuổi: 20
  // Tên: Binh, Tuổi: 22
  // Tên: Lan, Tuổi: 21
  // (Nếu có 2 sinh viên tên "An", người lớn tuổi hơn sẽ đứng trước)
  ```

- **"Giải mã" ví dụ:**  
  `OrderBy(sv => sv.Ten)` sắp xếp danh sách theo tên theo thứ tự ABC, còn `ThenByDescending(sv => sv.Tuoi)` thực hiện
  sắp xếp thứ hai (trong nhóm sinh viên có cùng tên) theo tuổi từ lớn đến nhỏ.

---

### 2.1.4. `GroupBy` – "Chiêu" Nhóm Dữ Liệu - Gom Chung "Đồ" Cùng Loại

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Toán tử `GroupBy` giúp bạn **"nhóm"** các "món đồ" trong "rổ" dữ liệu lại với nhau dựa trên một **"điểm chung"** (khóa
  nhóm). Kết quả là bạn sẽ có một "rổ" các "nhóm", mỗi "nhóm" chứa các "món đồ" có cùng "điểm chung" đó.

- **"Thần chú" (Cú pháp) của `GroupBy`:**

    - **Method Syntax (Kiểu "chấm chấm"):**
      ```csharp
      source.GroupBy(keySelector)
      ```
    - **Query Syntax (Kiểu SQL):**
      ```csharp
      from element in source
      group element by keySelector
      ```

  Trong đó:

    - `keySelector`: Là **"điểm chung" để nhóm**. Biểu thức lambda (ví dụ: `sv => sv.Tuoi`) này sẽ "chỉ ra" cách bạn
      muốn nhóm các "món đồ".

- **Ví dụ "thực tế":** Nhóm danh sách sinh viên theo tuổi:

  ```csharp
  // Sử dụng danhSachSinhVien đã định nghĩa ở trên

  // Method Syntax (Kiểu "chấm chấm")
  var sinhVienTheoTuoi_Method = danhSachSinhVien.GroupBy(sv => sv.Tuoi); // Nhóm theo "Tuổi"

  // Query Syntax (Kiểu SQL)
  var sinhVienTheoTuoi_Query = from sv in danhSachSinhVien // Từ danh sách 'danhSachSinhVien'
                               group sv by sv.Tuoi;      // Nhóm theo 'Tuổi'

  Console.WriteLine("Sinh viên được nhóm theo tuổi:");
  foreach (var group in sinhVienTheoTuoi_Method) // Hoặc dùng sinhVienTheoTuoi_Query
  {
      Console.WriteLine($"Tuổi: {group.Key}"); // group.Key là "điểm chung" (tuổi)
      foreach (var sv in group) // group chính là một "nhóm" các sinh viên cùng tuổi
      {
          Console.WriteLine($"  - Tên: {sv.Ten}");
      }
  }
  // Kết quả mẫu:
  // Sinh viên được nhóm theo tuổi:
  // Tuổi: 20
  //   - Tên: An
  // Tuổi: 22
  //   - Tên: Binh
  // Tuổi: 21
  //   - Tên: Lan
  ```

- **"Giải mã" ví dụ:**  
  Mỗi "nhóm" mà `GroupBy` tạo ra là một "hộp" `IGrouping<TKey, TElement>` với:
    - `group.Key`: Chứa giá trị của "điểm chung" (trong ví dụ này là tuổi).
    - `group`: Chứa danh sách các "món đồ" (sinh viên) thuộc "nhóm" đó.

---

### 2.1.5. `Join` – "Chiêu" Kết Hợp Dữ Liệu Từ Nhiều Nguồn - "Bắt Tay" Các "Rổ" Dữ Liệu

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Toán tử `Join` được dùng để **"kết hợp"** các "món đồ" từ **hai "rổ" dữ liệu khác nhau** dựa trên một **"mối liên hệ"
  ** chung giữa chúng (giống như phép JOIN trong SQL khi làm việc với cơ sở dữ liệu).

- **"Thần chú" (Cú pháp) của `Join` (chỉ có Method Syntax):**

  ```csharp
  source1.Join(source2,
               outerKeySelector,
               innerKeySelector,
               resultSelector)
  ```

  Trong đó:

    - `source1`: "Rổ" dữ liệu **thứ nhất** (rổ "chính", outer sequence).
    - `source2`: "Rổ" dữ liệu **thứ hai** (rổ "phụ", inner sequence).
    - `outerKeySelector`: Biểu thức lambda để "chọn ra" **"khóa liên kết"** từ mỗi "món đồ" trong `source1`.
    - `innerKeySelector`: Biểu thức lambda để "chọn ra" **"khóa liên kết"** từ mỗi "món đồ" trong `source2`.
    - `resultSelector`: Biểu thức lambda để "xác định" cách **"tạo ra"** một "món đồ" **mới** từ việc "kết hợp" một "món
      đồ" từ `source1` và một "món đồ" từ `source2` (khi chúng có "khóa liên kết" giống nhau).

- **Ví dụ "thực tế":** Kết hợp danh sách sinh viên và danh sách lớp học dựa trên "mã lớp" chung:

  ```csharp
  public class SinhVien // "Khuôn mẫu" SinhVien (mở rộng thêm thuộc tính MaLop)
  {
      public string Ten { get; set; }
      public int Tuoi { get; set; }
      public int MaLop { get; set; } // Mã lớp học - "mối liên hệ"
  }

  public class LopHoc // "Khuôn mẫu" LopHoc
  {
      public int MaLop { get; set; }   // Mã lớp học - "mối liên hệ"
      public string TenLop { get; set; } // Tên lớp học
  }

  List<SinhVien> danhSachSinhVien = new List<SinhVien>() // "Rổ" SinhVien
  {
      new SinhVien { Ten = "An", Tuoi = 20, MaLop = 1 }, // Sinh viên An học lớp 1
      new SinhVien { Ten = "Binh", Tuoi = 22, MaLop = 2 },// Sinh viên Binh học lớp 2
      new SinhVien { Ten = "Lan", Tuoi = 21, MaLop = 1 } // Sinh viên Lan học lớp 1
  };

  List<LopHoc> danhSachLopHoc = new List<LopHoc>() // "Rổ" LopHoc
  {
      new LopHoc { MaLop = 1, TenLop = "Toán" }, // Lớp 1 tên là "Toán"
      new LopHoc { MaLop = 2, TenLop = "Văn" },  // Lớp 2 tên là "Văn"
      new LopHoc { MaLop = 3, TenLop = "Anh" }   // Lớp 3 tên là "Anh"
  };

  var ketQuaJoin = danhSachSinhVien.Join( // "Bắt tay" 2 "rổ"
      danhSachLopHoc,                  // "Rổ" thứ hai (inner sequence)
      sinhVien => sinhVien.MaLop,        // "Khóa liên kết" từ "rổ" SinhVien (MaLop)
      lopHoc => lopHoc.MaLop,            // "Khóa liên kết" từ "rổ" LopHoc (MaLop)
      (sinhVien, lopHoc) => new          // "Công thức" tạo "món đồ" mới khi "bắt tay" thành công
      {
          TenSinhVien = sinhVien.Ten,   // Lấy tên sinh viên
          TenLopHoc = lopHoc.TenLop    // Lấy tên lớp học
      }
  );

  Console.WriteLine("Thông tin sinh viên và lớp học:");
  foreach (var item in ketQuaJoin) // Duyệt qua kết quả "bắt tay"
  {
      Console.WriteLine($"Sinh viên: {item.TenSinhVien}, Lớp: {item.TenLopHoc}");
  }
  // Kết quả:
  // Sinh viên: An, Lớp: Toán
  // Sinh viên: Binh, Lớp: Văn
  // Sinh viên: Lan, Lớp: Toán
  // (Sinh viên An và Lan cùng học lớp "Toán", sinh viên Binh học lớp "Văn")
  ```

- **"Giải mã" ví dụ:**  
  `Join` sẽ "bắt tay" các "món đồ" từ `danhSachSinhVien` và `danhSachLopHoc` khi chúng có thuộc tính `MaLop` giống nhau.
  Chỉ những cặp sinh viên và lớp học có `MaLop` "khớp" nhau mới được "kết hợp" và tạo ra "món đồ" mới trong kết quả.

---

### 2.1.6. `Distinct` – "Chiêu" Loại Bỏ Dữ Liệu Trùng Lặp - Chỉ Giữ Lại Hàng "Độc"

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Toán tử `Distinct` giúp bạn **"loại bỏ"** các "món đồ" **trùng lặp** trong "rổ" dữ liệu, chỉ giữ lại các giá trị **"
  độc nhất vô nhị"**.

- **"Thần chú" (Cú pháp) của `Distinct`:**

    - **Method Syntax (Kiểu "chấm chấm"):**
      ```csharp
      source.Distinct()
      // hoặc
      source.Distinct(comparer) // Nếu cần so sánh "đặc biệt"
      ```
    - **Query Syntax (Kiểu SQL):**
      ```csharp
      (from element in source
       select element).Distinct()
      ```

  Ở đây, `comparer` (nếu cần) là một "công cụ so sánh" đặc biệt, giúp bạn tùy chỉnh cách `Distinct` xác định xem hai "
  món đồ" có "giống nhau" hay không.

- **Ví dụ "thực tế":** Loại bỏ các số trùng lặp trong danh sách số:

  ```csharp
  List<int> numbersWithDuplicates = new List<int>() { 1, 2, 2, 3, 4, 4, 4, 5 }; // Danh sách có số trùng

  // Method Syntax (Kiểu "chấm chấm")
  var uniqueNumbers_Method = numbersWithDuplicates.Distinct(); // Loại bỏ trùng lặp

  // Query Syntax (Kiểu SQL)
  var uniqueNumbers_Query = (from num in numbersWithDuplicates // Từ danh sách 'numbersWithDuplicates'
                             select num).Distinct();         // Loại bỏ trùng lặp

  Console.WriteLine("Các số duy nhất:");
  foreach (var num in uniqueNumbers_Method) // Hoặc dùng uniqueNumbers_Query
  {
      Console.WriteLine(num); // Kết quả: 1, 2, 3, 4, 5 (các số trùng đã biến mất)
  }
  ```

- **"Giải mã" ví dụ:**  
  `Distinct()` sử dụng cách so sánh "mặc định" của kiểu dữ liệu (ví dụ: so sánh bằng giá trị cho số, so sánh bằng tham
  chiếu cho đối tượng) để tìm và loại bỏ các "món đồ" trùng lặp. Nó trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) chỉ
  chứa các "món đồ" "độc nhất", và cũng hoạt động theo cơ chế deferred execution.

---

### 2.1.7. `Union`, `Intersect`, `Except` – "Chiêu" Phép Toán Tập Hợp - Như Toán Học Mà Bạn Biết

Những toán tử này thực hiện các phép toán tập hợp quen thuộc (giống như trong môn Toán học) trên hai "rổ" dữ liệu:

- **`Union` – "Chiêu" Hợp:**  
  "Trộn" hai "rổ" dữ liệu lại với nhau và loại bỏ các "món đồ" trùng lặp, trả về một "rổ" mới chứa tất cả các "món đồ" "
  độc nhất" từ cả hai "rổ" ban đầu.

    - **"Thần chú" (Cú pháp):**
      ```csharp
      source1.Union(source2)
      // hoặc
      source1.Union(source2, comparer) // Nếu cần so sánh "đặc biệt"
      ```

- **`Intersect` – "Chiêu" Giao:**  
  Trả về một "rổ" mới chỉ chứa các "món đồ" **"chung"** mà có mặt ở **cả hai** "rổ" dữ liệu ban đầu.

    - **"Thần chú" (Cú pháp):**
      ```csharp
      source1.Intersect(source2)
      // hoặc
      source1.Intersect(source2, comparer) // Nếu cần so sánh "đặc biệt"
      ```

- **`Except` – "Chiêu" Hiệu:**  
  Trả về một "rổ" mới chỉ chứa các "món đồ" **"riêng"** có trong "rổ" thứ nhất nhưng **không có** trong "rổ" thứ hai.

    - **"Thần chú" (Cú pháp):**
      ```csharp
      source1.Except(source2)
      // hoặc
      source1.Except(source2, comparer) // Nếu cần so sánh "đặc biệt"
      ```

- **Ví dụ "thực tế":**

  ```csharp
  List<int> numbers1 = new List<int>() { 1, 2, 3, 4, 5 }; // "Rổ" số 1
  List<int> numbers2 = new List<int>() { 3, 5, 6, 7, 8 }; // "Rổ" số 2

  // Union - "Hợp" hai "rổ"
  var unionResult = numbers1.Union(numbers2); // Kết quả: 1, 2, 3, 4, 5, 6, 7, 8 (tất cả các số "độc nhất" từ cả hai "rổ")

  // Intersect - "Giao" hai "rổ"
  var intersectResult = numbers1.Intersect(numbers2); // Kết quả: 3, 5 (chỉ các số "chung" của cả hai "rổ")

  // Except - "Hiệu" của "rổ" 1 và "rổ" 2
  var exceptResult = numbers1.Except(numbers2); // Kết quả: 1, 2, 4 (chỉ các số có trong "rổ" 1 mà không có trong "rổ" 2)

  Console.WriteLine("Union (Hợp): " + string.Join(", ", unionResult));
  Console.WriteLine("Intersect (Giao): " + string.Join(", ", intersectResult));
  Console.WriteLine("Except (Hiệu): " + string.Join(", ", exceptResult));
  ```

- **"Giải mã" ví dụ:**  
  Các phép toán tập hợp này đều trả về một "rổ" dữ liệu mới (`IEnumerable<T>`), tự động loại bỏ trùng lặp, và cũng hoạt
  động theo cơ chế deferred execution.

---

### 2.1.8. `Concat` – "Chiêu" Ghép Nối Chuỗi - Nối Dài "Rổ" Dữ Liệu

- **"Tuyệt chiêu" này dùng để làm gì?**  
  Toán tử `Concat` giúp bạn **"ghép nối"** hai "rổ" dữ liệu lại với nhau theo thứ tự, **không loại bỏ** các "món đồ"
  trùng lặp. Nó giống như bạn "đổ" "rổ" thứ hai vào "rổ" thứ nhất để tạo ra một "rổ" dài hơn.

- **"Thần chú" (Cú pháp) của `Concat`:**

  ```csharp
  source1.Concat(source2)
  ```

  Trong đó, `source1` và `source2` là hai "rổ" dữ liệu mà bạn muốn ghép nối.

- **Ví dụ "thực tế":**

  ```csharp
  List<string> names1 = new List<string>() { "Alice", "Bob" }; // "Rổ" tên 1
  List<string> names2 = new List<string>() { "Charlie", "David", "Alice" }; // "Rổ" tên 2 (có "Alice" trùng)

  var concatResult = names1.Concat(names2); // Ghép nối "rổ" 2 vào sau "rổ" 1

  Console.WriteLine("Concat (Ghép nối): " + string.Join(", ", concatResult));
  // Kết quả: "Alice", "Bob", "Charlie", "David", "Alice" (chú ý "Alice" bị lặp lại, không bị loại bỏ)
  ```

- **"Giải mã" ví dụ:**  
  `Concat` chỉ đơn giản là "dán" "rổ" thứ hai vào "đuôi" "rổ" thứ nhất, giữ nguyên tất cả các "món đồ" (kể cả những "món
  đồ" lặp lại), và trả về một "rổ" dữ liệu mới (`IEnumerable<T>`) thực hiện deferred execution.

---

## Bài Tập "Làm Nóng Tay"

Hãy cùng thử sức với một vài bài tập nhỏ sau để "luyện công" nhé:

1. **Bài Tập 1:**

    - Cho một danh sách các sản phẩm (Product) với các "đặc điểm": `TenSanPham` (Tên sản phẩm), `DanhMucSanPham` (Danh
      mục sản phẩm), `Gia` (Giá).
    - Dùng `Where` để "lọc" ra các sản phẩm có giá **cao hơn 100**.
    - Dùng `Select` để "lấy ra" danh sách **tên sản phẩm và giá** của các sản phẩm đã lọc, và "biến hình" thành chuỗi có
      dạng:  
      `"Sản phẩm: [Tên sản phẩm], Giá: [Giá]"`.

2. **Bài Tập 2:**

    - Dùng `OrderByDescending` để "sắp xếp" danh sách sản phẩm ban đầu theo **giá giảm dần**.

3. **Bài Tập 3:**

    - Sử dụng `GroupBy` để "nhóm" các sản phẩm theo `DanhMucSanPham`. In ra **tên danh mục** và danh sách các **sản phẩm
      ** thuộc danh mục đó.

4. **Bài Tập 4:**
    - Thử "kết hợp" các "chiêu" `Where`, `Select`, `OrderBy`, `GroupBy` trong một câu truy vấn để giải quyết một bài
      toán "khó" hơn. Ví dụ: Lấy danh sách các **danh mục** có **tổng giá trị sản phẩm** lớn hơn 500, và sắp xếp các
      danh mục này theo **tổng giá trị giảm dần**.

---

## Bước Tiếp Theo

Trong phần tiếp theo, chúng ta sẽ tiếp tục "khám phá" các toán tử truy vấn còn lại như `Join`, `Distinct`, `Union`,
`Intersect`, `Except`, và `Concat`. Hãy "thực hành" các ví dụ và bài tập ở đây cho đến khi bạn cảm thấy "thuần thục"
chúng, rồi chúng ta sẽ "lên đường" đến bước tiếp theo nhé!

Nếu bạn có bất kỳ câu hỏi hay "vướng mắc" nào về các toán tử `Where`, `Select`, `OrderBy`, `GroupBy` thì đừng ngần
ngại "hỏi han" nhé, chúng ta sẽ cùng nhau "tháo gỡ" để hiểu sâu hơn!

Chúc bạn "luyện công" vui vẻ và hiệu quả!
