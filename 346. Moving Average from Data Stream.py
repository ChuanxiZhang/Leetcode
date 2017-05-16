class MovingAverage(object):
    def __init__(self, size):
        self.up = size
        self.res = []

    def next(self, val):
        self.res.append(val)
        if len(self.res) <= self.up:
        else:
            self.res.pop(0)



            # Your MovingAverage object will be instantiated and called as such:
            # obj = MovingAverage(size)
            # param_1 = obj.next(val)
