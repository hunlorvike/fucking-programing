# Caching trong Next.js với `next/cache`

## **Mục lục**

1. [Giới thiệu về Caching trong Next.js](#1-gioi-thieu-ve-caching-trong-nextjs)
2. [Caching với `next/cache`](#2-caching-voi-nextcache)
    1. [Sử dụng Cache trong Server-side Rendering (SSR)](#21-su-dung-cache-trong-server-side-rendering-ssr)
    2. [Sử dụng Cache trong Static Site Generation (SSG)](#22-su-dung-cache-trong-static-site-generation-ssg)
    3. [Sử dụng Cache với API Routes](#23-su-dung-cache-voi-api-routes)
3. [Phương pháp caching trong Next.js](#3-phuong-phap-caching-trong-nextjs)
    1. [Caching với HTTP Headers](#31-caching-voi-http-headers)
    2. [Incremental Static Regeneration (ISR) và Caching](#32-incremental-static-regeneration-isr-va-caching)
4. [Ví dụ thực tế về Caching trong Next.js](#4-vi-du-thuc-te-ve-caching-trong-nextjs)
5. [Lưu ý khi sử dụng Caching trong Next.js](#5-luu-y-khi-su-dung-caching-trong-nextjs)

---

### 1. **Giới thiệu về Caching trong Next.js**

Caching (lưu trữ tạm thời) là một kỹ thuật giúp tăng hiệu suất ứng dụng bằng cách giảm số lần truy xuất lại dữ liệu từ
các nguồn bên ngoài (như API hoặc cơ sở dữ liệu). Trong Next.js, caching có thể được sử dụng trong nhiều tình huống khác
nhau, chẳng hạn như khi rendering trang, khi gọi API, hoặc khi làm việc với static files.

Next.js cung cấp một số công cụ và kỹ thuật để caching, bao gồm `next/cache`, các HTTP headers, và khả năng tái sử dụng
dữ liệu đã được render (như với **Incremental Static Regeneration**).

---

### 2. **Caching với `next/cache`**

`next/cache` là một module cung cấp các API để dễ dàng quản lý caching trong Next.js. Module này giúp cache dữ liệu trên
server và client, và có thể kết hợp với các kỹ thuật khác như SSR, SSG, hoặc ISR.

#### 2.1. **Sử dụng Cache trong Server-side Rendering (SSR)**

Trong SSR, bạn có thể sử dụng `next/cache` để cache kết quả của các request bên server. Điều này giúp giảm thiểu thời
gian tải trang cho các request có cùng dữ liệu, tiết kiệm tài nguyên và cải thiện hiệu suất.

##### **Cú pháp**:

```javascript
import { cache } from 'next/cache';

export async function getServerSideProps(context) {
    const cacheKey = 'some-unique-key';

    // Kiểm tra nếu dữ liệu đã có trong cache
    const cachedData = cache.get(cacheKey);
    if (cachedData) {
        return { props: { data: cachedData } };
    }

    // Nếu không có trong cache, lấy dữ liệu mới
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    // Lưu dữ liệu vào cache
    cache.set(cacheKey, data, { ttl: 3600 }); // ttl là thời gian sống của cache (ví dụ 1 giờ)

    return { props: { data } };
}
```

##### **Đặc điểm**:

- **Cache expiration**: Bạn có thể thiết lập thời gian sống của cache (`ttl`) để đảm bảo dữ liệu được cập nhật định kỳ.
- **Chia sẻ cache giữa các request**: Cache có thể chia sẻ giữa các request giống nhau, giúp giảm tải cho server.

---

#### 2.2. **Sử dụng Cache trong Static Site Generation (SSG)**

Đối với SSG, các trang được render và cache sẵn tại build time. Bạn có thể kiểm soát thời gian tái tạo lại các trang đã
được render thông qua ISR (Incremental Static Regeneration), kết hợp với caching để tăng tốc độ và hiệu quả.

##### **Cú pháp**:

```javascript
export async function getStaticProps() {
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    return {
        props: { data },
        revalidate: 60, // Cập nhật dữ liệu mỗi 60 giây (ISR)
    };
}
```

##### **Đặc điểm**:

- Các trang đã được render sẽ được cache và phục vụ nhanh chóng cho người dùng.
- `revalidate` cho phép cache được tái tạo sau một thời gian (ISR), đảm bảo dữ liệu mới mà không cần phải rebuild lại
  toàn bộ ứng dụng.

---

#### 2.3. **Sử dụng Cache với API Routes**

Next.js cũng hỗ trợ caching trong các API Routes. Khi bạn sử dụng API Routes để xử lý các request, bạn có thể cache kết
quả của các truy vấn để giảm tải cho server hoặc API bên ngoài.

##### **Cú pháp**:

```javascript
export default async function handler(req, res) {
    const cacheKey = 'api-key';

    // Kiểm tra cache
    const cachedData = cache.get(cacheKey);
    if (cachedData) {
        return res.status(200).json(cachedData);
    }

    // Nếu không có trong cache, lấy dữ liệu và lưu vào cache
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();

    cache.set(cacheKey, data, { ttl: 300 }); // Lưu vào cache trong 5 phút
    return res.status(200).json(data);
}
```

##### **Đặc điểm**:

- Giảm thiểu thời gian phản hồi cho các request có cùng dữ liệu.
- Giúp API hoạt động hiệu quả hơn khi có nhiều request giống nhau.

---

### 3. **Phương pháp caching trong Next.js**

#### 3.1. **Caching với HTTP Headers**

Next.js hỗ trợ caching qua HTTP headers, đặc biệt là trong SSR và API Routes. Bạn có thể sử dụng các headers như
`Cache-Control` để chỉ định cách thức cache cho các tài nguyên của ứng dụng.

##### **Ví dụ**:

```javascript
export default function handler(req, res) {
    res.setHeader('Cache-Control', 'public, max-age=3600, stale-while-revalidate=59');
    res.status(200).json({ message: 'Hello, World!' });
}
```

##### **Đặc điểm**:

- **`Cache-Control`**: Chỉ định cách cache các tài nguyên. Ví dụ: `public` cho phép cache ở bất kỳ nơi nào,
  `max-age=3600` cho phép cache trong 1 giờ.
- **`stale-while-revalidate`**: Cho phép sử dụng dữ liệu đã cache trong khi đang làm mới dữ liệu.

---

#### 3.2. **Incremental Static Regeneration (ISR) và Caching**

ISR kết hợp với caching giúp các trang đã được generate (tĩnh) vẫn có thể được cập nhật định kỳ mà không cần rebuild lại
toàn bộ ứng dụng. Caching trong ISR đảm bảo các trang được phục vụ nhanh chóng và tiết kiệm tài nguyên.

##### **Cú pháp**:

```javascript
export async function getStaticProps() {
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    return {
        props: { data },
        revalidate: 60, // Cập nhật dữ liệu mỗi 60 giây (ISR)
    };
}
```

##### **Đặc điểm**:

- Caching dữ liệu tĩnh giúp giảm thời gian load trang.
- Cập nhật dữ liệu sau mỗi lần tái tạo lại mà không cần rebuild toàn bộ ứng dụng.

---

### 4. **Ví dụ thực tế về Caching trong Next.js**

Dưới đây là một ví dụ về cách kết hợp `next/cache` và HTTP caching trong API Routes:

```javascript
// pages/api/data.js
import { cache } from 'next/cache';

export default async function handler(req, res) {
    const cacheKey = 'unique-data-key';

    // Kiểm tra cache
    const cachedData = cache.get(cacheKey);
    if (cachedData) {
        return res.status(200).json(cachedData);
    }

    // Nếu không có trong cache, lấy dữ liệu từ API
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();

    // Lưu vào cache
    cache.set(cacheKey, data, { ttl: 600 }); // cache dữ liệu trong 10 phút

    res.setHeader('Cache-Control', 'public, max-age=600, stale-while-revalidate=59');
    return res.status(200).json(data);
}
```

---

### 5. **Lưu ý khi sử dụng Caching trong Next.js**

1. **Quản lý thời gian sống của cache**: Đảm bảo thời gian sống của cache (`ttl`) phù hợp với loại dữ liệu bạn đang
   cache. Dữ liệu thay đổi thường xuyên không nên cache quá lâu.
2. **Cache control headers**: Khi sử dụng caching với HTTP headers, hãy sử dụng `Cache-Control` một cách hợp lý để kiểm
   soát cách thức và thời gian cache.
3. **Cache invalidation**: Cần lưu ý về việc làm mới hoặc hủy bỏ cache khi dữ liệu thay đổi. ISR có thể giúp bạn tái tạo
   dữ liệu mà không cần rebuild toàn bộ ứng dụng.
4. **Đảm bảo đồng bộ hóa

cache**: Nếu bạn có nhiều server, hãy đảm bảo cache được đồng bộ giữa chúng (sử dụng Redis hoặc một dịch vụ caching phân
tán).

Bằng cách sử dụng caching hợp lý, Next.js có thể giúp bạn tối ưu hóa hiệu suất và giảm tải cho server, đặc biệt là khi
ứng dụng của bạn phát triển lớn và có lưu lượng người dùng cao.
