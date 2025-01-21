## **🚀 "GIẢI MÃ" DANH SÁCH LIÊN KẾT (LINKED LIST): CẤU TRÚC DỮ LIỆU DẺO DAI CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một cấu trúc dữ liệu cực kỳ linh hoạt: Danh sách liên kết (Linked List). Đây là một "người bạn" rất quan trọng khi bạn cần quản lý dữ liệu động. Cùng mình "mổ xẻ" nó nhé!

### **I. DANH SÁCH LIÊN KẾT (LINKED LIST) LÀ GÌ?**

*   **Danh sách liên kết (Linked List):** Là một chuỗi các "nút" (node), mỗi nút chứa dữ liệu và một con trỏ (pointer) đến nút tiếp theo.
*   **Nó hoạt động như thế nào?**
    *   Giống như một đoàn tàu: mỗi toa tàu có dữ liệu và liên kết với toa tiếp theo.
*   **Ưu điểm:**
    *   **Linh hoạt:** Dễ thêm/xóa phần tử ở bất kỳ đâu.
    *   **Kích thước động:** Không cần xác định trước kích thước.
*   **Nhược điểm:**
    *   **Truy cập chậm:** Để đến một phần tử, cần phải đi theo các con trỏ.
    *   **Tốn bộ nhớ:** Cần thêm bộ nhớ để lưu con trỏ.

### **II. CÁC LOẠI DANH SÁCH LIÊN KẾT (MỖI LOẠI MỘT VẺ)**

1.  **Danh sách liên kết đơn (Singly Linked List):** Mỗi nút có 1 con trỏ đến nút tiếp theo.
2.  **Danh sách liên kết đôi (Doubly Linked List):** Mỗi nút có 2 con trỏ: 1 trỏ đến nút trước và 1 trỏ đến nút sau.

### **III. CÀI ĐẶT DANH SÁCH LIÊN KẾT ĐƠN (C#)**

```csharp
public class Node
{
    public int data;
    public Node next;

    public Node(int data)
    {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList
{
    public Node head;

    public LinkedList()
    {
        head = null;
    }

    public void Append(int data)
    {
        Node newNode = new Node(data);
        if (head == null)
        {
            head = newNode;
            return;
        }
        Node lastNode = head;
        while (lastNode.next != null)
        {
            lastNode = lastNode.next;
        }
        lastNode.next = newNode;
    }

      public void PrintList()
      {
          Node current = head;
          while(current != null)
          {
                Console.Write(current.data + " ");
                current = current.next;
          }
      }
}

public class Example
{
    public static void Main(string[] args)
    {
         LinkedList list = new LinkedList();
         list.Append(1);
         list.Append(2);
         list.Append(3);
         list.PrintList(); // Output: 1 2 3
    }
}
```

**Giải thích:**

*   **`Node`:** Lớp biểu diễn một nút, chứa data và `next` (con trỏ tới nút sau).
*   **`LinkedList`:** Lớp biểu diễn danh sách liên kết, có `head` (con trỏ tới nút đầu).
    *   **`Append(data)`:** Thêm nút mới vào cuối danh sách.
    *    **`PrintList()`:** In các phần tử trong danh sách.

### **IV. CÁC THAO TÁC TRÊN DANH SÁCH LIÊN KẾT (NHỮNG GÌ CÓ THỂ LÀM)**

1.  **Chèn (Insert):** Thêm nút mới vào một vị trí.
2.  **Xóa (Delete):** Xóa một nút.
3.  **Tìm kiếm (Search):** Tìm nút có giá trị cho trước.

### **V. ƯU ĐIỂM CỦA DANH SÁCH LIÊN KẾT (NHỮNG ĐIỂM "ĐÁNG YÊU")**

*   **Linh hoạt:** Dễ dàng thêm/xóa nút ở bất kỳ đâu mà không cần di chuyển các nút khác.
*   **Kích thước động:** Không cần xác định trước kích thước, có thể mở rộng thoải mái.

### **VI. NHƯỢC ĐIỂM CỦA DANH SÁCH LIÊN KẾT (NHỮNG ĐIỂM "KHÓ CHỊU")**

*   **Truy cập chậm:** Để đến một nút, cần phải đi qua các nút trước đó (không truy cập trực tiếp bằng index như mảng).
*   **Tốn bộ nhớ:** Mỗi nút cần thêm bộ nhớ để lưu con trỏ.

### **VII. ỨNG DỤNG CỦA DANH SÁCH LIÊN KẾT (ĐƯỢC DÙNG Ở ĐÂU?)**

*   **Quản lý bộ nhớ:** Theo dõi các vùng nhớ trống.
*   **Xử lý dữ liệu:** Sắp xếp, tìm kiếm, duyệt dữ liệu.
*   **Nền tảng:** Xây các cấu trúc khác (stack, queue, graph).

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Danh sách liên kết là một cấu trúc dữ liệu linh hoạt, giúp bạn quản lý dữ liệu động một cách hiệu quả. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó. Chúc các bạn code thành công! 😎
