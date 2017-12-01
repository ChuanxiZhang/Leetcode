class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        minval = sys.maxint
        maxval =  - sys.maxint
        ht = {}
        for point in points:
            minval = min(minval, point[0])
            maxval = max(maxval, point[0])
            ht[point[0]] = point[1]
        sumval = maxval + minval
        for point in points:
            if sumval - point[0] not in ht.keys() or ht[sumval - point[0]] != ht[point[0]]:
                return False
        return True
