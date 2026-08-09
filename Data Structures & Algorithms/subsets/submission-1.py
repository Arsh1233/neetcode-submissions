class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        for i in range(1<<n):
            res=[]
            for j in range(n):
                if (i&1<<j!=0):
                    res.append(nums[j])
            ans.append(res)
        return ans
