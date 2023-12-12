from sys import stdin

input = stdin.readline


def largestSquare(H: int, W: int, tiles: list[list[int]]) -> int:
    dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
    max_length = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if tiles[i - 1][j - 1] == 0:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_length = max(max_length, dp[i][j])

    return max_length * max_length


H, W = map(int, input().rstrip().rsplit())
tiles = []
for _ in range(H):
    tile_row = list(map(int, input().rstrip().rsplit()))
    tiles.append(tile_row)

print(largestSquare(H, W, tiles))
