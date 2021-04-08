class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        N = len(T)
        stack = [(T[-1], N-1)]
        T[-1] = 0
        for i in range(N-2, -1, -1):
            t = T[i]
            while stack and t >= stack[-1][0]:
                stack.pop()
            if stack:
                T[i] = stack[-1][1]-i
            else:
                T[i] = 0

            stack.append((t, i))
        return T
