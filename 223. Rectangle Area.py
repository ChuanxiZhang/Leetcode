class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = 0
        area1 = abs(C - A) * abs(D - B)
        area2 = abs(G - E) * abs(H - F)
        left = max(A, E)
        right = min(C, G)
        bottom = max(B, F)
        top = min(D, H)
        if right > left and top > bottom:
            overlap = abs(left - right) * abs(bottom - top)
        return area1 + area2 - overlap        
