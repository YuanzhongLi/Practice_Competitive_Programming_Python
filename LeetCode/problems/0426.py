class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None: return root
        # head is the smallest
        head = None
        head_val = INF

        def rec(node):
            nonlocal head, head_val
            if node.val < head_val:
                head = node; head_val = node.val

            mi_node = node; ma_node = node
            prev = next = None
            if node.left != None:
                mi_node, prev = rec(node.left)
            if node.right != None:
                next, ma_node = rec(node.right)

            if prev != None:
                prev.right = node; node.left = prev
            if next != None:
                node.right = next; next.left = node

            return mi_node, ma_node

        _, tail = rec(root)
        head.left = tail; tail.right = head

        return head
