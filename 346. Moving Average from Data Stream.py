class MovingAverage(object):
    def __init__(self, size):
        self.up = size
        self.res = []

    def next(self, val):
        self.res.append(val)
        if len(self.res) <= self.up:
            return round((reduce(lambda x, y: x + y, self.res) / float(len(self.res))), 5)
        else:
            self.res.pop(0)
            return round((reduce(lambda x, y: x + y, self.res) / float(len(self.res))), 5)



            # Your MovingAverage object will be instantiated and called as such:
            # obj = MovingAverage(size)
            # param_1 = obj.next(val)