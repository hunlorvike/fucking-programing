Dưới đây là tài liệu chi tiết về sử dụng **React Router** để triển khai **Single Page Application (SPA)** trong React. Tài liệu sẽ hướng dẫn cách cấu hình và sử dụng React Router để chuyển đổi giữa các trang mà không cần tải lại toàn bộ trang.

# Điều Hướng Trong React: Sử Dụng React Router Để Tạo SPA

React Router là thư viện giúp quản lý điều hướng (routing) trong ứng dụng React. Điều này cho phép tạo các ứng dụng SPA (Single Page Application), nơi người dùng có thể chuyển đổi giữa các trang mà không cần tải lại toàn bộ trang, mang đến trải nghiệm mượt mà và nhanh chóng.

## Cài Đặt và Thiết Lập React Router

### Bước 1: Cài Đặt React Router

Cài đặt **React Router** thông qua `react-router-dom`:

```bash
npm install react-router-dom
```

### Bước 2: Cấu Trúc Cơ Bản của SPA Với React Router

Trong React, `React Router` quản lý điều hướng bằng cách kết hợp **BrowserRouter**, **Routes**, và **Route**.

- **BrowserRouter**: Đóng vai trò là router chính, giúp theo dõi lịch sử điều hướng của người dùng.
- **Routes**: Được dùng để bao bọc các **Route** và cho phép điều hướng giữa các trang.
- **Route**: Xác định một đường dẫn cụ thể và gắn với một component sẽ được hiển thị khi đường dẫn này được kích hoạt.

```javascript
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import ContactPage from './pages/ContactPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/contact" element={<ContactPage />} />
      </Routes>
    </Router>
  );
}

export default App;
```

## Các Thành Phần Chính trong React Router

Dưới đây là các thành phần chính giúp React Router hoạt động mượt mà:

### 1. **BrowserRouter**

- **BrowserRouter** tạo một router chính sử dụng API `History` của trình duyệt, giúp điều hướng mà không cần tải lại trang.
- Thường được dùng để bọc toàn bộ ứng dụng để kích hoạt điều hướng cho các component con.

### 2. **Routes** và **Route**

- **Routes** là nơi định nghĩa các đường dẫn (routes) và component tương ứng.
- **Route** nhận `path` là đường dẫn URL và `element` là component hiển thị khi đường dẫn được kích hoạt.

```javascript
<Route path="/about" element={<AboutPage />} />
```

### 3. **Link** và **NavLink**

- **Link** thay thế thẻ `<a>` để chuyển trang trong ứng dụng SPA mà không cần tải lại.
- **NavLink** là phiên bản nâng cao của `Link`, cung cấp thêm tính năng để tự động thêm class `active` khi đường dẫn tương ứng đang được chọn.

```javascript
// src/components/Navbar.js
import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <NavLink to="/" exact activeClassName="active">
        Home
      </NavLink>
      <NavLink to="/about" activeClassName="active">
        About
      </NavLink>
      <NavLink to="/contact" activeClassName="active">
        Contact
      </NavLink>
    </nav>
  );
}

export default Navbar;
```

### 4. **useNavigate**

- **useNavigate** là một hook được dùng để điều hướng (navigation) một cách chương trình hóa. Bạn có thể dùng nó trong các tình huống khi cần điều hướng sau khi một sự kiện xảy ra, chẳng hạn như sau khi hoàn thành một form.

```javascript
// src/pages/LoginPage.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Xử lý đăng nhập thành công
    navigate('/dashboard');
  };

  return <button onClick={handleLogin}>Login</button>;
}

export default LoginPage;
```

### 5. **Outlet** (Nested Routes)

**Outlet** được sử dụng để tạo ra **nested routes** (các route lồng nhau), cho phép xây dựng cấu trúc trang có các layout phụ.

```javascript
// src/pages/Dashboard.js
import React from 'react';
import { Outlet, Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav>
        <Link to="profile">Profile</Link>
        <Link to="settings">Settings</Link>
      </nav>
      <Outlet />
    </div>
  );
}

export default Dashboard;
```

```javascript
// src/App.js
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Profile from './pages/Profile';
import Settings from './pages/Settings';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />}>
          <Route path="profile" element={<Profile />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </Router>
  );
}
```

## Các Tính Năng Nâng Cao Trong React Router

### 1. **Redirect** (Navigate trong phiên bản mới)

Trong phiên bản mới của React Router, sử dụng `useNavigate` để chuyển hướng, thay thế cho `Redirect` trong phiên bản cũ.

```javascript
import { useNavigate } from 'react-router-dom';

function SomeComponent() {
  const navigate = useNavigate();

  useEffect(() => {
    // Điều kiện chuyển hướng
    navigate('/target-path');
  }, [navigate]);

  return <div>Redirecting...</div>;
}
```

### 2. **useParams**

`useParams` là hook cho phép truy cập các tham số từ đường dẫn động.

```javascript
// src/pages/Product.js
import React from 'react';
import { useParams } from 'react-router-dom';

function Product() {
  const { productId } = useParams();

  return <h2>Product ID: {productId}</h2>;
}

export default Product;
```

### 3. **404 Not Found Route**

Để xử lý các đường dẫn không hợp lệ, thêm một `Route` có `path="*"` vào cuối danh sách.

```javascript
<Route path="*" element={<NotFound />} />
```

## Kết Hợp React Router Với Quản Lý State

React Router có thể kết hợp với **Redux** hoặc **Context API** để quản lý trạng thái, tạo nên các ứng dụng SPA mạnh mẽ và dễ mở rộng.

## Kết Luận

Việc sử dụng React Router giúp dễ dàng quản lý và điều hướng trong ứng dụng React theo cấu trúc SPA. Qua đó, trải nghiệm người dùng được tối ưu hơn, không cần tải lại toàn bộ trang.
