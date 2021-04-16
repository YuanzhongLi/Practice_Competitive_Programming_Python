# Union Find
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # (person, email) assign id
        # union forest unite
        pi2id = defaultdict(int)
        id2pi = {}
        cur_id = 1
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if pi2id[(name, email)] == 0:
                    pi2id[(name, email)] = cur_id
                    id2pi[cur_id] = (name, email)
                    cur_id += 1
        N = cur_id
        unionforest = [i for i in range(N)]
        rank = [i for i in range(N)]
        def root(a):
            if unionforest[a] != a:
                unionforest[a] = root(unionforest[a])
                return unionforest[a]
            else:
                return unionforest[a]

        def unite(a, b):
            a = root(a); b = root(b)
            if a == b: return
            if rank[a] > rank[b]:
                unionforest[b] = a
            elif rank[a] == rank[b]:
                unionforest[b] = a
                rank[a] += 1
            else:
                unionforest[a] = b

        for account in accounts:
            name = account[0]
            first_email = account[1]
            a_id = pi2id[(name, first_email)]
            for email in account[2:]:
                b_id = pi2id[(name, email)]
                unite(a_id, b_id)

        group = {}
        for i in range(1, N):
            root_id = root(i)
            if group.get(root_id, None) == None:
                group[root_id] = [i]
            else:
                group[root_id].append(i)

        ans = []
        for item in group.items():
            root_id, ids = item[0], item[1]
            name = id2pi[root_id][0]
            emails = []
            for id in ids:
                email = id2pi[id][1]
                emails.append(email)
            emails.sort()
            alt = [name]
            for email in emails:
                alt.append(email)
            ans.append(alt)

        return ans

# bfs
from collections import defaultdict, deque
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        e2n = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                e2n[email] = name
        visited = set()
        ans = []
        for email in graph:
            if email in visited: continue
            name = e2n[email]
            q = deque([email])
            emails = []
            while q:
                u = q.popleft()
                if u in visited: continue
                emails.append(u); visited.add(u)

                for v in graph[u]:
                    if v in visited: continue
                    q.append(v)
            emails.sort()
            ans.append([name]+emails)
        return ans
