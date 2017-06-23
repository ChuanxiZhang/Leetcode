class Solution(object):
    def complexNumberMultiply(self, a, b):
        a,ai,b,bi=map(int, (a[:-1]+'+'+b[:-1]).split('+'))
        return str(a*b-ai*bi)+'+'+str(a*bi+ai*b)+"i"