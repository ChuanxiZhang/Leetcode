class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.data = re.findall(r"([a-zA-Z])(\d+)",compressedString)
        self.count, self.index = 0, -1

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.count -= 1
            return self.data[self.index][0]
        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count == 0 and self.index + 1 < len(self.data):
            self.index += 1
            self.count = int(self.data[self.index][1])
        return self.count > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
