# Tài liệu Cấu trúc Dự án Next.js

## Giới thiệu

Tài liệu này cung cấp cái nhìn tổng quan toàn diện về cấu trúc dự án của một ứng dụng Next.js, chi tiết các tệp và thư mục tạo nên một cấu hình Next.js điển hình. Nó nhấn mạnh cả các thư mục cấp cao và lồng ghép, các tệp cấu hình, cũng như các quy tắc định tuyến, giúp bạn hiểu rõ hơn về cách tổ chức và quản lý các dự án Next.js một cách hiệu quả.

## Bắt đầu

Để bắt đầu sử dụng Next.js, bạn cần thiết lập cấu trúc dự án một cách chính xác. Dưới đây là cấu trúc điển hình mà bạn nên theo trong một ứng dụng Next.js, đặc biệt khi sử dụng thư mục src để tổ chức mã nguồn tốt hơn.

## Cấu trúc Dự án

```
next-app/
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   ├── hooks/
│   ├── utils/
│   ├── contexts/
│   ├── lib/
│   ├── middlewares/
│   └── services/
├── .env.local
├── .gitignore
├── next.config.js
├── package.json
└── README.md
```

Cấu trúc này được thiết kế để nâng cao tổ chức, khả năng bảo trì và khả năng mở rộng của ứng dụng của bạn.

## Giải thích chi tiết từng thư mục

### 1. **public/**

Chứa các tài nguyên tĩnh không cần xử lý. Tệp tin trong thư mục này sẽ được phục vụ trực tiếp từ gốc của ứng dụng, như favicon, ảnh nền, và các tệp tĩnh khác.

### 2. **src/**

Thư mục chứa mã nguồn chính của ứng dụng, giúp tổ chức và quản lý mã dễ dàng hơn.

