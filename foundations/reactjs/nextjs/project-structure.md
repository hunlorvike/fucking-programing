# Tài liệu Cấu trúc Dự án Next.js

## Mục Lục

1. [Giới thiệu](#1-giới-thiệu)  
2. [Cấu trúc Thư mục Dự án](#2-cấu-trúc-thư-mục-dự-án)  
3. [Chi Tiết Các Thư Mục và Tệp](#3-chi-tiết-các-thư-mục-và-tệp)  
4. [Quy Tắc Định Tuyến](#4-quy-tắc-định-tuyến)  
5. [Best Practices](#5-best-practices)  
6. [Kết Luận](#6-kết-luận)  

---

## 1. Giới thiệu

### 1.1 Cấu trúc Dự án trong Next.js

Cấu trúc dự án trong Next.js đóng vai trò cốt lõi, giúp tổ chức mã nguồn một cách khoa học và dễ bảo trì. Next.js hỗ trợ một mô hình thư mục dựa trên hệ thống định tuyến file, cho phép tự động ánh xạ các tệp và thư mục thành các route.

### 1.2 Tại sao cần tổ chức cấu trúc tốt?

- **Quản lý dễ dàng**: Phân chia rõ ràng giúp tìm kiếm và chỉnh sửa dễ hơn.  
- **Tăng năng suất**: Dễ dàng mở rộng hoặc thêm các tính năng mới mà không làm phức tạp mã nguồn.  
- **Khả năng bảo trì**: Hỗ trợ team phát triển duy trì và phát triển dự án lâu dài.  

---

## 2. Cấu trúc Thư mục Dự án

Dưới đây là cấu trúc dự án Next.js điển hình:

```
next-app/
├── public/
├── src/
│   ├── app/
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

---

## 3. Chi Tiết Các Thư Mục và Tệp

### 3.1 **Thư mục chính**

#### **`public/`**
Chứa các tài nguyên tĩnh như hình ảnh, favicon, tệp tải xuống, v.v.

- **Đặc điểm**: Tất cả tệp trong thư mục này sẽ được phục vụ tại gốc URL.  
- **Ví dụ**:  
  ```
  public/favicon.ico -> https://example.com/favicon.ico
  ```

#### **`src/`**
Nơi chứa toàn bộ mã nguồn chính, phân chia thành các phần như sau:

1. **`app/`**  
   - Sử dụng với App Router (Next.js 13+).  
   - Cấu trúc này tổ chức các route bằng cách chia nhỏ thành **layouts**, **pages**, **loading**, và **error boundaries**.  
   - **Ví dụ**:
     ```
     src/app/
     ├── layout.tsx       # Layout gốc
     ├── page.tsx         # Trang chính (/)
     ├── about/
     │   └── page.tsx     # Trang About (/about)
     └── blog/
         ├── layout.tsx   # Layout cho blog
         ├── page.tsx     # Trang Blog (/blog)
         └── [slug]/page.tsx  # Bài viết động (/blog/:slug)
     ```

2. **`components/`**  
   - Chứa các thành phần UI tái sử dụng.  
   - **Ví dụ**:  
     ```
     src/components/Button.tsx
     src/components/Navbar.tsx
     ```

3. **`pages/`**  
   - Sử dụng với Pages Router.  
   - Mỗi tệp là một route, hỗ trợ các route động và API route.  
   - **Ví dụ**:
     ```
     src/pages/
     ├── index.tsx      # Trang chính (/)
     ├── about.tsx      # Trang Giới thiệu (/about)
     └── api/
         └── posts.ts   # API route (/api/posts)
     ```

4. **`styles/`**  
   - Chứa các tệp CSS hoặc SCSS toàn cục và module CSS.  
   - **Ví dụ**:
     ```
     src/styles/global.css
     src/styles/Home.module.css
     ```

5. **`hooks/`**  
   - Chứa các custom hooks dùng chung.  
   - **Ví dụ**:  
     ```
     src/hooks/useAuth.ts
     src/hooks/useFetch.ts
     ```

6. **`utils/`**  
   - Chứa các hàm tiện ích dùng chung trong ứng dụng.  
   - **Ví dụ**:  
     ```
     src/utils/formatDate.ts
     src/utils/calculateTotal.ts
     ```

7. **`contexts/`**  
   - Chứa các React Context để quản lý state toàn cục.  
   - **Ví dụ**:  
     ```
     src/contexts/AuthContext.tsx
     ```

8. **`lib/`**  
   - Chứa các thư viện tích hợp hoặc các helper liên quan tới backend.  
   - **Ví dụ**:  
     ```
     src/lib/apiClient.ts
     src/lib/db.ts
     ```

9. **`middlewares/`**  
   - Chứa middleware để xử lý logic trước hoặc sau các thao tác.  
   - **Ví dụ**:  
     ```
     src/middlewares/authMiddleware.ts
     ```

10. **`services/`**  
    - Chứa logic tương tác với backend (API calls, xử lý dữ liệu).  
    - **Ví dụ**:  
      ```
      src/services/userService.ts
      src/services/productService.ts
      ```

---

### 3.2 **Các tệp cấu hình chính**

- **`next.config.js`**: Tệp cấu hình Next.js (ví dụ: tối ưu hình ảnh, cấu hình alias).  
- **`.env.local`**: Lưu trữ các biến môi trường nhạy cảm như API key.  
- **`package.json`**: Quản lý dependencies và các script cho dự án.  
- **`.gitignore`**: Tệp để loại trừ các file/thư mục không muốn đẩy lên Git.

---

## 4. Quy Tắc Định Tuyến

### 4.1 App Router (Thư mục `app/`)
1. **File-based Routing**:  
   - Mỗi tệp trong thư mục `app` là một route.  
   - Sử dụng `layout.tsx`, `page.tsx`, `error.tsx`, và `loading.tsx` để tối ưu hóa giao diện và xử lý trạng thái.  

2. **Dynamic Routes**:  
   - Tạo các route động bằng cách sử dụng dấu ngoặc vuông.  
   - **Ví dụ**:  
     ```
     src/app/products/[id]/page.tsx
     ```

3. **Metadata SEO**:  
   - Cấu hình metadata như title và description.  
   - **Ví dụ**:  
     ```tsx
     export async function generateMetadata({ params }) {
       return {
         title: `Sản phẩm ${params.id}`,
         description: `Chi tiết sản phẩm ${params.id}`,
       };
     }
     ```

### 4.2 Pages Router (Thư mục `pages/`)
1. **Dynamic Routes**:  
   - **Ví dụ**:  
     ```
     src/pages/products/[id].tsx
     ```

2. **API Routes**:  
   - **Ví dụ**:  
     ```
     src/pages/api/users.ts
     ```

---

## 5. Best Practices

1. **Sử dụng thư mục `src/`**: Giúp phân biệt rõ ràng giữa mã nguồn và tệp cấu hình.  
2. **Tách biệt logic**:  
   - Sử dụng `services/` cho các API calls.  
   - Sử dụng `utils/` cho các hàm tiện ích.  
3. **Tái sử dụng thành phần**: Lưu tất cả UI components trong thư mục `components/`.  
4. **Định nghĩa rõ ràng metadata**: Tối ưu SEO cho mỗi route với metadata.  
5. **Sử dụng Middleware**: Quản lý quyền truy cập và bảo mật dễ dàng.  

---

## 6. Kết Luận

Cấu trúc dự án rõ ràng là bước đầu tiên để xây dựng một ứng dụng mạnh mẽ, dễ bảo trì và mở rộng. Bằng cách áp dụng các quy tắc trong tài liệu này, bạn sẽ tối ưu hóa quy trình phát triển và cải thiện hiệu suất ứng dụng của mình.