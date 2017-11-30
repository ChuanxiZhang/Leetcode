class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def find(node, pos):
            while node[pos] != pos:
                node[pos] = node[node[pos]]
                pos = node[pos]
            return pos
        count = n
        node = [i for i in range(n)]
        for edge in edges:
            node1 = find(node, edge[0])
            node2 = find(node, edge[1])
            if not node1 == node2:
                count -= 1
                node[node1] = node2
            else:
                return False
        return count == 1

        
