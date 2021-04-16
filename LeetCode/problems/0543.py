class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ret = 0
        def dfs(node, d):
            nonlocal ret
            ld = rd = d
            if node.left != None:
                ld = dfs(node.left, d+1)
            if node.right != None:
                rd = dfs(node.right, d+1)

            ret = max(ret, (ld-d)+(rd-d))
            return max(ld, rd)

        dfs(root, 0)
        return ret
