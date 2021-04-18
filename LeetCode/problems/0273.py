smalls = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
          'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
bigs = ['', 'Thousand', 'Million', 'Billion']
hundred = 'Hundred'

def get3digit(x):
    ret = ''
    hundred_digit = x//100
    if hundred_digit > 0:
        ret += smalls[hundred_digit] + ' ' + hundred + ' '

    ten = x % 100
    if 1 <= ten and ten <= 19:
        ret += smalls[ten] + ' '
    elif ten >= 20:
        ten_digit, one_digit = ten//10, ten%10
        ret += tens[ten_digit] + ' '
        if one_digit > 0:
            ret += smalls[one_digit] + ' '
    return ret[:-1]


class Solution:
    def numberToWords(self, x: int) -> str:
        if x < 20: return smalls[x]
        else:
            A = []
            while x > 0:
                A.append(x%1000)
                x //= 1000

            ret = []
            for i,a in enumerate(A):
                s = get3digit(a)

                if s == '': continue
                if i > 0:
                    s += ' ' + bigs[i]
                ret.append(s)
            ret.reverse()
            return ' '.join(ret)
