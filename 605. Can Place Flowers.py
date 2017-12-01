class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0]+flowerbed+[0]
        count, flower = 0 ,0

        for i in flowerbed:
            if i == 1:
                flower += (count - 1) / 2
                count = 0
            else: count += 1
        flower += (count - 1) / 2
        return n <= flower
