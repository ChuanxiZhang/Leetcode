class Solution(object):
    def plusOne(self, digits):
        num=reduce(lambda x,y:x*10+y,digits)+1
        return [int(res) for res in str(num)]
solution =Solution()
print solution.plusOne([1,2,3])

