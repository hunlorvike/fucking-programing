## **🚀 "GIẢI MÃ" TỐI ƯU HÓA DATABASE: "BƠM" DỮ LIỆU NHANH NHƯ CHỚP CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một chủ đề rất quan trọng: Tối ưu hóa Database. Đây là
một kỹ năng "đắt giá" giúp bạn "cân" mọi bài toán liên quan đến dữ liệu. Cùng mình "mổ xẻ" nó nhé!

### **I. TỐI ƯU HÓA DATABASE LÀ GÌ? (LÀM CHO DATABASE "NGON" HƠN)**

- **Tối ưu hóa Database:** Là quá trình _cải thiện_ hiệu suất của cơ sở dữ liệu, giúp:
    - **Truy vấn nhanh:** Lấy dữ liệu nhanh hơn.
    - **Giảm tải:** Tiết kiệm tài nguyên (CPU, RAM, ổ cứng).
    - **Ổn định:** Đảm bảo database hoạt động ổn định, không bị chậm, treo.
- **Quan trọng vì:**
    - **Tốc độ:** Ứng dụng chạy nhanh hơn, trải nghiệm tốt hơn.
    - **Tài nguyên:** Tiết kiệm chi phí server.
    - **Mở rộng:** Giúp ứng dụng dễ dàng mở rộng khi dữ liệu lớn.

### **II. CÁC YẾU TỐ CẦN TỐI ƯU (CÁI GÌ CẦN "LÀM MỊN")**

1. **Truy vấn (Query):** Tối ưu câu lệnh SQL (như `SELECT`, `JOIN`,...).
2. **Chỉ mục (Index):** Tạo index để tìm kiếm nhanh.
3. **Bảng (Table):** Thiết kế bảng hợp lý (chuẩn hóa, khử chuẩn hóa, ...).
4. **Phân vùng (Partitioning):** Chia nhỏ bảng khi dữ liệu quá lớn.
5. **Caching (Bộ nhớ đệm):** Lưu kết quả query thường dùng để lấy nhanh.
6. **Replication/Sharding:** Nhân bản database để tăng hiệu suất, chịu tải.

### **III. CÁC KỸ THUẬT TỐI ƯU HÓA (NHỮNG "CHIÊU" LÀM DATABASE "NGON" HƠN)**

1. **Tối ưu hóa Truy vấn (Query Optimization):**

    - Chỉ lấy các cột cần thiết (`SELECT column1, column2,...` thay vì `SELECT *`).
    - Dùng `WHERE` để lọc dữ liệu trước khi lấy (như đã nói ở bài về WHERE).
    - Dùng `JOIN` thay vì dùng subquery (truy vấn con) khi cần thiết (bài về join).
    - Tránh dùng `SELECT DISTINCT` nếu không cần thiết.

2. **Sử Dụng Index (Indexing):**

    - Tạo index trên các cột thường dùng để tìm kiếm, sắp xếp, ...
    - **Ví dụ:** `CREATE INDEX idx_name ON Employees (LastName)`.
    - **Chú ý:** Đừng tạo quá nhiều index, làm chậm các thao tác ghi.
        - Tạo index cho các cột thường dùng trong `WHERE`, `JOIN`, `ORDER BY`.

3. **Thiết kế Bảng (Table Design):**

    - **Chuẩn hóa (Normalization):** Chia bảng nhỏ hơn, tránh trùng lặp dữ liệu (bài về chuẩn hóa database).
    - **Khử chuẩn hóa (Denormalization):** Kết hợp một số bảng (tránh JOIN nhiều) khi cần (ví dụ trong data warehouse).
    - Chọn kiểu dữ liệu phù hợp (như đã nói ở bài về database).

4. **Phân Vùng Bảng (Partitioning):**

    - Chia bảng lớn thành các phần nhỏ hơn (theo thời gian, vùng, ...).
    - **Ví dụ:** Chia bảng `Orders` theo tháng.
    - Có thể là Horizontal Partitioning và Vertical Partitioning.

5. **Bộ nhớ đệm (Caching):**

    - Lưu kết quả truy vấn thường dùng vào cache (Redis, Memcached) để truy cập nhanh hơn.
    - **Ví dụ:** Cache kết quả các truy vấn `SELECT` thường dùng.

6. **Replication & Sharding:**

    - **Replication:** Nhân bản database để tăng khả năng chịu tải.
    - **Sharding:** Chia database thành nhiều phần để giảm tải cho một server.

7. **Tối ưu Full-Text Search:**

    - Nếu cần tìm kiếm toàn văn, hãy dùng Full-Text Search (thay vì dùng `LIKE` hoặc `CONTAINS` chậm).

8. **Tối ưu dữ liệu:**
    - Dữ liệu được nén và lưu trữ dạng blob để giảm dung lượng.
    - Dữ liệu có được phân loại hợp lý, các dữ liệu hay được truy cập nên được đặt gần nhau để dễ tìm kiếm

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **Tối ưu query:**

    - **Thay vì:**
      ```sql
      SELECT *
      FROM Employees
      WHERE Department = 'Sales';
      ```
    - **Hãy dùng:**
      ```sql
      SELECT FirstName, LastName, Email, Salary
      FROM Employees
      WHERE Department = 'Sales';
      ```

2. **Tạo index:**

```sql
CREATE INDEX idx_department ON Employees (Department);
```

3. **Dùng caching:**
    - **Code ví dụ (C#):**

```csharp
using Microsoft.Extensions.Caching.Memory;

public class DataService
{
    private readonly IMemoryCache _memoryCache;
    public DataService(IMemoryCache memoryCache) {
       _memoryCache = memoryCache;
    }

    public string GetData(string key) {
         string cacheEntry;
         if(!_memoryCache.TryGetValue(key, out cacheEntry)) {
            cacheEntry = "Data từ database"; // giả sử lấy data từ db
            var cacheEntryOptions = new MemoryCacheEntryOptions()
                .SetAbsoluteExpiration(TimeSpan.FromSeconds(3));
            _memoryCache.Set(key, cacheEntry, cacheEntryOptions);
          }
      return cacheEntry;
    }
}
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Hiểu rõ dữ liệu:** Hiểu rõ dữ liệu, cách dùng để chọn index, cấu trúc,... phù hợp.
- **Đo đạc:** Đo hiệu suất query để biết cái nào chậm, cần tối ưu.
- **Cân bằng:** Chọn cách tối ưu phù hợp với tình huống (đừng lạm dụng).
- **Tối ưu từ từ:** Không cần tối ưu mọi thứ ngay, từ từ làm từng bước.
- **Theo dõi và bảo trì**: Sau khi tối ưu, cần theo dõi và bảo trì database thường xuyên.

### **VI. KẾT LUẬN (TỔNG KẾT)**

Tối ưu hóa database là một quá trình liên tục, đòi hỏi sự hiểu biết sâu rộng về cả database và ứng dụng. Hy vọng qua bài
viết này, các bạn đã hiểu rõ hơn về các kỹ thuật tối ưu hóa và có thể áp dụng chúng vào dự án của mình. Chúc các bạn
code thành công! 😎
