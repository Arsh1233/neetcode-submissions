class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minCost=prices[0]
        cost=0
        for i in range(1,len(prices)):
            minCost=min(minCost,prices[i])
            cost=prices[i]-minCost
            profit=max(cost,profit)
        return profit