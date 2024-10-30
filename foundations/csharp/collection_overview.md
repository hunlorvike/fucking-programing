### 1. **Namespace `System.Collections`**

`System.Collections` chứa các collection không generic, chủ yếu phục vụ cho các ứng dụng .NET Framework cũ. Những collection này vẫn hữu ích trong một số tình huống nhất định, nhưng thiếu tính an toàn về kiểu dữ liệu so với các collection generic.

#### **Ví dụ về từng loại collection trong `System.Collections`**:

- **ArrayList**

  - **Mô tả**: Lưu trữ một danh sách các đối tượng có kích thước động.
  - **Ví dụ**:
    ```csharp
    ArrayList arrayList = new ArrayList();
    arrayList.Add("Hello");
    arrayList.Add(123);
    arrayList.Add(DateTime.Now);
    Console.WriteLine(arrayList[0]); // Kết quả: Hello
    ```

- **Hashtable**

  - **Mô tả**: Lưu trữ các cặp khóa-giá trị với khả năng truy cập nhanh qua khóa.
  - **Ví dụ**:
    ```csharp
    Hashtable hashtable = new Hashtable();
    hashtable["key1"] = "value1";
    hashtable["key2"] = "value2";
    Console.WriteLine(hashtable["key1"]); // Kết quả: value1
    ```

- **Queue**

  - **Mô tả**: Hàng đợi (FIFO - First In, First Out).
  - **Ví dụ**:
    ```csharp
    Queue queue = new Queue();
    queue.Enqueue("First");
    queue.Enqueue("Second");
    Console.WriteLine(queue.Dequeue()); // Kết quả: First
    ```

- **Stack**

  - **Mô tả**: Ngăn xếp (LIFO - Last In, First Out).
  - **Ví dụ**:
    ```csharp
    Stack stack = new Stack();
    stack.Push("First");
    stack.Push("Second");
    Console.WriteLine(stack.Pop()); // Kết quả: Second
    ```

- **SortedList**
  - **Mô tả**: Lưu trữ các cặp khóa-giá trị tự động sắp xếp theo khóa.
  - **Ví dụ**:
    ```csharp
    SortedList sortedList = new SortedList();
    sortedList.Add("key2", "value2");
    sortedList.Add("key1", "value1");
    Console.WriteLine(sortedList[0]); // Kết quả: value1
    ```

---

### 2. **Namespace `System.Collections.Generic`**

`System.Collections.Generic` chứa các collection generic, cho phép định nghĩa kiểu dữ liệu cụ thể (type-safe), giúp tối ưu hóa hiệu suất và tránh lỗi khi sử dụng sai kiểu dữ liệu.

#### **Ví dụ về từng loại collection trong `System.Collections.Generic`**:

- **List<T>**

  - **Mô tả**: Danh sách generic với kiểu dữ liệu cụ thể `T`.
  - **Ví dụ**:
    ```csharp
    List<string> list = new List<string>();
    list.Add("Apple");
    list.Add("Banana");
    Console.WriteLine(list[1]); // Kết quả: Banana
    ```

- **Dictionary<TKey, TValue>**

  - **Mô tả**: Lưu trữ các cặp khóa-giá trị với khóa là duy nhất.
  - **Ví dụ**:
    ```csharp
    Dictionary<int, string> dictionary = new Dictionary<int, string>();
    dictionary[1] = "One";
    dictionary[2] = "Two";
    Console.WriteLine(dictionary[2]); // Kết quả: Two
    ```

- **Queue<T>**

  - **Mô tả**: Hàng đợi generic theo FIFO.
  - **Ví dụ**:
    ```csharp
    Queue<int> queue = new Queue<int>();
    queue.Enqueue(1);
    queue.Enqueue(2);
    Console.WriteLine(queue.Dequeue()); // Kết quả: 1
    ```

- **Stack<T>**

  - **Mô tả**: Ngăn xếp generic theo LIFO.
  - **Ví dụ**:
    ```csharp
    Stack<string> stack = new Stack<string>();
    stack.Push("First");
    stack.Push("Second");
    Console.WriteLine(stack.Pop()); // Kết quả: Second
    ```

- **SortedList<TKey, TValue>**

  - **Mô tả**: Tương tự `Dictionary`, nhưng các phần tử được sắp xếp theo khóa.
  - **Ví dụ**:
    ```csharp
    SortedList<int, string> sortedList = new SortedList<int, string>();
    sortedList.Add(2, "Two");
    sortedList.Add(1, "One");
    Console.WriteLine(sortedList[1]); // Kết quả: One
    ```

