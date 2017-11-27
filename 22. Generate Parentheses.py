class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res= []
        left, right = 0, 0
        def generate(rlist, left, right, every, n):
            if left < n:
                generate(res, left+1, right, every+"(", n)
            if right < left:
                generate(res, left, right+1, every+")", n)
            if len(every) == n*2:
                res.append(every)
        generate(res, left, right, "", n)
        return res


    
