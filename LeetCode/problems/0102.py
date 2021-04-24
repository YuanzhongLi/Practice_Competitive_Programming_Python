from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        ret = []
        q = deque([(root, 1)])
        while q:
            node, d = q.popleft()
            if d == len(ret):
                ret[-1].append(node.val)
            else:
                ret.append([node.val])

            if node.left != None:
                q.append((node.left, d+1))
            if node.right != None:
                q.append((node.right, d+1))

        return ret
