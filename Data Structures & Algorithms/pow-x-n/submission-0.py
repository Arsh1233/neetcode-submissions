class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        exp=abs(n)
        if x==0:
            return 0
        if n==0:
            return 1
        while exp>0:
            if exp%2==1:
                ans*=x
                exp-=1
            x=x*x
            exp/=2
        if n<0 :
            return 1.0/ans
        return ans