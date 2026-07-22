class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnd1=0
        cnd2=0
        cnt1=0
        cnt2=0
        ans=[]
        for i in nums:
            if i == cnd1:
                cnt1+=1
            elif i ==cnd2:
                cnt2+=1
            elif cnt1==0:
                cnd1=i
                cnt1=1
            elif cnt2==0:
                cnd2=i
                cnt=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=0
        cnt2=0
        for i in nums:
            if i == cnd1:
                cnt1+=1
            if i== cnd2:
                cnt2+=1
        if cnt1>(len(nums)//3):
            ans.append(cnd1)
        if cnt2>(len(nums)//3):
            ans.append(cnd2)
        return ans
            
