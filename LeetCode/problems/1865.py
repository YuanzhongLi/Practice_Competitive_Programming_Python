# Solution Link: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/solutions/6925419/python-hash-table-solution-with-japanese-4zwn/


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = defaultdict(int)
        for num in nums2:
            self.cnt[num] += 1

    def add(self, index: int, val: int) -> None:
        nums2, cnt = self.nums2, self.cnt
        cur_val = nums2[index]
        nums2[index] += val
        cnt[cur_val] -= 1
        cnt[nums2[index]] += 1

    def count(self, tot: int) -> int:
        nums1, cnt = self.nums1, self.cnt
        ret = 0
        for num in nums1:
            ret += cnt[tot - num]
        return ret


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
