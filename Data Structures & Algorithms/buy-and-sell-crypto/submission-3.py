class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        curr=prices[0]
        for i in prices:
            curr=min(curr,i)
            profit=max(i-curr,profit)
        return profit