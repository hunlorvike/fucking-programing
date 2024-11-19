# Middleware trong Next.js

## **Mục lục**

1. [Giới thiệu về Middleware trong Next.js](#1-gioi-thieu-ve-middleware-trong-nextjs)
2. [Cài đặt Middleware trong Next.js](#2-cai-dat-middleware-trong-nextjs)
   1. [Tạo file Middleware](#21-tao-file-middleware)
   2. [Cấu trúc Middleware](#22-cau-truc-middleware)
   3. [Sử dụng Middleware trong Next.js](#23-su-dung-middleware-trong-nextjs)
3. [Cách tổ chức Middleware một cách mô-đun](#3-cach-to-chuc-middleware-mot-cach-mo-dun)
4. [Các tính năng và tác dụng của Middleware trong Next.js](#4-cac-tinh-nang-va-tac-dung-cua-middleware-trong-nextjs)
5. [Ví dụ thực tế về Middleware](#5-vi-du-thuc-te-ve-middleware)
6. [Lưu ý khi sử dụng Middleware trong Next.js](#6-luu-y-khi-su-dung-middleware-trong-nextjs)

---

### 1. **Giới thiệu về Middleware trong Next.js**

Middleware trong Next.js là một đoạn mã được thực thi trong quá trình xử lý yêu cầu HTTP, trước khi yêu cầu đó đến các route handler hoặc sau khi route handler trả về kết quả. Middleware giúp bạn có thể can thiệp vào chuỗi yêu cầu và phản hồi HTTP, như xác thực người dùng, kiểm tra quyền truy cập, hoặc xử lý dữ liệu đầu vào.

Middleware trong Next.js được hỗ trợ từ phiên bản Next.js 12. Nó giúp tăng cường khả năng quản lý logic xử lý các yêu cầu và giúp tối ưu hóa ứng dụng bằng cách giảm thiểu sự phức tạp của các API route hoặc các handler cụ thể.

---

### 2. **Cài đặt Middleware trong Next.js**

#### 2.1. **Tạo file Middleware**

Để sử dụng Middleware trong Next.js, bạn cần tạo một file có tên là `middleware.ts` hoặc `middleware.js` ở thư mục gốc của dự án, cùng cấp với thư mục `pages` hoặc `app` trong cấu trúc dự án.

Cấu trúc thư mục:

```
/my-nextjs-app
  /app
    /page.tsx
  /middleware.ts
  /pages
    /index.tsx
```

#### 2.2. **Cấu trúc Middleware**

File `middleware.ts` có thể chứa logic xử lý yêu cầu HTTP, và có thể được áp dụng cho tất cả các yêu cầu hoặc chỉ một số yêu cầu cụ thể.

Dưới đây là cấu trúc cơ bản của một middleware:

```ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Middleware sẽ được gọi với mỗi yêu cầu
export function middleware(request: NextRequest) {
  // Logic xử lý yêu cầu tại đây
  // Ví dụ: kiểm tra cookie, xác thực người dùng, vv.
  
  // Trả về NextResponse để tiếp tục xử lý hoặc thay đổi phản hồi
  return NextResponse.next();
}
```

#### 2.3. **Sử dụng Middleware trong Next.js**

Middleware có thể được áp dụng cho các route cụ thể hoặc toàn bộ ứng dụng. Bạn có thể xác định phạm vi của Middleware bằng cách sử dụng các điều kiện dựa trên URL, headers, hoặc các thuộc tính khác của yêu cầu.

##### Ví dụ về Middleware toàn cục:

Nếu bạn muốn áp dụng Middleware cho tất cả các yêu cầu của ứng dụng:

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Kiểm tra cookie hoặc xác thực người dùng tại đây
  if (!request.cookies.has('auth-token')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Tiếp tục xử lý yêu cầu nếu người dùng đã đăng nhập
  return NextResponse.next();
}
```

##### Ví dụ về Middleware cho các route cụ thể:

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Chỉ áp dụng Middleware cho các route có URL bắt đầu với "/admin"
export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith('/admin')) {
    // Kiểm tra quyền truy cập cho người dùng admin
    if (!request.cookies.has('admin-token')) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }

  return NextResponse.next();
}
```

---

### 3. **Cách tổ chức Middleware một cách mô-đun**

Trong một dự án lớn, bạn có thể muốn chia Middleware ra thành các module con để dễ quản lý và tái sử dụng. Để làm điều này, bạn có thể tạo nhiều file Middleware và nhập chúng vào trong file `middleware.ts` chính.

Ví dụ, bạn có thể có một file `auth-middleware.ts` cho logic xác thực:

```ts
// lib/middleware/auth-middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function authMiddleware(request: NextRequest) {
  if (!request.cookies.has('auth-token')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}
```

Sau đó, trong file `middleware.ts` chính, bạn có thể nhập và sử dụng middleware này:

```ts
// middleware.ts
import { authMiddleware } from './lib/middleware/auth-middleware';

export function middleware(request: NextRequest) {
  return authMiddleware(request);
}
```

Bằng cách này, bạn có thể tái sử dụng và dễ dàng bảo trì các phần logic trong Middleware.

---

### 4. **Các tính năng và tác dụng của Middleware trong Next.js**

Middleware cung cấp nhiều tính năng hữu ích trong ứng dụng Next.js, bao gồm:

- **Xác thực và quyền truy cập**: Kiểm tra người dùng có quyền truy cập vào một route hay không, ví dụ: kiểm tra token, cookie, hoặc session.
- **Chuyển hướng (Redirects)**: Tự động chuyển hướng người dùng đến các trang khác nếu họ không đáp ứng được yêu cầu xác thực hoặc quyền truy cập.
- **Tiền xử lý dữ liệu (Preprocessing)**: Xử lý các yêu cầu HTTP trước khi chúng đến các route handler, như định dạng lại dữ liệu, lọc query string, hoặc điều chỉnh headers.
- **Caching**: Thiết lập caching cho các yêu cầu và phản hồi để tối ưu hóa hiệu suất.
- **Điều hướng các route động**: Áp dụng Middleware cho các route động hoặc điều kiện cụ thể.

---

### 5. **Ví dụ thực tế về Middleware**

Giả sử bạn muốn tạo một middleware để kiểm tra quyền truy cập cho các trang quản trị, và nếu người dùng chưa đăng nhập, sẽ chuyển hướng họ đến trang login:

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Kiểm tra xem người dùng có cookie 'auth-token' không
  if (!request.cookies.has('auth-token')) {
    // Nếu không có, chuyển hướng đến trang login
    return NextResponse.redirect(new URL('/login', request.url));
  }
  // Nếu có, cho phép yêu cầu tiếp tục
  return NextResponse.next();
}
```

Trong ví dụ này, Middleware kiểm tra sự tồn tại của một cookie `auth-token` để xác định liệu người dùng đã đăng nhập hay chưa. Nếu không có token, người dùng sẽ bị chuyển hướng tới trang đăng nhập.

---

### 6. **Lưu ý khi sử dụng Middleware trong Next.js**

- **Chỉ áp dụng một Middleware duy nhất**: Mặc dù bạn có thể phân tách Middleware ra thành các module nhỏ, nhưng chỉ có một file `middleware.ts` được hỗ trợ trong mỗi dự án Next.js.
- **Hiệu suất**: Middleware có thể ảnh hưởng đến hiệu suất của ứng dụng nếu xử lý quá nhiều logic nặng nề. Hãy tối ưu hóa các đoạn mã trong Middleware để đảm bảo tốc độ phản hồi nhanh.
- **Không dùng để xử lý trạng thái**: Middleware không nên được dùng để lưu trữ trạng thái của ứng dụng, vì chúng được thực thi trên mỗi yêu cầu HTTP. Hãy sử dụng chúng cho logic xử lý yêu cầu và phản hồi.

---

Trên đây là hướng dẫn về cách sử dụng và tổ chức Middleware trong Next.js, giúp bạn dễ dàng quản lý và tối ưu hóa các logic xử lý yêu cầu trong ứng dụng của mình.