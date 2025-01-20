# Hoàn Tác Thay Đổi trong Git (Reset, Checkout, Revert, Restore)

Git cung cấp nhiều cách để hoàn tác các thay đổi, cho phép bạn kiểm soát lịch sử commit và trạng thái mã nguồn một cách
hiệu quả. Tài liệu này giải thích các lệnh như `git reset`, `git checkout`, `git revert`, và `git restore`, cùng với các
tình huống sử dụng phù hợp.

---

## 1. **Hoàn Tác Thay Đổi Chưa Commit**

### a. **Hủy Thay Đổi trong Working Directory (Restore)**:

Nếu bạn chỉnh sửa file nhưng muốn khôi phục lại trạng thái ban đầu từ bản copy trong **index (staging area)** hoặc *
*HEAD**, sử dụng lệnh:

```bash
git restore <tên file>
```

Khôi phục toàn bộ thư mục:

```bash
git restore .
```

**Lưu ý**: Thao tác này sẽ xóa các thay đổi chưa được staged và không thể khôi phục.

---

### b. **Hủy Thay Đổi đã Staged**:

Nếu bạn đã staged thay đổi nhưng chưa commit, sử dụng lệnh:

```bash
git restore --staged <tên file>
```

Hoặc để unstaged tất cả các thay đổi:

```bash
git restore --staged .
```

---

### c. **Hủy Thay Đổi với Checkout (Cũ)**:

Lệnh `git checkout` cũng có thể được dùng để khôi phục file, nhưng đây là cách làm **không khuyến khích** từ Git 2.23
trở đi. Thay vào đó, sử dụng `git restore`.

```bash
git checkout -- <tên file>
```

---

## 2. **Hoàn Tác Commit Gần Nhất**

### a. **Thay Đổi Nội Dung Commit Cuối Cùng (Amend)**:

Nếu bạn muốn chỉnh sửa commit cuối mà không tạo commit mới, sử dụng:

```bash
git commit --amend
```

Ví dụ: Chỉnh sửa message commit:

```bash
git commit --amend -m "Thông điệp commit mới"
```

---

### b. **Hoàn Tác Commit Nhưng Giữ Thay Đổi trong Staging Area**:

Sử dụng `git reset --soft` để quay lại trạng thái trước commit gần nhất nhưng giữ nguyên thay đổi trong staged:

```bash
git reset --soft HEAD~1
```

---

### c. **Hoàn Tác Commit và Bỏ Staged Thay Đổi**:

Sử dụng `git reset --mixed` để hoàn tác commit và đưa thay đổi trở lại working directory:

```bash
git reset --mixed HEAD~1
```

---

### d. **Hoàn Tác Commit và Xóa Thay Đổi**:

Nếu bạn muốn hoàn toàn xóa bỏ thay đổi của commit gần nhất, sử dụng `git reset --hard`:

```bash
git reset --hard HEAD~1
```

**Lưu ý**: Thay đổi sẽ bị mất và không thể khôi phục.

---

## 3. **Hoàn Tác Commit Đã Push Lên Remote**

### a. **Sử dụng Revert**:

Để hoàn tác một commit mà không thay đổi lịch sử commit (an toàn cho remote repository), sử dụng `git revert`:

```bash
git revert <hash commit>
```

Git sẽ tạo một commit mới để đảo ngược các thay đổi của commit được chỉ định.

---

### b. **Sửa Lịch Sử Commit với Reset (Cẩn Thận)**:

Nếu commit đã được push nhưng cần thay đổi, sử dụng `reset` kết hợp với `--force`. **Điều này không được khuyến khích
nếu các thành viên khác đang làm việc trên cùng repository**.

```bash
git reset --hard <hash commit>
git push --force
```

---

## 4. **Hủy Toàn Bộ Thay Đổi**

### a. **Reset Repository Về Trạng Thái Ban Đầu**:

Nếu bạn muốn xóa toàn bộ thay đổi và khôi phục repository về một trạng thái cụ thể:

```bash
git reset --hard <hash commit>
```

---

### b. **Khôi Phục từ Remote Repository**:

Nếu bạn muốn đồng bộ lại với remote repository, bỏ qua mọi thay đổi cục bộ:

```bash
git fetch origin
git reset --hard origin/<tên nhánh>
```

---

## 5. **Hoàn Tác trên Một File Cụ Thể**

### a. **Khôi Phục File từ Commit Cụ Thể**:

Nếu bạn muốn khôi phục một file từ một commit cũ:

```bash
git checkout <hash commit> -- <tên file>
```

Hoặc:

```bash
git restore --source=<hash commit> <tên file>
```

### b. **Khôi Phục File từ Remote Repository**:

Nếu bạn muốn khôi phục file từ remote repository (bỏ qua thay đổi cục bộ):

```bash
git fetch origin
git checkout origin/<tên nhánh> -- <tên file>
```

---

## 6. **So Sánh Reset, Checkout, Revert, Restore**

| **Lệnh**       | **Mục Đích**                                                               | **Thay Đổi Lịch Sử Commit?** | **Mất Dữ Liệu?**           |
|----------------|----------------------------------------------------------------------------|------------------------------|----------------------------|
| `git reset`    | Hoàn tác commit hoặc staged changes, có thể giữ hoặc xóa working directory | Có                           | Có (với `--hard`)          |
| `git checkout` | Chuyển nhánh, khôi phục file (cũ)                                          | Không                        | Có (trên file chưa commit) |
| `git revert`   | Tạo commit mới để hoàn tác thay đổi từ commit trước đó                     | Không                        | Không                      |
| `git restore`  | Khôi phục file hoặc staged changes (mới)                                   | Không                        | Có (với working directory) |

---

## 7. **Ví Dụ Thực Tế**

### a. Quay Lại Trạng Thái Ban Đầu:

Bạn chỉnh sửa mã nhưng muốn quay lại trạng thái sạch (trước thay đổi):

```bash
git restore .
```

### b. Hoàn Tác Commit Gần Nhất:

Nếu bạn vừa commit nhầm nhưng chưa push:

```bash
git reset --soft HEAD~1
```

### c. Đảo Ngược Một Commit Đã Push:

Nếu commit gây lỗi đã được push, bạn có thể sửa bằng `revert`:

```bash
git revert <hash commit>
git push
```

### d. Khôi Phục File Cụ Thể:

Nếu chỉ muốn khôi phục file `index.html` về trạng thái trong commit trước:

```bash
git restore index.html
```

---

## 8. **Kết Luận**

Hiểu rõ cách hoàn tác thay đổi là một kỹ năng quan trọng khi làm việc với Git. Tùy thuộc vào tình huống, bạn có thể chọn
`reset`, `checkout`, `revert`, hoặc `restore` để xử lý thay đổi một cách an toàn và hiệu quả. Hãy cẩn thận khi sử dụng
các lệnh như `reset --hard` để tránh mất dữ liệu không mong muốn.