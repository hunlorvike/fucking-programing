# Tài liệu về Repository trong GitHub

## 1. **Khái niệm về Repository**

Trong GitHub, **repository (repo)** là nơi chứa tất cả các tệp tin và lịch sử thay đổi (commit history) của dự án phần
mềm. Một repository có thể chứa mã nguồn, tài liệu, hình ảnh, và bất kỳ tệp nào liên quan đến dự án. Nó cũng giúp quản
lý các thay đổi của dự án theo thời gian.

Repository có thể được phân loại thành hai loại:

- **Public repositories**: Mọi người có thể xem và đóng góp vào dự án.
- **Private repositories**: Chỉ những người được cấp quyền mới có thể truy cập và đóng góp.

## 2. **Cấu trúc của một Repository**

Một repository trong GitHub thường có các thành phần sau:

- **Code (Mã nguồn)**: Đây là các tệp tin mã nguồn của dự án.
- **README file**: Tệp README thường được dùng để giải thích về dự án, cách cài đặt, sử dụng và đóng góp vào dự án. Nó
  thường được viết bằng Markdown.
- **Branches (Nhánh)**: Dùng để phát triển các tính năng mới, sửa lỗi, hoặc thử nghiệm mà không ảnh hưởng đến mã nguồn
  chính (main branch).
- **Issues**: Đây là phần giúp theo dõi lỗi (bug), yêu cầu tính năng mới hoặc công việc cần làm.
- **Pull requests**: Là cách để đóng góp mã vào repository. Một pull request giúp người khác kiểm tra mã nguồn bạn đã
  thay đổi trước khi hợp nhất nó vào nhánh chính.
- **Actions (GitHub Actions)**: Dùng để tự động hóa quy trình làm việc, như chạy kiểm tra mã nguồn, triển khai phần mềm,
  v.v.
- **Wiki**: Một tài liệu giúp giải thích chi tiết hơn về dự án hoặc quy trình phát triển.

## 3. **Các thao tác cơ bản với Repository**

### 3.1. **Tạo Repository mới**

Để tạo một repository mới trên GitHub, bạn cần:

1. Đăng nhập vào GitHub.
2. Click vào nút "New" (hoặc "Create new repository") ở trang chính.
3. Điền tên cho repository, chọn chế độ public hoặc private.
4. Có thể thêm tệp README hoặc chọn không.
5. Click "Create repository".

### 3.2. **Clone Repository về máy tính**

Để làm việc với mã nguồn trong repository, bạn có thể "clone" repository về máy tính cá nhân bằng cách sử dụng Git.

```bash
git clone https://github.com/username/repository-name.git
```

Lệnh này sao chép toàn bộ mã nguồn và lịch sử thay đổi từ GitHub về máy tính của bạn.

### 3.3. **Commit và Push thay đổi**

- **Commit**: Lưu lại các thay đổi trong repository, kèm theo thông tin mô tả về những thay đổi đó.

```bash
git add .
git commit -m "Mô tả về thay đổi"
```

- **Push**: Đẩy các thay đổi từ máy tính của bạn lên GitHub.

```bash
git push origin main
```

### 3.4. **Branch và Merge**

- **Branch**: Tạo nhánh mới để phát triển tính năng mà không làm ảnh hưởng đến nhánh chính (main branch).

```bash
git checkout -b new-feature
```

- **Merge**: Khi bạn đã hoàn tất thay đổi trên nhánh mới, bạn cần hợp nhất (merge) nó vào nhánh chính.

```bash
git checkout main
git merge new-feature
```

### 3.5. **Tạo Pull Request**

Pull request (PR) là cách để bạn đề xuất các thay đổi của mình vào nhánh chính hoặc nhánh khác trong repository. Để tạo
một PR:

1. Push nhánh của bạn lên GitHub.
2. Vào GitHub, chuyển đến repository và tạo Pull Request.
3. Chọn nhánh cần hợp nhất và nhánh đích (như `main`).
4. Mô tả các thay đổi trong Pull Request và gửi để người khác xem xét.

## 4. **Quản lý Issues**

Issues giúp bạn theo dõi các vấn đề trong dự án:

- **Mở issue**: Khi phát hiện một lỗi hoặc muốn yêu cầu tính năng mới.
- **Label**: Gắn nhãn để phân loại vấn đề.
- **Assignee**: Gán người phụ trách vấn đề.
- **Milestones**: Gắn vấn đề với một cột mốc hoặc phiên bản phát hành cụ thể.

## 5. **Collaborating (Hợp tác)**

GitHub hỗ trợ làm việc nhóm hiệu quả với tính năng quản lý quyền và review:

- **Collaborators**: Người được mời vào repository có thể truy cập và đóng góp.
- **Fork**: Khi bạn muốn sao chép repository của người khác để phát triển độc lập, sau đó gửi pull request để hợp nhất
  các thay đổi.
- **Review Pull Request**: Người quản lý repository có thể xem và duyệt các pull request trước khi hợp nhất chúng.

## 6. **GitHub Actions (Tự động hóa)**

GitHub Actions giúp tự động hóa các quy trình như kiểm tra mã, triển khai dự án, v.v. Các tác vụ này được cấu hình trong
tệp `.yml` nằm trong thư mục `.github/workflows`.

## 7. **Các mẹo và best practices**

- **Sử dụng .gitignore**: Đảm bảo không đưa vào repository các tệp không cần thiết (như tệp cấu hình cá nhân, thư mục
  build).
- **Cập nhật README**: Đảm bảo README luôn được cập nhật với hướng dẫn sử dụng và đóng góp vào dự án.
- **Sử dụng issues và pull requests hiệu quả**: Giúp theo dõi công việc và phối hợp trong nhóm tốt hơn.

## 8. **Tổng kết**

Repository trong GitHub là công cụ quan trọng giúp các lập trình viên và nhóm phát triển phần mềm quản lý mã nguồn, theo
dõi thay đổi, và hợp tác dễ dàng hơn. Hiểu rõ và sử dụng thành thạo các tính năng như commit, branch, pull request, và
issues giúp dự án của bạn phát triển mượt mà và hiệu quả.
