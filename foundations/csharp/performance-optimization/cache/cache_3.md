# Chương 3: Caching "Phân Tán" (Distributed Caching) - "Chiếc 'Bể Nước' Công Cộng" "Mạnh Mẽ" - "Cache 'Quy Mô Lớn' Cho Ứng Dụng 'Phân Tán' "

Chào mừng bạn đến với **Chương 3: Caching "Phân Tán" (Distributed Caching)**! Trong chương này, chúng ta sẽ "vượt ra
khỏi" "giới hạn" của In-Memory Caching và "khám phá" **Distributed Caching**, "giải pháp" caching **"mạnh mẽ"** và **"mở
rộng"** hơn, "phù hợp" với các ứng dụng **"quy mô lớn"** và **"phân tán"**. Chúng ta sẽ "làm quen" với **Redis** và *
*Memcached**, hai "người khổng lồ" trong thế giới Distributed Caching.

**Phần 3: Caching "Phân Tán" (Distributed Caching) - "Chiếc 'Bể Nước' Công Cộng"**

**3.1. Caching "Phân Tán" Là Gì? (Khi "Một 'Bình Nước' Không Đủ") - "Cache 'Chia Sẻ' Cho 'Hệ Thống Lớn' "**

- **"Khi nào 'Chiếc 'Bình Nước' Cá Nhân' " `MemoryCache` "Không Còn Đủ Dùng"?**

    - Như chúng ta đã "thảo luận" ở Chương 2, `MemoryCache` rất "tuyệt vời" cho **"ứng dụng 'đơn giản' "** hoặc **"ứng
      dụng chạy trên 'một máy chủ' duy nhất"**.
    - Tuy nhiên, trong thế giới ứng dụng **"hiện đại"** và **"quy mô lớn"**, ứng dụng thường được **"phân tán"** trên *
      *"nhiều máy chủ"** (ví dụ: ứng dụng web chạy trên nhiều web server, ứng dụng microservices).
    - Trong môi trường "phân tán" này, `MemoryCache` **"bộc lộ 'hạn chế' "**:
        - **"Dữ liệu cache 'không được chia sẻ' ":** Mỗi "phiên bản" ứng dụng (instance) hoặc "máy chủ" có "riêng" một
          `MemoryCache`. Dữ liệu cache **"không được 'đồng bộ hóa' "** và **"chia sẻ"** giữa các "phiên bản" ứng dụng.
          Điều này có thể dẫn đến **"tính không nhất quán"** của dữ liệu cache trong toàn hệ thống.
        - **"Khó 'mở rộng' ":** Dung lượng cache bị "giới hạn" bởi "bộ nhớ RAM" của **"từng máy chủ"**. "Khó" "mở rộng"
          dung lượng cache khi "lượng dữ liệu" cache "tăng lên" hoặc "lưu lượng truy cập" "tăng cao".

- **Caching "Phân Tán" (Distributed Caching) - "Giải Pháp" "Cache 'Chia Sẻ' " "Mạnh Mẽ" và "Mở Rộng":**

    - **Distributed Caching** (caching phân tán) là một "giải pháp" caching **"thiết kế"** để "giải quyết" các "hạn chế"
      của In-Memory Caching trong môi trường "phân tán".
    - Hãy tưởng tượng Distributed Caching như một **"chiếc 'bể nước' công cộng"** "lớn" và "mạnh mẽ", được **"chia sẻ"**
      bởi **"tất cả"** các "phiên bản" ứng dụng và các "máy chủ" trong hệ thống.
    - **"Đặc điểm" "chính" của Distributed Caching:**
        - **"Lưu trữ" cache ở "ngoài ứng dụng":** Dữ liệu cache được "lưu trữ" trong một **"hệ thống cache 'riêng
          biệt' "** (distributed cache system), thường là một **"cluster"** (cụm) các máy chủ cache, **"tách biệt"** với
          các máy chủ ứng dụng.
        - **"Chia sẻ" dữ liệu cache:** Dữ liệu cache được **"chia sẻ"** giữa **"tất cả"** các "phiên bản" ứng dụng và
          các "máy chủ" khác nhau trong hệ thống. Bất kỳ "phiên bản" ứng dụng nào cũng có thể "truy cập" và "sử dụng" dữ
          liệu cache "chung".
        - **"Khả năng mở rộng" "cao":** Hệ thống distributed cache có thể được **"mở rộng"** "dễ dàng" bằng cách "thêm"
          máy chủ cache vào cluster để "tăng" dung lượng cache và "tăng" "khả năng chịu tải".
        - **"Độ tin cậy" "cao":** Hệ thống distributed cache thường được "thiết kế" để có **"độ tin cậy" "cao"**. Nếu
          một máy chủ cache bị "lỗi", các máy chủ cache khác trong cluster vẫn có thể "tiếp tục" "hoạt động" và "phục
          vụ" yêu cầu cache.

