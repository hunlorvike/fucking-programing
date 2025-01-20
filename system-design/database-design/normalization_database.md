## **🔥 "BÍ KÍP" CHUẨN HÓA DATABASE: 1NF, 2NF, 3NF CHO DÂN CODE 🔥**

Yo các bạn sinh viên IT! Chắc hẳn ai cũng từng nghe qua 1NF, 2NF, 3NF rồi đúng không? Nghe có vẻ "hack não" nhưng thực
ra rất dễ hiểu nếu mình "mổ xẻ" nó ra. Hôm nay mình sẽ cùng các bạn khám phá "bí kíp" chuẩn hóa database, giúp dữ liệu
vừa "sạch", vừa "ngon", lại vừa dễ bảo trì nhé!

### **I. TẠI SAO CẦN CHUẨN HÓA DATABASE?**

* **Chuẩn hóa (Normalization):** Là quá trình sắp xếp dữ liệu để loại bỏ trùng lặp, đảm bảo tính toàn vẹn.
* **Lợi ích:**
    * **Giảm dư thừa:** Tiết kiệm dung lượng.
    * **Dữ liệu nhất quán:** Tránh lỗi khi cập nhật.
    * **Tăng hiệu suất:** Truy vấn nhanh hơn.
    * **Dễ bảo trì:** Thay đổi không làm hỏng cấu trúc.

### **II. 1NF (FIRST NORMAL FORM) - "SẠCH" DỮ LIỆU TỪ ĐẦU**

* **Mục tiêu:** Đảm bảo mọi giá trị trong bảng đều là **nguyên tử** (không có danh sách, mảng, bảng lồng nhau).
* **Quy tắc:**
    1. Mỗi ô chỉ chứa một giá trị duy nhất (không có list, array).
    2. Mỗi hàng phải là duy nhất (có khóa chính - Primary Key).
    3. Không có bảng lồng.

* **Ví dụ:**

    * **Chưa đạt 1NF:**

      | StudentID | Name  | Subjects      |
                      |-----------|-------|---------------|
      | 1         | John  | Math, Science |
      | 2         | Mary  | Science       |
      | 3         | Peter | Math, English |

        * **Vấn đề:** Cột `Subjects` chứa nhiều giá trị.
    * **Đạt 1NF:**

      | StudentID | Name  | Subject |
                      |-----------|-------|---------|
      | 1         | John  | Math    |
      | 1         | John  | Science |
      | 2         | Mary  | Science |
      | 3         | Peter | Math    |
      | 3         | Peter | English |

        * **Giải pháp:** Tách giá trị trong `Subjects` thành các dòng riêng.

* **Mẹo:** 1NF giống như việc "dọn dẹp" dữ liệu, không để "rác" trong bảng.

### **III. 2NF (SECOND NORMAL FORM) - "LOẠI BỎ" PHỤ THUỘC MỘT PHẦN**

* **Mục tiêu:** Loại bỏ **phụ thuộc một phần (Partial Dependency)** vào khóa chính (khi khóa chính là một tập hợp các
  cột).
* **Quy tắc:**
    1. Phải đạt chuẩn 1NF.
    2. Mọi cột không khóa phải phụ thuộc **hoàn toàn** vào khóa chính.
* **Phụ thuộc một phần:** Khi một cột không khóa chỉ phụ thuộc vào *một phần* của khóa chính.

* **Ví dụ:**

    * **Chưa đạt 2NF:**

      | StudentID | CourseID | CourseName | Grade |
                      |-----------|----------|------------|-------|
      | 1         | C001     | Math       | A     |
      | 2         | C002     | Science    | B     |

        * **Khóa chính:** (`StudentID`, `CourseID`).
        * **Vấn đề:** `CourseName` chỉ phụ thuộc vào `CourseID`, không phụ thuộc vào `StudentID`.

    * **Đạt 2NF:**

        1. **Bảng `Courses`:**

           | CourseID | CourseName |
                                   |----------|------------|
           | C001     | Math       |
           | C002     | Science    |
        2. **Bảng `Enrollments`:**

           | StudentID | CourseID | Grade |
                                   |-----------|----------|-------|
           | 1         | C001     | A     |
           | 2         | C002     | B     |

        * **Giải pháp:** Tách `CourseName` ra bảng riêng.

