class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=int((l+r)/2)
            time=0
            for x in piles:
                time+=math.ceil(x/mid)
            if time>h:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res