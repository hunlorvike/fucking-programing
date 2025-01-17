# **Danh Sách Kiểm Tra Code Front-End (Next.js)**

## **Nó là gì? Tại sao quan trọng?**

**Danh sách kiểm tra Code Front-End cho Next.js** là một công cụ để đảm bảo chất lượng code trong quá trình phát triển.
Với đặc thù của Next.js, danh sách này sẽ giúp các nhà phát triển chú ý đến các khía cạnh quan trọng, như server-side
rendering (SSR), static site generation (SSG), bảo mật và tối ưu hiệu suất, để đảm bảo sản phẩm chất lượng cao.

---

## **Next.js**

### **Bảo mật**

- [ ] **XSS**: Bạn đã sử dụng các công cụ như `sanitize-html` hoặc các API built-in để lọc dữ liệu đầu vào/hiển thị
  chưa?
- [ ] **API Routes**: Tất cả các route API trong thư mục `pages/api` có xác thực và phân quyền phù hợp chưa?
- [ ] **HTTP Headers**: Bạn đã cấu hình các HTTP header quan trọng (e.g., CSP, X-Content-Type-Options, X-Frame-Options)
  trong tệp `next.config.js` hoặc middleware chưa?
- [ ] **CSRF**: Các form hoặc endpoint nhạy cảm đã được bảo vệ chống **CSRF (Cross-Site Request Forgery)** chưa?
- [ ] **Environment Variables**: Biến môi trường (e.g., API_KEY) có được quản lý qua `.env` và không bị lộ trên
  client-side không?
- [ ] **JWT và Auth**: Nếu sử dụng JWT, bạn có thiết lập thời gian hết hạn và lưu trữ token một cách an toàn không? (
  e.g., `HttpOnly` cookie)
- [ ] **Path Traversal**: Bạn đã kiểm tra các route động trong Next.js để tránh lỗ hổng truy cập file ngoài ý muốn chưa?
- [ ] **Error Handling**: Bạn đã triển khai xử lý lỗi toàn cục bằng cách sử dụng `getServerSideProps`, `getStaticProps`
  hoặc các custom error page (e.g., `pages/404.js`, `pages/_error.js`) chưa?
- [ ] **Redirects**: Các logic chuyển hướng trong `next.config.js` có kiểm tra nguồn gốc của yêu cầu để ngăn **open
  redirects** không?

---

### **Hiệu suất**

- [ ] **SSR và SSG**: Bạn đã cân nhắc chọn giữa SSR, SSG, ISR (Incremental Static Regeneration), và CSR (Client-Side
  Rendering) cho từng trang để tối ưu hiệu suất chưa?
- [ ] **Image Optimization**: Bạn đã sử dụng `<Image>` của Next.js để tối ưu hóa hình ảnh chưa?
- [ ] **Code Splitting**: Tất cả các module không cần thiết có được lazy-loaded bằng dynamic imports (`next/dynamic`)
  không?
- [ ] **Caching**: Bạn đã sử dụng header `Cache-Control` trong SSR hoặc các API routes để tối ưu hóa caching chưa?
- [ ] **Font Loading**: Fonts có được tải thông qua công cụ built-in của Next.js (e.g., Google Fonts Optimization)
  không?
- [ ] **Middleware và Edge Functions**: Middleware có xử lý logic nhẹ và nhanh để tránh làm chậm phản hồi không?
- [ ] **Pre-fetching**: Các liên kết có sử dụng thuộc tính `prefetch` (mặc định trong Next.js) để tải trước dữ liệu
  không?
- [ ] **Gzip/Brotli Compression**: Bạn đã kích hoạt nén trên server-side hoặc CDN chưa?
- [ ] **Tối ưu JS/CSS**: Bạn có giảm kích thước bundle thông qua các công cụ như `webpack-bundle-analyzer` chưa?

---

## **Chất lượng mã nguồn**

- [ ] **Cấu trúc thư mục**: Mã nguồn có được tổ chức theo chuẩn Next.js (e.g., `pages`, `components`, `lib`, `styles`)
  không?
- [ ] **Reusable Components**: Các thành phần React có được viết tái sử dụng và không lặp lại logic không?
- [ ] **Code Cleanliness**: Bạn đã loại bỏ tất cả các `console.log`, đoạn code không sử dụng, hoặc tạm thời chưa?
- [ ] **State Management**: Bạn có sử dụng đúng công cụ quản lý state (e.g., React Context API, Redux, Zustand) cho các
  yêu cầu cụ thể chưa?
