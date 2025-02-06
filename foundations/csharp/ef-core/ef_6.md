 # Chương 6: Truy Vấn Nâng Cao Với LINQ - "Hỏi Han" Database "Chuyên Nghiệp" - "Tuyệt Chiêu" LINQ "Cao Cấp" Để "Khai Thác" Dữ Liệu

Chào mừng bạn đến với **Chương 6: Truy Vấn Nâng Cao Với LINQ**! Trong chương này, chúng ta sẽ "nâng cấp" "trình độ" truy vấn LINQ của bạn lên một "đẳng cấp mới" với các "chiêu thức" "cao cấp" hơn, giúp bạn "khai thác" dữ liệu từ database một cách "mạnh mẽ", "linh hoạt", và "hiệu quả".

**Phần 6: Truy Vấn Nâng Cao Với LINQ - "Hỏi Han" Database "Chuyên Nghiệp"**

**6.1. Projections (Chọn Lọc Cột) - "Chiêu" "Chỉ Lấy" Dữ Liệu "Cần Thiết" - "Gọn Nhẹ" Hóa Truy Vấn**

-   **"Vấn đề": "Lấy Quá Nhiều Cột Dữ Liệu Không Cần Thiết" - "Lãng Phí" Tài Nguyên:**

    -   Trong các ví dụ truy vấn "cơ bản" ở Chương 3, chúng ta thường "lấy" **"toàn bộ"** các cột của bảng (ví dụ: `select sp` trong Query Syntax hoặc `.ToList()` sau `DbSet<SanPham>` trong Method Syntax).
    -   Tuy nhiên, trong nhiều trường hợp, bạn có thể **"không cần"** "lấy" **tất cả** các cột dữ liệu từ bảng, mà chỉ cần **"một vài"** cột **"cần thiết"** để "hiển thị" hoặc "xử lý".
    -   "Lấy" **"toàn bộ"** cột khi chỉ cần **"một vài"** cột là **"lãng phí"** tài nguyên database, "tăng" thời gian truy vấn, và "tăng" lượng dữ liệu "vận chuyển" từ database về ứng dụng.

-   **Projections (Chọn Lọc Cột) - "Chiêu" "Chọn Đúng" Cột "Cần":**

    -   **Projections** (trong LINQ và EF Core) là kỹ thuật giúp bạn **"chọn"** ra **"chỉ những cột"** dữ liệu mà bạn **"thực sự"** cần từ database, **"bỏ qua"** các cột "không cần thiết".
    -   Projections giúp **"gọn nhẹ" hóa** truy vấn, **"giảm"** lượng dữ liệu "vận chuyển", và **"tăng"** "hiệu năng" ứng dụng.

-   **"Cách thực hiện" Projections trong LINQ queries:**

    -   **Query Syntax:** "Dùng" từ khóa `select` để "chọn" ra các cột mong muốn, "tạo ra" một **"kiểu dữ liệu vô danh" (anonymous type)** hoặc một **DTO (Data Transfer Object) class** để "chứa" kết quả "chọn lọc".

        ```csharp
        // Query Syntax - "Chọn" "tên sản phẩm" và "giá" sản phẩm
        var sanPham_Ten_Gia_Query = from sp in dbContext.SanPhams // "Từ" bảng SanPhams
                                    select new // "Tạo" "kiểu dữ liệu vô danh" để "chứa" kết quả "chọn lọc"
                                    {
                                        Ten = sp.TenSanPham, // "Chọn" cột TenSanPham và "đặt tên" là "Ten"
                                        Gia = sp.Gia        // "Chọn" cột Gia và "đặt tên" là "Gia"
                                    };

        foreach (var item in sanPham_Ten_Gia_Query) // Duyệt qua kết quả "chọn lọc"
        {
            Console.WriteLine($"- Tên: {item.Ten}, Giá: {item.Gia:#,##0}"); // "Chỉ" có "tên" và "giá" sản phẩm, không có các cột khác
        }
        ```

    -   **Method Syntax:** "Dùng" "chiêu" `Select()` để "chọn" ra các cột mong muốn, "tương tự" "tạo ra" "kiểu dữ liệu vô danh" hoặc DTO class.

        ```csharp
        // Method Syntax - "Chọn" "tên sản phẩm" và "giá" sản phẩm
        var sanPham_Ten_Gia_Method = dbContext.SanPhams // "Bắt đầu" từ DbSet<SanPham>
                                             .Select(sp => new // "Chiêu" Select để "chọn" cột và "tạo" "kiểu dữ liệu vô danh"
                                             {
                                                 Ten = sp.TenSanPham, // "Chọn" cột TenSanPham và "đặt tên" là "Ten"
                                                 Gia = sp.Gia        // "Chọn" cột Gia và "đặt tên" là "Gia"
                                             })
                                             .ToList(); // "Ép" truy vấn "chạy" và "lấy" kết quả dạng List<kiểu vô danh>

        Console.WriteLine("\n--- Sản phẩm (chỉ tên và giá) ---");
        foreach (var item in sanPham_Ten_Gia_Method) // Duyệt qua kết quả "chọn lọc"
        {
            Console.WriteLine($"- Tên: {item.Ten}, Giá: {item.Gia:#,##0}"); // "Chỉ" có "tên" và "giá" sản phẩm
        }
        ```

