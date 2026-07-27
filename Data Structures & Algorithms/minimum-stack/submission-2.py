class MinStack:

    def __init__(self):
        self.minStack=[]
        self.s2=[]

    def push(self, val: int) -> None:
        self.s2.append(val)
        if self.minStack:
            val=min(val,self.minStack[-1])
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.s2.pop()


    def top(self) -> int:
        return self.s2[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
