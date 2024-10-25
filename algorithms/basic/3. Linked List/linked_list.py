from typing import Optional, Tuple, List


class Node:
    """
    Class đại diện một nút trong linked list.

    Attributes:
        data: Dữ liệu được lưu trữ trong nút.
        next: Con trỏ trỏ đến nút tiếp theo trong linked list.
    """

    data: int
    next: Optional["Node"]

    def __init__(self, data: int):
        """
        Khởi tạo một nút mới.

        Args:
            data: Dữ liệu được lưu trữ trong nút.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Lớp biểu diễn một linked list.

    Attributes:
        head: Con trỏ trỏ đến nút đầu tiên trong linked list.
    """

    head: Optional["Node"]

    def __init__(self):
        """
        Khởi tạo một linked list rỗng.
        """
        self.head: Optional[Node] = None

    def traverse(self) -> None:
        """
        Duyệt qua linked list và in ra giá trị của từng nút.
        """
        current: Optional[Node] = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def add_to_head(self, data: int) -> None:
        """
        Thêm một nút mới vào đầu linked list.

        Args:
            data: Dữ liệu được lưu trữ trong nút mới.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, data: int) -> None:
        """
        Thêm một nút mới vào cuối linked list.

        Args:
            data: Dữ liệu được lưu trữ trong nút mới.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current: Optional[Node] = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_head(self) -> None:
        """
        Xóa nút đầu tiên trong linked list.
        """
        if self.head is not None:
            self.head = self.head.next

    def delete_tail(self) -> None:
        """
        Xóa nút cuối cùng trong linked list.
        """
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        else:
            current: Optional[Node] = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def find(self, value: int) -> Optional[Node]:
        """
        Tìm nút đầu tiên có giá trị bằng một giá trị cho trước trong linked list.

        Args:
            value: Giá trị cần tìm.

        Returns:
            Nút có giá trị bằng value nếu tìm thấy, ngược lại trả về None.
        """
        current: Optional[Node] = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def insert_at_position(self, data: int, position: int) -> None:
        """
        Chèn nút mới vào linked list ở vị trí cụ thể.

        Args:
            data: Dữ liệu được lưu trữ trong nút mới.
            position: Vị trí cần chèn (bắt đầu từ 0).
        """
        new_node = Node(data)
        if position == 0:
            self.add_to_head(data)
            return

        current: Optional[Node] = self.head
        current_position = 0

        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            print(f"Vị trí {position} vượt quá độ dài của linked list.")
        else:
            new_node.next = current.next
            current.next = new_node

    def delete_value(self, value: int) -> None:
        """
        Xóa tất cả các nút có giá trị bằng một giá trị cho trước trong linked list.

        Args:
            value: Giá trị cần xóa.
        """
        while self.head and self.head.data == value:
            self.head = self.head.next

        current: Optional[Node] = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def reverse(self) -> None:
        """
        Đảo ngược linked list tại chỗ (không tạo linked list mới).
        """
        prev: Optional[Node] = None
        current: Optional[Node] = self.head
        while current is not None:
            next_node: Optional[Node] = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def has_cycle(self) -> bool:
        """
        Kiểm tra xem linked list có vòng lặp hay không.

        Returns:
            True nếu linked list có vòng lặp, False nếu không.
        """
        slow: Optional[Node] = self.head
        fast: Optional[Node] = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def merge_sorted_lists(
        self, list1: "LinkedList", list2: "LinkedList"
    ) -> "LinkedList":
        """
        Hợp nhất hai linked list đã được sắp xếp theo thứ tự tăng dần.

        Args:
            list1: Linked list thứ nhất.
            list2: Linked list thứ hai.

        Returns:
            Một linked list mới chứa tất cả các nút từ hai linked list ban đầu,
            được sắp xếp theo thứ tự tăng dần.
        """
        dummy = Node(0)
        tail: Optional[Node] = dummy

        l1: Optional[Node] = list1.head
        l2: Optional[Node] = list2.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def split_even_odd(self) -> Tuple["LinkedList", "LinkedList"]:
        """
        Phân chia linked list thành hai linked list mới, một chứa các nút có giá trị chẵn,
        một chứa các nút có giá trị lẻ.

        Returns:
            Một tuple chứa hai linked list: (linked list chứa giá trị chẵn, linked list chứa giá trị lẻ).
        """
        even_list = LinkedList()
        odd_list = LinkedList()

        current: Optional[Node] = self.head
        while current:
            if current.data % 2 == 0:
                even_list.add_to_tail(current.data)
            else:
                odd_list.add_to_tail(current.data)
            current = current.next

        return even_list, odd_list

    def find_first_k_nodes(self, k: int) -> List[int]:
        """
        Tìm k nút đầu tiên trong linked list.

        Args:
            k: Số lượng nút cần tìm.

        Returns:
            Một list chứa giá trị của k nút đầu tiên.
        """
        result: List[int] = []
        current: Optional[Node] = self.head
        while current and k > 0:
            result.append(current.data)
            current = current.next
            k -= 1
        return result

    def remove_kth_from_end(self, k: int) -> None:
        """
        Xoá nút thứ k từ cuối linked list.

        Args:
            k: Vị trí của nút cần xóa (tính từ cuối linked list).
        """
        fast: Optional[Node] = self.head
        slow: Optional[Node] = self.head

        for _ in range(k):
            if fast is None:
                return
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow and slow.next:
            slow.next = slow.next.next

    def find_intersection(
        self, list1: "LinkedList", list2: "LinkedList"
    ) -> Optional[Node]:
        """
        Tìm điểm giao nhau của hai linked list.

        Args:
            list1: Linked list thứ nhất.
            list2: Linked list thứ hai.

        Returns:
            Nút giao nhau nếu tìm thấy, ngược lại trả về None.
        """

        def get_length(head: Optional[Node]) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        l1: Optional[Node] = list1.head
        l2: Optional[Node] = list2.head
        len1, len2 = get_length(l1), get_length(l2)

        if len1 > len2:
            for _ in range(len1 - len2):
                l1 = l1.next
        else:
            for _ in range(len2 - len1):
                l2 = l2.next

        while l1 and l2:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
        return None
