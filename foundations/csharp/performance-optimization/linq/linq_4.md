## **Chương 4: LINQ to XML - "Bắt Tay" Với Dữ Liệu XML - Đơn Giản Hóa Việc Xử Lý XML**

Chào mừng bạn đến với **Chương 4: LINQ to XML**! Trong chương này, chúng ta sẽ "mở cánh cửa" vào thế giới XML và học cách dùng LINQ để "thuần hóa" dữ liệu XML, biến việc xử lý XML từ "khó nhằn" thành "dễ thở" hơn bao giờ hết.

**Phần 4: LINQ to XML - "Bắt Tay" Với Dữ Liệu XML**

**4.1. Giới thiệu LINQ to XML: XDocument, XElement, XAttribute, XNode - "Mảnh Ghép" XML Trong LINQ**

LINQ to XML là một phần "đặc biệt" của LINQ, được "thiết kế riêng" để "làm việc" với dữ liệu XML. Nó mang đến một "cách tiếp cận" trực quan, "mạnh mẽ", và "ăn ý" với C# hơn so với các phương pháp XML DOM "cổ điển".

**Các "mảnh ghép" chính trong LINQ to XML (tưởng tượng như các "viên gạch" xây dựng XML):**

-   **`XDocument`:** "Viên gạch" đại diện cho **"toàn bộ tài liệu XML"**. Nó giống như **"gốc cây"** của XML, chứa đựng mọi thứ bên trong, bao gồm cả một "phần tử gốc" (`XElement`) duy nhất, các "khai báo" XML (ví dụ: phiên bản XML), và các "ghi chú" (comment) ở "gốc" tài liệu. Bạn thường "bắt đầu" với `XDocument` khi muốn "làm việc" với một file XML hoặc chuỗi XML hoàn chỉnh.

-   **`XElement`:** "Viên gạch" đại diện cho một **"phần tử XML"** (ví dụ: `<SanPham>`, `<Ten>`, `<Gia>`). Nó có thể chứa các "thuộc tính" (`XAttribute`), các "phần tử con" (`XElement` con), và "nội dung chữ" (text content - ví dụ: "Laptop", "1500"). `XElement` là "viên gạch" cơ bản nhất để "xây dựng" cây XML.

-   **`XAttribute`:** "Viên gạch" đại diện cho một **"thuộc tính XML"** của một "phần tử" (`XElement`). Thuộc tính luôn "đi kèm" với một "phần tử" và có một "tên" và một "giá trị" (ví dụ: `MaSP="SP001"` trong `<SanPham MaSP="SP001">`).

-   **`XNode`:** "Viên gạch" "tổ tông" - là "lớp cha" chung của tất cả các "viên gạch" XML khác. `XElement`, `XDocument`, `XComment` (ghi chú XML), `XText` (văn bản XML), `XProcessingInstruction`, `XDeclaration`, `XDocumentType` đều là "con cháu" của `XNode`. Khi "vọc" LINQ to XML, bạn sẽ chủ yếu "đụng" đến `XElement` và `XAttribute`.

**"Điểm sáng" của LINQ to XML so với XML DOM "ngày xưa":**

-   **"API thân thiện" và "dễ dùng":** LINQ to XML có "bộ điều khiển" (API) rõ ràng, "hướng đối tượng", và "dễ làm quen" hơn so với DOM.
-   **"Kết hợp sức mạnh" LINQ:** "Tận dụng" "chiêu thức" LINQ (Query Syntax và Method Syntax) để "truy vấn" XML một cách "mạnh mẽ" và "linh hoạt".
-   **"Nhanh nhẹn" hơn:** LINQ to XML thường "chạy nhanh" hơn và "tiết kiệm bộ nhớ" hơn DOM trong nhiều trường hợp, đặc biệt khi "xử lý" các file XML "to bự".
-   **"Dễ dàng" tạo và "biến đổi" XML:** Việc "xây dựng" và "chỉnh sửa" XML bằng LINQ to XML rất "trực quan" và "thuận tay", dùng cú pháp C# mà bạn đã "thuần thục".
-   **"Chạy tốt" trên mọi nền tảng .NET:** LINQ to XML là "người nhà" của .NET, "chiến đấu" tốt trên cả .NET Framework và .NET Core (và .NET 5+ trở lên).

**4.2. Truy vấn, tạo, sửa đổi và xóa dữ liệu XML bằng LINQ - "Làm Chủ" XML Với LINQ**

**4.2.1. Đọc XML (Loading and Parsing XML) - "Mở Cửa" File XML**

