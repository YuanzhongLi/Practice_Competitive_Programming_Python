from sys import stdin

input = stdin.readline


def lengthOfLIS(A: list[int]) -> int:
    DP = []
    for a in A:
        if (not DP) or DP[len(DP) - 1] < a:
            # DPが空の場合追加
            # DP[len(DP)-1]：現状の最長の増加列の最終要素
            # その最終要素よりaが大きいとき、その増加列にaを追加することで1つ長い増加列が作れる
            DP.append(a)
        else:
            ok, ng = len(DP) - 1, -1
            # ng = -1は大丈夫なのか？（-1はアクセスする要素がない）
            # なぜかというと、実際にアクセスするのはmid = (ok+ng) // 2
            # mid == -1となるのはok = 0, ng = -1のときのみ
            # このときはabs(ok - ng) > 1が条件を満たさないのでそもそもwhile文に入らない
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                # 以上（<=）でいいのか？
                # ex). DP = [1,2,4,6], a = 4だとDP[2] = 4で同じ値を代入するだけ
                # ex). DP = [1,2,5,6], a = 4だとDP[2] = 4となり更新される
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
