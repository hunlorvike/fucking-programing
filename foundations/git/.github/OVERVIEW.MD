# Thư Mục .github trong Dự Án

## Mục Lục

1. [Tổng Quan về Thư Mục .github](#1-tổng-quan-về-thư-mục-github)

    - [Khái Niệm](#khái-niệm)
    - [Mục Đích Sử Dụng](#mục-đích-sử-dụng)

2. [Các Thành Phần Chính trong Thư Mục .github](#2-các-thành-phần-chính-trong-thư-mục-github)

    - [Tệp ISSUE_TEMPLATE](#tệp-issue_template)
    - [Tệp PULL_REQUEST_TEMPLATE.md](#tệp-pull_request_templatemd)
    - [Thư Mục Workflows](#thư-mục-workflows)
    - [Tệp CODEOWNERS](#tệp-codeowners)
    - [Tệp CONTRIBUTING.md](#tệp-contributingmd)
    - [Tệp FUNDING.yml](#tệp-fundingyml)

3. [Tùy Chỉnh và Tích Hợp GitHub Actions](#3-tùy-chỉnh-và-tích-hợp-github-actions)

4. [Ưu Điểm và Hạn Chế của Thư Mục .github](#4-ưu-điểm-và-hạn-chế-của-thư-mục-github)

5. [Tóm Tắt](#5-tóm-tắt)

---

### 1. Tổng Quan về Thư Mục .github

#### Khái Niệm

Thư mục `.github` là một thư mục đặc biệt trong các dự án sử dụng GitHub. Đây là nơi chứa các tệp và cấu hình được
GitHub sử dụng để tự động hóa, tổ chức và quản lý các khía cạnh khác nhau của dự án.

Thư mục này không ảnh hưởng đến mã nguồn chính nhưng đóng vai trò quan trọng trong việc tối ưu hóa các quy trình làm
việc (workflow), giao tiếp giữa các thành viên nhóm và cấu hình tài trợ.

#### Mục Đích Sử Dụng

- Tự động hóa quy trình kiểm thử và triển khai với GitHub Actions.
- Chuẩn hóa cách mở **issue** hoặc **pull request**.
- Quản lý trách nhiệm và vai trò trong dự án.
- Tích hợp tài trợ hoặc quy định đóng góp.

---

### 2. Các Thành Phần Chính trong Thư Mục .github

#### Tệp ISSUE_TEMPLATE

**Đường dẫn:** `.github/ISSUE_TEMPLATE/`

- Tệp hoặc thư mục con này chứa các mẫu (template) để hướng dẫn người dùng khi họ mở một **issue** mới.
- **Lợi ích:** Chuẩn hóa cách báo cáo lỗi hoặc yêu cầu tính năng, giúp tiết kiệm thời gian trong quá trình xử lý.

**Ví dụ:**

Tệp `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Báo cáo lỗi
about: Báo cáo lỗi trong dự án
title: "[Lỗi] Tiêu đề lỗi"
labels: bug
assignees: ''
---

### Mô tả lỗi
Mô tả chi tiết lỗi và cách tái hiện nó.

### Môi trường
- Phiên bản: 
- Hệ điều hành:
```

#### Tệp PULL_REQUEST_TEMPLATE.md

**Đường dẫn:** `.github/PULL_REQUEST_TEMPLATE.md`

- Mẫu để hướng dẫn người dùng khi họ tạo một **Pull Request (PR)**.
- **Lợi ích:** Giúp người đóng góp ghi chú các thay đổi và kiểm tra kỹ trước khi gửi PR.

**Ví dụ:**

```markdown
### Mô tả
- [ ] Đã kiểm tra các thay đổi
- [ ] Đã viết/xóa các dòng mã không cần thiết
- [ ] Đã cập nhật tài liệu (nếu cần)

### Liên kết Issue
- Đóng #123
```

#### Thư Mục Workflows

**Đường dẫn:** `.github/workflows/`

- Chứa các tệp YAML để định nghĩa các quy trình tự động hóa bằng GitHub Actions.
- **Lợi ích:** Tự động hóa các quy trình như kiểm thử, triển khai hoặc kiểm tra mã nguồn.

**Ví dụ:** Tệp `.github/workflows/ci.yml`:

```yaml
name: CI Pipeline
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Cài đặt môi trường
        run: npm install
      - name: Kiểm thử
        run: npm test
```

#### Tệp CODEOWNERS

**Đường dẫn:** `.github/CODEOWNERS`

- Chỉ định các thành viên chịu trách nhiệm xem xét mã cho từng phần của dự án.
- **Lợi ích:** Tự động thông báo cho đúng người chịu trách nhiệm khi có thay đổi trong mã.

**Ví dụ:**

```plaintext
# Mọi thay đổi trong thư mục `src/` cần được review bởi @username
/src/ @username
```

#### Tệp CONTRIBUTING.md

**Đường dẫn:** `.github/CONTRIBUTING.md`

- Chứa hướng dẫn chi tiết về cách đóng góp vào dự án.
- **Lợi ích:** Giúp người mới dễ dàng bắt đầu và hiểu các quy tắc trong dự án.

**Ví dụ:**

```markdown
# Hướng dẫn đóng góp

1. Fork dự án và tạo một nhánh mới.
2. Thực hiện các thay đổi cần thiết.
3. Đảm bảo mã của bạn đã được kiểm thử.
4. Gửi một Pull Request với mô tả đầy đủ.
```

#### Tệp FUNDING.yml

**Đường dẫn:** `.github/FUNDING.yml`

- Định cấu hình thông tin tài trợ cho dự án.
- **Lợi ích:** Cho phép hiển thị các kênh tài trợ trên trang chính của dự án.

**Ví dụ:**

```yaml
github: [username]
patreon: [patreon_username]
```

---

### 3. Tùy Chỉnh và Tích Hợp GitHub Actions

GitHub Actions trong thư mục `.github/workflows/` cho phép tự động hóa các quy trình như:

- Kiểm tra mã nguồn khi có **commit** hoặc **pull request**.
- Triển khai ứng dụng lên môi trường thực tế.
- Quét lỗ hổng bảo mật.

**Ví dụ:** Tự động chạy kiểm thử:

```yaml
name: Test Automation
on:
  pull_request:
    branches:
      - main
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Tests
        run: dotnet test
```

---

### 4. Ưu Điểm và Hạn Chế của Thư Mục .github

#### Ưu Điểm

- **Quản Lý Dự Án Chuyên Nghiệp:** Cải thiện giao tiếp giữa các thành viên nhóm.
- **Tự Động Hóa:** Tiết kiệm thời gian thông qua các quy trình tự động.
- **Tăng Tính Minh Bạch:** Chuẩn hóa cách báo cáo lỗi, tạo PR và tài trợ.

#### Hạn Chế

- **Yêu Cầu Cấu Hình Ban Đầu:** Đòi hỏi thời gian thiết lập các tệp và quy trình.
- **Cần Hiểu Biết GitHub Actions:** Để tận dụng hiệu quả các workflows, cần kiến thức về YAML và GitHub.

---

### 5. Tóm Tắt

Thư mục `.github` là công cụ mạnh mẽ để tối ưu hóa quy trình làm việc trên GitHub. Nó giúp tăng tính chuyên nghiệp và
cải thiện hiệu quả của dự án thông qua tự động hóa và chuẩn hóa.

**Các điểm chính:**

1. Cung cấp các tệp như ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE, CODEOWNERS và CONTRIBUTING.md.
2. Hỗ trợ tự động hóa với GitHub Actions trong thư mục `workflows/`.
3. Cho phép tích hợp các phương thức tài trợ thông qua FUNDING.yml.
4. Là công cụ không thể thiếu để quản lý dự án nguồn mở hoặc nhóm.