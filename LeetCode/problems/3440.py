# Solution Link: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/solutions/6940985/python-enumerate-solution-with-japanese-1tmmu/


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        N = len(startTime)

        spaces = []
        prev_e = 0
        for i in range(N):
            s, e = startTime[i], endTime[i]
            spaces.append(s - prev_e)
            prev_e = e
        spaces.append(eventTime - prev_e)

        space1, space2, space3 = -1, -1, -1
        i1, i2, i3 = -1, -1, -1
        for i, space in enumerate(spaces):
            if space > space1:
                space1, space2, space3 = space, space1, space2
                i1, i2, i3 = i, i1, i2
            elif space > space2:  # space1 >= space
                space2, space3 = space, space2
                i2, i3 = i, i2
            elif space >= space3:  # space2 >= space
                space3 = space
                i3 = i

        ans = 0
        for i in range(N):
            s1, s2 = spaces[i], spaces[i + 1]
            concat_s = s1 + s2
            ans = max(ans, concat_s)
            event_len = endTime[i] - startTime[i]
            if event_len > space1:
                continue
            elif event_len > space2:  # space1 >= event_len
                # space1にevent_lenを入れられるか
                if i != i1 and i + 1 != i1:
                    ans = max(ans, concat_s + event_len)
            elif event_len > space3:  # space2 >= event_len
                # space1またはspace2にevent_lenを入れられるか
                if (i != i1 and i + 1 != i1) or (i != i2 and i + 1 != i2):
                    ans = max(ans, concat_s + event_len)
            else:  # space3 >= event_len
                ans = max(ans, concat_s + event_len)

        return ans