-   **"Mở" file XML:** Dùng "chiêu" tĩnh `XDocument.Load(filePath)` để "đọc" nội dung XML từ một file và "biến" nó thành một đối tượng `XDocument` trong "bộ nhớ".

    ```csharp
    // Giả sử có file "du_lieu.xml" chứa XML
    XDocument xmlDoc = XDocument.Load("du_lieu.xml"); // "Mở" file XML

    Console.WriteLine(xmlDoc.Declaration); // In ra "khai báo" XML (nếu có, ví dụ: <?xml version="1.0" ... ?>)
    Console.WriteLine(xmlDoc.Root.Name);   // In ra "tên" của "phần tử gốc" (ví dụ: "CuaHang")
    ```

-   **"Phân tích" chuỗi XML:** Dùng "chiêu" tĩnh `XDocument.Parse(xmlString)` để "biến" một chuỗi XML thành một đối tượng `XDocument`.

    ```csharp
    string xmlChuoi = @"<SanPham>
                            <Ten>Laptop</Ten>
                            <Gia>1500</Gia>
                         </SanPham>"; // Chuỗi XML

    XDocument xmlDocFromString = XDocument.Parse(xmlChuoi); // "Phân tích" chuỗi XML

    Console.WriteLine(xmlDocFromString.Root.Element("Ten").Value); // In ra "nội dung" của "phần tử" <Ten> (kết quả: "Laptop")
    ```

**4.2.2. Truy vấn XML (Querying XML) - "Hỏi Han" Dữ Liệu XML**

LINQ to XML "cho phép" bạn dùng các "chiêu" LINQ quen thuộc để "truy vấn" dữ liệu XML. Các "chiêu" quan trọng khi "hỏi han" XML bao gồm:

-   **`Descendants(elementName)`:** "Lấy" **tất cả** các "phần tử con cháu" (ở bất kỳ "tầng lớp" nào) có "tên" là `elementName`.
-   **`Elements(elementName)`:** "Lấy" các "phần tử con trực tiếp" (chỉ "tầng lớp" con ruột) có "tên" là `elementName`.
-   **`Element(elementName)`:** "Lấy" "phần tử con trực tiếp" **đầu tiên** có "tên" là `elementName`.
-   **`Attributes(attributeName)`:** "Lấy" **tất cả** các "thuộc tính" có "tên" là `attributeName` của một "phần tử".
    -   **`Attribute(attributeName)`:** "Lấy" "thuộc tính" **đầu tiên** có "tên" là `attributeName` của một "phần tử".
    -   **`Value`:** "Lấy" "giá trị văn bản" bên trong một "phần tử" hoặc "thuộc tính".

**Ví dụ "truy vấn" (giả sử `xmlDoc` đã được "mở" từ file hoặc "phân tích" từ chuỗi):**

```csharp
// Giả sử xmlDoc có "cấu trúc" XML như sau:
/*
<CuaHang>
  <SanPham MaSP="SP001">
    <Ten>Điện thoại</Ten>
    <Gia>1000</Gia>
    <DanhMuc>Điện tử</DanhMuc>
  </SanPham>
  <SanPham MaSP="SP002">
    <Ten>Sách</Ten>
    <Gia>20</Gia>
    <DanhMuc>Sách</DanhMuc>
  </SanPham>
  <SanPham MaSP="SP003">
    <Ten>Laptop</Ten>
    <Gia>1500</Gia>
    <DanhMuc>Điện tử</DanhMuc>
  </SanPham>
</CuaHang>
*/

// 1. "Lấy" danh sách "tên sản phẩm" của tất cả sản phẩm có "danh mục" là "Điện tử" (Query Syntax)
var sanPhamDienTuQuery = from sp in xmlDoc.Descendants("SanPham") // "Soi" tất cả "phần tử con cháu" <SanPham>
                         where sp.Element("DanhMuc").Value == "Điện tử" // "Lọc": chỉ lấy <SanPham> nào có <DanhMuc> là "Điện tử"
                         select sp.Element("Ten").Value; // "Chọn": lấy "nội dung" của <Ten> bên trong <SanPham>

Console.WriteLine("Sản phẩm điện tử (Query Syntax):");
foreach (var tenSP in sanPhamDienTuQuery) // Duyệt qua kết quả
{
    Console.WriteLine($"- {tenSP}"); // In ra tên sản phẩm (ví dụ: - Điện thoại, - Laptop)
}

// 2. "Lấy" danh sách "tên sản phẩm" và "giá" của tất cả sản phẩm (Method Syntax)
var thongTinSanPhamMethod = xmlDoc.Descendants("SanPham") // "Soi" tất cả "phần tử con cháu" <SanPham>
                                 .Select(sp => new // "Chọn" và "biến hình" thành kiểu "vô danh"
                                 {
                                     TenSP = sp.Element("Ten").Value, // "Lấy" "nội dung" <Ten> làm thuộc tính TenSP
                                     GiaSP = decimal.Parse(sp.Element("Gia").Value) // "Lấy" "nội dung" <Gia> và "biến" thành số decimal, làm thuộc tính GiaSP
                                 });

Console.WriteLine("\nThông tin sản phẩm (Method Syntax):");
foreach (var spInfo in thongTinSanPhamMethod) // Duyệt qua kết quả
{
    Console.WriteLine($"- Tên: {spInfo.TenSP}, Giá: {spInfo.GiaSP}"); // In ra thông tin sản phẩm (ví dụ: - Tên: Điện thoại, Giá: 1000)
}

// 3. "Lấy" "thuộc tính" MaSP của "phần tử" <SanPham> đầu tiên
string maSP_SP_DauTien = xmlDoc.Descendants("SanPham").First().Attribute("MaSP").Value; // "Soi" <SanPham> đầu tiên, "lấy" "thuộc tính" MaSP, "lấy" "giá trị" thuộc tính
Console.WriteLine($"\nMã sản phẩm của sản phẩm đầu tiên: {maSP_SP_DauTien}"); // Kết quả: SP001

// 4. "Đếm" số lượng sản phẩm có "giá" lớn hơn 500
int soLuongSP_GiaHon500 = xmlDoc.Descendants("SanPham").Count(sp => decimal.Parse(sp.Element("Gia").Value) > 500); // "Soi" <SanPham>, "đếm" những <SanPham> có <Gia> > 500
Console.WriteLine($"\nSố lượng sản phẩm giá > 500: {soLuongSP_GiaHon500}"); // Kết quả: 2 (Điện thoại và Laptop có giá > 500)
```

