class Solution(object):
    def smallestRange(self, A):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(row[0], cur_arr, 0) for cur_arr, row in enumerate(A)]
        heapq.heapify(pq)
        res = (-sys.maxint, sys.maxint)
        right = max(row[0] for row in A)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < res[1] - res[0]:
                res = (left, right)
            if j + 1 == len(A[i]):
                return res
            cur = A[i][j + 1]
            right = max(right, cur)
            heapq.heappush(pq,(cur, i, j + 1))
                
