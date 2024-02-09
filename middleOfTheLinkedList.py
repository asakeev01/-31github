from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listLen = 0
        l = []
        while head != None:
            listLen += 1
            l.append(head)
            head = head.next
        mid = listLen // 2
        return l[mid]