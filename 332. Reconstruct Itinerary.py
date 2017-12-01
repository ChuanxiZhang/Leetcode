class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        hash_table = collections.defaultdict(lambda:[])
        tickets.sort(reverse = True)
        for start, end in tickets:
            print start, end
            hash_table[start].append(end)
        print hash_table
        res = []
        def dfs(airport):
            while hash_table[airport]:
                dfs(hash_table[airport].pop())
            res.append(airport)
        dfs('JFK')
        return res[::-1]
        
