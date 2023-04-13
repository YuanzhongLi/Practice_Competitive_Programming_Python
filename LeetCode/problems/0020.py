class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    ch_ = stack.pop()
                    if (ch == ')' and ch_ == '(') or (ch == '}' and ch_ == '{') or (ch == ']' and ch_ == '['):
                        continue
                    else:
                        return False

        return len(stack) == 0
