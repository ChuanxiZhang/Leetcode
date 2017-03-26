class Solution(object):
    def hammingDistance(self, x, y):
        result= bin(x^y)[2:]
        count=0
        for i in result:
            if i=='1':
                count+=1
        return count

solution=Solution()
print solution.hammingDistance(1,4)