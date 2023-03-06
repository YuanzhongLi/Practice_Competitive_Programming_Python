# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preNode = head
        if preNode == None:
            return head

        node = preNode.next
        if node == None:
            return head

        # node number is >= 2
        head = node

        nextNode = node.next
        node.next = preNode
        preNode.next = nextNode


        preNode = head.next
        node = preNode.next
        while node != None:
            nextNode = node.next
            if nextNode != None:
                node.next = nextNode.next
                nextNode.next = node
                preNode.next = nextNode

                preNode = node
                node = node.next
            else:
                break

        return head