- **"Khi nào" nên "dùng" Distributed Caching? - "Khi Ứng Dụng 'Lớn Mạnh' và 'Phân Tán' ":**

    - Ứng dụng **"quy mô lớn"**, **"phân tán"**, chạy trên **"nhiều máy chủ"**.
    - Ứng dụng **web "quy mô lớn"** với "lượng truy cập" "cao".
    - **Ứng dụng microservices** - nơi các services "giao tiếp" và "chia sẻ" dữ liệu thông qua cache.
    - Khi bạn **"cần" "chia sẻ" dữ liệu cache** giữa các "phiên bản" ứng dụng để đảm bảo **"tính nhất quán"**.
    - Khi bạn **"cần" "mở rộng" dung lượng cache** và **"khả năng chịu tải"** của hệ thống cache.
    - Khi bạn **"ưu tiên" "độ tin cậy"** của hệ thống cache.

**3.2. Các "Nhà Cung Cấp" Cache "Phân Tán" "Nổi Tiếng" (Redis, Memcached) - "Chọn 'Bể Nước' Uy Tín"**

- **"Hai 'Anh Cả' " Trong Thế Giới Distributed Caching: Redis và Memcached:**

    - **Redis (Remote Dictionary Server):**

        - Một "hệ thống" distributed cache **"mã nguồn mở"** (open-source) **"phổ biến"** và **"mạnh mẽ"** nhất hiện
          nay.
        - **"Lưu trữ" dữ liệu "trong bộ nhớ"** (in-memory data store), nhưng cũng có thể "lưu trữ" dữ liệu **"trên đĩa"
          ** (disk persistence) để đảm bảo **"độ bền"** dữ liệu (data durability) khi server "khởi động lại".
        - **"Hỗ trợ" nhiều "kiểu dữ liệu" "phong phú"**: strings, hashes, lists, sets, sorted sets, bitmaps,
          hyperloglogs, geospatial indexes, streams.
        - **"Tính năng" "nổi bật"**: pub/sub (publish/subscribe), transactions, scripting (Lua scripting), clustering (
          để "mở rộng" và "tăng" "độ tin cậy").
        - **"Ưu điểm": "Mạnh mẽ", "đa năng", "hiệu năng cao", "khả năng mở rộng tốt", "cộng đồng lớn mạnh".**
        - **"Nhược điểm": "Phức tạp" hơn Memcached, "yêu cầu" "cấu hình" và "quản lý" "kỹ lưỡng" hơn.**
        - **"Phù hợp" với:** Ứng dụng **"yêu cầu" "hiệu năng cao"**, **"đa dạng" "kiểu dữ liệu"**, **"tính năng" "nâng
          cao"**, và **"khả năng mở rộng"**. Ứng dụng web "quy mô lớn", e-commerce, gaming, social media, v.v.

    - **Memcached (Memory Cache Daemon):**
        - Một "hệ thống" distributed cache **"mã nguồn mở"** (open-source) **"lâu đời"** và **"đơn giản"**.
        - **"Lưu trữ" dữ liệu "trong bộ nhớ"** (in-memory caching system) **"thuần túy"**. Dữ liệu cache **"không được '
          lưu' trên đĩa"**, nên sẽ **"bị mất"** khi server "khởi động lại".
        - **"Chỉ hỗ trợ" "kiểu dữ liệu" "duy nhất"**: strings (dữ liệu được xem như là chuỗi bytes).
        - **"Tính năng" "đơn giản"**: "Tập trung" vào "tốc độ" và "hiệu năng" caching "cơ bản".
        - **"Ưu điểm": "Cực kỳ nhanh", "đơn giản", "dễ sử dụng", "nhẹ nhàng", "tiêu thụ ít tài nguyên".**
        - **"Nhược điểm": "Tính năng" "hạn chế", "không có" "độ bền" dữ liệu, "khả năng mở rộng" "kém hơn" Redis.**
        - **"Phù hợp" với:** Ứng dụng **"yêu cầu" "tốc độ" "cực nhanh"**, **caching "đơn giản"**, **không cần" "độ bền"
          dữ liệu** và **"tính năng" "phức tạp"**. Caching session, caching HTML fragments, v.v.