-   **"Giải mã" code Projections:**

    -   `select new { Ten = sp.TenSanPham, Gia = sp.Gia }` (Query Syntax) và `.Select(sp => new { Ten = sp.TenSanPham, Gia = sp.Gia })` (Method Syntax): "Tạo ra" một **"kiểu dữ liệu vô danh"** "ngay tại chỗ" (anonymous type) với **"hai properties"**: `Ten` (lấy từ cột `sp.TenSanPham`) và `Gia` (lấy từ cột `sp.Gia`). Kết quả truy vấn sẽ là một "rổ" các đối tượng "vô danh" này, chỉ chứa "tên" và "giá" sản phẩm, "nhẹ nhàng" hơn so với việc "lấy" "toàn bộ" đối tượng `SanPham`.

**6.2. Filtering (Lọc Nâng Cao) - "Chiêu" "Lọc Dữ Liệu" "Chính Xác" Hơn - "Tìm Đúng" "Món Đồ" "Cần**

-   **"Vấn đề": "Lọc Dữ Liệu" "Đơn Giản" Chưa Đủ - "Nhu Cầu" "Lọc" "Phức Tạp" Hơn:**

    -   Trong Chương 3, chúng ta đã "làm quen" với "chiêu" `Where` để "lọc" dữ liệu theo các "điều kiện" "cơ bản" (ví dụ: `sp.Gia > 1000`, `sp.DanhMucSanPham == "Điện tử"`).
    -   Tuy nhiên, trong thực tế, bạn có thể gặp các "yêu cầu" "lọc" dữ liệu **"phức tạp" hơn**, cần "kết hợp" nhiều "điều kiện" "khác nhau", hoặc "lọc" theo các "tiêu chí" "nâng cao".

-   **Filtering (Lọc Nâng Cao) - "Chiêu" "Lọc Dữ Liệu" "Đa Dạng" và "Mạnh Mẽ":**

    -   **Filtering** (trong LINQ và EF Core) cung cấp các "chiêu thức" "đa dạng" và "mạnh mẽ" hơn để "lọc" dữ liệu theo các "tiêu chí" "phức tạp".

