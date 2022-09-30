from collections import defaultdict
class Solution:
    def isPossible(self, A: List[int]) -> bool:
        mem = defaultdict(int) # memo the number of each element in list
        array = [[A[0]]]
        for i in range(1, len(A)):
            mem[A[i]] += 1

        for key in mem:
            val = mem[key]
            for i in range(len(array)-1, -1, -1): # reverse order
                if val <= 0:
                    break
                else:
                    if key == array[i][-1] + 1:
                        array[i].append(key)
                        val -= 1
                    else:
                        break

            while val > 0:
                array.append([key])
                val -= 1

        for ar in array:
            if len(ar) < 3:
                return False

        return True
