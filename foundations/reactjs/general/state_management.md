# Tìm hiểu về State Management với Redux trong ReactJS

**Redux** là một thư viện quản lý trạng thái phổ biến, giúp quản lý trạng thái của ứng dụng React một cách có tổ chức và dễ dàng kiểm soát. Redux hoạt động dựa trên nguyên tắc lưu trữ một **state duy nhất** của ứng dụng trong một **store** và sử dụng các **action** và **reducer** để cập nhật state.

## Các khái niệm cơ bản trong Redux

### 1. Store

- **Bản chất**: Store là nơi lưu trữ toàn bộ state của ứng dụng Redux. Chỉ có một store duy nhất trong ứng dụng Redux.
- **Vai trò**: Giúp centralize state, làm cho state trở nên nhất quán và dễ dàng quản lý hơn.
- **Cú pháp tạo store**:

  ```javascript
  import { createStore } from 'redux';
  import rootReducer from './reducers';

  const store = createStore(rootReducer);
  ```

### 2. State

- **Bản chất**: State là dữ liệu của ứng dụng, được lưu trong store.
- **Vai trò**: State đại diện cho trạng thái hiện tại của ứng dụng và có thể được truy cập hoặc cập nhật thông qua các action và reducer.

### 3. Action

- **Bản chất**: Action là một đối tượng đơn giản có thuộc tính `type` (bắt buộc) và các dữ liệu cần thiết khác (payload) để truyền dữ liệu tới store.
- **Vai trò**: Action mô tả những gì cần thay đổi trong state, nhưng không tự thực hiện thay đổi.
- **Cú pháp**:

  ```javascript
  const incrementAction = {
    type: 'INCREMENT',
    payload: 1,
  };
  ```

### 4. Reducer

- **Bản chất**: Reducer là một hàm nhận vào state hiện tại và action, sau đó trả về state mới.
- **Vai trò**: Reducer xác định cách state thay đổi dựa trên action nhận được.
- **Cú pháp**:

  ```javascript
  function counterReducer(state = { count: 0 }, action) {
    switch (action.type) {
      case 'INCREMENT':
        return { count: state.count + action.payload };
      case 'DECREMENT':
        return { count: state.count - action.payload };
      default:
        return state;
    }
  }
  ```

### 5. Dispatch

- **Bản chất**: Dispatch là phương thức để gửi một action tới store.
- **Vai trò**: Khi dispatch một action, Redux sẽ chuyển action này đến reducer để cập nhật state.

- **Cú pháp**:

  ```javascript
  store.dispatch(incrementAction);
  ```

## Thiết lập Redux trong ứng dụng React

### 1. Cài đặt Redux và React-Redux

- Chạy lệnh sau để cài đặt Redux và thư viện tích hợp React-Redux:

  ```bash
  npm install redux react-redux
  ```

### 2. Tạo Reducer

- Tạo file `counterReducer.js` và định nghĩa reducer như sau:

  ```javascript
  const initialState = { count: 0 };

  function counterReducer(state = initialState, action) {
    switch (action.type) {
      case 'INCREMENT':
        return { count: state.count + 1 };
      case 'DECREMENT':
        return { count: state.count - 1 };
      default:
        return state;
    }
  }

  export default counterReducer;
  ```

### 3. Tạo Store

- Tạo file `store.js` để khởi tạo store với reducer đã định nghĩa.

  ```javascript
  import { createStore } from 'redux';
  import counterReducer from './counterReducer';

  const store = createStore(counterReducer);

  export default store;
  ```

### 4. Kết nối Store với Ứng dụng

- Sử dụng **Provider** từ `react-redux` để kết nối store với toàn bộ ứng dụng React.

  ```javascript
  import React from 'react';
  import ReactDOM from 'react-dom';
  import { Provider } from 'react-redux';
  import store from './store';
  import App from './App';

  ReactDOM.render(
    <Provider store={store}>
      <App />
    </Provider>,
    document.getElementById('root')
  );
  ```

### 5. Sử dụng Redux State trong Component với `useSelector` và `useDispatch`

- **`useSelector`**: Lấy dữ liệu từ store.
- **`useDispatch`**: Gửi action tới store để cập nhật state.

- **Ví dụ**:

  ```javascript
  import React from 'react';
  import { useSelector, useDispatch } from 'react-redux';

  function Counter() {
    const count = useSelector(state => state.count);
    const dispatch = useDispatch();

    return (
      <div>
        <p>Count: {count}</p>
        <button onClick={() => dispatch({ type: 'INCREMENT' })}>Tăng</button>
        <button onClick={() => dispatch({ type: 'DECREMENT' })}>Giảm</button>
      </div>
    );
  }

  export default Counter;
  ```

