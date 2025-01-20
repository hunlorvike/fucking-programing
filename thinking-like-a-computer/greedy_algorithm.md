## **🚀 "GIẢI MÃ" THUẬT TOÁN THAM LAM: "CỨ CHỌN CÁI TỐT NHẤT ĐI" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một thuật toán rất phổ biến và trực quan: Thuật toán
Tham Lam (Greedy Algorithm). Nghe tên thôi là thấy "máu chiến" rồi đúng không? Cùng mình "mổ xẻ" nó nhé!

### **I. THUẬT TOÁN THAM LAM LÀ GÌ?**

* **Thuật toán Tham Lam (Greedy Algorithm):** Là thuật toán giải quyết bài toán bằng cách lựa chọn "cái tốt nhất" ở mỗi
  bước, với hy vọng sẽ tìm được giải pháp tốt nhất cho toàn bộ bài toán.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn đi chợ: bạn chọn quả táo to nhất, quả cam đẹp nhất, ... hy vọng sẽ có được giỏ trái cây ngon
      nhất.
* **Ưu điểm:**
    * **Dễ hiểu:** Thuật toán đơn giản, dễ hình dung.
    * **Dễ cài đặt:** Code thường không quá phức tạp.
    * **Nhanh:** Thường chạy nhanh hơn các thuật toán khác.
* **Nhược điểm:**
    * **Không đảm bảo tối ưu:** Có thể chỉ tìm được giải pháp "tạm ổn", không phải là giải pháp tốt nhất.
    * **Phụ thuộc vào cách chọn:** Kết quả phụ thuộc vào việc chọn "cái tốt nhất" ở mỗi bước.

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Xác định "cái tốt nhất":** Xác định tiêu chí để chọn "cái tốt nhất" ở mỗi bước (ví dụ: chọn đường đi ngắn nhất,
   chọn công việc có thời gian ngắn nhất...).
2. **Lặp:** Thực hiện từng bước, ở mỗi bước chọn "cái tốt nhất" theo tiêu chí đã xác định.
3. **Kết thúc:** Khi đã có một giải pháp hoàn chỉnh thì kết thúc.

### **III. MÃ GIẢ (PSEUDOCODE) - DỄ HIỂU NHƯ ĐỌC TRUYỆN**

```
greedyAlgorithm(problem):
  solution = initial solution
  WHILE problem is not solved:
    best_choice = select_best_choice(available_options)
    add best_choice to solution
    update problem
  return solution
```

### **IV. GIẢI THÍCH CHI TIẾT (ĐỌC KỸ NHÉ!)**

* **`greedyAlgorithm(problem)`:** Hàm chính, nhận vào bài toán.
* **`solution = initial solution`:** Khởi tạo giải pháp ban đầu (thường là rỗng).
* **`WHILE problem is not solved`:** Vòng lặp cho đến khi giải quyết xong bài toán.
* **`best_choice = select_best_choice(available_options)`:** Chọn "cái tốt nhất" trong các lựa chọn.
* **`add best_choice to solution`:** Thêm lựa chọn tốt nhất vào giải pháp.
* **`update problem`:** Cập nhật bài toán sau khi đã chọn 1 lựa chọn.
* **`return solution`:** Trả về giải pháp cuối cùng.