- **"Chọn 'Bể Nước' Nào Cho Vừa?" - "Cân Nhắc 'Nhu Cầu' và 'Ngân Sách' ":**

    - **Redis:** "Lựa chọn" **"phổ biến"** và **"mạnh mẽ"** hơn, "phù hợp" với hầu hết các ứng dụng "hiện đại" "yêu
      cầu" "hiệu năng cao", "đa năng", và "khả năng mở rộng". Tuy nhiên, có thể **"phức tạp"** hơn trong "cấu hình" và "
      quản lý".
    - **Memcached:** "Lựa chọn" **"đơn giản"** và **"nhanh chóng"** hơn, "phù hợp" với các ứng dụng **"nhỏ"** hoặc **"
      vừa"** "yêu cầu" **"tốc độ" "cực nhanh"** và **caching "cơ bản"**. Tuy nhiên, có thể **"hạn chế"** về "tính năng"
      và "khả năng mở rộng" cho các ứng dụng "lớn".
    - **"Các 'nhà cung cấp' khác":** Ngoài Redis và Memcached, còn có nhiều "nhà cung cấp" Distributed Cache khác (ví
      dụ: Hazelcast, Apache Ignite, NCache, Azure Cache for Redis, Amazon ElastiCache, Google Cloud Memorystore,
      v.v.). "Lựa chọn" "tùy thuộc vào" "yêu cầu" cụ thể của bạn.
    - **"Dịch vụ Cloud Managed Cache":** Nếu bạn "chạy" ứng dụng trên cloud (ví dụ: Azure, AWS, Google Cloud), "xem
      xét" "sử dụng" các **"dịch vụ cloud managed cache"** (ví dụ: Azure Cache for Redis, Amazon ElastiCache, Google
      Cloud Memorystore). Các dịch vụ này "cung cấp" Distributed Cache dưới dạng **"dịch vụ" "quản lý" hoàn toàn** (
      fully managed service), giúp bạn "tiết kiệm" công sức "cài đặt", "cấu hình", và "quản lý" hệ thống cache.

**3.3. "Kết Nối" Với Redis Trong .NET (Ví dụ: StackExchange.Redis) - "Bắt Tay" Với Redis - "Mở 'Cánh Cửa' Vào Redis"**

- **"Thư Viện 'Trợ Thủ' " StackExchange.Redis - "Cầu Nối" Giữa .NET và Redis:**

    - Để "kết nối" và "tương tác" với Redis server từ ứng dụng .NET, chúng ta cần "dùng" một **"thư viện client"** (
      client library).
    - **StackExchange.Redis** là một thư viện client Redis **"mã nguồn mở"** (open-source) **"phổ biến"** và **"mạnh mẽ"
      ** nhất cho .NET.
    - StackExchange.Redis cung cấp một API **"dễ dùng"** và **"hiệu năng cao"** để "thực hiện" các thao tác với Redis
      server (ví dụ: "thêm", "lấy", "sửa", "xóa" dữ liệu cache, "thực hiện" các lệnh Redis, v.v.).

- **"Cài đặt" NuGet Package StackExchange.Redis:**

    - Trong Visual Studio, mở **NuGet Package Manager**.
    - "Tìm kiếm" package **`StackExchange.Redis`** và "cài đặt" vào dự án của bạn.

