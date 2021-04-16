class Solution:
    def buildTree(self, P: List[int], I: List[int]) -> TreeNode:
        root = TreeNode()
        id = 0
        def rec(l, r, node):
            nonlocal id
            top = P[id]; id += 1
            node.val = top
            pivot = -1
            for i in range(l, r):
                if I[i] == top:
                    pivot = i
                    break


            if l < pivot:
                left = TreeNode()
                node.left = left
                rec(l, pivot, left)

            if r > pivot+1:
                right = TreeNode()
                node.right = right
                rec(pivot+1, r, right)

        rec(0, len(P), root)
        return root

# dictを使ってpivotをメモしておく
class Solution:
    def buildTree(self, P: List[int], I: List[int]) -> TreeNode:
        mp = {}
        for i, num in enumerate(I):
            mp[num] = i

        root = TreeNode()
        id = 0
        def rec(l, r, node):
            nonlocal id
            top = P[id]; id += 1
            node.val = top
            pivot = mp[top]

            if l < pivot:
                left = TreeNode()
                node.left = left
                rec(l, pivot, left)

            if r > pivot+1:
                right = TreeNode()
                node.right = right
                rec(pivot+1, r, right)

        rec(0, len(P), root)
        return root
