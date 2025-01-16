# Async/Await Patterns Nâng Cao

## Mục Lục

1. [Tổng Quan về Async/Await](#1-tổng-quan-về-asyncawait)

   - [Khái Niệm](#khái-niệm)
   - [Cách Hoạt Động](#cách-hoạt-động)

2. [Các Mẫu Sử Dụng Async/Await](#2-các-mẫu-sử-dụng-asyncawait)

   - [Mẫu Fire-and-Forget](#mẫu-fire-and-forget)
   - [Mẫu Chuỗi Nhiệm Vụ (Task Chaining)](#mẫu-chuỗi-nhiệm-vụ-task-chaining)
   - [Mẫu Đồng Thời Hóa (Parallelization)](#mẫu-đồng-thời-hóa-parallelization)

3. [Quản Lý Ngoại Lệ trong Async/Await](#3-quản-lý-ngoại-lệ-trong-asyncawait)

4. [Các Kỹ Thuật Tối Ưu với Async/Await](#4-các-kỹ-thuật-tối-ưu-với-asyncawait)

   - [Sử Dụng `ValueTask`](#sử-dụng-valuetask)
   - [Tránh `ConfigureAwait(false)` Không Hợp Lý](#tránh-configureawaitfalse-không-hợp-lý)
   - [Hạn Chế Chặn (`Task.Wait()` hoặc `.Result`)](#hạn-chế-chặn-taskwait-hoặc-result)

5. [Ưu Điểm và Nhược Điểm](#5-ưu-điểm-và-nhược-điểm)

6. [Tóm Tắt](#6-tóm-tắt)

---

### 1. Tổng Quan về Async/Await

#### Khái Niệm

**Async/Await** là một cặp từ khóa trong C# được giới thiệu để làm việc với các hoạt động bất đồng bộ (asynchronous). Chúng giúp mã trở nên dễ đọc và bảo trì hơn so với việc sử dụng các callback hoặc các mô hình lập trình bất đồng bộ trước đây như `Task` hoặc `IAsyncResult`.

- **Từ khóa `async`**: Được sử dụng để khai báo một phương thức bất đồng bộ.
- **Từ khóa `await`**: Dùng để "chờ" một tác vụ bất đồng bộ hoàn thành mà không chặn luồng chính.

#### Cách Hoạt Động

Khi một phương thức được đánh dấu là `async`, nó có thể chứa từ khóa `await` để tạm dừng thực thi phương thức đó cho đến khi tác vụ (task) được chờ hoàn thành. Sau đó, thực thi sẽ được tiếp tục.

Ví dụ đơn giản:

```csharp
public async Task FetchDataAsync()
{
    Console.WriteLine("Bắt đầu tải dữ liệu...");
    await Task.Delay(2000); // Mô phỏng việc tải dữ liệu
    Console.WriteLine("Hoàn thành tải dữ liệu.");
}
```

---

### 2. Các Mẫu Sử Dụng Async/Await

#### Mẫu Fire-and-Forget

Mẫu **Fire-and-Forget** được sử dụng khi bạn muốn bắt đầu một tác vụ bất đồng bộ mà không cần chờ kết quả.

```csharp
public void LogActivity()
{
    _ = LogAsync(); // Gọi mà không chờ
}

private async Task LogAsync()
{
    await Task.Delay(1000); // Mô phỏng ghi nhật ký
    Console.WriteLine("Hoàn thành ghi nhật ký.");
}
```

> **Lưu ý**: Không khuyến nghị sử dụng mẫu này trừ khi bạn đã kiểm soát được ngoại lệ phát sinh.

---

#### Mẫu Chuỗi Nhiệm Vụ (Task Chaining)

Chuỗi nhiệm vụ cho phép thực thi tuần tự nhiều tác vụ bất đồng bộ bằng cách sử dụng `await` trong một chuỗi.

```csharp
public async Task ProcessDataAsync()
{
    var data = await FetchDataAsync();
    await SaveDataAsync(data);
    Console.WriteLine("Xử lý hoàn tất.");
}

private async Task<string> FetchDataAsync()
{
    await Task.Delay(1000);
    return "Dữ liệu đã tải";
}

private async Task SaveDataAsync(string data)
{
    await Task.Delay(500);
    Console.WriteLine($"Dữ liệu đã lưu: {data}");
}
```

---

#### Mẫu Đồng Thời Hóa (Parallelization)

Đồng thời hóa cho phép thực thi nhiều tác vụ cùng một lúc thay vì tuần tự. Sử dụng `Task.WhenAll` hoặc `Task.WhenAny`.

```csharp
public async Task ProcessMultipleTasksAsync()
{
    var task1 = Task.Delay(2000);
    var task2 = Task.Delay(1000);
    await Task.WhenAll(task1, task2);
    Console.WriteLine("Tất cả tác vụ đã hoàn thành.");
}
```

---

### 3. Quản Lý Ngoại Lệ trong Async/Await

Để xử lý ngoại lệ trong các phương thức async, bạn có thể sử dụng `try-catch`.

```csharp
public async Task FetchDataWithExceptionHandlingAsync()
{
    try
    {
        await Task.Delay(1000);
        throw new Exception("Có lỗi xảy ra!");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Ngoại lệ: {ex.Message}");
    }
}
```

Ngoài ra, sử dụng `Task.WhenAll` cần chú ý bắt nhiều ngoại lệ.

```csharp
public async Task ProcessWithMultipleExceptionsAsync()
{
    var tasks = new[]
    {
        Task.Run(() => throw new Exception("Lỗi 1")),
        Task.Run(() => throw new Exception("Lỗi 2"))
    };

    try
    {
        await Task.WhenAll(tasks);
    }
    catch
    {
        foreach (var t in tasks.Where(t => t.IsFaulted))
        {
            Console.WriteLine(t.Exception?.Message);
        }
    }
}
```

---

### 4. Các Kỹ Thuật Tối Ưu với Async/Await

#### Sử Dụng `ValueTask`

`ValueTask` giúp giảm việc phân bổ bộ nhớ không cần thiết cho các tác vụ ngắn hạn.

```csharp
public ValueTask<int> ComputeAsync(int x)
{
    return x > 10 ? new ValueTask<int>(x * 2) : new ValueTask<int>(Task.FromResult(x * 2));
}
```

---

#### Tránh `ConfigureAwait(false)` Không Hợp Lý

Sử dụng `ConfigureAwait(false)` để tránh việc bắt buộc sử dụng context đồng bộ hóa khi không cần thiết (ví dụ: trong các thư viện).

```csharp
await Task.Delay(1000).ConfigureAwait(false);
```

> **Lưu ý**: Chỉ sử dụng khi chắc chắn không cần context đồng bộ hóa.

---

#### Hạn Chế Chặn (`Task.Wait()` hoặc `.Result`)

Việc sử dụng `.Wait()` hoặc `.Result` để chặn một tác vụ bất đồng bộ có thể dẫn đến deadlock.

Sai lầm:

```csharp
public void Process()
{
    var result = GetDataAsync().Result; // Deadlock tiềm ẩn
}
```

Giải pháp:

```csharp
public async Task ProcessAsync()
{
    var result = await GetDataAsync();
}
```

---

### 5. Ưu Điểm và Nhược Điểm

#### Ưu Điểm

- **Cải Thiện Hiệu Suất**: Cho phép tận dụng tối đa tài nguyên hệ thống thông qua xử lý bất đồng bộ.
- **Mã Dễ Đọc**: Dễ viết và duy trì hơn so với mô hình callback truyền thống.
- **Thích Hợp với Các Hoạt Động IO**: Tối ưu hóa cho các tác vụ IO như đọc/ghi tệp hoặc gọi API.

#### Nhược Điểm

- **Phức Tạp trong Quản Lý Ngoại Lệ**: Việc xử lý ngoại lệ trong các tác vụ đồng thời có thể gây khó khăn.
- **Khả Năng Deadlock**: Dễ gây ra deadlock nếu sử dụng sai cách (như `.Result` hoặc `.Wait()`).
- **Tiêu Tốn Bộ Nhớ**: Sử dụng nhiều tác vụ nhỏ có thể tạo thêm áp lực lên bộ thu gom rác (GC).

---

### 6. Tóm Tắt

Async/Await là công cụ mạnh mẽ để thực hiện các tác vụ bất đồng bộ một cách hiệu quả và dễ đọc. Tuy nhiên, việc sử dụng không đúng cách có thể dẫn đến các vấn đề hiệu suất hoặc lỗi khó tìm.

**Các điểm chính:**

1. Async/Await giúp mã bất đồng bộ dễ đọc hơn.
2. Các mẫu sử dụng bao gồm Fire-and-Forget, Chuỗi Nhiệm Vụ, và Đồng Thời Hóa.
3. Cần xử lý ngoại lệ cẩn thận khi làm việc với các tác vụ bất đồng bộ.
4. Sử dụng các kỹ thuật tối ưu như `ValueTask` và `ConfigureAwait(false)` đúng lúc để cải thiện hiệu suất.
