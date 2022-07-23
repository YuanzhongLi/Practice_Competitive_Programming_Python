class Logger:
    def __init__(self):
        self.mp = {}

    def shouldPrintMessage(self, t: int, msg: str) -> bool:
        mp = self.mp
        if msg not in mp:
            mp[msg] = t
            return True
        else:
            if t - mp[msg] >= 10:
                mp[msg] = t
                return True
            else:
                return False
