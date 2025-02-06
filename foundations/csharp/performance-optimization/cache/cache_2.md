# Chương 2: Caching "Ngay Trong Bộ Nhớ" (In-Memory Caching) Với .NET - "Chiếc 'Bình Nước' Cá Nhân" "Tiện Lợi" Của .NET - "Cache 'Tốc Độ Ánh Sáng' Ngay Trong Ứng Dụng"

Chào mừng bạn đến với **Chương 2: Caching "Ngay Trong Bộ Nhớ" (In-Memory Caching) Với .NET**! Trong chương này, chúng ta sẽ "đi sâu" vào **In-Memory Caching**, "loại hình" caching **"đơn giản"**, **"nhanh chóng"**, và **"dễ sử dụng"** nhất. Chúng ta sẽ "khám phá" **`MemoryCache`**, "công cụ" "caching" "có sẵn" trong .NET, và "học cách" "vận dụng" nó để "tăng tốc" ứng dụng của bạn.

**Phần 2: Caching "Ngay Trong Bộ Nhớ" (In-Memory Caching) Với .NET - "Chiếc 'Bình Nước' Cá Nhân"**

**2.1. `MemoryCache` - "Chiếc 'Bình Nước' Cá Nhân" "Tiện Lợi" Của .NET - "Cache 'Tức Thì' Không Cần 'Đi Xa' "**

-   **`MemoryCache` là gì?**

    -   **`MemoryCache`** là một class trong .NET Framework và .NET Core (namespace `System.Runtime.Caching`) cung cấp một "cơ chế" **In-Memory Caching** "đơn giản" và "hiệu quả".
    -   Hãy tưởng tượng `MemoryCache` như một **"chiếc 'bình nước' cá nhân"** mà bạn có thể "đặt ngay cạnh bàn làm việc" của ứng dụng. Bạn có thể "lưu trữ" dữ liệu (ví dụ: "nước") vào "bình" (cache) và "lấy ra" (uống) khi cần, rất "nhanh chóng" và "tiện lợi".
    -   `MemoryCache` "lưu trữ" dữ liệu cache **"ngay trong bộ nhớ"** (RAM) của ứng dụng. Điều này giúp "truy cập" dữ liệu cache **"siêu nhanh"**, vì "truy cập" bộ nhớ RAM là một trong những thao tác "nhanh nhất" trong máy tính.
    -   `MemoryCache` "tự động" "quản lý" bộ nhớ cache, "loại bỏ" dữ liệu cache "hết hạn" (expired) hoặc "ít được sử dụng" (least recently used - LRU) khi bộ nhớ "đầy".

-   **"Ưu điểm" của `MemoryCache`:**

    -   **"Tốc độ 'siêu nhanh' ":** Truy cập dữ liệu cache từ `MemoryCache` cực kỳ nhanh, vì dữ liệu nằm "ngay trong bộ nhớ" ứng dụng.
    -   **"Đơn giản" và "dễ sử dụng":** API của `MemoryCache` rất "trực quan" và "dễ học". Bạn có thể "bắt đầu" "sử dụng" `MemoryCache` trong ứng dụng của mình một cách "nhanh chóng".
    -   **"Có sẵn" trong .NET:** `MemoryCache` là một phần của .NET Framework và .NET Core, bạn không cần "cài đặt" thêm bất kỳ thư viện bên ngoài nào.
    -   **"Tự động quản lý bộ nhớ":** `MemoryCache` "tự động" "lo liệu" việc "quản lý" bộ nhớ cache, giúp bạn "tập trung" vào "logic" ứng dụng chính.
    -   **"Hỗ trợ" "nhiều tính năng" "hay ho":** `MemoryCache` cung cấp nhiều tính năng "nâng cao" như cache expiration, cache dependencies, cache eviction policies, v.v. (chúng ta sẽ "khám phá" ở các phần sau).

