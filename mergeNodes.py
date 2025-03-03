from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        new_list = dummy
        temp = head.next
        current_sum = 0

        while temp:
            if temp.val == 0:
                if current_sum > 0:
                    new_list.next = ListNode(current_sum)
                    new_list = new_list.next
                    current_sum = 0
            else:
                current_sum += temp.val
            temp = temp.next

        return dummy.next