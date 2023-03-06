# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        cur = head.next
        new_head = head
        new_head.next = None

        while cur != None:
            nxt = cur.next
            cur.next = None # separate from list

            if cur.val < new_head.val:
                cur.next = new_head
                new_head = cur
                cur = nxt
                continue

            node = new_head
            while True:
                if node.val <= cur.val:
                    if node.next == None:
                        node.next = cur
                        cur = nxt
                        break
                    elif node.next.val >= cur.val:
                        cur.next = node.next
                        node.next = cur
                        cur = nxt
                        break
                    else: # node.next.val < cur.val
                        node = node.next
                        continue
                else:
                    node = node.next
                    continue

        return new_head