-   **"Nhược điểm" của `MemoryCache`:**

    -   **"Phạm vi 'giới hạn' ":** Dữ liệu cache trong `MemoryCache` chỉ được "lưu trữ" trong **"bộ nhớ"** của **"một phiên bản"** ứng dụng (instance) hoặc **"một máy chủ"** duy nhất. Nếu bạn có nhiều "phiên bản" ứng dụng (ví dụ: ứng dụng web chạy trên nhiều web server), dữ liệu cache **"không được chia sẻ"** giữa các "phiên bản" này.
    -   **"Dữ liệu cache 'mất đi' khi ứng dụng 'khởi động lại' ":** Khi ứng dụng "khởi động lại" hoặc "máy chủ" "restart", dữ liệu cache trong `MemoryCache` sẽ **"bị mất"** (vì dữ liệu nằm trong bộ nhớ RAM, bộ nhớ RAM là "volatile").
    -   **"Giới hạn" về "dung lượng bộ nhớ":** Dung lượng cache của `MemoryCache` bị "giới hạn" bởi **"dung lượng bộ nhớ RAM"** có sẵn của máy chủ. Nếu bạn cache quá nhiều dữ liệu, có thể "gây ra" "vấn đề" về bộ nhớ (ví dụ: `OutOfMemoryException`).

**2.2. "Thao Tác" "Cơ Bản" Với `MemoryCache` ("Thêm", "Lấy", "Sửa", "Xóa" Dữ Liệu Cache) - "Làm Quen" Với "Chiếc 'Bình Nước' Cá Nhân"**

-   **"Mở 'chiếc bình nước' " `MemoryCache`:**

    -   Để "sử dụng" `MemoryCache`, bạn cần "tạo" một instance của class `MemoryCache`. Bạn có thể "tạo" một instance "duy nhất" và "dùng chung" trong toàn ứng dụng (singleton pattern), hoặc "tạo" instance "mỗi khi cần" (tùy theo "thiết kế" ứng dụng của bạn).

    ```csharp
    // "Tạo" một instance của MemoryCache (dùng tên "mặc định" - Default)
    MemoryCache memoryCache = MemoryCache.Default;
    ```

-   **"Thêm" dữ liệu vào cache (Add):**

    -   "Chiêu" `Add(key, value, policy)` dùng để "thêm" một cặp **"khóa-giá trị"** (key-value pair) vào cache.
        -   `key`: "Khóa" (string) để "định danh" dữ liệu cache (giống như "tên nhãn" trên "bình nước").
        -   `value`: "Giá trị" (object) dữ liệu cache (giống như "nước" trong "bình nước").
        -   `policy`: `CacheItemPolicy` object để "cấu hình" các "tùy chọn" cache (ví dụ: expiration, dependencies - chúng ta sẽ nói ở phần sau). Nếu không cần "tùy chọn" gì "đặc biệt", bạn có thể "truyền" `null`.

    ```csharp
    // Dữ liệu sản phẩm (ví dụ)
    var sanPham = new { Id = 1, Ten = "Chuột không dây", Gia = 250000 };

    // "Khóa" cache (ví dụ)
    string cacheKey_SanPham_1 = "SanPham_1";

    // "Thêm" dữ liệu sản phẩm vào cache với "khóa" "SanPham_1" (không có "tùy chọn" đặc biệt)
    memoryCache.Add(cacheKey_SanPham_1, sanPham, null);

    Console.WriteLine($"Đã thêm sản phẩm vào cache với khóa: {cacheKey_SanPham_1}");
    ```

-   **"Lấy" dữ liệu từ cache (Get):**

    -   "Chiêu" `Get(key)` dùng để "lấy" dữ liệu cache theo "khóa".
        -   `key`: "Khóa" (string) của dữ liệu cache bạn muốn "lấy".
        -   "Trả về": "Giá trị" (object) dữ liệu cache nếu "tìm thấy" trong cache (cache hit). "Trả về" `null` nếu "không tìm thấy" (cache miss).

    ```csharp
    // "Khóa" cache muốn "lấy" (ví dụ)
    string cacheKey_SanPham_1_Get = "SanPham_1";

    // "Lấy" dữ liệu sản phẩm từ cache theo "khóa" "SanPham_1"
    var sanPham_Cached = memoryCache.Get(cacheKey_SanPham_1_Get);

    if (sanPham_Cached != null) // "Kiểm tra" xem có "tìm" thấy dữ liệu trong cache không (cache hit)
    {
        Console.WriteLine($"Cache hit! Lấy sản phẩm từ cache: {((dynamic)sanPham_Cached).Ten}"); // "Ép kiểu" dynamic để "truy cập" property "Ten" (ví dụ)
    }
    else // "Không tìm thấy" trong cache (cache miss)
    {
        Console.WriteLine("Cache miss! Không tìm thấy sản phẩm trong cache.");
        // (Code để "lấy" dữ liệu từ "nguồn gốc" - ví dụ: database - và "thêm" vào cache - xem phần sau)
    }
    ```

