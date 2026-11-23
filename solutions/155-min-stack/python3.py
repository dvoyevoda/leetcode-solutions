class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None
        self.min_list = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_val == None:
            self.min_val = value
            self.min_list.append(self.min_val)
        elif value <= self.min_val:
            self.min_val = value
            self.min_list.append(self.min_val)

    def pop(self) -> None:
        if self.min_val == self.stack[-1]:
            self.min_list.pop()
            if self.min_list:
                self.min_val = self.min_list[-1]
            else:
                self.min_val = None
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()