def parse(log):
    str_id, str_type, str_time = log.split(':')
    return int(str_id), str_type, int(str_time)

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret = [0 for _ in range(n)]
        stack = []
        for log in logs:
            id, type, time = parse(log)
            if type == 'start':
                stack.append([time, id, 0])
            else:
                start_time, start_id, mid_time = stack.pop()
                ret[start_id] += (time-start_time+1)-mid_time
                prev_mid = time-start_time+1
                if stack:
                    stack[-1][2] += prev_mid
        return ret
