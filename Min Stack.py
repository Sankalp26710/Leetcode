class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=[]
        self.min=[float('inf')]

    def push(self, x: int) -> None:
        self.stk.append(x)
        if x <= self.min[-1]: self.min.append(x)
        
    def pop(self) -> None:
        x=self.stk.pop()
        if x == self.min[-1]: self.min.pop()
        return self.stk

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1]
