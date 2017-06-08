class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        str = re.findall('^[+\-]?\d+', str)
        try:
            res = int(''.join(str))
            if res > 2147483647:
                return 2147483647
            if res < -2147483648:
                return -2147483648
            return res
        except:
            return 0
