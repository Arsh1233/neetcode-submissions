class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if stack and c=="}" and stack[-1]=="{":
                stack.pop()
            elif stack and c==")" and stack[-1]=="(":
                stack.pop()
            elif stack and c=="]" and stack[-1]=="[":
                stack.pop()
            elif c=="(" or c=="[" or c=="{":
                stack.append(c)
            else:
                return False
        return False if stack else True