class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                res=stack.pop()
                stack.append(res+stack.pop())
            elif i=="-":
                res=stack.pop()
                stack.append(stack.pop()-res)
            elif i=="*":
                res=stack.pop()
                stack.append(res*stack.pop())
            elif i=="/":
                res=stack.pop()
                stack.append(int(float(stack.pop())/res))
            else:
                stack.append(int(i))
        return stack[-1]