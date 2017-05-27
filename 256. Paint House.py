class Solution(object):
    def minCost(self, costs):
        res=[0,0,0]
        for cost in costs:
            res=[cost[i]+min(res[:i]+res[i+1:])for i in range(3)]
        return min(res)