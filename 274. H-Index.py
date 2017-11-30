class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h = 0
        for i in range(len(citations)):
            h = max(h, min(len(citations) - i, citations[i]))
        return h 
