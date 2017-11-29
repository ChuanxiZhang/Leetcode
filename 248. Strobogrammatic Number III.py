class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        len_1 = len(low)
        len_2 = len(high)
        arr = []
        res = 0
        for i in range(len_1, len_2 + 1):
            arr.extend(self.helper(i,i))
        low = int(low)
        high = int(high)
        for num in arr:
            if low <= int(num) <= high:
                res += 1
        return res

    def helper(self, n ,m):
        if n == 1:
            return ["1", "8", "0"]
        if n == 0:
            return [""]

        arr = self.helper(n - 2, m)
        res = []
        for num in arr:
            if not n == m:
                res.append("0" + num + "0")
            res.append("1" + num + "1")
            res.append("8" + num + "8")
            res.append("6" + num + "9")
            res.append("9" + num + "6")
        return res
