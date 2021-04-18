from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None: return None
        mp = {} # val -> Node
        s = set([])
        q = deque([node])
        edges = set([])
        while q:
            u = q.popleft()
            if u.val in s: continue
            s.add(u.val)
            mp[u.val] = Node(u.val, [])
            for v in u.neighbors:
                edge = (min(u.val, v.val), max(u.val, v.val)); edges.add(edge)
                if v in s: continue
                q.append(v)

        for a, b in edges:
            node1 = mp[a]; node2 = mp[b]
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)

        return mp[node.val]
