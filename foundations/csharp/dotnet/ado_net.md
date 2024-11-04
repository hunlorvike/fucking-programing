## ADO.NET trong C# .NET

### 1. Tổng quan về ADO.NET

#### 1.1. ADO.NET là gì?

ADO.NET là một tập hợp các lớp trong .NET Framework cho phép bạn làm việc với dữ liệu trong các ứng dụng .NET. Nó cung cấp các khả năng để kết nối, truy vấn và thao tác với cơ sở dữ liệu. ADO.NET hỗ trợ nhiều loại cơ sở dữ liệu, bao gồm SQL Server, Oracle, MySQL, và nhiều loại khác.

#### 1.2. Các thành phần chính của ADO.NET

##### **1. Connection**

**Mô tả**: `Connection` là thành phần dùng để mở và quản lý kết nối tới cơ sở dữ liệu. Nó cung cấp thông tin cần thiết để ADO.NET có thể kết nối với cơ sở dữ liệu, như tên máy chủ, tên cơ sở dữ liệu, và thông tin xác thực.

**Cách sử dụng**:

- **Lớp chính**: `SqlConnection` cho SQL Server (có các lớp tương tự cho các cơ sở dữ liệu khác như `OleDbConnection`, `OracleConnection`, v.v.).
- **Cách mở kết nối**:
  ```csharp
  using (SqlConnection connection = new SqlConnection(connectionString))
  {
      connection.Open();
      // Thực hiện các thao tác với cơ sở dữ liệu
  }
  ```
- **Quản lý vòng đời**: Kết nối nên được mở khi cần và đóng lại ngay sau khi sử dụng để giải phóng tài nguyên.

##### **2. Command**

**Mô tả**: `Command` là thành phần cho phép bạn thực thi các câu lệnh SQL hoặc các stored procedures trên cơ sở dữ liệu.

**Cách sử dụng**:

- **Lớp chính**: `SqlCommand` cho SQL Server (có các lớp tương tự cho các cơ sở dữ liệu khác).
- **Cách thực thi câu lệnh**:
  ```csharp
  using (SqlCommand command = new SqlCommand("SELECT * FROM Employees", connection))
  {
      // Thực thi câu lệnh
      using (SqlDataReader reader = command.ExecuteReader())
      {
          while (reader.Read())
          {
              Console.WriteLine(reader["Name"]);
          }
      }
  }
  ```
- **Sử dụng tham số**: Để tránh tấn công SQL injection và cải thiện hiệu suất.
  ```csharp
  command.Parameters.AddWithValue("@Name", "John Doe");
  ```

##### **3. DataReader**

**Mô tả**: `DataReader` là thành phần cho phép bạn đọc dữ liệu từ cơ sở dữ liệu một cách tuần tự. Nó cung cấp khả năng đọc dữ liệu một cách nhanh chóng, nhưng không hỗ trợ lưu trữ dữ liệu để truy xuất sau này.

**Cách sử dụng**:

- **Lớp chính**: `SqlDataReader` cho SQL Server.
- **Đọc dữ liệu**:
  ```csharp
  using (SqlDataReader reader = command.ExecuteReader())
  {
      while (reader.Read())
      {
          Console.WriteLine($"{reader["Name"]}, {reader["Position"]}");
      }
  }
  ```
- **Tính năng**:
  - Chỉ có thể đọc dữ liệu theo dòng (từng dòng một).
  - Hiệu suất cao vì không lưu trữ dữ liệu trong bộ nhớ.

##### **4. DataAdapter**

**Mô tả**: `DataAdapter` là thành phần dùng để làm cầu nối giữa `DataSet` và cơ sở dữ liệu. Nó cho phép bạn lấy dữ liệu từ cơ sở dữ liệu vào `DataSet` và gửi dữ liệu đã thay đổi từ `DataSet` trở lại cơ sở dữ liệu.

**Cách sử dụng**:

