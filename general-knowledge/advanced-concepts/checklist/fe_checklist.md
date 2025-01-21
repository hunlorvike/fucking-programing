## **🚀 DANH SÁCH KIỂM TRA CODE FRONT-END NEXT.JS: "CHECKLIST" ĐỈNH CAO CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay mình sẽ chia sẻ một "checklist" cực kỳ quan trọng cho dân code frontend Next.js: **Danh
sách kiểm tra code (Code Checklist)**. Đây là một công cụ giúp bạn kiểm tra lại code của mình, đảm bảo chất lượng, bảo
mật, hiệu suất và dễ bảo trì cho ứng dụng Next.js của bạn. Cùng mình khám phá nhé!

### **I. TẠI SAO CẦN CHECKLIST? (VÌ "CẨN TẮC VÔ ƯU")**

- **Checklist:** Là danh sách các việc cần làm để kiểm tra code trước khi chạy thật.
- **Quan trọng vì:**
    - **Chất lượng:** Đảm bảo code chạy đúng, không có lỗi.
    - **Bảo mật:** Ngăn chặn hacker tấn công.
    - **Hiệu suất:** Giúp ứng dụng chạy nhanh, mượt mà.
    - **Dễ bảo trì:** Code dễ đọc, dễ sửa chữa sau này.

### **II. CHECKLIST CHI TIẾT CHO FRONT-END NEXT.JS**

#### **1. BẢO MẬT (SECURITY) - "KHÓA CỬA" CẨN THẬN**

-   [ ] **XSS (Cross-Site Scripting):**
    - Dùng `sanitize-html` hoặc các API để lọc dữ liệu đầu vào/hiển thị (như bài trước về bảo mật cơ sở dữ liệu).
    - **Kiểm tra:** Có chặn XSS không?
-   [ ] **API Routes:**
    - Xác thực và phân quyền cho các API trong `pages/api` (như bài trước về API).
    - **Kiểm tra:** Chỉ có người dùng được phép mới gọi API được không?
-   [ ] **HTTP Headers:**
    - Cấu hình các header (CSP, X-Content-Type-Options, X-Frame-Options) trong `next.config.js` hoặc middleware (như đã
      nói ở bài về bảo mật web).
    - **Kiểm tra:** Có thiết lập bảo mật header không?
-   [ ] **CSRF (Cross-Site Request Forgery):**
    - Bảo vệ form bằng CSRF token.
    - **Kiểm tra:** Có dùng CSRF token không?
-   [ ] **Environment Variables:**
    - Quản lý biến môi trường (`.env`) và không để lộ trên client (như đã nói ở bài về bảo mật cơ sở dữ liệu).
    - **Kiểm tra:** Biến môi trường có lộ trên client không?
-   [ ] **JWT (JSON Web Token) và Auth:**
    - Có thời gian hết hạn (expire), dùng `HttpOnly` cookie (bài về authentication).
    - **Kiểm tra:** JWT có an toàn không?
-   [ ] **Path Traversal:**
    - Kiểm tra các route động để tránh truy cập file ngoài ý muốn.
    - **Kiểm tra:** Có ai truy cập file ngoài ý muốn không?
-   [ ] **Error Handling:**
    - Xử lý lỗi bằng `getServerSideProps`, `getStaticProps`, hoặc `pages/_error.js`.
    - **Kiểm tra:** Có trang lỗi 404, 500 không?
-   [ ] **Redirects:**
    - Kiểm tra nguồn gốc của yêu cầu trong `next.config.js` để tránh **open redirects**.
    - **Kiểm tra:** Redirect có an toàn không?

#### **2. HIỆU SUẤT (PERFORMANCE) - "CHẠY NHANH NHƯ CHỚP"**

-   [ ] **SSR/SSG/ISR/CSR:**
    - Cân nhắc chọn SSR, SSG, ISR, CSR để tối ưu cho từng trang (như đã nói ở bài về server-side rendering).
    - **Kiểm tra:** Có dùng đúng kỹ thuật cho từng trang không?
-   [ ] **Image Optimization:**
    - Dùng `<Image>` của Next.js để tối ưu hình ảnh.
    - **Kiểm tra:** Ảnh có được tối ưu không?
-   [ ] **Code Splitting:**
    - Dùng dynamic imports (`next/dynamic`) để lazy-load các module không cần thiết.
    - **Kiểm tra:** Module nào không dùng thì có lazy-load không?
-   [ ] **Caching:**
    - Dùng `Cache-Control` header trong SSR hoặc API routes (như bài về API).
    - **Kiểm tra:** Có cache dữ liệu không?
-   [ ] **Font Loading:**
    - Dùng tính năng tối ưu font của Next.js (Google Fonts Optimization).
    - **Kiểm tra:** Font có tối ưu không?
-   [ ] **Middleware/Edge Functions:**
    - Middleware có xử lý nhẹ, tránh làm chậm response.
    - **Kiểm tra:** Middleware có chạy nhanh không?
