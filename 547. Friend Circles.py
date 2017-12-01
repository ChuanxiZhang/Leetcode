
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, cur, visited):
            for i in range(len(M)):
                if M[cur][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    dfs(M, i, visited)
        count = 0
        visited = [0] * len(M)
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M, i, visited)
                count += 1
        return count

            
