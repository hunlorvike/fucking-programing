# Tìm hiểu về Hooks trong ReactJS

**Hooks** là một tính năng quan trọng trong React 16.8, cho phép bạn sử dụng trạng thái và các tính năng khác của React mà không cần viết class. Chúng đơn giản hóa cấu trúc component, dễ dàng tái sử dụng logic và cải thiện khả năng bảo trì mã nguồn.

## Quy tắc và điều kiện khi sử dụng Hooks

### 1. Gọi Hooks ở Cấp Cao Nhất của Component

- **Mô tả**: Gọi Hooks ở cấp cao nhất của component, không trong vòng lặp, điều kiện hay hàm lồng.
  
- **Lý do**: Giúp React duy trì thứ tự gọi giữa các lần render, tránh lỗi không mong muốn.

- **Ví dụ**:

  ```javascript
  function MyComponent() {
      const [count, setCount] = useState(0); // Đúng
      useEffect(() => {
          console.log(count);
      }, [count]);

      return <div>{count}</div>;
  }
  ```

### 2. Không Gọi Hooks Trong Vòng Lặp hoặc Hàm Lồng

- **Mô tả**: Hooks không được gọi trong vòng lặp `for`, `map`, hoặc hàm lồng.

- **Lý do**: Ngăn thay đổi thứ tự gọi Hooks, tránh vấn đề quản lý trạng thái.

- **Ví dụ**:

  ```javascript
  function MyComponent() {
      const [count, setCount] = useState(0);
      useEffect(() => {
          console.log(count);
      }, [count]); // Đúng

      return <div>{count}</div>;
  }
  ```

### 3. Sử Dụng Hooks Trong Component hoặc Custom Hook

- **Mô tả**: Gọi Hooks chỉ trong function components hoặc custom hooks (tên bắt đầu bằng "use").

- **Lý do**: Giúp React theo dõi và quản lý trạng thái một cách chính xác.

- **Ví dụ**:

  ```javascript
  function MyComponent() {
      const [count, setCount] = useState(0); // Đúng
      return <div>{count}</div>;
  }

  function useMyCustomHook() {
      const [value, setValue] = useState(0); // Đúng
      return [value, setValue];
  }
  ```

### 4. Sử Dụng Dependency Array Đúng Cách

- **Mô tả**: Đối với `useEffect`, phải có mảng phụ thuộc để xác định khi nào effect cần chạy lại.

- **Ví dụ**:

  ```javascript
  useEffect(() => {
      // Logic thực hiện side effect
  }, [count]); // Chạy lại khi count thay đổi
  ```

### 5. Cleanup Effects

- **Mô tả**: Trong `useEffect`, có thể trả về hàm cleanup để thực hiện dọn dẹp khi component unmount hoặc trước khi effect chạy lại.

- **Ví dụ**:

  ```javascript
  useEffect(() => {
      const timer = setTimeout(() => {
          console.log('Hello World');
      }, 1000);

      return () => clearTimeout(timer); // Dọn dẹp
  }, []);
  ```

### 6. Sử Dụng Custom Hooks Để Tái Sử Dụng Logic

- **Mô tả**: Tạo custom hooks để tái sử dụng logic giữa các component.

- **Ví dụ**:

  ```javascript
  function useFetch(url) {
      const [data, setData] = useState(null);
      const [loading, setLoading] = useState(true);

      useEffect(() => {
          fetch(url)
              .then(response => response.json())
              .then(data => {
                  setData(data);
                  setLoading(false);
              });
      }, [url]);

      return { data, loading };
  }

  function DataComponent() {
      const { data, loading } = useFetch('https://api.example.com/data');

      if (loading) return <div>Loading...</div>;
      return <div>Data: {JSON.stringify(data)}</div>;
  }
  ```

## Tóm tắt

- **Gọi Hooks đúng nơi**: Gọi ở cấp cao nhất, không bên trong điều kiện hay vòng lặp.
- **Sử dụng Dependency Array**: Đảm bảo xác định các giá trị mà effect phụ thuộc vào.
- **Dọn dẹp Resource**: Sử dụng cleanup effects để tránh rò rỉ bộ nhớ.
- **Tái sử dụng Logic**: Sử dụng custom hooks để cải thiện khả năng bảo trì mã nguồn.

## Các Hooks cơ bản trong React

