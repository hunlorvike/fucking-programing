## Tìm tất cả các chuỗi con có tổng bằng một giá trị cho trước

**Tên bài toán:** Find All Subarrays With Given Sum

**Mô tả bài toán:**

Cho một mảng số nguyên `arr` và một số nguyên `k`, hãy tìm tất cả các chuỗi con của `arr` có tổng bằng `k`. Lưu ý rằng các phần tử trong chuỗi con không nhất thiết phải liên tiếp nhau.

**Ví dụ:**

**Input:**

```
arr = [1, 2, 3, 4, 5]
k = 7
```

**Output:**

```
[[2, 5], [1, 3, 3], [1, 2, 4]]
```

**Input:**

```
arr = [1, 2, 3, 4, 5]
k = 9
```

**Output:**

```
[[1, 2, 3, 3], [2, 4, 3], [1, 2, 6]]
```

**Điều kiện ràng buộc:**

- 1 <= arr.length <= 100
- -100 <= arr[i] <= 100
- -1000 <= k <= 1000

**Yêu cầu:**

- Viết một hàm `findSubarrays(arr, k)` trả về một danh sách các chuỗi con có tổng bằng `k`.
- Danh sách kết quả phải là một danh sách các danh sách số nguyên.
- Nếu không tìm thấy chuỗi con nào có tổng bằng `k`, hãy trả về một danh sách rỗng.

**Lưu ý:**

- Có thể có nhiều chuỗi con có tổng bằng `k`.
- Chuỗi con có thể chứa các phần tử lặp lại.
- Trật tự của các chuỗi con trong danh sách kết quả không quan trọng.

**Phân tích:**

Bài toán tìm tất cả các chuỗi con có tổng bằng `k` có thể được giải quyết bằng cách sử dụng hai kỹ thuật phổ biến:

### 1. Backtracking:

Backtracking là một kỹ thuật tìm kiếm giải pháp bằng cách thăm dò từng nhánh của một cây tìm kiếm. Trong bài toán này, mỗi nhánh của cây tìm kiếm đại diện cho một chuỗi con tiềm năng.

Để tìm tất cả các chuỗi con có tổng bằng `k`, ta có thể chia bài toán thành các bài toán con sau:

- **Bài toán lớn:** Tìm các chuỗi con của toàn bộ mảng `arr` sao cho tổng của các phần tử trong chuỗi con bằng `k`.
- **Bài toán con:** Xét từng phần tử của mảng `arr`, ta có 2 lựa chọn:
  1. Chọn phần tử hiện tại (`arr[i]`) và tiếp tục tìm chuỗi con từ các phần tử còn lại sao cho tổng của chuỗi con bằng `k - arr[i]`.
  2. Không chọn phần tử hiện tại và tiếp tục tìm chuỗi con từ các phần tử còn lại sao cho tổng của chuỗi con bằng `k`.

**Ví dụ:**

Cho `arr = [1, 2, 3, 4, 5]` và `k = 7`.

Cây tìm kiếm cho bài toán này sẽ có dạng như sau:

```
            [1, 2, 3, 4, 5]
            / \
           /   \
          /     \
         /       \
        /         \
       1          [2, 3, 4, 5]
      / \          / \
     /   \        /   \
    /     \      /     \
   2       [3, 4, 5]   [3, 4, 5]
  / \     / \       / \
 /   \   /   \     /   \
3      [4, 5]    [4, 5]   [4, 5]
/ \   / \     / \     / \
4    5   4    5   4    5   4    5
```

Bằng cách thăm dò từng nhánh của cây tìm kiếm, ta có thể tìm ra tất cả các chuỗi con có tổng bằng `k = 7`, đó là `[2, 5]` và `[1, 3, 3]`.

**Lưu ý:**

- Thuật toán backtracking có thể tốn nhiều thời gian và bộ nhớ nếu mảng đầu vào có kích thước lớn.

### 2. Sử dụng lập trình động:

Để giải quyết bài toán này bằng cách sử dụng lập trình động, ta có thể sử dụng một bảng (dp) để lưu trữ kết quả của các bài toán con nhỏ hơn, nhằm tránh việc tính toán lại các tập con đã được xử lý trước đó.

**Ý tưởng chính:**

Tạo bảng `dp`: Bảng `dp[i][j]` sẽ lưu giá trị True nếu có thể chọn một chuỗi con từ các phần tử đầu tiên của mảng `arr[0]...arr[i]` sao cho tổng của chuỗi con bằng `j`. Ngược lại, nếu không thể chọn được chuỗi con nào có tổng bằng `j`, ta đặt giá trị là False.

**Công thức truy hồi:**

Nếu không chọn phần tử `arr[i]`, thì tổng `j` có thể đạt được nếu trước đó tổng `j` đã có thể đạt được với các phần tử từ `arr[0]` đến `arr[i-1]` (tức là `dp[i-1][j]`).
Nếu chọn phần tử `arr[i]`, thì tổng `j` có thể đạt được nếu trước đó tổng `j - arr[i]` có thể đạt được với các phần tử từ `arr[0]` đến `arr[i-1]` (tức là `dp[i-1][j-arr[i]]`).

**Công thức:**

```
dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]] (nếu j >= arr[i])
```

**Cách tiếp cận:**

1. Khởi tạo bảng `dp` với kích thước `(n + 1) x (k + 1)` (với `n` là số lượng phần tử trong mảng và `k` là tổng cần đạt được).
2. Sử dụng bảng `dp` để kiểm tra các tổng từ `0` đến `k` cho từng phần tử trong mảng.
3. Sau khi bảng `dp` được tính toán đầy đủ, ta có thể xác định liệu có thể tìm được chuỗi con có tổng bằng `k` hay không.

**Ví dụ về mã (Sử dụng đệ quy và bộ nhớ đệm):**

```python
def findSubarrays(arr, k):
  """
  Tìm tất cả các chuỗi con có tổng bằng k bằng đệ quy và bộ nhớ đệm.

  Args:
    arr: Mảng số nguyên.
    k: Số nguyên.

  Returns:
    Danh sách các chuỗi con có tổng bằng k.
  """
  n = len(arr)
  dp = [[False for _ in range(k + 1)] for _ in range(n + 1)]
  result = []

  def find_subarrays_recursive(index, current_sum, current_subarray):
    if index == n:
      if current_sum == k:
        result.append(current_subarray.copy())
      return

    # Không chọn phần tử hiện tại
    find_subarrays_recursive(index + 1, current_sum, current_subarray)

    # Chọn phần tử hiện tại
    current_subarray.append(arr[index])
    current_sum += arr[index]
    find_subarrays_recursive(index + 1, current_sum, current_subarray)
    current_subarray.pop()
    current_sum -= arr[index]

  find_subarrays_recursive(0, 0, [])
  return result
```

**Lưu ý:**

- Kỹ thuật sử dụng đệ quy và bộ nhớ đệm thường hiệu quả hơn backtracking trong trường hợp mảng đầu vào có kích thước lớn.
- Cả hai phương pháp đều có thể giải quyết bài toán này một cách hiệu quả.
- Chọn phương pháp phù hợp với nhu cầu cụ thể của bạn.
