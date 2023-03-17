# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        none_flag = False
        while len(q) > 0:
            node = q.popleft()
            if none_flag and node != None:
                return False
            elif node == None:
                none_flag = True
            else: # node != None and none_flag = False
                q.append(node.left)
                q.append(node.right)

        return True
