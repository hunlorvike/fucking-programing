# Styling trong Next.js

## **Mục lục**

1. [Giới thiệu về Styling trong Next.js](#1-gioi-thieu-ve-styling-trong-nextjs)
2. [Các phương pháp Styling trong Next.js](#2-cac-phuong-phap-styling-trong-nextjs)
    1. [CSS Modules](#21-css-modules)
    2. [Global CSS](#22-global-css)
    3. [CSS-in-JS](#23-css-in-js)
    4. [Tailwind CSS](#24-tailwind-css)
3. [Ví dụ thực tế về Styling trong Next.js](#3-vi-du-thuc-te-ve-styling-trong-nextjs)
4. [Lưu ý khi sử dụng Styling trong Next.js](#4-luu-y-khi-su-dung-styling-trong-nextjs)

---

### 1. **Giới thiệu về Styling trong Next.js**

Styling trong Next.js rất linh hoạt và có nhiều phương pháp khác nhau để bạn chọn lựa, tùy thuộc vào yêu cầu của dự án
và sở thích cá nhân. Next.js hỗ trợ nhiều kỹ thuật styling phổ biến như **CSS Modules**, **Global CSS**, **CSS-in-JS**,
và **Tailwind CSS**. Các phương pháp này giúp bạn dễ dàng quản lý và tối ưu hóa giao diện người dùng (UI) của ứng dụng.

---

### 2. **Các phương pháp Styling trong Next.js**

#### 2.1. **CSS Modules**

CSS Modules là một cách để sử dụng CSS mà không lo lắng về việc các lớp (class) bị trùng tên giữa các component. Mỗi
file CSS được áp dụng theo phạm vi component, giúp tránh tình trạng xung đột tên class trong toàn bộ ứng dụng.

- **Cách sử dụng**:
    - Tạo một file CSS với hậu tố `.module.css` hoặc `.module.scss` (nếu sử dụng SCSS).
    - Import và sử dụng như một đối tượng trong component.

**Ví dụ**:

```css
/* styles/Button.module.css */
.button {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
}
```

```javascript
// components/Button.js
import styles from './Button.module.css';

const Button = () => {
  return <button className={styles.button}>Click Me</button>;
};

export default Button;
```

- **Đặc điểm**:
    - Các lớp CSS được scoped tự động cho mỗi component, tránh xung đột.
    - Hỗ trợ cả CSS và SCSS.

---

#### 2.2. **Global CSS**

Global CSS cho phép bạn áp dụng các styles toàn cục cho toàn bộ ứng dụng, chẳng hạn như reset CSS, hoặc các styles không
đặc thù cho component nào.

- **Cách sử dụng**:
    - Global CSS được import vào trong file `pages/_app.tsx` (hoặc `pages/_app.js` nếu sử dụng JavaScript).

**Ví dụ**:

```css
/* styles/globals.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
```

```javascript
// pages/_app.js
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

- **Đặc điểm**:
    - Thích hợp cho các styles toàn cục như reset, typography, hoặc themes.
    - Các styles này sẽ áp dụng cho toàn bộ ứng dụng.

---

#### 2.3. **CSS-in-JS**

CSS-in-JS là một phương pháp viết CSS trực tiếp trong JavaScript hoặc TypeScript, giúp bạn dễ dàng sử dụng dynamic
styles và tổ chức CSS theo cách modular hơn. Next.js hỗ trợ nhiều thư viện CSS-in-JS, trong đó **styled-components** và
**emotion** là phổ biến nhất.

- **Cách sử dụng**:
    - Cài đặt thư viện CSS-in-JS (như `styled-components` hoặc `emotion`).
    - Viết CSS trực tiếp trong JavaScript.

**Ví dụ với `styled-components`**:

```bash
npm install styled-components
```

```javascript
// components/Button.js
import styled from 'styled-components';

const Button = styled.button`
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
`;

const App = () => {
  return <Button>Click Me</Button>;
};

export default App;
```

- **Đặc điểm**:
    - Phong cách modular, giúp bạn kết hợp logic và styling trong cùng một file.
    - Hỗ trợ tính năng như theming, media queries, và dynamic styles.

---

#### 2.4. **Tailwind CSS**

Tailwind CSS là một framework utility-first CSS, cho phép bạn sử dụng các lớp tiện ích để xây dựng giao diện mà không
cần viết CSS tùy chỉnh. Điều này giúp tăng tốc quá trình phát triển, đồng thời giảm thiểu CSS không sử dụng.

- **Cách tích hợp và sử dụng**:
    - Cài đặt Tailwind CSS vào dự án Next.js.
    - Sử dụng các lớp tiện ích trực tiếp trong JSX.

**Cài đặt Tailwind CSS**:

```bash
npm install tailwindcss postcss autoprefixer
npx tailwindcss init
```

Cấu hình `tailwind.config.js`:

```javascript
// tailwind.config.js
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

**Cấu hình PostCSS** (`postcss.config.js`):

```javascript
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

**Sử dụng Tailwind trong component**:

```javascript
// components/Button.js
const Button = () => {
  return <button className="bg-blue-500 text-white py-2 px-4 rounded">Click Me</button>;
};

export default Button;
```

- **Đặc điểm**:
    - Sử dụng các lớp tiện ích (utility classes) để xây dựng giao diện nhanh chóng.
    - Tiết kiệm thời gian phát triển và dễ dàng tùy chỉnh theme.
    - Tailwind hỗ trợ responsive design và dark mode một cách dễ dàng.

---

### 3. **Ví dụ thực tế về Styling trong Next.js**

Dưới đây là ví dụ kết hợp sử dụng **CSS Modules** và **Tailwind CSS** trong một ứng dụng Next.js:

**Tạo một component Button sử dụng CSS Modules**:

```css
/* styles/Button.module.css */
.button {
  padding: 10px 20px;
  border-radius: 5px;
}
```

```javascript
// components/Button.js
import styles from '../styles/Button.module.css';

const Button = ({ children, className }) => {
  return (
    <button className={`${styles.button} ${className}`}>
      {children}
    </button>
  );
};

export default Button;
```

**Sử dụng Tailwind CSS để thêm các lớp tiện ích**:

```javascript
// pages/index.js
import Button from '../components/Button';

const Home = () => {
  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-100">
      <Button className="bg-blue-500 text-white">Click Me</Button>
    </div>
  );
};

export default Home;
```

Trong ví dụ này:

- **CSS Modules** được sử dụng để thêm các styles cơ bản cho button.
- **Tailwind CSS** được sử dụng để thêm các lớp tiện ích giúp dễ dàng bố trí và tạo kiểu nhanh chóng.

---

### 4. **Lưu ý khi sử dụng Styling trong Next.js**

1. **Quản lý Styles**: Nếu bạn sử dụng CSS Modules, đảm bảo rằng bạn tổ chức các file `.module.css` theo từng component
   để tránh tình trạng xung đột. Nếu sử dụng Tailwind CSS, hãy đảm bảo rằng bạn sử dụng các lớp tiện ích đúng cách để
   duy trì mã sạch sẽ.

2. **Global CSS**: Chỉ nên sử dụng Global CSS cho các styles chung như reset CSS hoặc typography. Tránh áp dụng global
   styles cho các component cụ thể để không gây khó khăn trong việc quản lý và mở rộng ứng dụng.

3. **Tối ưu hóa hiệu suất**: Sử dụng các thư viện như `styled-components` hoặc `emotion` để tận dụng tính năng dynamic
   styles. Tuy nhiên, hãy cẩn thận với việc sinh ra quá nhiều lớp CSS không cần thiết, điều này có thể ảnh hưởng đến
   hiệu suất của ứng dụng.

4. **Tailwind CSS**: Nếu bạn sử dụng Tailwind CSS, hãy tận dụng tính năng `purge` của Tailwind để loại bỏ các lớp không
   sử dụng trong build production, giúp giảm kích thước CSS.

Bằng cách sử dụng các phương pháp styling này, bạn có thể xây dựng giao diện người dùng mạnh mẽ, dễ bảo trì và hiệu quả
trong Next.js.
