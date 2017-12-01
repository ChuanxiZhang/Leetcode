class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        res = 0
        diff = -sys.maxint
        distance = 0
        for nut in nuts:
            distance = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            res += 2 * distance
            diff = max(diff, distance - (abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1])))

        return res - diff
