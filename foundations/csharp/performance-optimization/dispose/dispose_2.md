# Chương 2: Interface

`IDisposable` - "Chứng Minh Thư" Của Đối Tượng "Cần Dọn Dẹp" - "Tấm Thẻ Căn Cước" Cho Class "Biết Tự 'Dọn Dẹp' "\*\*

Chào mừng bạn trở lại với **Chương 2: Interface `IDisposable`**! Trong chương này, chúng ta sẽ "khám phá" *
*`IDisposable` interface** - "giao diện" "quan trọng" nhất để "hiện thực hóa" "khả năng" "tự dọn dẹp" tài nguyên cho các
class C# của bạn.

**Phần 2: Interface `IDisposable` - "Chứng Minh Thư" Của Đối Tượng "Cần Dọn Dẹp"**

**2.1. `IDisposable` Interface là gì? (Giải thích "dễ hiểu" và "vai trò" của Interface) - "Giao Diện" "Chuẩn" Để "Báo
Hiệu" "Khả Năng Tự 'Dọn Dẹp' "**

- **`IDisposable` Interface - "Giao Diện" "Chuẩn" Để "Dọn Dẹp" Tài Nguyên:**

    - **`IDisposable`** là một **"interface"** (giao diện) "được định nghĩa sẵn" trong .NET Framework (trong namespace
      `System`).
    - `IDisposable` interface "chỉ" có **một "thành viên" duy nhất**: phương thức **`Dispose()`**.
    - **"Vai trò" chính** của `IDisposable` interface là **"báo hiệu"** cho .NET runtime (và cho lập trình viên khác)
      biết rằng một class **"implement"** interface này **"có 'trách nhiệm' " "quản lý"** và **"giải phóng"** các **"tài
      nguyên 'unmanaged' "** (ví dụ: file handles, network connections, database connections, v.v.) mà nó đang "sử
      dụng".
    - Class "implement" `IDisposable` interface được gọi là **"disposable class"** (class "có thể dọn dẹp").

- **Interface - "Hợp Đồng" "Cam Kết" "Chức Năng":**

    - **Interface** (giao diện) trong lập trình hướng đối tượng (OOP) là một **"bản hợp đồng"** hoặc **"giao kèo"** giữa
      các class.
    - Interface "định nghĩa" một **"tập hợp" các "phương thức"** (methods), **"thuộc tính"** (properties), **"sự kiện"
      ** (events), hoặc các "thành viên" khác mà các class "implement" interface phải "cung cấp" (implement).
    - Interface "không" "hiện thực hóa" (implement) "logic" "cụ thể" của các "thành viên", mà chỉ "định nghĩa" **"khuôn
      mẫu"** hoặc **"hợp đồng"** "chung".
    - Class "implement" interface "cam kết" sẽ "hiện thực hóa" "đầy đủ" các "thành viên" mà interface "định nghĩa", "đảm
      bảo" "cung cấp" các "chức năng" theo "hợp đồng" của interface.

- **`IDisposable` Interface - "Hợp Đồng" "Dọn Dẹp" Tài Nguyên:**

    - `IDisposable` interface "định nghĩa" một **"hợp đồng"** "đơn giản" nhưng "vô cùng quan trọng": **"Class '
      implement' `IDisposable` 'cam kết' sẽ 'cung cấp' phương thức `Dispose()` để 'dọn dẹp' tài nguyên"**.
    - Bằng cách "implement" `IDisposable` interface, class của bạn "tự giác" "gánh vác" "trách nhiệm" "quản lý" và "giải
      phóng" tài nguyên, và "báo hiệu" cho .NET runtime và lập trình viên khác biết rằng đối tượng của class này **"cần
      được 'dọn dẹp' " "đúng cách"** sau khi "dùng xong".

**2.2. "Khai Báo" `IDisposable` Interface Trong Class - "Đánh Dấu" Class "Cần Dọn Dẹp" - "Gắn 'Tấm Thẻ Căn Cước' "**

- Để "đánh dấu" một class là "disposable class" (class "có thể dọn dẹp"), bạn cần "khai báo" class đó **"implement"**
  interface **`IDisposable`**.

