# Tìm hiểu về JSX trong ReactJS

**JSX** (JavaScript XML) là một cú pháp mở rộng cho JavaScript, được sử dụng trong React để mô tả cấu trúc giao diện
người dùng. JSX cho phép bạn viết mã HTML trong tệp JavaScript, giúp cho việc tạo và cấu trúc giao diện trở nên trực
quan và dễ dàng hơn.

## Tại sao lại sử dụng JSX?

### Lợi ích của JSX

1. **Cú pháp quen thuộc**: JSX cho phép bạn viết mã giống như HTML, giúp lập trình viên dễ dàng hơn khi làm việc với cấu
   trúc giao diện.
2. **Tích hợp với JavaScript**: Bạn có thể kết hợp mã JavaScript trực tiếp trong JSX, cho phép bạn sử dụng các biểu thức
   và logic một cách linh hoạt.
3. **Dễ dàng bảo trì**: Với JSX, mã nguồn trở nên dễ đọc và dễ bảo trì hơn, vì nó phản ánh rõ ràng cấu trúc của giao
   diện.

## Cú pháp của JSX

### 1. Cú pháp cơ bản

- JSX bắt đầu và kết thúc với dấu ngoặc đơn (parentheses) nếu cần thiết. Nếu bạn chỉ trả về một dòng duy nhất, bạn có
  thể không cần sử dụng dấu ngoặc đơn.

**Ví dụ**:

```javascript
const element = <h1>Hello, world!</h1>;
```

### 2. Nhúng biểu thức

- Bạn có thể nhúng biểu thức JavaScript bên trong JSX bằng cách sử dụng dấu ngoặc nhọn `{}`. Điều này cho phép bạn kết
  hợp dữ liệu và logic vào giao diện.

**Ví dụ**:

```javascript
const name = 'React';
const element = <h1>Hello, {name}!</h1>;
```

### 3. Thuộc tính trong JSX

- Các thuộc tính trong JSX giống như thuộc tính trong HTML, nhưng chúng được viết theo camelCase thay vì lowercase. Ví
  dụ, thuộc tính `class` trong HTML sẽ trở thành `className` trong JSX.

**Ví dụ**:

```javascript
const element = <div className="container">Nội dung</div>;
```

### 4. Biểu thức điều kiện

- Bạn có thể sử dụng các biểu thức điều kiện để hiển thị nội dung khác nhau trong JSX, thường sử dụng toán tử điều
  kiện (ternary operator).

**Ví dụ**:

```javascript
const isLoggedIn = true;
const element = (
    <div>
        {isLoggedIn ? <h1>Chào mừng quay lại!</h1> : <h1>Xin chào, khách!</h1>}
    </div>
);
```

### 5. Lặp qua danh sách

- JSX hỗ trợ việc lặp qua danh sách các phần tử bằng cách sử dụng phương thức `map` trong JavaScript.

**Ví dụ**:

```javascript
const items = ['Apple', 'Banana', 'Cherry'];
const listItems = items.map(item => <li key={item}>{item}</li>);

const element = <ul>{listItems}</ul>;
```

### 6. Kết hợp với Component

- JSX cho phép bạn sử dụng component giống như các thẻ HTML. Bạn chỉ cần gọi component bằng tên của nó với chữ cái đầu
  tiên viết hoa.

**Ví dụ**:

```javascript
function Welcome(props) {
    return <h1>Xin chào, {props.name}!</h1>;
}

const element = <Welcome name="React" />;
```

## Kết luận

JSX là một phần quan trọng trong React, giúp lập trình viên dễ dàng tạo ra giao diện người dùng trực quan và dễ bảo trì.
Bằng cách kết hợp JavaScript và HTML, JSX tạo ra một trải nghiệm phát triển mượt mà và hiệu quả. Khi bạn làm quen với
JSX, bạn sẽ thấy rằng nó trở thành một công cụ mạnh mẽ trong việc xây dựng ứng dụng React.
