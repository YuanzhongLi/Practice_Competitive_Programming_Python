class Solution:
    def mergeSimilarItems(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        A.sort(key = lambda x: x[0])
        B.sort(key = lambda x: x[0])
        na = len(A)
        nb = len(B)
        i, j = 0, 0
        ans = []
        while i < na or j < nb:
            if i < na and j < nb:
                av, bv = A[i][0], B[j][0]
                aw, bw = A[i][1], B[j][1]
                if av == bv:
                    ans.append([av, aw+bw])
                    i += 1
                    j += 1
                elif av < bv:
                    ans.append([av, aw])
                    i += 1
                else: # av > bv
                    ans.append([bv, bw])
                    j += 1
            elif i < na:
                av, aw = A[i]
                ans.append([av, aw])
                i += 1
            elif j < nb:
                bv, bw = B[j]
                ans.append([bv, bw])
                j += 1

        return ans