- **"Cách 'khai báo' " `IDisposable` interface trong class C#:**

  ```csharp
  public class MyDisposableClass : IDisposable // "Kế thừa" (implement) interface IDisposable
  {
      // ... (các thành viên khác của class) ...

      public void Dispose() // "Implement" phương thức Dispose() - "bắt buộc" khi implement IDisposable
      {
          // ... (code "dọn dẹp" tài nguyên "unmanaged" ở đây) ...

          // "Giải phóng" tài nguyên "unmanaged" (ví dụ: file handles, network connections, database connections, v.v.)
          ReleaseUnmanagedResources();

          // "Giải phóng" tài nguyên "managed" (optional - thường không cần thiết, GC lo)
          DisposeManagedResources();

          // "Báo" cho Garbage Collector (GC) biết rằng đối tượng này đã được "dọn dẹp"
          // GC không cần phải "gọi" Finalizer (Destructor) nữa (tối ưu hiệu năng)
          GC.SuppressFinalize(this);
      }

      // (Optional) Phương thức "ảo" (virtual) để class con có thể "ghi đè" (override) và "thêm" logic "dọn dẹp" riêng (Dispose Pattern - xem Chương 6)
      protected virtual void Dispose(bool disposing)
      {
          if (disposing)
          {
              // "Giải phóng" tài nguyên "managed" (optional - thường không cần thiết, GC lo)
              DisposeManagedResources();
          }

          // "Giải phóng" tài nguyên "unmanaged" (luôn "giải phóng" trong Dispose Pattern)
          ReleaseUnmanagedResources();
      }


      ~MyDisposableClass() // Finalizer (Destructor) - "Phương án 'cuối cùng' " để "dọn dẹp" tài nguyên "unmanaged" (chỉ dùng khi "quên" gọi Dispose)
      {
          // "Gọi" Dispose(false) từ Finalizer - "đảm bảo" "dọn dẹp" tài nguyên "unmanaged" ngay cả khi "quên" gọi Dispose
          Dispose(disposing: false);
      }


      private void ReleaseUnmanagedResources() // Phương thức "riêng" để "giải phóng" tài nguyên "unmanaged"
      {
          // ... (code "giải phóng" tài nguyên "unmanaged" - ví dụ: đóng file handle, đóng kết nối, v.v.) ...
          Console.WriteLine("Giải phóng tài nguyên Unmanaged..."); // Ví dụ
      }

      private void DisposeManagedResources() // Phương thức "riêng" để "giải phóng" tài nguyên "managed" (optional - thường không cần thiết, GC lo)
      {
          // ... (code "giải phóng" tài nguyên "managed" - ví dụ: Dispose các đối tượng IDisposable khác mà class này "sở hữu") ...
          Console.WriteLine("Giải phóng tài nguyên Managed..."); // Ví dụ
      }
  }
  ```

- **"Giải mã" code "Implement" `IDisposable`:**

    - `public class MyDisposableClass : IDisposable`: "Khai báo" class `MyDisposableClass` "implement" interface
      `IDisposable` (giống như "ký" vào "hợp đồng" "dọn dẹp" tài nguyên).
    - `public void Dispose()`: "Implement" phương thức `Dispose()` - **"bắt buộc"** khi implement `IDisposable`. Đây là
      **"nơi"** bạn sẽ "viết code" **"dọn dẹp" tài nguyên**.
    - `GC.SuppressFinalize(this)`: "Gọi" `GC.SuppressFinalize(this)` ở **"cuối"** phương thức `Dispose()` để "báo" cho
      Garbage Collector (GC) biết rằng đối tượng này đã được "dọn dẹp" "đúng cách", và GC **"không cần"** phải "gọi"
      Finalizer (Destructor) nữa. Điều này giúp **"tối ưu" "hiệu năng"**, vì Finalizer là "tốn kém" hơn `Dispose`.
    - `protected virtual void Dispose(bool disposing)`: **"Dispose Pattern"** (khuôn mẫu `Dispose`) - chúng ta sẽ "khám
      phá" "chi tiết" ở Chương 6. Phương thức `Dispose(bool disposing)` là một "phiên bản" "mở rộng" của `Dispose()`,
      giúp "phân biệt" giữa việc "dọn dẹp" tài nguyên "managed" và "unmanaged" và hỗ trợ "kế thừa" (inheritance).
    - `~MyDisposableClass() // Finalizer (Destructor)`: **Finalizer (Destructor)** - "phương án 'cuối cùng' " để "dọn
      dẹp" tài nguyên "unmanaged" trong trường hợp lập trình viên **"quên"** "gọi" `Dispose()`. Finalizer được GC "tự
      động" "gọi" khi đối tượng bị "thu gom rác", nhưng **"không đáng tin cậy"** và **"tốn kém" "hiệu năng"**.
    - `ReleaseUnmanagedResources()` và `DisposeManagedResources()`: Các phương thức "riêng" để "chứa" code "dọn dẹp" tài
      nguyên "unmanaged" và "managed" - giúp code `Dispose()` và Finalizer "gọn gàng" và "dễ đọc" hơn.

**2.3. Phương Thức `Dispose()` - "Nơi" "Dọn Dẹp" Tài Nguyên - "Trái Tim" Của `IDisposable` - "Vùng Đất Thánh" Để "Giải
Phóng" Tài Nguyên**

