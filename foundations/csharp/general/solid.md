# SOLID Principles in Software Design

**Mục lục**

1. [Giới thiệu về SOLID](#giới-thiệu-về-solid)
2. [Single Responsibility Principle (SRP)](#1-single-responsibility-principle-srp---nguyên-lý-trách-nhiệm-duy-nhất)
3. [Open-Closed Principle (OCP)](#2-open-closed-principle-ocp---nguyên-lý-mở-rộng-đóng)
4. [Liskov Substitution Principle (LSP)](#3-liskov-substitution-principle-lsp---nguyên-lý-thay-thế-liskov)
5. [Interface Segregation Principle (ISP)](#4-interface-segregation-principle-isp---nguyên-lý-phân-tách-interface)
6. [Dependency Inversion Principle (DIP)](#5-dependency-inversion-principle-dip---nguyên-lý-đảo-ngược-phụ-thuộc)
7. [Kết luận](#kết-luận)

---

### Giới thiệu về SOLID

SOLID là tập hợp 5 nguyên lý thiết kế phần mềm quan trọng giúp làm cho mã nguồn trở nên dễ hiểu, dễ bảo trì và mở rộng hơn. Chúng bao gồm các nguyên lý: **Single Responsibility Principle (SRP)**, **Open-Closed Principle (OCP)**, **Liskov Substitution Principle (LSP)**, **Interface Segregation Principle (ISP)**, và **Dependency Inversion Principle (DIP)**. Dưới đây là giải thích chi tiết về từng nguyên lý cùng các ví dụ minh họa bằng C#.

---

### 1. **Single Responsibility Principle (SRP) - Nguyên lý trách nhiệm duy nhất**

SRP nêu rằng một lớp chỉ nên có một lý do để thay đổi, tức là nó chỉ nên chịu trách nhiệm cho một phần duy nhất của chức năng trong hệ thống. Điều này giúp cho mã dễ bảo trì, dễ đọc và dễ kiểm thử hơn, vì mỗi lớp chỉ có một vai trò.

#### Ví dụ về SRP

Giả sử chúng ta có một lớp `Employee` để quản lý thông tin nhân viên và lưu dữ liệu vào cơ sở dữ liệu. Một thiết kế không tuân thủ SRP có thể là:

```csharp
public class Employee
{
    public string Name { get; set; }
    public decimal Salary { get; set; }

    // Lưu trữ thông tin nhân viên vào database
    public void SaveToDatabase()
    {
        // Code lưu vào cơ sở dữ liệu
    }
}
```

Trong ví dụ trên, lớp `Employee` vừa chịu trách nhiệm về dữ liệu nhân viên vừa chịu trách nhiệm lưu dữ liệu vào cơ sở dữ liệu. Để tuân thủ SRP, chúng ta tách biệt chức năng lưu trữ dữ liệu vào một lớp khác:

```csharp
public class Employee
{
    public string Name { get; set; }
    public decimal Salary { get; set; }
}

public class EmployeeRepository
{
    public void SaveToDatabase(Employee employee)
    {
        // Code lưu vào cơ sở dữ liệu
    }
}
```

Giờ đây, `Employee` chỉ chịu trách nhiệm quản lý thông tin nhân viên, còn `EmployeeRepository` đảm nhiệm việc lưu trữ.

---

### 2. **Open-Closed Principle (OCP) - Nguyên lý mở rộng đóng**

OCP nói rằng các lớp, module hay hàm nên **mở để mở rộng** nhưng **đóng để chỉnh sửa**. Điều này nghĩa là bạn nên có thể thêm chức năng mới mà không cần thay đổi mã gốc, thường được thực hiện bằng cách sử dụng tính kế thừa hoặc interface.

#### Ví dụ về OCP

Giả sử chúng ta có một hệ thống tính thuế:

```csharp
public class TaxCalculator
{
    public decimal CalculateTax(string country, decimal income)
    {
        if (country == "USA")
            return income * 0.1m;
        else if (country == "UK")
            return income * 0.15m;
        else
            return income * 0.2m;
    }
}
```

Để thêm quy định tính thuế cho một quốc gia mới, chúng ta phải thay đổi lớp `TaxCalculator`. Để tuân thủ OCP, chúng ta có thể sử dụng tính đa hình:

```csharp
public interface ITaxCalculator
{
    decimal CalculateTax(decimal income);
}

public class USATaxCalculator : ITaxCalculator
{
    public decimal CalculateTax(decimal income) => income * 0.1m;
}

public class UKTaxCalculator : ITaxCalculator
{
    public decimal CalculateTax(decimal income) => income * 0.15m;
}

public class TaxCalculator
{
    public decimal CalculateTax(ITaxCalculator taxCalculator, decimal income)
    {
        return taxCalculator.CalculateTax(income);
    }
}
```

Với cách này, khi muốn thêm quy định tính thuế mới, chúng ta chỉ cần tạo lớp mới thay vì thay đổi mã gốc.

---

### 3. **Liskov Substitution Principle (LSP) - Nguyên lý thay thế Liskov**

LSP nói rằng các đối tượng của lớp con phải có thể thay thế các đối tượng của lớp cha mà không làm thay đổi tính đúng đắn của chương trình. Điều này có nghĩa là các lớp con không nên thay đổi hành vi dự kiến của lớp cha.

#### Ví dụ về LSP

Giả sử có lớp `Rectangle` và lớp `Square` kế thừa từ `Rectangle`:

```csharp
public class Rectangle
{
    public virtual int Width { get; set; }
    public virtual int Height { get; set; }

    public int Area() => Width * Height;
}

public class Square : Rectangle
{
    public override int Width
    {
        set { base.Width = base.Height = value; }
    }

    public override int Height
    {
        set { base.Width = base.Height = value; }
    }
}
```

Lớp `Square` cố gắng thay thế `Rectangle`, nhưng cách tính toán diện tích sẽ không đúng nếu sử dụng `Square` thay cho `Rectangle`. Để tuân thủ LSP, chúng ta nên tách riêng `Square` và `Rectangle` mà không kế thừa lẫn nhau.

---

### 4. **Interface Segregation Principle (ISP) - Nguyên lý phân tách interface**

ISP nói rằng một lớp không nên bị buộc phải triển khai những phương thức mà nó không sử dụng. Nói cách khác, thay vì có một interface lớn, bạn nên chia thành các interface nhỏ hơn với các phương thức cụ thể để mỗi lớp chỉ thực hiện những gì nó cần.

#### Ví dụ về ISP

Giả sử có interface `IMachine` với tất cả các chức năng của một máy phức hợp:

```csharp
public interface IMachine
{
    void Print(Document document);
    void Scan(Document document);
    void Fax(Document document);
}

public class MultiFunctionPrinter : IMachine
{
    public void Print(Document document) { /* Print */ }
    public void Scan(Document document) { /* Scan */ }
    public void Fax(Document document) { /* Fax */ }
}

public class OldPrinter : IMachine
{
    public void Print(Document document) { /* Print */ }
    public void Scan(Document document) { throw new NotImplementedException(); }
    public void Fax(Document document) { throw new NotImplementedException(); }
}
```

`OldPrinter` chỉ cần chức năng in nhưng vẫn phải triển khai các phương thức không cần thiết. Để tuân thủ ISP, chúng ta có thể tách `IMachine` thành nhiều interface nhỏ hơn:

```csharp
public interface IPrinter
{
    void Print(Document document);
}

public interface IScanner
{
    void Scan(Document document);
}

public class MultiFunctionPrinter : IPrinter, IScanner
{
    public void Print(Document document) { /* Print */ }
    public void Scan(Document document) { /* Scan */ }
}

public class OldPrinter : IPrinter
{
    public void Print(Document document) { /* Print */ }
}
```

---

### 5. **Dependency Inversion Principle (DIP) - Nguyên lý đảo ngược phụ thuộc**

DIP nói rằng các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào các abstraction (interface hoặc abstract class). Thay vì các lớp phụ thuộc trực tiếp vào nhau, chúng ta nên làm cho chúng phụ thuộc vào các abstraction, nhờ đó tăng tính linh hoạt và khả năng mở rộng của hệ thống.

#### Ví dụ về DIP

Giả sử chúng ta có một lớp `LightSwitch` để điều khiển `LightBulb`:

```csharp
public class LightBulb
{
    public void TurnOn() { /* Bật đèn */ }
    public void TurnOff() { /* Tắt đèn */ }
}

public class LightSwitch
{
    private LightBulb _lightBulb = new LightBulb();

    public void SwitchOn() => _lightBulb.TurnOn();
    public void SwitchOff() => _lightBulb.TurnOff();
}
```

Lớp `LightSwitch` phụ thuộc trực tiếp vào `LightBulb`, vi phạm DIP. Để tuân thủ DIP, chúng ta nên sử dụng abstraction:

```csharp
public interface ISwitchable
{
    void TurnOn();
    void TurnOff();
}

public class LightBulb : ISwitchable
{
    public void TurnOn() { /* Bật đèn */ }
    public void TurnOff() { /* Tắt đèn */ }
}

public class LightSwitch
{
    private ISwitchable _device;



    public LightSwitch(ISwitchable device)
    {
        _device = device;
    }

    public void SwitchOn() => _device.TurnOn();
    public void SwitchOff() => _device.TurnOff();
}
```

Giờ đây, `LightSwitch` có thể làm việc với bất kỳ thiết bị nào tuân theo `ISwitchable`, giúp mã dễ dàng mở rộng và kiểm thử hơn.

---

### Kết luận

SOLID giúp xây dựng phần mềm rõ ràng, dễ bảo trì và mở rộng linh hoạt, mang lại hiệu quả cao trong các dự án phức tạp. Việc tuân thủ các nguyên lý này không chỉ cải thiện chất lượng mã nguồn mà còn nâng cao khả năng làm việc nhóm và giảm thiểu chi phí bảo trì trong tương lai.
