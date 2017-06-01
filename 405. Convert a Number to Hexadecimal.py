class Solution(object):
    def toHex(self, num):
        if num==0:
            return '0'
        mp="0123456789abcdef"
        res=''
        for i in range(8):
            n=num&15
            c=mp[n]
            res=c+res
            num=num>>4
        return res.lstrip('0')