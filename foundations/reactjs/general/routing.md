# Routing trong React

Trong phát triển ứng dụng web hiện đại, việc điều hướng giữa các trang và quản lý trạng thái của URL là rất quan trọng.
**React Router** là thư viện phổ biến nhất được sử dụng để quản lý routing trong các ứng dụng React. Thư viện này cung
cấp các thành phần và API để thiết lập và xử lý routing một cách dễ dàng.

## Khái niệm cơ bản về Routing

**Routing** là quá trình xác định nội dung nào sẽ được hiển thị cho người dùng dựa trên URL hiện tại. Routing cho phép
người dùng điều hướng qua lại giữa các trang mà không cần phải tải lại toàn bộ ứng dụng.

## Các thành phần chính của React Router

React Router bao gồm các thành phần và hooks cơ bản để quản lý routing:

1. **BrowserRouter**: Cung cấp ngữ cảnh routing cho ứng dụng, cho phép sử dụng HTML5 history API để quản lý URL.
2. **Routes**: Container chứa các route con. Mỗi route xác định một đường dẫn (path) và component nào sẽ được hiển thị
   khi đường dẫn đó được truy cập.
3. **Route**: Định nghĩa mối quan hệ giữa một đường dẫn URL và một component.
4. **Link**: Component để tạo các liên kết, cho phép người dùng điều hướng đến các route khác trong ứng dụng mà không
   cần tải lại trang.
5. **useNavigate**: Hook cho phép bạn điều hướng đến một route khác programmatically.

## Các bước triển khai Routing trong React

### 1. Cài đặt React Router

Để sử dụng React Router, trước tiên bạn cần cài đặt thư viện này:

```bash
npm install react-router-dom
```

### 2. Thiết lập BrowserRouter

Wrap ứng dụng của bạn trong component `BrowserRouter` để kích hoạt routing:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById('root')
);
```

### 3. Định nghĩa Routes

Trong component `App`, bạn có thể định nghĩa các routes bằng cách sử dụng component `Routes` và `Route`:

```javascript
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';
import NotFound from './NotFound';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="*" element={<NotFound />} /> {/* Route không tìm thấy */}
    </Routes>
  );
}
```

### 4. Điều hướng giữa các routes

Sử dụng component `Link` để điều hướng giữa các routes mà không cần tải lại trang:

```javascript
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
    </nav>
  );
}
```

### 5. Điều hướng programmatically

Sử dụng hook `useNavigate` để điều hướng từ một hàm hoặc trong các sự kiện:

```javascript
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  const goToAbout = () => {
    navigate('/about');
  };

  return (
    <div>
      <h1>Home Page</h1>
      <button onClick={goToAbout}>Go to About</button>
    </div>
  );
}
```

## Các loại Route trong React Router

### 1. Route chính

Là các route được xác định bằng đường dẫn cụ thể, như trong ví dụ trên với `path="/"` và `path="/about"`.

### 2. Route lồng nhau (Nested Routes)

React Router hỗ trợ các route lồng nhau, cho phép bạn tổ chức các component con trong các route cha. Đây là cách để tạo
cấu trúc URL phức tạp hơn.

```javascript
<Route path="/users" element={<Users />}>
  <Route path=":userId" element={<UserDetail />} />
</Route>
```

### 3. Route động

Bạn có thể sử dụng các tham số trong đường dẫn để tạo các route động, giúp hiển thị thông tin khác nhau dựa trên URL.

```javascript
<Route path="/products/:productId" element={<ProductDetail />} />
```

### 4. Redirect

React Router cho phép bạn điều hướng tự động đến một route khác nếu một điều kiện nhất định được đáp ứng.

```javascript
import { Navigate } from 'react-router-dom';

<Route path="/old-path" element={<Navigate to="/new-path" replace />} />;
```

## Tóm tắt về Routing trong React

| Tính năng          | Mô tả                                        |
|--------------------|----------------------------------------------|
| **BrowserRouter**  | Cung cấp ngữ cảnh cho routing.               |
| **Routes**         | Container chứa các route.                    |
| **Route**          | Định nghĩa đường dẫn và component tương ứng. |
| **Link**           | Component để tạo liên kết điều hướng.        |
| **useNavigate**    | Hook cho phép điều hướng programmatically.   |
| **Nested Routes**  | Hỗ trợ cấu trúc route phức tạp hơn.          |
| **Dynamic Routes** | Sử dụng tham số trong đường dẫn.             |
| **Redirect**       | Điều hướng tự động đến một route khác.       |

## Kết luận

Routing trong React là một phần quan trọng trong việc xây dựng các ứng dụng web hiện đại, cho phép quản lý URL và điều
hướng một cách hiệu quả. Thư viện **React Router** cung cấp một API mạnh mẽ và linh hoạt để thiết lập và kiểm soát
routing trong ứng dụng của bạn. Việc hiểu rõ cách hoạt động của routing sẽ giúp bạn tạo ra trải nghiệm người dùng mượt
mà và dễ dàng hơn trong việc điều hướng giữa các phần của ứng dụng.
