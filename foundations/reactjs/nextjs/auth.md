# Xử lý Authentication, Authorization, và Refresh Token trong Next.js sử dụng NextAuth

## **Mục lục**

1. [Giới thiệu về NextAuth và cách hoạt động](#1-gioi-thieu-ve-nextauth-va-cach-hoat-dong)
2. [Cài đặt NextAuth trong Next.js](#2-cai-dat-nextauth-trong-nextjs)
   1. [Cài đặt NextAuth trong dự án Next.js](#21-cai-dat-nextauth-trong-du-an-nextjs)
   2. [Cấu hình NextAuth](#22-cau-hinh-nextauth)
3. [Xử lý Authentication và Authorization](#3-xu-ly-authentication-va-authorization)
   1. [Xác thực người dùng (Authentication)](#31-xac-thuc-nguoi-dung-authentication)
   2. [Phân quyền người dùng (Authorization)](#32-phan-quyen-nguoi-dung-authorization)
4. [Sử dụng Refresh Token trong NextAuth](#4-su-dung-refresh-token-trong-nextauth)
5. [Ví dụ thực tế về Authentication, Authorization, và Refresh Token](#5-vi-du-thuc-te-ve-authentication-authorization-va-refresh-token)
6. [Lưu ý khi sử dụng NextAuth](#6-luu-y-khi-su-dung-nextauth)

---

### 1. **Giới thiệu về NextAuth và cách hoạt động**

NextAuth là một thư viện mã nguồn mở dành cho Next.js, cung cấp giải pháp đơn giản và dễ sử dụng cho việc xử lý Authentication và Authorization trong ứng dụng. NextAuth hỗ trợ nhiều phương thức đăng nhập (login) khác nhau như OAuth, Email, Credentials (tài khoản và mật khẩu), và các dịch vụ xác thực bên ngoài như Google, Facebook, GitHub, v.v.

NextAuth giúp bạn xử lý các vấn đề như:

- **Authentication**: Xác thực người dùng khi họ đăng nhập vào ứng dụng.
- **Authorization**: Kiểm tra quyền truy cập của người dùng sau khi đã xác thực.
- **Refresh Tokens**: Quản lý và gia hạn token để duy trì trạng thái đăng nhập lâu dài.

---

### 2. **Cài đặt NextAuth trong Next.js**

#### 2.1. **Cài đặt NextAuth trong dự án Next.js**

Để sử dụng NextAuth, bạn cần cài đặt thư viện `next-auth` vào dự án Next.js của bạn. Thực hiện cài đặt qua npm hoặc yarn:

```bash
npm install next-auth
```

Hoặc sử dụng yarn:

```bash
yarn add next-auth
```

#### 2.2. **Cấu hình NextAuth**

Sau khi cài đặt, bạn cần tạo một file cấu hình `[...]nextauth.js` (hoặc `.ts` nếu sử dụng TypeScript) trong thư mục `pages/api/auth/`. Đây là nơi bạn cấu hình các provider (ví dụ: Google, GitHub), cách xác thực và cách quản lý token.

Ví dụ về cấu hình cơ bản:

```js
// pages/api/auth/[...nextauth].js
import NextAuth from "next-auth";
import Providers from "next-auth/providers";

export default NextAuth({
  providers: [
    Providers.Google({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
    Providers.Credentials({
      name: "Credentials",
      credentials: {
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        // Kiểm tra thông tin người dùng và trả về đối tượng người dùng nếu hợp lệ
        const user = { id: 1, name: "User" };
        if (user) {
          return user;
        } else {
          return null;
        }
      },
    }),
  ],
  session: {
    jwt: true, // Sử dụng JWT để lưu trữ phiên người dùng
  },
  callbacks: {
    async jwt(token, user) {
      // Lưu thông tin người dùng vào JWT token
      if (user) {
        token.id = user.id;
        token.name = user.name;
      }
      return token;
    },
    async session(session, token) {
      // Cập nhật thông tin session từ token
      session.id = token.id;
      session.name = token.name;
      return session;
    },
  },
  pages: {
    signIn: "/auth/signin", // Tùy chỉnh trang đăng nhập
    error: "/auth/error",   // Tùy chỉnh trang lỗi
  },
});
```

Trong ví dụ trên:
- **Google** và **Credentials** là hai provider để đăng nhập (Google OAuth và đăng nhập qua tài khoản/mật khẩu).
- **JWT** được sử dụng để lưu trữ session của người dùng.
- Các `callbacks` cho phép tùy chỉnh cách xử lý thông tin người dùng và session.

---

### 3. **Xử lý Authentication và Authorization**

#### 3.1. **Xác thực người dùng (Authentication)**

NextAuth cung cấp các cơ chế xác thực người dùng qua nhiều provider khác nhau. Khi người dùng đăng nhập thành công, NextAuth sẽ tạo một session và lưu trữ thông tin vào JWT hoặc cookie (tùy vào cấu hình).

Bạn có thể sử dụng hook `useSession` để lấy thông tin về session người dùng và xác thực người dùng trong các component React.

Ví dụ:

```jsx
// pages/index.js
import { useSession, signIn, signOut } from "next-auth/react";

export default function Home() {
  const { data: session } = useSession();

  if (!session) {
    return (
      <div>
        <h1>Not authenticated</h1>
        <button onClick={() => signIn("google")}>Sign in with Google</button>
      </div>
    );
  }

  return (
    <div>
      <h1>Welcome, {session.user.name}</h1>
      <button onClick={() => signOut()}>Sign out</button>
    </div>
  );
}
```

- `useSession` hook giúp lấy thông tin session của người dùng.
- `signIn` và `signOut` để thực hiện đăng nhập và đăng xuất.

#### 3.2. **Phân quyền người dùng (Authorization)**

Sau khi người dùng đã được xác thực, bạn có thể kiểm tra quyền truy cập của họ đối với các trang hoặc hành động cụ thể. Điều này có thể được thực hiện thông qua việc kiểm tra thông tin trong `session`.

Ví dụ, chỉ cho phép người dùng có quyền admin truy cập một trang quản trị:

```jsx
// pages/admin.js
import { useSession } from "next-auth/react";

export default function AdminPage() {
  const { data: session } = useSession();

  if (!session || session.user.role !== "admin") {
    return <h1>Access Denied</h1>;
  }

  return <h1>Welcome to Admin Page</h1>;
}
```

Trong ví dụ trên, nếu người dùng không phải là admin hoặc chưa đăng nhập, họ sẽ không thể truy cập trang quản trị.

---

### 4. **Sử dụng Refresh Token trong NextAuth**

NextAuth hỗ trợ sử dụng JWT để lưu trữ phiên làm việc của người dùng, và bạn có thể cấu hình refresh token để gia hạn phiên làm việc khi token hết hạn.

Cấu hình refresh token trong NextAuth thường đi kèm với các provider hỗ trợ refresh token, ví dụ như Google OAuth, GitHub, v.v. Dưới đây là cách cấu hình refresh token trong NextAuth:

```js
// pages/api/auth/[...nextauth].js
export default NextAuth({
  providers: [
    Providers.Google({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      authorization: {
        params: {
          scope: "openid profile email",
        },
      },
    }),
  ],
  callbacks: {
    async jwt(token, user) {
      if (user) {
        // Lưu token từ Google OAuth vào token JWT
        token.accessToken = user.access_token;
        token.refreshToken = user.refresh_token;
      }

      // Kiểm tra nếu token sắp hết hạn, và nếu có refresh token, thì gia hạn
      if (Date.now() < token.exp * 1000) {
        return token;
      }

      if (token.refreshToken) {
        // Gọi API của Google để refresh token
        const refreshedTokens = await refreshAccessToken(token.refreshToken);
        token.accessToken = refreshedTokens.access_token;
        token.refreshToken = refreshedTokens.refresh_token;
      }

      return token;
    },
  },
});

async function refreshAccessToken(refreshToken) {
  // Gửi yêu cầu API để lấy refresh token mới
  const response = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    body: new URLSearchParams({
      client_id: process.env.GOOGLE_CLIENT_ID,
      client_secret: process.env.GOOGLE_CLIENT_SECRET,
      refresh_token: refreshToken,
      grant_type: "refresh_token",
    }),
  });

  return response.json();
}
```

Trong ví dụ này, khi token hết hạn, NextAuth sẽ sử dụng refresh token để gia hạn token và giữ người dùng đăng nhập mà không cần yêu cầu họ đăng nhập lại.

---

### 5. **Ví dụ thực tế về Authentication, Authorization, và Refresh Token**

Giả sử bạn có một ứng dụng với các tính năng yêu cầu người dùng phải đăng nhập, và chỉ cho phép người dùng

 có vai trò admin truy cập trang quản trị. Dưới đây là cách triển khai:

```js
// pages/api/auth/[...nextauth].js
import NextAuth from "next-auth";
import Providers from "next-auth/providers";

export default NextAuth({
  providers: [
    Providers.Google({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
  ],
  callbacks: {
    async jwt(token, user) {
      if (user) {
        token.accessToken = user.access_token;
        token.refreshToken = user.refresh_token;
      }
      return token;
    },
    async session(session, token) {
      session.accessToken = token.accessToken;
      session.refreshToken = token.refreshToken;
      return session;
    },
  },
});
```

Sau khi cấu hình như trên, bạn có thể sử dụng `useSession` để xác định quyền truy cập của người dùng và hiển thị các trang hoặc chức năng phù hợp với quyền của họ.

---

### 6. **Lưu ý khi sử dụng NextAuth**

- **Bảo mật token**: Đảm bảo rằng bạn luôn lưu trữ token một cách an toàn, tránh việc rò rỉ hoặc đánh cắp token.
- **Refresh token**: Khi sử dụng refresh token, hãy cẩn thận với các cuộc tấn công tái sử dụng token (replay attacks). Hãy đảm bảo rằng refresh token được sử dụng trong các kênh bảo mật.
- **Tùy chỉnh pages**: NextAuth cho phép bạn tùy chỉnh các trang đăng nhập và lỗi, điều này giúp cải thiện trải nghiệm người dùng.
