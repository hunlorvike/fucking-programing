# Cấu trúc dữ liệu Đồ thị (Graph)

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Các loại đồ thị](#các-loại-đồ-thị)
3. [Biểu diễn đồ thị trong TypeScript](#biểu-diễn-đồ-thị-trong-typescript)
   - [Danh sách kề (Adjacency List)](#danh-sách-kề-adjacency-list)
   - [Ma trận kề (Adjacency Matrix)](#ma-trận-kề-adjacency-matrix)
4. [Triển khai đồ thị trong TypeScript](#triển-khai-đồ-thị-trong-typescript)
5. [Các thuật toán liên quan đến đồ thị](#các-thuật-toán-liên-quan-đến-đồ-thị)
6. [Ứng dụng của đồ thị](#ứng-dụng-của-đồ-thị)
7. [Kết luận](#kết-luận)

---

## Giới thiệu

Đồ thị là một cấu trúc dữ liệu phi tuyến tính đại diện cho mối quan hệ giữa các đối tượng. Nó được cấu tạo từ hai thành phần chính:

- **Đỉnh (Node/Vertex):** Các đối tượng trong đồ thị.
- **Cạnh (Edge):** Mối quan hệ kết nối giữa hai đỉnh. Cạnh có thể có hướng (directed) hoặc không có hướng (undirected), và có thể được gán trọng số (weighted).

## Các loại đồ thị

- **Đồ thị có hướng (Directed Graph):** Các cạnh có hướng xác định, ví dụ: quan hệ "theo dõi" trên mạng xã hội.
- **Đồ thị vô hướng (Undirected Graph):** Các cạnh không có hướng, ví dụ: quan hệ "bạn bè" trên mạng xã hội.
- **Đồ thị có trọng số (Weighted Graph):** Các cạnh được gán trọng số, ví dụ: khoảng cách giữa các thành phố.

## Biểu diễn đồ thị trong TypeScript

### Danh sách kề (Adjacency List)

- Sử dụng một đối tượng hoặc `Map` để lưu trữ các đỉnh và danh sách các đỉnh kề với nó.

```typescript
const graph: { [key: string]: string[] } = {
  A: ['B', 'C'],
  B: ['D', 'E'],
  C: ['F'],
  D: [],
  E: ['F'],
  F: [],
};
```

### Ma trận kề (Adjacency Matrix)

- Sử dụng một mảng hai chiều để biểu diễn các cạnh. Mỗi hàng và cột đại diện cho một đỉnh, và giá trị tại ô `(i, j)` thể hiện có cạnh kết nối giữa đỉnh `i` và `j`.

```typescript
const graph: number[][] = [
  [0, 1, 1, 0, 0, 0],
  [1, 0, 0, 1, 1, 0],
  [1, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 1, 0],
];
```

## Triển khai đồ thị trong TypeScript

```typescript
class Graph {
  private vertices: number;
  private adjacencyList: Map<number, number[]>;

  constructor(vertices: number) {
    this.vertices = vertices;
    this.adjacencyList = new Map<number, number[]>();
    for (let i = 0; i < vertices; i++) {
      this.adjacencyList.set(i, []);
    }
  }

  // Thêm cạnh vào đồ thị
  addEdge(u: number, v: number): void {
    this.adjacencyList.get(u)?.push(v);
  }

  // In đồ thị
  printGraph(): void {
    for (let [vertex, adj] of this.adjacencyList) {
      console.log(`${vertex} -> ${adj.join(', ')}`);
    }
  }
}

// Ví dụ sử dụng
const graph = new Graph(6);
graph.addEdge(0, 1);
graph.addEdge(0, 2);
graph.addEdge(1, 3);
graph.addEdge(1, 4);
graph.addEdge(2, 5);
graph.addEdge(4, 5);

graph.printGraph();
// Output:
// 0 -> 1, 2
// 1 -> 3, 4
// 2 -> 5
// 3 ->
// 4 -> 5
// 5 ->
```

## Các thuật toán liên quan đến đồ thị

- **Duyệt đồ thị (Traversal):**
  - **BFS (Breadth-First Search)**: Duyệt theo chiều rộng.
  - **DFS (Depth-First Search)**: Duyệt theo chiều sâu.
- **Tìm đường đi:**
  - **Tìm đường đi ngắn nhất** (Dijkstra, Bellman-Ford).
  - **Tìm đường đi Euler** và **đường đi Hamilton**.
- **Tìm chu trình:**
  - **Chu trình Euler**, **chu trình Hamilton**.
- **Tìm cây khung:**
  - **Thuật toán Kruskal**, **Prim**.
- **Tô màu đồ thị:** Được ứng dụng để kiểm tra khả năng phân vùng của đồ thị (Welsh-Powell).

## Ứng dụng của đồ thị

- **Mạng xã hội:** Mô phỏng kết nối giữa các người dùng, tìm kiếm bạn bè, đề xuất nội dung.
- **Dẫn đường:** Tìm đường đi ngắn nhất, tối ưu hóa tuyến đường.
- **Mạng máy tính:** Phân bổ tài nguyên, kiểm soát lưu lượng.
- **Khoa học máy tính:** Phân tích dữ liệu, xử lý ngôn ngữ tự nhiên.

## Kết luận

Đồ thị là một cấu trúc dữ liệu mạnh mẽ và linh hoạt, được sử dụng trong nhiều lĩnh vực của khoa học máy tính. Việc hiểu rõ các khái niệm và cách triển khai đồ thị sẽ giúp bạn giải quyết hiệu quả các bài toán liên quan đến mối quan hệ giữa các đối tượng.
