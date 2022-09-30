# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if node == None:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.left == None and node.right == None and node.val != 1:
                node = None

            return node

        dfs(root)
        if root.left == None and root.right == None and root.val != 1:
            return None

        return root
