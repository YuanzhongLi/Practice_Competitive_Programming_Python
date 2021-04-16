class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas += gas
        cost += cost
        i = 0
        while i < N:
            if gas[i] >= cost[i]:
                g = 0; c = 0
                flag = True
                for j in range(N):
                    g += gas[i+j]; c += cost[i+j]
                    if g < c:
                        flag = False
                        i += j
                        break

                if flag:
                    return i
            else:
                i += 1
        return -1
