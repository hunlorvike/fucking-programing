# Tập Hợp (Set)

## Mục lục

1. [Đặc điểm](#đặc-điểm)
2. [Ưu điểm và nhược điểm](#ưu-điểm-và-nhược-điểm)
3. [Ứng dụng](#ứng-dụng)
4. [Ví dụ triển khai tập hợp trong TypeScript](#ví-dụ-triển-khai-tập-hợp-trong-typescript)
5. [Bổ sung](#bổ-sung)

---

## Đặc điểm

- Là một cấu trúc dữ liệu phi tuyến tính, các phần tử không được sắp xếp theo một thứ tự cố định.
- **Không cho phép phần tử trùng lặp** - mỗi phần tử chỉ xuất hiện một lần trong tập hợp.
- Hỗ trợ nhiều thao tác tập hợp, ví dụ:
  - **Hợp (Union):** Kết hợp các phần tử của hai tập hợp.
  - **Giao (Intersection):** Tìm các phần tử chung của hai tập hợp.
  - **Hiệu (Difference):** Tìm các phần tử chỉ có trong tập hợp đầu tiên mà không có trong tập hợp thứ hai.
  - **Kiểm tra thuộc tính (Membership):** Kiểm tra xem một phần tử có tồn tại trong tập hợp hay không.

## Ưu điểm và nhược điểm

- **Ưu điểm:**

  - **Thao tác tập hợp nhanh:** Các thao tác như hợp, giao, hiệu, kiểm tra thuộc tính thường có độ phức tạp \(O(1)\).
  - **Loại bỏ trùng lặp:** Tập hợp tự động loại bỏ các phần tử trùng lặp, giúp đảm bảo tính duy nhất.

- **Nhược điểm:**
  - **Không có thứ tự:** Các phần tử trong tập hợp không có thứ tự rõ ràng.
  - **Khó duyệt:** Việc duyệt qua tất cả các phần tử có thể kém hiệu quả nếu tập hợp lớn.

## Ứng dụng

- **Lý thuyết tập hợp:** Tìm giao, hiệu của hai tập hợp các số, từ.
- **Loại bỏ trùng lặp:** Dùng để loại bỏ phần tử trùng lặp, ví dụ như danh sách từ, email.
- **Kiểm tra thuộc tính:** Xác minh sự tồn tại của một phần tử trong tập hợp, như kiểm tra từ điển, dữ liệu người dùng.

## Ví dụ triển khai tập hợp trong TypeScript

```typescript
class SetCollection<T> {
  private items: Set<T>;

  constructor(initialItems?: T[]) {
    this.items = new Set(initialItems);
  }

  // Thêm một phần tử vào tập hợp
  add(element: T): void {
    this.items.add(element);
  }

  // Kiểm tra thuộc tính
  has(element: T): boolean {
    return this.items.has(element);
  }

  // Hợp của hai tập hợp
  union(otherSet: SetCollection<T>): SetCollection<T> {
    const unionSet = new SetCollection<T>();
    this.items.forEach(item => unionSet.add(item));
    otherSet.items.forEach(item => unionSet.add(item));
    return unionSet;
  }

  // Giao của hai tập hợp
  intersection(otherSet: SetCollection<T>): SetCollection<T> {
    const intersectionSet = new SetCollection<T>();
    this.items.forEach(item => {
      if (otherSet.has(item)) {
        intersectionSet.add(item);
      }
    });
    return intersectionSet;
  }

  // Hiệu của hai tập hợp
  difference(otherSet: SetCollection<T>): SetCollection<T> {
    const differenceSet = new SetCollection<T>();
    this.items.forEach(item => {
      if (!otherSet.has(item)) {
        differenceSet.add(item);
      }
    });
    return differenceSet;
  }

  // Hiển thị tập hợp
  display(): void {
    console.log(Array.from(this.items));
  }
}

// Sử dụng ví dụ
const setA = new SetCollection<number>([1, 2, 3, 4, 5]);
const setB = new SetCollection<number>([4, 5, 6, 7, 8]);

// Hợp của hai tập hợp
const unionSet = setA.union(setB);
unionSet.display(); // Output: [1, 2, 3, 4, 5, 6, 7, 8]

// Giao của hai tập hợp
const intersectionSet = setA.intersection(setB);
intersectionSet.display(); // Output: [4, 5]

// Hiệu của hai tập hợp
const differenceSet = setA.difference(setB);
differenceSet.display(); // Output: [1, 2, 3]
```

## Bổ sung

Tập hợp là một cấu trúc dữ liệu rất hữu ích cho các thao tác liên quan đến lý thuyết tập hợp. Trong TypeScript, chúng ta có thể sử dụng lớp `Set` để triển khai các thao tác như `add`, `has`, `union`, `intersection`, và `difference`.
