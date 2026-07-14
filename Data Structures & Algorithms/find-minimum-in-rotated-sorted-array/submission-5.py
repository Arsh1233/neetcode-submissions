class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        mini=1001
        while low<=high:
            mid=low+(high-low)//2
            if nums[low]<=nums[mid]:
                if nums[low]<mini:
                    mini=nums[low]
                low=mid+1
            else:
                if nums[mid]<mini:
                    mini=nums[mid]
                high=mid-1
        return mini
                