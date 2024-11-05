Dưới đây là tài liệu mô tả chi tiết về các loại data loading trong Entity Framework, bao gồm `Eager Loading`, `Lazy Loading`, và `Explicit Loading`. Mỗi loại loading sẽ được giải thích với định nghĩa, ưu điểm, nhược điểm, ví dụ cụ thể và các câu SQL tương ứng nếu cần.

---

# Các Loại Data Loading trong Entity Framework

## Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Eager Loading](#1-eager-loading)
   - [Định nghĩa](#định-nghĩa)
   - [Ví dụ](#ví-dụ)
   - [Câu SQL tương ứng](#câu-sql-tương-ứng)
   - [Ưu điểm](#ưu-điểm)
   - [Nhược điểm](#nhược-điểm)
3. [Lazy Loading](#2-lazy-loading)
   - [Định nghĩa](#định-nghĩa-1)
   - [Ví dụ](#ví-dụ-1)
   - [Câu SQL tương ứng](#câu-sql-tương-ứng-1)
   - [Ưu điểm](#ưu-điểm-1)
   - [Nhược điểm](#nhược-điểm-1)
4. [Explicit Loading](#3-explicit-loading)
   - [Định nghĩa](#định-nghĩa-2)
   - [Ví dụ](#ví-dụ-2)
   - [Câu SQL tương ứng](#câu-sql-tương-ứng-2)
   - [Ưu điểm](#ưu-điểm-2)
   - [Nhược điểm](#nhược-điểm-2)
5. [Kết Luận](#kết-luận)

---

## Giới Thiệu

Tài liệu này mô tả chi tiết các loại data loading trong Entity Framework, bao gồm `Eager Loading`, `Lazy Loading`, và `Explicit Loading`. Mỗi loại loading sẽ được giải thích với định nghĩa, ưu điểm, nhược điểm và ví dụ cụ thể.

---

## 1. Eager Loading

### Định nghĩa

Eager loading là phương pháp tải dữ liệu mà trong đó tất cả các entity và các liên kết liên quan đến nó được tải ngay lập tức khi truy vấn đầu tiên được thực hiện. Điều này thường được thực hiện bằng cách sử dụng phương thức `Include` trong Entity Framework.

### Ví dụ

Giả sử bạn có hai entity là `Blog` và `Post`, trong đó mỗi `Blog` có nhiều `Post`.

```csharp
using (var context = new BloggingContext())
{
    var blogs = context.Blogs.Include(b => b.Posts).ToList();
}
```

### Câu SQL tương ứng

```sql
SELECT *
FROM Blogs
LEFT JOIN Posts ON Blogs.Id = Posts.BlogId;
```

### Ưu điểm

- Tất cả dữ liệu cần thiết được tải trong một lần truy vấn, giúp giảm số lần gọi đến cơ sở dữ liệu.
- Giảm thiểu hiện tượng N+1 queries (vấn đề tải nhiều truy vấn).

### Nhược điểm

- Nếu số lượng dữ liệu lớn, có thể gây ra vấn đề hiệu suất do tải quá nhiều dữ liệu không cần thiết.
- Tăng kích thước dữ liệu truyền qua mạng.

---

## 2. Lazy Loading

### Định nghĩa

Lazy loading là phương pháp tải dữ liệu mà trong đó các entity và các liên kết của chúng sẽ chỉ được tải khi cần thiết. Điều này có nghĩa là dữ liệu sẽ không được tải cho đến khi bạn thực sự truy cập vào thuộc tính đó.

### Ví dụ

Tiếp tục với ví dụ trên, bạn có thể định nghĩa các liên kết trong entity `Blog` để sử dụng lazy loading.

```csharp
public class Blog
{
    public int Id { get; set; }
    public string Name { get; set; }
    virtual public ICollection<Post> Posts { get; set; }
}

// Sử dụng lazy loading
using (var context = new BloggingContext())
{
    var blog = context.Blogs.First();
    var posts = blog.Posts; // Tại thời điểm này, dữ liệu của Posts được tải
}
```

### Câu SQL tương ứng

```sql
SELECT *
FROM Blogs
WHERE Id = @blogId; -- Truy vấn đầu tiên

-- Sau khi truy cập vào blog.Posts
SELECT *
FROM Posts
WHERE BlogId = @blogId; -- Truy vấn thứ hai
```

### Ưu điểm

- Giảm tải ban đầu và chỉ tải dữ liệu khi thực sự cần thiết.
- Hữu ích khi làm việc với các liên kết lớn mà không cần thiết phải tải ngay lập tức.

### Nhược điểm

- Có thể dẫn đến N+1 queries, làm giảm hiệu suất do phải thực hiện nhiều truy vấn đến cơ sở dữ liệu.
- Khó khăn trong việc dự đoán số lượng truy vấn sẽ thực hiện.

---

## 3. Explicit Loading

### Định nghĩa

Explicit loading là phương pháp tải dữ liệu mà trong đó bạn yêu cầu tải dữ liệu cụ thể một cách rõ ràng, thường sử dụng phương thức `Load` trong Entity Framework.

### Ví dụ

Bạn có thể sử dụng explicit loading khi bạn đã có một entity và muốn tải các liên kết của nó một cách rõ ràng.

```csharp
using (var context = new BloggingContext())
{
    var blog = context.Blogs.First();
    context.Entry(blog).Collection(b => b.Posts).Load(); // Tải rõ ràng Posts
}
```

### Câu SQL tương ứng

```sql
SELECT *
FROM Blogs
WHERE Id = @blogId; -- Truy vấn đầu tiên

SELECT *
FROM Posts
WHERE BlogId = @blogId; -- Truy vấn thứ hai
```

### Ưu điểm

- Cung cấp sự kiểm soát rõ ràng hơn về việc khi nào và cái gì được tải.
- Giảm nguy cơ N+1 queries vì bạn có thể tải nhiều collection hoặc reference một cách có kế hoạch.

### Nhược điểm

- Cần phải viết mã rõ ràng hơn, có thể gây ra sự phức tạp trong mã nguồn.
- Có thể vẫn phải thực hiện nhiều truy vấn đến cơ sở dữ liệu nếu không được xử lý đúng cách.

---

## Kết Luận

Việc lựa chọn phương pháp data loading trong Entity Framework phụ thuộc vào yêu cầu của ứng dụng và cách bạn muốn quản lý dữ liệu. Mỗi phương pháp đều có những ưu điểm và nhược điểm riêng, do đó, cần cân nhắc kỹ lưỡng trước khi quyết định áp dụng cho dự án của mình. Việc sử dụng đúng phương pháp loading sẽ giúp tối ưu hóa hiệu suất và cấu trúc truy vấn trong ứng dụng.
