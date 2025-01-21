## **🚀 "GIẢI MÃ" CON TRỎ VÀ QUẢN LÝ BỘ NHỚ: "SỨC MẠNH" VÀ "NGUY HIỂM" CHO DÂN CODE C/C++ 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một chủ đề cực kỳ quan trọng và cũng khá "khoai" trong
C/C++: Con trỏ (Pointers) và Quản lý Bộ nhớ (Memory Management). Đây là những "vũ khí" mạnh mẽ nhưng nếu không cẩn thận
thì dễ "tẩu hỏa nhập ma" lắm đấy. Cùng mình "mổ xẻ" nó nhé!

### **I. CON TRỎ LÀ GÌ? (NHƯ "SỐ NHÀ" TRONG MÁY TÍNH)**

- **Con trỏ (Pointer):** Là một biến đặc biệt, dùng để _lưu địa chỉ_ của một biến khác trong bộ nhớ.
- **Nó hoạt động như thế nào?**
    - Giống như "số nhà": con trỏ cho bạn biết "nhà" của dữ liệu ở đâu.
- **Đặc điểm:**
    - Lưu địa chỉ bộ nhớ (không phải giá trị trực tiếp).
    - Cho phép truy cập, thay đổi dữ liệu gián tiếp.
    - Là "công cụ" mạnh mẽ, nhưng cũng dễ gây lỗi.

### **II. CÁC LOẠI CON TRỎ (MỖI LOẠI MỘT VẺ)**

1. **Con trỏ cơ bản:** Trỏ đến địa chỉ của biến thông thường.

   ```c
   int a = 5;
   int *p = &a; // p trỏ đến a
   ```

2. **Con trỏ NULL:** Không trỏ đến đâu cả (như kiểu địa chỉ "ma"), dùng khi chưa gán địa chỉ.

   ```c
   int *p = NULL; // p chưa trỏ đến đâu
   ```

3. **Con trỏ void:** Trỏ đến bất kỳ kiểu dữ liệu nào (như kiểu "địa chỉ đa năng").

   ```c
   void *p;
   int a = 10;
   p = &a; // p trỏ đến int a
   ```

4. **Con trỏ hàm:** Trỏ đến địa chỉ của một hàm (dùng để gọi hàm linh hoạt).

   ```c
   int add(int a, int b) { return a + b; }
   int (*func_ptr)(int, int) = &add; // con trỏ trỏ đến hàm add
   ```

5. **Con trỏ đa cấp:** Trỏ đến con trỏ khác (như kiểu địa chỉ của địa chỉ).

   ```c
   int a = 5;
   int *p = &a;  // p trỏ đến a
   int **pp = &p; // pp trỏ đến p
   ```

6. **Con trỏ hằng:** Địa chỉ không thể thay đổi.

   ```c
   int a = 10;
   int * const p = &a; // p trỏ đến a nhưng địa chỉ của p không thể đổi
   ```

7. **Hằng con trỏ:** Giá trị trỏ đến không thể thay đổi.

   ```c
   int a = 10;
   const int *p = &a; // p trỏ đến int a nhưng giá trị tại địa chỉ mà p trỏ đến không thể đổi qua con trỏ p
   ```

### **III. QUẢN LÝ BỘ NHỚ ĐỘNG (CẤP PHÁT VÀ GIẢI PHÓNG)**

1. **Cấp phát động:** Dùng `malloc`, `calloc`, hoặc `new` (cấp phát bộ nhớ khi chạy chương trình).
2. **Giải phóng:** Dùng `free` (cho `malloc`/`calloc`) hoặc `delete` (cho `new`) để trả bộ nhớ cho hệ thống khi không
   dùng nữa.

```c
#include <stdlib.h> // để có thể sử dụng malloc và free

 int main() {
     int *arr = (int *)malloc(5 * sizeof(int)); // Cấp phát 5 ô nhớ kiểu int
         if (arr == NULL)
         {
           printf("Không đủ bộ nhớ\n");
            return 1;
        }
     arr[0] = 10; // gán giá trị
     printf("%d\n", arr[0]); // Output: 10
     free(arr); // Giải phóng bộ nhớ
     return 0;
 }
```

### **IV. LỖI HAY GẶP KHI DÙNG CON TRỎ (CỰC KỲ CẨN THẬN)**

1. **Dangling pointer:** Con trỏ trỏ đến vùng nhớ đã bị giải phóng.
2. **Memory leak:** Quên giải phóng bộ nhớ (làm bộ nhớ bị "rò rỉ").
3. **Double free:** Giải phóng bộ nhớ 2 lần (gây lỗi).

   ```c
   int *ptr = (int *)malloc(sizeof(int));
   free(ptr);
   *ptr = 10; // Dangling pointer (lỗi!)
   ```

### **V. CON TRỎ VÀ HÀM (THAM CHIẾU)**

1. **Truyền tham chiếu:** Dùng con trỏ để thay đổi trực tiếp giá trị biến gốc trong hàm.

   ```c
    void changeValue(int *p) {
       *p = 20;
    }
    int main() {
       int a = 10;
       changeValue(&a);  // Truyền địa chỉ của a
       printf("%d\n", a); // Output: 20
       return 0;
   }
   ```

2. **Trả về con trỏ:** Hàm trả về con trỏ (nhớ cấp phát bộ nhớ động hoặc địa chỉ biến tồn tại).

   ```c
    int* createArray(int size) {
       return (int *)malloc(size * sizeof(int));
     }

     int main() {
       int *arr = createArray(5);
       arr[0] = 100;
       printf("%d\n", arr[0]);  // Output: 100
       free(arr);
       return 0;
    }
   ```

### **VI. SO SÁNH THAM TRỊ, THAM CHIẾU, CON TRỎ (HIỂU ĐỂ DÙNG ĐÚNG)**

| Tính chất        | Tham trị            | Tham chiếu             | Con trỏ              |
|------------------|---------------------|------------------------|----------------------|
| **Truyền**       | Bản sao của giá trị | Alias đến biến gốc     | Địa chỉ của biến     |
| **Thay đổi gốc** | Không               | Có                     | Có                   |
| **Linh hoạt**    | Thấp                | Cao                    | Cao                  |
| **Dùng cho hàm** | Thay đổi bản sao    | Truy cập trực tiếp gốc | Thao tác với địa chỉ |

### **VII. KẾT LUẬN (TỔNG KẾT)**

Con trỏ là "vũ khí" mạnh mẽ trong C/C++ giúp bạn kiểm soát bộ nhớ và tạo ra các cấu trúc dữ liệu linh hoạt. Tuy nhiên,
hãy dùng chúng cẩn thận để tránh các lỗi không đáng có. Chúc các bạn thành công! 😎
