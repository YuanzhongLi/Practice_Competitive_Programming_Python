# Solution Link: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/solutions/6805867/python-bfs-solution-with-japanese-explan-czcr/

from collections import deque


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        N = len(status)
        opend = [False for _ in range(N)]
        # 箱はあるが鍵がない
        waitedBoxes = set([])
        # 開ける箱をキューに入れていく
        q = deque([])
        for i in initialBoxes:
            if status[i] == 1:
                q.append(i)
            else:
                waitedBoxes.add(i)

        ans = 0
        while q:
            u = q.popleft()
            if opend[u]:
                continue
            opend[u] = True
            ans += candies[u]

            # 鍵がある箱はopenな状態となる
            for k in keys[u]:
                status[k] = 1
                if k in waitedBoxes:
                    q.append(k)
                    waitedBoxes.remove(k)

            for b in containedBoxes[u]:
                if status[b] == 1:
                    q.append(b)
                else:
                    waitedBoxes.add(b)

        return ans
