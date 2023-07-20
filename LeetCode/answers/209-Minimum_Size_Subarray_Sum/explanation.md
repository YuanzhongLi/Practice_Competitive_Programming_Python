# Intuition & Approach
<!-- Describe your first thoughts on how to solve this problem. -->
- ある範囲の和が```target```以上を確認するのは典型的なSliding Windowの問題。
- [l, r)の範囲の和で考える。
    - 和が```target```未満のときは右(r)を進める
    - 和が```target```以上のときは左(l)を進める

*注意: [ ]は含める, ( )は含めない. 
ex) [2, 5) = [2, 3, 4]
2は含めるが5は含めない


# Complexity
N: ```nums```の長さ

- Time complexity: O(N)
<!-- Add your time complexity here, e.g. O(n) -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. O(n) -->
定数メモリのみ使用。

# Code
```
INF = 1 << 30

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)

        # 最初は[0, 1)の範囲の和を持っているとする
        l, r = 0, 1
        s = nums[l] # [l, r)範囲の和

        ans = INF
        while r < N:
            # 和がtarget未満の時は右に進める
            while s < target and r < N:
                s += nums[r]
                r += 1

            # 和がtarget以上の時は答えの更新をしてから、左に進める
            while s >= target and l < r:
                ans = min(ans, r - l)
                s -= nums[l]
                l += 1

        return ans if ans != INF else 0               
```
