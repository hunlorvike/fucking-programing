# Git Hooks: Tự Động Hóa Quy Trình Phát Triển Phần Mềm

Git Hooks là các script mà Git thực thi trong một số sự kiện đặc biệt trong quá trình làm việc với Git, như trước khi commit, sau khi commit, trước khi push, v.v. Việc sử dụng Git hooks giúp tự động hóa các tác vụ, đảm bảo rằng mã nguồn luôn tuân thủ các quy chuẩn nhất định và cải thiện quy trình làm việc.

---

## 1. **Khái Niệm về Git Hooks**

Git hooks là các script được Git tự động gọi vào các thời điểm nhất định trong quá trình sử dụng hệ thống kiểm soát phiên bản Git. Các hook này có thể được sử dụng để thực hiện các tác vụ như kiểm tra mã nguồn, chạy tests, hoặc thực hiện các hành động khác khi có sự kiện xảy ra, chẳng hạn như khi commit, push hoặc merge.

Git hỗ trợ các hook qua các file script nằm trong thư mục `.git/hooks` của mỗi repository. Những file này có thể được cấu hình để thực thi tự động các tác vụ khi một sự kiện cụ thể xảy ra.

---

## 2. **Các Hook Thường Dùng**

### a. **Pre-commit Hook**

Pre-commit hook được gọi ngay trước khi commit được thực hiện. Đây là thời điểm lý tưởng để kiểm tra mã nguồn trước khi ghi vào lịch sử của Git. Bạn có thể sử dụng pre-commit hook để:
- Kiểm tra cú pháp mã nguồn.
- Chạy các kiểm tra tự động (linter).
- Đảm bảo mã nguồn không chứa lỗi hoặc vi phạm các quy chuẩn (style guide).

#### Cấu hình Pre-commit Hook:
1. Mở thư mục `.git/hooks`.
2. Tạo hoặc chỉnh sửa file `pre-commit`.
3. Thêm script kiểm tra, ví dụ, kiểm tra cú pháp Python:
   ```bash
   #!/bin/sh
   python -m py_compile $(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
   if [ $? -ne 0 ]; then
       echo "Python syntax errors found, commit aborted."
       exit 1
   fi
   ```

### b. **Post-commit Hook**

Post-commit hook được gọi ngay sau khi commit thành công. Đây là thời điểm thích hợp để thực hiện các tác vụ liên quan đến thông báo hoặc các tác vụ khác mà không ảnh hưởng đến commit của bạn. Một số tác vụ có thể thực hiện là:
- Gửi thông báo về commit mới.
- Cập nhật hệ thống theo dõi hoặc công cụ quản lý dự án.

#### Cấu hình Post-commit Hook:
1. Mở thư mục `.git/hooks`.
2. Tạo hoặc chỉnh sửa file `post-commit`.
3. Thêm các lệnh thực thi sau commit, ví dụ, gửi thông báo:
   ```bash
   #!/bin/sh
   echo "Commit successful! Notify the team..."
   ```

### c. **Pre-push Hook**

Pre-push hook được gọi ngay trước khi push code lên remote repository. Hook này giúp bạn kiểm tra các yếu tố cần thiết trước khi dữ liệu được đẩy lên server. Đây là một nơi tốt để:
- Chạy các bài kiểm tra (tests).
- Kiểm tra rằng bạn không push nhầm nhánh hoặc dữ liệu nhạy cảm.

#### Cấu hình Pre-push Hook:
1. Mở thư mục `.git/hooks`.
2. Tạo hoặc chỉnh sửa file `pre-push`.
3. Thêm script kiểm tra trước khi push, ví dụ, kiểm tra xem các bài kiểm tra có thành công không:
   ```bash
   #!/bin/sh
   echo "Running tests before pushing..."
   npm test
   if [ $? -ne 0 ]; then
       echo "Tests failed, push aborted."
       exit 1
   fi
   ```

---

## 3. **Cấu Hình Git Hooks**

### a. **Thiết Lập Git Hooks**

Git hooks có thể được cấu hình trong thư mục `.git/hooks` trong repository của bạn. Thư mục này chứa các script mẫu với đuôi `.sample`. Để bắt đầu sử dụng một hook, bạn cần:
1. Chuyển đến thư mục `.git/hooks`.
2. Sao chép file hook mẫu (ví dụ: `pre-commit.sample`) và đổi tên thành `pre-commit`.
3. Mở file hook và thêm các lệnh hoặc script bạn muốn thực hiện khi hook đó được gọi.
4. Đảm bảo rằng script có quyền thực thi:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

### b. **Sử Dụng Các Công Cụ Quản Lý Git Hooks**

Một số công cụ như [Husky](https://github.com/typicode/husky) có thể giúp bạn quản lý và cấu hình Git hooks dễ dàng hơn. Husky hỗ trợ tích hợp với các hệ thống CI/CD và giúp việc cấu hình các hooks trở nên đơn giản hơn.

#### Cài Đặt Husky:
1. Cài đặt Husky:
   ```bash
   npm install husky --save-dev
   ```
2. Kích hoạt Husky để sử dụng các hook:
   ```bash
   npx husky install
   ```

3. Thêm hook vào package.json:
   ```json
   "husky": {
     "hooks": {
       "pre-commit": "npm run lint",
       "pre-push": "npm test"
     }
   }
   ```

---

## 4. **Ví Dụ Thực Tế**

### a. **Pre-commit Hook - Kiểm Tra Cú Pháp**

Trong dự án Python, bạn có thể sử dụng pre-commit hook để kiểm tra cú pháp mã nguồn trước khi commit.

Tạo file `.git/hooks/pre-commit` với nội dung:

```bash
#!/bin/sh
python -m py_compile $(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
if [ $? -ne 0 ]; then
    echo "Python syntax errors found, commit aborted."
    exit 1
fi
```

### b. **Post-commit Hook - Gửi Thông Báo**

Trong file `.git/hooks/post-commit`:

```bash
#!/bin/sh
echo "Commit successful! Notify the team..."
```

### c. **Pre-push Hook - Kiểm Tra Tests Trước Khi Push**

Trong file `.git/hooks/pre-push`:

```bash
#!/bin/sh
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed, push aborted."
    exit 1
fi
```

---

## 5. **Kết Luận**

Git Hooks là một công cụ mạnh mẽ giúp tự động hóa các tác vụ trong quy trình phát triển phần mềm, từ kiểm tra mã nguồn, chạy tests cho đến gửi thông báo và nhiều tác vụ khác. Việc cấu hình và sử dụng các Git hooks sẽ giúp nâng cao chất lượng mã nguồn, giảm thiểu lỗi và cải thiện quy trình làm việc trong nhóm. Hãy sử dụng các Git hooks để đảm bảo mã nguồn luôn tuân thủ các quy chuẩn và kiểm tra tự động trong quá trình phát triển.