**4.2.3. Tạo XML (Creating XML) - "Xây Dựng" XML Từ Đầu**

Bạn có thể "tự tay" "xây dựng" một "tài liệu XML" mới một cách "dễ dàng" bằng cách dùng các "công cụ xây dựng" (constructor) của `XDocument`, `XElement`, và `XAttribute`.

```csharp
// "Xây" XML document mới "từ đầu"
XDocument newXmlDoc = new XDocument( // Tạo "tài liệu" XDocument mới
    new XDeclaration("1.0", "utf-8", "yes"), // "Khai báo" XML (version, encoding, standalone)
    new XComment("Đây là tài liệu XML ví dụ"), // "Ghi chú" ở "gốc" tài liệu
    new XElement("SinhViens", // "Phần tử gốc" <SinhViens>
        new XElement("SinhVien", // "Phần tử con" <SinhVien>
            new XAttribute("MaSV", "SV001"), // "Thuộc tính" MaSV="SV001" cho <SinhVien>
            new XElement("Ten", "Nguyen Van A"), // "Phần tử con" <Ten> bên trong <SinhVien>
            new XElement("Tuoi", "20")          // "Phần tử con" <Tuoi> bên trong <SinhVien>
        ),
        new XElement("SinhVien", // Thêm một "phần tử con" <SinhVien> nữa
            new XAttribute("MaSV", "SV002"),
            new XElement("Ten", "Tran Thi B"),
            new XElement("Tuoi", "21")
        )
    )
);

Console.WriteLine("\nXML mới được tạo:");
Console.WriteLine(newXmlDoc.ToString()); // "Biến" XML document thành chuỗi và in ra
```

**4.2.4. Sửa đổi XML (Modifying XML) - "Chỉnh Trang" XML**

LINQ to XML cung cấp các "chiêu" để "chỉnh sửa" "kiến trúc" và "nội dung" của XML:

-   **`Element(elementName).SetValue(newValue)`:** "Thay đổi" "nội dung văn bản" của một "phần tử".
-   **`Attribute(attributeName).SetValue(newValue)`:** "Thay đổi" "giá trị" của một "thuộc tính".
-   **`Add(newContent)`:** "Thêm" "nội dung mới" (phần tử, thuộc tính, ghi chú, v.v.) vào một "phần tử".
-   **`Remove()`:** "Xóa" một "phần tử" hoặc "thuộc tính".
    -   **`ReplaceNodes(newContent)`:** "Thay thế" **toàn bộ** các "phần tử con" của một "phần tử" bằng "nội dung mới".
    -   **`ReplaceAttributes(newAttributes)`:** "Thay thế" **toàn bộ** các "thuộc tính" của một "phần tử" bằng các "thuộc tính mới".

**Ví dụ "chỉnh sửa" XML (tiếp tục với `xmlDoc` đã "mở"):**

