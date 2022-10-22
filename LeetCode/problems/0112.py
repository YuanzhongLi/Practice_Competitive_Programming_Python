# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeaf(node):
    return node.left == None and node.right == None

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if root == None:
            return False

        s = [0]
        def dfs(node):
            s[0] += node.val
            if isLeaf(node) and s[0] == target:
                return True

            if node.left != None:
                if dfs(node.left):
                    return True

            if node.right != None:
                if dfs(node.right):
                    return True


            s[0] -= node.val
            return False

        return dfs(root)
