# Quản Lý Bảo Mật và Quyền Truy Cập trong GitHub

Quản lý bảo mật và quyền truy cập là một trong những yếu tố quan trọng để bảo vệ mã nguồn và đảm bảo tính toàn vẹn của dự án. Các tính năng như SSH keys, HTTPS, Git Credential Manager, Personal Access Tokens, và bảo vệ nhánh giúp kiểm soát và bảo vệ quyền truy cập vào repository.

---

## 1. **SSH Keys và HTTPS**

### a. **SSH Keys là gì?**

SSH (Secure Shell) Keys là một phương pháp xác thực an toàn được sử dụng để truy cập các repository từ xa như GitHub, GitLab, hay Bitbucket. Thay vì sử dụng tên đăng nhập và mật khẩu, SSH keys sử dụng cặp khóa (private key và public key) để xác thực danh tính của người dùng. 

#### Tạo SSH Keys:
Bạn có thể tạo cặp SSH keys bằng lệnh sau:

```bash
ssh-keygen -t rsa -b 4096 -C "email@example.com"
```

- **`-t rsa`**: Sử dụng thuật toán RSA.
- **`-b 4096`**: Độ dài của khóa là 4096 bit.
- **`-C`**: Email dùng để nhận diện khóa.

#### Thêm SSH Key vào GitHub:
1. Sao chép public key vào clipboard:
   ```bash
   cat ~/.ssh/id_rsa.pub | pbcopy   # MacOS
   cat ~/.ssh/id_rsa.pub | xclip   # Linux
   ```

2. Thêm SSH key vào GitHub:
   - Đăng nhập vào GitHub.
   - Vào **Settings > SSH and GPG Keys > New SSH Key**.
   - Dán public key và lưu lại.

---

### b. **HTTPS là gì?**

HTTPS sử dụng tên đăng nhập và mật khẩu để xác thực khi truy cập repository. Đây là cách đơn giản để làm việc với Git nhưng có thể kém an toàn hơn nếu mật khẩu bị đánh cắp.

#### Sử dụng HTTPS:
Clone repository qua HTTPS:

```bash
git clone https://github.com/<username>/<repository>.git
```

---

## 2. **Quản Lý Mật Khẩu và Token**

### a. **Git Credential Manager**

Git Credential Manager (GCM) giúp lưu trữ và quản lý thông tin xác thực (credentials) của bạn một cách an toàn. Khi được cấu hình, GCM sẽ tự động lưu mật khẩu hoặc token trong trình quản lý mật khẩu của hệ điều hành.

#### Cài đặt Git Credential Manager:
1. Tải và cài đặt GCM: [Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager).
2. Bật GCM trong Git:
   ```bash
   git config --global credential.helper manager
   ```

---

### b. **Personal Access Tokens (PATs)**

PATs là một phương pháp an toàn hơn so với mật khẩu để truy cập các API hoặc repository trên GitHub. Chúng được sử dụng thay cho mật khẩu khi bạn thực hiện các thao tác qua HTTPS.

#### Tạo PAT:
1. Đăng nhập GitHub.
2. Vào **Settings > Developer Settings > Personal Access Tokens > Generate new token**.
3. Chọn phạm vi (scope) quyền truy cập (ví dụ: `repo` để truy cập repository).
4. Copy token và lưu lại (vì bạn không thể xem lại sau khi đóng trang).

#### Sử dụng PAT:
Khi được yêu cầu nhập mật khẩu, thay vào đó hãy dán PAT của bạn.

---

## 3. **Bảo Vệ Nhánh**

### a. **Branch Protection Rules**

Branch protection rules (quy tắc bảo vệ nhánh) trong GitHub giúp bạn kiểm soát việc thay đổi trên các nhánh quan trọng, ví dụ: `main` hoặc `release`. Các quy tắc này có thể yêu cầu review code, kiểm tra CI/CD, hoặc hạn chế quyền merge.

#### Thiết Lập Quy Tắc Bảo Vệ Nhánh:
1. Truy cập repository trên GitHub.
2. Vào **Settings > Branches > Branch Protection Rules**.
3. Nhấp vào **Add Rule** và thiết lập các tùy chọn:
   - **Require pull request reviews**: Yêu cầu một hoặc nhiều người review trước khi merge.
   - **Require status checks to pass before merging**: Yêu cầu các kiểm tra CI/CD phải thành công.
   - **Restrict who can push to matching branches**: Hạn chế người có thể push trực tiếp.

### b. **Bảo Vệ Nhánh Chính (Main/Default)**

Các nhánh chính thường chứa mã nguồn được kiểm thử và ổn định. Việc bảo vệ nhánh giúp:
- Ngăn chặn việc sửa đổi trực tiếp.
- Giảm thiểu lỗi hoặc xung đột trong mã nguồn.

#### Ví dụ Quy Tắc:
- Tên nhánh: `main`.
- Yêu cầu:
  - Ít nhất 2 người phê duyệt pull request.
  - CI/CD phải thành công.
  - Không cho phép force push.

---

## 4. **Ví Dụ Thực Tế**

### a. Cấu hình SSH Keys:
1. Tạo SSH key:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "you@example.com"
   ```
2. Thêm public key vào GitHub và xác nhận kết nối:
   ```bash
   ssh -T git@github.com
   ```

### b. Tạo PAT:
1. Tạo token trên GitHub với quyền `repo`.
2. Dùng token để clone repository qua HTTPS:
   ```bash
   git clone https://github.com/<username>/<repository>.git
   ```

### c. Cấu hình Bảo Vệ Nhánh:
1. Thiết lập quy tắc:
   - Tên nhánh: `main`.
   - Yêu cầu phê duyệt: 1 người review.
2. Push code qua pull request thay vì trực tiếp.

---

## 5. **Kết Luận**

Việc quản lý bảo mật và quyền truy cập là yếu tố quan trọng để đảm bảo tính toàn vẹn và an toàn của mã nguồn. Sử dụng SSH keys, HTTPS, Git Credential Manager, Personal Access Tokens, và branch protection rules sẽ giúp bạn kiểm soát quyền truy cập hiệu quả hơn. Hãy ưu tiên các phương pháp bảo mật mạnh mẽ như SSH và PAT để bảo vệ repository của bạn trong các dự án cá nhân hoặc nhóm.