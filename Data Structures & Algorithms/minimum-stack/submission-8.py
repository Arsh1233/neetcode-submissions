class MinStack:

    def __init__(self):
        self.minstack=[]
        self.stack=[]
        self.mini= 2<<31 -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]