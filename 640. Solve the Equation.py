class Solution(object):
    def breakIt(self, part):
        temp = ""
        res=[]
        for s in part:
            if s in "+-":
                if len(temp) > 0:
                       res.append(temp)
                if s == "+":
                    temp = ""
                if s == "-":
                    temp = s
            else:
                temp += s
        res.append(temp)
        return res

    def deflag(self, x):
        if len(x) > 1 and "0" <= x[-2] <= "9":
            res = x.replace('x', '')
        else:
            res = x.replace('x', '1')
        print res
        return res

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        lp, rp = 0, 0
        part = equation. split("=")
        for emt in self.breakIt(part[0]):
            if emt.count("x") > 0:
                lp += int(self.deflag(emt))
            else:
                rp -= int(emt)

        for emt in self.breakIt(part[1]):
            if emt.count("x") > 0:
                lp -= int(self.deflag(emt))
            else:
                rp += int(emt)
        if lp == 0:
            if rp == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(rp / lp)







        
