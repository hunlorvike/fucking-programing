## Lifetime trong C# và .NET

**Lifetime** của một đối tượng hoặc thành phần trong ứng dụng C#/.NET đề cập đến thời gian tồn tại của nó trong bộ nhớ, từ lúc được tạo ra đến lúc bị giải phóng. Quản lý lifetime đúng cách giúp tối ưu hóa hiệu suất và tránh rò rỉ bộ nhớ trong ứng dụng.

### Mục lục

1. [Lifetime trong Dependency Injection của ASP.NET Core](#di-lifetime)
2. [Lifetime của đối tượng trong Garbage Collection (GC)](#gc-lifetime)
3. [Static và Non-static Lifetime](#static-lifetime)
4. [Lifetime trong Event và Delegate](#event-lifetime)
5. [Lifetime trong Task và Async/Await](#task-lifetime)
6. [Lifetime trong File Handling và I/O](#file-lifetime)
7. [Disposable Pattern và Quản lý Lifetime thủ công](#disposable-lifetime)

### <a name="di-lifetime"></a>1. Lifetime trong Dependency Injection của ASP.NET Core

Trong ASP.NET Core, **Dependency Injection (DI)** là một cơ chế quản lý và cung cấp các phụ thuộc của một lớp hoặc thành phần. Có ba kiểu lifetime phổ biến trong DI:

#### a. Singleton

- **Định nghĩa**: Khởi tạo một lần và dùng chung cho toàn bộ ứng dụng.
- **Sử dụng**: Cho dịch vụ chia sẻ dữ liệu hoặc trạng thái toàn cục.
- **Đăng ký**: `.AddSingleton<TService, TImplementation>()`

#### b. Scoped

- **Định nghĩa**: Tạo mới mỗi yêu cầu HTTP và chỉ tồn tại trong suốt vòng đời của yêu cầu đó.
- **Sử dụng**: Phù hợp với các dịch vụ xử lý dữ liệu theo từng yêu cầu (session, database).
- **Đăng ký**: `.AddScoped<TService, TImplementation>()`

#### c. Transient

- **Định nghĩa**: Tạo mới mỗi khi có yêu cầu dịch vụ.
- **Sử dụng**: Phù hợp với các dịch vụ không giữ trạng thái và cần nhiều thể hiện độc lập.
- **Đăng ký**: `.AddTransient<TService, TImplementation>()`

#### Lưu ý khi sử dụng DI Lifetime

- **Không inject dịch vụ Scoped hoặc Transient vào Singleton** để tránh các vấn đề rò rỉ bộ nhớ.
- Chọn đúng lifetime để tối ưu hóa hiệu suất và bộ nhớ.

### <a name="gc-lifetime"></a>2. Lifetime của đối tượng trong Garbage Collection (GC)

**Garbage Collection (GC)** là hệ thống tự động quản lý bộ nhớ trong .NET, giúp giải phóng các đối tượng không còn được sử dụng. GC trong .NET chia các đối tượng thành ba thế hệ:

- **Generation 0**: Dành cho các đối tượng có lifetime ngắn, dễ bị thu gom.
- **Generation 1**: Đối tượng có lifetime trung bình, không bị thu gom lần đầu tiên.
- **Generation 2**: Đối tượng có lifetime dài, khó bị thu gom.

> **Lưu ý**: GC xác định lifetime dựa vào khả năng truy cập của đối tượng. Khi đối tượng không còn được tham chiếu, nó sẽ trở thành "rác" và được thu gom.

### <a name="static-lifetime"></a>3. Static và Non-static Lifetime

- **Static lifetime**: Các biến hoặc phương thức `static` tồn tại trong suốt thời gian chạy của ứng dụng, chia sẻ trạng thái giữa các thành phần.

  ```csharp
  public static class MyClass
  {
      public static int MyStaticValue = 0;
  }
  ```

- **Non-static lifetime (Instance lifetime)**: Các đối tượng được tạo từ lớp thông thường có lifetime phụ thuộc vào tham chiếu. Khi không còn tham chiếu, đối tượng sẽ bị GC giải phóng.

  ```csharp
  public class MyClass
  {
      public int MyValue = 0;
  }

  MyClass instance = new MyClass(); // Lifetime của instance phụ thuộc vào tham chiếu này.
  ```

### <a name="event-lifetime"></a>4. Lifetime trong Event và Delegate

- **Event handlers**: Đăng ký event có thể giữ tham chiếu đến đối tượng chứa phương thức, gây rò rỉ bộ nhớ nếu không hủy đăng ký đúng cách.

  ```csharp
  eventHandler.EventOccurred += OnEventOccurred;
  // Để kết thúc lifetime của event, cần unsubcribe khi không dùng đến:
  eventHandler.EventOccurred -= OnEventOccurred;
  ```

- **Delegate lifetime**: Delegate có thể kéo dài lifetime của đối tượng chứa phương thức. Hủy delegate khi không cần để giải phóng đối tượng.

### <a name="task-lifetime"></a>5. Lifetime trong Task và Async/Await

- **Task lifetime**: Các `Task` trong async/await có lifetime dựa trên trạng thái hoàn thành. `Task` sẽ không bị thu gom nếu vẫn đang xử lý hoặc chờ.
- **CancellationToken**: Giúp kết thúc sớm các task không cần thiết, tránh giữ lại các task không sử dụng.

```csharp
CancellationTokenSource cts = new CancellationTokenSource();
await SomeTask(cts.Token);
cts.Cancel(); // Hủy task khi không cần thiết
```

### <a name="file-lifetime"></a>6. Lifetime trong File Handling và I/O

- **File Stream Lifetime**: Đối tượng `FileStream` cần được đóng hoặc hủy sau khi sử dụng để giải phóng tài nguyên hệ thống.

  ```csharp
  using (FileStream fileStream = new FileStream("file.txt", FileMode.Open))
  {
      // Xử lý file
  } // FileStream sẽ được giải phóng khi thoát khỏi khối `using`.
  ```

Nếu không giải phóng tài nguyên đúng cách, file stream có thể tồn tại lâu hơn cần thiết, giữ tài nguyên không cần thiết.

### <a name="disposable-lifetime"></a>7. Disposable Pattern và Quản lý Lifetime thủ công

**Disposable Pattern** trong C# cho phép quản lý tài nguyên một cách chính xác qua giao diện `IDisposable`. Điều này giúp giải phóng các tài nguyên không quản lý (unmanaged resources) khi không còn sử dụng.

#### Lifetime qua `Dispose`

- **Dispose**: Khi gọi `Dispose()`, đối tượng giải phóng tài nguyên không quản lý, giúp giảm lượng tài nguyên giữ lại trong bộ nhớ.

  ```csharp
  public class MyResource : IDisposable
  {
      public void Dispose()
      {
          // Giải phóng tài nguyên
      }
  }

  using (var resource = new MyResource())
  {
      // Sử dụng resource
  } // Dispose() được gọi tự động khi thoát khỏi using
  ```

> **Lưu ý**: Disposable Pattern đặc biệt hữu ích cho các đối tượng dùng nhiều tài nguyên hoặc không thuộc quyền quản lý của GC, như kết nối cơ sở dữ liệu và tài nguyên hệ thống.

## Tóm tắt

- **DI Lifetime (Singleton, Scoped, Transient)**: Cung cấp các tùy chọn quản lý dịch vụ, giúp tối ưu hóa bộ nhớ và hiệu suất trong ứng dụng ASP.NET Core.
- **GC Lifetime**: Dựa vào khả năng truy cập của đối tượng, giúp thu gom các đối tượng không còn sử dụng.
- **Static và Instance Lifetime**: Static tồn tại toàn cục, trong khi instance phụ thuộc vào tham chiếu.
- **Event và Delegate Lifetime**: Cẩn thận khi dùng event và delegate để tránh giữ tham chiếu không cần thiết.
- **Task và Async Lifetime**: Task tồn tại khi chờ xử lý và có thể kết thúc sớm với `CancellationToken`.
- **File và I/O Lifetime**: Cần đóng và hủy các tài nguyên I/O đúng cách.
- **Disposable Lifetime**: Quản lý tài nguyên không quản lý bằng `IDisposable` và `Dispose()` giúp tối ưu hóa bộ nhớ.
