# **Giải Thích Chi Tiết Các Chuẩn 1NF, 2NF, 3NF trong Thiết Kế Database**

Các dạng chuẩn hóa (Normalization) giúp đảm bảo tính toàn vẹn dữ liệu và loại bỏ dư thừa trong cơ sở dữ liệu. Dưới đây
là giải thích cụ thể về **1NF**, **2NF**, và **3NF**:

---

## **1NF (First Normal Form) – Dạng Chuẩn Thứ Nhất**

### **Mục Tiêu:**

Đảm bảo rằng tất cả các cột trong bảng chỉ chứa **dữ liệu nguyên tử (atomic)** và không có dữ liệu dạng lặp hay bảng
lồng trong bảng.

### **Quy Tắc:**

1. Mỗi ô trong bảng chỉ chứa một giá trị duy nhất (không có danh sách hoặc tập hợp).
2. Mỗi hàng phải là duy nhất (sử dụng khóa chính - Primary Key).
3. Không có bảng lồng hoặc cấu trúc dữ liệu phức tạp.

### **Ví Dụ:**

#### **Bảng chưa đạt chuẩn 1NF:**

| StudentID | Name  | Subjects      |
|-----------|-------|---------------|
| 1         | John  | Math, Science |
| 2         | Mary  | Science       |
| 3         | Peter | Math, English |

#### **Vấn Đề:**

- Cột `Subjects` chứa nhiều giá trị (không nguyên tử).

#### **Bảng đạt chuẩn 1NF:**

| StudentID | Name  | Subject |
|-----------|-------|---------|
| 1         | John  | Math    |
| 1         | John  | Science |
| 2         | Mary  | Science |
| 3         | Peter | Math    |
| 3         | Peter | English |

- **Giải pháp:** Mỗi giá trị trong cột `Subject` được tách riêng thành các dòng riêng biệt.

---

## **2NF (Second Normal Form) – Dạng Chuẩn Thứ Hai**

### **Mục Tiêu:**

Loại bỏ các phụ thuộc một phần (Partial Dependency) vào **khóa chính**.

### **Quy Tắc:**

1. Bảng phải thỏa mãn chuẩn 1NF.
2. Mỗi cột không khóa phải phụ thuộc **hoàn toàn** vào **khóa chính** (không phụ thuộc một phần).

### **Phụ Thuộc Một Phần (Partial Dependency):**

- Xảy ra khi một thuộc tính không khóa chỉ phụ thuộc vào một phần của khóa chính (trong trường hợp khóa chính là một tập
  hợp nhiều cột).

### **Ví Dụ:**

#### **Bảng chưa đạt chuẩn 2NF:**

| StudentID | CourseID | CourseName | Grade |
|-----------|----------|------------|-------|
| 1         | C001     | Math       | A     |
| 2         | C002     | Science    | B     |

- **Khóa chính:** (`StudentID`, `CourseID`).
- **Vấn đề:** `CourseName` chỉ phụ thuộc vào `CourseID`, không phụ thuộc vào cả khóa chính.

#### **Bảng đạt chuẩn 2NF:**

1. **Tách bảng `Courses`:**
   | CourseID | CourseName |
   |----------|------------|
   | C001 | Math |
   | C002 | Science |

2. **Bảng `Enrollments`:**
   | StudentID | CourseID | Grade |
   |-----------|----------|-------|
   | 1 | C001 | A |
   | 2 | C002 | B |

- **Giải pháp:** Tách `CourseName` vào bảng riêng, chỉ giữ lại các thuộc tính phụ thuộc hoàn toàn vào khóa chính.

---

## **3NF (Third Normal Form) – Dạng Chuẩn Thứ Ba**

### **Mục Tiêu:**

Loại bỏ **phụ thuộc bắc cầu (Transitive Dependency)** để đảm bảo mỗi cột không khóa chỉ phụ thuộc vào **khóa chính** và
không phụ thuộc vào các cột khác.

### **Quy Tắc:**

1. Bảng phải thỏa mãn chuẩn 2NF.
2. Không có phụ thuộc bắc cầu:
    - Nếu cột A → B và B → C, thì A → C là phụ thuộc bắc cầu.

### **Phụ Thuộc Bắc Cầu (Transitive Dependency):**

- Xảy ra khi một thuộc tính không khóa phụ thuộc vào một thuộc tính không khóa khác thay vì trực tiếp phụ thuộc vào khóa
  chính.

### **Ví Dụ:**

#### **Bảng chưa đạt chuẩn 3NF:**

| StudentID | AdvisorID | AdvisorName |
|-----------|-----------|-------------|
| 1         | A001      | John        |
| 2         | A002      | Mary        |

- **Vấn đề:**
    - `AdvisorName` phụ thuộc vào `AdvisorID`.
    - `AdvisorID` phụ thuộc vào `StudentID` (khóa chính).
    - Do đó, `AdvisorName` phụ thuộc bắc cầu vào `StudentID`.

#### **Bảng đạt chuẩn 3NF:**

1. **Tách bảng `Advisors`:**
   | AdvisorID | AdvisorName |
   |-----------|-------------|
   | A001 | John |
   | A002 | Mary |

2. **Bảng `Students`:**
   | StudentID | AdvisorID |
   |-----------|-----------|
   | 1 | A001 |
   | 2 | A002 |

- **Giải pháp:** Tách dữ liệu `AdvisorName` vào bảng riêng, chỉ giữ lại các thuộc tính liên kết trực tiếp với khóa
  chính.

---

## **Tóm Tắt Các Chuẩn**

| **Chuẩn** | **Yêu Cầu**                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------|
| **1NF**   | Dữ liệu trong bảng phải nguyên tử (không chứa danh sách, bảng lồng) và mỗi hàng phải có khóa chính.                                 |
| **2NF**   | Loại bỏ phụ thuộc một phần vào khóa chính (các cột không khóa phải phụ thuộc hoàn toàn vào khóa chính).                             |
| **3NF**   | Loại bỏ phụ thuộc bắc cầu (các cột không khóa chỉ phụ thuộc trực tiếp vào khóa chính, không phụ thuộc vào các cột không khóa khác). |

---

## **Lợi Ích của Chuẩn Hóa**

1. **Giảm Dư Thừa Dữ Liệu:** Tiết kiệm dung lượng lưu trữ.
2. **Đảm Bảo Tính Toàn Vẹn:** Tránh lỗi đồng bộ khi dữ liệu được thay đổi.
3. **Tăng Hiệu Quả Truy Vấn:** Giảm thiểu dữ liệu không cần thiết.
4. **Dễ Duy Trì và Mở Rộng:** Thay đổi hoặc thêm thông tin dễ dàng mà không phá vỡ cấu trúc hiện tại.