- **Lớp chính**: `SqlDataAdapter` cho SQL Server.
- **Cách sử dụng**:
  ```csharp
  SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM Employees", connection);
  DataSet dataSet = new DataSet();
  adapter.Fill(dataSet, "Employees"); // Lấy dữ liệu vào DataSet
  ```
- **Cập nhật dữ liệu**: Để cập nhật dữ liệu từ `DataSet` trở lại cơ sở dữ liệu, bạn cần thiết lập các `Command` cho việc thêm, sửa, xóa.
  ```csharp
  SqlCommandBuilder commandBuilder = new SqlCommandBuilder(adapter);
  adapter.Update(dataSet, "Employees"); // Cập nhật dữ liệu
  ```

##### **5. DataSet**

**Mô tả**: `DataSet` là một đối tượng chứa nhiều bảng dữ liệu (DataTable) và các mối quan hệ giữa chúng. Nó cho phép bạn làm việc với dữ liệu trong bộ nhớ mà không cần phải kết nối liên tục với cơ sở dữ liệu.

**Cách sử dụng**:

- **Cách tạo `DataSet`**:
  ```csharp
  DataSet dataSet = new DataSet();
  SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM Employees", connection);
  adapter.Fill(dataSet, "Employees"); // Lấy dữ liệu vào DataSet
  ```
- **Làm việc với `DataTable`**:
  ```csharp
  DataTable employeesTable = dataSet.Tables["Employees"];
  foreach (DataRow row in employeesTable.Rows)
  {
      Console.WriteLine($"{row["Name"]}, {row["Position"]}");
  }
  ```
- **Mối quan hệ giữa các bảng**: Bạn có thể thiết lập mối quan hệ giữa các bảng trong `DataSet` bằng cách sử dụng `DataRelation`.
  ```csharp
  DataRelation relation = new DataRelation("RelationName", parentTableColumn, childTableColumn);
  dataSet.Relations.Add(relation);
  ```

### 2. Cài đặt ADO.NET

#### 2.1. Cài đặt môi trường phát triển

- Cài đặt Visual Studio hoặc một IDE hỗ trợ C#.
- Cài đặt SQL Server hoặc một cơ sở dữ liệu tương thích.

#### 2.2. Thêm thư viện cần thiết

Trong Visual Studio, bạn cần thêm các thư viện cần thiết:

```csharp
using System.Data;
using System.Data.SqlClient;
```

### 3. Các bước sử dụng ADO.NET

#### 3.1. Kết nối tới cơ sở dữ liệu

Để kết nối tới cơ sở dữ liệu, bạn cần tạo một đối tượng `SqlConnection`.

```csharp
string connectionString = "Data Source=server_name;Initial Catalog=database_name;User ID=user_id;Password=password;";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();
    // Thao tác với cơ sở dữ liệu
}
```

#### 3.2. Thực thi câu lệnh SQL với `JOIN`

Bạn có thể sử dụng đối tượng `SqlCommand` để thực thi các câu lệnh SQL, bao gồm cả câu lệnh `JOIN` để kết hợp dữ liệu từ nhiều bảng.

```csharp
string query = @"
    SELECT e.Name, e.Position, d.DepartmentName
    FROM Employees e
    JOIN Departments d ON e.DepartmentId = d.Id";

using (SqlCommand command = new SqlCommand(query, connection))
{
    using (SqlDataReader reader = command.ExecuteReader())
    {
        while (reader.Read())
        {
            Console.WriteLine($"{reader["Name"]}, {reader["Position"]}, {reader["DepartmentName"]}");
        }
    }
}
```

#### 3.3. Sử dụng `WHERE` để lọc dữ liệu

Để lọc dữ liệu theo điều kiện, bạn có thể sử dụng mệnh đề `WHERE`.

