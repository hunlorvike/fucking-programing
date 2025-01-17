# Tối Ưu Hóa Hiệu Suất Trong React: Kỹ Thuật Memoization và Quá Trình Render

React cung cấp nhiều công cụ để tối ưu hóa hiệu suất ứng dụng, đặc biệt là giảm thiểu các lần render không cần thiết và
quản lý bộ nhớ. Những kỹ thuật như **memoization**, **React.memo**, **useMemo**, và **useCallback** giúp tối ưu hóa quá
trình render và đảm bảo rằng các component chỉ render lại khi thực sự cần thiết.

## 1. **React.memo**

`React.memo` là một HOC (higher-order component) giúp ngăn chặn các component con không render lại nếu props không thay
đổi. Điều này đặc biệt hữu ích với các component ít thay đổi dữ liệu, giúp giảm thiểu lượng render không cần thiết.

### Cách sử dụng:

```javascript
import React from 'react';

const ChildComponent = React.memo(({ data }) => {
  console.log('Child component rendered');
  return <div>{data}</div>;
});

export default ChildComponent;
```

Trong ví dụ này, `ChildComponent` sẽ không render lại nếu props `data` không thay đổi.

### Khi nào nên sử dụng:

- Khi component con nhận các props ít thay đổi và không phụ thuộc vào state bên trong.
- Không nên sử dụng nếu component cần luôn render lại khi component cha render.

## 2. **useMemo**

`useMemo` là một Hook giúp ghi nhớ (memoize) giá trị của một biến. React chỉ tính toán lại giá trị khi các dependencies
thay đổi, giúp tối ưu hóa các phép tính phức tạp hoặc các dữ liệu có chi phí tính toán cao.

### Cách sử dụng:

```javascript
import React, { useMemo } from 'react';

function ExpensiveComponent({ number }) {
  const computedValue = useMemo(() => {
    // Giả sử đây là một phép tính phức tạp
    return number ** 2;
  }, [number]);

  return <div>Computed Value: {computedValue}</div>;
}

export default ExpensiveComponent;
```

### Khi nào nên sử dụng:

- Khi cần tối ưu các phép tính tốn kém chỉ phụ thuộc vào các biến cụ thể.
- Tránh sử dụng quá nhiều, vì có thể làm cho code trở nên phức tạp và khó đọc.

## 3. **useCallback**

`useCallback` là một Hook giúp ghi nhớ hàm (memoize functions), đảm bảo rằng React chỉ tạo một hàm mới khi các
dependencies thay đổi. Điều này đặc biệt hữu ích khi các hàm được truyền xuống component con và có thể gây ra render lại
không cần thiết.

### Cách sử dụng:

```javascript
import React, { useCallback, useState } from 'react';

function ParentComponent() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(prevCount => prevCount + 1);
  }, []);

  return (
    <div>
      <button onClick={increment}>Increment</button>
      <ChildComponent increment={increment} />
    </div>
  );
}

const ChildComponent = React.memo(({ increment }) => {
  console.log('Child component rendered');
  return <button onClick={increment}>Increment from Child</button>;
});

export default ParentComponent;
```

Trong ví dụ này, `ChildComponent` sẽ không render lại khi `ParentComponent` render, vì `increment` đã được ghi nhớ (
memoize) với `useCallback`.

### Khi nào nên sử dụng:

- Khi truyền hàm xuống các component con qua props, đặc biệt với các component sử dụng `React.memo`.
- Tránh sử dụng cho các hàm đơn giản hoặc hàm không được truyền xuống component con.

## 4. **Tối Ưu Hóa Quá Trình Render**

### Tránh Render Lại Không Cần Thiết

Để hạn chế render không cần thiết, hãy áp dụng các kỹ thuật sau:

1. **Kiểm soát component con**: Sử dụng `React.memo` và `useCallback` để ngăn các component con không render lại khi
   không cần thiết.
2. **Chia nhỏ component**: Các component nhỏ và ít phức tạp sẽ dễ quản lý và tối ưu hóa hơn. Chia nhỏ các phần của
   component giúp giới hạn phạm vi render lại.

### Lazy Loading và Code Splitting

Lazy loading cho phép tải các component chỉ khi cần thiết, đặc biệt hữu ích khi ứng dụng có nhiều trang hoặc các thành
phần không cần tải ngay từ đầu.

```javascript
import React, { Suspense, lazy } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <HeavyComponent />
      </Suspense>
    </div>
  );
}

export default App;
```

### Tối Ưu Hóa với List (Danh sách)

Sử dụng `key` thích hợp và tránh tạo key động sẽ giúp React quản lý hiệu quả việc render lại của các item trong list:

```javascript
const items = [1, 2, 3];

return (
  <ul>
    {items.map(item => (
      <li key={item}>{item}</li>
    ))}
  </ul>
);
```

## Kết Luận

Các kỹ thuật tối ưu hóa hiệu suất trong React như `React.memo`, `useMemo`, `useCallback` giúp giảm thiểu render không
cần thiết và tăng hiệu quả sử dụng tài nguyên. Khi áp dụng những kỹ thuật này, hãy đảm bảo chỉ sử dụng khi cần thiết để
tránh làm cho mã trở nên phức tạp và khó duy trì.
