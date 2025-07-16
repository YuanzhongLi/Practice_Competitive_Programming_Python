# Solution Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solutions/6955171/python-bit-manupulation-solution-with-ja-6ikb/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        start = False
        ans = 0
        node = head
        while node != None:
            if not start:
                if node.val == 1:
                    ans = 1
                    start = True
            else:
                ans <<= 1
                ans += node.val

            node = node.next

        return ans