- **`Dispose()` Method - "Nơi" "Giải Phóng" Tài Nguyên "Unmanaged":**

    - **Phương thức `Dispose()`** (trong interface `IDisposable`) là **"trái tim"** của cơ chế `Dispose`. Đây là **"nơi"
      ** bạn sẽ "viết code" **"dọn dẹp"** và **"giải phóng"** các **"tài nguyên 'unmanaged' "** mà class của bạn đang "
      quản lý".
    - Code "dọn dẹp" trong `Dispose()` cần **"đảm bảo"** rằng các "tài nguyên 'unmanaged' " được **"giải phóng" "hoàn
      toàn"** và **"ngay lập tức"** khi phương thức `Dispose()` được "gọi".

- **"Code 'Dọn Dẹp' " Trong `Dispose()` Method - "Thường Bao Gồm" Các "Thao Tác" Sau:**

    - **"Giải phóng" "tài nguyên 'unmanaged' ":**

        - "Đóng" (Close) hoặc "giải phóng" (Release) các "tay cầm" file (File Handles) bằng `fileStream.Close()`,
          `streamReader.Dispose()`, `streamWriter.Dispose()`, v.v.
        - "Đóng" (Close) hoặc "giải phóng" (Dispose) các "kết nối mạng" (Network Connections) bằng
          `httpClient.Dispose()`, `socket.Close()`, v.v.
        - "Đóng" (Close) hoặc "giải phóng" (Dispose) các "kết nối database" (Database Connections) bằng
          `sqlConnection.Close()`, `sqlCommand.Dispose()`, v.v.
        - "Giải phóng" các "tài nguyên hệ điều hành" khác (GDI objects, Window Handles, Memory Mappings, Mutexes,
          Semaphores, v.v.) bằng các "phương thức" "giải phóng" "tương ứng" của từng loại tài nguyên.

    - **"Giải phóng" "tài nguyên 'managed' " (optional - thường không cần thiết, GC lo):**

        - "Dispose" các đối tượng "managed" khác mà class của bạn đang "sở hữu" và chúng cũng "implement" `IDisposable`
          interface (composition of disposables). "Gọi" phương thức `Dispose()` của các đối tượng "con" này trong phương
          thức `Dispose()` của class "cha".
        - Tuy nhiên, việc "giải phóng" "tài nguyên 'managed' " trong `Dispose()` là **"không bắt buộc"** và thường **"
          không cần thiết"**, vì .NET Garbage Collector (GC) sẽ "tự động" "quản lý" và "giải phóng" bộ nhớ "managed".
          Bạn chỉ cần "quan tâm" đến việc "giải phóng" **"tài nguyên 'unmanaged' "** trong `Dispose()`.

    - **"Giải phóng" "bộ nhớ" (optional - thường không cần thiết, GC lo):**
        - "Gán" `null` cho các "tham chiếu" đến các đối tượng "managed" "lớn" hoặc "tốn kém" bộ nhớ (ví dụ: arrays,
          collections) để "gợi ý" cho GC rằng bạn "không còn cần" các đối tượng này nữa và GC có thể "thu gom rác" chúng
          sớm hơn.
        - Tuy nhiên, việc "giải phóng" "bộ nhớ" "managed" "bằng tay" cũng thường **"không cần thiết"** và đôi khi có thể
          **"phản tác dụng"** (làm "phức tạp" code và "giảm" "hiệu năng"). Hãy "tin tưởng" vào "khả năng" "quản lý bộ
          nhớ" của GC.

- **"Gọi" `Dispose()` Method - "Ra Lệnh" "Dọn Dẹp" Tài Nguyên:**

    - Phương thức `Dispose()` thường được "gọi" **"một lần duy nhất"** khi đối tượng "không còn cần thiết" nữa.
    - Bạn có thể "gọi" `Dispose()` **"trực tiếp"** (explicitly) trong code của mình (ví dụ:
      `myDisposableObject.Dispose();`).
    - Hoặc "dùng" **`using` statement** (sẽ "khám phá" ở Chương 3) để "tự động" "gọi" `Dispose()` khi đối tượng "ra
      khỏi" "vùng phủ sóng" (scope).

**2.4. Ví dụ code đơn giản "Implement" `IDisposable` - "Thấy Tận Mắt" `Dispose` "Hoạt Động" - "Thực Hành" "Dọn Dẹp" Tài
Nguyên**

