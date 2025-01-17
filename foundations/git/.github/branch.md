# Tài liệu về Branch trong Git và GitHub

## 1. **Khái niệm về Branch**

Trong Git, **branch** (nhánh) là một tính năng mạnh mẽ cho phép bạn phát triển các tính năng mới, sửa lỗi hoặc thử
nghiệm mà không làm gián đoạn mã nguồn chính. Mỗi branch có thể chứa các commit riêng biệt và khi hoàn thành, bạn có thể
hợp nhất (merge) các thay đổi từ nhánh đó vào nhánh chính (thường là nhánh `main` hoặc `master`).

### 1.1. **Cấu trúc của Branch**

- **Main/Master branch**: Đây là nhánh chính của repository. Mọi thay đổi ổn định và sẵn sàng để triển khai thường được
  hợp nhất vào nhánh này.
- **Feature branch**: Các nhánh con thường được tạo ra để phát triển các tính năng mới hoặc sửa lỗi mà không ảnh hưởng
  đến nhánh chính.
- **Hotfix branch**: Nhánh này được tạo để sửa các lỗi quan trọng hoặc khẩn cấp trong quá trình triển khai.
- **Release branch**: Nhánh này dùng để chuẩn bị cho việc phát hành phiên bản mới, giúp kiểm tra các tính năng và sửa
  lỗi trước khi phát hành chính thức.

## 2. **Các thao tác cơ bản với Branch**

### 2.1. **Tạo Branch mới**

Khi bạn muốn phát triển một tính năng mới hoặc sửa lỗi mà không làm ảnh hưởng đến nhánh chính, bạn cần tạo một nhánh
mới.

- **Tạo nhánh mới và chuyển sang nhánh đó**:

```bash
git checkout -b <branch-name>
```

Lệnh này sẽ tạo một nhánh mới có tên `<branch-name>` và chuyển sang nhánh đó.

- **Tạo nhánh mới mà không chuyển sang**:

```bash
git branch <branch-name>
```

Lệnh này chỉ tạo ra nhánh mới, nhưng không tự động chuyển sang nhánh đó.

### 2.2. **Chuyển giữa các Branch**

Khi bạn đã tạo nhiều nhánh, bạn có thể chuyển đổi giữa các nhánh để làm việc.

- **Chuyển sang nhánh khác**:

```bash
git checkout <branch-name>
```

Lệnh này giúp bạn chuyển từ nhánh hiện tại sang nhánh có tên `<branch-name>`.

- **Danh sách tất cả các nhánh trong repository**:

```bash
git branch
```

Lệnh này liệt kê tất cả các nhánh trong repository và đánh dấu nhánh hiện tại bằng dấu sao (\*).

### 2.3. **Hợp nhất (Merge) Branch**

Khi bạn đã hoàn thành công việc trên nhánh con (feature branch hoặc hotfix branch), bạn có thể hợp nhất các thay đổi đó
vào nhánh chính (main/master).

- **Chuyển sang nhánh chính (main) trước**:

```bash
git checkout main
```

- **Hợp nhất nhánh con vào nhánh chính**:

```bash
git merge <branch-name>
```

Lệnh này sẽ hợp nhất nhánh `<branch-name>` vào nhánh chính (hoặc nhánh hiện tại mà bạn đang đứng).

### 2.4. **Xóa Branch**

Khi một nhánh không còn cần thiết (ví dụ: sau khi đã hợp nhất vào nhánh chính), bạn có thể xóa nhánh đó để dọn dẹp
repository.

- **Xóa nhánh cục bộ (local branch)**:

```bash
git branch -d <branch-name>
```

Lệnh này sẽ xóa nhánh `<branch-name>` sau khi đảm bảo rằng nhánh đó đã được hợp nhất vào nhánh chính. Nếu bạn muốn xóa
một nhánh mà không kiểm tra việc hợp nhất, dùng `-D` thay vì `-d`.

- **Xóa nhánh từ GitHub (remote branch)**:

```bash
git push origin --delete <branch-name>
```

Lệnh này sẽ xóa nhánh `<branch-name>` khỏi repository trên GitHub.

### 2.5. **Push Branch lên GitHub**

Khi bạn tạo một nhánh mới và muốn chia sẻ nó với những người khác, bạn có thể push nhánh đó lên GitHub.

- **Push nhánh mới lên GitHub**:

```bash
git push origin <branch-name>
```

Lệnh này sẽ đẩy nhánh `<branch-name>` lên GitHub.

### 2.6. **Pull Branch từ GitHub**

