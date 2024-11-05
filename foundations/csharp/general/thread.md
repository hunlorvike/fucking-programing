# **Thread trong C# .NET**

**Thread** trong C#/.NET là đơn vị thực thi độc lập trong một ứng dụng, cho phép thực hiện song song hoặc đồng thời, cải thiện hiệu suất và khả năng phản hồi của ứng dụng, đặc biệt trong các tình huống cần xử lý đồng thời hoặc không đồng bộ.

### Mục lục

1. [Giới thiệu về Thread](#intro-thread)
2. [Tạo và quản lý Thread](#create-manage-thread)
3. [Thread Pool và TPL](#thread-pool-tpl)
4. [Đồng bộ hóa và An toàn cho Thread](#synchronization)
5. [Async/Await và Lập trình không đồng bộ](#async-await)
6. [Hủy bỏ và Thời gian sống của Thread](#cancellation)
7. [Vòng đời của Thread](#thread-lifecycle)
8. [Hướng dẫn sử dụng Thread và Lập trình không đồng bộ](#usage-guidelines)

### <a name="intro-thread"></a>1. Giới thiệu về Thread

**Thread** là đơn vị nhỏ hơn trong một tiến trình, cho phép thực thi song song. C# hỗ trợ lập trình đa luồng (multithreading) để tăng hiệu suất ứng dụng.

- **Chia sẻ dữ liệu**: Thread có thể chia sẻ dữ liệu, nhưng điều này có thể gây ra vấn đề về an toàn dữ liệu.
- **Các loại Thread**: Có thể tạo thread mới hoặc sử dụng lại thông qua Thread Pool.

### <a name="create-manage-thread"></a>2. Tạo và quản lý Thread

Bạn có thể tạo thread mới bằng lớp `Thread` trong không gian tên `System.Threading`:

```csharp
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Thread myThread = new Thread(PrintNumbers);
        myThread.Start(); // Khởi động thread
    }

    static void PrintNumbers()
    {
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(i);
            Thread.Sleep(500); // Giả lập công việc
        }
    }
}
```

#### Quản lý Thread

- **Join**: Đợi cho thread hoàn tất.
- **Abort**: Ngừng thread (không khuyến khích).
- **Sleep**: Tạm dừng thread trong khoảng thời gian nhất định.

### <a name="thread-pool-tpl"></a>3. Thread Pool và Task Parallel Library (TPL)

**Thread Pool** là tập hợp các thread đã được khởi tạo, cho phép tái sử dụng mà không cần tạo mới:

```csharp
ThreadPool.QueueUserWorkItem(PrintNumbers);
```

**Task Parallel Library (TPL)** cung cấp cách tiếp cận cao cấp hơn cho việc quản lý các tác vụ đồng thời:

```csharp
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        Task.Run(() => PrintNumbers()); // Tạo và chạy task
    }
}
```

### <a name="synchronization"></a>4. Đồng bộ hóa và An toàn cho Thread

Khi nhiều thread truy cập vào dữ liệu chung, có thể xảy ra tình trạng tranh chấp (race condition). Để đảm bảo an toàn, sử dụng các kỹ thuật đồng bộ:

- **Lock**: Đảm bảo chỉ một thread có thể truy cập vào đoạn mã tại một thời điểm.

```csharp
private static readonly object _lock = new object();

lock (_lock)
{
    // Code được bảo vệ
}
```

- **Mutex**: Giống như lock nhưng có thể hoạt động trên nhiều tiến trình.

### <a name="async-await"></a>5. Async/Await và Lập trình không đồng bộ

Lập trình không đồng bộ giúp cải thiện khả năng phản hồi mà không cần tạo nhiều thread. Sử dụng từ khóa `async` và `await`:

```csharp
public async Task ExecuteAsync()
{
    await Task.Run(() => PrintNumbers());
}
```

### <a name="cancellation"></a>6. Hủy bỏ và Thời gian sống của Thread

Sử dụng `CancellationToken` để cho phép hủy các hoạt động đang chạy:

```csharp
CancellationTokenSource cts = new CancellationTokenSource();
Task task = Task.Run(() => DoWork(cts.Token), cts.Token);

// Hủy task khi không cần thiết
cts.Cancel();
```

### <a name="thread-lifecycle"></a>7. Vòng đời của Thread

**Thread Lifecycle** mô tả các trạng thái của một thread:

- **Unstarted**: Thread đã được tạo nhưng chưa khởi động.
- **Running**: Thread đang hoạt động.
- **WaitSleepJoin**: Thread đang chờ hoặc tạm dừng.
- **Stopped**: Thread đã hoàn tất hoặc dừng lại.

### <a name="usage-guidelines"></a>8. Hướng dẫn sử dụng Thread và Lập trình không đồng bộ

#### Khi nào nên sử dụng Thread

1. **Công việc CPU-bound**:

   - Tốt cho các tác vụ tính toán phức tạp.
   - Ví dụ: Tính toán ma trận lớn.

2. **Cần kiểm soát chi tiết**:

   - Khi bạn cần kiểm soát vòng đời của thread.
   - Ví dụ: Các tác vụ nền cần dừng tại thời điểm cụ thể.

3. **Sử dụng Thread Pool**:
   - Tái sử dụng thread mà không cần tạo mới.
   - Ví dụ: Thực thi nhiều tác vụ đồng thời.

#### Khi nào nên sử dụng Asynchronous Programming

1. **Công việc I/O-bound**:

   - Giải phóng thread trong khi chờ I/O hoàn thành.
   - Ví dụ: Gọi API web mà không làm nghẽn giao diện.

2. **Khả năng phản hồi cao**:

   - Giữ cho giao diện không bị đóng băng.
   - Ví dụ: Ứng dụng Windows Forms sử dụng `async` và `await`.

3. **Dễ dàng quản lý và bảo trì**:
   - Mã dễ đọc và bảo trì hơn so với quản lý nhiều thread thủ công.

### Tóm tắt so sánh

| Tình huống                              | Sử dụng Thread                        | Sử dụng Asynchronous              |
| --------------------------------------- | ------------------------------------- | --------------------------------- |
| **Công việc CPU-bound**                 | Tạo thread để xử lý song song         | Không thích hợp                   |
| **Công việc I/O-bound**                 | Không thích hợp                       | Sử dụng `async/await`             |
| **Kiểm soát chi tiết vòng đời thread**  | Sử dụng thread để kiểm soát           | Không cần thiết                   |
| **Phản hồi tức thì trong ứng dụng GUI** | Có thể làm cho giao diện bị đóng băng | Giúp giao diện không bị đóng băng |
| **Dễ đọc và bảo trì**                   | Thường phức tạp hơn                   | Dễ đọc và bảo trì hơn             |

### Kết luận

Việc lựa chọn giữa thread và lập trình bất đồng bộ phụ thuộc vào yêu cầu cụ thể của ứng dụng. Thường thì, kết hợp cả hai kỹ thuật sẽ mang lại hiệu suất tốt nhất cho ứng dụng của bạn.
