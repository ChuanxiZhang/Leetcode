class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        length = len(citations)
        left, right, mid = 0 , length - 1, 0
        while left <= right:
            mid = (left + right) >> 1
            if citations[mid] == (length - mid):
                return length - mid
            elif citations[mid] < (length - mid):
                left = mid + 1
            else:
                right = mid - 1

        return length - left
            
