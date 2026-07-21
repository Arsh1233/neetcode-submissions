class Solution:
    def firstUniqChar(self, s: str) -> int:
        hasmap={}
        for i in s:
            hasmap[i] = 1 + hasmap.get(i,0)
        for i in range(len(s)):
            if hasmap[s[i]]==1:
                return i
        return -1