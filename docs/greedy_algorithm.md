## Thuật Toán Tham Lam (Greedy Algorithm)

**Khái niệm:**

Thuật toán tham lam là một kỹ thuật giải quyết vấn đề bằng cách lựa chọn giải pháp tốt nhất tại mỗi bước, với hy vọng rằng những lựa chọn tốt nhất tại từng bước sẽ dẫn đến giải pháp tốt nhất chung.

**Ứng dụng:** Thuật toán tham lam được sử dụng rộng rãi trong nhiều lĩnh vực, bao gồm:

- **Tối ưu hóa:** Tìm kiếm giải pháp tốt nhất cho một bài toán, ví dụ: tìm đường đi ngắn nhất, sắp xếp công việc, quản lý kho hàng.
- **Phân bổ tài nguyên:** Phân bổ tài nguyên hiệu quả nhất, ví dụ: phân bổ băng thông mạng, phân bổ thời gian máy tính.
- **Lựa chọn:** Tìm tập hợp con tốt nhất từ một tập hợp lớn, ví dụ: chọn sản phẩm tối ưu, chọn nhân viên phù hợp.

**Ưu điểm:**

- **Dễ hiểu và triển khai:** Thuật toán tham lam thường dễ hiểu và dễ triển khai hơn so với các phương pháp khác.
- **Hiệu quả:** Greedy Algorithm thường chạy nhanh hơn các thuật toán khác, đặc biệt là khi số lượng dữ liệu lớn.

**Nhược điểm:**

- **Không đảm bảo tối ưu:** Thuật toán tham lam không đảm bảo tìm ra giải pháp tốt nhất cho tất cả các vấn đề. Nó có thể dẫn đến giải pháp cục bộ tối ưu thay vì giải pháp toàn cục tối ưu.
- **Phụ thuộc vào việc lựa chọn:** Kết quả của thuật toán tham lam phụ thuộc vào cách lựa chọn tại mỗi bước.

**Ví dụ:**

**Bài toán tìm đường đi ngắn nhất:** Thuật toán tham lam có thể được sử dụng để tìm đường đi ngắn nhất từ điểm A đến điểm B. Tại mỗi bước, thuật toán sẽ lựa chọn đường đi ngắn nhất từ điểm hiện tại đến điểm tiếp theo.

**Bài toán sắp xếp công việc:** Thuật toán tham lam có thể được sử dụng để sắp xếp công việc để tối ưu hóa thời gian hoàn thành. Thuật toán sẽ lựa chọn công việc có thời gian hoàn thành ngắn nhất trước tiên.

**Minh họa với bài toán ba lô:**

**Bài toán:** Cho một ba lô có trọng lượng tối đa là W và một tập hợp các đồ vật, mỗi đồ vật có trọng lượng và giá trị tương ứng. Yêu cầu tìm cách chọn các đồ vật để đưa vào ba lô sao cho tổng giá trị của các đồ vật được chọn là lớn nhất, đồng thời tổng trọng lượng không vượt quá trọng lượng tối đa của ba lô.

**Thuật toán tham lam:**

1. **Tính đơn giá cho mỗi đồ vật:** Chia giá trị của mỗi đồ vật cho trọng lượng của nó để có được đơn giá.
2. **Sắp xếp các đồ vật theo thứ tự đơn giá giảm dần:** Đặt các đồ vật có đơn giá cao nhất lên đầu danh sách.
3. **Chọn các đồ vật theo thứ tự ưu tiên:** Bắt đầu từ đồ vật có đơn giá cao nhất, lần lượt chọn đồ vật cho vào ba lô cho đến khi trọng lượng còn lại trong ba lô không đủ để thêm đồ vật tiếp theo.

**Ví dụ:**

Ba lô có trọng lượng tối đa là 37, và 4 loại đồ vật với trọng lượng và giá trị tương ứng:

| Loại đồ vật | Trọng lượng | Giá trị | Đơn giá |
| ----------- | ----------- | ------- | ------- |
| A           | 15          | 30      | 2       |
| B           | 10          | 25      | 2.5     |
| C           | 2           | 2       | 1       |
| D           | 4           | 6       | 1.5     |

**Bước 1:** Tính đơn giá cho mỗi đồ vật.

**Bước 2:** Sắp xếp các đồ vật theo thứ tự đơn giá giảm dần: B, A, D, C.

**Bước 3:** Chọn các đồ vật:

- Chọn 3 vật loại B (vì trọng lượng mỗi vật là 10 và ba lô có trọng lượng 37, ta chọn được tối đa 3 vật). Trọng lượng còn lại là 37 - 30 = 7.
- Không thể chọn vật A vì trọng lượng của nó là 15, trong khi trọng lượng còn lại của ba lô là 7.
- Chọn 1 vật loại D. Trọng lượng còn lại là 7 - 4 = 3.
- Chọn 1 vật loại C. Trọng lượng còn lại là 3 - 2 = 1.

**Kết quả:**

Chúng ta đã chọn 3 cái loại B, một cái loại D và 1 cái loại C. Tổng trọng lương là 30 + 4 + 2 = 36 và tổng giá trị là 75 + 6 + 2 = 83.
