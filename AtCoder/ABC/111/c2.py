from heapq import heapify, heappop, heappush, heappushpop
e_pq = []
o_pq = []
heapify(e_pq)
heapify(o_pq)

n = int(input().rstrip())
v_max = 100005
even = [[0, i] for i in range(v_max)]
odd = [[0, i] for i in range(v_max)]
V = list(map(int, input().rstrip().rsplit()))
for i, v in enumerate(V):
  if i&1:
    odd[v][0] += 1
  else:
    even[v][0] += 1

for i in range(v_max):
  e = even[i]
  o = odd[i]
  heappush(e_pq, e)
  heappush(o_pq, o)
  if len(e_pq) > 2:
   heappop(e_pq)
  if len(o_pq) > 2:
    heappop(o_pq)

e2 = heappop(e_pq)
en2 = e2[1]
en2_num = e2[0]
e = heappop(e_pq)
en = e[1]
en_num = e[0]

o2 = heappop(o_pq)
on2 = o2[1]
on2_num = o2[0]
o = heappop(o_pq)
on = o[1]
on_num = o[0]

if en != on or en_num == en2_num or on_num == on2_num:
  print(n-(en_num + on_num))
else:
  print(n-max(en2_num+on_num, en_num+on2_num))