## Middleware trong Redux

- **Bản chất**: Middleware là các hàm trung gian xử lý action trước khi đến reducer. Các middleware phổ biến bao gồm `redux-thunk` và `redux-saga` để xử lý các tác vụ bất đồng bộ.
- **Cú pháp tích hợp redux-thunk**:

  ```javascript
  import { createStore, applyMiddleware } from 'redux';
  import thunk from 'redux-thunk';
  import rootReducer from './reducers';

  const store = createStore(rootReducer, applyMiddleware(thunk));
  ```

- **Ví dụ sử dụng Thunk**:

  ```javascript
  const fetchData = () => {
    return dispatch => {
      fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => dispatch({ type: 'FETCH_DATA_SUCCESS', payload: data }));
    };
  };
  ```

## Tóm tắt

- **Store**: Lưu trữ state của toàn bộ ứng dụng.
- **Action**: Mô tả các sự kiện thay đổi state.
- **Reducer**: Hàm xử lý và cập nhật state dựa trên action.
- **Dispatch**: Gửi action tới store để cập nhật state.
- **Middleware**: Xử lý các tác vụ bổ sung (như async) trước khi action tới reducer.

## Các công cụ hữu ích trong Redux

### Redux DevTools

- **Bản chất**: Công cụ giúp bạn xem xét các hành động và trạng thái trong ứng dụng.
- **Cài đặt**: Cài đặt Redux DevTools trong Chrome hoặc Firefox và tích hợp vào store.

  ```javascript
  import { createStore } from 'redux';
  import { composeWithDevTools } from 'redux-devtools-extension';

  const store = createStore(rootReducer, composeWithDevTools());
  ```

### Redux Toolkit

- **Bản chất**: Redux Toolkit là một thư viện của Redux giúp thiết lập Redux nhanh chóng và giảm boilerplate code.
- **Ví dụ tạo store với Redux Toolkit**:

  ```javascript
  import { configureStore, createSlice } from '@reduxjs/toolkit';

  const counterSlice = createSlice({
    name: 'counter',
    initialState: { count: 0 },
    reducers: {
      increment: state => {
        state.count += 1;
      },
      decrement: state => {
        state.count -= 1;
      },
    },
  });

  export const { increment, decrement } = counterSlice.actions;

  const store = configureStore({
    reducer: {
      counter: counterSlice.reducer,
    },
  });

  export default store;
  ```

## Kết luận

Redux giúp quản lý trạng thái ứng dụng một cách rõ ràng và dễ bảo trì, đặc biệt là khi ứng dụng trở nên phức tạp. Việc hiểu và sử dụng các khái niệm của Redux, cùng với Redux DevTools và Redux Toolkit, sẽ giúp bạn xây dựng các ứng dụng React mạnh mẽ và dễ dàng kiểm soát.

Để minh họa cách sử dụng Redux để quản lý trạng thái, chúng ta sẽ triển khai một ví dụ về một **danh sách công việc** (to-do list). Trong ví dụ này, bạn có thể thêm, xóa và đánh dấu công việc là hoàn thành. Đây là một ví dụ cơ bản nhưng giúp bạn hiểu cách sử dụng Redux trong một ứng dụng React thực tế.

### 1. Cài đặt Redux và React-Redux

Đầu tiên, hãy cài đặt các thư viện cần thiết cho Redux:

```bash
npm install redux react-redux @reduxjs/toolkit
```

### 2. Thiết lập Redux Store

Chúng ta sẽ sử dụng **Redux Toolkit** để tạo store và các slice (khối mã chứa reducer và các action liên quan). Điều này sẽ giúp giảm thiểu boilerplate code.

#### Tạo Redux Slice cho To-Do

Tạo một file `todoSlice.js` trong thư mục `redux` để định nghĩa trạng thái và các hàm reducer cho to-do list:

