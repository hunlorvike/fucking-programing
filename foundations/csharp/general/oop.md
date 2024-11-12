# Các Nguyên Lý Cơ Bản Của OOP

## Mục Lục

1. [Encapsulation (Đóng gói)](#1-encapsulation-đóng-gói)
2. [Inheritance (Kế thừa)](#2-inheritance-kế-thừa)
   - [Sự Khác Biệt giữa Single Inheritance và Multiple Inheritance](#sự-khác-biệt-giữa-single-inheritance-và-multiple-inheritance)
3. [Polymorphism (Đa hình)](#3-polymorphism-đa-hình)
   - [Overloading (Nạp chồng phương thức)](#overloading-nạp-chồng-phương-thức)
   - [Overriding (Ghi đè phương thức)](#overriding-ghi-đè-phương-thức)
4. [Abstraction (Trừu tượng hóa)](#4-abstraction-trừu-tượng-hóa)
   - [Abstract Class (class trừu tượng)](#abstract-class-class-trừu-tượng)
   - [Interface (Giao diện)](#interface-giao-diện)
5. [Tại Sao Nên Sử Dụng OOP? Lợi Ích Của OOP](#tại-sao-nên-sử-dụng-oop-lợi-ích-của-oop)

---

### 1. **Encapsulation (Đóng gói)**

- Là việc nhóm các thuộc tính (data) và phương thức (methods) lại thành một đối tượng. Bằng cách đóng gói, dữ liệu chỉ có thể được truy cập hoặc thay đổi thông qua các phương thức của đối tượng, không thể trực tiếp truy cập từ bên ngoài.
- Điều này giúp bảo vệ dữ liệu khỏi việc thay đổi không mong muốn và dễ dàng quản lý.
- Ví dụ: Việc thiết lập và truy xuất giá trị của các thuộc tính được thực hiện thông qua getter và setter.

#### Ví dụ về Encapsulation trong Csharp

```csharp
public class Person
{
    // Biến private chỉ có thể truy cập trong class Person
    private string name;
    private int age;

    // Thuộc tính công khai để lấy và thay đổi giá trị của name
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public int Age
    {
        get { return age; }
        set
        {
            if (value >= 0) age = value; // Chỉ cho phép gán giá trị >= 0
        }
    }

    // Phương thức công khai để hiển thị thông tin
    public void DisplayInfo()
    {
        Console.WriteLine($"Name: {name}, Age: {age}");
    }
}
```

Ở ví dụ trên, các biến `name` và `age` chỉ có thể được truy cập qua các phương thức `Name` và `Age`, nhờ đó mà dữ liệu được bảo vệ và kiểm soát tốt hơn.

### 2. **Inheritance (Kế thừa)**

- Là cơ chế cho phép một class (class) kế thừa các thuộc tính và phương thức của một class khác, giúp tái sử dụng mã nguồn.

- class con (subclass) có thể kế thừa các thành phần của class cha (superclass) và có thể mở rộng hoặc thay thế chúng.

- Trong C#, một class chỉ có thể kế thừa từ một class cha duy nhất, gọi là **single inheritance**. **Multiple inheritance** (kế thừa nhiều class cha) không được hỗ trợ trực tiếp trong C#; tuy nhiên, có thể sử dụng interface để đạt được tính đa kế thừa.

#### Ví dụ về Single Inheritance

```csharp
public class Animal
{
    public void Speak()
    {
        Console.WriteLine("The animal speaks.");
    }
}

public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("The dog barks.");
    }
}

// Sử dụng:
Dog dog = new Dog();
dog.Speak(); // Kế thừa từ Animal
dog.Bark();  // Phương thức của Dog
```

#### Sự Khác Biệt giữa Single Inheritance và Multiple Inheritance

- **Single Inheritance**: class con chỉ có thể kế thừa từ một class cha duy nhất.
- **Multiple Inheritance**: class con có thể kế thừa từ nhiều class cha. C# không hỗ trợ multiple inheritance trực tiếp, nhưng có thể đạt được tính đa kế thừa qua các interface.

```csharp
public interface IFlyable
{
    void Fly();
}

public interface ISwimmable
{
    void Swim();
}

public class Duck : IFlyable, ISwimmable
{
    public void Fly() => Console.WriteLine("The duck flies.");
    public void Swim() => Console.WriteLine("The duck swims.");
}
```

### 3. **Polymorphism (Đa hình)**

- Là khả năng sử dụng một phương thức với nhiều hình thức khác nhau. Điều này có thể được thực hiện thông qua method overriding (ghi đè) và method overloading (nạp chồng).

- Polymorphism cho phép một đối tượng thuộc lớp con có thể sử dụng các phương thức của lớp cha nhưng có hành vi khác nhau.

- Ví dụ: Cùng phương thức sound() nhưng đối với lớp Dog, nó có thể là Bark, còn với lớp Cat, nó có thể là Meow.

#### Overloading (Nạp chồng phương thức)

Overloading là khả năng định nghĩa nhiều phương thức cùng tên nhưng khác tham số (số lượng hoặc kiểu tham số) trong cùng một class.

```csharp
public class MathOperations
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }
}

// Sử dụng:
MathOperations operations = new MathOperations();
Console.WriteLine(operations.Add(2, 3));         // Sử dụng Add(int, int)
Console.WriteLine(operations.Add(2.5, 3.5));     // Sử dụng Add(double, double)
```

#### Overriding (Ghi đè phương thức)

Overriding là khả năng class con ghi đè phương thức của class cha với cú pháp `override`, cho phép class con cung cấp cách triển khai riêng.

```csharp
public class Animal
{
    public virtual void Speak()
    {
        Console.WriteLine("The animal speaks.");
    }
}

public class Dog : Animal
{
    public override void Speak()
    {
        Console.WriteLine("The dog barks.");
    }
}

// Sử dụng:
Animal myDog = new Dog();
myDog.Speak(); // Sẽ gọi phương thức Speak của Dog
```

### 4. **Abstraction (Trừu tượng hóa)**

- Là quá trình che giấu các chi tiết cài đặt và chỉ hiển thị các tính năng quan trọng, giúp người dùng dễ dàng sử dụng mà không cần quan tâm đến cách thức hoạt động bên trong.

- Trừu tượng hóa có thể được thực hiện thông qua các lớp trừu tượng hoặc giao diện (interface).

- Ví dụ: Một lớp xe có thể có phương thức start() mà không cần phải biết cách thức động cơ hoạt động.

#### Abstract Class (class trừu tượng)

Abstract class là class chứa các phương thức trừu tượng (chưa được triển khai) và các phương thức đã được triển khai. Các class con kế thừa từ abstract class cần phải triển khai các phương thức trừu tượng.

```csharp
public abstract class Shape
{
    public abstract double GetArea(); // Phương thức trừu tượng

    public void Display() // Phương thức thông thường
    {
        Console.WriteLine("Displaying shape.");
    }
}

public class Circle : Shape
{
    private double radius;

    public Circle(double radius)
    {
        this.radius = radius;
    }

    public override double GetArea()
    {
        return Math.PI * radius * radius;
    }
}
```

#### Interface (Giao diện)

Interface chỉ chứa khai báo các phương thức mà không có triển khai. Các class thực thi interface phải cung cấp triển khai cho tất cả các phương thức trong interface.

```csharp
public interface IMovable
{
    void Move();
}

public class Car : IMovable
{
    public void Move()
    {
        Console.WriteLine("The car is moving.");
    }
}
```

### 5. **Tại Sao Nên Sử Dụng OOP? Lợi Ích Của OOP**

Sử dụng OOP mang lại nhiều lợi ích lớn cho quá trình phát triển phần mềm:

1. **Tái sử dụng mã**: Các class và đối tượng có thể được tái sử dụng trong các dự án khác hoặc ở các phần khác nhau của chương trình.

2. **Dễ bảo trì và mở rộng**: OOP hỗ trợ dễ dàng mở rộng mã nguồn bằng cách thêm các class mới hoặc phương thức mới mà không ảnh hưởng đến mã hiện có.

3. **Giảm thiểu lỗi và bảo mật dữ liệu**: Encapsulation giúp bảo vệ dữ liệu nhạy cảm khỏi truy cập ngoài ý muốn và giảm thiểu lỗi bằng cách giới hạn quyền truy cập.

4. **Phân cấp tổ chức tốt**: Các đối tượng và class trong OOP giúp phân chia chương trình thành các phần nhỏ dễ hiểu, dễ duy trì hơn.

5. **Dễ phát triển và bảo trì nhóm**: OOP giúp tách các phần của chương trình thành các đối tượng và class độc lập, tạo điều kiện cho các thành viên trong nhóm làm việc trên các phần khác nhau mà ít ảnh hưởng đến nhau.

6. **Hỗ trợ đa hình (Polymorphism)**: Cho phép các đối tượng hành xử khác nhau dựa trên ngữ cảnh, giúp mã linh hoạt hơn và tăng khả năng mở rộng.
