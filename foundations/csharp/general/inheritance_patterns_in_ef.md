# Các Kiểu Kế Thừa trong Entity Framework

## Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Table per Hierarchy (TPH)](#1-table-per-hierarchy-tph)
   - [Định nghĩa](#định-nghĩa)
   - [Cấu trúc](#cấu-trúc)
   - [Ví dụ](#ví-dụ)
   - [Câu SQL tạo bảng](#câu-sql-tạo-bảng)
   - [Cấu trúc Bảng](#cấu-trúc-bảng)
   - [Ưu điểm](#ưu-điểm)
   - [Nhược điểm](#nhược-điểm)
3. [Table per Type (TPT)](#2-table-per-type-tpt)
   - [Định nghĩa](#định-nghĩa-1)
   - [Cấu trúc](#cấu-trúc-1)
   - [Ví dụ](#ví-dụ-1)
   - [Câu SQL tạo bảng](#câu-sql-tạo-bảng-1)
   - [Cấu trúc Bảng](#cấu-trúc-bảng-1)
   - [Ưu điểm](#ưu-điểm-1)
   - [Nhược điểm](#nhược-điểm-1)
4. [Table per Concrete Class (TPC)](#3-table-per-concrete-class-tpc)
   - [Định nghĩa](#định-nghĩa-2)
   - [Cấu trúc](#cấu-trúc-2)
   - [Ví dụ](#ví-dụ-2)
   - [Câu SQL tạo bảng](#câu-sql-tạo-bảng-2)
   - [Cấu trúc Bảng](#cấu-trúc-bảng-2)
   - [Ưu điểm](#ưu-điểm-2)
   - [Nhược điểm](#nhược-điểm-2)
5. [Kết Luận](#kết-luận)

---

## Giới Thiệu

Tài liệu này mô tả chi tiết hơn về các kiểu kế thừa trong Entity Framework, bao gồm `Table per Hierarchy (TPH)`, `Table per Type (TPT)`, và `Table per Concrete Class (TPC)`. Mỗi kiểu kế thừa sẽ được giải thích với định nghĩa, ưu điểm, nhược điểm và ví dụ cụ thể, bao gồm cả các câu SQL tạo bảng tương ứng.

---

## 1. Table per Hierarchy (TPH)

### Định nghĩa

Trong mô hình TPH, tất cả các entity con được lưu trữ trong một bảng duy nhất. Một cột trong bảng này xác định loại entity (loại của lớp).

### Cấu trúc

- Một bảng duy nhất lưu trữ tất cả các thuộc tính của cả lớp cha và lớp con.
- Có một cột phân biệt loại entity con.

### Ví dụ

Giả sử chúng ta có một lớp cha `Animal` và hai lớp con `Dog` và `Cat`.

```csharp
public class Animal
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string AnimalType { get; set; } // Cột xác định loại entity
}

public class Dog : Animal
{
    public string Breed { get; set; }
}

public class Cat : Animal
{
    public bool IsIndoor { get; set; }
}
```

### Câu SQL tạo bảng

```sql
CREATE TABLE Animals (
    Id INT PRIMARY KEY,
    Name NVARCHAR(100),
    AnimalType NVARCHAR(50),
    Breed NVARCHAR(100), -- Cột cho Dog
    IsIndoor BIT -- Cột cho Cat
);
```

### Cấu trúc Bảng

| Id  | Name     | AnimalType | Breed  | IsIndoor |
| --- | -------- | ---------- | ------ | -------- |
| 1   | Max      | Dog        | Beagle | NULL     |
| 2   | Whiskers | Cat        | NULL   | 1        |

### Ưu điểm

- Giảm số lượng bảng trong cơ sở dữ liệu.
- Dễ dàng truy vấn tất cả các loại entity.

### Nhược điểm

- Có thể gây ra việc lãng phí không gian do cột không sử dụng (NULL) cho các entity con.
- Khó khăn trong việc bảo trì và mở rộng nếu có nhiều thuộc tính riêng biệt.

---

## 2. Table per Type (TPT)

### Định nghĩa

Trong mô hình TPT, mỗi entity con sẽ có bảng riêng và các bảng này sẽ có quan hệ với bảng cha. Bảng cha chứa các thuộc tính chung, trong khi bảng con chứa các thuộc tính riêng.

### Cấu trúc

- Một bảng cho lớp cha và một bảng cho mỗi lớp con.
- Các bảng con có khóa ngoại tham chiếu đến bảng cha.

### Ví dụ

Tiếp tục với ví dụ trên, chúng ta có cấu trúc như sau:

```csharp
public class Animal
{
    public int Id { get; set; }
    public string Name { get; set; }
}

public class Dog : Animal
{
    public string Breed { get; set; }
}

public class Cat : Animal
{
    public bool IsIndoor { get; set; }
}
```

### Câu SQL tạo bảng

```sql
CREATE TABLE Animals (
    Id INT PRIMARY KEY,
    Name NVARCHAR(100)
);

CREATE TABLE Dogs (
    Id INT PRIMARY KEY,
    Breed NVARCHAR(100),
    FOREIGN KEY (Id) REFERENCES Animals(Id) -- Khóa ngoại đến bảng Animals
);

CREATE TABLE Cats (
    Id INT PRIMARY KEY,
    IsIndoor BIT,
    FOREIGN KEY (Id) REFERENCES Animals(Id) -- Khóa ngoại đến bảng Animals
);
```

### Cấu trúc Bảng

**Bảng Animals**
| Id | Name |
|----|---------|
| 1 | Max |
| 2 | Whiskers|

**Bảng Dogs**
| Id | Breed |
|----|-----------|
| 1 | Beagle |

**Bảng Cats**
| Id | IsIndoor |
|----|----------|
| 2 | 1 |

### Ưu điểm

- Dễ dàng mở rộng thêm thuộc tính riêng cho từng loại entity mà không ảnh hưởng đến các entity khác.
- Tránh việc lãng phí không gian do không cần cột NULL.

### Nhược điểm

- Tăng số lượng bảng và phức tạp trong việc truy vấn.
- Có thể làm giảm hiệu suất do cần phải thực hiện nhiều phép JOIN khi truy vấn dữ liệu.

---

## 3. Table per Concrete Class (TPC)

### Định nghĩa

Trong mô hình TPC, mỗi lớp cụ thể (không bao gồm lớp cha) sẽ có bảng riêng. Không có quan hệ kế thừa giữa chúng trong cơ sở dữ liệu.

### Cấu trúc

- Mỗi lớp con có bảng riêng và bảng này chứa tất cả các thuộc tính của lớp con.
- Không có bảng cha trong cơ sở dữ liệu.

### Ví dụ

Tiếp tục với ví dụ `Animal`, chúng ta có thể tạo các lớp con như sau:

```csharp
public class Dog
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Breed { get; set; }
}

public class Cat
{
    public int Id { get; set; }
    public string Name { get; set; }
    public bool IsIndoor { get; set; }
}
```

### Câu SQL tạo bảng

```sql
CREATE TABLE Dogs (
    Id INT PRIMARY KEY,
    Name NVARCHAR(100),
    Breed NVARCHAR(100)
);

CREATE TABLE Cats (
    Id INT PRIMARY KEY,
    Name NVARCHAR(100),
    IsIndoor BIT
);
```

### Cấu trúc Bảng

**Bảng Dogs**
| Id | Name | Breed |
|----|---------|-----------|
| 1 | Max | Beagle |

**Bảng Cats**
| Id | Name | IsIndoor |
|----|---------|----------|
| 2 | Whiskers| 1 |

### Ưu điểm

- Mỗi lớp có thể được thiết kế riêng biệt mà không cần quan tâm đến các lớp khác.
- Không có cột NULL do không cần cột chung.

### Nhược điểm

- Không dễ dàng truy vấn chung giữa các loại entity.
- Khó khăn trong việc chia sẻ các thuộc tính chung giữa các lớp con.

---

## Kết Luận

Việc chọn kiểu kế thừa trong Entity Framework phụ thuộc vào yêu cầu của ứng dụng và cách bạn muốn quản lý dữ liệu. Mỗi kiểu kế thừa đều có những ưu điểm và nhược điểm riêng, do đó, cần cân nhắc kỹ lưỡng trước khi quyết định áp dụng cho dự án của mình. Việc sử dụng đúng kiểu kế thừa sẽ giúp tối ưu hóa cấu trúc cơ sở dữ liệu và cải thiện hiệu suất của ứng dụng.
