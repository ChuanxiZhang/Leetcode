class Solution(object):
    def romanToInt(self, s):
        trans_table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        previous = result = 0
        for i in range(len(s)-1, -1, -1):
            now = trans_table[s[i]];
            if previous > now:
                result -= now
            else:
                result += now
            previous=now
        return result

solution = Solution()
print solution.romanToInt('MMMCMXCIX')
