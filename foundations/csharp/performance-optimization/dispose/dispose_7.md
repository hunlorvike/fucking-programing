# Chương 7: `Dispose` Và "Kế Thừa" (Inheritance) - "Dọn Dẹp" Tài Nguyên Trong "Hệ Thống Kế Thừa" - "Không Để 'Con Cháu' 'Bỏ Quên' Trách Nhiệm" - "Gia Đình" "Dọn Dẹp" Tài Nguyên

Chào mừng bạn đến với **Chương 7: `Dispose` Và "Kế Thừa" (Inheritance)**! Trong chương này, chúng ta sẽ "giải quyết" một "thách thức" "phức tạp" hơn trong "quản lý" tài nguyên: **"dọn dẹp" tài nguyên trong "hệ thống kế thừa" (inheritance hierarchy)**. Khi bạn có các class "con" "kế thừa" từ class "cha" và **cả class cha và class con đều "quản lý" "tài nguyên 'unmanaged' "**, bạn cần "đảm bảo" rằng **"cả class cha" và "class con" đều "dọn dẹp" tài nguyên "đúng cách"** khi đối tượng bị `Dispose`.

**Phần 7: `Dispose` Và "Kế Thừa" (Inheritance) - "Dọn Dẹp" Tài Nguyên Trong "Hệ Thống Kế Thừa"**

**7.1. "Vấn Đề" "Dọn Dẹp" Tài Nguyên Trong "Hệ Thống Kế Thừa" - "Ai 'Lo' Phần Việc Của Ai?" - "Trách Nhiệm" "Chia Sẻ"**

-   **"Tình Huống" "Phức Tạp" - Class Cha và Class Con "Cùng" "Quản Lý" Tài Nguyên:**

    -   Trong "hệ thống kế thừa" (inheritance hierarchy), class "con" "kế thừa" các "thành viên" (fields, properties, methods) từ class "cha".
    -   Nếu **cả class "cha"** và **class "con"** đều **"quản lý"** các **"tài nguyên 'unmanaged' " "riêng" của mình**, việc "dọn dẹp" tài nguyên trở nên **"phức tạp"** hơn một chút. Bạn cần "đảm bảo" rằng **"cả tài nguyên"** của class "cha" và class "con" đều được **"dọn dẹp" "đúng cách"** khi đối tượng class "con" bị `Dispose`.
    -   **"Không 'cẩn thận' "**, bạn có thể "quên" "dọn dẹp" tài nguyên của class "cha" hoặc class "con", "gây ra" "rò rỉ tài nguyên".

-   **"Ai 'Lo' Phần Việc Của Ai?" - "Phân Chia" "Trách Nhiệm" "Dọn Dẹp" Tài Nguyên Trong "Hệ Thống Kế Thừa":**

    -   **Class "cha" "chịu trách nhiệm" "dọn dẹp" "tài nguyên" mà class "cha" "quản lý"**.
    -   **Class "con" "chịu trách nhiệm" "dọn dẹp" "tài nguyên" mà class "con" "quản lý"**.
    -   Các class "cha" và class "con" cần **"phối hợp"** với nhau trong quá trình "dọn dẹp" tài nguyên để "đảm bảo" rằng **"tất cả"** tài nguyên của **"cả gia đình"** "hệ thống kế thừa" đều được "giải phóng" "đúng cách".

**7.2. "Gọi" `Dispose(disposing)` Từ Class Con Đến Class Cha - "Phối Hợp" "Dọn Dẹp" "Nhịp Nhàng" - "Bàn Tay Lớn" "Dìu Dắt" "Bàn Tay Bé"**

-   **"Giải Pháp" "Phối Hợp" "Dọn Dẹp" Tài Nguyên Trong "Hệ Thống Kế Thừa" - "Gọi" `Dispose(disposing)` Từ Class Con Đến Class Cha:**

    -   Trong "hệ thống kế thừa", class **"con" "ghi đè" (override) phương thức `Dispose(bool disposing)`** (protected virtual) của class **"cha"** (như một phần của `Dispose Pattern` - xem Chương 6).
    -   Trong phương thức `Dispose(bool disposing)` "ghi đè" của class "con", bạn cần **"gọi" phương thức `Dispose(disposing)` của class "cha"** để "cho phép" class "cha" "thực hiện" "logic" "dọn dẹp" tài nguyên của nó.
    -   "Gọi" `base.Dispose(disposing)` ở **"cuối"** phương thức `Dispose(disposing)` "ghi đè" của class "con" (sau khi class "con" đã "dọn dẹp" xong tài nguyên của mình). "Đảm bảo" "thứ tự" "dọn dẹp" "từ 'con' đến 'cha' ".

