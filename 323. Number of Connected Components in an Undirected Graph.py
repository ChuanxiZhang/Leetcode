class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(node, pos):
            while node[pos] != pos:
                node[pos] = node[node[pos]]
                pos = node[pos]
            return pos

        root = [i for i in range(n)]
        count = n
        for edge in edges:
            root1 = find (root, edge[0])
            root2 = find (root, edge[1])
            if not root1 == root2:
                count -= 1
                root[root1] = root2
        return count
