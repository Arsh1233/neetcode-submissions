class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        ans=[]
        while low<=high:
            sum_=numbers[low]+numbers[high]
            if sum_==target:
                ans.append(low+1)
                ans.append(high+1)
                return ans
            elif sum_>target:
                high-=1
            else :
                low+=1
        return ans