class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        pro=1
        zcnt=0
        for i in range(len(nums)):
            if nums[i]!=0:
                pro*=nums[i]
            if nums[i]==0:
                zcnt+=1
        if zcnt>1:
            return [0]*len(nums)
        for j in range(len(nums)):
            if zcnt==1:
                if nums[j]==0:
                    ans[j]=pro
                else:
                    ans[j]=0
            if zcnt==0:
                ans[j]=pro//nums[j]
        return ans
            