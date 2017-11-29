class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        total = 0
        sign = [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i<len(s) and s[i]. isdigit():
                    i += 1
                total += sign.pop() * int(s[start:i])
                continue
            if c in '+-(':
                sign.append(sign[-1] * (1,-1)[c == '-'])
            if c == ')':
                sign.pop()
            i += 1
        return total








                
