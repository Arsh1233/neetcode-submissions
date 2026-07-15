class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_=0
        for i in nums:
            sum_+=i
        n=len(nums)
        n=(n*(n+1)//2)
        return n-sum_