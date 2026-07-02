class Solution:
    def validPalindrome(self, s: str) -> bool:
        low=0
        high=len(s)-1
        def helper(low,high):
            while low<high:
                if s[low]!=s[high]:
                    return False
                low+=1
                high-=1
            return True
        while low<high:
            if s[low]!=s[high]:
                return helper(low+1,high) or helper(low,high-1)
            low+=1
            high-=1
        return True
        