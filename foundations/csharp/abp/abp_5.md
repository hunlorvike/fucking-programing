# Chương 5: Domain-Driven Design (DDD) Với ABP Framework - " 'Thiết Kế' " Ứng Dụng "Hướng Nghiệp Vụ" - " 'Đặt' " "Nghiệp Vụ" Vào "Trung Tâm"

Chào mừng bạn đến với **Chương 5: Domain-Driven Design (DDD) Với ABP Framework**! Trong chương này, chúng ta sẽ "khám
phá" **Domain-Driven Design (DDD)**, một "phương pháp luận" (methodology) **"thiết kế" phần mềm** "hướng nghiệp vụ" (
domain-driven), "tìm hiểu" các **"khái niệm" "cốt lõi" của DDD**, và "xem" cách ABP Framework **"hỗ trợ" "triển khai"
DDD** trong ứng dụng của bạn một cách **"dễ dàng"** và **"hiệu quả"**. DDD "giúp" bạn "xây dựng" các ứng dụng **"phức
tạp"** với **"logic nghiệp vụ" "chặt chẽ"** và **"gần gũi"** với "thực tế" "nghiệp vụ" của doanh nghiệp.

**Phần 5: Domain-Driven Design (DDD) Với ABP Framework - " 'Thiết Kế' " Ứng Dụng "Hướng Nghiệp Vụ"**

- **Domain-Driven Design (DDD) - " 'Đặt' " "Nghiệp Vụ" Vào "Trung Tâm" Của "Thiết Kế" Phần Mềm:**

    - **Domain-Driven Design (DDD)** là một **"phương pháp luận"** (methodology) hoặc **"cách tiếp cận"** (approach)
      trong **"thiết kế" và "phát triển" phần mềm**, "tập trung" vào việc **"mô hình hóa"** (modeling) **"miền nghiệp
      vụ"** (business domain) của ứng dụng một cách **"sâu sắc"** và **"chính xác"**.
    - DDD "đặt" **"miền nghiệp vụ"** (business domain) vào **"trung tâm"** của quá trình "thiết kế" phần mềm. DDD "nhấn
      mạnh" vào việc **"hiểu rõ" "nghiệp vụ"** (business), **"giao tiếp" "chặt chẽ"** với các **"chuyên gia" "nghiệp
      vụ"** (domain experts), và "xây dựng" một **"ngôn ngữ chung"** (ubiquitous language) để "mô tả" "miền nghiệp vụ"
      trong code.
    - DDD "không phải" là một "công nghệ" (technology) hay "framework" (bộ khung) "cụ thể". DDD là một **"tập hợp" các "
      nguyên tắc"** (principles), **"mô hình"** (patterns), và **"kỹ thuật"** (techniques) để "thiết kế" phần mềm **"
      hướng nghiệp vụ"**.
    - DDD "thường" được "áp dụng" cho các ứng dụng **"phức tạp"** với **"logic nghiệp vụ" "đa dạng"** và **"thay đổi" "
      thường xuyên"**. DDD "không phù hợp" cho các ứng dụng "đơn giản" với "ít" logic nghiệp vụ.

