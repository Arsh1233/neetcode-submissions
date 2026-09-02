class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        res=0
        while low<=high:
            mid=int((low +high )/2)
            if (mid*mid)==x:
                return mid  
            elif (mid*mid)<x :
                res=mid
                low=mid+1
            else:
                high=mid-1
        return int(res)