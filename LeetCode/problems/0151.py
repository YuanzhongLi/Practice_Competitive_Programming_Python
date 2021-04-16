def Reverse(s, l=None, r=None):
    if l == None:
        l = 0; r = len(s)
    for i in range(l, (l+r)//2):
        s[i], s[r-1-(i-l)] = s[r-1-(i-l)], s[i]
    return

def Replace(s, l, r, l_, r_):
    for i in range(r-l):
        s[l+i] = s[l_+i]
    for i in range(r, r_):
        s[i] = ' '

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        N = len(s)
        Reverse(s)
        i = 0
        words = 0
        chs = 0
        while i < N:
            if s[i] != ' ':
                l = i
                r = i
                words += 1
                while r+1 < N and s[r+1] != ' ':
                    r += 1
                Reverse(s, l, r+1)
                chs += r-l+1
                i = r
            i += 1
        i = 0; j = 0; k = 0
        while i < N and j < N and k < N:
            if s[i] != ' ':
                i += 1
            elif i > 0 and s[i-1] != ' ':
                i += 1
            else:
                j = i+1
                if j >= N: break
                while j < N and s[j] == ' ':
                    j += 1
                if j >= N: break
                k = j
                while k < N and s[k] != ' ':
                    k += 1
                size = k-j
                Replace(s, i, i+size, j, k)
                i += size
        # print(s, words, chs)
        return ''.join(s[:chs+(words-1)])
