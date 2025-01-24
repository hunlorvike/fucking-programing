## **🚀 HƯỚNG DẪN SIÊU CHI TIẾT THIẾT KẾ API CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Chắc hẳn ai cũng nghe đến API rồi đúng không? Nó như kiểu "người phiên dịch" giúp các ứng
dụng "tám chuyện" với nhau ấy. Thiết kế API ngon nghẻ thì app mới chạy mượt mà, dễ dùng và không bị "tắc đường" giữa
chừng. Bài này mình sẽ chỉ các bạn cách thiết kế API từ A đến Z, đảm bảo sau bài này, các bạn sẽ tự tin "cân" mọi loại
API luôn.

---

### **I. API LÀ GÌ VÀ TẠI SAO PHẢI QUAN TÂM?**

**API (Application Programming Interface)**, dịch nôm na là "Giao diện lập trình ứng dụng", là tập hợp các quy tắc cho
phép các phần mềm giao tiếp với nhau. Hiểu đơn giản:

* **Ví dụ:** Bạn dùng app đặt đồ ăn, app đó gửi yêu cầu đến server của nhà hàng để lấy thông tin món ăn. API chính là "
  cầu nối" giúp hai bên nói chuyện được với nhau.
* **Quan trọng:** API xịn thì:
    * **Dễ dùng:** Code nhanh, không phải "vật lộn" với nó.
    * **Ngon:** Chạy nhanh, không giật lag.
    * **Dễ nâng cấp:** Thêm tính năng mới thoải mái, không "đụng hàng" cái cũ.
    * **Bảo mật:** Dữ liệu "an toàn như trong két sắt".

---

### **II. NGUYÊN TẮC VÀNG TRONG THIẾT KẾ API (DỄ NHỚ NHA!)**

1. **Đơn giản như đan rổ (Simplicity):**
    * **Endpoint ít thôi:** API nên tập trung vào chức năng chính, đừng có "tham" quá nhiều.
    * **Tên dễ hiểu:** Dùng tiếng Anh quen thuộc, ai đọc cũng hiểu.
        * **Ví dụ:** `GET /users` (lấy danh sách user) thay vì `GET /getAllUserInformation`.
    * **Code dễ đọc:** Tham số, dữ liệu phải rõ ràng, dễ hiểu như đọc truyện tranh.

2. **Nhất quán như sinh đôi (Consistency):**
    * **Tên "tài nguyên" đồng đều:**
        * Số nhiều cho danh sách: `/users`, `/products`.
        * Dùng HTTP method, không dùng từ trong URL: (đúng: `GET /users`, sai: `/getUsers`).
    * **Mã trạng thái HTTP:** Như kiểu "cờ báo", phải chuẩn:
        * `200`: Thành công (OK).
        * `201`: Tạo mới thành công (Created).
        * `400`: Yêu cầu sai (Bad Request).
        * `401`: Chưa đăng nhập (Unauthorized).
        * `404`: Không tìm thấy (Not Found).
        * `500`: Lỗi server (Internal Server Error).

3. **Linh hoạt như cao su (Flexibility):**
    * **Mở rộng:** Dự trù trước tương lai:
        * Dùng trường tùy chọn.
        * Dùng JSON hoặc XML cho dễ thay đổi.
    * **Không "phá game":** Khi thay đổi, API cũ vẫn phải chạy tốt.

4. **Bảo mật như két sắt (Security):**
    * **HTTPS:** Mã hóa dữ liệu truyền qua mạng (bắt buộc!).
    * **Xác thực và ủy quyền:** Dùng JWT hoặc OAuth 2.0 (sẽ nói rõ sau).
    * **Chống hacker:**
        * Kiểm tra đầu vào (input) để tránh SQL Injection.
        * "Chặn" XSS.
        * Thêm "tường lửa" chống DDoS.

5. **Nhanh như chớp (Performance):**
    * **Trả dữ liệu "vừa đủ":** Đừng "tham" trả hết, chỉ trả cái cần thiết thôi.
    * **Phân trang:** Với danh sách dài, chia nhỏ ra: `/users?page=2&limit=20`.
    * **Caching:** "Gom" dữ liệu lại để lần sau lấy cho nhanh.

---

### **III. "BẮT CHƯỚC" API RESTful (ĐƠN GIẢN MÀ CHẤT LƯỢNG)**

API RESTful là kiểu API "hot" nhất hiện nay. Nó tuân theo các quy tắc của REST (Representational State Transfer).

1. **Method HTTP (Động từ của API):**

   | Method    | Chức năng                               | Ví dụ               |
                          |-----------|-----------------------------------------|---------------------|
   | `GET`     | Lấy thông tin                           | `GET /users`        |
   | `POST`    | Tạo mới                                | `POST /users`       |
   | `PUT`     | Cập nhật toàn bộ                        | `PUT /users/123`    |
   | `PATCH`   | Cập nhật một phần                       | `PATCH /users/123`  |
   | `DELETE`  | Xóa bỏ                                 | `DELETE /users/123` |

2. **Tên tài nguyên (Danh từ của API):**

    * Dùng danh từ, không dùng động từ:
        * **Đúng:** `/users`, `/orders/123`.
        * **Sai:** `/getUsers`, `/createOrder`.
    * URL phân cấp:
        * Cha - con: `/users/123/orders`.

3. **Tham số truy vấn:**

    * Lọc: `GET /users?role=admin`.
    * Sắp xếp: `GET /users?sort=name`.
    * Phân trang: `GET /users?page=2&limit=10`.

---

### **IV. PHIÊN BẢN API (AI RỒI CŨNG KHÁC!)**

