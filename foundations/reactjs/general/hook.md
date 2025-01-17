Dưới đây là tài liệu chi tiết về quản lý trạng thái trong React với Redux và các thư viện bổ sung giúp giảm boilerplate
như Redux Toolkit và Redux-Saga, cùng với ví dụ minh họa về chế độ **Dark Mode / Light Mode**.

# Quản Lý State Trong React: Kết Hợp Hooks và Redux Với Dark Mode / Light Mode

React cung cấp quản lý trạng thái cục bộ qua **Hooks** như `useState` và `useReducer`. Tuy nhiên, khi ứng dụng trở nên
phức tạp, cần giải pháp mạnh mẽ hơn cho quản lý trạng thái toàn cục và đó là khi **Redux** phát huy vai trò. Redux là
một thư viện quản lý trạng thái phổ biến giúp đảm bảo tính nhất quán và dễ kiểm soát trạng thái trong các ứng dụng lớn.

## Các Khái Niệm Cơ Bản Trong Redux

Trước khi triển khai ví dụ, cần hiểu rõ nhiệm vụ của các thành phần chính trong Redux:

### 1. **Store**

- **Store** là nơi lưu trữ toàn bộ trạng thái của ứng dụng dưới dạng một cây đối tượng.
- Mỗi khi trạng thái thay đổi, `store` sẽ cập nhật trạng thái này và tất cả các component có kết nối với `store` sẽ được
  cập nhật lại.
- Store được tạo ra bằng cách kết hợp các `reducer`, là nơi cập nhật trạng thái dựa trên các `action`.

### 2. **State**

- **State** là một đối tượng JavaScript lưu trữ trạng thái hiện tại của ứng dụng.
- Trong ví dụ này, state chứa thông tin về **theme** của ứng dụng (`light` hoặc `dark`), giúp ứng dụng hiển thị đúng
  giao diện người dùng.

### 3. **Action**

- **Action** là một đối tượng JavaScript có thuộc tính `type` mô tả loại hành động và có thể có thuộc tính `payload`
  chứa dữ liệu đi kèm.
- `Action` là tín hiệu yêu cầu thay đổi trạng thái. Ví dụ, `TOGGLE_THEME` là action sẽ yêu cầu chuyển đổi chế độ theme.

```javascript
const toggleThemeAction = { type: 'TOGGLE_THEME' };
```

### 4. **Reducer**

- **Reducer** là một hàm nhận `state` hiện tại và `action`, sau đó trả về trạng thái mới.
- Reducer đảm bảo việc cập nhật là **pure function** (hàm thuần túy) và không làm thay đổi `state` hiện tại trực tiếp.

```javascript
function themeReducer(state = { theme: 'light' }, action) {
  switch (action.type) {
    case 'TOGGLE_THEME':
      return { theme: state.theme === 'light' ? 'dark' : 'light' };
    default:
      return state;
  }
}
```

### 5. **Dispatch**

- `Dispatch` là phương thức để gửi một `action` tới `store`, kích hoạt `reducer` xử lý và cập nhật trạng thái.

```javascript
store.dispatch(toggleThemeAction);
```

## Cài Đặt và Thiết Lập Redux Trong Ứng Dụng React

### Bước 1: Cài Đặt Redux và React-Redux

Cài đặt hai gói:

```bash
npm install redux react-redux
```

### Bước 2: Tạo `store`

Tạo `store` bằng cách kết hợp các `reducer` và kết nối `store` với ứng dụng qua `Provider` của React-Redux.

```javascript
// src/store.js
import { createStore } from 'redux';
import themeReducer from './reducers/themeReducer';

const store = createStore(themeReducer);

export default store;
```

Trong `App.js`, kết nối `store` với ứng dụng qua `Provider`:

```javascript
// src/App.js
import React from 'react';
import { Provider } from 'react-redux';
import store from './store';
import ThemeToggle from './ThemeToggle';

function App() {
  return (
    <Provider store={store}>
      <ThemeToggle />
    </Provider>
  );
}

export default App;
```

### Bước 3: Tạo Reducer Cho Theme

Tạo file `themeReducer.js` để xác định cách xử lý các `action` liên quan đến theme.

```javascript
// src/reducers/themeReducer.js
const initialState = {
  theme: 'light',
};

function themeReducer(state = initialState, action) {
  switch (action.type) {
    case 'TOGGLE_THEME':
      return { theme: state.theme === 'light' ? 'dark' : 'light' };
    default:
      return state;
  }
}

export default themeReducer;
```

### Bước 4: Tạo Component `ThemeToggle` và Kết Nối Với Redux

Trong `ThemeToggle`, sử dụng `useSelector` để lấy `theme` từ `store` và `useDispatch` để gửi `action`.

```javascript
// src/ThemeToggle.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

function ThemeToggle() {
  const theme = useSelector(state => state.theme);
  const dispatch = useDispatch();

  const toggleTheme = () => dispatch({ type: 'TOGGLE_THEME' });

  return (
    <div
      style={{
        backgroundColor: theme === 'light' ? '#fff' : '#333',
        color: theme === 'light' ? '#000' : '#fff',
        textAlign: 'center',
        padding: '20px',
      }}
    >
      <h1>{theme === 'light' ? 'Light Mode' : 'Dark Mode'}</h1>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
}

export default ThemeToggle;
```

## Sử Dụng Các Thư Viện Giảm Boilerplate Cho Redux

### 1. **Redux Toolkit**

**Redux Toolkit** là bộ công cụ được xây dựng để giảm thiểu cấu trúc và mã lặp lại khi sử dụng Redux, hỗ trợ các API như
`createSlice` để tạo reducer và action trong một bước:

```javascript
// src/reducers/themeSlice.js
import { createSlice } from '@reduxjs/toolkit';

const themeSlice = createSlice({
  name: 'theme',
  initialState: { theme: 'light' },
  reducers: {
    toggleTheme: state => {
      state.theme = state.theme === 'light' ? 'dark' : 'light';
    },
  },
});

export const { toggleTheme } = themeSlice.actions;
export default themeSlice.reducer;
```

```javascript
// src/store.js
import { configureStore } from '@reduxjs/toolkit';
import themeReducer from './reducers/themeSlice';

const store = configureStore({
  reducer: themeReducer,
});

export default store;
```

### 2. **Redux-Saga**

**Redux-Saga** hỗ trợ quản lý các side effects, chẳng hạn như gọi API, một cách có cấu trúc và dễ kiểm soát.

- Cài đặt Redux-Saga:

  ```bash
  npm install redux-saga
  ```

- Định nghĩa một saga cơ bản (ví dụ như để lưu theme hiện tại vào localStorage):

  ```javascript
  // src/sagas/themeSaga.js
  import { put, takeLatest } from 'redux-saga/effects';
  import { toggleTheme } from '../reducers/themeSlice';

  function* saveTheme(action) {
    yield localStorage.setItem('theme', action.payload);
  }

  function* watchToggleTheme() {
    yield takeLatest(toggleTheme.type, saveTheme);
  }

  export default watchToggleTheme;
  ```

## Kết Luận

Sự kết hợp giữa Hooks và Redux giúp quản lý trạng thái trong React linh hoạt và mạnh mẽ. Redux Toolkit giảm bớt cấu trúc
và mã lặp lại, trong khi Redux-Saga giúp quản lý các side effects. Tùy thuộc vào độ phức tạp của ứng dụng, bạn có thể
chọn kết hợp Redux với các thư viện này để tối ưu hóa quy trình quản lý trạng thái.
