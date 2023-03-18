class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            a, b = e
            graph[a].append(b)
            graph[b].append(a)

        root = -1
        for i, has in enumerate(hasApple):
            if has:
                root = i
                break

        if root == -1:
            return 0

        ret = [0]
        def dfs(node, par):
            back_load_has_apple = hasApple[node]
            for next_node in graph[node]:
                if next_node == par:
                    continue

                ret[0] += 1
                if dfs(next_node, node):
                    back_load_has_apple = True

            if back_load_has_apple:
                ret[0] += 1
            else:
                ret[0] -= 1

            return back_load_has_apple

        dfs(0, -1)
        return ret[0] - 1
