class Solution:
    def maxSubsequence(self, A: List[int], k: int) -> List[int]:
        B = []
        for a in A:
            B.append(a)
        B.sort()
        B.reverse()
        B_dict = {}
        for i in range(k):
            b = B[i]
            if b in B_dict:
                B_dict[b] += 1
            else:
                B_dict[b] = 1

        ans = []
        for a in A:
            if a in B_dict and B_dict[a] > 0:
                ans.append(a)
                B_dict[a] -= 1

        return ans
