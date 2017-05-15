class TwoSum(object):
    def __init__(self):
        self.arr = dict()

    def add(self, number):
        self.arr[number] = self.arr.get(number, 0) + 1

    def find(self, value):
        for i in self.arr.keys():
            j = value - i
            if j == i and self.arr.get(j) > 1 or j != i and self.arr.get(j) > 0:
                return True
        return False



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)