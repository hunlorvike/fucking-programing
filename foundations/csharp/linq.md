## LINQ - Tổng Quan và Hướng Dẫn Sử Dụng Chi Tiết

### 1. **Giới thiệu về LINQ**

LINQ (Language Integrated Query) là một tính năng mạnh mẽ trong C# cho phép bạn truy vấn và thao tác với dữ liệu một cách dễ dàng và hiệu quả. LINQ giúp việc xử lý dữ liệu trở nên trực quan hơn bằng cách cho phép bạn sử dụng cú pháp tương tự như SQL để truy vấn các nguồn dữ liệu khác nhau, từ mảng đơn giản đến cơ sở dữ liệu phức tạp.

#### 1.1 **Lợi ích của LINQ**

- **Cú pháp rõ ràng**: Cú pháp truy vấn của LINQ tương tự như SQL, giúp dễ hiểu hơn cho lập trình viên.
- **Tính mở rộng**: LINQ có thể làm việc với nhiều loại nguồn dữ liệu khác nhau, bao gồm cơ sở dữ liệu, XML, và các tập hợp dữ liệu trong bộ nhớ.
- **Tính linh hoạt**: LINQ cho phép bạn xây dựng các truy vấn phức tạp với các phép toán như lọc, sắp xếp và nhóm dữ liệu.

### 2. **Các loại LINQ**

LINQ có thể được phân loại thành các loại chính sau đây:

#### 2.1 **LINQ to Objects**

- **Định nghĩa**: LINQ to Objects cho phép bạn truy vấn các tập hợp dữ liệu trong bộ nhớ như mảng, danh sách, và các kiểu dữ liệu khác trong .NET.
- **Sử dụng**: Không cần kết nối đến cơ sở dữ liệu, bạn có thể truy vấn trực tiếp trên các tập hợp dữ liệu.

#### 2.2 **LINQ to SQL**

- **Định nghĩa**: LINQ to SQL cho phép bạn truy vấn cơ sở dữ liệu SQL Server bằng cách sử dụng các đối tượng C#.
- **Sử dụng**: Thực hiện truy vấn dữ liệu từ cơ sở dữ liệu và ánh xạ các bảng trong cơ sở dữ liệu thành các lớp trong C#.

#### 2.3 **LINQ to Entities (Entity Framework)**

- **Định nghĩa**: LINQ to Entities là một phần của Entity Framework, cho phép bạn truy vấn dữ liệu từ cơ sở dữ liệu theo cách hướng đối tượng.
- **Sử dụng**: Ánh xạ giữa các đối tượng C# và các bảng trong cơ sở dữ liệu, cho phép thực hiện các truy vấn phức tạp với các đối tượng liên kết.

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

LINQ cung cấp nhiều phép toán để truy vấn và thao tác với dữ liệu. Dưới đây là một số phép toán cơ bản cùng với mô tả chi tiết và ví dụ minh họa.

#### 4.1 **Where**

- **Mô tả**: Phép toán `Where` cho phép bạn lọc các phần tử trong một tập hợp dựa trên điều kiện cho trước. Điều kiện này được xác định thông qua một biểu thức lambda hoặc một hàm.
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

- **Mô tả**: Phép toán `Select` cho phép bạn chọn một tập con thuộc tính từ các đối tượng trong tập hợp. Bạn có thể sử dụng nó để ánh xạ dữ liệu từ các đối tượng thành một loại dữ liệu khác.
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

- **Mô tả**: Phép toán `OrderBy` cho phép bạn sắp xếp các phần tử trong một tập hợp theo một hoặc nhiều thuộc tính. Sắp xếp có thể thực hiện theo thứ tự tăng dần hoặc giảm dần.
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

- **Mô tả**: Phép toán `GroupBy` cho phép bạn nhóm các phần tử trong một tập hợp dựa trên một thuộc tính. Kết quả là một tập hợp các nhóm, mỗi nhóm chứa các phần tử có giá trị chung cho thuộc tính đã chọn.
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

- **Mô tả**: Phép toán `Join` cho phép bạn kết hợp hai tập dữ liệu dựa trên một khóa chung. Điều này cho phép bạn tạo ra một tập hợp mới chứa các phần tử từ cả hai tập dữ liệu.
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

- **Mô tả**: Phép toán `Count` cho phép bạn đếm số phần tử trong một tập hợp. Bạn có thể đếm tất cả các phần tử hoặc chỉ những phần tử thỏa mãn một điều kiện nhất định.
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

- **Mô tả**: Phép toán `Sum` cho phép bạn tính tổng giá trị của một thuộc tính trong một tập hợp. Điều này rất hữu ích cho việc tính toán tổng số tiền, số lượng, hoặc bất kỳ giá trị số nào.
- **Cú pháp**:
  ```csharp
  var totalSum = collection.Sum(item => item.Property);
  ```
- **Ví dụ**:
  ```csharp
  var totalPrice = products.Sum(p => p.Price);
  // Kết quả: Tổng giá của tất cả sản phẩm
  ```

### Kết luận