```csharp
string query = @"
    SELECT e.Name, e.Position
    FROM Employees e
    WHERE e.Position = @position";

using (SqlCommand command = new SqlCommand(query, connection))
{
    command.Parameters.AddWithValue("@position", "Manager");

    using (SqlDataReader reader = command.ExecuteReader())
    {
        while (reader.Read())
        {
            Console.WriteLine($"{reader["Name"]}, {reader["Position"]}");
        }
    }
}
```

#### 3.4. Sử dụng `DataAdapter` và `DataSet`

`DataAdapter` giúp bạn thực hiện các hoạt động như thêm, cập nhật, xóa dữ liệu trong `DataSet`.

```csharp
SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM Employees", connection);
DataSet dataSet = new DataSet();
adapter.Fill(dataSet, "Employees");

// Thao tác với DataTable
DataTable employeesTable = dataSet.Tables["Employees"];
foreach (DataRow row in employeesTable.Rows)
{
    Console.WriteLine($"{row["Name"]}, {row["Position"]}");
}
```

### 4. Ánh xạ dữ liệu với class Model

Để ánh xạ dữ liệu từ cơ sở dữ liệu vào các đối tượng C#, bạn có thể tạo các lớp mô hình tương ứng.

#### 4.1. Định nghĩa mô hình

```csharp
public class Employee
{
    public string Name { get; set; }
    public string Position { get; set; }
    public string DepartmentName { get; set; }
}
```

#### 4.2. Sử dụng mô hình trong truy vấn

Dưới đây là ví dụ sử dụng mô hình để lưu trữ dữ liệu từ truy vấn `JOIN`.

```csharp
List<Employee> employees = new List<Employee>();

string query = @"
    SELECT e.Name, e.Position, d.DepartmentName
    FROM Employees e
    JOIN Departments d ON e.DepartmentId = d.Id";

using (SqlCommand command = new SqlCommand(query, connection))
{
    using (SqlDataReader reader = command.ExecuteReader())
    {
        while (reader.Read())
        {
            Employee employee = new Employee
            {
                Name = reader["Name"].ToString(),
                Position = reader["Position"].ToString(),
                DepartmentName = reader["DepartmentName"].ToString()
            };
            employees.Add(employee);
        }
    }
}

// Hiển thị thông tin nhân viên
foreach (var emp in employees)
{
    Console.WriteLine($"{emp.Name}, {emp.Position}, {emp.DepartmentName}");
}
```

### 5. Ví dụ hoàn chỉnh

Dưới đây là một ví dụ hoàn chỉnh về việc sử dụng ADO.NET để kết nối tới cơ sở dữ liệu, thực thi các câu lệnh với `JOIN` và `WHERE`, và ánh xạ dữ liệu vào mô hình C#:

```csharp
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;

class Program
{
    public class Employee
    {
        public string Name { get; set; }
        public string Position { get; set; }
        public string DepartmentName { get; set; }
    }

    static void Main()
    {
        string connectionString = "Data Source=server_name;Initial Catalog=database_name;User ID=user_id;Password=password;";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            connection.Open();

            List<Employee> employees = new List<Employee>();

            string query = @"
                SELECT e.Name, e.Position, d.DepartmentName
                FROM Employees e
                JOIN Departments d ON e.DepartmentId = d.Id
                WHERE e.Position = @position";

            using (SqlCommand command = new SqlCommand(query, connection))
            {
                command.Parameters.AddWithValue("@position", "Manager");

                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        Employee employee = new Employee
                        {
                            Name = reader["Name"].ToString(),
                            Position = reader["Position"].ToString(),
                            DepartmentName = reader["DepartmentName"].ToString()
                        };
                        employees.Add(employee);
                    }
                }
            }

            // Hiển thị thông tin nhân viên
            foreach (var emp in employees)
            {
                Console.WriteLine($"{emp.Name}, {emp.Position}, {emp.DepartmentName}");
            }
        }
    }
}
```

### 6. Kết luận

