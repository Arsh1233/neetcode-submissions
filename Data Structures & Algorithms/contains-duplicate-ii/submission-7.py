class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hasMap={}
        for i in range(len(nums)):
            if nums[i] in hasMap and k>= abs(hasMap[nums[i]]-i):
                return True
            else:
                hasMap[nums[i]]=i    
        return False
