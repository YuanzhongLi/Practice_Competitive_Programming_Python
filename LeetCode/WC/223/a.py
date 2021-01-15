class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = []
        ret.append(first)
        for i, a in enumerate(encoded):
            ret.append(ret[-1]^encoded[i])
        return ret