-   **"Kiểm tra" dữ liệu có tồn tại trong cache (Contains):**

    -   "Chiêu" `Contains(key)` dùng để "kiểm tra" xem một "khóa" có "tồn tại" trong cache hay không.
        -   `key`: "Khóa" (string) bạn muốn "kiểm tra".
        -   "Trả về": `true` nếu "khóa" "tồn tại" trong cache, `false` nếu "không tồn tại".

    ```csharp
    // "Khóa" cache muốn "kiểm tra" (ví dụ)
    string cacheKey_SanPham_1_Check = "SanPham_1";

    // "Kiểm tra" xem "khóa" "SanPham_1" có "tồn tại" trong cache không
    bool isCached = memoryCache.Contains(cacheKey_SanPham_1_Check);

    if (isCached)
    {
        Console.WriteLine($"Khóa '{cacheKey_SanPham_1_Check}' có tồn tại trong cache.");
    }
    else
    {
        Console.WriteLine($"Khóa '{cacheKey_SanPham_1_Check}' không tồn tại trong cache.");
    }
    ```

-   **"Xóa" dữ liệu khỏi cache (Remove):**

    -   "Chiêu" `Remove(key)` dùng để "xóa" dữ liệu cache theo "khóa".
        -   `key`: "Khóa" (string) của dữ liệu cache bạn muốn "xóa".
        -   "Trả về": "Giá trị" (object) dữ liệu cache đã bị "xóa" (nếu có). "Trả về" `null` nếu "khóa" "không tồn tại" trong cache.

    ```csharp
    // "Khóa" cache muốn "xóa" (ví dụ)
    string cacheKey_SanPham_1_Remove = "SanPham_1";

    // "Xóa" dữ liệu sản phẩm khỏi cache theo "khóa" "SanPham_1"
    var sanPham_Removed = memoryCache.Remove(cacheKey_SanPham_1_Remove);

    if (sanPham_Removed != null) // "Kiểm tra" xem có dữ liệu nào bị "xóa" không
    {
        Console.WriteLine($"Đã xóa sản phẩm khỏi cache với khóa: {cacheKey_SanPham_1_Remove}, Tên: {((dynamic)sanPham_Removed).Ten}"); // "Ép kiểu" dynamic để "truy cập" property "Ten" (ví dụ)
    }
    else
    {
        Console.WriteLine($"Không tìm thấy khóa '{cacheKey_SanPham_1_Remove}' trong cache để xóa."); // Thông báo nếu không tìm thấy khóa để xóa
    }
    ```

-   **"Sửa" dữ liệu trong cache (Set):**

    -   `MemoryCache` **"không có" "chiêu" "sửa" trực tiếp** (Update). Để "sửa" dữ liệu cache, bạn cần "dùng" "chiêu" **`Set(key, value, policy)`**.
        -   `Set(key, value, policy)` có thể "vừa" "thêm" dữ liệu mới vào cache (nếu "khóa" chưa tồn tại), **"vừa" "thay thế" dữ liệu đã có** trong cache (nếu "khóa" đã tồn tại).
        -   "Về mặt 'logic' ", `Set` có thể được xem như là "sửa" dữ liệu cache.

    ```csharp
    // "Khóa" cache muốn "sửa" (ví dụ)
    string cacheKey_SanPham_1_Set = "SanPham_1";

    // "Lấy" dữ liệu sản phẩm từ cache (giả sử đã có trong cache)
    var sanPham_Cached_Set = memoryCache.Get(cacheKey_SanPham_1_Set);

    if (sanPham_Cached_Set != null) // "Kiểm tra" xem có "tìm" thấy dữ liệu trong cache không
    {
        // "Sửa" "giá" sản phẩm (ví dụ)
        ((dynamic)sanPham_Cached_Set).Gia = 300000;

        // "Set" lại dữ liệu đã "sửa" vào cache (thay thế dữ liệu cũ)
        memoryCache.Set(cacheKey_SanPham_1_Set, sanPham_Cached_Set, null); // "Dùng" Set để "sửa" (thay thế) dữ liệu cache

        Console.WriteLine($"Đã sửa giá sản phẩm trong cache với khóa: {cacheKey_SanPham_1_Set}, Giá mới: {((dynamic)sanPham_Cached_Set).Gia}"); // Thông báo "sửa thành công"
    }
    else
    {
        Console.WriteLine($"Không tìm thấy khóa '{cacheKey_SanPham_1_Set}' trong cache để sửa."); // Thông báo nếu không tìm thấy khóa để sửa
    }
    ```

