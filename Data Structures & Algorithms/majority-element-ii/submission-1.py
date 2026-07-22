class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1=0
        cand2=0
        cnt1=0
        cnt2=0
        ans=[]
        for i in nums:
            if i==cand1:
                cnt1+=1
            elif i==cand2:
                cnt2+=1
            elif cnt1==0:
                cand1=i
                cnt1=1
            elif cnt2==0:
                cand2=i
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=0
        cnt2=0
        for i in nums:
            if i==cand1:
                cnt1+=1
            if i==cand2:
                cnt2+=1
        n=len(nums)
        if cnt1> (n//3):
            ans.append(cand1)
        if cnt2> (n//3):
            ans.append(cand2)
        return ans