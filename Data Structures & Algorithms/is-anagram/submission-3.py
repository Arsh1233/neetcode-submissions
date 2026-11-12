class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap={}
        tmap={}
        for i,n in enumerate(s):
            smap[n] = 1 + smap.get(n,0)
        for i,n in enumerate(t):
            tmap[n] = 1 + tmap.get(n,0)
        print(tmap)
        print(smap)
        if tmap==smap:
            return True
        return False