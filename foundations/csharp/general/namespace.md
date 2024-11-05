Trong ngôn ngữ C#, các **namespace cốt lõi** cung cấp những lớp, phương thức, và kiểu dữ liệu cơ bản cho phép bạn xây dựng ứng dụng. Các namespace này bao gồm các thư viện chứa chức năng cho thao tác dữ liệu, xử lý file, kết nối mạng, quản lý bộ nhớ và nhiều chức năng khác.

Dưới đây là các namespace cốt lõi của C# và .NET Framework mà bạn sẽ thường xuyên làm việc:

### 1. `System`

- **Mô tả**: Namespace nền tảng nhất trong .NET, chứa các lớp cơ bản và kiểu dữ liệu thiết yếu như `Int32`, `String`, `DateTime`, `Array`, và các ngoại lệ.
- **Các lớp chính**:
  - `System.Object`: Lớp cơ sở của mọi lớp trong .NET.
  - `System.String`: Đại diện cho chuỗi ký tự.
  - `System.DateTime`: Quản lý và xử lý ngày giờ.
  - `System.Exception`: Cơ sở cho tất cả các ngoại lệ (exceptions).

### 2. `System.Collections` và `System.Collections.Generic`

- **Mô tả**: Cung cấp các lớp và giao diện để làm việc với tập hợp dữ liệu như danh sách, từ điển, ngăn xếp, và hàng đợi.
- **Các lớp chính**:
  - `System.Collections.ArrayList`, `System.Collections.Hashtable` (các lớp không generic).
  - `System.Collections.Generic.List<T>`, `System.Collections.Generic.Dictionary<TKey, TValue>` (các lớp generic).

### 3. `System.IO`

- **Mô tả**: Cung cấp các lớp cho việc thao tác với file và dữ liệu đầu vào/đầu ra (I/O) cơ bản.
- **Các lớp chính**:
  - `System.IO.File`: Thao tác với các file.
  - `System.IO.Stream`, `System.IO.FileStream`, `System.IO.MemoryStream`: Quản lý luồng dữ liệu.
  - `System.IO.StreamReader`, `System.IO.StreamWriter`: Đọc và ghi dữ liệu dạng text.

### 4. `System.Text`

- **Mô tả**: Cung cấp các lớp để xử lý chuỗi và mã hóa văn bản.
- **Các lớp chính**:
  - `System.Text.StringBuilder`: Xây dựng chuỗi với hiệu suất cao.
  - `System.Text.Encoding`: Xử lý mã hóa ký tự (như UTF-8, ASCII).

### 5. `System.Threading`

- **Mô tả**: Hỗ trợ các tính năng liên quan đến đa luồng và xử lý bất đồng bộ.
- **Các lớp chính**:
  - `System.Threading.Thread`: Đại diện cho một luồng (thread) riêng biệt.
  - `System.Threading.Tasks.Task`: Hỗ trợ lập trình bất đồng bộ.
  - `System.Threading.Mutex`, `System.Threading.Semaphore`: Quản lý đồng bộ hóa giữa các luồng.

### 6. `System.Net`

- **Mô tả**: Cung cấp các lớp cho kết nối mạng và truyền dữ liệu qua mạng.
- **Các lớp chính**:
  - `System.Net.WebClient`: Tải xuống hoặc tải lên dữ liệu qua HTTP.
  - `System.Net.Http.HttpClient`: Tương tác với các API HTTP hiện đại.
  - `System.Net.Sockets.Socket`: Làm việc với giao thức TCP/IP ở mức thấp.

### 7. `System.Data`

- **Mô tả**: Hỗ trợ làm việc với dữ liệu, đặc biệt là dữ liệu liên quan đến cơ sở dữ liệu.
- **Các lớp chính**:
  - `System.Data.DataSet`, `System.Data.DataTable`: Quản lý dữ liệu dạng bảng.
  - `System.Data.SqlClient.SqlConnection`, `System.Data.SqlClient.SqlCommand`: Kết nối và tương tác với cơ sở dữ liệu SQL Server.

### 8. `System.Linq`

- **Mô tả**: Cung cấp các phương thức LINQ (Language-Integrated Query) để truy vấn dữ liệu từ các tập hợp.
- **Các lớp chính**:
  - `System.Linq.Enumerable`: Chứa các phương thức mở rộng như `Where`, `Select`, `OrderBy` cho tập hợp.

### 9. `System.Xml`

- **Mô tả**: Cung cấp các lớp để làm việc với XML.
- **Các lớp chính**:
  - `System.Xml.XmlDocument`: Đọc và ghi dữ liệu XML dưới dạng DOM.
  - `System.Xml.XmlReader`, `System.Xml.XmlWriter`: Đọc và ghi dữ liệu XML một cách hiệu quả.

### 10. `System.Drawing`

- **Mô tả**: Cung cấp các lớp cho việc vẽ đồ họa, xử lý ảnh và tạo hình ảnh bitmap.
- **Các lớp chính**:
  - `System.Drawing.Bitmap`: Làm việc với ảnh bitmap.
  - `System.Drawing.Graphics`: Cung cấp phương thức vẽ đồ họa.

### 11. `System.Runtime`

- **Mô tả**: Chứa các lớp liên quan đến thời gian chạy, bao gồm việc xử lý các ứng dụng động, nạp các module và thư viện.
- **Các lớp chính**:
  - `System.Runtime.InteropServices`: Tích hợp với mã không thuộc .NET.
  - `System.Runtime.Serialization`: Hỗ trợ cho việc tuần tự hóa (serialization) các đối tượng.

### 12. `System.Security`

- **Mô tả**: Hỗ trợ bảo mật và mã hóa.
- **Các lớp chính**:
  - `System.Security.Cryptography`: Chứa các lớp cho mã hóa và giải mã.
  - `System.Security.Permissions`: Quản lý quyền truy cập và bảo mật.

### 13. `System.ComponentModel`

- **Mô tả**: Hỗ trợ các thành phần và điều khiển được thiết kế, bao gồm hỗ trợ cho việc dữ liệu binding.
- **Các lớp chính**:
  - `System.ComponentModel.Component`: Lớp cơ sở cho các thành phần không phải giao diện người dùng.
  - `System.ComponentModel.INotifyPropertyChanged`: Được sử dụng trong việc binding dữ liệu.

### 14. `System.Reflection`

- **Mô tả**: Cung cấp khả năng xem xét thông tin về các kiểu trong thời gian chạy và thực hiện các thao tác như khởi tạo đối tượng, gọi phương thức.
- **Các lớp chính**:
  - `System.Reflection.Assembly`: Tải và lấy thông tin về các assembly.
  - `System.Reflection.MethodInfo`, `System.Reflection.PropertyInfo`: Truy xuất thông tin về các phương thức và thuộc tính của lớp.

### 15. `System.Globalization`

- **Mô tả**: Hỗ trợ cho các ứng dụng toàn cầu hóa, quản lý thông tin văn hóa, định dạng số, ngày giờ và chuỗi.
- **Các lớp chính**:
  - `System.Globalization.CultureInfo`: Thông tin văn hóa.
  - `System.Globalization.DateTimeFormatInfo`, `System.Globalization.NumberFormatInfo`: Định dạng cho ngày giờ và số.