- **HashSet<T>**

  - **Mô tả**: Tập hợp không chứa phần tử trùng lặp.
  - **Ví dụ**:
    ```csharp
    HashSet<string> hashSet = new HashSet<string>();
    hashSet.Add("Apple");
    hashSet.Add("Banana");
    hashSet.Add("Apple"); // Không thêm lại phần tử trùng
    Console.WriteLine(hashSet.Count); // Kết quả: 2
    ```

- **LinkedList<T>**

  - **Mô tả**: Danh sách liên kết hai chiều.
  - **Ví dụ**:
    ```csharp
    LinkedList<string> linkedList = new LinkedList<string>();
    linkedList.AddLast("First");
    linkedList.AddLast("Second");
    Console.WriteLine(linkedList.First.Value); // Kết quả: First
    ```

- **SortedDictionary<TKey, TValue>**
  - **Mô tả**: Tương tự `Dictionary` nhưng lưu trữ theo thứ tự sắp xếp của khóa.
  - **Ví dụ**:
    ```csharp
    SortedDictionary<string, int> sortedDict = new SortedDictionary<string, int>();
    sortedDict["B"] = 2;
    sortedDict["A"] = 1;
    Console.WriteLine(sortedDict.First().Value); // Kết quả: 1
    ```

---

### 3. **Namespace `System.Collections.Concurrent`**

Các collection trong `System.Collections.Concurrent` được thiết kế để đảm bảo an toàn khi thao tác trong môi trường đa luồng (thread-safe).

#### **Ví dụ về từng loại collection trong `System.Collections.Concurrent`**:

- **ConcurrentDictionary<TKey, TValue>**

  - **Mô tả**: Dictionary hỗ trợ thao tác an toàn trong môi trường đa luồng.
  - **Ví dụ**:
    ```csharp
    ConcurrentDictionary<int, string> concurrentDict = new ConcurrentDictionary<int, string>();
    concurrentDict.TryAdd(1, "One");
    Console.WriteLine(concurrentDict[1]); // Kết quả: One
    ```

- **BlockingCollection<T>**

  - **Mô tả**: Queue thread-safe hỗ trợ các thao tác đồng bộ hóa.
  - **Ví dụ**:
    ```csharp
    BlockingCollection<int> blockingCollection = new BlockingCollection<int>();
    blockingCollection.Add(1);
    Console.WriteLine(blockingCollection.Take()); // Kết quả: 1
    ```

- **ConcurrentQueue<T>**

  - **Mô tả**: Hàng đợi thread-safe.
  - **Ví dụ**:
    ```csharp
    ConcurrentQueue<string> concurrentQueue = new ConcurrentQueue<string>();
    concurrentQueue.Enqueue("First");
    concurrentQueue.Enqueue("Second");
    Console.WriteLine(concurrentQueue.TryDequeue(out string result) ? result : "Queue is empty"); // Kết quả: First
    ```

- **ConcurrentStack<T>**

  - **Mô tả**: Ngăn xếp thread-safe.
  - **Ví dụ**:
    ```csharp
    ConcurrentStack<string> concurrentStack = new ConcurrentStack<string>();
    concurrentStack.Push("First");
    concurrentStack.Push("Second");
    Console.WriteLine(concurrentStack.TryPop(out string popped) ? popped : "Stack is empty"); // Kết quả: Second
    ```

- **ConcurrentBag<T>**
  - **Mô tả**: Túi thread-safe, không có thứ tự cố định.
  - **Ví dụ**:
    ```csharp
    ConcurrentBag<int> bag = new ConcurrentBag<int>();
    bag.Add(1);
    bag.Add(2);
    Console.WriteLine(bag.Count); // Kết quả: 2
    ```

---

### 4. **Namespace `System.Collections.Specialized`**

Namespace `System.Collections.Specialized` cung cấp các collection đặc biệt, được thiết kế cho các trường hợp sử dụng chuyên biệt.

#### **Ví dụ về từng loại collection trong `System.Collections.Specialized`**:

- **NameValueCollection**
  - **Mô tả**: Lưu trữ các cặp tên-giá trị, cho phép nhiều giá trị cho một tên.
  - **Ví dụ**:

````csharp
   NameValueCollection nameValueCollection = new NameValueCollection();
   nameValueCollection.Add("key1", "value1");
   nameValueCollection.Add("key1", "value2");
   Console.WriteLine(nameValueCollection["key1"][0]); // Kết quả: value1
   ```

- **StringCollection**
 - **Mô tả**: Một danh sách chứa các chuỗi (string).
 - **Ví dụ**:
   ```csharp
   StringCollection stringCollection = new StringCollection();
   stringCollection.Add("Hello");
   stringCollection.Add("World");
   Console.WriteLine(stringCollection[1]); // Kết quả: World
   ```

- **StringDictionary**
 - **Mô tả**: Dictionary dành riêng cho các cặp khóa-giá trị là chuỗi.
 - **Ví dụ**:
   ```csharp
   StringDictionary stringDict = new StringDictionary();
   stringDict.Add("key1", "value1");
   Console.WriteLine(stringDict["key1"]); // Kết quả: value1
   ```

- **OrderedDictionary**
 - **Mô tả**: Dictionary có thứ tự.
 - **Ví dụ**:
   ```csharp
   OrderedDictionary orderedDict = new OrderedDictionary();
   orderedDict.Add("key1", "value1");
   orderedDict.Add("key2", "value2");
   Console.WriteLine(orderedDict[0]); // Kết quả: value1
   ```

- **HybridDictionary**
 - **Mô tả**: Dictionary linh hoạt, tự động chuyển đổi giữa `ListDictionary` và `Hashtable`.
 - **Ví dụ**:
   ```csharp
   HybridDictionary hybridDict = new HybridDictionary();
   hybridDict.Add("key1", "value1");
   Console.WriteLine(hybridDict["key1"]); // Kết quả: value1
   ```

---

### 5. **Namespace `System.Collections.Immutable`**

Namespace `System.Collections.Immutable` cung cấp các collection bất biến, giúp ngăn ngừa thay đổi dữ liệu sau khi khởi tạo, rất hữu ích trong các ứng dụng đa luồng.

#### **Ví dụ về từng loại collection trong `System.Collections.Immutable`**:

- **ImmutableList<T>**
 - **Mô tả**: Danh sách bất biến.
 - **Ví dụ**:
   ```csharp
   ImmutableList<int> immutableList = ImmutableList.Create(1, 2, 3);
   // immutableList.Add(4); // Lỗi: không thể thêm phần tử mới
   Console.WriteLine(immutableList[1]); // Kết quả: 2
   ```

- **ImmutableDictionary<TKey, TValue>**
 - **Mô tả**: Dictionary bất biến.
 - **Ví dụ**:
   ```csharp
   ImmutableDictionary<int, string> immutableDict = ImmutableDictionary.Create<int, string>()
       .Add(1, "One")
       .Add(2, "Two");
   // immutableDict.Add(3, "Three"); // Lỗi: không thể thêm phần tử mới
   Console.WriteLine(immutableDict[2]); // Kết quả: Two
   ```

- **ImmutableQueue<T>**
 - **Mô tả**: Hàng đợi bất biến.
 - **Ví dụ**:
   ```csharp
   ImmutableQueue<int> immutableQueue = ImmutableQueue.Create(1, 2);
   // immutableQueue.Enqueue(3); // Lỗi: không thể thêm phần tử mới
   Console.WriteLine(immutableQueue.Dequeue()); // Kết quả: 1
   ```

- **ImmutableStack<T>**
 - **Mô tả**: Ngăn xếp bất biến.
 - **Ví dụ**:
   ```csharp
   ImmutableStack<string> immutableStack = ImmutableStack.Create("First", "Second");
   // immutableStack.Push("Third"); // Lỗi: không thể thêm phần tử mới
   Console.WriteLine(immutableStack.Pop()); // Kết quả: Second
   ```

- **ImmutableHashSet<T>**
 - **Mô tả**: Tập hợp bất biến.
 - **Ví dụ**:
   ```csharp
   ImmutableHashSet<string> immutableHashSet = ImmutableHashSet.Create("Apple", "Banana");
   // immutableHashSet.Add("Cherry"); // Lỗi: không thể thêm phần tử mới
   Console.WriteLine(immutableHashSet.Contains("Apple")); // Kết quả: True
   ```

---

### **Tổng kết lựa chọn Collection phù hợp**

- **Danh sách các phần tử có thứ tự**: `List<T>`, `LinkedList<T>`, `ImmutableList<T>`
- **Các cặp khóa-giá trị**: `Dictionary<TKey, TValue>`, `SortedDictionary<TKey, TValue>`, `ConcurrentDictionary<TKey, TValue>`
- **Ngăn xếp và hàng đợi**: `Queue<T>`, `Stack<T>`, `ConcurrentQueue<T>`, `ConcurrentStack<T>`
- **Tập hợp không trùng lặp**: `HashSet<T>`, `ImmutableHashSet<T>`
````