- **"Lợi Ích" Của Việc "Áp Dụng" Domain-Driven Design (DDD):**

    - **"Mô Hình Hóa" "Nghiệp Vụ" "Chính Xác" (Accurate Business Modeling):** DDD "giúp" bạn "xây dựng" một **"mô hình"
      ** (model) phần mềm **"phản ánh" "chính xác" "thực tế" "nghiệp vụ"** của doanh nghiệp. "Giảm thiểu" "sự khác biệt"
      giữa "mô hình" phần mềm và "thực tế" nghiệp vụ, "giúp" ứng dụng **"đáp ứng" "tốt hơn"** "nhu cầu" của người dùng
      và doanh nghiệp.
    - **"Giao Tiếp" "Hiệu Quả" Giữa Các "Bên Liên Quan" (Effective Communication):** DDD "tạo ra" một **"ngôn ngữ
      chung"** (ubiquitous language) để **"giao tiếp"** giữa các **"lập trình viên"** (developers) và các **"chuyên gia"
      "nghiệp vụ"** (domain experts). "Giúp" mọi người "hiểu" nhau "dễ dàng" hơn và "tránh" các "hiểu lầm" trong quá
      trình "phát triển" phần mềm.
    - **"Code" "Chất Lượng Cao" (High-Quality Code):** DDD "khuyến khích" việc "tổ chức" code theo **"miền nghiệp vụ"**,
      "tạo ra" các **"modules" "gắn kết"** (cohesive modules) và **"giảm thiểu" "sự phụ thuộc"** (coupling) giữa các "
      thành phần" của ứng dụng. "Giúp" code **"dễ đọc"**, **"dễ hiểu"**, **"dễ bảo trì"**, và **"dễ kiểm thử"** hơn.
    - **"Dễ Dàng" "Thay Đổi" và "Mở Rộng" Ứng Dụng (Flexibility and Extensibility):** DDD "tạo ra" một **"kiến trúc"
      ứng dụng "linh hoạt"** và **"dễ mở rộng"**. "Dễ dàng" "thêm" các "tính năng" "mới", "thay đổi" các "quy tắc
      nghiệp vụ", hoặc "tích hợp" với các "hệ thống" "khác" mà "không ảnh hưởng" đến các "phần khác" của ứng dụng (nếu "tuân thủ" các "nguyên tắc" DDD "đúng cách").
    - **"Tập Trung" Vào "Giá Trị" "Nghiệp Vụ" (Focus on Business Value):** DDD "giúp" lập trình viên **"tập trung"** vào
      việc "giải quyết" các **"vấn đề" "nghiệp vụ"** "thực tế" thay vì "vật lộn" với các "vấn đề" "kỹ thuật" "không cần
      thiết". "Tạo ra" các ứng dụng **"mang lại 'giá trị' " "thực sự"** cho doanh nghiệp.

- **"Các Khái Niệm" "Cốt Lõi" Của Domain-Driven Design (DDD):**

    - DDD "bao gồm" **"nhiều khái niệm"** và **"mô hình"** (patterns) "khác nhau". "Một số" "khái niệm" "cốt lõi" của
      DDD bao gồm:
        *   **Domain (Miền nghiệp vụ):** Lĩnh vực hoạt động, nghiệp vụ mà phần mềm đang giải quyết.
        *   **Ubiquitous Language (Ngôn ngữ chung):** Ngôn ngữ chung được sử dụng bởi cả team dev và domain experts.
        *   **Bounded Context (Bối cảnh giới hạn):** Ranh giới xác định của một mô hình nghiệp vụ cụ thể.
        *   **Entities (Thực thể):** Các đối tượng có định danh, có vòng đời.
        *   **Value Objects (Đối tượng giá trị):** Các đối tượng mô tả, không có định danh, bất biến.
        *   **Aggregates (Tập hợp):** Nhóm các đối tượng liên quan, được quản lý như một đơn vị.
        *   **Domain Services (Dịch vụ nghiệp vụ):** Các dịch vụ chứa logic nghiệp vụ, không thuộc về entity/value
            object cụ thể nào.
        *   **Repositories (Kho chứa):** Ẩn đi chi tiết truy cập dữ liệu, cung cấp interface để thao tác với domain
            objects.
        *   **Domain Events (Sự kiện nghiệp vụ):** Các sự kiện xảy ra trong domain.
        *   **Factories:** Chịu trách nhiệm tạo các object phức tạp.

