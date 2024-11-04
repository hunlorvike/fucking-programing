# Vòng đời của Component trong Lập trình Front-End

Trong lập trình giao diện người dùng (UI) hiện đại, đặc biệt là với các framework và thư viện như **React**, **Vue.js** hoặc **Angular**, khái niệm **vòng đời (lifecycle)** của một **component** rất quan trọng. Mỗi component trong ứng dụng front-end sẽ trải qua các giai đoạn vòng đời khác nhau, từ khi được tạo ra cho đến khi bị xóa khỏi giao diện. Hiểu rõ các giai đoạn này giúp lập trình viên tối ưu hóa hiệu suất, quản lý tài nguyên và kiểm soát chặt chẽ các thao tác xảy ra trong suốt quá trình hoạt động của component.

## Các Giai đoạn chính trong Vòng đời của Component

Một component thường trải qua các giai đoạn sau:

1. **Giai đoạn khởi tạo (Initialization)**:
   - Component được khởi tạo với các **dữ liệu ban đầu**. Các giá trị của **state** (trạng thái nội bộ) và **props** (dữ liệu truyền vào từ component cha) sẽ được thiết lập trong giai đoạn này.
   - Đây là lúc component nhận được những giá trị đầu tiên cần thiết để sẵn sàng render lên giao diện.

2. **Giai đoạn gắn vào DOM (Mounting)**:
   - Sau khi khởi tạo, component bắt đầu được **gắn vào giao diện** (DOM). Đây là khi nó xuất hiện lần đầu tiên trong trình duyệt.
   - Các thao tác khởi tạo như gọi **API** để lấy dữ liệu, đăng ký các sự kiện, hoặc các tác vụ khởi tạo khác thường được thực hiện ở giai đoạn này.

3. **Giai đoạn cập nhật (Updating)**:
   - Mỗi khi có thay đổi về **props** hoặc **state**, component sẽ được render lại để phản ánh những thay đổi đó.
   - Đây là lúc các thao tác kiểm tra và kiểm soát cập nhật cần được thực hiện, nhằm tránh việc render lại không cần thiết và tối ưu hiệu suất của ứng dụng.

4. **Giai đoạn hủy (Unmounting)**:
   - Khi component không còn cần thiết và bị xóa khỏi giao diện, nó sẽ đi vào giai đoạn hủy.
   - Các tài nguyên mà component đã sử dụng (như các sự kiện, bộ đếm thời gian) cần được giải phóng để tránh tình trạng rò rỉ bộ nhớ, giữ cho ứng dụng hoạt động hiệu quả.

## Vòng đời của Component trong ReactJS

Trong **React**, vòng đời của component được quản lý qua các phương thức lifecycle đối với **class component** và qua **hooks** đối với **function component**. Dưới đây là chi tiết các phương thức và hook thường dùng trong mỗi giai đoạn của vòng đời component trong React.

### 1. Giai đoạn Khởi tạo trong React

- **Class Component**:
  - `constructor(props)`: Hàm khởi tạo, được gọi đầu tiên khi component được tạo, cho phép khởi tạo state và nhận giá trị props từ component cha.
  
- **Function Component**:
  - Với function component, không cần hàm khởi tạo riêng. State ban đầu có thể được thiết lập bằng hook `useState` trực tiếp bên trong hàm component.

### 2. Giai đoạn Gắn vào DOM trong React

- **Class Component**:
  - `componentDidMount()`: Được gọi ngay sau khi component đã được render lần đầu tiên. Đây là nơi thích hợp để thực hiện các thao tác như gọi API, thiết lập các sự kiện hoặc tạo kết nối.

- **Function Component**:
  - `useEffect(() => { ... }, [])`: Trong function component, `useEffect` với dependency array rỗng `[]` sẽ chạy một lần duy nhất sau lần render đầu tiên, tương tự `componentDidMount` trong class component.

    ```javascript
    useEffect(() => {
        // Logic chạy khi component mount
    }, []); // Dependency array rỗng để chạy một lần
    ```

### 3. Giai đoạn Cập nhật trong React

- **Class Component**:
  - `componentDidUpdate(prevProps, prevState)`: Được gọi sau khi component được cập nhật (khi `props` hoặc `state` thay đổi).
  - `shouldComponentUpdate(nextProps, nextState)`: Được sử dụng để kiểm soát xem component có cần cập nhật hay không, trả về `true` hoặc `false`.

