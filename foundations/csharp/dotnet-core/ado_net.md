# ADO.NET trong C# .NET

## Mục lục

1. [Tổng quan về ADO.NET](#1-tổng-quan-về-adonet)
    - [1.1. ADO.NET là gì?](#11-adonet-là-gì)
    - [1.2. Các thành phần chính của ADO.NET](#12-các-thành-phần-chính-của-adonet)
        - [1. Connection](#connection)
        - [2. Command](#command)
        - [3. DataReader](#datareader)
        - [4. DataAdapter](#dataadapter)
        - [5. DataSet](#dataset)
2. [Cài đặt ADO.NET](#2-cài-đặt-adonet)
    - [2.1. Cài đặt môi trường phát triển](#21-cài-đặt-môi-trường-phát-triển)
    - [2.2. Thêm thư viện cần thiết](#22-thêm-thư-viện-cần-thiết)
3. [Các bước sử dụng ADO.NET](#3-các-bước-sử-dụng-adonet)
    - [3.1. Kết nối tới cơ sở dữ liệu](#31-kết-nối-tới-cơ-sở-dữ-liệu)
    - [3.2. Thực thi câu lệnh SQL với JOIN](#32-thực-thi-câu-lệnh-sql-với-join)
    - [3.3. Sử dụng WHERE để lọc dữ liệu](#33-sử-dụng-where-để-lọc-dữ-liệu)
    - [3.4. Sử dụng DataAdapter và DataSet](#34-sử-dụng-dataadapter-và-dataset)
4. [Ánh xạ dữ liệu với class Model](#4-ánh-xạ-dữ-liệu-với-class-model)
    - [4.1. Định nghĩa mô hình](#41-định-nghĩa-mô-hình)
    - [4.2. Sử dụng mô hình trong truy vấn](#42-sử-dụng-mô-hình-trong-truy-vấn)
5. [Ví dụ hoàn chỉnh](#5-ví-dụ-hoàn-chỉnh)
6. [Kết luận](#6-kết-luận)
7. [Giới thiệu một số ORM phổ biến](#7-giới-thiệu-một-số-orm-phổ-biến)
    - [Bảng so sánh ORM](#bảng-so-sánh-orm)
    - [Điểm cần lưu ý](#điểm-cần-lưu-y)

---

## 1. Tổng quan về ADO.NET

### 1.1. ADO.NET là gì?

ADO.NET là một tập hợp các lớp trong .NET Framework cho phép bạn làm việc với dữ liệu trong các ứng dụng .NET. Nó cung
cấp các khả năng để kết nối, truy vấn và thao tác với cơ sở dữ liệu. ADO.NET hỗ trợ nhiều loại cơ sở dữ liệu, bao gồm
SQL Server, Oracle, MySQL, và nhiều loại khác.

### 1.2. Các thành phần chính của ADO.NET

#### **1. Connection**

**Mô tả**: `Connection` là thành phần dùng để mở và quản lý kết nối tới cơ sở dữ liệu. Nó cung cấp thông tin cần thiết
để ADO.NET có thể kết nối với cơ sở dữ liệu, như tên máy chủ, tên cơ sở dữ liệu, và thông tin xác thực.

**Cách sử dụng**:

- **Lớp chính**: `SqlConnection` cho SQL Server (có các lớp tương tự cho các cơ sở dữ liệu khác như `OleDbConnection`,
  `OracleConnection`, v.v.).
- **Cách mở kết nối**:
  ```csharp
  using (SqlConnection connection = new SqlConnection(connectionString))
  {
      connection.Open();
      // Thực hiện các thao tác với cơ sở dữ liệu
  }
  ```
- **Quản lý vòng đời**: Kết nối nên được mở khi cần và đóng lại ngay sau khi sử dụng để giải phóng tài nguyên.

#### **2. Command**

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

#### **3. DataReader**

**Mô tả**: `DataReader` là thành phần cho phép bạn đọc dữ liệu từ cơ sở dữ liệu một cách tuần tự. Nó cung cấp khả năng
đọc dữ liệu một cách nhanh chóng, nhưng không hỗ trợ lưu trữ dữ liệu để truy xuất sau này.

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

#### **4. DataAdapter**

**Mô tả**: `DataAdapter` là thành phần dùng để làm cầu nối giữa `DataSet` và cơ sở dữ liệu. Nó cho phép bạn lấy dữ liệu
từ cơ sở dữ liệu vào `DataSet` và gửi dữ liệu đã thay đổi từ `DataSet` trở lại cơ sở dữ liệu.

**Cách sử dụng**:

- **Lớp chính**: `SqlDataAdapter` cho SQL Server.
- **Cách sử dụng**:
  ```csharp
  SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM Employees", connection);
  DataSet dataSet = new DataSet();
  adapter.Fill(dataSet, "Employees"); // Lấy dữ liệu vào DataSet
  ```
- **Cập nhật dữ liệu**: Để cập nhật dữ liệu từ `DataSet` trở lại cơ sở dữ liệu, bạn cần thiết lập các `Command` cho việc
  thêm, sửa, xóa.
  ```csharp
  SqlCommandBuilder commandBuilder = new SqlCommandBuilder(adapter);
  adapter.Update(dataSet, "Employees"); // Cập nhật dữ liệu
  ```

#### **5. DataSet**

**Mô tả**: `DataSet` là một đối tượng chứa nhiều bảng dữ liệu (DataTable) và các mối quan hệ giữa chúng. Nó cho phép bạn
làm việc với dữ liệu trong bộ nhớ mà không cần phải kết nối liên tục với cơ sở dữ liệu.

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
- **Mối quan hệ giữa các bảng**: Bạn có thể thiết lập mối quan hệ giữa các bảng trong `DataSet` bằng cách sử dụng
  `DataRelation`.
  ```csharp
  DataRelation relation = new DataRelation("RelationName", parentTableColumn, childTableColumn);
  dataSet.Relations.Add(relation);
  ```

## 2. Cài đặt ADO.NET

### 2.1. Cài đặt môi trường phát triển

- Cài đặt Visual Studio hoặc một IDE hỗ trợ C#.
- Cài đặt SQL Server hoặc một cơ sở dữ liệu tương thích.

### 2.2. Thêm thư viện cần thiết

Trong Visual Studio, bạn cần thêm các thư viện cần thiết:

```csharp
using System.Data;
using System.Data.SqlClient;
```

## 3. Các bước sử dụng ADO.NET

### 3.1. Kết nối tới cơ sở dữ liệu

Để kết nối tới cơ sở dữ liệu, bạn cần tạo một đối tượng `SqlConnection`.

```csharp
string connectionString = "Data Source=server_name;Initial Catalog=database_name;User ID=user_id;Password=password;";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();
    // Thao tác với cơ sở dữ liệu
}
```

### 3.2. Thực thi câu lệnh SQL với `JOIN`

Bạn có thể sử dụng đối tượng `SqlCommand` để thực thi các câu lệnh SQL, bao gồm cả câu lệnh `JOIN` để kết

nối dữ liệu từ nhiều bảng.

```csharp
using (SqlCommand command = new SqlCommand("SELECT Employees.Name, Departments.Name FROM Employees JOIN Departments ON Employees.DepartmentId = Departments.Id", connection))
{
    using (SqlDataReader reader = command.ExecuteReader())
    {
        while (reader.Read())
        {
            Console.WriteLine($"{reader["EmployeeName"]}, {reader["DepartmentName"]}");
        }
    }
}
```

### 3.3. Sử dụng `WHERE` để lọc dữ liệu

Bạn có thể thêm điều kiện `WHERE` để lọc dữ liệu trả về.

```csharp
using (SqlCommand command = new SqlCommand("SELECT * FROM Employees WHERE Age > @Age", connection))
{
    command.Parameters.AddWithValue("@Age", 30);
    using (SqlDataReader reader = command.ExecuteReader())
    {
        while (reader.Read())
        {
            Console.WriteLine($"{reader["Name"]}, {reader["Age"]}");
        }
    }
}
```

### 3.4. Sử dụng `DataAdapter` và `DataSet`

Khi cần làm việc với nhiều bảng và thực hiện các thao tác phức tạp hơn, bạn có thể sử dụng `DataAdapter` và `DataSet`.

```csharp
SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM Employees", connection);
DataSet dataSet = new DataSet();
adapter.Fill(dataSet, "Employees");

// Lấy dữ liệu từ DataSet
DataTable employeesTable = dataSet.Tables["Employees"];
foreach (DataRow row in employeesTable.Rows)
{
    Console.WriteLine($"{row["Name"]}, {row["Position"]}");
}
```

## 4. Ánh xạ dữ liệu với class Model

### 4.1. Định nghĩa mô hình

Để ánh xạ dữ liệu từ cơ sở dữ liệu sang các đối tượng trong C#, bạn có thể định nghĩa các lớp mô hình.

```csharp
public class Employee
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
    public string Position { get; set; }
}
```

### 4.2. Sử dụng mô hình trong truy vấn

Bạn có thể sử dụng các lớp mô hình để lưu trữ dữ liệu từ cơ sở dữ liệu.

```csharp
List<Employee> employees = new List<Employee>();

using (SqlCommand command = new SqlCommand("SELECT * FROM Employees", connection))
{
    using (SqlDataReader reader = command.ExecuteReader())
    {
        while (reader.Read())
        {
            Employee employee = new Employee
            {
                Id = (int)reader["Id"],
                Name = reader["Name"].ToString(),
                Age = (int)reader["Age"],
                Position = reader["Position"].ToString()
            };
            employees.Add(employee);
        }
    }
}
```

## 5. Ví dụ hoàn chỉnh

```csharp
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;

namespace AdoNetExample
{
    public class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
        public string Position { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string connectionString = "Data Source=server_name;Initial Catalog=database_name;User ID=user_id;Password=password;";
            List<Employee> employees = new List<Employee>();

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                using (SqlCommand command = new SqlCommand("SELECT * FROM Employees", connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            Employee employee = new Employee
                            {
                                Id = (int)reader["Id"],
                                Name = reader["Name"].ToString(),
                                Age = (int)reader["Age"],
                                Position = reader["Position"].ToString()
                            };
                            employees.Add(employee);
                        }
                    }
                }
            }

            // Hiển thị thông tin nhân viên
            foreach (var employee in employees)
            {
                Console.WriteLine($"{employee.Id}: {employee.Name}, {employee.Age}, {employee.Position}");
            }
        }
    }
}
```

## 6. Kết luận

ADO.NET là một công cụ mạnh mẽ cho việc quản lý và thao tác dữ liệu trong các ứng dụng .NET. Với các thành phần như
`Connection`, `Command`, `DataReader`, `DataAdapter`, và `DataSet`, bạn có thể dễ dàng kết nối, truy vấn và thao tác với
cơ sở dữ liệu.

## 7. Giới thiệu một số ORM phổ biến

ORM (Object-Relational Mapping) là một công nghệ giúp ánh xạ các đối tượng trong ứng dụng với các bảng trong cơ sở dữ
liệu. Một số ORM phổ biến hiện nay bao gồm:

- **Entity Framework**: Là một ORM được Microsoft phát triển, hỗ trợ cả LINQ và truy vấn SQL.
- **Dapper**: Một ORM nhẹ, hiệu suất cao, dễ sử dụng.
- **NHibernate**: ORM mã nguồn mở cho .NET, nổi tiếng với khả năng ánh xạ phức tạp.

### Bảng so sánh ORM

| Tính năng          | Entity Framework | Dapper  | NHibernate |
|--------------------|------------------|---------|------------|
| Độ phức tạp        | Cao              | Thấp    | Trung bình |
| Hiệu suất          | Thấp hơn Dapper  | Rất cao | Trung bình |
| Hỗ trợ LINQ        | Có               | Không   | Có         |
| Hỗ trợ mã nguồn mở | Có               | Có      | Có         |

### Điểm cần lưu ý

- ADO.NET là một lựa chọn tuyệt vời cho những người cần kiểm soát chi tiết và hiệu suất tối ưu.
- ORM có thể làm đơn giản hóa việc phát triển, nhưng cần lưu ý về hiệu suất khi làm việc với lượng dữ liệu lớn hoặc phức
  tạp.

Hy vọng tài liệu này sẽ hữu ích cho bạn trong việc tìm hiểu và làm việc với ADO.NET trong các ứng dụng C# .NET!
