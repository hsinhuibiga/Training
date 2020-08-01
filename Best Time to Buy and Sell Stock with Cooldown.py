#Best Time to Buy and Sell Stock with Cooldown

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        prev_sell = 0
        curr_sell = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            temp = curr_sell
            curr_sell = max(curr_sell, hold + prices[i])
            hold = max(hold, (prev_sell if i >= 2 else 0) - prices[i])
            prev_sell = temp
        return curr_sell