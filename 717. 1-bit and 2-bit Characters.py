class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        end = len(bits) - 1
        i = 0
        while i < end:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == end
            