- **ABP Framework "Hỗ Trợ" Domain-Driven Design (DDD) "Như Thế Nào"?**

    - ABP Framework "được thiết kế" để **"hỗ trợ" "triển khai" DDD** một cách **"dễ dàng"** và **"hiệu quả"**. ABP
      Framework "cung cấp" các **"khối xây dựng"** (building blocks), **"kiến trúc"**, và **"công cụ"** để "giúp" bạn
      "áp dụng" các "khái niệm" và "mô hình" DDD trong ứng dụng của mình.
    - **"Một Số" "Hỗ Trợ" "Cụ Thể" Của ABP Framework Cho DDD:**
        *   **Layered Architecture (Kiến trúc đa tầng):** ABP Framework "cung cấp" một "kiến trúc" "đa tầng" "chuẩn" (
            Presentation Layer, Application Layer, Domain Layer, Infrastructure Layer) "phù hợp" với các "nguyên tắc"
            của DDD.
        *   **Base Classes for DDD Concepts (Các lớp cơ sở cho các khái niệm DDD):** ABP Framework "cung cấp" các **"lớp
            cơ sở"** (base classes) và **"giao diện"** (interfaces) để bạn "dễ dàng" "triển khai" các "khái niệm" DDD
            (ví dụ: `Entity`, `AggregateRoot`, `ValueObject`, `IRepository`, `DomainService`).
        *   **Domain Events (Sự kiện nghiệp vụ):** ABP Framework "tích hợp" sẵn **"hệ thống" "xử lý" "sự kiện nghiệp vụ"**
            (domain events) để bạn "dễ dàng" "phát hành" (publish) và "xử lý" (handle) các sự kiện trong Domain Layer.
        *   **Repositories (Kho chứa):** ABP Framework "cung cấp" **"giao diện" `IRepository`** và các **"triển khai" "
            mặc định"** (default implementations) cho các "thao tác" CRUD (Create, Read, Update, Delete) trên
            repositories, "giúp" bạn "truy cập" dữ liệu một cách "dễ dàng" và "nhất quán".
        *   **Unit of Work (Đơn vị công việc):** ABP Framework "cung cấp" **"cơ chế" "quản lý" "giao dịch" (transaction)**
            "tự động" thông qua **Unit of Work pattern**, "đảm bảo" "tính 'nhất quán' " của dữ liệu khi "thực hiện"
            nhiều "thao tác" trên database trong cùng một "giao dịch".
        *   **Dependency Injection (DI):** ABP Framework "tích hợp" sẵn **Dependency Injection (DI)**, "giúp" bạn "quản
            lý" các "phụ thuộc" (dependencies) giữa các "thành phần" của ứng dụng một cách "dễ dàng" và "linh hoạt", "
            phù hợp" với các "nguyên tắc" của DDD.
        * **ABP Suite:** Hỗ trợ code generation cho DDD.

