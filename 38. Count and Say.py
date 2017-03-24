class Solution(object):
    def countAndSay(self, n):
        start = '1'
        def countnum(n):
            count = 1
            for j in range(len(start)):
                if start[j] != start[j - 1]:
                    return count
                    count = 1
                else:
                    count += 1
                    
        if n == 1:
            return start
        else:
            for i in range(1, n - 1):
                start=