```csharp
// 1. "Thay đổi" "giá" của sản phẩm có "tên" là "Sách" thành 25
XElement sanPhamSach = xmlDoc.Descendants("SanPham").FirstOrDefault(sp => sp.Element("Ten").Value == "Sách"); // "Tìm" <SanPham> có <Ten> là "Sách"
if (sanPhamSach != null) // Nếu "tìm" thấy
{
    sanPhamSach.Element("Gia").SetValue("25"); // "Thay đổi" "nội dung" của <Gia> thành "25"
}

// 2. "Thêm" một "thuộc tính" mới "XuatXu" vào sản phẩm "Laptop"
XElement sanPhamLaptop = xmlDoc.Descendants("SanPham").FirstOrDefault(sp => sp.Element("Ten").Value == "Laptop"); // "Tìm" <SanPham> có <Ten> là "Laptop"
if (sanPhamLaptop != null) // Nếu "tìm" thấy
{
    sanPhamLaptop.Add(new XAttribute("XuatXu", "Trung Quốc")); // "Thêm" "thuộc tính" XuatXu="Trung Quốc" vào <SanPham>
}

// 3. "Xóa" sản phẩm có "mã" "SP002"
XElement sanPhamCanXoa = xmlDoc.Descendants("SanPham").FirstOrDefault(sp => sp.Attribute("MaSP").Value == "SP002"); // "Tìm" <SanPham> có "thuộc tính" MaSP="SP002"
if (sanPhamCanXoa != null) // Nếu "tìm" thấy
{
    sanPhamCanXoa.Remove(); // "Xóa" "phần tử" <SanPham> đó
}

Console.WriteLine("\nXML sau khi sửa đổi:");
Console.WriteLine(xmlDoc.ToString()); // In ra XML đã "tân trang"
```

**4.2.5. Xóa XML (Deleting XML) - "Dọn Dẹp" XML**

Như bạn thấy trong ví dụ "chỉnh sửa", bạn có thể dùng `Remove()` để "xóa sổ" các "phần tử" hoặc "thuộc tính" XML không mong muốn.

**4.3. Đọc và ghi dữ liệu XML từ/đến file - "Lưu Giữ" Và "Mở Lại" XML**

Chúng ta đã biết cách "mở" file XML bằng `XDocument.Load(filePath)`. Để **"ghi" XML trở lại file**, bạn dùng "chiêu" `XDocument.Save(filePath)`.

```csharp
// "Lưu" XML document đã "tân trang" vào file "du_lieu_da_sua.xml"
xmlDoc.Save("du_lieu_da_sua.xml"); // "Lưu" XML vào file

Console.WriteLine("\nĐã lưu XML đã sửa đổi vào file 'du_lieu_da_sua.xml'");
```

**Ngoài ra, bạn có thể "biến" `XDocument` thành chuỗi XML bằng "chiêu" `XDocument.ToString()` (như đã dùng trong các ví dụ trên).**

**Tổng Kết Chương 4:**

-   Bạn đã "làm quen" với LINQ to XML và các "viên gạch" cơ bản: `XDocument`, `XElement`, `XAttribute`, `XNode`.
-   Học cách "mở" XML từ file và chuỗi.
    -   "Nắm vững" cách "truy vấn" XML bằng các "chiêu" LINQ (Query Syntax và Method Syntax).
    -   Biết cách "xây" XML document mới "từ tay".
    -   Học cách "chỉnh sửa" và "dọn dẹp" dữ liệu XML.
    -   Biết cách "lưu" XML document trở lại file.

LINQ to XML là một "công cụ" rất "lợi hại" để "làm chủ" XML trong .NET. Nó giúp bạn "thao tác" với XML một cách "trực quan", "hiệu quả", và "tận dụng" được "sức mạnh" của LINQ.

**Bài Tập "Thực Hành XML":**

1.  Tạo một file XML chứa thông tin về sách (tên sách, tác giả, giá, nhà xuất bản).
2.  "Mở" file XML này bằng LINQ to XML.
3.  Sử dụng "chiêu" LINQ để:
    -   "Lấy" danh sách "tên sách" của tất cả sách có "giá" "cao hơn" một giá trị nào đó do bạn chọn.
    -   "Lấy" danh sách "tên sách" và "nhà xuất bản" của tất cả sách được "xuất bản" bởi một "nhà xuất bản" cụ thể.
    -   "Tính tổng" "giá trị" của tất cả các sách.
4.  "Thêm" một cuốn sách mới vào XML document.
5.  "Chỉnh sửa" "giá" của một cuốn sách cụ thể trong XML document.
6.  "Xóa" một cuốn sách khỏi XML document.
7.  "Lưu" XML document đã "tân trang" trở lại file.

**Bước Tiếp Theo:**

Chúng ta sẽ "tiến thẳng" đến **Chương 5: LINQ to SQL/Entities (LINQ to Database) - "Bắt Nhịp" Với Cơ Sở Dữ Liệu**. Chúng ta sẽ "khám phá" cách sử dụng LINQ để "truy vấn" và "thao tác" với dữ liệu trong cơ sở dữ liệu quan hệ.

Bạn có câu hỏi nào về LINQ to XML này không? Hãy cứ "hỏi han" nhé!