- **"Các Khái Niệm" "Cốt Lõi" Của DDD Trong ABP Framework (Chi Tiết):**

    **5.1. Entities (Thực Thể) và Value Objects (Đối Tượng Giá Trị):**

    *   **Entities (Thực thể):**
        *   **"Định nghĩa" (nhắc lại):** Entities là các **"đối tượng" "kinh doanh" (business objects)** "quan trọng"
            của ứng dụng, có **"danh tính" "duy nhất"** (unique identity) và **"vòng đời"** (lifecycle).
        *   **"Triển khai" trong ABP Framework:**
            *   "Kế thừa" từ lớp **`Entity`** hoặc **`AggregateRoot`** (sẽ "giải thích" ở phần sau).
            *   "Định nghĩa" **"khóa chính"** (primary key) (ID) của entity (thường là `Guid` hoặc `int`).
            *   "Định nghĩa" các **"thuộc tính"** (properties) và **"phương thức"** (methods) của entity.
            *   **"Ví dụ":**

                ```csharp
                // Entities/Product.cs (Entity)

                using System;
                using Volo.Abp.Domain.Entities;

                namespace MyProject.Products
                {
                    public class Product : Entity<Guid> // Kế thừa từ Entity<Guid> (Guid là kiểu dữ liệu của khóa chính)
                    {
                        public string Name { get; private set; } // Thuộc tính (property)
                        public string Description { get; set; }
                        public decimal Price { get; private set; }
                        public int StockCount { get; private set; }

                        // Constructor (hàm tạo)
                        private Product() { } // Private constructor (để EF Core có thể tạo entity khi truy vấn database)

                        public Product(Guid id, string name, decimal price, int stockCount) // Public constructor
                        {
                            Id = id;
                            Name = name;
                            Price = price;
                            StockCount = stockCount;
                        }

                        // Phương thức (methods)
                        public void DecreaseStock(int quantity)
                        {
                            if (StockCount < quantity)
                            {
                                throw new BusinessException("Not enough stock!"); // Ném ra ngoại lệ (exception) nếu không đủ hàng
                            }
                            StockCount -= quantity;
                        }

                        public void SetPrice(decimal price)
                        {
                          if(price <= 0)
                          {
                            throw new ArgumentException("...");
                          }

                          Price = price;
                        }
                    }
                }
                ```

    *   **Value Objects (Đối tượng giá trị):**
        *   **"Định nghĩa" (nhắc lại):** Value Objects là các **"đối tượng" "mô tả"** (descriptive objects) **"không
            có" "danh tính" "duy nhất"**. Value Objects "đại diện" cho các "khái niệm" "nhỏ" trong "miền nghiệp vụ" và "
            thường" được "dùng" để "nhóm" các "thuộc tính" "liên quan" lại với nhau.
        *   **"Triển khai" trong ABP Framework:**
            *   "Kế thừa" từ lớp **`ValueObject`**.
            *   "Định nghĩa" các **"thuộc tính"** (properties) của value object.
            *   **"Ghi đè"** (override) phương thức **`GetAtomicValues`** để "trả về" các "thuộc tính" "tạo nên" "giá
                trị" của value object. ABP Framework sẽ "dùng" phương thức này để "so sánh" hai value objects.
            *   **"Ví dụ":**

                ```csharp
                // ValueObjects/Address.cs (Value Object)

                using System.Collections.Generic;
                using Volo.Abp.Domain.Values;

                namespace MyProject.ValueObjects
                {
                    public class Address : ValueObject // Kế thừa từ ValueObject
                    {
                        public string Street { get; private set; }
                        public string City { get; private set; }
                        public string State { get; private set; }
                        public string ZipCode { get; private set; }

                        private Address() { } // Private constructor (để EF Core có thể tạo value object khi truy vấn database)

                        public Address(string street, string city, string state, string zipCode)
                        {
                            Street = street;
                            City = city;
                            State = state;
                            ZipCode = zipCode;
                        }

                        // Ghi đè phương thức GetAtomicValues để "trả về" các "thuộc tính" "tạo nên" "giá trị" của value object
                        protected override IEnumerable<object> GetAtomicValues()
                        {
                            yield return Street;
                            yield return City;
                            yield return State;
                            yield return ZipCode;
                        }
                    }
                }
                ```

    **5.2. Aggregates (Tập hợp) và Aggregate Roots:**

    *   **Aggregates (Tập hợp):**
        *   **"Định nghĩa" (nhắc lại):** Aggregates là **"nhóm"** các **Entities** và **Value Objects** "liên quan" "
            chặt chẽ" với nhau và được "quản lý" như một **"đơn vị" "duy nhất"**. Aggregates "đảm bảo" **"tính 'nhất
            quán' " (consistency)** và **"tính 'toàn vẹn' " (integrity)** của dữ liệu trong "miền nghiệp vụ".
        *   **"Ví dụ" (nhắc lại):** `Order` (Đơn hàng) là một Aggregate. `Order` có thể "chứa" các Entities và Value
            Objects "con" như `OrderItem` (Chi tiết đơn hàng), `Address` (Địa chỉ giao hàng), `PaymentMethod` (Phương
            thức thanh toán).

    *   **Aggregate Root:**
        *   **"Định nghĩa" (nhắc lại):** Aggregate Root là một **Entity "đặc biệt"** trong Aggregate, "đóng vai trò"
            là **"điểm truy cập" "duy nhất"** vào Aggregate. "Mọi thao tác" trên Aggregate phải được "thực hiện" thông
            qua Aggregate Root.
        *   **"Triển khai" trong ABP Framework:**
            *   Aggregate Root "kế thừa" từ lớp **`AggregateRoot`** (lớp `AggregateRoot` kế thừa từ lớp `Entity`).
            *   Aggregate Root "thường" là entity có **"khóa chính"** (ID) của Aggregate.
        *   **"Ví dụ":**

            ```csharp
            // Entities/Order.cs (Aggregate Root)

            using System;
            using System.Collections.Generic;
            using Volo.Abp.Domain.Entities.Auditing;

            namespace MyProject.Orders
            {
                public class Order : AggregateRoot<Guid> // Kế thừa từ AggregateRoot<Guid> (Guid là kiểu dữ liệu của khóa chính)
                {
                    public Guid CustomerId { get; private set; }
                    public DateTime OrderDate { get; private set; }
                    public Address ShippingAddress { get; private set; } // Value Object
                    public List<OrderItem> OrderItems { get; private set; } // Danh sách các OrderItem (Entity con)

                    private Order() { } // Private constructor

                    public Order(Guid id, Guid customerId, Address shippingAddress)
                    {
                        Id = id;
                        CustomerId = customerId;
                        OrderDate = DateTime.Now;
                        ShippingAddress = shippingAddress;
                        OrderItems = new List<OrderItem>();
                    }

                    // Phương thức để "thêm" OrderItem vào Order (phải thông qua Order - Aggregate Root)
                    public void AddOrderItem(Guid productId, string productName, decimal unitPrice, int quantity)
                    {
                        // Kiểm tra "quy tắc nghiệp vụ" (business rules) (ví dụ: kiểm tra xem sản phẩm có tồn tại không, số lượng có hợp lệ không, v.v.)
                        // ...

                        OrderItems.Add(new OrderItem(Guid.NewGuid(), Id, productId, productName, unitPrice, quantity)); // Tạo OrderItem mới và thêm vào danh sách
                    }

                    // ... (Các phương thức khác để "thao tác" trên Order)
                }
            }
            ```

            ```csharp
            // Entities/OrderItem.cs (Entity con của Order)
            using System;
            using Volo.Abp.Domain.Entities;
            namespace MyProject.Orders
            {
              public class OrderItem : Entity<Guid>
              {
                public Guid OrderId {get; private set;}
                public Guid ProductId {get; private set;}
                public string ProductName {get; private set;}
                public decimal UnitPrice {get; private set;}
                public int Quantity {get; private set;}
                private OrderItem(){}
                internal OrderItem(Guid id, Guid orderId, Guid productId, string productName, decimal unitPrice, int quantity): base(id)
                {
                  OrderId = orderId;
                  ProductId = productId;
                  ProductName = productName;
                  UnitPrice = unitPrice;
                  Quantity = quantity;
                }
              }
            }

            ```

    **5.3. Domain Services (Dịch vụ nghiệp vụ):**

    *   **"Định nghĩa" (nhắc lại):** Domain Services là các **"lớp"** (classes) "chứa" **"logic nghiệp vụ" (business
        logic) "phức tạp"** của ứng dụng. Domain Services "thực hiện" các **"quy tắc nghiệp vụ"** (business rules) và
        **"thao tác"** trên các Entities và Value Objects trong Domain Layer.
    *   **"Triển khai" trong ABP Framework:**
        *   Domain Services "thường" được "đặt" trong **Domain Layer**.
        *   Domain Services "thường" "kế thừa" từ lớp **`DomainService`** của ABP Framework (tùy chọn, nhưng "khuyến
            khích").
        *   Domain Services "thường" được "đăng ký" trong hệ thống **Dependency Injection (DI)** của ABP Framework.
        *   **"Ví dụ":**

            ```csharp
            // DomainServices/OrderManager.cs (Domain Service)

            using System;
            using System.Threading.Tasks;
            using MyProject.Orders;
            using Volo.Abp.Domain.Services;

            namespace MyProject.DomainServices
            {
                public class OrderManager : DomainService // Kế thừa từ DomainService
                {
                    private readonly IOrderRepository _orderRepository; // Inject IOrderRepository

                    public OrderManager(IOrderRepository orderRepository)
                    {
                        _orderRepository = orderRepository;
                    }

                    // Phương thức "xử lý" logic nghiệp vụ "phức tạp" (ví dụ: "tạo đơn hàng mới")
                    public async Task<Order> CreateOrderAsync(Guid customerId, Address shippingAddress, List<OrderItem> orderItems)
                    {
                        // Kiểm tra "quy tắc nghiệp vụ" (business rules) (ví dụ: kiểm tra xem khách hàng có tồn tại không, địa chỉ có hợp lệ không, v.v.)
                        // ...

                        // Tạo Order mới
                        var order = new Order(Guid.NewGuid(), customerId, shippingAddress);

                        // Thêm các OrderItem vào Order
                        foreach (var item in orderItems)
                        {
                            order.AddOrderItem(item.ProductId, item.ProductName, item.UnitPrice, item.Quantity);
                        }

                        // Lưu Order vào database thông qua Repository
                        await _orderRepository.InsertAsync(order);

                        return order;
                    }
                }
            }
            ```

    **5.4. Repositories (Kho chứa):**

    *  **"Định nghĩa" (nhắc lại):** Repositories là các "lớp" (classes) "cung cấp" một "lớp 'trừu tượng' " (
        abstraction layer) để "truy cập" dữ liệu (thường là từ database).
    * **Interface ở Domain Layer, Implementation ở Infrastructure Layer:**
    *   **"Triển khai" trong ABP Framework:**
        *   ABP Framework "cung cấp" **"giao diện" `IRepository<TEntity, TKey>`** (và các biến thể của nó) để bạn
            "định nghĩa" các Repositories cho các Entities của bạn.
        *   ABP Framework "cung cấp" các **"triển khai" "mặc định"** của `IRepository` cho **Entity Framework Core**
            và **MongoDB**. Bạn có thể "sử dụng" các "triển khai" "mặc định" này hoặc "tự mình" "triển khai"
            `IRepository` cho các "công nghệ" "truy cập" dữ liệu khác.
        *   **"Ví dụ":**

            ```csharp
            // Domain/Products/IProductRepository.cs (Repository Interface - trong Domain Layer)

            using System;
            using System.Collections.Generic;
            using System.Threading.Tasks;
            using Volo.Abp.Domain.Repositories;

            namespace MyProject.Products
            {
                public interface IProductRepository : IRepository<Product, Guid> // Kế thừa từ IRepository<Product, Guid> (Guid là kiểu dữ liệu của khóa chính)
                {
                    // Có thể "thêm" các phương thức "tùy chỉnh" để "truy vấn" dữ liệu (nếu cần)
                    // Ví dụ:
                    // Task<List<Product>> GetListByCategoryIdAsync(Guid categoryId);
                    // Task<Product> FindByNameAsync(string name);
                }
            }
            ```

**Tổng Kết Chương 5:**

-   Bạn đã "khám phá" **Domain-Driven Design (DDD)**, một "phương pháp luận" "thiết kế" phần mềm "hướng nghiệp vụ", và "
    cách" ABP Framework "hỗ trợ" "triển khai" DDD.
    -   "Hiểu" **Domain-Driven Design (DDD) là gì** ("phương pháp luận" "thiết kế" phần mềm "tập trung" vào "miền
        nghiệp vụ", "đặt" "nghiệp vụ" vào "trung tâm").
    -   "Nắm vững" các **"khái niệm" "cốt lõi" của DDD**: Domain, Ubiquitous Language, Bounded Context, Entities,
        Value Objects, Aggregates, Domain Services, Repositories, Domain Events.
    -   "Biết" cách ABP Framework **"hỗ trợ" "triển khai" DDD** (Layered Architecture, Base Classes for DDD Concepts,
        Domain Events, Repositories, Unit of Work, Dependency Injection).
    -   "Học cách" "triển khai" các "khái niệm" DDD (Entities, Value Objects, Aggregates, Domain Services,
        Repositories) trong ABP Framework bằng code C#.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: Application Services - " 'Cầu Nối' " Giữa " 'Ngoại Vi' " và " 'Nội Tại' "**. Chúng
ta sẽ "tìm hiểu" về **Application Services**, "vai trò" của Application Services trong kiến trúc ABP Framework, và "
cách" "tạo" và "sử dụng" Application Services để "triển khai" các **"use cases"** của ứng dụng.

Bạn có câu hỏi nào về Domain-Driven Design (DDD) và ABP Framework này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn
sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" ABP Framework.
