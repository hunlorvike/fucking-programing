# Data Fetching trong Next.js

## **Mục lục**

1. [Giới thiệu về Data Fetching](#1-gioi-thieu-ve-data-fetching)
2. [Các phương pháp Data Fetching](#2-cac-phuong-phap-data-fetching)
    1. [Server-side Rendering (SSR) với `getServerSideProps`](#21-server-side-rendering-ssr-voi-getserversideprops)
    2. [Static Site Generation (SSG) với `getStaticProps`](#22-static-site-generation-ssg-voi-getstaticprops)
    3. [Incremental Static Regeneration (ISR)](#23-incremental-static-regeneration-isr)
    4. [Client-side Fetching](#24-client-side-fetching)
3. [Phân biệt SSR, SSG, ISR và Client-side Fetching](#3-phan-biet-ssr-ssg-isr-va-client-side-fetching)
4. [Ví dụ thực tế](#4-vi-du-thuc-te)
5. [Lưu ý khi sử dụng Data Fetching trong Next.js](#5-luu-y-khi-su-dung-data-fetching-trong-nextjs)

---

### 1. **Giới thiệu về Data Fetching**

Data Fetching (lấy dữ liệu) là một phần quan trọng trong việc xây dựng các ứng dụng web động. Trong Next.js, bạn có thể
lấy dữ liệu ở nhiều giai đoạn khác nhau tùy thuộc vào yêu cầu của ứng dụng, như trên server, khi biên dịch, hoặc trên
client.

Next.js cung cấp các phương thức mạnh mẽ để xử lý data fetching như:

- **Server-side Rendering (SSR)**
- **Static Site Generation (SSG)**
- **Incremental Static Regeneration (ISR)**
- **Client-side Fetching**

---

### 2. **Các phương pháp Data Fetching**

#### 2.1. **Server-side Rendering (SSR) với `getServerSideProps`**

Server-side Rendering là phương pháp lấy dữ liệu trên server **mỗi khi có request**. Dữ liệu sẽ được render trên server
và trả về HTML tĩnh cho client.

##### **Cú pháp**:

```javascript
export async function getServerSideProps(context) {
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    return {
        props: {
            data,
        },
    };
}
```

##### **Đặc điểm**:

- Lý tưởng cho dữ liệu thay đổi thường xuyên.
- Thích hợp khi dữ liệu phụ thuộc vào request cụ thể (ví dụ: authentication, params).
- Thời gian render có thể chậm hơn so với SSG vì phải thực hiện trên mỗi request.

##### **Ví dụ**:

```javascript
function SSRPage({ data }) {
    return <div>{data.message}</div>;
}

export default SSRPage;
export async function getServerSideProps() {
    const res = await fetch('https://api.example.com/hello');
    const data = await res.json();

    return {
        props: { data },
    };
}
```

---

#### 2.2. **Static Site Generation (SSG) với `getStaticProps`**

SSG cho phép lấy dữ liệu **khi biên dịch (build time)** và tạo các trang tĩnh. Các trang này không được cập nhật cho đến
khi ứng dụng được rebuild.

##### **Cú pháp**:

```javascript
export async function getStaticProps() {
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    return {
        props: {
            data,
        },
    };
}
```

##### **Đặc điểm**:

- Lý tưởng cho dữ liệu không thay đổi thường xuyên.
- Tăng tốc độ tải trang vì nội dung đã được render trước (pre-rendered).
- Không phù hợp cho các ứng dụng cần dữ liệu thời gian thực.

##### **Ví dụ**:

```javascript
function SSGPage({ data }) {
    return <div>{data.message}</div>;
}

export default SSGPage;
export async function getStaticProps() {
    const res = await fetch('https://api.example.com/hello');
    const data = await res.json();

    return {
        props: { data },
    };
}
```

---

#### 2.3. **Incremental Static Regeneration (ISR)**

ISR cho phép các trang SSG được **cập nhật sau một khoảng thời gian** mà không cần rebuild toàn bộ ứng dụng.

##### **Cú pháp**:

```javascript
export async function getStaticProps() {
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    return {
        props: {
            data,
        },
        revalidate: 10, // Thời gian (tính bằng giây) để trang được cập nhật
    };
}
```

##### **Đặc điểm**:

- Lý tưởng cho dữ liệu thay đổi không quá thường xuyên.
- Kết hợp tốc độ của SSG và tính năng động của SSR.
- Tự động cập nhật trang trong nền (background regeneration).

##### **Ví dụ**:

```javascript
function ISRPage({ data }) {
    return <div>{data.message}</div>;
}

export default ISRPage;
export async function getStaticProps() {
    const res = await fetch('https://api.example.com/hello');
    const data = await res.json();

    return {
        props: { data },
        revalidate: 5, // Cập nhật trang mỗi 5 giây
    };
}
```

---

#### 2.4. **Client-side Fetching**

Dữ liệu được lấy trực tiếp trên trình duyệt sau khi trang đã được render. Sử dụng các thư viện như `fetch`, `axios`,
hoặc React Query.

##### **Ví dụ**:

```javascript
import { useEffect, useState } from 'react';

function ClientSidePage() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('https://api.example.com/data')
            .then((res) => res.json())
            .then((data) => setData(data));
    }, []);

    if (!data) return <div>Loading...</div>;

    return <div>{data.message}</div>;
}

export default ClientSidePage;
```

##### **Đặc điểm**:

- Phù hợp cho các ứng dụng cần dữ liệu động hoặc tương tác cao.
- Không tối ưu cho SEO nếu dữ liệu cần thiết cho nội dung chính của trang.

---

### 3. **Phân biệt SSR, SSG, ISR và Client-side Fetching**

| **Phương pháp** | **Thời điểm lấy dữ liệu**                 | **Ưu điểm**                          | **Nhược điểm**                              |
|-----------------|-------------------------------------------|--------------------------------------|---------------------------------------------|
| **SSR**         | Mỗi request                               | Dữ liệu luôn mới                     | Hiệu suất chậm hơn vì render trên server    |
| **SSG**         | Khi biên dịch (build time)                | Tăng hiệu suất, phù hợp dữ liệu tĩnh | Không phù hợp dữ liệu thay đổi thường xuyên |
| **ISR**         | Khi biên dịch và sau thời gian revalidate | Kết hợp hiệu suất của SSG và SSR     | Cần quản lý thời gian revalidate            |
| **Client-side** | Sau khi trang render trên client          | Tương tác tốt, cập nhật dữ liệu động | Không tối ưu cho SEO                        |

---

### 4. **Ví dụ thực tế**

```javascript
// pages/products.js
function ProductsPage({ products }) {
    return (
        <div>
            <h1>Products</h1>
            <ul>
                {products.map((product) => (
                    <li key={product.id}>{product.name}</li>
                ))}
            </ul>
        </div>
    );
}

export async function getStaticProps() {
    const res = await fetch('https://api.example.com/products');
    const products = await res.json();

    return {
        props: { products },
        revalidate: 60, // Cập nhật mỗi 60 giây
    };
}

export default ProductsPage;
```

---

### 5. **Lưu ý khi sử dụng Data Fetching trong Next.js**

1. **Chọn phương pháp phù hợp**: Xác định rõ yêu cầu về tốc độ, SEO và tính động của dữ liệu để chọn SSR, SSG, ISR hay
   Client-side Fetching.
2. **Tối ưu hóa API**: Đảm bảo các API sử dụng nhanh chóng và đáng tin cậy.
3. **Xử lý lỗi**: Kiểm tra lỗi trong các phương thức fetching (`try-catch`, kiểm tra status code, v.v.).
4. **Phân biệt dữ liệu quan trọng và không quan trọng**: Sử dụng SSR hoặc SSG cho nội dung chính, Client-side Fetching
   cho các phần không quan trọng với SEO.
5. **Quản lý state**: Sử dụng các thư viện như React Query hoặc Redux để xử lý dữ liệu động phức tạp.