ADO.NET là một công cụ mạnh mẽ cho phép lập trình viên .NET thao tác với dữ liệu trong cơ sở dữ liệu. Bằng cách hiểu và áp dụng các thành phần của ADO.NET, bạn có thể xây dựng các ứng dụng có khả năng tương tác với dữ liệu một cách hiệu quả. Hướng dẫn này đã cung cấp thông tin chi tiết về việc sử dụng `JOIN`, `WHERE` và ánh xạ dữ liệu tới mô hình C#, giúp bạn nâng cao kỹ năng làm việc với ADO.NET trong C#.

Hy vọng hướng dẫn này hữu ích cho bạn trong việc tìm hiểu về ADO.NET trong C# .NET!

Dưới đây là bảng giới thiệu một số ORM (Object-Relational Mapping) phổ biến được phát triển trên nền ADO.NET. Các ORM này giúp lập trình viên dễ dàng làm việc với cơ sở dữ liệu mà không cần viết nhiều câu lệnh SQL phức tạp.

| Tên ORM                  | Mô Tả                                                                                 | Đặc Điểm Nổi Bật                                                               | Tài Liệu / Liên Kết                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **Entity Framework**     | ORM chính thức của Microsoft cho .NET, hỗ trợ làm việc với các cơ sở dữ liệu quan hệ. | - Hỗ trợ LINQ cho truy vấn. <br> - Code First, Database First.                 | [Entity Framework](https://learn.microsoft.com/en-us/ef/)                               |
| **Dapper**               | Một micro ORM nhẹ và nhanh, phù hợp cho các ứng dụng có hiệu suất cao.                | - Hiệu suất cao, gần như nguyên thủy. <br> - Dễ sử dụng.                       | [Dapper](https://dapper-tutorial.net/)                                                  |
| **NHibernate**           | Một ORM mạnh mẽ và linh hoạt, dựa trên Hibernate từ Java.                             | - Hỗ trợ nhiều tính năng như caching, lazy loading. <br> - Cấu hình linh hoạt. | [NHibernate](https://nhibernate.info/)                                                  |
| **Linq to SQL**          | Một ORM đơn giản được tích hợp trong .NET để làm việc với SQL Server.                 | - Hỗ trợ LINQ cho truy vấn. <br> - Dễ dàng ánh xạ dữ liệu.                     | [Linq to SQL](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/) |
| **ServiceStack OrmLite** | ORM nhanh chóng và nhẹ, giúp kết nối với nhiều loại cơ sở dữ liệu khác nhau.          | - Hiệu suất cao, đơn giản hóa mã. <br> - Hỗ trợ nhiều loại cơ sở dữ liệu.      | [ServiceStack OrmLite](https://ormlite.readthedocs.io/en/latest/)                       |
| **PetaPoco**             | Một micro ORM rất nhẹ cho .NET, dễ dàng tích hợp và sử dụng.                          | - Đơn giản và dễ hiểu. <br> - Tích hợp tốt với các framework khác.             | [PetaPoco](https://petapoco.com/)                                                       |

### Một số điểm cần lưu ý:

- **Entity Framework**: Là lựa chọn phổ biến nhất cho các ứng dụng .NET, cung cấp nhiều tính năng mạnh mẽ giúp phát triển nhanh chóng.
- **Dapper**: Nếu hiệu suất là ưu tiên hàng đầu, Dapper là lựa chọn tuyệt vời do tốc độ và tính nhẹ của nó.
- **NHibernate**: Phù hợp cho các ứng dụng phức tạp cần nhiều tính năng như caching và mối quan hệ phức tạp giữa các bảng.
- **Linq to SQL**: Dễ sử dụng cho các ứng dụng đơn giản, nhưng chỉ hỗ trợ SQL Server.
- **ServiceStack OrmLite và PetaPoco**: Thích hợp cho những ai muốn tìm kiếm một giải pháp đơn giản và dễ sử dụng mà vẫn mạnh mẽ.

Hy vọng bảng trên sẽ giúp bạn có cái nhìn tổng quan về các ORM phổ biến trên nền ADO.NET!