- **components/**:
  Chứa các thành phần giao diện tái sử dụng, có thể được chia thành nhiều tệp nhỏ hơn cho logic và style. Ví dụ:

  ```
  src/components/Button.tsx
  src/components/Header.tsx
  ```

- **pages/**:
  Mỗi tệp trong thư mục này tự động trở thành một route. Có thể tạo các route động bằng dấu ngoặc vuông (ví dụ: `pages/[id].tsx`).

  - **api/**: Thư mục con dành riêng cho các API route, cho phép tạo các endpoint mà không cần backend riêng biệt.
  - **index.tsx**: Tệp này định nghĩa route chính của ứng dụng (trang chính).
  - **about.tsx**: Tệp này định nghĩa route cho trang "Giới thiệu".
  - **products/**:
    - **index.tsx**: Danh sách tất cả sản phẩm.
    - **[id].tsx**: Chi tiết sản phẩm cụ thể, nơi `id` là tham số động.

- **styles/**:
  Chứa các tệp CSS hoặc CSS modules cho từng component, cũng có thể tích hợp SCSS hoặc CSS-in-JS. Ví dụ:

  ```
  src/styles/global.css
  src/styles/Button.module.css
  ```

- **hooks/**:
  Nơi chứa các custom hook của React, giúp tái sử dụng logic trong ứng dụng. Ví dụ:

  ```
  src/hooks/useFetch.ts
  ```

- **utils/**:
  Chứa các hàm tiện ích dùng chung cho ứng dụng, như format date hay tính toán. Ví dụ:

  ```
  src/utils/formatDate.ts
  ```

- **contexts/**:
  Chứa các context cho React Context API, cho phép quản lý state toàn cục cho ứng dụng. Ví dụ:

  ```
  src/contexts/AuthContext.tsx
  ```

- **lib/**:
  Thư mục chứa các thư viện hoặc module bên ngoài tích hợp vào ứng dụng. Ví dụ:

  ```
  src/lib/apiClient.ts
  ```

- **middlewares/**:
  Chứa các middleware cho server-side hoặc client-side, giúp kiểm soát truy cập và xử lý dữ liệu. Ví dụ:

  ```
  src/middlewares/authMiddleware.ts
  ```

- **services/**:
  Nơi chứa logic liên quan đến việc tương tác với backend, như gọi API và xử lý các yêu cầu. Ví dụ:
  ```
  src/services/productService.ts
  ```

### 3. **Các tệp cấu hình chính bên ngoài src**

- **next.config.js**:
  Chứa các cấu hình tùy chỉnh cho Next.js, cho phép bạn mở rộng và tùy chỉnh hành vi của ứng dụng.

- **.env.local**:
  Lưu trữ các biến môi trường nhạy cảm như API keys mà không muốn đẩy lên repository.

- **package.json**:
  Quản lý tất cả các dependency của dự án, các script để chạy ứng dụng, và các thông tin liên quan đến dự án như tên, phiên bản, tác giả, v.v.

## Quy tắc Định tuyến

### 1. **Quy tắc Định tuyến Ứng dụng**

Thư mục `app` (nếu sử dụng) cung cấp các quy tắc cụ thể để định nghĩa các route và xử lý metadata:

- **Tệp Định tuyến**:

  - **layout.tsx**: Định nghĩa layout cho các trang, cho phép chia sẻ cấu trúc chung giữa các trang. Ví dụ:

    ```tsx
    // src/app/layout.tsx
    import React from 'react';

    const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
      return (
        <div>
          <header>Header Content</header>
          <main>{children}</main>
          <footer>Footer Content</footer>
        </div>
      );
    };

    export default Layout;
    ```

  - **page.tsx**: Định nghĩa một trang cụ thể, nơi bạn có thể đặt nội dung của trang. Ví dụ:

    ```tsx
    // src/app/about/page.tsx
    const AboutPage: React.FC = () => {
      return <div>Giới thiệu về ứng dụng</div>;
    };

    export default AboutPage;
    ```

  - **loading.tsx**: Thành phần giao diện loading hiển thị trong quá trình tải trang. Ví dụ:

    ```tsx
    // src/app/loading.tsx
    const Loading: React.FC = () => {
      return <div>Đang tải...</div>;
    };

    export default Loading;
    ```

  - **not-found.tsx**: Thành phần giao diện hiển thị khi không tìm thấy trang yêu cầu. Ví dụ:

    ```tsx
    // src/app/not-found.tsx
    const NotFound: React.FC = () => {
      return <div>Trang không tồn tại!</div>;
    };

    export default NotFound;
    ```

  - **error.tsx**: Thành phần giao diện cho việc xử lý lỗi. Ví dụ:

    ```tsx
    // src/app/error.tsx
    const ErrorPage: React.FC = () => {
      return <div>Đã xảy ra lỗi!</div>;
    };

    export default ErrorPage;
    ```

  - **global-error.tsx**: Xử lý lỗi toàn cục cho toàn bộ ứng dụng. Ví dụ:

    ```tsx
    // src/app/global-error.tsx
    const GlobalError: React.FC = () => {
      return <div>Lỗi xảy ra trong toàn bộ ứng dụng!</div>;
    };

    export default GlobalError;
    ```

  - **route.ts**: Định nghĩa các endpoint API cho ứng dụng.

### 2. **Các Route Lồng Ghép**

- **folder/**: Một thư mục xác định một segment route, giúp phân chia các route thành các nhóm hợp lý.
- **[folder]**: Một segment route động, cho phép định nghĩa các route có tham số. Ví dụ:

  ```tsx
  // src/app/products/[id].tsx
  const ProductDetail: React.FC<{ params: { id: string } }> = ({ params }) => {
    return <div>Chi tiết sản phẩm với ID: {params.id}</div>;
  };

  export default ProductDetail;
  ```

- **[...folder]**: Một segment route catch-all, cho phép định nghĩa các route có thể khớp với nhiều giá trị.

### 3. **Nhóm Route và Thư mục Riêng**

- **(folder)**: Nhóm các route mà không ảnh hưởng đến định tuyến, cho phép tổ chức mã nguồn tốt hơn mà không làm ảnh hưởng đến các route.
- **\_folder**: Loại bỏ một thư mục và tất cả các segment con của nó khỏi định tuyến, giúp kiểm soát rõ hơn về các route có sẵn.

### 4. **Quy tắc Tệp Metadata**

Đối với SEO và xử lý metadata, bạn có thể sử dụng:

- **favicon.ico**: Favicon cho ứng dụng của bạn.
- **opengraph-image**: Hình ảnh Open Graph cho việc chia sẻ trên mạng xã hội.
- **robots.txt**: Cấu hình cho việc lập chỉ mục bởi công cụ tìm kiếm.

### 5. **Quy tắc Định tuyến Trang**

Đối với router trang, hãy làm theo các quy tắc này:

- **Tệp Đặc Biệt**:

  - **\_app.tsx**: Custom App cho cài đặt toàn cầu, nơi bạn có thể cấu hình các provider và global styles.
  - **\_document.tsx**: Custom Document cho Server-Side Rendering (SSR), cho phép bạn tùy chỉnh phần HTML đầu ra.
  - **\_error.tsx**: Trang Lỗi Tùy Chỉnh cho việc xử lý lỗi.
  - **404.tsx**: Trang Lỗi 404 Tùy Chỉnh, hiển thị khi người dùng truy cập vào một route không tồn tại.

- **Các Route Động**:
  - **[folder]/index.tsx**: Segment route động, cho phép tạo các route với tham số.
  - **[[...folder]]/index.tsx**: Segment route catch-all tùy chọn, cho phép khớp với nhiều route.

## Lợi ích của Việc Sử dụng Thư mục src

1. **Cải thiện Tổ chức**: Sự phân tách rõ ràng giữa mã nguồn và các tệp cấu hình giúp dự án dễ dàng điều hướng.
2. **Tăng cường Tính Tái Sử Dụng**: Các thành phần, hook và tiện ích dễ dàng tái sử dụng, khuyến khích các nguyên tắc DRY (Don't Repeat Yourself).
3. **Khả Năng Mở Rộng**: Một dự án có cấu trúc tốt có thể phát triển dễ dàng hơn, cho phép thêm các tính năng mới mà không làm phức tạp mã nguồn hiện tại.

## Kết luận

Việc sử dụng thư mục `src` trong một dự án Next.js giúp nâng cao đáng kể tổ chức và khả năng bảo trì của mã nguồn của bạn. Một cấu trúc dự án rõ ràng không chỉ tạo điều kiện thuận lợi cho việc hợp tác giữa các lập trình viên mà còn tối ưu hóa quy trình phát triển khi ứng dụng mở rộng. Bằng cách tuân theo các quy tắc và phương pháp tốt nhất này, bạn có thể tạo ra một ứng dụng Next.js mạnh mẽ, dễ quản lý và mở rộng theo thời gian.

Hy vọng tài liệu này sẽ hữu ích cho bạn trong việc phát triển và quản lý ứng dụng Next.js của mình!
