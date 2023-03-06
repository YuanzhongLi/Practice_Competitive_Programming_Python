# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchNode(self, root, key):
        p_branch = None
        p_node = None
        node = root
        while node != None:
            if key == node.val:
                return node, p_node, p_branch

            p_node = node
            if key > node.val:
                p_branch = 'R'
                node = node.right
            else:
                p_branch = 'L'
                node = node.left

        return node, p_node, p_branch

    def left(self, node):
        while node.left != None:
            node = node.left

        return node

    def right(self, node):
        while node.right != None:
            node = node.right

        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        node, p_node, p_branch = self.searchNode(root, key)
        if node == None:
            return root

        # print(node, p_node, p_branch)
        if p_node == None: # is root
            rootR = root.right
            rootL = root.left
            if rootL != None and rootR != None:
                rootRL = self.left(rootR)
                rootRL.left = rootL.right
                rootL.right = rootR
                return rootL
            elif rootL == None:
                return root.right
            elif rootR == None:
                return root.left

            return None
        else:
            nodeR = node.right
            nodeL = node.left
            if nodeL != None and nodeR != None:
                nodeRL = self.left(nodeR)
                nodeRL.left = nodeL.right
                nodeL.right = nodeR
                if p_branch == 'R':
                    p_node.right = nodeL
                else:
                    p_node.left = nodeL

            elif nodeL == None:
                if p_branch == 'R':
                    p_node.right = nodeR
                else:
                    p_node.left = nodeR
            elif nodeR == None:
                if p_branch == 'R':
                    p_node.right = nodeL
                else:
                    p_node.left = nodeL
            else:
                if p_branch == 'R':
                    p_node.right = None
                else:
                    p_node.left = None

            return root
