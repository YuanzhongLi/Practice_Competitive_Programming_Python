from sys import stdin

input = stdin.readline
INF = float("inf")

N = int(input().rstrip())


graph = [[] for _ in range(N)]

for u in range(N):
    edges = [int(e) for e in input().rstrip().rsplit()]
    for v, w in enumerate(edges):
        if w != -1:
            graph[u].append((v, w))


# 最小全域木にまだ追加していないノード
undecided = set([i for i in range(N)])

# 最小全域木から各ノードへの最短距離inf(無限距離)として初期化
distance = [INF for _ in range(N)]

# 始点としてノード0を選択
# ノード0は一番最初に最小全域木に追加され、その距離は0
distance[0] = 0

# 最小全域木(mst)のエッジの重みの和
mst_cost = 0
while len(undecided) > 0:
    # 最小全域木からの最短距離となるノード
    target_node = -1
    # 最小全域木からの最短距離となるノードへの距離
    target_node_d = INF

    # 最小全域木に未追加のノードの内で最も最小全域木への距離が短いノードを１つ選ぶ
    for node_id in undecided:
        if distance[node_id] < target_node_d:
            target_node = node_id
            target_node_d = distance[node_id]

    # target_nodeを最小全域木に追加する
    undecided.remove(target_node)
    mst_cost += target_node_d

    # target_nodeが最小全域木へと追加されたので、それと隣接するノードの最小全域木への距離を更新
    for edge in graph[target_node]:
        node_id, w = edge
        distance[node_id] = min(distance[node_id], w)

print(mst_cost)
