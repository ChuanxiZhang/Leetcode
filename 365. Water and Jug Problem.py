class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        def GCD(a, b):
            while a:
                a, b = b % a, a
            return b

        return z == x + y or (z < x + y and z % GCD(x, y) == 0)