- **Ví dụ class `MyFileLogger` "implement" `IDisposable` để "quản lý" "tay cầm file" (FileStream) "unmanaged":**

  ```csharp
  using System;
  using System.IO; // "Nhập" không gian tên cho FileStream, StreamWriter

  public class MyFileLogger : IDisposable // Class "ghi log" ra file - "implement" IDisposable để "quản lý" FileStream
  {
      private StreamWriter _writer; // "Biến" "thành viên" để "giữ" FileStream (tài nguyên "unmanaged")

      public MyFileLogger(string filePath) // Constructor - "mở" file và tạo StreamWriter
      {
          _writer = new StreamWriter(filePath); // "Mở" file ở chế độ "ghi" và tạo StreamWriter
          Console.WriteLine($"MyFileLogger: File mở tại '{filePath}'"); // Thông báo "file đã mở"
      }

      public void LogMessage(string message) // Phương thức "ghi log" thông điệp
      {
          _writer.WriteLine($"{DateTime.Now}: {message}"); // "Ghi" thông điệp vào file
      }

      public void Dispose() // "Implement" phương thức Dispose() - "dọn dẹp" FileStream
      {
          Console.WriteLine("MyFileLogger.Dispose() được gọi."); // Thông báo Dispose được gọi
          _writer.Close(); // "Đóng" FileStream - "giải phóng" "tay cầm file" "unmanaged"
          _writer.Dispose(); // "Giải phóng" FileStream (gọi Dispose của FileStream) - "dọn dẹp" "sâu hơn" (nếu cần)
          _writer = null;    // "Gán" null để "giải phóng" tham chiếu "managed" (optional - GC lo)
          Console.WriteLine("MyFileLogger: File đã đóng và giải phóng."); // Thông báo "file đã đóng và giải phóng"
      }
  }

  public class Program
  {
      static void Main(string[] args)
      {
          string logFilePath = "app.log"; // "Đường đi" đến file log

          // "Dùng" MyFileLogger trong khối 'using' statement - "tự động" "gọi" Dispose khi "ra khỏi" khối 'using'
          using (MyFileLogger logger = new MyFileLogger(logFilePath)) // Tạo instance MyFileLogger và "giao phó" cho 'using' statement "quản lý" "vòng đời"
          {
              logger.LogMessage("Ứng dụng bắt đầu chạy."); // "Ghi log" thông điệp 1
              logger.LogMessage("Thực hiện công việc 1..."); // "Ghi log" thông điệp 2
              logger.LogMessage("Thực hiện công việc 2..."); // "Ghi log" thông điệp 3
              Console.WriteLine("Ứng dụng đang chạy..."); // Thông báo ứng dụng đang chạy
          } // Khi "ra khỏi" khối 'using', Dispose() của 'logger' sẽ được "gọi" "tự động"

          Console.WriteLine("Ứng dụng kết thúc."); // Thông báo ứng dụng kết thúc
          Console.ReadKey();
      }
  }
  ```

- **"Chạy" ví dụ và "quan sát" kết quả:**

    - Khi ứng dụng "chạy", bạn sẽ thấy các thông báo console "in ra" "quá trình" "mở file", "ghi log", "đóng file", và
      `Dispose()` được "gọi".
    - File `app.log` sẽ được "tạo ra" (hoặc "mở" nếu đã có) và chứa các thông điệp log mà ứng dụng đã "ghi" vào.
    - **"Quan trọng":** Khi "ra khỏi" khối `using` statement, phương thức `Dispose()` của đối tượng `logger` sẽ được **"
      tự động" "gọi"**, "đảm bảo" rằng "tay cầm file" (FileStream) được **"giải phóng"** một cách **"chắc chắn"**, **"
      không lo" "rò rỉ" tài nguyên**.

**Tổng Kết Chương 2:**

- Bạn đã "làm quen" với **`IDisposable` interface** - "chứng minh thư" của đối tượng "cần dọn dẹp" tài nguyên.
    - "Hiểu" được "vai trò" của `IDisposable` interface trong việc "báo hiệu" "khả năng tự 'dọn dẹp' " tài nguyên.
    - Học cách "khai báo" `IDisposable` interface trong class để "đánh dấu" class "cần dọn dẹp".
    - "Nắm vững" "ý nghĩa" và "cách thức hoạt động" của phương thức `Dispose()` - "trái tim" của `IDisposable`.
    - "Thấy tận mắt" ví dụ code đơn giản "implement" `IDisposable` và "hoạt động" của `Dispose()`.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 3: `using` Statement - "Chiếc 'Ô Dù' " "Tự Động" Gọi `Dispose`**. Chúng ta sẽ "khám
phá" `using` statement - một "công cụ" "vô cùng" "tiện lợi" và "an toàn" để "tự động" "gọi" `Dispose()` và "đảm bảo" "
dọn dẹp" tài nguyên "chắc chắn" trong mọi tình huống.

Bạn có câu hỏi nào về `IDisposable` interface này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn lòng "giải đáp" và "
cùng bạn" "làm chủ" `Dispose`.

