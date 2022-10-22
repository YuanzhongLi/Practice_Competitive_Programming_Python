class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def dfs(node):
            if node == None:
                return
            ret.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ret
