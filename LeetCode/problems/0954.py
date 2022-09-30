from collections import defaultdict
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        zero = 0
        neg = []
        pos = []
        for a in A:
            if a > 0:
                pos.append(a)
            elif a < 0:
                neg.append(a)
            else:
                zero += 1

        if zero % 2 != 0:
            return False

        neg.sort()
        neg.reverse()
        pos.sort()

        neg_dict = defaultdict(int)
        pos_dict = defaultdict(int)
        for ne in neg:
            neg_dict[ne] += 1

        for po in pos:
            pos_dict[po] += 1


        for key in neg_dict:
            if neg_dict[key] == 0:
                continue
            if neg_dict[key * 2] < neg_dict[key]:
                return False

            neg_dict[key * 2] -= neg_dict[key]
            neg_dict[key] = 0

        for key in neg_dict:
            if neg_dict[key] != 0:
                return False

        for key in pos_dict:
            if pos_dict[key] == 0:
                continue
            if pos_dict[key * 2] < pos_dict[key]:
                return False

            pos_dict[key * 2] -= pos_dict[key]
            pos_dict[key] = 0

        for key in pos_dict:
            if pos_dict[key] != 0:
                return False

        return True
