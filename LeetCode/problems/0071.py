class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        A  = path.split('/')
        for a in A:
            if a == '.' or a == '':
                continue
            elif a == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(a)
        ans = '/'.join(stack)
        return '/' + ans
