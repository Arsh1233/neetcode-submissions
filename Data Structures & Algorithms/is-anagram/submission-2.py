class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack=[]
        if len(t)!=len(s):
            return False
        for i in range(len(s)):
            stack.append(s[i])
        for i in range(len(s)):
            if t[i] in stack:
                stack.remove(t[i])
        return False if stack else True