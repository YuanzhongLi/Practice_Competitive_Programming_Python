# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check(ary):
    odds = 0
    for a in ary:
        if (a & 1) == 1:
            odds += 1

        if odds > 1:
            return False

    return True


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node.left == None and node.right == None

        mem = [0 for _ in range(9)]
        ans = [0]

        def dfs(node):
            mem[node.val - 1] += 1
            if isLeaf(node):
                if check(mem):
                    ans[0] += 1
            else:
                if node.left != None:
                    dfs(node.left)
                if node.right != None:
                    dfs(node.right)

            mem[node.val - 1] -= 1

        dfs(root)
        return ans[0]
