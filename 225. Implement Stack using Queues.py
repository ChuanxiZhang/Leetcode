class MyStack(object):
    def __init__(self):
        self.arr = list()

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        return self.arr.pop(-1)

    def top(self):
        return self.arr[-1]

    def empty(self):
        if not self.arr:
            return True
        return False



        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()