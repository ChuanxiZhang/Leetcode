class MinStack(object):
    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, x):
        self.arr.append(x)
        if not self.minarr or x <= self.minarr[-1]:
            self.minarr.append(x)

    def pop(self):
        if self.arr and self.minarr and self.arr[-1] == self.minarr[-1]:
            self.arr.pop()
            self.minarr.pop()
        else:
            self.arr.pop()

    def top(self):
        return self.arr[-1] if self.arr else[]

    def getMin(self):
        return self.minarr[-1] if self.minarr else[]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()