# Cache trong C# .NET

## Mục Lục

1. [Tổng quan về Cache](#1-tổng-quan-về-cache)
    - [Cache là gì?](#cache-là-gì)
    - [Lợi ích của Cache](#lợi-ích-của-cache)
    - [Cache hoạt động như thế nào?](#cache-hoạt-động-như-thế-nào)
2. [Các loại Cache trong C# .NET](#2-các-loại-cache-trong-c-net)
    - [In-Memory Cache](#in-memory-cache)
    - [Distributed Cache](#distributed-cache)
    - [Persistent Cache](#persistent-cache)
    - [Client-Side Cache](#client-side-cache)
3. [Sử dụng Cache trong ASP.NET Core](#3-sử-dụng-cache-trong-aspnet-core)
    - [Cấu hình và sử dụng In-Memory Cache](#cấu-hình-và-sử-dụng-in-memory-cache)
    - [Cấu hình và sử dụng Distributed Cache](#cấu-hình-và-sử-dụng-distributed-cache)
4. [Thiết lập thời gian tồn tại và làm mới Cache](#4-thiết-lập-thời-gian-tồn-tại-và-làm-mới-cache)
5. [Lưu ý về bảo mật và hiệu suất Cache](#5-lưu-ý-về-bảo-mật-và-hiệu-suất-cache)
    - [Quản lý bộ nhớ Cache hiệu quả](#quản-lý-bộ-nhớ-cache-hiệu-quả)
    - [Cache dữ liệu nhạy cảm](#cache-dữ-liệu-nhạy-cảm)
6. [Công cụ quản lý Cache trong môi trường Production](#6-công-cụ-quản-lý-cache-trong-môi-trường-production)
7. [Kết luận](#kết-luận)

---

### 1. Tổng quan về Cache

#### Cache là gì?

Cache là một kỹ thuật lưu trữ tạm thời dữ liệu đã truy xuất hoặc tính toán để phục vụ nhanh chóng khi có yêu cầu tương
tự trong tương lai. Thay vì truy xuất lại từ nguồn dữ liệu gốc (ví dụ: cơ sở dữ liệu), ứng dụng có thể lấy dữ liệu từ bộ
nhớ cache, giúp cải thiện tốc độ và hiệu suất.

#### Lợi ích của Cache

- **Cải thiện hiệu suất**: Giảm thời gian truy xuất dữ liệu từ nguồn gốc.
- **Giảm tải hệ thống**: Giảm số lượng truy vấn vào cơ sở dữ liệu hoặc các hệ thống bên ngoài.
- **Tăng khả năng mở rộng**: Hệ thống có thể xử lý lượng truy cập lớn hơn với ít tài nguyên hơn.

#### Cache hoạt động như thế nào?

1. Khi một yêu cầu dữ liệu mới xuất hiện, ứng dụng kiểm tra cache xem dữ liệu có sẵn không.
2. Nếu có, ứng dụng trả về dữ liệu từ cache.
3. Nếu không, ứng dụng truy xuất dữ liệu từ nguồn gốc, sau đó lưu dữ liệu vào cache cho các yêu cầu sau.

### 2. Các loại Cache trong C# .NET

#### In-Memory Cache

In-Memory Cache lưu trữ dữ liệu ngay trên bộ nhớ của ứng dụng, giúp truy xuất dữ liệu nhanh chóng. Tuy nhiên, dữ liệu
này sẽ mất khi ứng dụng khởi động lại hoặc khi bộ nhớ đầy.

- **Ưu điểm**: Truy cập nhanh, dễ cấu hình, phù hợp với dữ liệu nhỏ và không cần chia sẻ giữa nhiều phiên bản ứng dụng.
- **Nhược điểm**: Mất dữ liệu khi ứng dụng khởi động lại, không hỗ trợ phân tán.

#### Distributed Cache

Distributed Cache là hệ thống cache phân tán, lưu trữ dữ liệu trên các dịch vụ bên ngoài như **Redis**, **SQL Server**
hoặc **NCache**, cho phép các phiên bản ứng dụng khác nhau cùng truy cập vào dữ liệu cache.

- **Ưu điểm**: Dữ liệu được chia sẻ và duy trì giữa các phiên bản ứng dụng, có thể cấu hình dữ liệu tồn tại lâu hơn.
- **Nhược điểm**: Truy xuất chậm hơn In-Memory Cache, cần thiết lập và quản lý dịch vụ phân tán.

#### Persistent Cache

Persistent Cache lưu trữ dữ liệu vào một nguồn dữ liệu lâu dài, thường là cơ sở dữ liệu hoặc lưu trữ đám mây. Dữ liệu
cache này sẽ không bị mất khi ứng dụng khởi động lại và thường được sử dụng cho dữ liệu có chu kỳ cập nhật chậm nhưng
cần truy xuất thường xuyên.

- **Ưu điểm**: Lưu trữ dữ liệu cache lâu dài, hỗ trợ khôi phục dữ liệu sau khi khởi động lại hệ thống.
- **Nhược điểm**: Truy xuất có thể chậm hơn so với In-Memory Cache hoặc Distributed Cache, tùy thuộc vào hệ thống lưu
  trữ dữ liệu.
- **Cách sử dụng**: Dữ liệu ít thay đổi như cấu hình hệ thống, dữ liệu thống kê, hoặc dữ liệu người dùng cần truy xuất
  liên tục mà không muốn truy vấn cơ sở dữ liệu gốc.

Ví dụ: Sử dụng Redis với cấu hình lưu trữ lâu dài hoặc kết hợp với SQL Server để đảm bảo dữ liệu không bị mất sau khi
khởi động lại.

#### Client-Side Cache

Client-Side Cache là bộ nhớ cache lưu trực tiếp trên trình duyệt hoặc thiết bị của người dùng, được sử dụng để lưu trữ
dữ liệu tạm thời nhằm giảm thiểu số lượng yêu cầu đến máy chủ và tăng tốc độ phản hồi.

- **Ưu điểm**: Giảm tải cho máy chủ, cải thiện tốc độ truy cập khi dữ liệu có sẵn ngay trên thiết bị người dùng.
- **Nhược điểm**: Dữ liệu phụ thuộc vào thiết bị người dùng, dễ bị mất khi người dùng xóa cache hoặc thay đổi thiết bị.
- **Cách sử dụng**: Các thư viện JavaScript như `localStorage` hoặc `sessionStorage` để lưu dữ liệu nhỏ, không nhạy cảm
  như các cấu hình hoặc phiên làm việc.

Ví dụ: Lưu trữ dữ liệu người dùng tạm thời như cấu hình giao diện hoặc dữ liệu đã tải về trước đó.

### 3. Sử dụng Cache trong ASP.NET Core

#### Cấu hình và sử dụng In-Memory Cache

ASP.NET Core hỗ trợ In-Memory Cache tích hợp sẵn, dễ dàng thiết lập và sử dụng. Để sử dụng In-Memory Cache, ta cần cấu
hình trong `Startup.cs`:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddMemoryCache(); // Thêm In-Memory Cache vào DI container
}
```

Ví dụ sử dụng In-Memory Cache trong một dịch vụ:

```csharp
public class SampleService
{
    private readonly IMemoryCache _cache;

    public SampleService(IMemoryCache cache)
    {
        _cache = cache;
    }

    public string GetCachedData()
    {
        string cacheKey = "sampleData";
        if (!_cache.TryGetValue(cacheKey, out string cachedData))
        {
            cachedData = "Data from source"; // Lấy dữ liệu từ nguồn gốc
            var cacheOptions = new MemoryCacheEntryOptions
            {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5),
                SlidingExpiration = TimeSpan.FromMinutes(2)
            };
            _cache.Set(cacheKey, cachedData, cacheOptions); // Lưu vào cache
        }

        return cachedData;
    }
}
```

#### Cấu hình và sử dụng Distributed Cache

Distributed Cache trong ASP.NET Core yêu cầu cấu hình thêm một số dịch vụ bên ngoài (ví dụ: Redis, SQL Server).

**Ví dụ với Redis Cache:**

1. **Cài đặt Redis package**:

   ```bash
   dotnet add package Microsoft.Extensions.Caching.StackExchangeRedis
   ```

2. **Cấu hình Redis Cache trong `Startup.cs`:**

   ```csharp
   public void ConfigureServices(IServiceCollection services)
   {
       services.AddStackExchangeRedisCache(options =>
       {
           options.Configuration = "localhost:6379";
           options.InstanceName = "SampleInstance";
       });
   }
   ```

3. **Sử dụng Redis Cache trong dịch vụ:**

   ```csharp
   public class SampleService
   {
       private readonly IDistributedCache _cache;

       public SampleService(IDistributedCache cache)
       {
           _cache = cache;
       }

       public async Task<string> GetCachedDataAsync()
       {
           string cacheKey = "sampleData";
           var cachedData = await _cache.GetStringAsync(cacheKey);
           if (cachedData == null)
           {
               cachedData = "Data from source";
               var options = new DistributedCacheEntryOptions
               {
                   AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5)
               };
               await _cache.SetStringAsync(cacheKey, cachedData, options);
           }

           return cachedData;
       }
   }
   ```

### 4. Thiết lập thời gian tồn tại và làm mới Cache

ASP.NET Core cung cấp các tùy chọn cấu hình cho thời gian tồn tại của dữ liệu trong cache:

- **Absolute Expiration**: Dữ liệu cache sẽ hết hạn sau một khoảng thời gian cố định, tính từ khi nó được lưu vào cache.
- **Sliding Expiration**: Mỗi khi dữ liệu được truy xuất, thời gian hết hạn sẽ được gia hạn thêm, giúp giữ dữ liệu cache
  lâu hơn nếu thường xuyên sử dụng.

Ví dụ cấu hình:

```csharp
var cacheOptions = new MemoryCacheEntryOptions
{
    AbsoluteExpirationRelativeTo

Now = TimeSpan.FromMinutes(10),
    SlidingExpiration = TimeSpan.FromMinutes(2)
};
_cache.Set("key", data, cacheOptions);
```

### 5. Lưu ý về bảo mật và hiệu suất Cache

#### Quản lý bộ nhớ Cache hiệu quả

- Chỉ nên lưu các dữ liệu thường xuyên được truy xuất và không quá lớn vào cache.
- Sử dụng các chính sách xóa dữ liệu cache không còn sử dụng để tránh tốn bộ nhớ.

#### Cache dữ liệu nhạy cảm

- Tránh cache các dữ liệu nhạy cảm như thông tin người dùng hoặc dữ liệu nhạy cảm khác.
- Nếu cần cache dữ liệu nhạy cảm, hãy mã hóa trước khi lưu vào cache để bảo vệ an toàn.

### 6. Công cụ quản lý Cache trong môi trường Production

Trong môi trường Production, có thể sử dụng các công cụ quản lý và giám sát cache mạnh mẽ để tối ưu hóa và đảm bảo hiệu
suất:

- **Redis**: Cung cấp khả năng phân tán và hiệu suất cao cho cache, hỗ trợ cấu trúc dữ liệu phức tạp.
- **NCache**: Giải pháp cache phân tán cho .NET với khả năng mở rộng và tính sẵn sàng cao.
- **Memcached**: Giải pháp cache phân tán phổ biến, nhẹ nhàng và hiệu quả.

Các công cụ này cung cấp các tính năng như tự động xóa dữ liệu cũ, kiểm tra sức khỏe hệ thống cache, và hỗ trợ cho các
ứng dụng quy mô lớn.

### Kết luận

Cache là một thành phần quan trọng để cải thiện hiệu suất và khả năng mở rộng của ứng dụng. ASP.NET Core cung cấp các
tùy chọn cấu hình cache linh hoạt, từ In-Memory Cache cho đến Distributed Cache với các dịch vụ bên ngoài. Việc quản lý
và bảo vệ dữ liệu cache đúng cách sẽ giúp hệ thống hoạt động ổn định và an toàn hơn.
