def Debug(stack):
    tmp = []
    for node in stack:
        tmp.append(node.val)
    print(tmp)

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.add_all_left(root)

    def next(self) -> int:
        stack = self.stack
        # Debug(stack)
        top_node = stack.pop()
        ret = top_node.val
        if top_node.right != None:
            self.add_all_left(top_node.right)
        return ret

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def add_all_left(self, node):
        stack = self.stack
        def dfs(node):
            if not node: return
            stack.append(node)
            if node.left != None:
                dfs(node.left)
        dfs(node)
