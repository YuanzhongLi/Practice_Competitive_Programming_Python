# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ret = []
        def dfs(node):
            if node == root:
                ret.append(str(node.val))
            else:
                ret.append("(" + str(node.val))

            if node.left != None and node.right != None:
                dfs(node.left)
                dfs(node.right)
            elif node.left != None and node.right == None:
                dfs(node.left)
            elif node.left == None and node.right != None:
                ret.append("()")
                dfs(node.right)
            # else left == None and right == None: nothing

            if node != root:
                ret.append(")")

        dfs(root)
        return ''.join(ret)