```javascript
// src/redux/todoSlice.js
import { createSlice } from '@reduxjs/toolkit';

const todoSlice = createSlice({
  name: 'todos',
  initialState: [
    // Danh sách công việc ban đầu (có thể để trống nếu muốn)
    { id: 1, text: 'Learn Redux', completed: false },
    { id: 2, text: 'Build a project', completed: false },
  ],
  reducers: {
    addTodo: (state, action) => {
      const newTodo = {
        id: Date.now(), // Tạo ID duy nhất cho mỗi công việc
        text: action.payload,
        completed: false,
      };
      state.push(newTodo);
    },
    toggleTodo: (state, action) => {
      const todo = state.find(todo => todo.id === action.payload);
      if (todo) {
        todo.completed = !todo.completed;
      }
    },
    deleteTodo: (state, action) => {
      return state.filter(todo => todo.id !== action.payload);
    },
  },
});

export const { addTodo, toggleTodo, deleteTodo } = todoSlice.actions;
export default todoSlice.reducer;
```

Ở đây, `todoSlice` chứa:

- `addTodo`: Thêm một công việc mới vào danh sách.
- `toggleTodo`: Đánh dấu công việc là hoàn thành hoặc chưa hoàn thành.
- `deleteTodo`: Xóa công việc khỏi danh sách.

#### Tạo Store

Tạo file `store.js` trong thư mục `redux` để khởi tạo Redux store với slice vừa tạo.

```javascript
// src/redux/store.js
import { configureStore } from '@reduxjs/toolkit';
import todoReducer from './todoSlice';

const store = configureStore({
  reducer: {
    todos: todoReducer,
  },
});

export default store;
```

### 3. Cấu hình Provider trong ứng dụng React

Chúng ta sẽ sử dụng **Provider** từ `react-redux` để cung cấp store cho toàn bộ ứng dụng React. Sửa `index.js` như sau:

```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './redux/store';
import App from './App';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

### 4. Tạo Component Giao Diện

#### Tạo ToDoList Component

Tạo file `ToDoList.js` trong thư mục `components` để hiển thị danh sách công việc và các nút điều khiển (hoàn thành, xóa).

```javascript
// src/components/ToDoList.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { toggleTodo, deleteTodo } from '../redux/todoSlice';

function ToDoList() {
  const todos = useSelector(state => state.todos);
  const dispatch = useDispatch();

  return (
    <div>
      <h2>To-Do List</h2>
      <ul>
        {todos.map(todo => (
          <li
            key={todo.id}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
          >
            {todo.text}
            <button onClick={() => dispatch(toggleTodo(todo.id))}>
              {todo.completed ? 'Undo' : 'Complete'}
            </button>
            <button onClick={() => dispatch(deleteTodo(todo.id))}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ToDoList;
```

#### Tạo AddToDo Component

Tạo file `AddToDo.js` trong thư mục `components` để thêm công việc mới vào danh sách.

```javascript
// src/components/AddToDo.js
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addTodo } from '../redux/todoSlice';

function AddToDo() {
  const [text, setText] = useState('');
  const dispatch = useDispatch();

  const handleAddTodo = () => {
    if (text.trim()) {
      dispatch(addTodo(text));
      setText('');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Add a new task"
      />
      <button onClick={handleAddTodo}>Add</button>
    </div>
  );
}

export default AddToDo;
```

### 5. Kết hợp các Component trong `App.js`

Trong `App.js`, kết hợp hai component `AddToDo` và `ToDoList` để tạo giao diện hoàn chỉnh.

```javascript
// src/App.js
import React from 'react';
import AddToDo from './components/AddToDo';
import ToDoList from './components/ToDoList';

function App() {
  return (
    <div>
      <h1>To-Do App with Redux</h1>
      <AddToDo />
      <ToDoList />
    </div>
  );
}

export default App;
```

### 6. Kết quả

Với cấu trúc này, bạn đã xây dựng thành công một ứng dụng To-Do sử dụng Redux để quản lý trạng thái:

- Bạn có thể thêm một công việc mới vào danh sách thông qua component `AddToDo`.
- `ToDoList` sẽ hiển thị danh sách công việc hiện tại, cho phép bạn đánh dấu là hoàn thành hoặc chưa hoàn thành, cũng như xóa các công việc khỏi danh sách.

### 7. Kiểm thử

1. **Thêm công việc**: Gõ vào ô input và nhấn nút "Add" để thêm công việc mới.
2. **Hoàn thành công việc**: Nhấn nút "Complete" bên cạnh mỗi công việc để đánh dấu hoàn thành.
3. **Xóa công việc**: Nhấn nút "Delete" để xóa công việc khỏi danh sách.

Ứng dụng này minh họa cách Redux giúp quản lý trạng thái toàn cục của ứng dụng. Redux giúp dễ dàng kiểm soát các hành động thêm, cập nhật, và xóa công việc mà không cần quản lý trực tiếp trạng thái trong từng component, giúp mã dễ bảo trì hơn.
