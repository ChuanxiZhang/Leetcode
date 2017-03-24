class Solution(object):
    def myAtoi(self, str):
        try:
            return int(str)
        except:
            return 0


solution =Solution()
print solution.myAtoi("+sad")


