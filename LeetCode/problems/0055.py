class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        visited = [False for _ in range(N)]
        visited[0] = True
        visited_max = 0
        for i in range(N):
            if not visited[i]:
                return False
            for j in range(visited_max+1, min(i + nums[i] + 1, N)):
                visited[j] = True
            visited_max = max(visited_max, min(i + nums[i], N-1))

        return True
