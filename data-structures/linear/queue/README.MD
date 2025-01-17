# Hàng đợi (Queue)

## Mục lục

1. [Đặc điểm](#Đặc-điểm)
2. [Ưu điểm](#Ưu-điểm)
3. [Nhược điểm](#Nhược-điểm)
4. [Ứng dụng](#Ứng-dụng)
5. [Ví dụ triển khai trong TypeScript](#Ví-dụ-triển-khai-trong-TypeScript)
6. [Bổ sung](#Bổ-sung)

---

## Đặc điểm

- Là một cấu trúc dữ liệu tuyến tính, tức là các phần tử được sắp xếp theo một thứ tự tuyến tính.
- Tuân theo nguyên tắc FIFO (First In, First Out): Phần tử được thêm vào đầu tiên sẽ được lấy ra đầu tiên.
- Có hai thao tác chính:
    - **Enqueue**: Thêm một phần tử vào cuối hàng đợi.
    - **Dequeue**: Lấy ra phần tử ở đầu hàng đợi.
- Ngoài ra, còn có các thao tác khác như:
    - **Peek**: Xem phần tử ở đầu hàng đợi mà không lấy nó ra.
    - **IsEmpty**: Kiểm tra xem hàng đợi có rỗng hay không.

## Ưu điểm

- **Xử lý dữ liệu theo thứ tự**: Hàng đợi rất hiệu quả khi xử lý dữ liệu theo thứ tự đến trước, chẳng hạn như:
    - Lập lịch CPU: Các tiến trình được thêm vào hàng đợi và xử lý theo thứ tự đến.
    - Quản lý yêu cầu trong hệ thống mạng: Các yêu cầu được thêm vào hàng đợi và xử lý theo thứ tự đến.
- **Dễ triển khai**: Hàng đợi có thể được triển khai một cách đơn giản bằng mảng hoặc danh sách liên kết.

## Nhược điểm

- **Truy cập hạn chế**: Chỉ có thể thao tác với phần tử ở đầu và cuối hàng đợi. Việc truy cập các phần tử khác trong
  hàng đợi yêu cầu dequeue các phần tử ở trên.
- **Khó tìm kiếm**: Việc tìm kiếm một phần tử cụ thể trong hàng đợi có độ phức tạp thời gian O(n) (n là số lượng phần
  tử).

## Ứng dụng

- **Lập lịch CPU**: Các tiến trình được thêm vào hàng đợi và xử lý theo thứ tự đến.
- **Quản lý yêu cầu trong hệ thống mạng**: Các yêu cầu được thêm vào hàng đợi và xử lý theo thứ tự đến.
- **Xử lý dữ liệu trong trò chơi**: Hàng đợi được sử dụng để lưu trữ các sự kiện xảy ra trong trò chơi và xử lý chúng
  theo thứ tự.
- **Hệ thống in ấn**: Các công việc in được thêm vào hàng đợi và xử lý theo thứ tự đến.

## Ví dụ triển khai trong TypeScript

```typescript
class Queue<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  // Thêm một phần tử vào cuối hàng đợi
  enqueue(item: T): void {
    this.items.push(item);
  }

  // Lấy ra phần tử ở đầu hàng đợi
  dequeue(): T | null {
    if (!this.isEmpty()) {
      return this.items.shift() || null;
    } else {
      return null;
    }
  }

  // Xem phần tử ở đầu hàng đợi mà không lấy nó ra
  peek(): T | null {
    if (!this.isEmpty()) {
      return this.items[0];
    } else {
      return null;
    }
  }

  // Kiểm tra xem hàng đợi có rỗng hay không
  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

// Tạo một hàng đợi
const myQueue = new Queue<number>();

// Thêm các phần tử vào hàng đợi
myQueue.enqueue(1);
myQueue.enqueue(2);
myQueue.enqueue(3);

// Lấy ra phần tử ở đầu hàng đợi
console.log(myQueue.dequeue()); // Output: 1

// Xem phần tử ở đầu hàng đợi
console.log(myQueue.peek()); // Output: 2
```

## Bổ sung

- Hàng đợi là một cấu trúc dữ liệu rất quan trọng trong lập trình, được sử dụng trong nhiều thuật toán và cấu trúc dữ
  liệu khác.
- Hàng đợi có thể được triển khai bằng mảng hoặc danh sách liên kết, nhưng việc triển khai bằng danh sách liên kết
  thường hiệu quả hơn, đặc biệt khi cần chèn hoặc xóa các phần tử ở đầu hàng đợi.
