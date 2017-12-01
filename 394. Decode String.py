class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count, res = [] , [""]
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while s[i+1].isdigit():
                    i+=1
                count.append(int(s[start:i+1]))
            elif s[i] == '[':
                res.append("")
            elif s[i] == ']':
                times = count.pop()
                strnow = res.pop()*times
                res.append(res.pop()+strnow)
            else:
                res.append(res.pop() + s[i])
            i+=1
        return res.pop()
                
