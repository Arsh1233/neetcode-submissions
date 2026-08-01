class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low=1
        res=max(piles)
        high=res
        while low<=high:
            hours=0
            mid=int((low+high)/2)
            for i in piles:
                hours=hours+math.ceil(float(i)/mid)
            if hours<=h:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
                