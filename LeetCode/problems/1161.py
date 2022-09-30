# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        mem = []
        q = deque([(0, root)])
        while len(q) > 0:
            level, node = q.popleft()
            if level == len(mem):
                mem.append(0)

            mem[level] += node.val

            if node.left != None:
                q.append((level + 1, node.left))

            if node.right != None:
                q.append((level + 1, node.right))


        ma = -4000000007
        ret = 0
        for i, s in enumerate(mem):
            if s > ma:
                ret = i+1
                ma = s

        return ret
