# Hướng Dẫn Chi Tiết về Routes trong Next.js 14

## Mục Lục

1. [Giới thiệu](#1-giới-thiệu)
2. [Cấu trúc Routes Cơ Bản](#2-cấu-trúc-routes-cơ-bản)
3. [Các Loại Routes Nâng Cao](#3-các-loại-routes-nâng-cao)
4. [Server và Client Components](#4-server-và-client-components)
5. [Xử Lý Lỗi và Loading States](#5-xử-lý-lỗi-và-loading-states)
6. [Best Practices và Tối Ưu Hóa](#6-best-practices-và-tối-ưu-hóa)

## 1. Giới thiệu

### 1.1 Routes trong Next.js là gì?

Routes trong Next.js là cơ chế xác định cách ứng dụng phản hồi với các URL khác nhau. Next.js 14 sử dụng hệ thống định tuyến dựa trên file (file-based routing) với hai loại chính:

- **App Router** (Mới - từ Next.js 13): Nằm trong thư mục `app/`
- **Pages Router** (Cũ): Nằm trong thư mục `pages/`

### 1.2 Tại sao cần hiểu rõ về Routes?

- Tối ưu hóa SEO
- Cải thiện trải nghiệm người dùng
- Quản lý state và data fetching hiệu quả
- Tăng hiệu suất ứng dụng

## 2. Cấu trúc Routes Cơ Bản

### 2.1 Cấu Trúc Thư Mục App

```plaintext
app/
├── layout.js        # Layout chung
├── page.js          # Trang chủ (/)
├── about/
│   └── page.js      # Trang About (/about)
└── blog/
    ├── layout.js    # Layout cho blog
    └── page.js      # Trang Blog (/blog)
```

### 2.2 File Đặc Biệt

| File | Mục đích |
|------|----------|
| `layout.js` | Layout chung cho nhiều trang |
| `page.js` | UI của route |
| `loading.js` | Loading UI |
| `error.js` | Error UI |
| `not-found.js` | UI khi không tìm thấy trang |

### 2.3 Ví Dụ Cơ Bản

```typescript
// app/page.tsx
export default function HomePage() {
  return (
    <div>
      <h1>Trang Chủ</h1>
    </div>
  );
}
```

```typescript
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="vi">
      <body>
        <nav>
          {/* Navigation */}
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
```

## 3. Các Loại Routes Nâng Cao

### 3.1 Dynamic Routes

Dynamic Routes cho phép tạo các trang với tham số động:

```plaintext
app/
└── blog/
    └── [slug]/
        └── page.js   # /blog/bai-viet-1
```

```typescript
// app/blog/[slug]/page.tsx
export default function BlogPost({
  params,
}: {
  params: { slug: string };
}) {
  return <h1>Bài viết: {params.slug}</h1>;
}

// Tạo các trang tĩnh khi build
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map((post) => ({
    slug: post.slug,
  }));
}
```

### 3.2 Group Routes

Group Routes giúp tổ chức code mà không ảnh hưởng URL:

```plaintext
app/
└── (marketing)/
    ├── about/
    │   └── page.js   # /about
    └── team/
        └── page.js   # /team
```

### 3.3 Parallel Routes

Cho phép render nhiều page cùng lúc:

```plaintext
app/
├── @dashboard/
│   └── page.js
└── @analytics/
    └── page.js
```

```typescript
// app/layout.tsx
export default function Layout({
  dashboard,
  analytics,
}: {
  dashboard: React.ReactNode;
  analytics: React.ReactNode;
}) {
  return (
    <div className="flex">
      <div>{dashboard}</div>
      <div>{analytics}</div>
    </div>
  );
}
```

### 3.4 Intercepting Routes

Dùng để chặn và xử lý routes:

```plaintext
app/
├── feed/
│   └── page.js
└── (.)feed/
    └── photo/[id]/
        └── page.js
```

## 4. Server và Client Components

### 4.1 Server Components

```typescript
// app/users/page.tsx
async function getUsers() {
  const res = await fetch('https://api.example.com/users');
  return res.json();
}

export default async function UsersPage() {
  const users = await getUsers();
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 4.2 Client Components

```typescript
'use client';

// app/components/Counter.tsx
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Đếm: {count}
    </button>
  );
}
```

## 5. Xử Lý Lỗi và Loading States

### 5.1 Error Boundary

```typescript
// app/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Đã xảy ra lỗi!</h2>
      <button onClick={() => reset()}>Thử lại</button>
    </div>
  );
}
```

### 5.2 Loading UI

```typescript
// app/loading.tsx
export default function Loading() {
  return (
    <div className="flex justify-center">
      <div className="animate-spin h-10 w-10 border-4 rounded-full" />
    </div>
  );
}
```

## 6. Best Practices và Tối Ưu Hóa

### 6.1 Tối Ưu SEO

```typescript
// app/blog/[slug]/page.tsx
import { Metadata } from 'next';

export async function generateMetadata({
  params,
}: {
  params: { slug: string };
}): Promise<Metadata> {
  const post = await getPost(params.slug);
  
  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      images: [post.image],
    },
  };
}
```

### 6.2 Route Handlers

```typescript
// app/api/posts/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  const posts = await getPosts();
  return NextResponse.json(posts);
}

export async function POST(request: Request) {
  const data = await request.json();
  const newPost = await createPost(data);
  return NextResponse.json(newPost, { status: 201 });
}
```

### 6.3 Middleware

```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');
  
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  return NextResponse.next();
}

export const config = {
  matcher: '/dashboard/:path*',
};
```

## Kết Luận

Next.js 14 cung cấp một hệ thống routing mạnh mẽ và linh hoạt, cho phép xây dựng các ứng dụng web phức tạp một cách có tổ chức. Việc hiểu và áp dụng đúng các khái niệm về routing sẽ giúp tối ưu hóa hiệu suất và trải nghiệm người dùng của ứng dụng.
