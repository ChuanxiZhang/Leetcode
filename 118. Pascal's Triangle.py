class Solution(object):
    def generate(self, numRows):
        str=[[1]]
        for _ in range(numRows):
            str+=[map(lambda x,y:x+y,str[-1]+[0],[0]+str[-1])]
        return str[:numRows]