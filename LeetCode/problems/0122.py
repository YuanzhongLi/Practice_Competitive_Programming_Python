INF = float('inf')
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_has_stock = -INF
        prev_not_stock = 0
        for p in prices:
            cur_has_stock = max(prev_has_stock, prev_not_stock-p)
            cur_not_stock = max(prev_not_stock, prev_has_stock+p)
            prev_has_stock = cur_has_stock
            prev_not_stock = cur_not_stock

        return cur_not_stock


# best explanation: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/803206/Python-O(n)-by-DP-w-Visualization