-   **Ví dụ "Implement" `Dispose` Pattern Trong "Hệ Thống Kế Thừa" - "Phối Hợp" "Dọn Dẹp" Tài Nguyên "Cha" và "Con":**

    ```csharp
    using System;
    using System.IO; // "Nhập" không gian tên cho FileStream

    // Class "cha" - "quản lý" "tài nguyên 'unmanaged' " riêng
    public class BaseLogger : IDisposable
    {
        private StreamWriter _writer; // "Tài nguyên 'unmanaged' " của class "cha"
        private bool _disposed = false;

        public BaseLogger(string filePath)
        {
            _writer = new StreamWriter(filePath);
            Console.WriteLine($"BaseLogger: File mở tại '{filePath}'");
        }

        public virtual void Log(string message) // Phương thức "ảo" Log (virtual) - class "con" có thể "ghi đè" (override)
        {
            _writer.WriteLine($"{DateTime.Now}: [BaseLogger] {message}"); // "Ghi log" với "nhãn" [BaseLogger]
        }

        public void Dispose() // Dispose() "public", "non-virtual" - từ Dispose Pattern
        {
            Dispose(disposing: true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing) // Dispose(bool disposing) "protected virtual" - từ Dispose Pattern
        {
            if (!_disposed)
            {
                if (disposing)
                {
                    DisposeManagedResources(); // "Dọn dẹp" tài nguyên "managed" (nếu có)
                }

                ReleaseUnmanagedResources(); // "Dọn dẹp" tài nguyên "unmanaged" của class "cha" (_writer)
                _disposed = true;
            }
        }

        ~BaseLogger() // Finalizer (Destructor) - từ Dispose Pattern
        {
            Dispose(disposing: false);
        }

        private void ReleaseUnmanagedResources() // ReleaseUnmanagedResources() - "dọn dẹp" tài nguyên "unmanaged" của class "cha"
        {
            if (_writer != null)
            {
                _writer.Close();
                _writer.Dispose();
                _writer = null;
                Console.WriteLine("BaseLogger.ReleaseUnmanagedResources() được gọi - FileStreamWriter (BaseLogger) đã Dispose."); // Thông báo "dọn dẹp" tài nguyên "unmanaged" của class "cha"
            }
        }

        private protected virtual void DisposeManagedResources() // DisposeManagedResources() "protected virtual" - class "con" có thể "ghi đè" và "mở rộng"
        {
            // Class "cha" không có tài nguyên "managed" nào để "dọn dẹp" trong ví dụ này
        }
    }

    // Class "con" - "kế thừa" từ BaseLogger và "quản lý" "tài nguyên 'unmanaged' " riêng
    public class DerivedLogger : BaseLogger, IDisposable
    {
        private FileStream _logFileStream; // "Tài nguyên 'unmanaged' " của class "con"

        private bool _isDisposedByDerived = false; // Biến cờ "theo dõi" Dispose của class "con"

        public DerivedLogger(string filePath, string baseFilePath) : base(baseFilePath) // Constructor class "con" - "gọi" constructor class "cha" (base)
        {
            _logFileStream = new FileStream(filePath, FileMode.Create); // "Mở" file "riêng" cho DerivedLogger
            Console.WriteLine($"DerivedLogger: File mở tại '{filePath}'"); // Thông báo "mở file" của class "con"
        }

        public override void Log(string message) // "Ghi đè" phương thức Log của class "cha" - "thêm" "nhãn" [DerivedLogger]
        {
            base.Log($"[DerivedLogger] {message}"); // "Gọi" phương thức Log của class "cha" (base.Log) để "ghi log" "chung"
            // ... (code "ghi log" "thêm" "thông tin" "riêng" của DerivedLogger nếu cần) ...
        }


        protected override void Dispose(bool disposing) // "Ghi đè" Dispose(disposing) của class "cha" - "mở rộng" "logic" "dọn dẹp" tài nguyên
        {
            if (!_isDisposedByDerived) // "Kiểm tra" biến cờ "riêng" của class "con"
            {
                if (disposing) // Nếu Dispose được gọi "chủ động" (disposing = true)
                {
                    DisposeManagedResources(); // "Dọn dẹp" tài nguyên "managed" của class "con" (nếu có)
                }

                ReleaseUnmanagedResources(); // "Dọn dẹp" tài nguyên "unmanaged" của class "con" (_logFileStream)

                _isDisposedByDerived = true; // "Đánh dấu" Dispose đã được gọi cho class "con"
            }

            base.Dispose(disposing); // **"Gọi" Dispose(disposing) của class "cha" (base.Dispose) - "quan trọng" để "dọn dẹp" tài nguyên của class "cha"**
        }


        ~DerivedLogger() // Finalizer (Destructor) - "tương tự" class "cha"
        {
            Dispose(disposing: false);
        }


        private new void ReleaseUnmanagedResources() // ReleaseUnmanagedResources() "private new" - "che giấu" phương thức "cùng tên" của class "cha" (không override)
        {
            if (_logFileStream != null)
            {
                _logFileStream.Close();
                _logFileStream.Dispose();
                _logFileStream = null;
                Console.WriteLine("DerivedLogger.ReleaseUnmanagedResources() được gọi - FileStream (DerivedLogger) đã Dispose."); // Thông báo "dọn dẹp" tài nguyên "unmanaged" của class "con"
            }
        }


        private protected override void DisposeManagedResources() // DisposeManagedResources() "protected override" - "ghi đè" phương thức "ảo" của class "cha" - "mở rộng" "logic" "dọn dẹp" tài nguyên "managed"
        {
            base.DisposeManagedResources(); // "Gọi" DisposeManagedResources() của class "cha" (base.DisposeManagedResources) - "dọn dẹp" tài nguyên "managed" của class "cha" (nếu có)
            // ... (code "dọn dẹp" tài nguyên "managed" "riêng" của class "con" nếu có) ...
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            string baseLogFilePath = "base_app.log"; // "Đường đi" file log của BaseLogger
            string derivedLogFilePath = "derived_app.log"; // "Đường đi" file log của DerivedLogger

            // "Dùng" DerivedLogger (class "con") trong khối 'using' statement - "tự động" "gọi" Dispose() cho "cả class cha và class con"
            using (DerivedLogger derivedLogger = new DerivedLogger(derivedLogFilePath, baseLogFilePath)) // Tạo instance DerivedLogger và "giao phó" cho 'using' statement
            {
                derivedLogger.Log("Ứng dụng bắt đầu chạy."); // "Ghi log" thông điệp (dùng phương thức Log "ghi đè" của class "con")
                Console.WriteLine("Ứng dụng đang chạy..."); // Thông báo ứng dụng đang chạy
            } // Khi "ra khỏi" khối 'using', Dispose() của 'derivedLogger' sẽ được "gọi" "tự động" - "dọn dẹp" tài nguyên của "cả class cha và class con"

            Console.WriteLine("Ứng dụng kết thúc."); // Thông báo ứng dụng kết thúc
            Console.ReadKey();
        }
    }
    ```

