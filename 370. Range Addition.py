class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for i in updates:
            start, end, val = i[0], i[1], i[2]
            res[start] += val
            if (end < len(res) - 1) :res[end+1] -= val

        for i in range(1,len(res)):
            res[i]+=res[i-1]
        return res
