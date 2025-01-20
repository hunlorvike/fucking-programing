# Quản Lý Stash trong Git và GitHub

Stash là một tính năng trong Git cho phép bạn lưu trữ tạm thời các thay đổi trong working directory mà không cần commit
chúng. Tính năng này hữu ích khi bạn muốn chuyển sang một nhánh khác hoặc làm việc trên một nhiệm vụ mới mà không làm
mất đi các thay đổi chưa hoàn thành.

---

## 1. **Tổng Quan về Stash**

### a. Stash Là Gì?

Stash tạo một "ngăn tạm" để lưu trữ các thay đổi chưa được commit. Nó bao gồm:

- Các thay đổi trong tracked files.
- Thay đổi trong staged files.

**Lưu ý**: Thay đổi trong untracked files hoặc ignored files không được lưu trữ mặc định.

---

## 2. **Các Lệnh Cơ Bản với Stash**

### a. **Lưu Trữ Thay Đổi với Stash**:

Sử dụng lệnh `git stash` để lưu các thay đổi chưa commit.

```bash
git stash
```

Bạn cũng có thể thêm mô tả cho stash:

```bash
git stash save "Mô tả thay đổi"
```

Nếu muốn lưu cả untracked files, sử dụng tùy chọn `-u` hoặc `--include-untracked`:

```bash
git stash -u
```

---

### b. **Xem Danh Sách Stash**:

Liệt kê tất cả các stash hiện có trong repository:

```bash
git stash list
```

Kết quả sẽ hiển thị danh sách các stash, bao gồm tên (vd: `stash@{0}`) và mô tả.

---

### c. **Áp Dụng Stash**:

Để áp dụng các thay đổi từ stash vào working directory, sử dụng lệnh:

```bash
git stash apply
```

Bạn cũng có thể áp dụng một stash cụ thể bằng cách chỉ định tên:

```bash
git stash apply stash@{0}
```

Nếu bạn muốn áp dụng và xóa stash sau đó, sử dụng:

```bash
git stash pop
```

---

### d. **Xóa Stash**:

Xóa stash sau khi không còn cần thiết:

- Xóa stash đầu tiên (stash@{0}):

```bash
git stash drop
```

- Xóa một stash cụ thể:

```bash
git stash drop stash@{<index>}
```

- Xóa tất cả các stash:

```bash
git stash clear
```

---

## 3. **Stash và Branches**

### a. **Tạo Branch từ Stash**:

Nếu bạn muốn tạo một nhánh mới dựa trên các thay đổi được lưu trữ trong stash, sử dụng lệnh:

```bash
git stash branch <tên nhánh>
```

Ví dụ:

```bash
git stash branch feature-branch
```

Lệnh này sẽ:

1. Tạo một nhánh mới.
2. Áp dụng các thay đổi từ stash vào nhánh mới.
3. Xóa stash sau khi áp dụng thành công.

---

## 4. **Stash Nâng Cao**

### a. **Kiểm Tra Nội Dung Stash**:

Xem chi tiết nội dung của một stash cụ thể:

```bash
git stash show stash@{0}
```

Để xem đầy đủ các thay đổi:

```bash
git stash show -p stash@{0}
```

---

### b. **Stash Chỉ Một File Cụ Thể**:

Bạn có thể stash một file cụ thể thay vì toàn bộ repository bằng cách sử dụng:

```bash
git stash push -m "Mô tả" <tên file>
```

Ví dụ:

```bash
git stash push -m "Lưu thay đổi file index.html" index.html
```

---

### c. **Stash với GitHub**:

Stash là tính năng cục bộ trong Git. Khi làm việc với GitHub:

- Bạn cần áp dụng stash vào repository local (`git stash apply` hoặc `git stash pop`) trước khi commit và push lên
  remote repository.
- Stash không được đồng bộ trực tiếp với GitHub.

---

## 5. **Các Lệnh Hữu Ích Khác**

- **Áp dụng stash nhưng giữ nguyên trong danh sách stash**:

```bash
git stash apply stash@{0}
```

- **Chỉ stash staged files**:

```bash
git stash --keep-index
```

- **Stash một phần thay đổi**:
  Nếu chỉ muốn stash một phần thay đổi, sử dụng interactive mode với `git add -p`, sau đó stash các thay đổi đã được
  staged:

```bash
git add -p
git stash
```

---

## 6. **Ví Dụ Thực Tế**

### a. Chuyển Nhánh Khi Có Thay Đổi Chưa Commit:

1. Lưu các thay đổi chưa commit:

```bash
git stash
```

2. Chuyển sang nhánh khác:

```bash
git checkout <tên nhánh>
```

3. Áp dụng lại thay đổi:

```bash
git stash pop
```

### b. Làm Việc với Nhiều Stash:

1. Tạo nhiều stash với các thay đổi khác nhau:

```bash
git stash save "Thay đổi cho task 1"
git stash save "Thay đổi cho task 2"
```

2. Liệt kê các stash:

```bash
git stash list
```

3. Áp dụng một stash cụ thể:

```bash
git stash apply stash@{1}
```

---

## 7. **Kết Luận**

Stash là một công cụ mạnh mẽ giúp bạn quản lý các thay đổi tạm thời mà không cần commit. Hiểu và sử dụng thành thạo các
lệnh stash sẽ giúp bạn làm việc linh hoạt hơn, tránh mất mát dữ liệu và tăng năng suất làm việc.
