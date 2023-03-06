# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

INF = 1000000007
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        mp = {}
        def dfs(node):
            if node == None:
                # is BST, sum, min, max
                return True, 0, INF, -INF

            flag_l, sum_l, mi_l, ma_l = dfs(node.left)
            flag_r, sum_r, mi_r, ma_r = dfs(node.right)

            if flag_l and flag_r and ma_l < node.val and node.val < mi_r:
                s = node.val + sum_l + sum_r
                ans[0] = max(ans[0], s)
                return True, s, min(node.val, mi_l), max(node.val, ma_r)
            else:
                return False, 0, 0, 0

        dfs(root)

        return ans[0]