Khi API thay đổi, ta cần phiên bản để API cũ vẫn chạy tốt. Các cách hay dùng:

1. **URL Versioning:** `/api/v1/users` (dễ hiểu nhất).
2. **Header Versioning:** `Accept: application/vnd.api+json;version=1`.
3. **Query Parameter Versioning:** `/api/users?version=1`.

---

### **V. BẢO MẬT (CỰC KÌ QUAN TRỌNG!)**

1. **Xác thực (Authentication):**

    * Xác định ai đang dùng API.
    * **OAuth 2.0:** Cho các app có nhiều bên tham gia.
    * **JWT (JSON Web Tokens):** Token nhỏ gọn, dễ xài.

2. **Ủy quyền (Authorization):**

    * Quy định xem ai được làm gì.
    * **RBAC (Role-Based Access Control):** Phân quyền theo vai trò (admin, user).
    * **ABAC (Attribute-Based Access Control):** Phân quyền dựa vào thuộc tính (tuổi, vị trí).

---

### **VI. CHẶN "NGHẼN MẠCH" (RATE LIMITING)**

* Giới hạn số lần gọi API trong 1 khoảng thời gian để tránh bị "tấn công".
* **Ví dụ header:**
    * `X-RateLimit-Limit`: Giới hạn số lần gọi.
    * `X-RateLimit-Remaining`: Số lần còn lại.
    * `X-RateLimit-Reset`: Thời gian reset lại giới hạn.

---

### **VII. TÀI LIỆU API (CẨN THẬN LÀM GÌ CŨNG TỐT!)**

* **Công cụ:** Swagger, Postman, OpenAPI.
* **Nội dung cần có:**
    * Mô tả endpoint, request/response mẫu.
    * Giải thích mã lỗi.
    * SDK hoặc code mẫu cho các ngôn ngữ.

---

### **VIII. XỬ LÝ LỖI (HƯỚNG DẪN CỤ THỂ)**

* **Định dạng lỗi:** Trả về JSON:

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "Tham số 'email' không hợp lệ",
    "details": {
      "field": "email",
      "reason": "Sai định dạng"
    }
  }
}
```

* **Mã trạng thái HTTP chuẩn:** Như đã nói ở trên.

---

### **IX. VÍ DỤ CODE C# (CHO DỄ HÌNH DUNG)**

Giả sử ta có 1 model `User`:

```csharp
public class User
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
}
```

Ví dụ API lấy danh sách user bằng C# (ASP.NET Core):

```csharp
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase
{
    private static List<User> _users = new List<User> {
        new User { Id = 1, Name = "John Doe", Email = "john.doe@example.com" },
        new User { Id = 2, Name = "Jane Smith", Email = "jane.smith@example.com" }
    };

    [HttpGet]
    public IActionResult GetUsers([FromQuery] int page = 1, [FromQuery] int limit = 10)
    {
       var paginatedUsers = _users
                           .Skip((page - 1) * limit)
                           .Take(limit)
                           .ToList();

        var response = new {
                data = paginatedUsers,
                total = _users.Count(),
                page = page,
                limit = limit
        };

        return Ok(response);
    }

    [HttpGet("{id}")]
    public IActionResult GetUser(int id)
    {
        var user = _users.FirstOrDefault(u => u.Id == id);
        if (user == null)
        {
            return NotFound(); // Trả về 404 nếu không tìm thấy
        }
        return Ok(user); // Trả về 200 nếu tìm thấy
    }

    [HttpPost]
    public IActionResult CreateUser([FromBody] User newUser)
    {
      _users.Add(newUser);
      return CreatedAtAction(nameof(GetUser), new { id = newUser.Id }, newUser); // Trả về 201
    }

    [HttpPut("{id}")]
    public IActionResult UpdateUser(int id, [FromBody] User updatedUser)
    {
        var user = _users.FirstOrDefault(u => u.Id == id);
        if (user == null) return NotFound();
        user.Name = updatedUser.Name;
        user.Email = updatedUser.Email;
        return NoContent(); // Trả về 204 nếu cập nhật thành công
    }
    
    [HttpDelete("{id}")]
    public IActionResult DeleteUser(int id)
    {
          var user = _users.FirstOrDefault(u => u.Id == id);
         if (user == null) return NotFound();
         _users.Remove(user);
          return NoContent();
     }
}
```

**Giải thích:**

* `[ApiController]`: Đánh dấu class này là Controller API.
* `[Route("api/[controller]")]`: Định tuyến cho API.
* `[HttpGet]`, `[HttpPost]`, `[HttpPut]`, `[HttpDelete]`: Định nghĩa HTTP method.
* `IActionResult`: Trả về kết quả cho client.
* `FromQuery`: Lấy tham số từ query string (`page`, `limit`).
* `FromBody`: Lấy dữ liệu từ body request (JSON).
* `Ok()`, `NotFound()`, `Created()`, `NoContent()`: Trả về HTTP status code tương ứng.

---

### **X. QUY TRÌNH THIẾT KẾ API**

1. Xác định yêu cầu: Chức năng API làm gì?
2. Thiết kế tài nguyên và endpoint: Dùng HTTP method nào? URL ra sao?
3. Phát triển API và tài liệu: Code API + viết tài liệu.
4. Kiểm thử: Test API thật kĩ.
5. Triển khai và giám sát: Đưa API lên server + theo dõi hoạt động.

---

### **KẾT LUẬN**

Thiết kế API không khó, chỉ cần nắm vững nguyên tắc và thực hành nhiều. Chúc các bạn code API thành công và trở thành
những dev pro nhé! Có gì thắc mắc cứ hỏi, mình luôn sẵn sàng giúp đỡ! 💪
