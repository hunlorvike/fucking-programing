## Bảo mật (Security)

Bảo mật trong hệ điều hành (HĐH) là một lĩnh vực quan trọng nhằm đảm bảo an toàn cho dữ liệu và ngăn chặn các hành vi truy cập trái phép. Dưới đây là các khía cạnh cơ bản trong bảo mật HĐH mà chúng ta cần quan tâm:

### 1. **Kiểm soát truy cập (Access Control)**

- **Xác thực (Authentication):** Là quá trình xác minh danh tính của người dùng hoặc ứng dụng. Các phương pháp phổ biến bao gồm mật khẩu, sinh trắc học (vân tay, nhận diện khuôn mặt), và các phương pháp xác thực đa yếu tố (Multi-Factor Authentication - MFA).
- **Phân quyền (Authorization):** Sau khi xác thực, hệ thống sẽ cấp quyền truy cập vào các tài nguyên nhất định, như tập tin hoặc thiết bị, tùy thuộc vào quyền hạn của người dùng.
- **Kiểm soát quyền truy cập (Access Control Lists - ACL):** Các bảng hoặc danh sách quy định rõ ai có thể truy cập tài nguyên nào, dưới quyền nào.

### 2. **Quản lý người dùng và nhóm (User and Group Management)**

- Hệ điều hành thường chia người dùng thành các nhóm, mỗi nhóm có quyền khác nhau. Ví dụ: người dùng bình thường có ít quyền hơn so với quản trị viên (admin).
- Các nhóm và người dùng này được quản lý nhằm giảm thiểu rủi ro bảo mật, ngăn ngừa việc một người dùng có thể truy cập vào các tài nguyên nhạy cảm nếu không có sự cho phép.

### 3. **Bảo mật cấp độ kernel (Kernel Security)**

- Kernel là lõi của hệ điều hành, quản lý tài nguyên hệ thống, và điều phối giao tiếp giữa phần cứng và phần mềm. Bảo mật kernel là yếu tố quan trọng để bảo vệ HĐH khỏi các mối đe dọa từ phần mềm độc hại.
- Các cơ chế bảo mật kernel như SELinux (Security-Enhanced Linux) và AppArmor trên Linux giúp kiểm soát và giới hạn quyền truy cập của ứng dụng vào các phần khác nhau của hệ thống.

### 4. **Mã hóa dữ liệu (Data Encryption)**

- **Mã hóa dữ liệu trên ổ đĩa (Disk Encryption):** Một số hệ điều hành hỗ trợ mã hóa toàn bộ ổ đĩa, ví dụ BitLocker trên Windows, hoặc FileVault trên macOS, giúp bảo vệ dữ liệu khi thiết bị bị mất hoặc đánh cắp.
- **Mã hóa dữ liệu trong truyền tải (Data in Transit):** Hệ điều hành thường hỗ trợ các giao thức mã hóa như SSL/TLS để bảo vệ dữ liệu khi được truyền qua mạng.

### 5. **Phát hiện và ngăn chặn xâm nhập (Intrusion Detection and Prevention Systems - IDS/IPS)**

- **IDS:** Hệ thống phát hiện xâm nhập giúp giám sát và ghi nhận các hành vi đáng ngờ. Ví dụ như phát hiện khi có hành vi truy cập bất thường vào hệ thống hoặc khi có người dùng cố gắng thực hiện các hành động trái phép.
- **IPS:** Hệ thống ngăn chặn xâm nhập có khả năng thực hiện hành động để ngăn chặn các cuộc tấn công đang diễn ra, ví dụ như chặn một địa chỉ IP có dấu hiệu tấn công.

### 6. **Bảo mật ứng dụng (Application Security)**

- Các hệ điều hành có khả năng chạy nhiều ứng dụng cùng lúc, vì vậy việc bảo vệ ứng dụng khỏi mã độc hoặc lỗ hổng bảo mật là rất quan trọng.
- Một số cơ chế bảo mật như ASLR (Address Space Layout Randomization) và DEP (Data Execution Prevention) giúp ngăn chặn các cuộc tấn công dựa trên bộ nhớ, như buffer overflow.

### 7. **Quản lý bản vá và cập nhật (Patch Management and Updates)**

- Hệ điều hành thường xuyên phát hành các bản vá bảo mật để sửa các lỗ hổng đã được phát hiện. Việc cập nhật hệ điều hành và các ứng dụng thường xuyên giúp giảm nguy cơ bị tấn công từ các lỗ hổng bảo mật.

### 8. **Giám sát và ghi log (Logging and Monitoring)**

- Việc ghi lại nhật ký hoạt động (logs) giúp hệ điều hành lưu trữ thông tin về các hành động, thay đổi trong hệ thống, và là công cụ hữu ích để kiểm tra khi có sự cố hoặc nghi ngờ xâm nhập.
- Giám sát các log để phát hiện kịp thời các hành vi bất thường là một phần quan trọng của bảo mật HĐH.

### 9. **Các nguyên tắc thiết kế bảo mật trong HĐH**

- **Nguyên tắc phân quyền tối thiểu (Principle of Least Privilege):** Chỉ cấp quyền cần thiết tối thiểu cho người dùng và ứng dụng.
- **Tách biệt trách nhiệm (Separation of Duties):** Tách biệt quyền của người dùng nhằm giảm nguy cơ một cá nhân có thể thực hiện nhiều nhiệm vụ nhạy cảm.
- **Bảo vệ lớp (Defense in Depth):** Sử dụng nhiều lớp bảo vệ để đảm bảo khi một lớp bị xâm nhập, các lớp khác vẫn giữ cho hệ thống an toàn.

Bảo mật hệ điều hành là một phần thiết yếu trong an toàn hệ thống và an ninh mạng. Nó đảm bảo rằng các thiết bị, dữ liệu, và mạng luôn được bảo vệ khỏi các mối đe dọa và xâm nhập không mong muốn.
