class Solution(object):
    def findComplement(self, num):
        binnum=(bin(num)[2:])
        ox=int(('1'*(len(binnum))),2)
        return int(bin(num^ox),2)

solution= Solution()
print solution.findComplement(1983)