Khi bạn làm việc trong nhóm và muốn kéo những thay đổi từ GitHub về, bạn có thể pull nhánh mới từ GitHub.

- **Pull nhánh từ GitHub**:

```bash
git pull origin <branch-name>
```

Lệnh này sẽ kéo nhánh `<branch-name>` từ GitHub về và hợp nhất với nhánh hiện tại trên máy tính của bạn.

## 3. **Best Practices khi sử dụng Branch**

### 3.1. **Sử dụng nhánh cho các tính năng và sửa lỗi**

Khi phát triển phần mềm, bạn nên tạo nhánh cho mỗi tính năng mới hoặc mỗi lần sửa lỗi. Điều này giúp mã nguồn của bạn
luôn sạch sẽ và dễ dàng theo dõi.

- **Tạo nhánh cho mỗi tính năng mới**: Tạo một nhánh mới cho mỗi tính năng bạn đang phát triển.
  ```bash
  git checkout -b feature/login-form
  ```
- **Tạo nhánh cho mỗi sửa lỗi**: Khi phát hiện lỗi, bạn nên tạo một nhánh hotfix.
  ```bash
  git checkout -b hotfix/fix-login-bug
  ```

### 3.2. **Đặt tên nhánh rõ ràng**

Tên nhánh nên mô tả rõ mục đích của nhánh đó, giúp nhóm phát triển dễ dàng hiểu được nội dung mà nhánh đó chứa đựng.

Ví dụ:

- **Feature branch**: `feature/user-authentication`
- **Bugfix branch**: `bugfix/fix-header-issue`
- **Release branch**: `release/v1.2.0`

### 3.3. **Merge đúng cách**

Khi thực hiện merge, luôn kiểm tra kỹ các thay đổi để tránh xung đột và đảm bảo rằng không có lỗi phát sinh. Nếu có xung
đột, Git sẽ yêu cầu bạn giải quyết xung đột trước khi tiếp tục merge.

### 3.4. **Không làm việc trên nhánh chính (main/master)**

Tránh việc phát triển trực tiếp trên nhánh chính (main). Luôn tạo nhánh riêng cho từng tính năng hoặc sửa lỗi để bảo vệ
nhánh chính và dễ dàng quản lý mã nguồn.

## 4. **Xử lý Conflicts trong Branch**

Khi hai nhánh có các thay đổi đối kháng trên cùng một tệp hoặc phần mã, Git sẽ không thể tự động hợp nhất các thay đổi
và sẽ thông báo có **conflict**. Bạn sẽ cần phải giải quyết xung đột này thủ công.

### 4.1. **Giải quyết Conflicts**

Khi gặp conflict, Git sẽ đánh dấu các đoạn mã có xung đột trong tệp và yêu cầu bạn chọn cách giải quyết. Sau khi giải
quyết xung đột, bạn cần thực hiện commit để hoàn thành việc hợp nhất.

1. Mở tệp có xung đột.
2. Tìm các đoạn mã được đánh dấu bởi Git.
3. Chọn hoặc chỉnh sửa mã theo cách mà bạn muốn.
4. Sau khi giải quyết xung đột, add và commit các thay đổi:

```bash
git add <file-name>
git commit
```

## 5. **Branch trong GitHub và Pull Requests**

### 5.1. **Pull Request**

Pull Request (PR) là cách để bạn gửi các thay đổi từ nhánh của mình tới nhánh chính của repository trên GitHub để người
khác xem xét và hợp nhất.

- **Tạo Pull Request**: Sau khi bạn đã push nhánh của mình lên GitHub, bạn có thể tạo một PR để gửi nhánh đó vào nhánh
  chính của dự án.
- **Review PR**: Người quản lý dự án sẽ kiểm tra mã của bạn, đưa ra phản hồi và cuối cùng hợp nhất PR nếu mọi thứ ổn.

### 5.2. **Phân quyền và Review Pull Requests**

GitHub cung cấp tính năng phân quyền cho phép người quản lý repository mời những người cụ thể vào để review và hợp nhất
các PR, đảm bảo chất lượng mã nguồn.

## 6. **Tổng kết**

Branch trong Git và GitHub là công cụ mạnh mẽ giúp bạn phát triển, thử nghiệm và sửa lỗi mà không làm gián đoạn mã nguồn
chính. Việc sử dụng branch một cách hiệu quả giúp bạn và nhóm phát triển phần mềm có thể hợp tác dễ dàng và quản lý mã
nguồn tốt hơn. Hy vọng tài liệu này giúp bạn hiểu rõ hơn về branch và cách sử dụng nó!
