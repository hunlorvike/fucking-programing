# Sự kiện trong ReactJS

Quản lý sự kiện là một phần thiết yếu trong phát triển ứng dụng React, cho phép bạn tương tác với người dùng và phản hồi lại các hành động của họ. React cung cấp một mô hình xử lý sự kiện rõ ràng và hiệu quả, giúp bạn quản lý sự kiện một cách dễ dàng.

## Khái niệm cơ bản về sự kiện trong React

Sự kiện trong React là các hành động do người dùng thực hiện, như nhấp chuột, nhập liệu, di chuyển chuột, hoặc các hành động khác mà ứng dụng có thể phản hồi. React xử lý các sự kiện này thông qua một hệ thống sự kiện ảo, giúp tối ưu hóa hiệu suất và đảm bảo tính nhất quán trong việc quản lý sự kiện.

## Các bước xử lý sự kiện trong React

### 1. Định nghĩa sự kiện

Trong React, bạn có thể định nghĩa sự kiện bằng cách sử dụng các thuộc tính sự kiện (event attributes) trên các component. Các thuộc tính sự kiện trong React thường được viết theo cú pháp camelCase, khác với HTML thông thường.

```javascript
<button onClick={handleClick}>Click me</button>
```

### 2. Tạo hàm xử lý sự kiện

Hàm xử lý sự kiện (event handler) là nơi bạn xác định hành động sẽ xảy ra khi sự kiện được kích hoạt. Bạn có thể tạo một hàm đơn giản như sau:

```javascript
function handleClick() {
  console.log('Button was clicked!');
}
```

### 3. Kết hợp sự kiện và hàm xử lý

Khi kết hợp hàm xử lý với sự kiện, bạn có thể truyền hàm xử lý vào thuộc tính sự kiện của component.

```javascript
function App() {
  const handleClick = () => {
    console.log('Button was clicked!');
  };

  return (
    <button onClick={handleClick}>Click me</button>
  );
}
```

## Các loại sự kiện trong React

React hỗ trợ nhiều loại sự kiện khác nhau, từ sự kiện chuột đến sự kiện bàn phím và sự kiện form. Dưới đây là một số loại sự kiện phổ biến:

### 1. Sự kiện chuột

- **onClick**: Kích hoạt khi người dùng nhấp chuột vào một phần tử.
- **onDoubleClick**: Kích hoạt khi người dùng nhấp đúp chuột vào phần tử.
- **onMouseEnter**: Kích hoạt khi con trỏ chuột di chuyển vào phần tử.
- **onMouseLeave**: Kích hoạt khi con trỏ chuột rời khỏi phần tử.

```javascript
<button onClick={handleClick}>Click me</button>
```

### 2. Sự kiện bàn phím

- **onKeyDown**: Kích hoạt khi một phím được nhấn xuống.
- **onKeyPress**: Kích hoạt khi một phím được nhấn (đã bị loại bỏ trong các phiên bản mới của React).
- **onKeyUp**: Kích hoạt khi một phím được thả ra.

```javascript
<input type="text" onKeyDown={handleKeyDown} />
```

### 3. Sự kiện form

- **onChange**: Kích hoạt khi giá trị của một input, textarea, hoặc select thay đổi.
- **onSubmit**: Kích hoạt khi một form được gửi.

```javascript
<form onSubmit={handleSubmit}>
  <input type="text" onChange={handleChange} />
  <button type="submit">Submit</button>
</form>
```

## Sự kiện và quản lý trạng thái

Khi xử lý sự kiện, bạn thường cần cập nhật state để phản ánh các thay đổi. Trong React, bạn có thể sử dụng hook `useState` để quản lý state trong component.

### Ví dụ: Quản lý sự kiện nhấp chuột

```javascript
import React, { useState } from 'react';

function ClickCounter() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <button onClick={handleClick}>Clicked {count} times</button>
    </div>
  );
}
```

### Ví dụ: Quản lý sự kiện nhập liệu

```javascript
import React, { useState } from 'react';

function TextInput() {
  const [text, setText] = useState('');

  const handleChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div>
      <input type="text" onChange={handleChange} />
      <p>You typed: {text}</p>
    </div>
  );
}
```

## Ngăn chặn sự kiện mặc định

Trong một số trường hợp, bạn có thể muốn ngăn chặn hành vi mặc định của sự kiện, chẳng hạn như khi gửi form. Để làm điều này, bạn có thể gọi `event.preventDefault()` trong hàm xử lý sự kiện.

```javascript
const handleSubmit = (event) => {
  event.preventDefault(); // Ngăn chặn hành vi mặc định
  // Thực hiện hành động gửi form
};
```

## Truyền tham số cho hàm xử lý sự kiện

Nếu bạn muốn truyền tham số cho hàm xử lý sự kiện, bạn có thể sử dụng một hàm ẩn danh hoặc arrow function:

```javascript
<button onClick={() => handleClick('Hello!')}>Click me</button>
```

## Tóm tắt về Sự kiện trong React

| Tính năng                | Mô tả                                        |
|-------------------------|---------------------------------------------|
| **Sự kiện chuột**      | `onClick`, `onDoubleClick`, `onMouseEnter`, `onMouseLeave` |
| **Sự kiện bàn phím**   | `onKeyDown`, `onKeyUp`                     |
| **Sự kiện form**       | `onChange`, `onSubmit`                     |
| **Ngăn chặn sự kiện**   | `event.preventDefault()`                    |
| **Quản lý trạng thái**  | Sử dụng hook `useState` để cập nhật state   |
| **Truyền tham số**      | Sử dụng arrow function để truyền tham số    |

## Kết luận

Sự kiện trong React là một phần quan trọng trong việc tạo ra các ứng dụng web tương tác và linh hoạt. Với các thuộc tính sự kiện rõ ràng và mô hình xử lý sự kiện hiệu quả, React giúp lập trình viên dễ dàng quản lý và xử lý các hành động của người dùng. Hiểu rõ cách thức hoạt động của sự kiện trong React sẽ giúp bạn xây dựng những ứng dụng tốt hơn và tăng cường trải nghiệm người dùng.
