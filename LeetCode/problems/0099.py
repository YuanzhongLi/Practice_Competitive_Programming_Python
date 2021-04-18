# space O(N)
INF = float('inf')
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        cur = 0
        A = [TreeNode(-INF)]
        def dfs(node):
            if node.left != None:
                dfs(node.left)
            A.append(node)
            if node.right != None:
                dfs(node.right)

        dfs(root)
        A.append(TreeNode(INF))
        N = len(A)
        node1 = node2 = None
        for i in range(1, N-1):
            if A[i].val > max(A[i-1].val, A[i+1].val):
                node1 = A[i]
                break

        for i in range(N-2, 0, -1):
            if A[i].val < min(A[i-1].val, A[i+1].val):
                node2 = A[i]
                break
        node1.val, node2.val = node2.val, node1.val

# only stack area O(H), H is the height of the tree
INF = float('inf')
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        node1 = TreeNode(-INF)
        def dfs1(node):
            nonlocal node1
            if node.left != None:
                if dfs1(node.left): return True

            if node.val < node1.val:
                return True
            else:
                node1 = node

            if node.right != None:
                if dfs1(node.right): return True
            return False
        dfs1(root)

        node2 = TreeNode(INF)
        def dfs2(node):
            nonlocal node2
            if node.right != None:
                if dfs2(node.right): return True

            if node.val > node2.val:
                return True
            else:
                node2 = node

            if node.left != None:
                if dfs2(node.left): return True
            return False

        dfs2(root)

        node1.val, node2.val = node2.val, node1.val
