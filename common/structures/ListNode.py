class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.value != current_other.value:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None
