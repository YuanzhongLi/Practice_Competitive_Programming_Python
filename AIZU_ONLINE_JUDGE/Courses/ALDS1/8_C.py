from typing import Optional
from sys import stdin

input = stdin.readline


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def search(self, x: int) -> Optional[Node]:
        node = self.root
        while node:
            if node.val == x:
                return node
            elif x < node.val:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, x: int) -> Optional[Node]:
        new_node = Node(x)
        if not self.root:
            self.root = new_node
            return new_node

        parent = None
        node = self.root
        while node:
            if node.val == x:
                return node
            elif x < node.val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        if x < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node

    def searchForRemove(self, x: int) -> tuple[Optional[Node], Optional[Node], bool]:
        parent = None
        isLeft = False
        node = self.root
        while node:
            if node.val == x:
                return node, parent, isLeft
            elif x < node.val:
                parent = node
                isLeft = True
                node = node.left
            else:
                parent = node
                isLeft = False
                node = node.right
        return None, None, False

    def getLeftestNode(
        self, node: Optional[Node]
    ) -> tuple[Optional[Node], Optional[Node]]:
        if not node:
            return None, None

        parent = None
        leftestNode = node
        while leftestNode.left:
            parent = leftestNode
            leftestNode = leftestNode.left

        return leftestNode, parent

    def remove(self, x):
        node, parent, isLeft = BST.searchForRemove(self, x)
        if not node:
            return

        if (not node.left) and (not node.right):
            if not parent:
                self.root = None
                return

            if isLeft:
                parent.left = None
            else:
                parent.right = None
        elif (not node.left) or (not node.right):
            child = node.left or node.right
            if not parent:
                self.root = child
                return

            if isLeft:
                parent.left = child
            else:
                parent.right = child
        else:
            left, right = node.left, node.right
            rightLeftestNode, rightLeftestNodeParent = BST.getLeftestNode(self, right)
            if not rightLeftestNodeParent:
                rightLeftestNodeParent = node

            rightLeftestNodeParent.left = rightLeftestNode.right
            if rightLeftestNode == right:
                rightLeftestNode.left = left
            else:
                rightLeftestNode.left, rightLeftestNode.right = left, right

            if not parent:
                self.root = rightLeftestNode
                return

            if isLeft:
                parent.left = rightLeftestNode
            else:
                parent.right = rightLeftestNode

        return


def preOrder(root):
    pre_order_output = []

    def dfs(node: Node):
        if not node:
            return

        pre_order_output.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return pre_order_output


def inOrder(root):
    in_order_output = []

    def dfs(node: Node):
        if not node:
            return

        dfs(node.left)
        in_order_output.append(node.val)
        dfs(node.right)

    dfs(root)
    return in_order_output


def print_order(order):
    print(" " + " ".join([str(num) for num in order]))


N = int(input().rstrip())
bst = BST()
while N:
    query = list(map(str, input().rstrip().rsplit()))
    if query[0] == "find":
        if bst.search(int(query[1])):
            print("yes")
        else:
            print("no")
    elif query[0] == "insert":
        bst.insert(int(query[1]))
    elif query[0] == "delete":
        bst.remove(int(query[1]))
    elif query[0] == "print":
        print_order(inOrder(bst.root))
        print_order(preOrder(bst.root))

    N -= 1
