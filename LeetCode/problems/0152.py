INF = float('inf')
def getMaximum(A):
    global INF
    N = len(A)
    if N == 1: return A[0]
    neg_num = 0
    mi_neg_id = INF; ma_neg_id = -INF
    for i,a in enumerate(A):
        if a < 0:
            neg_num += 1
            mi_neg_id = min(mi_neg_id, i)
            ma_neg_id = max(ma_neg_id, i)

    if neg_num%2 == 0:
        ret = 1
        for a in A:
            ret *= a
        return ret
    else:
        alt1 = None; alt2 = None
        for i in range(mi_neg_id+1, N):
            if alt1 == None:
                alt1 = A[i]
            else:
                alt1 *= A[i]

        for i in range(ma_neg_id):
            if alt2 == None:
                alt2 = A[i]
            else:
                alt2 *= A[i]

        if alt1 == None:
            return alt2
        elif alt2 == None:
            return alt1
        else:
            return max(alt1, alt2)


class Solution:
    def maxProduct(self, A: List[int]) -> int:
        ret = -INF
        tmp = []
        for i,a in enumerate(A):
            if a == 0:
                ret = max(ret, 0)
                if tmp:
                    ret = max(ret, getMaximum(tmp))
                    tmp = []
            else:
                tmp.append(a)


        if tmp:
            ret = max(ret, getMaximum(tmp))
        return ret
