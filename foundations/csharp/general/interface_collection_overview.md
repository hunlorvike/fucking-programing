# Tài liệu Về Các Interface Collection Trong .NET

## Mục Lục

1. [Namespace `System.Collections`](#1-namespace-systemcollections)

   - [ICollection](#-icollection)
   - [IEnumerable](#-ienumerable)
   - [IEnumerator](#-ienumerator)
   - [IList](#-ilist)
   - [IDictionary](#-idictionary)
   - [IQueue](#-iqueue)
   - [IStack](#-istack)

2. [Namespace `System.Collections.Generic`](#2-namespace-systemcollectionsgeneric)

   - [ICollection<T>](#-icollectiont)
   - [IEnumerable<T>](#-ienumerablet)
   - [IEnumerator<T>](#-ienumeratort)
   - [IList<T>](#-ilistt)
   - [IDictionary<TKey, TValue>](#-idictionarytkey-tvalue)
   - [ISet<T>](#-iset)

3. [Namespace `System.Collections.Concurrent`](#3-namespace-systemcollectionsconcurrent)

   - [IProducerConsumerCollection<T>](#-iproducerconsumercollectiont)
   - [IBlockingCollection<T>](#-iblockingcollectiont)

4. [Namespace `System.Collections.Specialized`](#4-namespace-systemcollectionsspecialized)

   - [INotifyCollectionChanged](#-inotifycollectionchanged)
   - [INotifyPropertyChanged](#-inotifypropertychanged)

5. [Tổng Kết Lựa Chọn Interface Collection Phù Hợp](#5-tong-ket-lua-chon-interface-collection-phu-hop)

6. [So Sánh Các Interface Collection](#6-so-sanh-cac-interface-collection)

7. [Khi Nào Sử Dụng Interface Nào?](#7-khi-nao-su-dung-interface-nao)

8. [Ví Dụ Cụ Thể về Tình Huống Sử Dụng](#8-vi-du-cu-the-ve-tinh-huong-su-dung)

---

## 1. Namespace `System.Collections`

`System.Collections` cung cấp các interface cho các collection không generic. Những interface này giúp quản lý các tập hợp đối tượng nhưng không bảo đảm an toàn về kiểu dữ liệu, có thể gây ra lỗi khi làm việc với các kiểu khác nhau.

### **ICollection**

- **Mô tả**: Đại diện cho một tập hợp các đối tượng có thể đếm được. Cho phép thêm, xóa, và kiểm tra sự tồn tại của các phần tử trong tập hợp.
- **Phương thức chính**:
  - `Add`: Thêm một phần tử vào collection.
  - `Remove`: Xóa một phần tử khỏi collection.
  - `Contains`: Kiểm tra sự tồn tại của một phần tử.
  - `Clear`: Xóa tất cả các phần tử trong collection.
- **Ví dụ**:
  ```csharp
  ICollection collection = new ArrayList();
  collection.Add("Hello");
  collection.Add(123);
  Console.WriteLine(collection.Count); // Kết quả: 2
  ```

### **IEnumerable**

- **Mô tả**: Cung cấp một phương thức để duyệt qua các đối tượng trong một collection mà không cần biết loại collection cụ thể.
- **Phương thức chính**:
  - `GetEnumerator`: Trả về một enumerator cho phép duyệt qua collection.
- **Ví dụ**:
  ```csharp
  IEnumerable enumerable = new ArrayList() { "Apple", "Banana" };
  foreach (var item in enumerable)
  {
      Console.WriteLine(item); // Kết quả: Apple, Banana
  }
  ```

### **IEnumerator**

- **Mô tả**: Cung cấp các phương thức để duyệt qua các phần tử trong collection. Phân biệt giữa vị trí của các phần tử và cho phép truy cập phần tử hiện tại.
- **Phương thức chính**:
  - `MoveNext`: Di chuyển đến phần tử tiếp theo trong collection.
  - `Reset`: Đặt lại enumerator về vị trí đầu.
  - `Current`: Lấy phần tử hiện tại.
- **Ví dụ**:
  ```csharp
  IEnumerator enumerator = new ArrayList() { "One", "Two", "Three" }.GetEnumerator();
  while (enumerator.MoveNext())
  {
      Console.WriteLine(enumerator.Current); // Kết quả: One, Two, Three
  }
  ```

### **IList**

- **Mô tả**: Mở rộng từ `ICollection`, đại diện cho một danh sách có thể truy cập các phần tử theo chỉ số. Hỗ trợ các thao tác thêm, xóa, và truy cập bằng chỉ số.
- **Phương thức chính**:
  - `Insert`: Chèn một phần tử tại chỉ số chỉ định.
  - `RemoveAt`: Xóa phần tử tại chỉ số chỉ định.
  - `this[int index]`: Truy cập phần tử tại chỉ số.
- **Ví dụ**:
  ```csharp
  IList list = new ArrayList() { "First", "Second" };
  Console.WriteLine(list[1]); // Kết quả: Second
  ```

### **IDictionary**

- **Mô tả**: Đại diện cho một collection các cặp khóa-giá trị, trong đó mỗi khóa là duy nhất. Hỗ trợ việc truy cập giá trị thông qua khóa.
- **Phương thức chính**:
  - `Add`: Thêm một cặp khóa-giá trị.
  - `Remove`: Xóa cặp khóa-giá trị bằng khóa.
  - `ContainsKey`: Kiểm tra sự tồn tại của một khóa.
  - `this[object key]`: Truy cập giá trị theo khóa.
- **Ví dụ**:
  ```csharp
  IDictionary dictionary = new Hashtable();
  dictionary["key1"] = "value1";
  Console.WriteLine(dictionary["key1"]); // Kết quả: value1
  ```

### **IQueue**

- **Mô tả**: Mặc dù không có interface chính thức cho hàng đợi, bạn có thể sử dụng `Queue` để quản lý các phần tử theo nguyên tắc FIFO (First In, First Out).
- **Phương thức chính**:
  - `Enqueue`: Thêm một phần tử vào cuối hàng đợi.
  - `Dequeue`: Xóa và trả về phần tử ở đầu hàng đợi.
- **Ví dụ**:
  ```csharp
  Queue queue = new Queue();
  queue.Enqueue("First");
  Console.WriteLine(queue.Dequeue()); // Kết quả: First
  ```

### **IStack**

- **Mô tả**: Tương tự như hàng đợi, không có interface cụ thể cho ngăn xếp nhưng `Stack` có thể được sử dụng để quản lý các phần tử theo nguyên tắc LIFO (Last In, First Out).
- **Phương thức chính**:
  - `Push`: Thêm một phần tử vào ngăn xếp.
  - `Pop`: Xóa và trả về phần tử ở đầu ngăn xếp.
- **Ví dụ**:
  ```csharp
  Stack stack = new Stack();
  stack.Push("First");
  Console.WriteLine(stack.Pop()); // Kết quả: First
  ```

---

## 2. Namespace `System.Collections.Generic`

`System.Collections.Generic` cung cấp các interface cho các collection generic, cho phép xác định kiểu dữ liệu cụ thể, tăng tính an toàn về kiểu và hiệu suất khi làm việc với các collection.

### **ICollection<T>**

- **Mô tả**: Tương tự như `ICollection`, nhưng với kiểu dữ liệu cụ thể `T`. Cho phép thêm, xóa và kiểm tra sự tồn tại của các phần tử.
- **Phương thức chính**: Tương tự như `ICollection`.
- **Ví dụ**:
  ```csharp
  ICollection<string> collection = new List<string>();
  collection.Add("Apple");
  Console.WriteLine(collection.Count); // Kết quả: 1
  ```

### **IEnumerable<T>**

- **Mô tả**: Cung cấp một phương thức để duyệt qua các đối tượng kiểu `T`. Cho phép truy cập vào từng phần tử trong collection theo kiểu an toàn.
- **Phương thức chính**: Tương tự như `IEnumerable`.
- **Ví dụ**:
  ```csharp
  IEnumerable<string> enumerable = new List<string> { "Apple", "Banana" };
  foreach (var item in enumerable)
  {
      Console.WriteLine(item); // Kết quả: Apple, Banana
  }
  ```

### **IEnumerator<T>**

- **Mô tả**: Cung cấp các phương thức để duyệt qua các phần tử trong collection kiểu `T`, cho phép truy cập phần tử hiện tại và di chuyển qua các phần tử.
- **Phương thức chính**: Tương tự như `IEnumerator`.
- **Ví dụ**:
  ```csharp
  IEnumerator<string> enumerator = new List<string> { "One", "Two", "Three" }.GetEnumerator();
  while (enumerator.MoveNext())
  {
      Console.WriteLine(enumerator.Current); // Kết quả: One, Two, Three
  }
  ```

### **IList<T>**

- **Mô tả**: Mở rộng từ `ICollection<T>`, đại diện cho một danh sách cho phép truy cập các phần tử theo chỉ số với kiểu dữ liệu cụ thể.
- **Phương thức chính**: Tương tự như `IList`.
- \*\*

Ví dụ\*\*:

```csharp
IList<string> list = new List<string> { "First", "Second" };
Console.WriteLine(list[1]); // Kết quả: Second
```

### **IDictionary<TKey, TValue>**

- **Mô tả**: Đại diện cho một collection các cặp khóa-giá trị với kiểu dữ liệu cụ thể cho cả khóa và giá trị.
- **Phương thức chính**: Tương tự như `IDictionary`.
- **Ví dụ**:
  ```csharp
  IDictionary<string, string> dictionary = new Dictionary<string, string>();
  dictionary["key1"] = "value1";
  Console.WriteLine(dictionary["key1"]); // Kết quả: value1
  ```

### **ISet<T>**

- **Mô tả**: Đại diện cho một collection các phần tử duy nhất (không trùng lặp) với kiểu dữ liệu cụ thể.
- **Phương thức chính**:
  - `Add`: Thêm phần tử (nếu chưa tồn tại).
  - `Remove`: Xóa phần tử.
  - `Contains`: Kiểm tra sự tồn tại của phần tử.
- **Ví dụ**:
  ```csharp
  ISet<string> set = new HashSet<string>();
  set.Add("Apple");
  set.Add("Apple"); // Không thêm vì trùng lặp
  Console.WriteLine(set.Count); // Kết quả: 1
  ```

---

## 3. Namespace `System.Collections.Concurrent`

`System.Collections.Concurrent` cung cấp các collection được tối ưu hóa cho việc sử dụng trong môi trường đa luồng.

### **IProducerConsumerCollection<T>**

- **Mô tả**: Cung cấp một phương thức để thêm và lấy phần tử một cách an toàn trong môi trường đa luồng.
- **Phương thức chính**: `TryAdd`, `TryTake`, v.v.
- **Ví dụ**:
  ```csharp
  IProducerConsumerCollection<string> collection = new ConcurrentQueue<string>();
  collection.TryAdd("item1");
  string item;
  collection.TryTake(out item);
  ```

### **IBlockingCollection<T>**

- **Mô tả**: Cho phép thêm và lấy phần tử từ collection, với khả năng chặn khi collection rỗng hoặc đầy.
- **Phương thức chính**: `Add`, `Take`, `TryAdd`, `TryTake`.
- **Ví dụ**:
  ```csharp
  BlockingCollection<string> collection = new BlockingCollection<string>();
  collection.Add("item1");
  string item = collection.Take(); // Chờ cho đến khi có phần tử
  ```

---

## 4. Namespace `System.Collections.Specialized`

`System.Collections.Specialized` cung cấp các collection bổ sung có tính năng đặc biệt hơn cho các tình huống cụ thể.

### **INotifyCollectionChanged**

- **Mô tả**: Cung cấp sự kiện thông báo khi một collection thay đổi, hỗ trợ cho việc binding dữ liệu trong các ứng dụng WPF hoặc UWP.
- **Sự kiện chính**: `CollectionChanged`.
- **Ví dụ**:
  ```csharp
  ObservableCollection<string> collection = new ObservableCollection<string>();
  collection.CollectionChanged += (s, e) => {
      Console.WriteLine("Collection changed");
  };
  collection.Add("New item"); // Gây ra sự kiện
  ```

### **INotifyPropertyChanged**

- **Mô tả**: Cung cấp sự kiện thông báo khi một thuộc tính của đối tượng thay đổi.
- **Sự kiện chính**: `PropertyChanged`.
- **Ví dụ**:

  ```csharp
  public class Person : INotifyPropertyChanged
  {
      private string name;
      public string Name
      {
          get => name;
          set
          {
              name = value;
              OnPropertyChanged(nameof(Name));
          }
      }

      public event PropertyChangedEventHandler PropertyChanged;
      protected void OnPropertyChanged(string propertyName) => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
  }
  ```

---

## 5. Tổng Kết Lựa Chọn Interface Collection Phù Hợp

- **Dùng `ICollection`** khi bạn cần một collection có thể đếm được, nhưng không quan tâm đến loại kiểu dữ liệu.
- **Dùng `IEnumerable`** khi bạn chỉ cần duyệt qua collection mà không cần chỉnh sửa.
- **Dùng `IList`** khi bạn cần truy cập theo chỉ số và hỗ trợ thêm/xóa phần tử.
- **Dùng `IDictionary`** khi cần một collection các cặp khóa-giá trị.
- **Dùng `ISet`** khi bạn cần một collection không chứa phần tử trùng lặp.
- **Dùng `Concurrent`** khi làm việc với nhiều luồng.
- **Dùng `INotifyCollectionChanged`** cho binding dữ liệu trong WPF/UWP.

---

## 6. So Sánh Các Interface Collection

| Interface                 | Tính Chất                                         | Kiểu Dữ Liệu  |
| ------------------------- | ------------------------------------------------- | ------------- |
| ICollection               | Tập hợp các đối tượng có thể đếm được             | Không generic |
| IEnumerable               | Duyệt qua các đối tượng                           | Không generic |
| IEnumerator               | Duyệt qua các phần tử trong collection            | Không generic |
| IList                     | Danh sách có thể truy cập theo chỉ số             | Không generic |
| IDictionary               | Collection các cặp khóa-giá trị                   | Không generic |
| ISet                      | Collection không chứa phần tử trùng lặp           | Không generic |
| ICollection<T>            | Tập hợp các đối tượng có thể đếm được (generic)   | Generic       |
| IEnumerable<T>            | Duyệt qua các đối tượng kiểu T (generic)          | Generic       |
| IEnumerator<T>            | Duyệt qua các phần tử kiểu T                      | Generic       |
| IList<T>                  | Danh sách có thể truy cập theo chỉ số (generic)   | Generic       |
| IDictionary<TKey, TValue> | Collection các cặp khóa-giá trị (generic)         | Generic       |
| ISet<T>                   | Collection không chứa phần tử trùng lặp (generic) | Generic       |

---

## 7. Khi Nào Sử Dụng Interface Nào?

- **Khi cần tính linh hoạt**: Sử dụng `IEnumerable` để duyệt mà không cần biết về kiểu dữ liệu.
- **Khi cần độ an toàn**: Sử dụng `ICollection<T>`, `IList<T>`, `IDictionary<TKey, TValue>` cho kiểu dữ liệu cụ thể.
- **Khi cần thao tác đồng thời**: Sử dụng `Concurrent` collections để an toàn khi sử dụng nhiều luồng.
- **Khi cần thông báo thay đổi**: Sử dụng `INotifyCollectionChanged` trong WPF/UWP cho binding dữ liệu.

---

## 8. Ví Dụ Cụ Thể về Tình Huống Sử Dụng

### Tình huống 1: Quản lý danh sách sinh viên

```csharp
public class Student
{
    public string Name { get; set; }
    public int ID { get; set; }
}

List<Student> students = new List<Student>();
students.Add(new Student { Name = "John", ID = 1 });
```

### Tình huống 2: Lưu trữ cấu hình ứng dụng

```csharp
Dictionary<string, string> config = new Dictionary<string, string>();
config["Theme"] = "Dark";
config["FontSize"] = "12";
```

### Tình huống 3: Tạo hàng đợi xử lý công việc

```csharp
BlockingCollection<string> jobs = new BlockingCollection<string>();
jobs.Add("Job1");
string job = jobs.Take(); // Chờ cho đến khi có công việc
```

### Tình huống 4: Theo dõi thay đổi trong danh sách

```csharp
ObservableCollection<string> items = new ObservableCollection<string>();
items.CollectionChanged += (s, e) => { /* xử lý thay đổi */ };
items.Add("New item"); // Kích hoạt sự kiện
```