- **"Kết nối" đến Redis server:**

    - Để "kết nối" đến Redis server, bạn cần "dùng" class `ConnectionMultiplexer` từ thư viện StackExchange.Redis.
    - `ConnectionMultiplexer` "quản lý" **"kết nối"** đến Redis server và "cho phép" bạn "thực hiện" các lệnh Redis.
    - Bạn có thể "tạo" một instance `ConnectionMultiplexer` **"duy nhất"** và "dùng chung" trong toàn ứng dụng (
      singleton pattern) để "tối ưu" "hiệu năng" kết nối.

  ```csharp
  using StackExchange.Redis;

  public class RedisExample
  {
      private static ConnectionMultiplexer _redisConnection; // "Biến" static để "lưu" instance ConnectionMultiplexer "dùng chung"

      // "Phương thức" để "khởi tạo" kết nối Redis (singleton pattern)
      public static ConnectionMultiplexer GetRedisConnection()
      {
          if (_redisConnection == null || !_redisConnection.IsConnected) // "Kiểm tra" xem kết nối đã được "khởi tạo" chưa hoặc có còn "kết nối" không
          {
              string redisConnectionString = "localhost:6379"; // "Chuỗi kết nối" Redis server (ví dụ: chạy Redis Local) - "thay đổi" nếu cần
              _redisConnection = ConnectionMultiplexer.Connect(redisConnectionString); // "Khởi tạo" kết nối Redis
          }
          return _redisConnection; // "Trả về" instance ConnectionMultiplexer
      }

      public static void Main(string[] args)
      {
          // "Lấy" instance ConnectionMultiplexer "dùng chung"
          ConnectionMultiplexer redis = GetRedisConnection();

          // ... (các thao tác với Redis - xem phần sau) ...

          Console.ReadKey(); // "Giữ" console "mở" để xem kết quả
      }
  }
  ```

- **"Thao Tác" "Cơ Bản" Với Redis (Sử Dụng StackExchange.Redis):**

    - **"Lấy" database Redis (IDatabase):**

        - Để "thực hiện" các thao tác với Redis database (ví dụ: "thêm", "lấy", "sửa", "xóa" dữ liệu cache), bạn cần "
          lấy" một instance của interface `IDatabase` từ `ConnectionMultiplexer`.
        - `IDatabase` "đại diện" cho một Redis database (mỗi Redis server có thể có nhiều database, mặc định là 16
          database, đánh số từ 0 đến 15). "Database mặc định" là database 0.

      ```csharp
      // "Lấy" database Redis (database 0 "mặc định")
      IDatabase db = redis.GetDatabase();
      ```

    - **"Thêm" dữ liệu vào Redis (StringSet):**

        - "Chiêu" `StringSet(key, value)` dùng để "thêm" một cặp **"khóa-giá trị"** (key-value pair) vào Redis.
        - "Khóa" và "giá trị" trong Redis là **`RedisKey`** và **`RedisValue`** (structs của StackExchange.Redis),
          thường bạn có thể "chuyển đổi" từ kiểu `string` và `string` (hoặc các kiểu dữ liệu .NET khác) một cách "dễ
          dàng".

      ```csharp
      // "Khóa" cache Redis (ví dụ)
      RedisKey redisKey_SanPham_Redis_Add = "SanPham_Redis_1";

      // Dữ liệu sản phẩm (ví dụ) - "chuyển đổi" sang string để "lưu" vào Redis
      string sanPham_Redis_Value_Add = "{ 'Id': 1, 'Ten': 'Chuột Bluetooth', 'Gia': 350000 }";

      // "Thêm" dữ liệu vào Redis với "khóa" "SanPham_Redis_1"
      db.StringSet(redisKey_SanPham_Redis_Add, sanPham_Redis_Value_Add);

      Console.WriteLine($"Đã thêm sản phẩm vào Redis với khóa: {redisKey_SanPham_Redis_Add}");
      ```

    - **"Lấy" dữ liệu từ Redis (StringGet):**

        - "Chiêu" `StringGet(key)` dùng để "lấy" dữ liệu cache theo "khóa" từ Redis.
        - "Trả về": `RedisValue` dữ liệu cache nếu "tìm thấy" trong Redis (cache hit). "Trả về" `RedisValue.Null` nếu "
          không tìm thấy" (cache miss).

      ```csharp
      // "Khóa" cache Redis muốn "lấy" (ví dụ)
      RedisKey redisKey_SanPham_Redis_Get = "SanPham_Redis_1";

      // "Lấy" dữ liệu sản phẩm từ Redis theo "khóa" "SanPham_Redis_1"
      RedisValue sanPham_Redis_Cached = db.StringGet(redisKey_SanPham_Redis_Get);

      if (!sanPham_Redis_Cached.IsNull) // "Kiểm tra" xem có "tìm" thấy dữ liệu trong Redis không (cache hit)
      {
          // "Chuyển đổi" RedisValue về string và "xử lý" (ví dụ: deserialize JSON)
          string sanPham_Redis_String = sanPham_Redis_Cached.ToString();
          Console.WriteLine($"Cache hit (Redis)! Lấy sản phẩm từ Redis: {sanPham_Redis_String}");
      }
      else // "Không tìm thấy" trong Redis (cache miss)
      {
          Console.WriteLine("Cache miss (Redis)! Không tìm thấy sản phẩm trong Redis.");
          // (Code để "lấy" dữ liệu từ "nguồn gốc" - ví dụ: database - và "thêm" vào Redis - xem phần sau)
      }
      ```

    - **"Xóa" dữ liệu khỏi Redis (KeyDelete):**

        - "Chiêu" `KeyDelete(key)` dùng để "xóa" dữ liệu cache theo "khóa" khỏi Redis.

      ```csharp
      // "Khóa" cache Redis muốn "xóa" (ví dụ)
      RedisKey redisKey_SanPham_Redis_Remove = "SanPham_Redis_1";

      // "Xóa" dữ liệu sản phẩm khỏi Redis theo "khóa" "SanPham_Redis_1"
      db.KeyDelete(redisKey_SanPham_Redis_Remove);

      Console.WriteLine($"Đã xóa sản phẩm khỏi Redis với khóa: {redisKey_SanPham_Redis_Remove}");
      ```

