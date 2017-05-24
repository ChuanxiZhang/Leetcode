class MyQueue(object):
    def __init__(self):
        self.arr = list()

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        return self.arr.pop(0)

    def peek(self):
        if self.arr:
            return self.arr[0]
        else:
            return []

    def empty(self):
        if not self.arr:
            return True
        return False



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()