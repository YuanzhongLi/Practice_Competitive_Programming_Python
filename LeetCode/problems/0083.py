# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        cur = head
        next = cur.next
        while next:
            cur.next = None
            if next.val == cur.val:
                next = next.next
            else:
                cur.next = next
                cur = next
                next = cur.next

        return head
