class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        maxval = num
        num_s = list(str(num))
        for i in range(len(num_s)):
            for j in range(i):
                num_s[i], num_s[j] = num_s[j], num_s[i]
                maxval = max(maxval, int("".join(num_s)))
                num_s = list(str(num))
        return maxval
