# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        i = None
        while b != None and b.next != None:
            a = a.next
            b = b.next.next
            if a == b:
                i = a
                break

        if i == None:
            return None

        a = head
        b = i
        while a != b:
            a = a.next
            b = b.next

        return a