- [ ] **Error Boundaries**: Các thành phần React có được bọc trong Error Boundaries để xử lý lỗi runtime không?
- [ ] **ESLint/Prettier**: Bạn đã thiết lập và chạy các công cụ này để đảm bảo code sạch và đồng nhất chưa?
- [ ] **TypeScript**: Nếu sử dụng TypeScript, bạn đã định nghĩa đầy đủ kiểu dữ liệu và kiểm tra type cho tất cả props
  không?
- [ ] **API Integration**: Bạn có tổ chức tất cả các yêu cầu API trong một thư mục `lib/api` hoặc tương tự không?
- [ ] **SEO**: Các trang có sử dụng `<Head>` để thêm metadata như tiêu đề, mô tả và canonical URL không?

---

## **Tài liệu**

- [ ] **README**: Tệp README có mô tả chi tiết về cách cài đặt, chạy, và cấu hình dự án không?
- [ ] **API Documentation**: Các API routes trong `pages/api` đã được tài liệu hóa (e.g., Postman, Swagger) chưa?
- [ ] **Logic Custom**: Bạn có thêm bình luận hoặc mô tả chi tiết ở các đoạn code phức tạp không?
- [ ] **Các Edge Case**: Bạn đã ghi chú rõ ràng những tình huống biên hoặc lỗi tiềm ẩn trong code không?

---

## **Kiểm thử**

### **Kiểm thử chức năng**

- [ ] **Rendering**: Tất cả các trang có hiển thị đúng nội dung khi chạy SSR, SSG và CSR không?
- [ ] **Routing**: Các route động (e.g., `/posts/[id]`) có hoạt động chính xác với các tình huống biên không?
- [ ] **API**: Tất cả các API routes (`pages/api`) có phản hồi đúng trạng thái và xử lý lỗi không?
- [ ] **Responsive Design**: Các thành phần UI có hiển thị đúng trên các kích thước màn hình khác nhau không?
- [ ] **Testing Frameworks**: Bạn đã viết bài kiểm thử với Jest, Cypress hoặc Playwright chưa?

### **Kiểm thử hiệu suất**

- [ ] **Lighthouse**: Điểm hiệu suất của ứng dụng có đạt trên 90 trong Google Lighthouse không?
- [ ] **Stress Testing**: Hệ thống có hoạt động ổn định khi tải cao (e.g., nhiều yêu cầu API) không?
- [ ] **Edge Case Testing**: Bạn đã kiểm tra hành vi của hệ thống khi không có dữ liệu hoặc xảy ra lỗi server chưa?

### **Kiểm thử khả năng tiếp cận**

- [ ] **ARIA Roles**: Các thành phần tương tác có sử dụng đúng thuộc tính ARIA không?
- [ ] **Bàn phím**: Trang có thể điều hướng bằng bàn phím không?
- [ ] **Trình đọc màn hình**: Các trang có hiển thị đúng thông tin khi được truy cập bởi trình đọc màn hình không?

---

## **Quản lý tài nguyên**

### **Tài nguyên**

- [ ] **Dynamic Imports**: Bạn đã sử dụng `next/dynamic` để tải các thành phần lớn chỉ khi cần không?
- [ ] **Static Files**: Tất cả các tệp tĩnh có được đặt trong thư mục `public` và truy cập qua đường dẫn hợp lệ không?
- [ ] **Image Sizes**: Hình ảnh được tối ưu và có các kích thước phù hợp với từng thiết bị không?

### **Bộ nhớ và Cache**

- [ ] **Bộ nhớ Trình duyệt**: Bạn có sử dụng `localStorage` hoặc `sessionStorage` một cách an toàn và hiệu quả không?
- [ ] **Incremental Cache**: Nếu sử dụng ISR, bạn đã kiểm tra thời gian tái tạo để đảm bảo hiệu suất không?
- [ ] **CDN**: Bạn đã sử dụng CDN để giảm tải trực tiếp từ server không?

---

## **Đóng góp**

- [ ] **Branching**: Dự án có quy tắc quản lý branch rõ ràng (e.g., `main`, `dev`, feature branches) không?
- [ ] **Code Review**: Mọi pull request có được xem xét kỹ lưỡng trước khi merge không?
- [ ] **SOLID Principles**: Bạn có tuân thủ nguyên tắc **SOLID** khi thiết kế các component hoặc module không?
- [ ] **Contributing Guide**: Dự án có tài liệu hướng dẫn đóng góp rõ ràng không?

Danh sách kiểm tra này sẽ giúp bạn phát triển và duy trì ứng dụng Next.js với chất lượng cao, tối ưu hiệu suất, bảo mật
tốt và dễ dàng mở rộng!
