class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        N = len(A)
        stack = []
        A += A
        for i in range(2*N-1, N-1, -1):
            a = A[i]
            if not stack:
                stack.append(a)
            else:
                while stack and stack[-1] <= a:
                    stack.pop()
                stack.append(a)
        ans = [-1 for _ in range(N)]
        for i in range(N-1, -1, -1):
            a = A[i]
            while stack and stack[-1] <= a:
                stack.pop()
            if not stack:
	            stack.append(a)
            else:
                ans[i] = stack[-1]
                stack.append(a)
        return ans