-   **"Các 'chiêu' lọc nâng cao" phổ biến:**

    -   **"Kết hợp" nhiều "điều kiện" bằng toán tử "logic" (AND, OR, NOT):**

        ```csharp
        // Lọc sản phẩm có "giá" > 1000 **VÀ** "danh mục" là "Điện tử" (AND)
        var sanPham_GiaHon1000_DienTu = dbContext.SanPhams
                                            .Where(sp => sp.Gia > 1000 && sp.DanhMucSanPham == "Điện tử") // "Kết hợp" 2 "điều kiện" bằng && (AND)
                                            .ToList();

        // Lọc sản phẩm có "giá" < 500 **HOẶC** "danh mục" là "Sách" (OR)
        var sanPham_GiaReHon500_Hoac_Sach = dbContext.SanPhams
                                                .Where(sp => sp.Gia < 500 || sp.DanhMucSanPham == "Sách") // "Kết hợp" 2 "điều kiện" bằng || (OR)
                                                .ToList();

        // Lọc sản phẩm **KHÔNG** thuộc "danh mục" "Điện tử" (NOT)
        var sanPham_KhongPhai_DienTu = dbContext.SanPhams
                                            .Where(sp => !(sp.DanhMucSanPham == "Điện tử")) // "Phủ định" "điều kiện" bằng ! (NOT)
                                            .ToList();
        ```

    -   **"Lọc" theo "khoảng giá trị" (Range):**

        ```csharp
        // Lọc sản phẩm có "giá" nằm trong "khoảng" từ 500 đến 1500 (bao gồm cả 500 và 1500)
        var sanPham_Gia_Tu_500_Den_1500 = dbContext.SanPhams
                                               .Where(sp => sp.Gia >= 500 && sp.Gia <= 1500) // "Lọc" theo "khoảng" bằng && (AND) và >=, <=
                                               .ToList();
        ```

    -   **"Lọc" theo "danh sách giá trị" (IN):**

        ```csharp
        // "Danh sách" các "danh mục" muốn "lọc"
        string[] danhMucCanLoc = { "Điện tử", "Sách" };

        // Lọc sản phẩm thuộc "một trong các" "danh mục" trong "danh sách" (IN)
        var sanPham_Thuoc_DanhMuc_Trong_DanhSach = dbContext.SanPhams
                                                        .Where(sp => danhMucCanLoc.Contains(sp.DanhMucSanPham)) // "Lọc" bằng Contains (IN) và "danh sách" 'danhMucCanLoc'
                                                        .ToList();
        ```

    -   **"Lọc" theo "chuỗi" (String operations):**

        ```csharp
        // Lọc sản phẩm có "tên sản phẩm" "chứa" từ khóa "Laptop" (Contains)
        var sanPham_Ten_Chua_Laptop = dbContext.SanPhams
                                             .Where(sp => sp.TenSanPham.Contains("Laptop")) // "Lọc" bằng Contains (chứa chuỗi con)
                                             .ToList();

        // Lọc sản phẩm có "tên sản phẩm" "bắt đầu bằng" chữ "S" (StartsWith)
        var sanPham_Ten_BatDau_S = dbContext.SanPhams
                                          .Where(sp => sp.TenSanPham.StartsWith("S")) // "Lọc" bằng StartsWith (bắt đầu bằng chuỗi)
                                          .ToList();

        // Lọc sản phẩm có "tên sản phẩm" "kết thúc bằng" chữ "o" (EndsWith)
        var sanPham_Ten_KetThuc_O = dbContext.SanPhams
                                           .Where(sp => sp.TenSanPham.EndsWith("o")) // "Lọc" bằng EndsWith (kết thúc bằng chuỗi)
                                           .ToList();
        ```

    -   **"Lọc" theo "ngày tháng" (DateTime operations):**

        (Ví dụ này cần thêm property `NgayNhapKho` kiểu `DateTime` vào Entity `SanPham`)

        ```csharp
        // Lọc sản phẩm được "nhập kho" trong "tháng 10 năm 2023"
        var sanPham_NhapKho_Thang10_2023 = dbContext.SanPhams
                                                 .Where(sp => sp.NgayNhapKho.Month == 10 && sp.NgayNhapKho.Year == 2023) // "Lọc" theo "tháng" và "năm" của DateTime
                                                 .ToList();

        // Lọc sản phẩm được "nhập kho" "sau ngày" 15/10/2023
        var sanPham_NhapKho_Sau_15_10_2023 = dbContext.SanPhams
                                                    .Where(sp => sp.NgayNhapKho > new DateTime(2023, 10, 15)) // "Lọc" theo "so sánh" DateTime
                                                    .ToList();
        ```

**6.3. Aggregation (Tổng Hợp) - "Chiêu" "Tính Toán" Trên Dữ Liệu Database - "Thống Kê" và "Phân Tích"**

