# Task Parallel Library (TPL)

## Mục Lục

1. [Tổng Quan về Task Parallel Library (TPL)](#1-tổng-quan-về-task-parallel-library-tpl)

   - [Mục Đích](#mục-đích)
   - [Cách Hoạt Động](#cách-hoạt-động)

2. [Các Thành Phần Chính của TPL](#2-các-thành-phần-chính-của-tpl)

3. [Cách Sử Dụng TPL](#3-cách-sử-dụng-tpl)

   - [a. Sử Dụng Task Class](#a-sử-dụng-task-class)
   - [b. Sử Dụng Parallel Class](#b-sử-dụng-parallel-class)

4. [Ưu Điểm và Nhược Điểm của TPL](#4-ưu-điểm-và-nhược-điểm-của-tpl)

5. [Ví Dụ Thực Tế với TPL](#5-ví-dụ-thực-tế-với-tpl)

   - [a. Tạo và Chạy Task](#a-tạo-và-chạy-task)
   - [b. Chạy Nhiều Task Song Song](#b-chạy-nhiều-task-song-song)
   - [c. Parallel.For và Parallel.ForEach](#c-parallelfor-và-parallelforeach)

6. [Các Lưu Ý Khi Sử Dụng TPL](#6-các-lưu-ý-khi-sử-dụng-tpl)

7. [Tóm Tắt](#7-tóm-tắt)

---

### 1. Tổng Quan về Task Parallel Library (TPL)

**Task Parallel Library (TPL)** là một phần của thư viện .NET, được thiết kế để giúp lập trình viên xử lý các tác vụ đa luồng (multithreading) một cách dễ dàng và hiệu quả. TPL cung cấp các API mạnh mẽ để lập trình song song, tập trung vào việc tận dụng tối đa hiệu suất của CPU.

#### Mục Đích

- **Tăng Hiệu Quả Xử Lý**: Giúp ứng dụng thực thi nhanh hơn bằng cách tận dụng nhiều lõi CPU.
- **Đơn Giản Hóa Đa Luồng**: Loại bỏ các thao tác phức tạp như quản lý thread thủ công.
- **Tăng Khả Năng Mở Rộng**: Tự động điều chỉnh tài nguyên để tối ưu hóa hiệu suất.

#### Cách Hoạt Động

- TPL hoạt động dựa trên khái niệm "task" (tác vụ), là một đơn vị công việc có thể được thực thi độc lập.
- Thư viện này sử dụng **Thread Pool** (bộ nhớ chứa các luồng có sẵn) để quản lý các luồng một cách hiệu quả.
- Người lập trình chỉ cần tập trung vào logic công việc, trong khi TPL sẽ tự động xử lý lịch trình và tối ưu hóa luồng.

---

### 2. Các Thành Phần Chính của TPL

1. **Task Class**: Được sử dụng để định nghĩa và thực thi các tác vụ độc lập.
2. **Parallel Class**: Cung cấp các phương thức như `Parallel.For` và `Parallel.ForEach` để xử lý vòng lặp song song.
3. **TaskScheduler**: Quản lý việc lập lịch thực thi các tác vụ.
4. **CancellationToken**: Cho phép hủy bỏ các tác vụ khi cần thiết.
5. **Continuation Tasks**: Hỗ trợ liên kết nhiều tác vụ với nhau để thực thi tuần tự hoặc song song.

---

### 3. Cách Sử Dụng TPL

#### a. Sử Dụng Task Class

```csharp
Task task = Task.Run(() =>
{
    Console.WriteLine("Task đang chạy...");
});
task.Wait(); // Đợi task hoàn thành
```

#### b. Sử Dụng Parallel Class

```csharp
Parallel.For(0, 10, i =>
{
    Console.WriteLine($"Chạy song song cho chỉ số: {i}");
});
```

---

### 4. Ưu Điểm và Nhược Điểm của TPL

#### Ưu Điểm

- **Dễ Sử Dụng**: API trực quan và đơn giản.
- **Tự Động Quản Lý Thread Pool**: Không cần quản lý luồng thủ công.
- **Hiệu Suất Cao**: Tận dụng tối đa tài nguyên CPU.

#### Nhược Điểm

- **Khó Debug**: Mã song song có thể phức tạp để gỡ lỗi.
- **Tiêu Tốn Tài Nguyên**: Nếu không kiểm soát tốt, có thể dẫn đến quá tải tài nguyên.

---

### 5. Ví Dụ Thực Tế với TPL

#### a. Tạo và Chạy Task

```csharp
Task task = Task.Run(() =>
{
    Console.WriteLine("Tác vụ đang chạy...");
});
task.Wait();
```

#### b. Chạy Nhiều Task Song Song

```csharp
Task[] tasks = new Task[3];
for (int i = 0; i < tasks.Length; i++)
{
    int taskIndex = i;
    tasks[i] = Task.Run(() =>
    {
        Console.WriteLine($"Task {taskIndex} đang chạy...");
    });
}

Task.WaitAll(tasks);
```

#### c. Parallel.For và Parallel.ForEach

```csharp
Parallel.For(0, 5, i =>
{
    Console.WriteLine($"Vòng lặp song song: {i}");
});

List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
Parallel.ForEach(numbers, number =>
{
    Console.WriteLine($"Số: {number}");
});
```

---

### 6. Các Lưu Ý Khi Sử Dụng TPL

1. **Sử Dụng CancellationToken**: Để kiểm soát và hủy tác vụ khi cần thiết.
2. **Cân Nhắc Deadlock**: Tránh sử dụng `Wait` hoặc `Result` trên các tác vụ không đồng bộ, vì có thể gây ra deadlock.
3. **Không Lạm Dụng Parallelism**: Chỉ nên sử dụng TPL khi thật sự cần thiết để tránh làm tăng độ phức tạp của mã.

---

### 7. Tóm Tắt

Task Parallel Library là một công cụ mạnh mẽ trong .NET để xây dựng các ứng dụng song song. TPL giúp lập trình viên đơn giản hóa việc quản lý đa luồng và tối ưu hóa hiệu suất ứng dụng. Việc nắm vững cách sử dụng các thành phần như `Task`, `Parallel`, và `CancellationToken` sẽ giúp bạn tận dụng tối đa lợi ích mà TPL mang lại.

**Các điểm chính:**

- TPL sử dụng **Task** như một đơn vị công việc cơ bản.
- API của TPL giúp xử lý các vòng lặp song song và quản lý luồng hiệu quả.
- Cần chú ý đến hiệu suất và độ phức tạp khi triển khai song song hóa.
