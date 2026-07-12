class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        cost=0
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            cost=prices[i]
            profit=max(profit,cost-mini)
        return profit
            