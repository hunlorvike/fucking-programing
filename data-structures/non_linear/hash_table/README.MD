# Bảng Băm (Hash Table)

## Mục lục

1. [Khái niệm](#khái-niệm)
2. [Cách thức hoạt động](#cách-thức-hoạt-động)
    - [Hàm băm](#hàm-băm)
    - [Xung đột (Collision)](#xung-đột-collision)
3. [Ưu điểm và nhược điểm](#ưu-điểm-và-nhược-điểm)
4. [Ví dụ: Bài toán lưu trữ thông tin người dùng](#ví-dụ-bài-toán-lưu-trữ-thông-tin-người-dùng)
5. [Triển khai Bảng băm trong TypeScript](#triển-khai-bảng-băm-trong-typescript)
6. [Ứng dụng của Bảng băm](#ứng-dụng-của-bảng-băm)
7. [Kết luận](#kết-luận)

---

## Khái niệm

Bảng băm (Hash Table) là một cấu trúc dữ liệu sử dụng **hàm băm** để ánh xạ dữ liệu sang các vị trí trong bộ nhớ. Dữ
liệu được lưu trữ dưới dạng các cặp khóa-giá trị (_key-value pairs_).

## Cách thức hoạt động

### Hàm băm

Hàm băm nhận một khóa (_key_) bất kỳ và trả về một giá trị số nguyên (_hash value_), đại diện cho vị trí trong bảng băm
mà khóa đó sẽ được lưu trữ.

### Xung đột (Collision)

Khi hai khóa khác nhau được ánh xạ đến cùng một vị trí trong bảng băm, xảy ra **xung đột**. Các phương pháp giải quyết
xung đột phổ biến gồm:

- **Chaining (Liên kết):** Lưu trữ các khóa có cùng hash value vào một danh sách liên kết tại vị trí đó.
- **Open Addressing (Địa chỉ mở):** Tìm các vị trí tiếp theo trong bảng băm cho đến khi tìm được vị trí trống.

## Ưu điểm và nhược điểm

- **Ưu điểm:**

    - **Truy cập nhanh chóng:** Thao tác tìm kiếm, chèn và xóa trong bảng băm thường có độ phức tạp trung bình là \(O(
      1)\).
    - **Phù hợp với truy cập ngẫu nhiên:** Bảng băm rất hiệu quả cho các thao tác truy cập nhanh dựa vào khóa.

- **Nhược điểm:**
    - **Xung đột:** Xung đột có thể làm giảm hiệu suất của bảng băm.
    - **Không hỗ trợ duyệt tuần tự:** Bảng băm không cung cấp một thứ tự cụ thể cho các phần tử.

## Ví dụ: Bài toán lưu trữ thông tin người dùng

Giả sử muốn lưu trữ thông tin người dùng, với mỗi người dùng được xác định bởi một **ID duy nhất**. Sử dụng bảng băm để
lưu trữ thông tin này:

- **Key:** ID của người dùng.
- **Value:** Thông tin về người dùng (tên, tuổi, địa chỉ...).

## Triển khai Bảng băm trong TypeScript

```typescript
class HashTable<K, V> {
  private size: number;
  private table: Array<[K, V][]>;

  constructor(size: number) {
    this.size = size;
    this.table = new Array(size).fill(null).map(() => []);
  }

  private hash(key: K): number {
    let hash = 0;
    const keyStr = String(key);
    for (let i = 0; i < keyStr.length; i++) {
      hash = (hash << 5) - hash + keyStr.charCodeAt(i);
      hash |= 0; // Chuyển hash thành 32-bit integer
    }
    return Math.abs(hash) % this.size;
  }

  // Thêm cặp key-value vào bảng băm
  put(key: K, value: V): void {
    const index = this.hash(key);
    const bucket = this.table[index];
    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket[i][1] = value;
        return;
      }
    }
    bucket.push([key, value]);
  }

  // Lấy giá trị từ bảng băm
  get(key: K): V | null {
    const index = this.hash(key);
    const bucket = this.table[index];
    for (const [k, v] of bucket) {
      if (k === key) {
        return v;
      }
    }
    return null;
  }

  // Xóa một khóa khỏi bảng băm
  delete(key: K): boolean {
    const index = this.hash(key);
    const bucket = this.table[index];
    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket.splice(i, 1);
        return true;
      }
    }
    return false;
  }
}

// Ví dụ sử dụng
const hashTable = new HashTable<string, any>(10);
hashTable.put('name', 'John');
hashTable.put('age', 30);

console.log(hashTable.get('name')); // Output: "John"
console.log(hashTable.get('age')); // Output: 30

hashTable.delete('name');
console.log(hashTable.get('name')); // Output: null
```

## Ứng dụng của Bảng băm

- **Tìm kiếm nhanh các phần tử:** Bảng băm được sử dụng trong các thuật toán tìm kiếm nhanh, ví dụ: tìm kiếm từ trong
  văn bản, tìm khóa trong tập dữ liệu lớn.
- **Bảng tra cứu:** Xây dựng bảng tra cứu (lookup table) cho các dữ liệu được truy cập thường xuyên, ví dụ: bảng mã hóa,
  bảng giá trị.
- **Bộ nhớ cache:** Quản lý bộ nhớ đệm (cache) cho các dữ liệu thường xuyên truy cập, giúp tăng tốc độ truy xuất.

## Kết luận

Bảng băm là một cấu trúc dữ liệu hiệu quả và được sử dụng rộng rãi trong các ứng dụng cần tìm kiếm nhanh. Nó cung cấp
khả năng truy cập ngẫu nhiên với độ phức tạp trung bình là \(O(1)\), phù hợp với các thao tác như tìm kiếm, chèn và xóa.
