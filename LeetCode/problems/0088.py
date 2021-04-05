class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        for i in range(m-1, -1, -1):
            A[i], A[i+n] = A[i+n], A[i]

        i = 0; j = 0; k=0
        while k < n+m:
            k_idx = k
            i_idx = i+n; j_idx = j
            if i < m and j < n:
                if A[i_idx] <= B[j_idx]:
                    A[k_idx], A[i_idx] = A[i_idx], A[k_idx]
                    k += 1; i += 1
                else:
                    A[k_idx] = B[j_idx]
                    k += 1; j += 1
            elif i < m:
                A[k_idx], A[i_idx] = A[i_idx], A[k_idx]
                k += 1; i += 1
            elif j < n:
                A[k_idx] = B[j_idx]
                k += 1; j += 1