**2.3. "Định Đoạt" "Tuổi Thọ" Dữ Liệu Cache (Cache Expiration - Absolute, Sliding) - "Giữ Dữ Liệu 'Tươi Mới' "**

-   **"Vấn đề": Dữ Liệu Cache "Lỗi Thời" - "Thông Tin 'Cũ Rích' Gây 'Hại' ":**

    -   Dữ liệu trong database có thể **"thay đổi"** theo thời gian (ví dụ: giá sản phẩm thay đổi, thông tin khách hàng được cập nhật, v.v.).
    -   Nếu dữ liệu cache **"không được 'làm mới' "** (refresh) "kịp thời", dữ liệu cache có thể trở nên **"lỗi thời"** (outdated) so với dữ liệu "gốc" trong database.
    -   "Dùng" dữ liệu cache "lỗi thời" có thể "gây ra" **"sai sót"** trong ứng dụng, "hiển thị" thông tin "không chính xác" cho người dùng, và "ảnh hưởng" đến "uy tín" của ứng dụng.

-   **Cache Expiration - "Giải Pháp" "Giữ Dữ Liệu 'Tươi Mới' " - "Định 'Hạn Sử Dụng' Cho 'Bình Nước' ":**

    -   **Cache Expiration** (hết hạn cache) là một "cơ chế" cho phép bạn **"định nghĩa" "thời gian 'tồn tại' "** (time-to-live - TTL) của dữ liệu cache trong `MemoryCache`. Khi dữ liệu cache "hết hạn", `MemoryCache` sẽ **"tự động" "loại bỏ"** (evict) dữ liệu đó khỏi cache.
    -   Cache Expiration giúp **"đảm bảo"** dữ liệu cache **"không bị 'quá cũ' "** và "luôn" **"tương đối 'tươi mới' "** so với dữ liệu "gốc".

-   **Các loại Cache Expiration phổ biến trong `MemoryCache`:**

    -   **Absolute Expiration (Hết Hạn Tuyệt Đối):**

        -   Dữ liệu cache sẽ "hết hạn" vào một **"thời điểm 'cố định' "** (absolute time) trong tương lai.
        -   Ví dụ: "Dữ liệu cache này sẽ hết hạn vào lúc 12:00 trưa ngày mai".
        -   "Phù hợp" với dữ liệu cache có "thời gian 'tươi mới' " "xác định" (ví dụ: dữ liệu chỉ "có giá trị" trong một "khoảng thời gian" nhất định).

        ```csharp
        // Dữ liệu sản phẩm (ví dụ)
        var sanPham_AbsoluteExp = new { Id = 2, Ten = "Bàn phím cơ", Gia = 1500000 };
        string cacheKey_SanPham_2_AbsoluteExp = "SanPham_2_AbsoluteExp";

        // "Cấu hình" CacheItemPolicy cho Absolute Expiration
        CacheItemPolicy policy_AbsoluteExp = new CacheItemPolicy();
        policy_AbsoluteExp.AbsoluteExpiration = DateTimeOffset.Now.AddSeconds(30); // "Đặt" thời gian "hết hạn tuyệt đối" là 30 giây sau thời điểm hiện tại

        // "Thêm" dữ liệu vào cache với CacheItemPolicy đã cấu hình
        memoryCache.Add(cacheKey_SanPham_2_AbsoluteExp, sanPham_AbsoluteExp, policy_AbsoluteExp);

        Console.WriteLine($"Đã thêm sản phẩm vào cache với khóa: {cacheKey_SanPham_2_AbsoluteExp}, Absolute Expiration: 30 giây");

        // (Sau 30 giây, dữ liệu cache "SanPham_2_AbsoluteExp" sẽ "tự động" bị "xóa" khỏi cache)
        ```

    -   **Sliding Expiration (Hết Hạn Trượt):**

        -   Dữ liệu cache sẽ "hết hạn" sau một **"khoảng thời gian 'nhất định' "** kể từ lần **"truy cập" "cuối cùng"** (last access time).
        -   Ví dụ: "Dữ liệu cache này sẽ hết hạn sau 10 phút kể từ lần cuối cùng được 'lấy' ra khỏi cache".
        -   "Phù hợp" với dữ liệu cache "ít được 'truy cập' " thường xuyên. Nếu dữ liệu cache được "truy cập" "thường xuyên", thời gian "hết hạn" sẽ được **"gia hạn"** (slide) mỗi lần "truy cập".

        ```csharp
        // Dữ liệu sản phẩm (ví dụ)
        var sanPham_SlidingExp = new { Id = 3, Ten = "Màn hình LCD", Gia = 3500000 };
        string cacheKey_SanPham_3_SlidingExp = "SanPham_3_SlidingExp";

        // "Cấu hình" CacheItemPolicy cho Sliding Expiration
        CacheItemPolicy policy_SlidingExp = new CacheItemPolicy();
        policy_SlidingExp.SlidingExpiration = TimeSpan.FromSeconds(15); // "Đặt" thời gian "hết hạn trượt" là 15 giây

        // "Thêm" dữ liệu vào cache với CacheItemPolicy đã cấu hình
        memoryCache.Add(cacheKey_SanPham_3_SlidingExp, sanPham_SlidingExp, policy_SlidingExp);

        Console.WriteLine($"Đã thêm sản phẩm vào cache với khóa: {cacheKey_SanPham_3_SlidingExp}, Sliding Expiration: 15 giây");

        // (Nếu bạn "truy cập" dữ liệu cache "SanPham_3_SlidingExp" "trước" khi 15 giây trôi qua, thời gian "hết hạn" sẽ được "reset" và "đếm lại" từ đầu 15 giây)
        ```

