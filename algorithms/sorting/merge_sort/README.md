# Thuật toán Merge Sort: Sắp xếp trộn

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Cách hoạt động](#cách-hoạt-động)
3. [Mã giả của thuật toán Merge Sort](#mã-giả-của-thuật-toán-merge-sort)
4. [Giải thích](#giải-thích)
5. [Ví dụ](#ví-dụ)
6. [Độ phức tạp](#độ-phức-tạp)
7. [Cải tiến](#cải-tiến)
8. [Lưu ý](#lưu-ý)

---

## Giới thiệu

Thuật toán Merge Sort (hay còn gọi là sắp xếp trộn) là một thuật toán sắp xếp dựa trên kỹ thuật chia để trị (divide and conquer). Thuật toán này chia mảng cần sắp xếp thành hai nửa, sau đó sắp xếp từng nửa và cuối cùng là gộp (merge) chúng lại với nhau. Merge Sort có ưu điểm là ổn định và hiệu quả ngay cả với các mảng lớn, với độ phức tạp thời gian là O(n log n).

## Cách hoạt động

1. **Chia:** Thuật toán bắt đầu bằng việc chia mảng cần sắp xếp thành hai nửa bằng nhau.
2. **Sắp xếp đệ quy:** Tiếp tục chia nhỏ hai nửa đó cho đến khi chỉ còn một phần tử (một phần tử được xem là đã sắp xếp).
3. **Gộp:** Sau đó, gộp hai nửa đã sắp xếp thành một mảng lớn hơn bằng cách so sánh từng phần tử từ hai nửa và đưa phần tử nhỏ hơn vào mảng kết quả.

## Mã giả của thuật toán Merge Sort

```typescript
function mergeSort(arr: number[]): number[] {
  const n = arr.length;

  if (n <= 1) {
    return arr;
  }

  const mid = Math.floor(n / 2);
  const leftHalf = arr.slice(0, mid);
  const rightHalf = arr.slice(mid);

  return merge(mergeSort(leftHalf), mergeSort(rightHalf));
}

function merge(left: number[], right: number[]): number[] {
  let i = 0,
    j = 0,
    result: number[] = [];

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }

  return result.concat(left.slice(i), right.slice(j));
}
```

## Giải thích

- **mergeSort(arr):** Hàm chính của thuật toán Merge Sort, nhận đầu vào là một mảng arr.
- **n = length(arr):** Lấy độ dài của mảng arr.
- **IF n <= 1:** Kiểm tra xem mảng có nhiều hơn một phần tử hay không. Nếu mảng có một phần tử hoặc rỗng, thuật toán sẽ trả về mảng đó.
- **mid = Math.floor(n / 2):** Tìm điểm giữa của mảng.
- **leftHalf = arr.slice(0, mid):** Tạo mảng nửa trái chứa các phần tử từ đầu đến điểm giữa.
- **rightHalf = arr.slice(mid):** Tạo mảng nửa phải chứa các phần tử từ điểm giữa đến cuối.
- **mergeSort(leftHalf):** Đệ quy gọi hàm mergeSort để sắp xếp mảng nửa trái.
- **mergeSort(rightHalf):** Đệ quy gọi hàm mergeSort để sắp xếp mảng nửa phải.
- **merge(left, right):** Gọi hàm merge để gộp hai mảng nửa trái và nửa phải đã được sắp xếp vào mảng kết quả.

- **merge(left, right):** Hàm gộp hai mảng đã sắp xếp vào mảng kết quả.
- **i = j = 0:** Khởi tạo các chỉ số cho hai mảng và mảng kết quả.
- **while i < left.length && j < right.length:** Vòng lặp duyệt qua hai mảng, so sánh từng phần tử và chèn phần tử nhỏ hơn vào mảng kết quả.
- **if left[i] < right[j]:** So sánh phần tử hiện tại của hai mảng. Nếu phần tử ở mảng trái nhỏ hơn, chèn nó vào mảng kết quả.
- **result.push(left[i]):** Chèn phần tử vào mảng kết quả.
- **i++:** Di chuyển chỉ số của mảng trái.
- **else:** Nếu phần tử ở mảng phải nhỏ hơn, chèn nó vào mảng kết quả.
- **result.push(right[j]):** Chèn phần tử vào mảng kết quả.
- **j++:** Di chuyển chỉ số của mảng phải.
- **return result.concat(left.slice(i), right.slice(j)):** Sau khi hết một mảng, nối phần tử còn lại của mảng trái hoặc mảng phải vào mảng kết quả.

## Ví dụ

Giả sử chúng ta có danh sách cần sắp xếp tăng dần: `5, 1, 4, 2, 8`

### Bước 1: Chia mảng thành hai nửa

- Nửa trái: `5, 1`
- Nửa phải: `4, 2, 8`

### Bước 2: Đệ quy gọi mergeSort cho mỗi nửa

- Nửa trái: `1, 5` (đã được sắp xếp)
- Nửa phải: `2, 4, 8` (đã được sắp xếp)

### Bước 3: Gộp hai nửa đã sắp xếp

- So sánh `1` và `2`, chèn `1` vào mảng kết quả.
- So sánh `5` và `2`, chèn `2` vào mảng kết quả.
- So sánh `5` và `4`, chèn `4` vào mảng kết quả.
- So sánh `5` và `8`, chèn `5` vào mảng kết quả.
- Chèn `8` vào mảng kết quả.

**Kết quả:** Danh sách đã được sắp xếp: `1, 2, 4, 5, 8`

## Độ phức tạp

- **Độ phức tạp thời gian:** O(n log n) cho mọi trường hợp.
- **Độ phức tạp không gian:** O(n) (do cần bộ nhớ để lưu trữ các mảng con).

## Cải tiến

- **Sử dụng bộ nhớ bổ sung:** Có thể cải tiến thuật toán bằng cách sử dụng bộ nhớ bổ sung để lưu trữ các mảng con thay vì tạo mảng mới trong mỗi lần đệ quy. Điều này có thể cải thiện hiệu suất của thuật toán, đặc biệt là khi mảng rất lớn.
- **Tối ưu hóa việc gộp:** Có thể tối ưu hóa việc gộp bằng cách sử dụng các kỹ thuật như insertion sort hoặc binary search.

## Lưu ý

- Thuật toán Merge Sort là một thuật toán sắp xếp rất hiệu quả và được sử dụng rộng rãi trong các ứng dụng thực tế.
- Thuật toán này là một thuật toán chia để trị, chia mảng thành các phần nhỏ hơn cho đến khi chỉ còn một phần tử, sau đó gộp chúng lại theo thứ tự.
- Merge Sort là một thuật toán ổn định, nghĩa là thứ tự của các phần tử bằng nhau được giữ nguyên sau khi sắp xếp.
- Thuật toán này sử dụng bộ nhớ bổ sung để lưu trữ các mảng con, điều này có thể là nhược điểm đối với các ứng dụng hạn chế về bộ nhớ.
- Tuy nhiên, độ phức tạp thời gian O(n log n) của thuật toán Merge Sort là rất hiệu quả và khiến nó trở thành một thuật toán được ưa chuộng cho các ứng dụng cần sắp xếp danh sách lớn.
