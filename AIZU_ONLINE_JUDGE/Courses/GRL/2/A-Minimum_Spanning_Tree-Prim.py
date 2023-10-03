from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
V, E = map(int, input().rstrip().rsplit())


edges = []

while E:
    edges.append([int(e) for e in list(input().rstrip().rsplit())])
    E -= 1


def createGraph(N: int, edges: list[list[int]]):
    graph = [[] for _ in range(N)]
    for edge in edges:
        u, v, w = edge
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def Prim(N: int, edges: list[list[int]]) -> list[int]:
    INF = float("inf")
    graph = createGraph(N, edges)

    # 最小全域木へ接するノードを格納しておくヒープ
    # (最小全域木への距離, ノードid)
    # 最小距離のノードを取り出せるようにタプルの最初の要素を最小距離としている
    heap = [(0, 0)]

    # 各ノードの最小全域木に含まれたかを記録
    decided = [False for _ in range(N)]

    # 最小全域木から各ノードへの最小距離をinf(無限距離)として初期化
    distance = [INF for _ in range(N)]
    # 始点であるノード0の距離は0で初期化
    distance[0] = 0

    mst_cost = 0
    while heap:
        _, target_node = heappop(heap)
        # 既に最小全域木に含まれているノードならスルー
        if decided[target_node]:
            continue

        # 最小全域木にtarget_nodeを追加し、エッジの長さを加える
        decided[target_node] = True
        mst_cost += distance[target_node]

        for edge in graph[target_node]:
            node_id, w = edge
            if not decided[node_id] and distance[node_id] > w:
                distance[node_id] = w
                heappush(heap, (w, node_id))

    return mst_cost


print(Prim(V, edges))