-   **"Chọn" loại Expiration nào? - "Tùy theo 'độ 'tươi' " mong muốn của dữ liệu":**

    -   **Absolute Expiration:** "Chính xác" về thời gian "hết hạn", "phù hợp" khi bạn "biết rõ" dữ liệu cache "có giá trị" trong "khoảng thời gian" nào.
    -   **Sliding Expiration:** "Tiết kiệm" bộ nhớ cache hơn (vì dữ liệu "ít dùng" sẽ bị "xóa" sớm), "phù hợp" khi bạn muốn "giữ" dữ liệu cache "lâu hơn" nếu nó được "truy cập" "thường xuyên".
    -   Bạn có thể **"kết hợp"** cả Absolute Expiration và Sliding Expiration trong một `CacheItemPolicy` để "kiểm soát" "tuổi thọ" dữ liệu cache một cách "linh hoạt" nhất.

**2.4. "Phụ Thuộc" Cache (Cache Dependencies) - "Cache 'Thông Minh' Tự Động 'Làm Mới' " - "Cache 'Biết Nghe Lời' Dữ Liệu Gốc"**

-   **"Vấn đề": Cache Expiration "Chưa Đủ" - "Cần Cache 'Nhạy Bén' Với Thay Đổi Dữ Liệu Gốc":**

    -   Cache Expiration (Absolute, Sliding) giúp "giữ" dữ liệu cache "tươi mới" ở một mức độ nhất định.
    -   Tuy nhiên, Cache Expiration chỉ "dựa vào" **"thời gian"** để "xác định" khi nào dữ liệu cache "hết hạn". Nó **"không 'nhận biết' "** được khi nào **"dữ liệu 'gốc' (ví dụ: trong database) "thay đổi"**.
    -   Nếu dữ liệu "gốc" "thay đổi" **"trước"** khi dữ liệu cache "hết hạn", dữ liệu cache vẫn có thể trở nên **"lỗi thời"**, dù chưa đến "thời điểm" "hết hạn".

-   **Cache Dependencies - "Giải Pháp" "Cache 'Thông Minh' Tự 'Làm Mới' " - "Cache 'Lắng Nghe' 'Tiếng Nói' Dữ Liệu Gốc":**

    -   **Cache Dependencies** (phụ thuộc cache) là một "cơ chế" cho phép bạn **"thiết lập" "mối 'quan hệ' 'phụ thuộc' "** giữa dữ liệu cache và một **"nguồn dữ liệu 'gốc' "** (ví dụ: file, database, một cache item khác, v.v.).
    -   Khi "nguồn dữ liệu 'gốc' " **"thay đổi"**, `MemoryCache` sẽ **"tự động" "vô hiệu hóa"** (invalidate) dữ liệu cache "phụ thuộc" vào "nguồn dữ liệu" đó, và "xóa" dữ liệu cache khỏi cache.
    -   Cache Dependencies giúp **"đảm bảo"** dữ liệu cache **"luôn 'đồng bộ' "** với dữ liệu "gốc" và **"tự động 'làm mới' "** khi dữ liệu "gốc" "thay đổi", "không cần" phải "chờ" đến khi cache "hết hạn" theo thời gian.

