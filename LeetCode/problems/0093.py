def insert_dots(s, dots):
    ret = ""
    dot_idx = 0
    for i, ch in enumerate(s):
        ret += ch
        if dot_idx < 3 and dots[dot_idx] == i:
            ret += '.'
            dot_idx += 1

    return ret

def is_valid(ip):
    for e in ip.split('.'):
        n = int(e)
        if e[0] == '0' and not (n == 0 and len(e) == 1):
            return False
        if not (0 <= n and n <= 255):
            return False

    return True

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        dots = []
        ans = []
        def dfs(start_idx):
            rest_dot = len(dots) - 3
            if rest_dot == 0:
                ip = insert_dots(s, dots)
                if is_valid(ip):
                    ans.append(ip)
                return

            unused_dot = N - 1 - start_idx
            if rest_dot > unused_dot:
                return

            for i in range(start_idx, N-1):
                dots.append(i)
                dfs(i+1)
                dots.pop()

        dfs(0)

        return ans
