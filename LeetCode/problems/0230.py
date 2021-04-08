class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        ans = None
        def rec(node):
            nonlocal cnt, ans
            if node == None:
                return

            if node.left == None and node.right == None: # is leaf
                cnt += 1
                if cnt == k:
                    ans = node.val
                    return True
                else: return False

            if node.left:
                if rec(node.left): return True

            cnt += 1
            if cnt == k:
                ans = node.val
                return True

            if node.right:
                if rec(node.right): return True

            return False

        rec(root)
        return ans