-   **"Giải mã" code "Implement" `Dispose` Pattern Trong "Hệ Thống Kế Thừa":**

    -   **Class `BaseLogger` (class "cha"):** "Implement" `Dispose Pattern` "chuẩn" để "quản lý" tài nguyên `_writer` "unmanaged" của mình. Phương thức `DisposeManagedResources()` được "để" `virtual` để class "con" có thể "ghi đè" và "mở rộng" (dù không dùng trong ví dụ này).
    -   **Class `DerivedLogger` (class "con"):**
        -   "Kế thừa" từ `BaseLogger` (`class DerivedLogger : BaseLogger, IDisposable`).
        -   "Khai báo" và "quản lý" thêm một "tài nguyên 'unmanaged' " riêng: `_logFileStream`.
        -   "Ghi đè" phương thức `Dispose(bool disposing)` của class "cha" (`protected override void Dispose(bool disposing)`).
        -   Trong phương thức `Dispose(bool disposing)` "ghi đè" của class "con":
            -   "Dọn dẹp" **"tài nguyên 'unmanaged' " "riêng" của class "con"** (`ReleaseUnmanagedResources()`).
            -   **"Gọi" `base.Dispose(disposing)`** - **"quan trọng"** để "cho phép" class "cha" "thực hiện" "logic" "dọn dẹp" tài nguyên của nó. "Đảm bảo" "dọn dẹp" tài nguyên của **"cả class cha và class con"**.
            -   "Dùng" biến cờ `_isDisposedByDerived` "riêng" cho class "con" để "đảm bảo" `Dispose` chỉ được "gọi" "một lần duy nhất" cho class "con".
        -   "Ghi đè" phương thức `DisposeManagedResources()` (protected virtual) của class "cha" để "thêm" "logic" "dọn dẹp" tài nguyên "managed" "riêng" của class "con" (không có trong ví dụ này).
        -   "Che giấu" (shadowing) phương thức `ReleaseUnmanagedResources()` của class cha bằng `private new void ReleaseUnmanagedResources()`. Vì class "con" có "logic" "dọn dẹp" tài nguyên "unmanaged" "riêng", nên "không muốn" "dùng lại" phương thức `ReleaseUnmanagedResources()` của class "cha".

**Tổng Kết Chương 7:**

-   Bạn đã "khám phá" cách "Implement" `Dispose` Pattern trong "Hệ Thống Kế Thừa" - "dọn dẹp" tài nguyên "nhịp nhàng" giữa class cha và class con.
    -   "Hiểu" được "vấn đề" "dọn dẹp" tài nguyên trong "hệ thống kế thừa" - "chia sẻ" "trách nhiệm" giữa class cha và class con.
    -   Học cách "gọi" `Dispose(disposing)` từ class con đến class cha (`base.Dispose(disposing)`) để "phối hợp" "dọn dẹp" tài nguyên.
    -   "Nắm vững" "cách implement" `Dispose Pattern` "chuẩn" cho class "cha" và class "con" trong "hệ thống kế thừa".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: Ứng Dụng Thực Tế Của `Dispose` - "Dispose Đi Muôn Nơi"**. Chúng ta sẽ "thấy" `Dispose` được "ứng dụng" như thế nào trong các "tình huống" "thực tế", từ ứng dụng console "đơn giản" đến ứng dụng web và desktop "phức tạp" hơn, "chứng minh" rằng `Dispose` là một "kỹ năng" "thiết yếu" cho mọi lập trình viên .NET "chuyên nghiệp".

Bạn có câu hỏi nào về `Dispose` và "kế thừa" này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn lòng "giải đáp" và "cùng bạn" "làm chủ" `Dispose`.
