class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows>=len(s):
            return s
        list =['']*numRows
        index,step=0,1
        for str in s:
            list[index]+=str
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step
        return ''.join(list)

solution = Solution()
print solution.convert("PAYPALISHIRING",3)