- **"Các thao tác khác" với Redis:**

    - StackExchange.Redis cung cấp **"đầy đủ" API** để "thực hiện" **"tất cả" các lệnh Redis** (ví dụ: `HashSet`,
      `ListPush`, `SetAdd`, `SortedSetIncrement`, `Publish`, `Subscribe`, v.v.).
    - Bạn có thể "khám phá" tài liệu StackExchange.Redis và tài liệu Redis chính thức để "tìm hiểu" thêm về các "tính
      năng" và "lệnh" "đa dạng" của Redis.

**3.4. "Cấu Hình" và "Quản Lý" Cache "Phân Tán" - "Điều Hành 'Bể Nước' " - "Làm Chủ 'Bể Nước' Redis"**

- **"Cấu Hình" Redis Server:**

    - Để "sử dụng" Redis làm Distributed Cache, bạn cần **"cài đặt"** và **"cấu hình"** **Redis server**.
    - **"Cài đặt" Redis:** Bạn có thể "tải" Redis server từ [trang web chính thức của Redis](https://redis.io/) và "cài
      đặt" trên máy chủ của bạn (Windows, macOS, Linux). Hoặc "sử dụng" các dịch vụ cloud managed Redis (ví dụ: Azure
      Cache for Redis, Amazon ElastiCache, Google Cloud Memorystore).
    - **"Cấu hình" Redis:** Bạn có thể "cấu hình" Redis server thông qua file cấu hình `redis.conf`. Các "tùy chọn" cấu
      hình quan trọng bao gồm:
        - `port`: "Cổng" mà Redis server "lắng nghe" (mặc định là 6379).
        - `bind`: "Địa chỉ IP" mà Redis server "bind" vào (mặc định là 127.0.0.1 - chỉ "cho phép" kết nối từ localhost).
          Nếu muốn "cho phép" kết nối từ "xa", bạn cần "bind" vào "0.0.0.0" (tất cả các địa chỉ IP) hoặc "địa chỉ IP" cụ
          thể của máy chủ.
        - `requirepass`: "Mật khẩu" để "bảo vệ" Redis server (nên "cài đặt" mật khẩu trong môi trường production).
        - `maxmemory`: "Dung lượng bộ nhớ" tối đa mà Redis server có thể "sử dụng". Khi "vượt quá" giới hạn này, Redis
          sẽ "áp dụng" các "chính sách 'loại bỏ' cache" (eviction policies) để "giải phóng" bộ nhớ.
        - `maxmemory-policy`: "Chính sách 'loại bỏ' cache" (eviction policy) khi bộ nhớ "đầy" (ví dụ: `volatile-lru`,
          `allkeys-lru`, `volatile-ttl`, `allkeys-random`, v.v.). "Chọn" chính sách phù hợp với "yêu cầu" ứng dụng của
          bạn.
        - `persistence`: "Cơ chế 'lưu trữ' dữ liệu trên đĩa" (persistence) để đảm bảo "độ bền" dữ liệu (data durability)
          khi server "khởi động lại" (ví dụ: RDB, AOF). "Chọn" cơ chế persistence phù hợp với "yêu cầu" "độ bền" dữ liệu
          của bạn.
        - `cluster-enabled`: "Bật chế độ" Redis Cluster để "mở rộng" và "tăng" "độ tin cậy" của hệ thống cache.

