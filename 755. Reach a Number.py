class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        sums = 0
        while sums < target:
            step += 1
            sums += step
        while (sums - target) % 2 != 0:
            step += 1
            sums += step
        return step
