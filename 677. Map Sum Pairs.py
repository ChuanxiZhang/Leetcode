class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(lambda:0)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum_num = 0
        for key , val in self.dic.items():
            length = len(prefix)
            if length <= len(key):
                if key[:length] == prefix:
                    sum_num += val
        return sum_num


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