* **Mẹo:** 2NF giống như việc "chia phòng" cho dữ liệu, mỗi cột có "chủ" rõ ràng.

### **IV. 3NF (THIRD NORMAL FORM) - "LOẠI BỎ" PHỤ THUỘC BẮC CẦU**

* **Mục tiêu:** Loại bỏ **phụ thuộc bắc cầu (Transitive Dependency)**.
* **Quy tắc:**
    1. Phải đạt chuẩn 2NF.
    2. Không có phụ thuộc bắc cầu:
        * Nếu A → B và B → C, thì A → C là phụ thuộc bắc cầu (không được phép có trực tiếp A-> C).
* **Phụ thuộc bắc cầu:** Khi một cột không khóa phụ thuộc vào một cột không khóa khác thay vì phụ thuộc trực tiếp vào
  khóa chính.

* **Ví dụ:**

    * **Chưa đạt 3NF:**

      | StudentID | AdvisorID | AdvisorName |
                      |-----------|-----------|-------------|
      | 1         | A001      | John        |
      | 2         | A002      | Mary        |

        * **Vấn đề:**
            * `AdvisorName` phụ thuộc vào `AdvisorID`.
            * `AdvisorID` phụ thuộc vào `StudentID`.
            * Vậy `AdvisorName` phụ thuộc bắc cầu vào `StudentID`.
    * **Đạt 3NF:**

        1. **Bảng `Advisors`:**

           | AdvisorID | AdvisorName |
                                   |-----------|-------------|
           | A001      | John        |
           | A002      | Mary        |
        2. **Bảng `Students`:**

           | StudentID | AdvisorID |
                                   |-----------|-----------|
           | 1         | A001      |
           | 2         | A002      |

        * **Giải pháp:** Tách `AdvisorName` ra bảng riêng.

* **Mẹo:** 3NF giống như việc "gỡ rối" dữ liệu, không để thông tin phụ thuộc "vòng vèo".

### **V. TÓM TẮT CÁC CHUẨN (NHỚ LÀM THEO NHA!)**

| Chuẩn | Yêu Cầu                                                                                       | Ví Dụ                                                                              |
|-------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 1NF   | Dữ liệu trong bảng phải nguyên tử, có khóa chính.                                             | Không có cột chứa nhiều giá trị (list, array).                                     |
| 2NF   | Đạt 1NF, loại bỏ phụ thuộc một phần (cột không khóa phụ thuộc *hoàn toàn* vào khóa chính).    | Tách thông tin `CourseName` vào bảng `Courses`, không để trong bảng `Enrollments`. |
| 3NF   | Đạt 2NF, loại bỏ phụ thuộc bắc cầu (cột không khóa chỉ phụ thuộc *trực tiếp* vào khóa chính). | Tách thông tin `AdvisorName` vào bảng `Advisors`, không để trong bảng `Students`.  |

### **VI. LỢI ÍCH CỦA CHUẨN HÓA (TẠI SAO PHẢI LÀM?)**

1. **Giảm dư thừa:** Tiết kiệm không gian lưu trữ, tránh lãng phí.
2. **Đảm bảo tính toàn vẹn:** Dữ liệu không bị mâu thuẫn khi cập nhật.
3. **Tăng hiệu quả truy vấn:** Truy vấn nhanh hơn, trả kết quả chính xác hơn.
4. **Dễ bảo trì, mở rộng:** Thay đổi, thêm bớt thông tin dễ dàng hơn.

### **KẾT LUẬN**

Chuẩn hóa database không phải là "bài toán khó nhằn" nếu bạn hiểu rõ các nguyên tắc và thực hành thường xuyên. Hy vọng "
bí kíp" này sẽ giúp các bạn nắm vững kiến thức và tự tin hơn khi thiết kế database nhé! Chúc các bạn thành công! 😎
