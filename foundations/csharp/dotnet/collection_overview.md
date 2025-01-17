# Tổng Quan Về Các Namespace Collection trong .NET

## Mục Lục

1. [Namespace `System.Collections`](#1-namespace-systemcollections)
    - 1.1 [ArrayList](#11-arraylist)
    - 1.2 [Hashtable](#12-hashtable)
    - 1.3 [Queue](#13-queue)
    - 1.4 [Stack](#14-stack)
    - 1.5 [SortedList](#15-sortedlist)
2. [Namespace `System.Collections.Generic`](#2-namespace-systemcollectionsgeneric)
    - 2.1 [List<T>](#21-listt)
    - 2.2 [Dictionary<TKey, TValue>](#22-dictionarytkey-tvalue)
    - 2.3 [Queue<T>](#23-queuet)
    - 2.4 [Stack<T>](#24-stackt)
    - 2.5 [SortedList<TKey, TValue>](#25-sortedlisttkey-tvalue)
    - 2.6 [HashSet<T>](#26-hashsett)
    - 2.7 [LinkedList<T>](#27-linkedlistt)
    - 2.8 [SortedDictionary<TKey, TValue>](#28-sorteddictionarytkey-tvalue)
3. [Namespace `System.Collections.Concurrent`](#3-namespace-systemcollectionsconcurrent)
    - 3.1 [ConcurrentDictionary<TKey, TValue>](#31-concurrentdictionarytkey-tvalue)
    - 3.2 [BlockingCollection<T>](#32-blockingcollectiont)
    - 3.3 [ConcurrentQueue<T>](#33-concurrentqueuet)
    - 3.4 [ConcurrentStack<T>](#34-concurrentstackt)
    - 3.5 [ConcurrentBag<T>](#35-concurrentbagt)
4. [Namespace `System.Collections.Specialized`](#4-namespace-systemcollectionsspecialized)
    - 4.1 [NameValueCollection](#41-namevaluecollection)
    - 4.2 [StringCollection](#42-stringcollection)
    - 4.3 [StringDictionary](#43-stringdictionary)
    - 4.4 [OrderedDictionary](#44-ordereddictionary)
    - 4.5 [HybridDictionary](#45-hybriddictionary)
5. [Namespace `System.Collections.Immutable`](#5-namespace-systemcollectionsimmutable)
    - 5.1 [ImmutableList<T>](#51-immutablelistt)
    - 5.2 [ImmutableDictionary<TKey, TValue>](#52-immutabledictionarytkey-tvalue)
    - 5.3 [ImmutableQueue<T>](#53-immutablequeuet)
    - 5.4 [ImmutableStack<T>](#54-immutablestackt)
    - 5.5 [ImmutableHashSet<T>](#55-immutablehashsett)
6. [Tổng Kết Lựa Chọn Collection Phù Hợp](#tổng-kết-lựa-chọn-collection-phù-hợp)

---

## 1. **Namespace `System.Collections`**

`System.Collections` chứa các collection không generic, chủ yếu phục vụ cho các ứng dụng .NET Framework cũ. Những
collection này vẫn hữu ích trong một số tình huống nhất định, nhưng thiếu tính an toàn về kiểu dữ liệu so với các
collection generic.

### 1.1. ArrayList

- **Mô tả**: Lưu trữ một danh sách các đối tượng có kích thước động.
- **Ví dụ**:
  ```csharp
  ArrayList arrayList = new ArrayList();
  arrayList.Add("Hello");
  arrayList.Add(123);
  arrayList.Add(DateTime.Now);
  Console.WriteLine(arrayList[0]); // Kết quả: Hello
  ```

### 1.2. Hashtable

- **Mô tả**: Lưu trữ các cặp khóa-giá trị với khả năng truy cập nhanh qua khóa.
- **Ví dụ**:
  ```csharp
  Hashtable hashtable = new Hashtable();
  hashtable["key1"] = "value1";
  hashtable["key2"] = "value2";
  Console.WriteLine(hashtable["key1"]); // Kết quả: value1
  ```

### 1.3. Queue

- **Mô tả**: Hàng đợi (FIFO - First In, First Out).
- **Ví dụ**:
  ```csharp
  Queue queue = new Queue();
  queue.Enqueue("First");
  queue.Enqueue("Second");
  Console.WriteLine(queue.Dequeue()); // Kết quả: First
  ```

### 1.4. Stack

- **Mô tả**: Ngăn xếp (LIFO - Last In, First Out).
- **Ví dụ**:
  ```csharp
  Stack stack = new Stack();
  stack.Push("First");
  stack.Push("Second");
  Console.WriteLine(stack.Pop()); // Kết quả: Second
  ```

### 1.5. SortedList

- **Mô tả**: Lưu trữ các cặp khóa-giá trị tự động sắp xếp theo khóa.
- **Ví dụ**:
  ```csharp
  SortedList sortedList = new SortedList();
  sortedList.Add("key2", "value2");
  sortedList.Add("key1", "value1");
  Console.WriteLine(sortedList[0]); // Kết quả: value1
  ```

---

## 2. **Namespace `System.Collections.Generic`**

`System.Collections.Generic` chứa các collection generic, cho phép định nghĩa kiểu dữ liệu cụ thể (type-safe), giúp tối
ưu hóa hiệu suất và tránh lỗi khi sử dụng sai kiểu dữ liệu.

### 2.1. List<T>

- **Mô tả**: Danh sách generic với kiểu dữ liệu cụ thể `T`.
- **Ví dụ**:
  ```csharp
  List<string> list = new List<string>();
  list.Add("Apple");
  list.Add("Banana");
  Console.WriteLine(list[1]); // Kết quả: Banana
  ```

### 2.2. Dictionary<TKey, TValue>

- **Mô tả**: Lưu trữ các cặp khóa-giá trị với khóa là duy nhất.
- **Ví dụ**:
  ```csharp
  Dictionary<int, string> dictionary = new Dictionary<int, string>();
  dictionary[1] = "One";
  dictionary[2] = "Two";
  Console.WriteLine(dictionary[2]); // Kết quả: Two
  ```

### 2.3. Queue<T>

- **Mô tả**: Hàng đợi generic theo FIFO.
- **Ví dụ**:
  ```csharp
  Queue<int> queue = new Queue<int>();
  queue.Enqueue(1);
  queue.Enqueue(2);
  Console.WriteLine(queue.Dequeue()); // Kết quả: 1
  ```

### 2.4. Stack<T>

- **Mô tả**: Ngăn xếp generic theo LIFO.
- **Ví dụ**:
  ```csharp
  Stack<string> stack = new Stack<string>();
  stack.Push("First");
  stack.Push("Second");
  Console.WriteLine(stack.Pop()); // Kết quả: Second
  ```

### 2.5. SortedList<TKey, TValue>

- **Mô tả**: Tương tự `Dictionary`, nhưng các phần tử được sắp xếp theo khóa.
- **Ví dụ**:
  ```csharp
  SortedList<int, string> sortedList = new SortedList<int, string>();
  sortedList.Add(2, "Two");
  sortedList.Add(1, "One");
  Console.WriteLine(sortedList[1]); // Kết quả: One
  ```

### 2.6. HashSet<T>

- **Mô tả**: Tập hợp không chứa phần tử trùng lặp.
- **Ví dụ**:
  ```csharp
  HashSet<string> hashSet = new HashSet<string>();
  hashSet.Add("Apple");
  hashSet.Add("Banana");
  hashSet.Add("Apple"); // Không thêm lại phần tử trùng
  Console.WriteLine(hashSet.Count); // Kết quả: 2
  ```

### 2.7. LinkedList<T>

- **Mô tả**: Danh sách liên kết hai chiều.
- **Ví dụ**:
  ```csharp
  LinkedList<string> linkedList = new LinkedList<string>();
  linkedList.AddLast("First");
  linkedList.AddLast("Second");
  Console.WriteLine(linkedList.First.Value); // Kết quả: First
  ```

### 2.8. SortedDictionary<TKey, TValue>

- **Mô tả**: Tương tự `Dictionary` nhưng lưu trữ theo thứ tự sắp xếp của khóa.
- **Ví dụ**:
  ```csharp
  SortedDictionary<string, int> sortedDict = new SortedDictionary<string, int>();
  sortedDict["B"] = 2;
  sortedDict["A"] = 1;
  Console.WriteLine(sortedDict.First().Value); // Kết quả: 1
  ```

---

## 3. **Namespace `System.Collections.Concurrent`**

Các collection trong `System.Collections.Concurrent` được thiết kế để đảm bảo an toàn khi thao tác trong môi trường đa
luồng (thread-safe).

### 3.1. ConcurrentDictionary<TKey, TValue>

- **Mô tả**: Dictionary hỗ trợ thao tác an toàn trong môi trường đa luồng.
- **Ví dụ**:

  ```csharp


  ConcurrentDictionary<int, string> concurrentDict = new ConcurrentDictionary<int, string>();
  concurrentDict[1] = "One";
  concurrentDict[2] = "Two";
  Console.WriteLine(concurrentDict[1]); // Kết quả: One
  ```

### 3.2. BlockingCollection<T>

- **Mô tả**: Hỗ trợ quản lý hàng đợi với các thao tác thêm và lấy ra an toàn.
- **Ví dụ**:
  ```csharp
  BlockingCollection<int> blockingCollection = new BlockingCollection<int>();
  blockingCollection.Add(1);
  Console.WriteLine(blockingCollection.Take()); // Kết quả: 1
  ```

### 3.3. ConcurrentQueue<T>

- **Mô tả**: Hàng đợi hỗ trợ thao tác an toàn trong môi trường đa luồng.
- **Ví dụ**:
  ```csharp
  ConcurrentQueue<int> concurrentQueue = new ConcurrentQueue<int>();
  concurrentQueue.Enqueue(1);
  concurrentQueue.Enqueue(2);
  concurrentQueue.TryDequeue(out int result);
  Console.WriteLine(result); // Kết quả: 1
  ```

### 3.4. ConcurrentStack<T>

- **Mô tả**: Ngăn xếp hỗ trợ thao tác an toàn trong môi trường đa luồng.
- **Ví dụ**:
  ```csharp
  ConcurrentStack<string> concurrentStack = new ConcurrentStack<string>();
  concurrentStack.Push("First");
  concurrentStack.Push("Second");
  concurrentStack.TryPop(out string poppedValue);
  Console.WriteLine(poppedValue); // Kết quả: Second
  ```

### 3.5. ConcurrentBag<T>

- **Mô tả**: Tập hợp không thứ tự hỗ trợ thao tác an toàn trong môi trường đa luồng.
- **Ví dụ**:
  ```csharp
  ConcurrentBag<string> concurrentBag = new ConcurrentBag<string>();
  concurrentBag.Add("First");
  concurrentBag.Add("Second");
  Console.WriteLine(concurrentBag.Count); // Kết quả: 2
  ```

---

## 4. **Namespace `System.Collections.Specialized`**

Namespace này chứa các collection đặc biệt không thuộc các loại thông thường.

### 4.1. NameValueCollection

- **Mô tả**: Lưu trữ các cặp khóa-giá trị cho phép khóa trùng lặp.
- **Ví dụ**:
  ```csharp
  NameValueCollection nvc = new NameValueCollection();
  nvc.Add("key1", "value1");
  nvc.Add("key1", "value2");
  Console.WriteLine(nvc["key1"][0]); // Kết quả: value1
  ```

### 4.2. StringCollection

- **Mô tả**: Danh sách chứa các chuỗi.
- **Ví dụ**:
  ```csharp
  StringCollection stringCollection = new StringCollection();
  stringCollection.Add("First");
  stringCollection.Add("Second");
  Console.WriteLine(stringCollection[1]); // Kết quả: Second
  ```

### 4.3. StringDictionary

- **Mô tả**: Dictionary với khóa là chuỗi.
- **Ví dụ**:
  ```csharp
  StringDictionary stringDict = new StringDictionary();
  stringDict["key1"] = "value1";
  Console.WriteLine(stringDict["key1"]); // Kết quả: value1
  ```

### 4.4. OrderedDictionary

- **Mô tả**: Dictionary cho phép sắp xếp theo thứ tự thêm.
- **Ví dụ**:
  ```csharp
  OrderedDictionary orderedDict = new OrderedDictionary();
  orderedDict.Add("key1", "value1");
  orderedDict.Add("key2", "value2");
  Console.WriteLine(orderedDict[1]); // Kết quả: value2
  ```

### 4.5. HybridDictionary

- **Mô tả**: Tự động chuyển đổi giữa Hashtable và List để tối ưu hóa hiệu suất.
- **Ví dụ**:
  ```csharp
  HybridDictionary hybridDict = new HybridDictionary();
  hybridDict.Add("key1", "value1");
  hybridDict.Add("key2", "value2");
  Console.WriteLine(hybridDict["key1"]); // Kết quả: value1
  ```

---

## 5. **Namespace `System.Collections.Immutable`**

Các collection trong namespace này không thể thay đổi sau khi được tạo ra, cung cấp độ tin cậy trong các ứng dụng đa
luồng.

### 5.1. ImmutableList<T>

- **Mô tả**: Danh sách không thay đổi.
- **Ví dụ**:
  ```csharp
  ImmutableList<int> immutableList = ImmutableList.Create(1, 2, 3);
  // immutableList.Add(4); // Không thể thêm phần tử
  Console.WriteLine(immutableList[0]); // Kết quả: 1
  ```

### 5.2. ImmutableDictionary<TKey, TValue>

- **Mô tả**: Dictionary không thay đổi.
- **Ví dụ**:
  ```csharp
  var immutableDict = ImmutableDictionary<int, string>.Empty
      .Add(1, "One")
      .Add(2, "Two");
  // immutableDict.Add(3, "Three"); // Không thể thêm phần tử
  Console.WriteLine(immutableDict[1]); // Kết quả: One
  ```

### 5.3. ImmutableQueue<T>

- **Mô tả**: Hàng đợi không thay đổi.
- **Ví dụ**:
  ```csharp
  var immutableQueue = ImmutableQueue.Create<int>().Enqueue(1).Enqueue(2);
  // immutableQueue.Enqueue(3); // Không thể thêm phần tử
  Console.WriteLine(immutableQueue.Dequeue()); // Kết quả: 1
  ```

### 5.4. ImmutableStack<T>

- **Mô tả**: Ngăn xếp không thay đổi.
- **Ví dụ**:
  ```csharp
  var immutableStack = ImmutableStack.Create<string>().Push("First").Push("Second");
  // immutableStack.Push("Third"); // Không thể thêm phần tử
  Console.WriteLine(immutableStack.Pop()); // Kết quả: Second
  ```

### 5.5. ImmutableHashSet<T>

- **Mô tả**: Tập hợp không thay đổi.
- **Ví dụ**:
  ```csharp
  var immutableHashSet = ImmutableHashSet.Create<int>().Add(1).Add(2);
  // immutableHashSet.Add(3); // Không thể thêm phần tử
  Console.WriteLine(immutableHashSet.Count); // Kết quả: 2
  ```

---

## 6. **Tổng Kết Lựa Chọn Collection Phù Hợp**

Khi chọn collection trong .NET, bạn nên xem xét các yếu tố như tính an toàn về kiểu dữ liệu, hiệu suất, và khả năng đa
luồng:

- **Sử dụng `System.Collections`** khi bạn làm việc với các ứng dụng cũ hoặc cần tương thích với .NET Framework.
- **Sử dụng `System.Collections.Generic`** để có các collection an toàn về kiểu dữ liệu và hiệu suất tốt hơn.
- **Sử dụng `System.Collections.Concurrent`** khi cần thao tác an toàn trong môi trường đa luồng.
- **Sử dụng `System.Collections.Specialized`** cho các nhu cầu đặc biệt như lưu trữ các cặp khóa-giá trị có khả năng
  trùng lặp.
- **Sử dụng `System.Collections.Immutable`** khi cần các collection không thể thay đổi.