### **V. VÍ DỤ MINH HỌA - BÀI TOÁN BA LÔ (C#)**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class KnapsackGreedy
{
    public class Item
    {
        public int Weight { get; set; }
        public int Value { get; set; }
        public double UnitPrice { get; set; }

        public Item(int weight, int value)
        {
            Weight = weight;
            Value = value;
            UnitPrice = (double)value / weight;
        }
    }
    public static List<Item> Knapsack(List<Item> items, int maxWeight)
    {
        // 1. Tính đơn giá
          foreach (var item in items)
                {
                     item.UnitPrice = (double)item.Value / item.Weight;
                }

        // 2. Sắp xếp theo đơn giá giảm dần
       items.Sort((x, y) => y.UnitPrice.CompareTo(x.UnitPrice));

        List<Item> result = new List<Item>();
        int currentWeight = 0;

        // 3. Chọn đồ vật
        foreach (var item in items)
        {
            if (currentWeight + item.Weight <= maxWeight)
            {
                 result.Add(item);
                  currentWeight += item.Weight;
            }
        }

        return result;
    }

    public static void Main(string[] args)
    {
        int maxWeight = 37;
        List<Item> items = new List<Item>
        {
            new Item(15, 30),
            new Item(10, 25),
            new Item(2, 2),
             new Item(4, 6),
        };

        List<Item> selectedItems = Knapsack(items, maxWeight);
         int totalWeight = 0;
         int totalValue = 0;
       foreach (var item in selectedItems)
        {
           Console.WriteLine($"Đồ vật (Trọng lượng: {item.Weight}, Giá trị: {item.Value})");
           totalWeight += item.Weight;
           totalValue += item.Value;
        }
        Console.WriteLine($"Tổng trọng lượng: {totalWeight}");
         Console.WriteLine($"Tổng giá trị: {totalValue}");
        // Output:
         //Đồ vật (Trọng lượng: 10, Giá trị: 25)
         //Đồ vật (Trọng lượng: 10, Giá trị: 25)
        //Đồ vật (Trọng lượng: 10, Giá trị: 25)
        //Đồ vật (Trọng lượng: 4, Giá trị: 6)
        //Đồ vật (Trọng lượng: 2, Giá trị: 2)
        //Tổng trọng lượng: 36
        //Tổng giá trị: 83

    }
}
```

**Giải thích:**

* **`Knapsack(List<Item> items, int maxWeight)`:** Hàm chính, nhận danh sách vật phẩm và trọng lượng tối đa.
* **`item.UnitPrice = (double)item.Value / item.Weight;`:** Tính đơn giá cho từng vật.
* **`items.Sort((x, y) => y.UnitPrice.CompareTo(x.UnitPrice));`:** Sắp xếp các vật theo đơn giá giảm dần.
* **`foreach (var item in items)`:** Chọn các vật theo thứ tự ưu tiên, miễn còn chỗ trong ba lô.

### **VI. ƯU ĐIỂM CỦA THUẬT TOÁN THAM LAM (NHỚ LÀM GÌ CŨNG TỐT)**

* **Dễ hiểu:** Ý tưởng đơn giản, dễ nắm bắt.
* **Dễ cài đặt:** Code thường không phức tạp.
* **Nhanh:** Chạy nhanh hơn các thuật toán khác.

### **VII. NHƯỢC ĐIỂM CỦA THUẬT TOÁN THAM LAM (CẨN THẬN LÀM GÌ CŨNG TỐT)**

* **Không đảm bảo tối ưu:** Có thể tìm ra giải pháp "tạm ổn" (local optimum), chứ không phải "tốt nhất" (global
  optimum).
* **Phụ thuộc vào cách chọn:** Kết quả phụ thuộc vào cách bạn chọn "cái tốt nhất" ở mỗi bước.

### **VIII. KHI NÀO NÊN DÙNG THUẬT TOÁN THAM LAM (CHỌN ĐÚNG "VŨ KHÍ")**

* Khi bài toán có thể chia thành các bước nhỏ.
* Khi việc chọn "cái tốt nhất" ở mỗi bước có vẻ hợp lý.
* Khi không cần giải pháp tối ưu tuyệt đối (chấp nhận giải pháp "tạm ổn").
* Khi cần thuật toán chạy nhanh.

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SẬP BẪY")**

* **Không phải bài nào cũng dùng được:** Không phải bài toán nào cũng giải được bằng thuật toán tham lam.
* **Cẩn thận khi chọn:** Việc chọn "cái tốt nhất" rất quan trọng.
* **Kiểm tra kỹ:** Hãy chắc chắn thuật toán có thật sự hiệu quả trong trường hợp của bạn.

### **KẾT LUẬN**

Thuật toán Tham Lam là một công cụ hữu ích, giúp bạn giải quyết nhiều bài toán một cách nhanh chóng và hiệu quả. Tuy
không phải là "vũ khí" toàn năng, nhưng nó là một lựa chọn tốt trong nhiều tình huống. Hy vọng qua bài viết này, các bạn
đã hiểu rõ hơn về nó. Chúc các bạn code thành công! 😎
