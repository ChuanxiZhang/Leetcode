class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = 1
        cur_A = A
        while len(cur_A) < len(B):
            count += 1
            cur_A += A

        if B in cur_A:
            return count
        if B in (cur_A + A):
            return count + 1
        else:
            return - 1


        
