class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnd=nums[0]
        cnt=0
        for i in nums:
            if cnd==i:
                cnt+=1
            if cnd!=i:
                cnt-=1
                if cnt==0:
                    cnd=i
                    cnt=1
        return cnd