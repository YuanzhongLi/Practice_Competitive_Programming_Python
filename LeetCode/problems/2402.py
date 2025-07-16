# Solution Link: https://leetcode.com/problems/meeting-rooms-iii/solutions/6944638/python-2-heap-solution-with-japanese-exp-9ddp/

from heapq import heapify, heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # (freeTime, roomId)
        # 各roomが使用可能になる時間とidが要素となるheap
        heap = [(0, i) for i in range(n)]
        heapify(heap)

        # 現時刻（今見ているmeetingのstart時刻）で使用可能なroomのidが要素となるheap
        heap2 = []

        cnt = [0 for _ in range(n)]

        for s, e in meetings:
            # 時刻sにおいて使用可能なルームをheapからheap2に移しておく
            while len(heap) > 0 and heap[0][0] <= s:
                free_time, room_id = heappop(heap)
                heappush(heap2, room_id)

            # 時刻sにおいて使用可能なroomがあるなら最小のidのroomを使用
            if len(heap2) > 0:
                room_id = heappop(heap2)
                cnt[room_id] += 1
                heappush(heap, (e, room_id))
            else:  # そうでないならfreeになる時間が最も小さいroomを使用
                free_time, room_id = heappop(heap)
                cnt[room_id] += 1
                heappush(heap, (free_time + e - s, room_id))

        ans = -1
        ma = -1
        for i, c in enumerate(cnt):
            if c > ma:
                ma = c
                ans = i

        return ans
