class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            prev=nums[i]
            ans=target-nums[i]
            if target-nums[i] in hashMap:
                return [hashMap[ans],i]
            hashMap[prev]=i