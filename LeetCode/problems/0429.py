"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        if root == None:
            return ret

        q = deque([(0, root)])
        while len(q) > 0:
            level, node = q.popleft()
            if level == len(ret):
                ret.append([node.val])
            else:
                ret[level].append(node.val)
            for child in node.children:
                q.append((level + 1, child))

        return ret
