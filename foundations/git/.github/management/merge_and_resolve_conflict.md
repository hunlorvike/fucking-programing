# Quản Lý Merge và Xử Lý Xung Đột trong Git  

Hợp nhất nhánh (merge), xử lý xung đột (resolve conflicts), và tái cấu trúc lịch sử commit (rebase) là các thao tác quan trọng giúp bạn quản lý hiệu quả lịch sử mã nguồn khi làm việc theo nhóm. Dưới đây là hướng dẫn chi tiết về các thao tác này.  

---

## 1. **Hợp Nhất Nhánh (Merge)**  

### a. **Tổng Quan về Merge**  
`git merge` là lệnh dùng để hợp nhất (merge) các thay đổi từ một nhánh khác vào nhánh hiện tại. Merge là cách phổ biến để tích hợp mã nguồn từ các nhánh tính năng (feature branch) về nhánh chính (main hoặc develop).  

### b. **Cách Thực Hiện Merge**  

#### 1. Chuyển Sang Nhánh Đích:  
Trước tiên, chuyển sang nhánh mà bạn muốn hợp nhất các thay đổi.  

```bash  
git checkout <tên nhánh đích>
# Hoặc:
git switch <tên nhánh đích>
```  

#### 2. Thực Hiện Merge:  
Hợp nhất nhánh khác vào nhánh hiện tại bằng cách chỉ định tên nhánh nguồn:  

```bash  
git merge <tên nhánh nguồn>
```  

Ví dụ: Hợp nhất nhánh `feature-branch` vào nhánh `main`:  

```bash  
git checkout main  
git merge feature-branch  
```  

---

### c. **Các Loại Merge**  

#### 1. **Fast-Forward Merge**  
Nếu không có commit nào mới trên nhánh đích, Git sẽ thực hiện fast-forward merge, di chuyển con trỏ `HEAD` để hợp nhất thay đổi.  

```bash  
git merge <tên nhánh nguồn>
```  

#### 2. **Three-Way Merge**  
Nếu nhánh đích và nhánh nguồn đều có commit mới, Git sẽ tạo một commit merge mới để hợp nhất thay đổi.  

---

### d. **Hủy Merge**  
Nếu gặp lỗi hoặc muốn hủy quá trình merge:  

```bash  
git merge --abort
```  

---

## 2. **Xử Lý Xung Đột (Resolve Conflicts)**  

### a. **Xung Đột Khi Merge**  
Xung đột xảy ra khi cùng một phần của file bị chỉnh sửa trên nhiều nhánh. Git sẽ không tự động hợp nhất mà yêu cầu bạn giải quyết xung đột.  

### b. **Cách Xử Lý Xung Đột**  

#### 1. Thông Báo Xung Đột:  
Khi gặp xung đột, Git hiển thị thông báo như:  

```bash  
CONFLICT (content): Merge conflict in <tên file>
Automatic merge failed; fix conflicts and then commit the result.
```  

#### 2. Đánh Dấu Xung Đột:  
Git thêm các đánh dấu trong file bị xung đột:  

```text  
<<<<<<< HEAD  
<Thay đổi trên nhánh hiện tại>  
=======  
<Thay đổi trên nhánh nguồn>  
>>>>>>> <tên nhánh nguồn>  
```  

#### 3. Giải Quyết Xung Đột:  
- Mở file bị xung đột và chỉnh sửa để giữ lại thay đổi phù hợp.  
- Xóa các dòng `<<<<<<<`, `=======`, và `>>>>>>>`.  

#### 4. Đánh Dấu File Đã Giải Quyết:  
Sau khi sửa xung đột, đánh dấu file đã được giải quyết:  

```bash  
git add <tên file>
```  

#### 5. Hoàn Thành Merge:  
Tạo commit mới để hoàn tất merge:  

```bash  
git commit
```  

---

## 3. **Tái Cấu Trúc Lịch Sử Commit (Rebase)**  

### a. **Tổng Quan về Rebase**  
`git rebase` là lệnh giúp tái cấu trúc lịch sử commit bằng cách chuyển các commit từ nhánh hiện tại lên trên đầu nhánh khác.  