- **"Quản Lý" Redis Server:**

    - **"Khởi động", "dừng", "khởi động lại" Redis server:** Bạn có thể "quản lý" Redis server thông qua command-line
      interface (CLI) hoặc các công cụ quản lý Redis khác (ví dụ: Redis Desktop Manager, RedisInsight).
    - **"Giám sát" "hiệu năng" Redis:** "Theo dõi" các "thông số" "hiệu năng" của Redis server (ví dụ: memory usage, CPU
      usage, connection count, cache hit rate, latency, v.v.) để "đảm bảo" Redis server "hoạt động" "ổn định" và "hiệu
      quả". Bạn có thể "dùng" các lệnh Redis CLI (`INFO`, `MONITOR`, `SLOWLOG`) hoặc các công cụ giám sát Redis để "theo
      dõi" "hiệu năng".
    - **"Backup" và "restore" dữ liệu Redis:** "Thực hiện" "backup" dữ liệu Redis định kỳ để "đảm bảo" "an toàn" dữ
      liệu. Bạn có thể "dùng" các lệnh Redis CLI (`SAVE`, `BGSAVE`) hoặc các công cụ backup Redis để "backup" dữ liệu.
      Khi cần "khôi phục" dữ liệu, bạn có thể "dùng" lệnh `RESTORE`.
    - **"Bảo mật" Redis server:** "Cài đặt" mật khẩu (`requirepass`), "giới hạn" "quyền truy cập" (access control list -
      ACL), "bật" TLS/SSL để "mã hóa" kết nối, và "tuân thủ" các "nguyên tắc" "bảo mật" khác để "bảo vệ" Redis server
      khỏi các "tấn công" bảo mật.

**Tổng Kết Chương 3:**

- Bạn đã "khám phá" **Distributed Caching**, "chiếc 'bể nước công cộng' " "mạnh mẽ" và "mở rộng", "phù hợp" với các ứng
  dụng "quy mô lớn" và "phân tán".
    - "Hiểu" **Distributed Caching là gì**, "khi nào" cần "dùng" Distributed Caching thay vì In-Memory Caching.
    - "Làm quen" với **Redis** và **Memcached**, hai "nhà cung cấp" Distributed Cache "nổi tiếng".
    - Học cách **"kết nối" với Redis trong .NET** bằng thư viện **StackExchange.Redis** và "thực hiện" các "thao tác" "
      cơ bản" với Redis.
    - Biết cách **"cấu hình"** và **"quản lý"** Redis server để "điều hành" "bể nước" Redis một cách "hiệu quả".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Caching Trong ASP.NET Core - "Web Cũng Cần 'Nước Ngọt' "**. Chúng ta sẽ "học cách" "
vận dụng" cả In-Memory Caching và Distributed Caching trong ứng dụng **ASP.NET Core**, "tối ưu hóa" "hiệu năng" cho ứng
dụng web của bạn.

Bạn có câu hỏi nào về Distributed Caching và Redis này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp"
và "đồng hành" cùng bạn trên con đường "chinh phục" Caching.