- **Function Component**:
  - `useEffect(() => { ... }, [dependencies])`: Trong function component, `useEffect` có thể được thiết lập để chạy mỗi khi một dependency cụ thể thay đổi, tương tự `componentDidUpdate`.

    ```javascript
    useEffect(() => {
        // Logic khi state hoặc props thay đổi
    }, [dependency1, dependency2]); // Chỉ chạy khi dependency1 hoặc dependency2 thay đổi
    ```

### 4. Giai đoạn Hủy trong React

- **Class Component**:
  - `componentWillUnmount()`: Được gọi ngay trước khi component bị gỡ khỏi DOM. Thích hợp để giải phóng các tài nguyên như sự kiện, hủy bỏ bộ đếm thời gian.

- **Function Component**:
  - `useEffect(() => { return () => { ... } }, [])`: Với function component, `useEffect` có thể trả về một hàm cleanup. Hàm này sẽ được gọi khi component bị unmount, giúp giải phóng tài nguyên tương tự như `componentWillUnmount`.

    ```javascript
    useEffect(() => {
        const handleResize = () => console.log("Window resized");
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []); // Chạy một lần khi mount và cleanup khi unmount
    ```

## Vòng đời của Component trong Angular

Trong **Angular**, các giai đoạn vòng đời của component được quản lý thông qua các lifecycle hooks, mỗi hook đại diện cho một giai đoạn khác nhau trong vòng đời của component. Các hook này được triển khai trong một **class component** thông qua các phương thức cụ thể.

### 1. Giai đoạn Khởi tạo trong Angular

- **`ngOnInit()`**: Được gọi sau khi Angular khởi tạo dữ liệu và thiết lập các input bindings cho component, tương đương với `componentDidMount` trong React.
- **Khởi tạo dependency**: Các service có thể được injected trong constructor, giúp thiết lập các dữ liệu cần thiết.

### 2. Giai đoạn Gắn vào DOM trong Angular

- **`ngAfterViewInit()`**: Được gọi khi các view của component và các thành phần con đã được render lên giao diện.
  - Đây là nơi thích hợp để tương tác với các phần tử DOM hoặc gọi API lấy dữ liệu.
- **`ngAfterContentInit()`**: Được gọi khi các nội dung được truyền vào qua `ng-content` đã được khởi tạo.

### 3. Giai đoạn Cập nhật trong Angular

- **`ngOnChanges(changes)`**: Được gọi mỗi khi có thay đổi ở các input properties. Thực hiện trước bất kỳ thao tác cập nhật nào khác.
- **`ngDoCheck()`**: Hook này cho phép developer tùy chỉnh logic kiểm tra thay đổi trong component. Tương tự `shouldComponentUpdate` trong React.
- **`ngAfterContentChecked()`** và **`ngAfterViewChecked()`**: Được gọi sau khi Angular kiểm tra nội dung hoặc view của component, hữu ích để xử lý các thay đổi phát sinh sau các lifecycle hooks khác.

### 4. Giai đoạn Hủy trong Angular

- **`ngOnDestroy()`**: Được gọi trước khi Angular hủy component. Đây là nơi thích hợp để dọn dẹp các tài nguyên, hủy bộ đếm thời gian, hoặc ngắt kết nối sự kiện tương tự như `componentWillUnmount` trong React.

## Tóm tắt Vòng đời trong Angular

| Giai đoạn         | Angular Lifecycle Hook                |
|-||
| Khởi tạo          | `ngOnInit`, `ngAfterContentInit`      |
| Gắn vào DOM       | `ngAfterViewInit`, `ngAfterContentInit` |
| Cập nhật          | `ngOnChanges`, `ngDoCheck`, `ngAfterContentChecked`, `ngAfterViewChecked` |
| Hủy               | `ngOnDestroy`                         |

## So sánh Vòng đời của Component trong React và Angular

| Giai đoạn         | React Class Component             | React Function Component                 | Angular Lifecycle Hook               |
|-|--||--|
| Khởi tạo          | `constructor`                    | `useState`                               | `ngOnInit`, `ngAfterContentInit`     |
| Gắn vào DOM       | `componentDidMount`              | `useEffect(() => { }, [])`               | `ngAfterViewInit`, `ngAfterContentInit` |
| Cập nhật          | `componentDidUpdate`, `shouldComponentUpdate` | `useEffect(() => { }, [deps])`         | `ngOnChanges`, `ngDoCheck`, `ngAfterContentChecked`, `ngAfterViewChecked` |
| Hủy               | `componentWillUnmount`           | `useEffect(() => { return () => { } }, [])` | `ngOnDestroy`                       |
