# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        mem = []
        q = deque([(0, root)])
        while len(q) > 0:
            level, node = q.popleft()
            if level == len(mem):
                mem.append([1, node.val])
            else:
                mem[level][0] += 1
                mem[level][1] += node.val

            left = node.left
            right = node.right
            if left != None:
                q.append((level + 1, left))
            if right != None:
                q.append((level + 1, right))

        ans = []
        for a in mem:
            ans.append(a[1] / a[0])

        return ans
