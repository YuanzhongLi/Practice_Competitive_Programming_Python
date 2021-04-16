class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        lefts = []
        find_leftest = False
        def dfs(node):
            if node == None: return
            nonlocal  find_leftest
            if not find_leftest:
                lefts.append(node.val)
            isleaf = True
            if node.left != None:
                isleaf = False
                dfs(node.left)
            if node.right != None:
                isleaf = False
                dfs(node.right)

            if isleaf and not find_leftest:
                find_leftest = True
            elif isleaf:
                lefts.append(node.val)

        rights = []
        find_rightest = False
        def dfs2(node):
            if node == None: return
            nonlocal find_rightest
            if not find_rightest:
                rights.append(node.val)
            isleaf = True
            if node.right != None:
                isleaf = False
                dfs2(node.right)
            if node.left != None:
                isleaf = False
                dfs2(node.left)

            if isleaf and not find_rightest:
                find_rightest = True
            elif isleaf:
                 rights.append(node.val)

        dfs(root.left)
        dfs2(root.right)

        ret = [root.val] + lefts + rights[::-1]
        return ret
