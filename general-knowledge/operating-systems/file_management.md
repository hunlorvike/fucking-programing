## Hệ thống tập tin (File System)

### 1. Giới thiệu

Hệ thống tập tin là một thành phần cốt lõi của hệ điều hành, chịu trách nhiệm quản lý cách thức lưu trữ, truy cập và tổ
chức dữ liệu trên các thiết bị lưu trữ như ổ cứng, SSD, USB. Nó đóng vai trò như một lớp trung gian giữa hệ điều hành và
các thiết bị lưu trữ, cho phép người dùng và ứng dụng tương tác với dữ liệu một cách dễ dàng và hiệu quả.

### 2. Mục đích và chức năng chính

Hệ thống tập tin đảm nhận nhiều vai trò quan trọng, bao gồm:

- **Lưu trữ và tổ chức dữ liệu:** Dữ liệu được lưu trữ dưới dạng các tệp (file) và thư mục (directory) theo một cấu trúc
  tổ chức hợp lý, giúp người dùng dễ dàng tìm kiếm và truy cập thông tin.
- **Quản lý quyền truy cập:** Hệ thống tập tin kiểm soát quyền truy cập của người dùng và ứng dụng vào các tệp và thư
  mục, đảm bảo tính bảo mật và toàn vẹn của dữ liệu.
- **Tối ưu hóa không gian lưu trữ:** Hệ thống tập tin phân bổ không gian lưu trữ hiệu quả, tránh phân mảnh và tối ưu hóa
  tốc độ truy cập dữ liệu.
- **Bảo vệ dữ liệu:** Hệ thống tập tin cung cấp các cơ chế bảo vệ dữ liệu khỏi bị mất mát, hư hỏng hoặc truy cập trái
  phép, bao gồm sao lưu, phục hồi dữ liệu, mã hóa, v.v.

### 3. Các khái niệm cơ bản

- **Tệp (File):** Đơn vị cơ bản để lưu trữ dữ liệu, có thể là văn bản, hình ảnh, video, chương trình, v.v. Mỗi tệp có
  một tên duy nhất và chứa các thông tin về nội dung, kích thước, ngày tạo, ngày sửa đổi, v.v.
- **Thư mục (Directory):** Một container chứa các tệp và thư mục con, tạo thành một cấu trúc cây để tổ chức dữ liệu.
- **Đường dẫn (Path):** Một chuỗi ký tự mô tả vị trí của một tệp hoặc thư mục trong hệ thống tập tin. Đường dẫn có thể
  là tuyệt đối (bắt đầu từ gốc hệ thống) hoặc tương đối (tính từ vị trí hiện tại).
- **Metadata (Siêu dữ liệu):** Thông tin về một tệp, như tên, kích thước, ngày tạo, ngày sửa đổi, quyền truy cập, v.v.
  Metadata giúp hệ thống tập tin quản lý và truy xuất dữ liệu hiệu quả.

### 4. Cấu trúc dữ liệu và quản lý không gian lưu trữ

- **Cấu trúc thư mục:** Hệ thống tập tin có thể sử dụng các cấu trúc thư mục khác nhau để tổ chức dữ liệu, phổ biến nhất
  là:
    - **Thư mục đơn cấp:** Tất cả các tệp nằm trong một thư mục duy nhất. Phương pháp này đơn giản nhưng không hiệu quả
      khi số lượng tệp tăng.
    - **Thư mục hai cấp:** Hệ thống cung cấp một thư mục riêng cho mỗi người dùng, giúp phân biệt dữ liệu của từng
      người.
    - **Thư mục dạng cây:** Cấu trúc thư mục lồng nhau theo dạng cây, phổ biến trong hầu hết các hệ điều hành hiện đại.
    - **Thư mục đồ thị:** Cho phép các tệp và thư mục có thể được liên kết với nhiều thư mục khác nhau bằng các liên
      kết (link), giúp tiết kiệm không gian và tránh lưu trữ lặp lại.
- **Phân bổ không gian lưu trữ:** Hệ thống tập tin sử dụng các phương pháp khác nhau để phân bổ không gian đĩa cho các
  tệp, mỗi phương pháp có ưu nhược điểm riêng:
    - **Phân bổ tuần tự (Contiguous Allocation):** Các khối dữ liệu của tệp được lưu liên tục trên đĩa, giúp truy xuất
      nhanh nhưng khó mở rộng.
    - **Phân bổ liên kết (Linked Allocation):** Các khối dữ liệu của tệp được liên kết với nhau thông qua con trỏ.
      Phương pháp này dễ mở rộng nhưng tốc độ truy cập ngẫu nhiên chậm.
    - **Phân bổ chỉ số (Indexed Allocation):** Sử dụng một khối chỉ số chứa các con trỏ đến các khối dữ liệu của tệp,
      giúp truy xuất hiệu quả hơn và dễ quản lý không gian.

### 5. Quản lý không gian trống

- **Danh sách liên kết:** Lưu trữ các khối trống vào một danh sách liên kết, dễ quản lý nhưng gây chậm trong việc tìm
  kiếm khối trống.
- **Bản đồ bit:** Mỗi khối được đại diện bởi một bit (0 cho trống, 1 cho đã sử dụng). Phương pháp này giúp xác định
  không gian trống dễ dàng nhưng tốn thêm bộ nhớ.
