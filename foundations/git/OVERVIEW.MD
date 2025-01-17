### **1. Khái Niệm Git: Git là gì và tại sao nó được sử dụng?**

**Git** là một hệ thống quản lý phiên bản phân tán, được phát triển bởi Linus Torvalds vào năm 2005 để hỗ trợ việc phát
triển Linux kernel. Git cho phép các lập trình viên theo dõi và quản lý các thay đổi trong mã nguồn của dự án qua thời
gian.

#### Tại sao Git được sử dụng?

Git được sử dụng bởi nhiều lý do sau:

- **Quản lý lịch sử phiên bản**: Git giúp lưu trữ và quản lý các thay đổi trong mã nguồn, giúp bạn dễ dàng quay lại một
  phiên bản trước của mã nguồn khi cần thiết.
- **Làm việc nhóm**: Git cho phép nhiều lập trình viên làm việc đồng thời trên các tính năng khác nhau mà không làm ảnh
  hưởng đến nhau.
- **Phân tán**: Git là hệ thống phân tán, có nghĩa là mỗi người dùng có một bản sao hoàn chỉnh của kho mã nguồn. Điều
  này giúp làm việc nhanh chóng và hiệu quả.
- **Dễ dàng phục hồi dữ liệu**: Git giúp phục hồi lại dữ liệu bị mất nếu có sự cố, vì mỗi thay đổi đều được lưu trữ
  trong lịch sử của Git.

### **2. Các Khái Niệm Cơ Bản trong Git**

Dưới đây là các khái niệm cơ bản trong Git mà bạn cần biết khi bắt đầu sử dụng Git:

#### **2.1. Repository (Repo)**

- **Repository** (hay còn gọi là "Repo") là nơi lưu trữ mã nguồn của dự án, nơi mà toàn bộ lịch sử và dữ liệu của dự án
  được quản lý. Một repository có thể là **local repository** (trên máy tính của bạn) hoặc **remote repository** (lưu
  trữ trên server như GitHub, GitLab, Bitbucket,...).
- Một repository trong Git có thể chứa tất cả các thông tin về dự án, bao gồm mã nguồn, commit history và các cài đặt.

#### **2.2. Commit**

- **Commit** là hành động ghi lại các thay đổi vào trong repository. Mỗi commit bao gồm một thông điệp mô tả về các thay
  đổi mà bạn đã thực hiện và một **hash** duy nhất để phân biệt giữa các commit.
- Commit cũng có thể được hiểu như là một "snapshot" của toàn bộ dự án tại thời điểm đó.
- Mỗi commit có một mã hash duy nhất (SHA-1) để giúp bạn theo dõi và quản lý thay đổi dễ dàng.

#### **2.3. Branch**

- **Branch** (nhánh) là một đường đi song song trong Git để bạn có thể làm việc độc lập mà không làm ảnh hưởng đến nhánh
  chính (thường là `main` hoặc `master`).
- Các nhánh cho phép bạn phát triển tính năng mới hoặc thử nghiệm mà không làm thay đổi mã nguồn chính cho đến khi hoàn
  thành.
- Ví dụ, bạn có thể tạo một nhánh mới để phát triển tính năng mới và khi tính năng đó hoàn thiện, bạn có thể **merge** (
  hợp nhất) lại vào nhánh chính.

#### **2.4. Merge**

- **Merge** là hành động kết hợp các thay đổi từ một nhánh này vào nhánh khác.
- Khi bạn đã hoàn thành công việc trên một nhánh, bạn có thể sử dụng lệnh merge để tích hợp thay đổi từ nhánh đó vào
  nhánh chính (hoặc bất kỳ nhánh nào bạn muốn).
- Khi merge, Git sẽ tự động xử lý hầu hết các xung đột, nhưng nếu có sự khác biệt lớn, bạn sẽ cần phải giải quyết các
  xung đột đó thủ công.

#### **2.5. Clone**

- **Clone** là hành động sao chép một repository từ một nơi khác về máy của bạn. Bạn có thể clone một repository từ một
  server như GitHub hoặc GitLab về máy tính của mình.
- Lệnh `git clone` tạo ra một bản sao hoàn chỉnh của repository, bao gồm tất cả các file, commit history và các nhánh
  của dự án.

#### **2.6. Pull**

- **Pull** là lệnh được sử dụng để tải về các thay đổi từ repository remote (trên server) vào repository local của bạn.
- Lệnh `git pull` thực hiện hai bước: **fetch** (lấy dữ liệu từ remote) và **merge** (hợp nhất các thay đổi vào nhánh
  hiện tại).

#### **2.7. Push**

- **Push** là hành động gửi các thay đổi mà bạn đã thực hiện từ repository local lên repository remote (trên server).
- Lệnh `git push` giúp bạn cập nhật các thay đổi mà bạn đã commit lên server, giúp đồng bộ hóa với các thành viên trong
  nhóm và làm việc với các bản sao của repository.

### **3. Tóm tắt các lệnh Git cơ bản**

Dưới đây là các lệnh Git cơ bản mà bạn sẽ thường xuyên sử dụng:

1. **Khởi tạo repository mới**:

   ```
   git init
   ```

2. **Clone một repository**:

   ```
   git clone <URL>
   ```

3. **Kiểm tra trạng thái các thay đổi**:

   ```
   git status
   ```

4. **Thêm các thay đổi vào staging area**:

   ```
   git add <file>
   ```

5. **Commit các thay đổi**:

   ```
   git commit -m "Thông điệp commit"
   ```

6. **Xem lịch sử commit**:

   ```
   git log
   ```

7. **Tạo nhánh mới**:

   ```
   git branch <tên nhánh>
   ```

8. **Chuyển sang nhánh khác**:

   ```
   git checkout <tên nhánh>
   ```

9. **Hợp nhất nhánh**:

   ```
   git merge <tên nhánh>
   ```

10. **Lấy các thay đổi từ remote repository**:

    ```
    git pull
    ```

11. **Đẩy các thay đổi lên remote repository**:
    ```
    git push
    ```

### **Kết luận**

Git là một công cụ vô cùng mạnh mẽ và quan trọng trong phát triển phần mềm. Nó không chỉ giúp bạn theo dõi sự thay đổi
của mã nguồn mà còn giúp bạn hợp tác hiệu quả với đồng nghiệp. Sau khi hiểu rõ các khái niệm cơ bản, bạn có thể dễ dàng
bắt đầu làm việc với Git để quản lý dự án của mình.

Nếu bạn có thêm câu hỏi hoặc muốn tìm hiểu sâu hơn về các tính năng nâng cao của Git, đừng ngần ngại yêu cầu!
