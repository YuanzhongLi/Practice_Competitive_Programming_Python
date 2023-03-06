class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        digits.reverse()
        carry = 1
        for i in range(N):
            d = digits[i]
            digits[i] = (d + carry) % 10
            carry = (d + carry) // 10

        if carry > 0:
            digits.append(carry)

        digits.reverse()
        return digits