### 1. `useState`

- **Bản chất**: Thêm trạng thái vào function component.

- **Cú pháp**:

  ```javascript
  const [state, setState] = useState(initialState);
  ```

- **Ví dụ**:

  ```javascript
  function Counter() {
      const [count, setCount] = useState(0);

      return (
          <div>
              <p>Count: {count}</p>
              <button onClick={() => setCount(count + 1)}>Tăng</button>
          </div>
      );
  }
  ```

### 2. `useEffect`

- **Bản chất**: Thực hiện các side effects trong component.

- **Cú pháp**:

  ```javascript
  useEffect(() => {
      // Logic thực hiện side effect
      return () => {
          // Hàm cleanup (tuỳ chọn)
      };
  }, [dependencies]);
  ```

- **Ví dụ**:

  ```javascript
  function DataFetcher() {
      const [data, setData] = useState(null);

      useEffect(() => {
          fetch('https://api.example.com/data')
              .then(response => response.json())
              .then(data => setData(data));
      }, []); // Chạy 1 lần sau lần render đầu tiên

      return (
          <div>
              {data ? <p>Dữ liệu: {JSON.stringify(data)}</p> : <p>Đang tải...</p>}
          </div>
      );
  }
  ```

### 3. `useContext`

- **Bản chất**: Sử dụng context API để chia sẻ dữ liệu giữa các component.

- **Cú pháp**:

  ```javascript
  const value = useContext(MyContext);
  ```

- **Ví dụ**:

  ```javascript
  const ThemeContext = React.createContext('light');

  function ThemedComponent() {
      const theme = useContext(ThemeContext);
      return <div className={theme}>This is a {theme} themed component.</div>;
  }

  function App() {
      return (
          <ThemeContext.Provider value="dark">
              <ThemedComponent />
          </ThemeContext.Provider>
      );
  }
  ```

### 4. `useReducer`

- **Bản chất**: Thay thế cho `useState`, thích hợp cho state phức tạp.

- **Cú pháp**:

  ```javascript
  const [state, dispatch] = useReducer(reducer, initialState);
  ```

- **Ví dụ**:

  ```javascript
  const initialState = { count: 0 };

  function reducer(state, action) {
      switch (action.type) {
          case 'increment':
              return { count: state.count + 1 };
          case 'decrement':
              return { count: state.count - 1 };
          default:
              throw new Error();
      }
  }

  function Counter() {
      const [state, dispatch] = useReducer(reducer, initialState);

      return (
          <div>
              <p>Count: {state.count}</p>
              <button onClick={() => dispatch({ type: 'increment' })}>Tăng</button>
              <button onClick={() => dispatch({ type: 'decrement' })}>Giảm</button>
          </div>
      );
  }
  ```

### 5. `useMemo` và `useCallback`

- **`useMemo`**: Tối ưu hóa hiệu suất bằng cách lưu trữ giá trị đã tính toán.

  **Ví dụ**:

  ```javascript
  function Component({ items }) {
      const total = useMemo(() => items.reduce((acc, item) => acc + item, 0), [items]);

      return <div>Tổng: {total}</div>;
  }
  ```

- **`useCallback`**: Lưu trữ các hàm để tránh tạo lại hàm trong mỗi lần render.

  **Ví dụ**:

  ```javascript
  function Component({ onClick }) {
      const handleClick = useCallback(() => {
          console.log('Clicked');
          onClick();
      }, [onClick]);

      return <button onClick={handleClick}>Click me</button>;
  }
  ```

### 6. `useRef`

- **Bản chất**: Tạo đối tượng ref để lưu trữ giá trị không thay đổi qua các lần render.

- **Cú pháp**:

  ```javascript
  const myRef = useRef(initialValue);
  ```

- **Ví dụ**:

```javascript
function FocusInput() {
    const inputRef = useRef(null);

    const focusInput = () => {
        inputRef.current.focus();
    };

    return (
        <div>
            <input

ref={inputRef} />
            <button onClick={focusInput}>Lấy nét vào ô input</button>
        </div>
    );
}
```

## Kết luận

Hooks trong ReactJS mang lại nhiều lợi ích cho việc phát triển ứng dụng. Việc hiểu và áp dụng đúng các quy tắc và hooks sẽ giúp bạn viết mã hiệu quả hơn, dễ bảo trì và mở rộng.
