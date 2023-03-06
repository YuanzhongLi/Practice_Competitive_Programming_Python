"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def rec(i, j, k, l):
            is_same = True
            for h in range(i, j):
                for w in range(k, l):
                    if grid[h][w] != grid[i][k]:
                        is_same = False
                        break
            new_node = Node(grid[i][k],0,None,None,None,None)
            if is_same:
                new_node.isLeaf = 1
            else:
                new_node.val = 0
                new_node.topLeft = rec(i, (i+j)//2, k, (k+l)//2)
                new_node.topRight = rec(i, (i+j)// 2, (k+l)//2, l)
                new_node.bottomLeft = rec((i+j)//2, j, k, (k+l)//2)
                new_node.bottomRight = rec((i+j)//2, j, (k+l)//2, l)

            return new_node

        n = len(grid)
        return rec(0, n, 0, n)
