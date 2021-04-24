# recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left = root.left; right = root.right
        def dfs(l_node, r_node):
            if l_node == None and r_node == None:
                return True
            elif l_node == None or r_node == None:
                return False
            else:
                ret = (l_node.val == r_node.val)
                if not ret: return ret
                ret &= dfs(l_node.left, r_node.right)
                if not ret: return ret
                ret &= dfs(l_node.right, r_node.left)
                return ret
        return dfs(left, right)

# iterative
from collections import deque
INF = float('inf')
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([(root, 0)])
        q2 = deque([])
        while q:
            node, d = q.popleft()
            if node == None:
                q2.append((INF, d))
            else:
                q2.append((node.val, d))
                q.append((node.left, d+1))
                q.append((node.right, d+1))

        cur_d = 0
        while q2:
            tmp = []
            while q2 and q2[0][1] == cur_d:
                tmp.append(q2.popleft()[0])
            N = len(tmp)
            for i in range(N//2):
                if tmp[i] != tmp[N-1-i]:
                    return False
            cur_d += 1

        return True