-   **"Vấn đề": "Tính Toán" "Tổng Hợp" Trên Dữ Liệu "Khổng Lồ" Trong Database - "Không Muốn" "Tải" Hết Dữ Liệu Về Ứng Dụng:**

    -   Trong nhiều trường hợp, bạn muốn "thực hiện" các phép **"tính toán" "tổng hợp"** (aggregation) trên dữ liệu trong database (ví dụ: "đếm" số lượng sản phẩm, "tính tổng" "giá trị" sản phẩm, "tìm" "giá" sản phẩm "cao nhất", "thấp nhất", "trung bình", v.v.).
    -   Nếu bạn "tải" **"toàn bộ"** dữ liệu từ database về ứng dụng rồi mới "tính toán" "tổng hợp" trên client-side (trong bộ nhớ ứng dụng), sẽ rất **"kém hiệu quả"** khi dữ liệu có "kích thước" "khổng lồ". "Lãng phí" băng thông mạng, "ngốn" bộ nhớ ứng dụng, và "chậm" "thời gian" "xử lý".

-   **Aggregation (Tổng Hợp) - "Chiêu" "Tính Toán" "Ngay Trên Database" - "Tối Ưu Hiệu Năng" "Vượt Trội":**

    -   **Aggregation** (trong LINQ và EF Core) "cho phép" bạn "thực hiện" các phép "tính toán" "tổng hợp" **"trực tiếp" "trên database server"**, **"chỉ tải về" "kết quả" "tổng hợp" "cuối cùng"**, **"không cần" "tải" "toàn bộ" dữ liệu về ứng dụng**.
    -   Aggregation giúp **"tối ưu" "hiệu năng"** "truy vấn" một cách "vượt trội", đặc biệt khi làm việc với dữ liệu "lớn".

-   **"Các 'chiêu' tổng hợp" phổ biến trong LINQ và EF Core:**

    -   **`Count()` - "Đếm" số lượng bản ghi:**

        ```csharp
        // "Đếm" "tổng số lượng" sản phẩm trong bảng SanPhams
        int tongSoSanPham = dbContext.SanPhams.Count(); // "Đếm" "toàn bộ" bản ghi trong bảng

        // "Đếm" "số lượng" sản phẩm có "danh mục" là "Điện tử"
        int soSanPhamDienTu = dbContext.SanPhams.Count(sp => sp.DanhMucSanPham == "Điện tử"); // "Đếm" có "điều kiện" "lọc"
        ```

    -   **`Sum()` - "Tính tổng" giá trị số:**

        ```csharp
        // "Tính tổng" "giá" của "tất cả" sản phẩm
        decimal tongGiaSanPham = dbContext.SanPhams.Sum(sp => sp.Gia); // "Tính tổng" cột "Gia"

        // "Tính tổng" "giá" của các sản phẩm có "danh mục" là "Sách"
        decimal tongGiaSanPhamSach = dbContext.SanPhams.Where(sp => sp.DanhMucSanPham == "Sách").Sum(sp => sp.Gia); // "Tính tổng" có "điều kiện" "lọc"
        ```

    -   **`Average()` - "Tính trung bình" giá trị số:**

        ```csharp
        // "Tính trung bình" "giá" của "tất cả" sản phẩm
        double trungBinhGiaSanPham = dbContext.SanPhams.Average(sp => sp.Gia); // "Tính trung bình" cột "Gia"
        ```

    -   **`Min()` - "Tìm giá trị nhỏ nhất":**

        ```csharp
        // "Tìm" "giá" sản phẩm "nhỏ nhất"
        decimal giaSanPhamNhoNhat = dbContext.SanPhams.Min(sp => sp.Gia); // "Tìm" giá trị "nhỏ nhất" của cột "Gia"
        ```

    -   **`Max()` - "Tìm giá trị lớn nhất":**

        ```csharp
        // "Tìm" "giá" sản phẩm "lớn nhất"
        decimal giaSanPhamLonNhat = dbContext.SanPhams.Max(sp => sp.Gia); // "Tìm" giá trị "lớn nhất" của cột "Gia"
        ```

