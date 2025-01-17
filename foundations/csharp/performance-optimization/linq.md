# LINQ - Tổng Quan và Hướng Dẫn Sử Dụng Chi Tiết

## Mục lục

1. [Giới thiệu về LINQ](#1-giới-thiệu-về-linq)
    - [Lợi ích của LINQ](#11-lợi-ích-của-linq)
2. [Các loại LINQ](#2-các-loại-linq)
    - [LINQ to Objects](#21-linq-to-objects)
    - [LINQ to SQL](#22-linq-to-sql)
    - [LINQ to Entities (Entity Framework)](#23-linq-to-entities-entity-framework)
    - [LINQ to XML](#24-linq-to-xml)
    - [LINQ to DataSet](#25-linq-to-dataset)
3. [Cú pháp cơ bản của LINQ](#3-cú-pháp-cơ-bản-của-linq)
    - [Cú pháp truy vấn (Query Syntax)](#31-cú-pháp-truy-vấn-query-syntax)
    - [Cú pháp phương thức (Method Syntax)](#32-cú-pháp-phương-thức-method-syntax)
4. [Các phép toán trong LINQ](#4-các-phép-toán-trong-linq)
    - [Where](#41-where)
    - [Select](#42-select)
    - [OrderBy](#43-orderby)
    - [GroupBy](#44-groupby)
    - [Join](#45-join)
    - [Distinct](#46-distinct)
    - [Count](#47-count)
    - [Sum](#48-sum)
5. [IQueryable vs IEnumerable](#5-iqueryable-vs-ienumerable)
    - [IEnumerable](#51-ienumerable)
    - [IQueryable](#52-iqueryable)
    - [So sánh giữa IQueryable và IEnumerable](#53-so-sánh-giữa-iqueryable-và-ienumerable)
6. [Kết luận](#6-kết-luận)

---

### 1. **Giới thiệu về LINQ**

LINQ (Language Integrated Query) là một tính năng mạnh mẽ trong C# cho phép bạn truy vấn và thao tác với dữ liệu một
cách dễ dàng và hiệu quả. LINQ giúp việc xử lý dữ liệu trở nên trực quan hơn bằng cách cho phép bạn sử dụng cú pháp
tương tự như SQL để truy vấn các nguồn dữ liệu khác nhau, từ mảng đơn giản đến cơ sở dữ liệu phức tạp.

#### 1.1 **Lợi ích của LINQ**

- **Cú pháp rõ ràng**: Cú pháp truy vấn của LINQ tương tự như SQL, giúp dễ hiểu hơn cho lập trình viên.
- **Tính mở rộng**: LINQ có thể làm việc với nhiều loại nguồn dữ liệu khác nhau, bao gồm cơ sở dữ liệu, XML, và các tập
  hợp dữ liệu trong bộ nhớ.
- **Tính linh hoạt**: LINQ cho phép bạn xây dựng các truy vấn phức tạp với các phép toán như lọc, sắp xếp và nhóm dữ
  liệu.

### 2. **Các loại LINQ**

LINQ có thể được phân loại thành các loại chính sau đây:

#### 2.1 **LINQ to Objects**

- **Định nghĩa**: LINQ to Objects cho phép bạn truy vấn các tập hợp dữ liệu trong bộ nhớ như mảng, danh sách, và các
  kiểu dữ liệu khác trong .NET.
- **Sử dụng**: Không cần kết nối đến cơ sở dữ liệu, bạn có thể truy vấn trực tiếp trên các tập hợp dữ liệu.

#### 2.2 **LINQ to SQL**

- **Định nghĩa**: LINQ to SQL cho phép bạn truy vấn cơ sở dữ liệu SQL Server bằng cách sử dụng các đối tượng C#.
- **Sử dụng**: Thực hiện truy vấn dữ liệu từ cơ sở dữ liệu và ánh xạ các bảng trong cơ sở dữ liệu thành các lớp trong
  C#.

#### 2.3 **LINQ to Entities (Entity Framework)**

- **Định nghĩa**: LINQ to Entities là một phần của Entity Framework, cho phép bạn truy vấn dữ liệu từ cơ sở dữ liệu theo
  cách hướng đối tượng.
- **Sử dụng**: Ánh xạ giữa các đối tượng C# và các bảng trong cơ sở dữ liệu, cho phép thực hiện các truy vấn phức tạp
  với các đối tượng liên kết.

#### 2.4 **LINQ to XML**

- **Định nghĩa**: LINQ to XML cho phép bạn truy vấn và thao tác với tài liệu XML một cách dễ dàng.
- **Sử dụng**: Thực hiện truy vấn, xây dựng, đọc, sửa đổi và lưu tài liệu XML.

#### 2.5 **LINQ to DataSet**

- **Định nghĩa**: LINQ to DataSet cho phép bạn truy vấn các đối tượng `DataSet` trong ADO.NET.
- **Sử dụng**: Dễ dàng xử lý dữ liệu trong bộ nhớ thông qua các bảng trong `DataSet`.

### 3. **Cú pháp cơ bản của LINQ**

LINQ có hai cú pháp chính: cú pháp truy vấn (Query Syntax) và cú pháp phương thức (Method Syntax).

#### 3.1 **Cú pháp truy vấn (Query Syntax)**

Cú pháp này tương tự như SQL và giúp lập trình viên dễ hiểu hơn.

**Ví dụ**:

```csharp
var query = from item in items
            where item.Price > 100
            select item;
```

#### 3.2 **Cú pháp phương thức (Method Syntax)**

Cú pháp này sử dụng các phương thức mở rộng và có thể linh hoạt hơn trong nhiều tình huống.

**Ví dụ**:

```csharp
var query = items.Where(item => item.Price > 100);
```

### 4. **Các phép toán trong LINQ**

LINQ cung cấp nhiều phép toán để truy vấn và thao tác với dữ liệu. Dưới đây là một số phép toán cơ bản cùng với mô tả
chi tiết và ví dụ minh họa.

#### 4.1 **Where**

- **Mô tả**: Phép toán `Where` cho phép bạn lọc các phần tử trong một tập hợp dựa trên điều kiện cho trước.
- **Cú pháp**:
  ```csharp
  var result = collection.Where(item => condition);
  ```
- **Ví dụ**:
  ```csharp
  var evenNumbers = numbers.Where(n => n % 2 == 0);
  // Kết quả: [2, 4, 6, 8, 10]
  ```

#### 4.2 **Select**

- **Mô tả**: Phép toán `Select` cho phép bạn chọn một tập con thuộc tính từ các đối tượng trong tập hợp.
- **Cú pháp**:
  ```csharp
  var result = collection.Select(item => selectedProperty);
  ```
- **Ví dụ**:
  ```csharp
  var productNames = products.Select(p => p.Name);
  // Kết quả: ["Product 1", "Product 2", "Product 3"]
  ```

#### 4.3 **OrderBy**

- **Mô tả**: Phép toán `OrderBy` cho phép bạn sắp xếp các phần tử trong một tập hợp theo một hoặc nhiều thuộc tính.
- **Cú pháp**:
  ```csharp
  var result = collection.OrderBy(item => property);
  ```
- **Ví dụ**:
  ```csharp
  var sortedProducts = products.OrderBy(p => p.Price);
  // Kết quả: Danh sách sản phẩm được sắp xếp theo giá tăng dần
  ```

#### 4.4 **GroupBy**

- **Mô tả**: Phép toán `GroupBy` cho phép bạn nhóm các phần tử trong một tập hợp dựa trên một thuộc tính.
- **Cú pháp**:
  ```csharp
  var result = collection.GroupBy(item => property);
  ```
- **Ví dụ**:
  ```csharp
  var groupedByCategory = products.GroupBy(p => p.Category);
  // Kết quả: Các nhóm sản phẩm theo danh mục
  ```

#### 4.5 **Join**

- **Mô tả**: Phép toán `Join` cho phép bạn kết hợp hai tập dữ liệu dựa trên một khóa chung.
- **Cú pháp**:
  ```csharp
  var result = collection1.Join(collection2,
                                 outerKeySelector,
                                 innerKeySelector,
                                 resultSelector);
  ```
- **Ví dụ**:
  ```csharp
  var productOrders = products.Join(orders,
                                     p => p.ProductId,
                                     o => o.ProductId,
                                     (p, o) => new { p.Name, o.Quantity });
  // Kết quả: Danh sách tên sản phẩm cùng với số lượng đã đặt
  ```

#### 4.6 **Distinct**

- **Mô tả**: Phép toán `Distinct` cho phép bạn lấy các phần tử duy nhất từ một tập hợp, loại bỏ các phần tử trùng lặp.
- **Cú pháp**:
  ```csharp
  var result = collection.Distinct();
  ```
- **Ví dụ**:
  ```csharp
  var uniqueNumbers = numbers.Distinct();
  // Kết quả: Danh sách số duy nhất trong tập hợp
  ```

#### 4.7 **Count**

- **Mô tả**: Phép toán `Count` cho phép bạn đếm số phần tử trong một tập hợp.

- **Cú pháp**:
  ```csharp
  var count = collection.Count();
  var countWithCondition = collection.Count(item => condition);
  ```
- **Ví dụ**:
  ```csharp
  var totalProducts = products.Count();
  var expensiveProductsCount = products.Count(p => p.Price > 100);
  // Kết quả: Tổng số sản phẩm và số sản phẩm có giá lớn hơn 100
  ```

#### 4.8 **Sum**

- **Mô tả**: Phép toán `Sum` cho phép bạn tính tổng giá trị của một thuộc tính trong một tập hợp.
- **Cú pháp**:
  ```csharp
  var totalSum = collection.Sum(item => item.Property);
  ```
- **Ví dụ**:
  ```csharp
  var totalPrice = products.Sum(p => p.Price);
  // Kết quả: Tổng giá của tất cả sản phẩm
  ```

#### 4.9 **Take và Skip**

- **Mô tả**:
    - `Take`: Lấy một số lượng phần tử đầu tiên từ một tập hợp.
    - `Skip`: Bỏ qua một số lượng phần tử đầu tiên từ một tập hợp.
- **Cú pháp**:
  ```csharp
  var resultTake = collection.Take(number);
  var resultSkip = collection.Skip(number);
  ```
- **Ví dụ**:
  ```csharp
  var topFiveProducts = products.Take(5);      // Lấy 5 sản phẩm đầu tiên
  var skipFiveProducts = products.Skip(5);     // Bỏ qua 5 sản phẩm đầu tiên
  ```

#### 4.10 **TakeWhile và SkipWhile**

- **Mô tả**:
    - `TakeWhile`: Lấy các phần tử từ đầu tập hợp cho đến khi gặp điều kiện sai.
    - `SkipWhile`: Bỏ qua các phần tử từ đầu tập hợp cho đến khi gặp điều kiện sai.
- **Cú pháp**:
  ```csharp
  var resultTakeWhile = collection.TakeWhile(item => condition);
  var resultSkipWhile = collection.SkipWhile(item => condition);
  ```
- **Ví dụ**:
  ```csharp
  var cheapProducts = products.TakeWhile(p => p.Price < 50);
  var expensiveProductsSkipped = products.SkipWhile(p => p.Price < 50);
  ```

#### 4.11 **All và Any**

- **Mô tả**:
    - `All`: Kiểm tra nếu tất cả các phần tử trong tập hợp thỏa mãn một điều kiện.
    - `Any`: Kiểm tra nếu có ít nhất một phần tử trong tập hợp thỏa mãn một điều kiện.
- **Cú pháp**:
  ```csharp
  bool allCondition = collection.All(item => condition);
  bool anyCondition = collection.Any(item => condition);
  ```
- **Ví dụ**:
  ```csharp
  bool allExpensive = products.All(p => p.Price > 100);
  bool anyExpensive = products.Any(p => p.Price > 100);
  ```

#### 4.12 **First, FirstOrDefault, Last, LastOrDefault**

- **Mô tả**:
    - `First`: Trả về phần tử đầu tiên của tập hợp, nếu không tìm thấy sẽ ném ngoại lệ.
    - `FirstOrDefault`: Trả về phần tử đầu tiên của tập hợp hoặc giá trị mặc định nếu không tìm thấy.
    - `Last`: Trả về phần tử cuối cùng của tập hợp, nếu không tìm thấy sẽ ném ngoại lệ.
    - `LastOrDefault`: Trả về phần tử cuối cùng của tập hợp hoặc giá trị mặc định nếu không tìm thấy.
- **Cú pháp**:
  ```csharp
  var firstElement = collection.First();
  var firstOrDefaultElement = collection.FirstOrDefault();
  var lastElement = collection.Last();
  var lastOrDefaultElement = collection.LastOrDefault();
  ```
- **Ví dụ**:
  ```csharp
  var firstProduct = products.First();
  var lastProduct = products.Last();
  var firstExpensiveProduct = products.FirstOrDefault(p => p.Price > 100);
  ```

#### 4.13 **Single và SingleOrDefault**

- **Mô tả**:
    - `Single`: Trả về duy nhất một phần tử thỏa mãn điều kiện, nếu có nhiều hơn một hoặc không có phần tử nào thì sẽ
      ném ngoại lệ.
    - `SingleOrDefault`: Trả về duy nhất một phần tử thỏa mãn điều kiện hoặc giá trị mặc định nếu không tìm thấy.
- **Cú pháp**:
  ```csharp
  var singleElement = collection.Single(item => condition);
  var singleOrDefaultElement = collection.SingleOrDefault(item => condition);
  ```
- **Ví dụ**:
  ```csharp
  var singleProduct = products.Single(p => p.ProductId == 1);
  var optionalProduct = products.SingleOrDefault(p => p.ProductId == 99);
  ```

#### 4.14 **Aggregate**

- **Mô tả**: Phép toán `Aggregate` thực hiện tính toán tùy chỉnh trên một tập hợp, ví dụ như tính tổng, tích, hoặc nối
  chuỗi.
- **Cú pháp**:
  ```csharp
  var result = collection.Aggregate(seed, (accumulator, item) => operation);
  ```
- **Ví dụ**:
  ```csharp
  var concatenatedNames = products.Aggregate((current, next) => current + ", " + next.Name);
  ```

#### 4.15 **Min, Max, Average**

- **Mô tả**:
    - `Min`: Tìm giá trị nhỏ nhất từ một thuộc tính của các phần tử trong tập hợp.
    - `Max`: Tìm giá trị lớn nhất từ một thuộc tính của các phần tử trong tập hợp.
    - `Average`: Tính giá trị trung bình từ một thuộc tính của các phần tử trong tập hợp.
- **Cú pháp**:
  ```csharp
  var min = collection.Min(item => item.Property);
  var max = collection.Max(item => item.Property);
  var avg = collection.Average(item => item.Property);
  ```
- **Ví dụ**:
  ```csharp
  var minPrice = products.Min(p => p.Price);
  var maxPrice = products.Max(p => p.Price);
  var averagePrice = products.Average(p => p.Price);
  ```

#### 4.16 **Concat**

- **Mô tả**: Phép toán `Concat` cho phép bạn nối hai tập hợp lại với nhau.
- **Cú pháp**:
  ```csharp
  var result = collection1.Concat(collection2);
  ```
- **Ví dụ**:
  ```csharp
  var combinedList = list1.Concat(list2);
  ```

#### 4.17 **Zip**

- **Mô tả**: `Zip` ghép nối các phần tử từ hai tập hợp lại với nhau, theo từng cặp tương ứng.
- **Cú pháp**:
  ```csharp
  var result = collection1.Zip(collection2, (first, second) => resultSelector);
  ```
- **Ví dụ**:
  ```csharp
  var pairedList = numbers.Zip(words, (n, w) => $"{n}: {w}");
  ```

#### 4.18 **DefaultIfEmpty**

- **Mô tả**: `DefaultIfEmpty` trả về tập hợp ban đầu hoặc một giá trị mặc định nếu tập hợp rỗng.
- **Cú pháp**:
  ```csharp
  var result = collection.DefaultIfEmpty(defaultValue);
  ```
- **Ví dụ**:
  ```csharp
  var productsOrDefault = products.DefaultIfEmpty(new Product { Name = "No products available" });
  ```

#### 4.19 **ToList, ToArray, ToDictionary**

- **Mô tả**:
    - `ToList`: Chuyển tập hợp thành danh sách `List`.
    - `ToArray`: Chuyển tập hợp thành mảng `Array`.
    - `ToDictionary`: Chuyển tập hợp thành từ điển `Dictionary` với khóa và giá trị chỉ định.
- **Cú pháp**:
  ```csharp
  var listResult = collection.ToList();
  var arrayResult = collection.ToArray();
  var dictionaryResult = collection.ToDictionary(item => item.Key, item => item.Value);
  ```
- **Ví dụ**:
  ```csharp
  var productList = products.ToList();
  var productArray = products.ToArray();
  var productDictionary = products.ToDictionary(p => p.ProductId, p => p.Name);
  ```

#### 4.20 **Union, Intersect, Except**

- **Mô tả**:
    - `Union`: Trả về tập hợp kết hợp của hai tập hợp, loại bỏ các phần tử trùng lặp.
    - `Intersect`: Trả về các phần tử có trong cả hai tập hợp.
    - `Except`: Trả về các phần tử chỉ có trong tập hợp đầu tiên mà không có trong tập hợp thứ hai.
- **Cú pháp**:
  ```csharp
  var unionResult = collection1.Union(collection2);
  var intersectResult = collection1.Intersect(collection2);
  var exceptResult = collection1.Except(collection2);
  ```
- **Ví dụ**:
  ```csharp
  var allUniqueProducts = products1.Union(products2);
  var commonProducts = products1.Intersect(products2);
  var differenceProducts = products1.Except(products2);
  ```

### 5. **IQueryable vs IEnumerable**

#### 5.1 **IEnumerable**

- **Mô tả**:

    - `IEnumerable` là một giao diện được sử dụng để đại diện cho một tập hợp các đối tượng trong bộ nhớ (RAM).
    - Khi làm việc với `IEnumerable`, toàn bộ dữ liệu từ cơ sở dữ liệu phải được tải vào bộ nhớ trước khi thực hiện các
      phương thức LINQ. Điều này có thể gây tiêu tốn tài nguyên và giảm hiệu suất, đặc biệt khi làm việc với các tập dữ
      liệu lớn.

- **Tính năng**:

    - Không hỗ trợ ánh xạ biểu thức; tất cả các truy vấn được thực hiện trong bộ nhớ.
    - Phù hợp khi dữ liệu đã được tải vào bộ nhớ và cần thực hiện các thao tác.
    - Thực hiện truy vấn ở mức client; tất cả dữ liệu phải được tải vào bộ nhớ trước.
    - Hiệu suất có thể kém hơn với các tập dữ liệu lớn do phải tải toàn bộ dữ liệu.

- **Ví dụ**:
  ```csharp
  IEnumerable<Product> enumerableProducts = context.Products.ToList();
  var expensiveProducts = enumerableProducts.Where(p => p.Price > 100);
  ```

#### 5.2 **IQueryable**

- **Mô tả**:

    - `IQueryable` là một giao diện cho phép bạn thực hiện truy vấn trên nguồn dữ liệu bên ngoài (như cơ sở dữ liệu).
    - Nó không tải toàn bộ dữ liệu vào bộ nhớ; thay vào đó, nó đại diện cho một truy vấn chưa được thực thi. Khi bạn áp
      dụng các phương thức LINQ (như `Where`, `Select`, v.v.) trên `IQueryable`, các phương thức này sẽ được chuyển đổi
      thành câu lệnh SQL và được thực thi trên cơ sở dữ liệu.

- **Tính năng**:

    - Hỗ trợ ánh xạ biểu thức (expression trees), cho phép chuyển đổi thành câu lệnh SQL.
    - Tối ưu hóa hiệu suất truy vấn bằng cách chuyển điều kiện về phía nguồn dữ liệu.
    - Thực hiện truy vấn trên server, chỉ tải dữ liệu cần thiết từ cơ sở dữ liệu.
    - Hiệu suất nhanh hơn với cơ sở dữ liệu vì chỉ truy xuất dữ liệu cần thiết.

- **Ví dụ**:
  ```csharp
  IQueryable<Product> queryableProducts = context.Products.AsQueryable();
  var expensiveProducts = queryableProducts.Where(p => p.Price > 100);
  ```

#### 5.3 **So sánh giữa IQueryable và IEnumerable**

| Tính năng            | **IQueryable**                                                    | **IEnumerable**                            |
|----------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Nguồn dữ liệu**    | Dữ liệu từ nhiều nguồn khác nhau (cơ sở dữ liệu, dịch vụ web,...) | Dữ liệu trong bộ nhớ (mảng, danh sách,...) |
| **Xử lý truy vấn**   | Xử lý truy vấn tại nguồn dữ liệu                                  | Xử lý truy vấn trong bộ nhớ                |
| **Ánh xạ biểu thức** | Hỗ trợ ánh xạ biểu thức (expression trees)                        | Không hỗ trợ ánh xạ biểu thức              |
| **Hiệu suất**        | Tối ưu hơn với truy vấn phức tạp                                  | Có thể kém hơn với tập dữ liệu lớn         |
| **Cú pháp**          | Cú pháp linh hoạt với LINQ                                        | Cú pháp đơn giản với LINQ                  |

- Khi lựa chọn giữa `IQueryable` và `IEnumerable`, hãy xem xét kích thước và nguồn dữ liệu của bạn. `IQueryable` phù hợp
  hơn cho các truy vấn lớn và phức tạp, trong khi `IEnumerable` có thể thích hợp cho các tập dữ liệu nhỏ đã được tải vào
  bộ nhớ.

### 6. **Kết luận**

LINQ là một công cụ mạnh mẽ giúp lập trình viên C# thao tác với dữ liệu một cách hiệu quả và dễ dàng. Bằng cách sử dụng
LINQ, bạn có thể thực hiện các truy vấn phức tạp trên nhiều nguồn dữ liệu khác nhau, đồng thời cải thiện độ rõ ràng và
tính bảo trì của mã nguồn.
