class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        res=1001
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]>=nums[low]:
                res=min(res,nums[low])
                low=mid+1
            else:
                res=min(res,nums[mid])
                high=mid-1
        return res
