## **🚀 "GIẢI MÃ" BẢNG BĂM (HASH TABLE): CẤU TRÚC DỮ LIỆU "TÌM NHANH" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một cấu trúc dữ liệu cực kỳ quan trọng và "bá đạo":
Bảng băm (Hash Table). Đây là một "vũ khí" bí mật giúp bạn tìm kiếm và quản lý dữ liệu siêu nhanh. Cùng mình "mổ xẻ" nó
nhé!

### **I. BẢNG BĂM (HASH TABLE) LÀ GÌ?**

- **Bảng băm (Hash Table):** Là cấu trúc dữ liệu dùng "hàm băm" để ánh xạ dữ liệu sang các vị trí trong bộ nhớ, giúp tìm
  kiếm nhanh.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn tìm sách trong thư viện: bạn dùng "mã số" của sách để biết nó ở kệ nào, chứ không cần tìm từng
      cuốn một.
- **Đặc điểm:**
    - **Hàm băm:** Ánh xạ "khóa" (key) thành "vị trí" (hash value).
    - **Khóa - giá trị:** Lưu dữ liệu dưới dạng cặp "khóa - giá trị" (key-value).
    - **Truy cập nhanh:** Thường mất O(1) để tìm kiếm, thêm, xóa (nhưng có thể chậm trong trường hợp xấu).

### **II. CÁCH HOẠT ĐỘNG (TỪNG BƯỚC CHI TIẾT)**

1. **Hàm băm:**
    - Nhận "khóa" (key) đầu vào.
    - Trả về một số nguyên (hash value), đó là vị trí trong bảng.
2. **Lưu trữ:**
    - Dùng hash value làm vị trí lưu trữ dữ liệu.
    - Nếu có 2 khóa cùng hash value (xung đột), dùng các cách giải quyết (liên kết hoặc địa chỉ mở).
3. **Tìm kiếm:**
    - Dùng hash function để tính hash value từ "khóa" cần tìm.
    - Truy cập trực tiếp vào vị trí đó để lấy dữ liệu.

### **III. GIẢI QUYẾT XUNG ĐỘT (KHI CÓ NHIỀU "SÁCH" Ở CÙNG "KỆ")**

1. **Chaining (Liên kết):** Mỗi vị trí trong bảng là 1 danh sách liên kết, các phần tử trùng hash value sẽ cùng nằm
   trong danh sách này.
2. **Open Addressing (Địa chỉ mở):** Nếu vị trí đã đầy, sẽ tìm vị trí trống tiếp theo theo một quy luật nhất định.

### **IV. ƯU ĐIỂM CỦA BẢNG BĂM (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Truy cập nhanh:** Tìm kiếm, thêm, xóa thường nhanh (O(1)).
- **Truy cập ngẫu nhiên:** Phù hợp khi cần truy cập dữ liệu bằng khóa.

### **V. NHƯỢC ĐIỂM CỦA BẢNG BĂM (NHỮNG ĐIỂM "KHÓ CHỊU")**

- **Xung đột:** Có thể làm chậm nếu có quá nhiều xung đột.
- **Không duyệt tuần tự:** Không có thứ tự cho các phần tử, không duyệt được theo thứ tự.

### **VI. VÍ DỤ MINH HỌA - LƯU THÔNG TIN NGƯỜI DÙNG (C#)**

```csharp
using System;
using System.Collections.Generic;

public class HashTableExample
{
    public class HashTable<K, V>
        {
            private int size;
            private List<(K, V)>[] table;

            public HashTable(int size)
            {
                this.size = size;
                table = new List<(K, V)>[size];
                for(int i = 0; i < size; i++)
                {
                     table[i] = new List<(K, V)>();
                }

            }

              private int Hash(K key)
           {
              int hash = 0;
                string keyStr = key.ToString();
               for (int i = 0; i < keyStr.Length; i++)
                  {
                         hash = (hash << 5) - hash + keyStr[i];
                            hash |= 0;
                   }
              return Math.Abs(hash) % size;
             }


             // Thêm cặp key-value vào bảng băm
             public void Put(K key, V value)
             {
                int index = Hash(key);
                List<(K, V)> bucket = table[index];
                foreach (var item in bucket)
                {
                     if(item.Item1.Equals(key))
                     {
                        bucket.Remove(item);
                        break;
                     }

                 }
              bucket.Add((key,value));

             }

            // Lấy giá trị từ bảng băm
             public V Get(K key)
            {
               int index = Hash(key);
                List<(K, V)> bucket = table[index];
                foreach(var item in bucket)
                {
                     if(item.Item1.Equals(key))
                     {
                           return item.Item2;
                     }
                }
               return default(V);
            }

               // Xóa một khóa khỏi bảng băm
            public bool Delete(K key)
            {
                 int index = Hash(key);
                 List<(K,V)> bucket = table[index];
                 for (int i = 0; i < bucket.Count; i++)
                     {
                            if(bucket[i].Item1.Equals(key))
                            {
                                bucket.RemoveAt(i);
                                return true;
                            }
                     }
                 return false;
             }

        }
    public static void Main(string[] args)
    {
         HashTable<string, string> hashTable = new HashTable<string, string>(10);
            hashTable.Put("name", "John");
            hashTable.Put("age", "30");

             Console.WriteLine("Tên: " + hashTable.Get("name")); // Output: Tên: John
            Console.WriteLine("Tuổi: " + hashTable.Get("age")); // Output: Tuổi: 30

            hashTable.Delete("name");
             Console.WriteLine("Tên: " + hashTable.Get("name"));  // Output: Tên:
        }
}
```

**Giải thích:**

- **`HashTable<K, V>`:** Class dùng generic để có thể chứa nhiều kiểu dữ liệu.
- **`table`:** Mảng chứa các danh sách liên kết (dùng List để làm danh sách liên kết)
- **`Hash(K key)`:** Hàm băm để tính index từ key
- **`Put(K key, V value)`:** Thêm cặp key-value vào bảng băm
- **`Get(K key)`:** Tìm và trả về value dựa vào key.
- **`Delete(K key)`:** Xóa key-value dựa vào key.

### **VII. ỨNG DỤNG CỦA BẢNG BĂM (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Tìm kiếm nhanh:** Tìm kiếm các phần tử nhanh chóng (từ điển, cơ sở dữ liệu).
- **Bảng tra cứu:** Dùng để tra cứu dữ liệu dựa trên khóa.
- **Bộ nhớ cache:** Quản lý các dữ liệu thường dùng để truy cập nhanh.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Bảng băm là một cấu trúc dữ liệu cực kỳ quan trọng, giúp bạn tìm kiếm, thêm, xóa dữ liệu một cách nhanh chóng. Hy vọng
qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