-   [ ] **Pre-fetching:**
    - Dùng `prefetch` để tải trước dữ liệu (mặc định trong Next.js).
    - **Kiểm tra:** Liên kết có prefetch không?
-   [ ] **Gzip/Brotli Compression:**
    - Có nén response (server-side hoặc CDN).
    - **Kiểm tra:** Có nén dữ liệu không?
-   [ ] **Tối ưu JS/CSS:**
    - Dùng `webpack-bundle-analyzer` để giảm kích thước bundle.
    - **Kiểm tra:** Bundle JS/CSS có quá lớn không?

#### **3. CHẤT LƯỢNG MÃ NGUỒN (CODE "GỌN GÀNG" VÀ DỄ HIỂU)**

-   [ ] **Cấu trúc thư mục:**
    - Code được tổ chức rõ ràng: `pages`, `components`, `lib`, `styles`.
-   [ ] **Reusable Components:**
    - Các component React được viết tái sử dụng (DRY principle).
-   [ ] **Code Cleanliness:**
    - Loại bỏ `console.log`, code không dùng, code tạm.
-   [ ] **State Management:**
    - Dùng đúng công cụ quản lý state: React Context, Redux, Zustand, ...
-   [ ] **Error Boundaries:**
    - Các component được bọc trong Error Boundaries để xử lý lỗi runtime.
-   [ ] **ESLint/Prettier:**
    - Dùng ESLint, Prettier để code sạch, đồng nhất.
-   [ ] **TypeScript:**
    - Dùng TypeScript, type đầy đủ cho props.
-   [ ] **API Integration:**
    - Các request API được tổ chức trong `lib/api` hoặc tương tự.
-   [ ] **SEO:**
    - Dùng `<Head>` để thêm metadata (title, description, canonical URL).

#### **4. TÀI LIỆU (DOCUMENTATION) - "HƯỚNG DẪN" ĐẦY ĐỦ**

-   [ ] **README:** Mô tả cách cài đặt, chạy, cấu hình dự án.
-   [ ] **API Documentation:** Các API route được tài liệu hóa (Postman, Swagger, ...).
-   [ ] **Chú thích:** Code phức tạp có comment đầy đủ.
-   [ ] **Hướng dẫn:** Hướng dẫn cách cài đặt, kết nối database, ...
-   [ ] **Lỗi và giới hạn:** Tài liệu liệt kê các lỗi, giới hạn của ứng dụng.
-   [ ] **Dependencies:** Liệt kê các package trong `README`.

#### **5. KIỂM THỬ (TESTING) - "THỬ NGHIỆM" CẨN THẬN**

1. **Kiểm thử chức năng (Functional Test):**
    - **Rendering:** Các trang render đúng nội dung.
    - **Routing:** Các route động hoạt động đúng.
    - **API:** Các API routes phản hồi đúng, xử lý lỗi.
    - **Responsive:** UI hiển thị đúng trên nhiều màn hình.
    - **Testing Frameworks:** Dùng Jest, Cypress, Playwright để viết test.
    - **Code Coverage:** Độ bao phủ code đạt mức mong muốn (≥80%).
2. **Kiểm thử hiệu suất (Performance Test):**
    - Dùng **Lighthouse** để đo hiệu suất (>=90).
    - Stress test để kiểm tra khi tải lớn.
    - Test các tình huống không có dữ liệu, lỗi server.
3. **Kiểm thử khả năng tiếp cận (Accessibility Test):**
    - Dùng **ARIA roles** cho các thành phần tương tác.
    - Kiểm tra khả năng điều hướng bằng bàn phím.
    - Kiểm tra bằng trình đọc màn hình.

#### **6. QUẢN LÝ TÀI NGUYÊN (KHÔNG LÃNG PHÍ)**

1. **Tài nguyên:**
    - Dùng `next/dynamic` để lazy-load các component.
    - Đặt các file tĩnh ở `public`.
    - Tối ưu kích thước hình ảnh.
2. **Bộ nhớ & Cache:**
    - Sử dụng `localStorage`, `sessionStorage` an toàn.
    - Kiểm tra thời gian tái tạo nếu dùng ISR.
    - Dùng CDN để giảm tải cho server.

#### **7. ĐÓNG GÓP (LÀM VIỆC "NHÓM" THẬT TỐT)**

- **Branching:** Có quy tắc quản lý branch (`main`, `dev`, feature branches).
- **Code Review:** Pull request được code review trước khi merge.
- **SOLID:** Tuân thủ nguyên tắc SOLID khi viết component.
- **Contributing:** Có hướng dẫn đóng góp rõ ràng.
- **Test before merge:** Yêu cầu các bài kiểm thử phải pass trước khi merge.

### **IX. KẾT LUẬN (TỔNG KẾT)**

Checklist này sẽ giúp các bạn kiểm tra code Next.js của mình một cách kỹ lưỡng, đảm bảo chất lượng, bảo mật, hiệu suất
và dễ bảo trì. Hy vọng nó sẽ là một "người bạn đồng hành" hữu ích cho các bạn trên con đường chinh phục thế giới
front-end! Chúc các bạn code thành công! 😎
