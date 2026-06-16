class MinStack:

    def __init__(self):
        self.stack = []
        self.minL = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.minL.append(val)
        if self.minL and val <= self.minL[-1]:
            self.minL.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minL[-1]:
            self.minL.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minL[-1]
        