-   **Các loại Cache Dependencies phổ biến trong `MemoryCache`:**

    -   **FileDependency (Phụ Thuộc File):**

        -   Dữ liệu cache "phụ thuộc" vào **"sự thay đổi"** của một hoặc nhiều **"file"**.
        -   Khi bất kỳ file nào trong danh sách "file phụ thuộc" bị **"thay đổi"** (ví dụ: "nội dung" file bị "sửa", file bị "xóa", file bị "đổi tên", v.v.), dữ liệu cache sẽ bị "vô hiệu hóa".
        -   "Phù hợp" với dữ liệu cache "dựa trên" nội dung của file cấu hình, file dữ liệu tĩnh, v.v.

        ```csharp
        // Dữ liệu cấu hình (ví dụ) - giả sử đọc từ file "config.txt"
        string configData = "AppSettings: { 'Theme': 'Dark', 'Language': 'vi-VN' }";
        string cacheKey_Config = "AppConfig";
        string configFilePath = "config.txt"; // "Đường dẫn" đến file cấu hình (ví dụ)

        // "Ghi" dữ liệu cấu hình vào file (ví dụ)
        File.WriteAllText(configFilePath, configData);

        // "Cấu hình" CacheItemPolicy với FileDependency
        CacheItemPolicy policy_FileDependency = new CacheItemPolicy();
        policy_FileDependency.SlidingExpiration = TimeSpan.FromMinutes(10); // Vẫn có Sliding Expiration (ví dụ)
        policy_FileDependency.ChangeMonitors.Add(new HostFileChangeMonitor(new List<string>() { configFilePath })); // "Thêm" FileDependency - "phụ thuộc" vào file "config.txt"

        // "Thêm" dữ liệu cấu hình vào cache với CacheItemPolicy đã cấu hình
        memoryCache.Add(cacheKey_Config, configData, policy_FileDependency);

        Console.WriteLine($"Đã thêm cấu hình vào cache với khóa: {cacheKey_Config}, File Dependency: {configFilePath}");

        // (Nếu bạn "sửa" file "config.txt", dữ liệu cache "AppConfig" sẽ "tự động" bị "xóa" khỏi cache)
        ```

    -   **CacheDependency (Phụ Thuộc Cache Item):**

        -   Dữ liệu cache "phụ thuộc" vào **"sự thay đổi"** của một **"cache item khác"** trong cùng `MemoryCache`.
        -   Khi cache item "phụ thuộc" bị **"xóa"** hoặc "hết hạn", dữ liệu cache "phụ thuộc" cũng sẽ bị "vô hiệu hóa".
        -   "Phù hợp" để "xây dựng" các "mối 'quan hệ' " "phụ thuộc" giữa các dữ liệu cache khác nhau.

        (Ví dụ về `CacheDependency` sẽ phức tạp hơn và ít phổ biến hơn `FileDependency`, nên có thể bỏ qua trong tài liệu "dành cho người mới bắt đầu" này. Nếu người dùng có nhu cầu, có thể bổ sung sau).

**Tổng Kết Chương 2:**

-   Bạn đã "làm quen" với **`MemoryCache`**, "chiếc 'bình nước cá nhân' " "tiện lợi" của .NET, và "học cách" "sử dụng" nó để "caching" dữ liệu "ngay trong bộ nhớ" ứng dụng.
    -   "Hiểu" **`MemoryCache` là gì**, "ưu điểm", và "nhược điểm" của nó.
    -   "Nắm vững" các "thao tác" "cơ bản" với `MemoryCache` ("thêm", "lấy", "sửa", "xóa" dữ liệu cache).
    -   Biết cách "định đoạt" "tuổi thọ" dữ liệu cache bằng **Cache Expiration** (Absolute, Sliding) để "giữ" dữ liệu cache "tươi mới".
    -   "Khám phá" **Cache Dependencies** (ví dụ: `FileDependency`) để "cache 'thông minh' tự động 'làm mới' " khi dữ liệu "gốc" "thay đổi".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 3: Caching "Phân Tán" (Distributed Caching) - "Chiếc 'Bể Nước' Công Cộng" "Mạnh Mẽ"**. Chúng ta sẽ "khám phá" khi nào cần "dùng" Distributed Caching (khi In-Memory Caching "không đủ"), và "làm quen" với các "nhà cung cấp" Distributed Cache "nổi tiếng" như **Redis** và **Memcached**.

Bạn có câu hỏi nào về In-Memory Caching với `MemoryCache` này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" Caching.