Các phép toán trên cung cấp cho lập trình viên các công cụ mạnh mẽ để thao tác và truy vấn dữ liệu một cách hiệu quả trong C#. Việc sử dụng linh hoạt các phép toán này giúp bạn dễ dàng xử lý các tập hợp dữ liệu phức tạp, tạo ra các truy vấn tùy chỉnh và đạt được kết quả mong muốn.

### 5. **Ví dụ chi tiết**

#### 5.1 **Ví dụ về LINQ to Objects**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

class Product
{
    public string Name { get; set; }
    public decimal Price { get; set; }
}

class Program
{
    static void Main()
    {
        List<Product> products = new List<Product>
        {
            new Product { Name = "Product 1", Price = 50 },
            new Product { Name = "Product 2", Price = 150 },
            new Product { Name = "Product 3", Price = 200 },
        };

        // Sử dụng cú pháp truy vấn
        var expensiveProducts = from p in products
                                where p.Price > 100
                                select p;

        // Sử dụng cú pháp phương thức
        var expensiveProductsMethod = products.Where(p => p.Price > 100);

        // Hiển thị kết quả
        Console.WriteLine("Sản phẩm đắt tiền:");
        foreach (var product in expensiveProducts)
        {
            Console.WriteLine($"{product.Name}: {product.Price}");
        }
    }
}
```

#### 5.2 **Ví dụ về LINQ to SQL**

```csharp
using (var context = new DataContext())
{
    var products = from p in context.Products
                   where p.Price > 100
                   select p;

    foreach (var product in products)
    {
        Console.WriteLine(product.Name);
    }
}
```

#### 5.3 **Ví dụ về LINQ to Entities (Entity Framework)**

```csharp
using (var context = new MyDbContext())
{
    var orders = from o in context.Orders
                 where o.OrderDate > DateTime.Now.AddMonths(-1)
                 select o;

    foreach (var order in orders)
    {
        Console.WriteLine($"Order ID: {order.OrderId}, Date: {order.OrderDate}");
    }
}
```

#### 5.4 **Ví dụ về LINQ to XML**

```csharp
using System;
using System.Linq;
using System.Xml.Linq;

class Program
{
    static void Main()
    {
        XElement xml = XElement.Parse(@"
            <books>
                <book>
                    <title>Book 1</title>
                    <author>Author 1</author>
                </book>
                <book>
                    <title>Book 2</title>
                    <author>Author 2</author>
                </book>
            </books>");

        var titles = from book in xml.Elements("book")
                     select book.Element("title").Value;

        Console.WriteLine("Danh sách tiêu đề sách:");
        foreach (var title in titles)
        {
            Console.WriteLine(title);
        }
    }
}
```

#### 5.5 **Ví dụ về LINQ to DataSet**

```csharp
using System;
using System.Data;
using System.Linq;

class Program
{
    static void Main()
    {
        DataTable table = new DataTable();
        table.Columns.Add("Id", typeof(int));
        table.Columns.Add("Name", typeof(string));

        table.Rows.Add(1, "Alice");
        table.Rows.Add(2, "Bob");

        var query = from row in table.AsEnumerable()
                    where row.Field<int>("Id") > 1
                    select row.Field<string>("Name");

        Console.WriteLine("Tên người có ID lớn hơn 1:");
        foreach (var name in query)
        {
            Console.WriteLine(name);
        }
    }
}
```

### 6. **Deferred Execution trong LINQ**

LINQ sử dụng **Deferred Execution**, có nghĩa là truy vấn không được thực hiện ngay lập tức mà chỉ được thực hiện khi bạn thực sự duyệt qua nó. Điều này cho phép bạn thay đổi dữ liệu mà không cần phải cập nhật truy vấn.

**Ví dụ về Deferred Execution**:

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
var query = numbers.Where(n => n > 3); // Chưa thực hiện truy vấn

numbers.Add(6); // Thay đổi dữ liệu

foreach (var num in query) // Truy vấn thực hiện tại đây
{
    Console.WriteLine(num); // Kết quả: 4, 5, 6
}
```

### 7. **Kết hợp LINQ với Entity Framework**

Khi sử dụng Entity Framework, bạn có thể sử dụng LINQ để truy vấn cơ sở dữ liệu một cách dễ dàng. LINQ giúp bạn xây dựng các truy vấn phức tạp mà vẫn giữ mã nguồn rõ ràng và dễ đọc.

#### Ví dụ:

```csharp
using (var context = new MyDbContext())
{
    var query = from p in context.Products
                where p.Price > 100
                select p;

    foreach (var product in query)
    {
        Console.WriteLine(product.Name);
    }
}
```

### 8. **Tóm tắt**

LINQ là một công cụ mạnh mẽ giúp

bạn truy vấn và thao tác dữ liệu trong C#. Việc sử dụng LINQ giúp mã nguồn trở nên ngắn gọn và dễ đọc hơn. Bạn có thể kết hợp LINQ với nhiều loại nguồn dữ liệu khác nhau, từ các tập hợp trong bộ nhớ đến các cơ sở dữ liệu phức tạp.

Nếu bạn cần thêm thông tin chi tiết về bất kỳ loại LINQ nào, hoặc có câu hỏi cụ thể nào về LINQ, đừng ngần ngại hỏi thêm!
