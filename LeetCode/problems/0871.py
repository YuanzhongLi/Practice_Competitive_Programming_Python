INF = int(1e18)
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp[i][j] = i the station, j refuel times, value: max fuel the tank has
        # dp[i][j] = (k < i) if dp[k][j-1] + gas[k] >= pos[i]-pos[k]: max(dp[k][j-1] - (pos[i]-pos[k]))
        stations.append([target, 0])
        N = len(stations)
        dp = [[-INF for _ in range(N+1)] for _ in range(N+1)]
        dp[0][0] = startFuel
        for i in range(1, N+1):
            for j in range(i):
                if j == 0 and startFuel >= stations[i-1][0]:
                    dp[i][j] = startFuel - stations[i-1][0]
                    continue

                for k in range(1, i): # k < i
                    pos_i = stations[i-1][0]; pos_k = stations[k-1][0]
                    if dp[k][j] >= pos_i - pos_k:
                        dp[i][j] = max(dp[i][j], dp[k][j] - (pos_i - pos_k))

                    fuel_k = stations[k-1][1]
                    if j > 0 and dp[k][j-1] + fuel_k >= pos_i - pos_k:
                        dp[i][j] = max(dp[i][j], dp[k][j-1] + fuel_k - (pos_i - pos_k))

        for i in range(N+1):
            if dp[N][i] >= 0:
                return i
        return -1