- **Bảng không gian trống:** Một bảng ghi lại vị trí các khối trống, giúp giảm thời gian tìm kiếm không gian trống cho
  các tệp mới.

### 6. Các hệ thống tập tin phổ biến

- **FAT (File Allocation Table):** Hệ thống tập tin đơn giản và phổ biến, được sử dụng trên USB, thẻ nhớ, và các thiết
  bị di động.
- **NTFS (New Technology File System):** Hệ thống tập tin của Windows, hỗ trợ bảo mật tốt, quản lý không gian hiệu quả
  và phục hồi dữ liệu khi xảy ra sự cố.
- **ext (Extended File System):** Hệ thống tập tin của Linux, có nhiều phiên bản (ext2, ext3, ext4) với cải tiến về hiệu
  suất và quản lý dữ liệu.
- **HFS+ và APFS:** Hệ thống tập tin của Apple, với APFS (Apple File System) là phiên bản hiện đại, tối ưu hóa cho SSD
  và cải thiện hiệu suất truy xuất.

### 7. Quản lý tệp (File Management)

Hệ điều hành cung cấp các lệnh và API để người dùng và ứng dụng có thể thực hiện các thao tác với tệp, bao gồm:

- **Tạo và xóa tệp:** Tạo mới hoặc xóa tệp khi cần.
- **Mở và đóng tệp:** Mở tệp để truy xuất dữ liệu và đóng tệp khi kết thúc.
- **Đọc và ghi tệp:** Đọc dữ liệu từ tệp vào bộ nhớ và ghi dữ liệu từ bộ nhớ vào tệp.
- **Cấp phát quyền truy cập:** Kiểm soát quyền truy cập của người dùng và ứng dụng vào tệp.

### 8. Quyền truy cập tệp (File Permissions)

Hệ thống tập tin kiểm soát quyền truy cập vào tệp thông qua các cấp quyền, bao gồm:

- **Quyền cơ bản:**
    - **Đọc (Read):** Cho phép xem nội dung tệp.
    - **Ghi (Write):** Cho phép thay đổi hoặc bổ sung nội dung tệp.
    - **Thực thi (Execute):** Cho phép chạy tệp (dành cho các chương trình).
- **Quyền nâng cao:**
    - **Quyền chủ sở hữu:** Người tạo ra tệp có toàn quyền thao tác.
    - **Quyền nhóm:** Quyền truy cập cho một nhóm người dùng.
    - **Quyền người khác:** Quyền truy cập cho những người dùng khác ngoài chủ sở hữu và nhóm.

### 9. Cấu trúc dữ liệu và các khối siêu dữ liệu (Metadata)

- **i-node:** Trên các hệ thống như ext, thông tin về tệp được lưu trong i-node, chứa các thuộc tính như kích thước,
  quyền truy cập, và các con trỏ đến khối dữ liệu.
- **MFT (Master File Table):** Trên hệ thống NTFS, MFT lưu trữ thông tin về các tệp, giúp xác định nhanh vị trí của tệp
  trên đĩa.
- **Superblock:** Lưu trữ các thông tin quan trọng của hệ thống tập tin như kích thước hệ thống, số lượng khối, vị trí
  của bảng i-node hoặc bảng FAT.

### 10. Cơ chế bảo vệ và an toàn dữ liệu

Hệ thống tập tin cung cấp các cơ chế bảo vệ dữ liệu khỏi bị mất mát hoặc truy cập trái phép, bao gồm:

- **Sao lưu và phục hồi:** Sao lưu các tệp quan trọng để phục hồi khi có sự cố.
- **Nhật ký (Journaling):** Ghi lại các thay đổi trước khi áp dụng, đảm bảo tính toàn vẹn của dữ liệu khi hệ thống gặp
  sự cố.
- **Mã hóa (Encryption):** Mã hóa dữ liệu nhạy cảm, chỉ cho phép người có quyền giải mã.

### 11. Vấn đề phân mảnh tập tin và giảm phân mảnh

- **Phân mảnh:** Xảy ra khi tệp được lưu trữ không liên tục, gây giảm hiệu suất truy cập.
- **Giảm phân mảnh:** Một số hệ điều hành cung cấp công cụ giảm phân mảnh, sắp xếp lại các khối dữ liệu của tệp thành
  liên tục để cải thiện hiệu suất.

### 12. Ý nghĩa của hệ thống tập tin

Hệ thống tập tin đóng vai trò quan trọng trong hoạt động của hệ điều hành, mang lại nhiều lợi ích cho người dùng:

- **Quản lý dữ liệu hiệu quả:** Giúp người dùng dễ dàng tổ chức, truy cập và quản lý dữ liệu.
- **Bảo vệ dữ liệu:** Đảm bảo tính an toàn và toàn vẹn của dữ liệu.
- **Tối ưu hóa hiệu suất:** Giúp hệ thống hoạt động mượt mà và truy xuất dữ liệu nhanh hơn.

### 13. Kết luận

Hệ thống tập tin là một thành phần không thể thiếu trong hệ điều hành, chịu trách nhiệm quản lý và tổ chức dữ liệu một
cách hiệu quả và an toàn. Việc hiểu rõ về cấu trúc, chức năng và các khái niệm liên quan đến hệ thống tập tin giúp người
dùng sử dụng hệ thống hiệu quả hơn và bảo vệ dữ liệu một cách tốt nhất.
