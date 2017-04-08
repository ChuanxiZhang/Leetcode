class Solution(object):
    def convertToTitle(self, n):
        out=""
        while n>0:
            if n%26==0:
                out+=chr(90)
                n=n/27
            else:
                out+=chr((n%26)+64)
                n=n/26%2
        return out[::-1]
solution=Solution()
print solution.convertToTitle(52)