-   **"Lưu ý quan trọng" về Aggregation và hiệu năng:**

    -   Khi bạn "dùng" các "chiêu" tổng hợp (Count, Sum, Average, Min, Max) trong LINQ queries với EF Core, EF Core sẽ **"dịch"** các "chiêu" này thành các câu lệnh **SQL Aggregation Functions** (ví dụ: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`) và "thực thi" chúng **"trực tiếp" "trên database server"**.
    -   Điều này giúp "tối ưu" "hiệu năng" "vượt trội", vì database server được "tận dụng" để "tính toán" "tổng hợp" dữ liệu, và ứng dụng của bạn chỉ "nhận" về **"kết quả" "cuối cùng"** (một con số duy nhất), "không cần" "tải" "toàn bộ" dữ liệu về "xử lý" trên client-side.

**7.4. Raw SQL Queries (Truy Vấn SQL "Thô") - "Chiêu" "Can Thiệp" Sâu Hơn Vào SQL - "Vượt Qua" "Giới Hạn" LINQ Khi Cần**

-   **"Vấn đề": LINQ "Không Đủ Sức Mạnh" Cho Một Số Truy Vấn "Phức Tạp" - "Cần 'Vũ Khí' Mạnh Hơn":**

    -   Mặc dù LINQ và EF Core cung cấp rất nhiều "chiêu thức" "truy vấn" "mạnh mẽ", nhưng đôi khi bạn có thể gặp các "tình huống" "đặc biệt" mà LINQ queries **"không thể"** hoặc **"khó"** "diễn đạt" được một cách "hiệu quả". Ví dụ:
        -   "Gọi" stored procedures (thủ tục lưu trữ) trong database.
        -   "Thực hiện" các truy vấn SQL "phức tạp" "đặc thù" của từng hệ quản trị cơ sở dữ liệu (DBMS-specific SQL).
        -   "Tối ưu hóa" hiệu năng truy vấn bằng cách viết SQL "tay" (tuning SQL queries).

-   **Raw SQL Queries - "Chiêu" "Triệu Hồi" SQL "Thô" - "Vượt Qua" "Giới Hạn" LINQ:**

    -   **Raw SQL Queries** (trong EF Core) "cho phép" bạn **"viết" và "thực thi" các câu lệnh SQL "thô"** (raw SQL) **"trực tiếp"** trên database, **"vượt qua"** các "giới hạn" của LINQ khi cần thiết.
    -   Raw SQL Queries "trao tay" cho bạn **"quyền kiểm soát" "tối đa"** đối với câu lệnh SQL được "gửi" đến database.

-   **"Các 'chiêu' Raw SQL Queries" phổ biến trong EF Core:**

    -   **`FromSqlRaw()` - "Truy vấn" dữ liệu bằng SQL "thô" và "trả về" Entities:**

        ```csharp
        // "Truy vấn" sản phẩm bằng SQL "thô" (ví dụ: "lấy" sản phẩm có "giá" > @gia - tham số hóa để "tránh" SQL injection)
        var sanPham_GiaHon_500_RawSQL = dbContext.SanPhams
                                                .FromSqlRaw("SELECT * FROM SanPhams WHERE Gia > {0}", 500) // "Viết" SQL "thô" và "truyền" tham số
                                                .ToList(); // Kết quả "trả về" vẫn là List<SanPham> (Entities)

        Console.WriteLine("\n--- Sản phẩm giá > 500 (Raw SQL) ---");
        foreach (var sp in sanPham_GiaHon_500_RawSQL) // Duyệt qua kết quả
        {
            Console.WriteLine($"- {sp.TenSanPham}, Giá: {sp.Gia:#,##0}");
        }
        ```

    -   **`SqlQueryRaw()` - "Truy vấn" dữ liệu bằng SQL "thô" và "trả về" "kiểu dữ liệu tùy chỉnh":**

        ```csharp
        // "Truy vấn" "tên sản phẩm" và "giá" bằng SQL "thô" và "trả về" "kiểu dữ liệu vô danh"
        var sanPham_Ten_Gia_RawSQL = dbContext.Database.SqlQueryRaw<dynamic>( // "Dùng" SqlQueryRaw<dynamic> để "trả về" "kiểu động" (dynamic)
            "SELECT TenSanPham AS Ten, Gia FROM SanPhams WHERE DanhMucSanPham = {0}", "Điện tử" // "Viết" SQL "thô" và "truyền" tham số
        );

        Console.WriteLine("\n--- Sản phẩm danh mục 'Điện tử' (Raw SQL, chỉ tên và giá) ---");
        foreach (var item in sanPham_Ten_Gia_RawSQL) // Duyệt qua kết quả "kiểu động"
        {
            Console.WriteLine($"- Tên: {item.Ten}, Giá: {item.Gia}"); // "Truy cập" properties "Ten" và "Gia" (dynamic)
        }
        ```

    -   **`ExecuteSqlRaw()` và `ExecuteSqlInterpolated()` - "Thực thi" các lệnh SQL "không trả về kết quả" (NonQuery):**

        ```csharp
        // "Thực thi" lệnh SQL "thô" để "cập nhật" "giá" sản phẩm (ExecuteSqlRaw)
        int rowsAffected = dbContext.Database.ExecuteSqlRaw(
            "UPDATE SanPhams SET Gia = Gia * 1.1 WHERE DanhMucSanPham = {0}", "Điện tử" // "Viết" SQL "thô" và "truyền" tham số
        );
        Console.WriteLine($"\nĐã cập nhật giá sản phẩm 'Điện tử', số dòng ảnh hưởng: {rowsAffected}"); // In ra "số dòng" bị ảnh hưởng

        // "Thực thi" lệnh SQL "thô" để "xóa" sản phẩm có "giá" < 100 (ExecuteSqlInterpolated - "an toàn" hơn với string interpolation)
        int rowsDeleted = dbContext.Database.ExecuteSqlInterpolated($"DELETE FROM SanPhams WHERE Gia < {100}"); // "Viết" SQL "thô" dùng string interpolation (an toàn hơn)
        Console.WriteLine($"Đã xóa sản phẩm giá rẻ, số dòng bị xóa: {rowsDeleted}"); // In ra "số dòng" bị xóa
        ```

-   **"Lưu ý quan trọng" khi dùng Raw SQL Queries:**

    -   **"Cẩn thận" với SQL Injection:** Khi "viết" SQL "thô", bạn phải **"tự" "đảm bảo"** "an toàn" trước các "tấn công" SQL injection bằng cách **"tham số hóa"** các giá trị đầu vào từ người dùng (ví dụ: dùng parameterized queries như trong ví dụ trên).
    -   **"Mất" "khả năng" "di động" giữa các DBMS:** Raw SQL Queries thường "phụ thuộc" vào "ngôn ngữ SQL" "đặc thù" của từng hệ quản trị cơ sở dữ liệu (DBMS-specific SQL). Nếu bạn "dùng" Raw SQL Queries "quá nhiều", ứng dụng của bạn có thể trở nên "khó" "chuyển đổi" sang DBMS khác sau này.
    -   **"Hạn chế" dùng Raw SQL Queries khi không "thực sự cần thiết":** "Ưu tiên" dùng LINQ queries và các "chiêu" EF Core "xịn sò" khác khi có thể. Chỉ "dùng" Raw SQL Queries khi LINQ "bó tay" hoặc khi bạn cần "tối ưu" "hiệu năng" truy vấn "đặc biệt".

**Tổng Kết Chương 6:**

-   Bạn đã "nâng cấp" "kỹ năng" truy vấn LINQ lên một "tầm cao mới" với các "chiêu thức" "cao cấp":
    -   Projections ("chọn lọc cột") - "gọn nhẹ" hóa truy vấn.
    -   Filtering ("lọc nâng cao") - "tìm đúng" "món đồ" "cần".
    -   Aggregation ("tổng hợp") - "tính toán" "ngay trên database" - "tối ưu hiệu năng".
    -   Raw SQL Queries ("truy vấn SQL thô") - "vượt qua" "giới hạn" LINQ khi cần - "vũ khí" "cuối cùng" khi "bí".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: Tối Ưu Hiệu Năng EF Core - "Chạy Nhanh Như Chớp" Với Database**. Chúng ta sẽ "khám phá" các "bí quyết" và "chiến lược" để "tăng tốc" ứng dụng EF Core của bạn, giúp ứng dụng "chạy nhanh", "mượt mà", và "tiết kiệm" tài nguyên.

Bạn có câu hỏi nào về "truy vấn nâng cao" với LINQ này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng bạn" "trở thành" "cao thủ" EF Core.

