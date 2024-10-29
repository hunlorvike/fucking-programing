## Các Nguyên Lý Cơ Bản Của OOP

### 1. **Encapsulation (Đóng gói)**

Encapsulation là nguyên lý đóng gói dữ liệu và các phương thức thao tác dữ liệu vào trong một lớp, để ẩn chi tiết triển khai và chỉ cung cấp các phương thức truy cập công khai (public) khi cần. Điều này giúp bảo vệ dữ liệu khỏi sự can thiệp hoặc sửa đổi không mong muốn từ bên ngoài lớp.

#### Ví dụ về Encapsulation trong C#

```csharp
public class Person
{
    // Biến private chỉ có thể truy cập trong lớp Person
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

Inheritance là cơ chế cho phép một lớp (gọi là lớp con) thừa hưởng các thuộc tính và phương thức của một lớp khác (lớp cha). Điều này giúp tránh lặp lại mã nguồn và tạo ra các hệ thống phân cấp lớp.

Trong C#, một lớp chỉ có thể kế thừa từ một lớp cha duy nhất, gọi là **single inheritance**. **Multiple inheritance** (kế thừa nhiều lớp cha) không được hỗ trợ trực tiếp trong C#; tuy nhiên, có thể sử dụng interface để đạt được tính đa kế thừa.

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

- **Single Inheritance**: Lớp con chỉ có thể kế thừa từ một lớp cha duy nhất.
- **Multiple Inheritance**: Lớp con có thể kế thừa từ nhiều lớp cha. C# không hỗ trợ multiple inheritance trực tiếp, nhưng có thể đạt được tính đa kế thừa qua các interface.

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

Polymorphism cho phép đối tượng có thể hành xử khác nhau tùy vào ngữ cảnh. Có hai loại polymorphism trong C#: **Overloading (nạp chồng)** và **Overriding (ghi đè)**.

#### Overloading (Nạp chồng phương thức)

Overloading là khả năng định nghĩa nhiều phương thức cùng tên nhưng khác tham số (số lượng hoặc kiểu tham số) trong cùng một lớp.

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

Overriding là khả năng lớp con ghi đè phương thức của lớp cha với cú pháp `override`, cho phép lớp con cung cấp cách triển khai riêng.

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

Abstraction là khái niệm che giấu các chi tiết cài đặt và chỉ hiển thị các tính năng chính. Trong C#, trừu tượng hóa được thực hiện qua các lớp abstract và interface.

#### Abstract Class (Lớp trừu tượng)

Abstract class là lớp chứa các phương thức trừu tượng (chưa được triển khai) và các phương thức đã được triển khai. Các lớp con kế thừa từ abstract class cần phải triển khai các phương thức trừu tượng.

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

Interface chỉ chứa khai báo các phương thức mà không có triển khai. Các lớp thực thi interface phải cung cấp triển khai cho tất cả các phương thức trong interface.

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

## Tại Sao Nên Sử Dụng OOP? Lợi Ích Của OOP

Sử dụng OOP mang lại nhiều lợi ích lớn cho quá trình phát triển phần mềm:

1. **Tái sử dụng mã**: Các lớp và đối tượng có thể được tái sử dụng trong các dự án khác hoặc ở các phần khác nhau của chương trình.

2. **Dễ bảo trì và mở rộng**: OOP hỗ trợ dễ dàng mở rộng mã nguồn bằng cách thêm các lớp mới hoặc phương thức mới mà không ảnh hưởng đến mã hiện có.

3. **Giảm thiểu lỗi và bảo mật dữ liệu**: Encapsulation giúp bảo vệ dữ liệu nhạy cảm khỏi truy cập ngoài ý muốn và giảm thiểu lỗi bằng cách giới hạn quyền truy cập.

4. **Phân cấp tổ chức tốt**: Các đối tượng và lớp trong OOP giúp phân chia chương trình thành các phần nhỏ dễ hiểu, dễ duy trì hơn.

5. **Dễ phát triển và bảo trì nhóm**: OOP giúp tách các phần của chương trình thành các đối tượng và lớp độc lập, tạo điều kiện cho các thành viên trong nhóm làm việc trên các phần khác nhau mà ít ảnh hưởng đến nhau.

6. **Hỗ trợ đa hình (Polymorphism)**: Cho phép các đối tượng hành xử khác nhau dựa trên ngữ cảnh, giúp mã linh hoạt hơn và tăng khả năng mở rộng.

Những lợi ích này làm cho OOP trở thành một trong những mô hình lập trình phổ biến và hiệu quả nhất trong phát triển phần mềm ngày nay.