---

### b. **Cách Sử Dụng Rebase**  

#### 1. Chuyển Sang Nhánh Cần Rebase:  
```bash  
git checkout <tên nhánh cần rebase>
# Hoặc:
git switch <tên nhánh cần rebase>
```  

#### 2. Thực Hiện Rebase:  
Rebase nhánh hiện tại lên nhánh đích:  

```bash  
git rebase <tên nhánh đích>
```  

Ví dụ: Rebase nhánh `feature-branch` lên `main`:  

```bash  
git checkout feature-branch  
git rebase main  
```  

---

### c. **Giải Quyết Xung Đột Khi Rebase**  
Nếu gặp xung đột trong quá trình rebase, Git sẽ dừng tại commit bị xung đột và yêu cầu bạn giải quyết.  

#### 1. Giải Quyết Xung Đột:  
- Sửa file bị xung đột.  
- Đánh dấu file đã sửa:  

```bash  
git add <tên file>
```  

#### 2. Tiếp Tục Rebase:  
Sau khi giải quyết xung đột, tiếp tục rebase bằng lệnh:  

```bash  
git rebase --continue
```  

#### 3. Hủy Rebase:  
Nếu muốn hủy rebase:  

```bash  
git rebase --abort
```  

---

### d. **Rebase Tương Tác (Interactive Rebase)**  
Interactive Rebase cho phép bạn chỉnh sửa, gộp, hoặc sắp xếp lại thứ tự commit.  

#### 1. Bắt Đầu Interactive Rebase:  
Chỉ định số lượng commit cần rebase:  

```bash  
git rebase -i HEAD~<số lượng commit>
```  

Ví dụ: Rebase 3 commit gần nhất:  

```bash  
git rebase -i HEAD~3
```  

#### 2. Chỉnh Sửa Commit:  
Git mở một trình soạn thảo, nơi bạn có thể:  
- **pick**: Giữ nguyên commit.  
- **edit**: Chỉnh sửa commit.  
- **squash**: Gộp commit vào commit trước đó.  
- **reword**: Chỉnh sửa thông điệp commit.  

---

## 4. **So Sánh Merge và Rebase**

| **Đặc Điểm**       | **Merge**                                           | **Rebase**                                       |
|---------------------|----------------------------------------------------|-------------------------------------------------|
| **Cách Làm Việc**   | Tạo commit merge mới để hợp nhất lịch sử.           | Tái cấu trúc lịch sử, không tạo commit merge.   |
| **Lịch Sử Commit**  | Giữ nguyên lịch sử commit của các nhánh.           | Lịch sử trở nên tuyến tính, gọn gàng hơn.       |
| **Sử Dụng Khi Nào** | Khi làm việc theo nhóm và cần giữ lịch sử đầy đủ.   | Khi làm việc cá nhân và muốn lịch sử gọn gàng. |

---

## 5. **Ví Dụ Thực Tế**

### a. Merge Nhánh Tính Năng:
1. Chuyển sang nhánh `main`:  

```bash  
git checkout main
```  

2. Merge nhánh `feature-branch`:  

```bash  
git merge feature-branch
```  

### b. Rebase Nhánh Tính Năng:
1. Chuyển sang nhánh `feature-branch`:  

```bash  
git checkout feature-branch
```  

2. Rebase nhánh `feature-branch` lên `main`:  

```bash  
git rebase main
```  

### c. Giải Quyết Xung Đột Trong Rebase:
1. Giải quyết xung đột.  
2. Tiếp tục rebase:  

```bash  
git rebase --continue
```  

---

## 6. **Kết Luận**  

Việc quản lý merge, xử lý xung đột, và tái cấu trúc lịch sử với rebase là các kỹ năng quan trọng khi làm việc với Git. Hiểu rõ sự khác biệt giữa merge và rebase, cũng như cách xử lý xung đột hiệu quả, sẽ giúp bạn làm việc nhóm tốt hơn và quản lý mã nguồn dễ dàng hơn.  