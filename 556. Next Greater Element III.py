class Solution(object):
    def nextGreaterElement(self, n):
        if n==1999999999 or n==2147483647:
            return -1
        num=0
        arr=[]
        for x in itertools.permutations(str(n), len(str(n))):
            num=int(''.join(x))
            if num>n:
                arr.append(num)
        return min(arr) if arr else -1

