class Solution:
    def isValid(self, s: str) -> bool:
        hasmap={"}":"{","]":"[",")":"("}
        stack=[]
        for c in s:
            if c in hasmap:
                if stack and hasmap[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False