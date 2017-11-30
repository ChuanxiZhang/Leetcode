class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        less_than_twenty= ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        bignumber = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return less_than_twenty[num] + " "
            elif num < 100:
                return tens[num / 10] +" "+helper(num % 10)
            else:
                return less_than_twenty[num / 100] + " "+"Hundred" + " " + helper(num % 100)


        if num == 0:
            return 'Zero'
        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + bignumber[i] +" "+ res
            num /= 1000
            i += 1
        return res.strip()
