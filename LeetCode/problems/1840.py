INF = float('inf')
class Solution:
    def maxBuilding(self, N: int, R: List[List[int]]) -> int:
        R = [[id-1,h] for id, h in R]
        R.append([0, 0])
        R.sort()
        if R[-1][0] != N-1: # do not have N building restriction
            R.append([N-1, INF])

        M = len(R)
        id2idx = {}
        idx2id = {}

        for idx, (id, _) in enumerate(R):
            id2idx[id] = idx
            idx2id[idx] = id

        # greedy from 1 to N building
        H = [INF for _ in range(M)]; H[0] = 0
        for idx in range(1, M):
            prev_h = H[idx-1]; prev_id = idx2id[idx-1]
            cur_max_h = R[idx][1]; cur_id = idx2id[idx]
            if prev_h - (cur_id-prev_id) > cur_max_h:
                H[idx] = cur_max_h
            else:
                H[idx] = min(prev_h + (cur_id-prev_id), cur_max_h)


        # greedy from N to 1 building
        # adjust height and find max height
        ret = H[M-1]
        for idx in range(M-2, -1, -1):
            prev_h = H[idx+1]; prev_id = idx2id[idx+1]
            cur_h = H[idx]; cur_id = idx2id[idx]

            if cur_h > prev_h + (prev_id-cur_id): # need to adjust
                H[idx] = prev_h + (prev_id-cur_id)
                ret = max(ret, H[idx])
            else:
                ret = max(ret, cur_h)
                # cur_h + x - y = prev_h & x+y = prev_id - cur_id
                if cur_h >= prev_h:       # max is cur_h + x
                    su = (prev_id-cur_id) # x+y
                    diff = prev_h-cur_h   # x-y
                    x2 = su+diff          # 2*x
                    x = x2//2
                    ret = max(ret, cur_h+max(0, x))
                else: # max is prev_h + y
                    su = (prev_id-cur_id) # x+y
                    diff = cur_h-prev_h   # y-x
                    y2 = su+diff          # 2*y
                    y = y2//2
                    ret = max(ret, prev_h+max(0, y))

        return ret
