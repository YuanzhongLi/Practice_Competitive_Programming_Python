from functools import cmp_to_key

def bits(num):
    ret = 0
    while num > 0:
        if num & 1:
            ret += 1
        num >>= 1

    return ret

def compare(num1, num2):
    bits1, bits2 = bits(num1), bits(num2)
    if bits1 == bits2:
        return num1 - num2
    return bits1 - bits2

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=cmp_to_key(compare))
        return arr
