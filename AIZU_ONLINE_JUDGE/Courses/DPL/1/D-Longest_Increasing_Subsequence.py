from sys import stdin

input = stdin.readline


def lengthOfLIS(A: list[int]) -> int:
    DP = []
    for a in A:
        if (not DP) or DP[len(DP) - 1] < a:
            DP.append(a)
        else:
            ok, ng = len(DP) - 1, -1
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if a <= DP[mid]:
                    ok = mid
                else:
                    ng = mid

            DP[ok] = a

    return len(DP)


N = int(input().rstrip())
A = []
for _ in range(N):
    a = int(input().rstrip())
    A.append(a)


print(lengthOfLIS(A))
