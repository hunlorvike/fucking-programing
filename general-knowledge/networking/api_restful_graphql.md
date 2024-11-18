# API và Kiến trúc RESTful/GraphQL

## Mục lục

1. [Tổng quan về API](#1-tổng-quan-về-api)  
2. [Kiến trúc RESTful](#2-kiến-trúc-restful)  
   - [2.1. Nguyên tắc REST](#21-nguyên-tắc-rest)  
   - [2.2. Phương thức HTTP](#22-phương-thức-http)  
   - [2.3. Định dạng dữ liệu](#23-định-dạng-dữ-liệu)  
   - [2.4. Ưu điểm và nhược điểm của REST](#24-ưu-điểm-và-nhược-điểm-của-rest)  
3. [GraphQL](#3-graphql)  
   - [3.1. Cơ chế hoạt động của GraphQL](#31-cơ-chế-hoạt-động-của-graphql)  
   - [3.2. Ưu điểm và nhược điểm của GraphQL](#32-ưu-điểm-và-nhược-điểm-của-graphql)  
4. [So sánh RESTful và GraphQL](#4-so-sánh-restful-và-graphql)  
5. [Ứng dụng thực tiễn](#5-ứng-dụng-thực-tiễn)  
6. [Tài liệu bổ sung](#6-tài-liệu-bổ-sung)  
7. [Kết luận](#7-kết-luận)  

---

## 1. Tổng quan về API

**API (Application Programming Interface)** là một giao diện lập trình cho phép các hệ thống hoặc ứng dụng giao tiếp với nhau.  
API cung cấp các điểm truy cập (endpoint) để nhận hoặc gửi dữ liệu, đảm bảo tính tương tác và tái sử dụng giữa các thành phần trong một hệ sinh thái phần mềm.  

### Các loại API phổ biến:
1. **REST API**: Được xây dựng trên kiến trúc REST.
2. **GraphQL API**: Sử dụng GraphQL làm giao thức.
3. **SOAP API**: Dựa trên XML để trao đổi dữ liệu.
4. **gRPC**: Sử dụng giao thức nhanh và hiệu quả do Google phát triển.

---

## 2. Kiến trúc RESTful

**REST (Representational State Transfer)** là một kiến trúc thiết kế API phổ biến, tận dụng giao thức HTTP để truyền tải dữ liệu.

### 2.1. Nguyên tắc REST:

1. **Client-Server**: Phân chia rõ ràng giữa máy khách (client) và máy chủ (server).  
2. **Stateless**: Máy chủ không lưu trạng thái của phiên làm việc, mỗi yêu cầu phải độc lập.  
3. **Cacheable**: Hỗ trợ lưu trữ (cache) để tăng tốc độ xử lý và giảm tải.  
4. **Uniform Interface**: Sử dụng giao diện thống nhất (URL và phương thức HTTP).  
5. **Layered System**: Cho phép các lớp trung gian giữa client và server.  
6. **Code on Demand (tùy chọn)**: Máy chủ có thể gửi mã thực thi cho client để mở rộng chức năng.

### 2.2. Phương thức HTTP

REST API dựa vào các phương thức HTTP chuẩn để thực hiện các thao tác:

| Phương thức | Mô tả               | Ví dụ                                   |
|-------------|---------------------|-----------------------------------------|
| **GET**     | Lấy dữ liệu         | `GET /api/books`                        |
| **POST**    | Tạo dữ liệu         | `POST /api/books`                       |
| **PUT**     | Cập nhật toàn bộ    | `PUT /api/books/{id}`                   |
| **PATCH**   | Cập nhật một phần   | `PATCH /api/books/{id}`                 |
| **DELETE**  | Xóa dữ liệu         | `DELETE /api/books/{id}`                |

### 2.3. Định dạng dữ liệu:

- **JSON** (JavaScript Object Notation): Định dạng phổ biến, dễ đọc và sử dụng.
- **XML** (Extensible Markup Language): Được sử dụng trong các hệ thống cũ.
- **YAML** hoặc **MessagePack**: Tùy ứng dụng cụ thể.

### 2.4. Ưu điểm và nhược điểm của REST:

**Ưu điểm:**
- **Tính đơn giản**: REST dễ học và triển khai nhờ dựa vào HTTP.
- **Mở rộng tốt**: API có thể dễ dàng được mở rộng khi yêu cầu thay đổi.
- **Công cụ hỗ trợ phong phú**: Hỗ trợ trên nhiều nền tảng.

**Nhược điểm:**
- **Over-fetching**: Máy khách nhận nhiều dữ liệu hơn cần thiết.
- **Under-fetching**: Máy khách phải thực hiện nhiều request để lấy đủ dữ liệu.
- **Thiếu tính mô hình hóa**: Không hỗ trợ cấu trúc truy vấn động như GraphQL.

---

## 3. GraphQL

**GraphQL** là một ngôn ngữ truy vấn API được Facebook phát triển vào năm 2012, cung cấp cách tiếp cận linh hoạt hơn trong việc lấy dữ liệu.

### 3.1. Cơ chế hoạt động của GraphQL:

1. **Query**: Máy khách gửi một truy vấn (query) định nghĩa dữ liệu cần lấy.
2. **Schema**: Máy chủ GraphQL dựa vào schema để xử lý truy vấn.
3. **Response**: Máy chủ trả về đúng và đủ dữ liệu theo yêu cầu.

Ví dụ truy vấn:  
```graphql
{
  books {
    title
    author
  }
}
```

Kết quả trả về:  
```json
{
  "data": {
    "books": [
      { "title": "Book A", "author": "Author X" },
      { "title": "Book B", "author": "Author Y" }
    ]
  }
}
```

### 3.2. Ưu điểm và nhược điểm của GraphQL:

**Ưu điểm:**
- **Truy vấn cụ thể**: Máy khách nhận đúng dữ liệu cần thiết.
- **Giảm tải băng thông**: Tối ưu hóa dữ liệu trả về.
- **Một request**: Gộp nhiều truy vấn vào một request duy nhất.

**Nhược điểm:**
- **Cần schema**: Cần thiết kế và duy trì schema phức tạp.
- **Học tập**: Độ phức tạp cao hơn REST đối với người mới.
- **Quản lý bộ nhớ**: Truy vấn phức tạp có thể gây quá tải máy chủ.

---

## 4. So sánh RESTful và GraphQL

| Tiêu chí             | RESTful                  | GraphQL                  |
|----------------------|--------------------------|--------------------------|
| **Cách truyền tải**   | Endpoint cố định         | Endpoint duy nhất        |
| **Truy vấn dữ liệu**  | Nhiều request            | Một request              |
| **Hiệu quả**          | Thấp (Over/Under-fetch) | Cao (Custom query)       |
| **Phức tạp**          | Thấp                    | Cao                      |
| **Khả năng mở rộng**  | Dễ                      | Yêu cầu cấu trúc schema  |

---

## 5. Ứng dụng thực tiễn

- **RESTful API**:  
  Thích hợp cho các hệ thống cần giao tiếp nhanh, đơn giản. Ví dụ:
  - Ứng dụng thương mại điện tử.
  - Các dịch vụ tích hợp bên thứ ba như PayPal, Stripe.

- **GraphQL API**:  
  Tốt cho ứng dụng cần dữ liệu động hoặc tiết kiệm băng thông. Ví dụ:
  - Ứng dụng di động.
  - Dịch vụ đòi hỏi hiệu suất cao như nền tảng truyền thông xã hội.

---

## 6. Tài liệu bổ sung

- **RESTful API**:
  - [Roy Fielding Dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
  - [REST API Tutorial](https://restfulapi.net/)

- **GraphQL**:
  - [Official GraphQL Documentation](https://graphql.org/)
  - [Apollo GraphQL](https://www.apollographql.com/)

---

## 7. Kết luận

RESTful API và GraphQL đều là các công cụ mạnh mẽ để xây dựng ứng dụng. Lựa chọn giữa chúng phụ thuộc vào yêu cầu cụ thể:  
- Chọn **RESTful API** nếu ứng dụng cần sự đơn giản, tiêu chuẩn hóa.  
- Chọn **GraphQL** nếu ứng dụng đòi hỏi hiệu quả cao và tùy biến dữ liệu linh hoạt.  

Việc kết hợp cả hai phương pháp (hybrid architecture) cũng là một xu hướng đang được nhiều tổ chức áp dụng.