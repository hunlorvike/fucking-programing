from typing import Optional

from common.structures import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to simplify list construction
        current = dummy  # Pointer to construct the new list
        carry = 0  # Initialize carry to 0

        # Loop until both lists are finished and there's no carry left
        while l1 is not None or l2 is not None or carry != 0:
            # Get the values from the current nodes, if they exist
            digit1 = l1.value if l1 is not None else 0
            digit2 = l2.value if l2 is not None else 0

            # Calculate the total sum of the two digits and the carry
            total = digit1 + digit2 + carry

            # Update the carry for the next iteration
            carry = total // 10

            # Create a new digit node with the sum modulo 10
            new_digit = total % 10
            current.next = ListNode(new_digit)  # Link the new digit to the result list

            # Move to the next node in the result
            current = current.next

            # Advance to the next nodes in l1 and l2, if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        result = dummy.next
        dummy.next = None
        return result
