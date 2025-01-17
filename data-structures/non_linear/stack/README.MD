# Ngăn Xếp (Stack)

## Mục lục

1. [Đặc điểm](#đặc-điểm)
2. [Ưu điểm và nhược điểm](#ưu-điểm-và-nhược-điểm)
3. [Ứng dụng](#ứng-dụng)
4. [Ví dụ triển khai ngăn xếp trong TypeScript](#ví-dụ-triển-khai-ngăn-xếp-trong-typescript)
5. [Bổ sung](#bổ-sung)

---

## Đặc điểm

- Ngăn xếp là một cấu trúc dữ liệu tuyến tính, trong đó các phần tử được sắp xếp và truy cập theo nguyên tắc LIFO (Last
  In, First Out), tức là phần tử được thêm vào cuối cùng sẽ được lấy ra đầu tiên.
- **Các thao tác chính:**
    - **Push:** Thêm một phần tử vào đỉnh ngăn xếp.
    - **Pop:** Lấy ra phần tử ở đỉnh ngăn xếp.
    - **Peek:** Xem phần tử ở đỉnh ngăn xếp mà không lấy nó ra.
    - **IsEmpty:** Kiểm tra xem ngăn xếp có rỗng hay không.

## Ưu điểm và nhược điểm

- **Ưu điểm:**

    - **Quản lý lịch sử hiệu quả:** Lưu trữ lịch sử thao tác trong các ứng dụng (Undo/Redo, điều hướng lịch sử).
    - **Dễ triển khai:** Ngăn xếp dễ triển khai bằng mảng hoặc danh sách liên kết.
    - **Kiểm soát luồng chương trình:** Được sử dụng để quản lý bộ nhớ và luồng thực thi trong lập trình.

- **Nhược điểm:**
    - **Truy cập hạn chế:** Chỉ có thể thao tác với phần tử ở đỉnh, không thể truy cập trực tiếp các phần tử khác.
    - **Khó tìm kiếm:** Tìm kiếm một phần tử cụ thể yêu cầu duyệt qua ngăn xếp với độ phức tạp O(n).

## Ứng dụng

- **Quản lý bộ nhớ:** Được sử dụng trong quản lý bộ nhớ trong các ngôn ngữ lập trình.
- **Kiểm tra biểu thức:** Kiểm tra tính hợp lệ của các biểu thức chứa dấu ngoặc.
- **Giải thuật quay lui (backtracking):** Lưu trữ trạng thái trong các thuật toán quay lui.
- **Lập trình hướng đối tượng:** Quản lý các đối tượng được tạo trong quá trình thực thi chương trình.

## Ví dụ triển khai ngăn xếp trong TypeScript

```typescript
class Stack<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  // Thêm phần tử vào đỉnh ngăn xếp
  push(item: T): void {
    this.items.push(item);
  }

  // Lấy phần tử ở đỉnh ngăn xếp và xóa nó khỏi ngăn xếp
  pop(): T | undefined {
    return this.items.pop();
  }

  // Xem phần tử ở đỉnh ngăn xếp mà không xóa nó
  peek(): T | undefined {
    return this.items.length > 0
      ? this.items[this.items.length - 1]
      : undefined;
  }

  // Kiểm tra ngăn xếp có rỗng không
  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

// Sử dụng ngăn xếp
const myStack = new Stack<number>();

// Thêm các phần tử vào ngăn xếp
myStack.push(1);
myStack.push(2);
myStack.push(3);

// Lấy ra phần tử ở đỉnh ngăn xếp
console.log(myStack.pop()); // Output: 3

// Xem phần tử ở đỉnh ngăn xếp
console.log(myStack.peek()); // Output: 2

// Kiểm tra ngăn xếp có rỗng không
console.log(myStack.isEmpty()); // Output: false
```

## Bổ sung

Ngăn xếp là một cấu trúc dữ liệu cơ bản trong lập trình, xuất hiện trong nhiều thuật toán và cấu trúc dữ liệu khác.
Trong TypeScript, ta có thể dễ dàng triển khai ngăn xếp bằng cách sử dụng mảng hoặc danh sách liên kết, với các thao tác
`push`, `pop`, `peek`, và `isEmpty`.
