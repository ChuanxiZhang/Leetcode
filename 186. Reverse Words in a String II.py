class Solution(object):
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """

        s.reverse()
        start = 0;
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                s[start:i] = s[start:i][::-1]
                start = i + 1
        
