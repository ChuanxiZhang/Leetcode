class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small, big = sys.maxint, sys.maxint
        for num in nums:
            if num <= small:
                small = num
            elif num <= big:
                big = num
            else:
                return True
        return False
                
