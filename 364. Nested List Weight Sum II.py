# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        if not nestedList:
            return 0
        def dfs(arr, depth, level):
            if len(arr) == 1 and arr[0].isInteger():
                return (depth - level + 1) * arr[0].getInteger()
            res = 0
            for i in range(len(arr)):
                if arr[i].isInteger():
                    res += (depth - level + 1) * arr[i].getInteger()
                else:
                    res += dfs(arr[i].getList(), depth, level + 1)
            return res

        def findDeep(arr):
            deep = 0
            if len(arr) == 1 and arr[0].isInteger():
                return 1
            for i in range(len(arr)):
                if arr[i].isInteger():
                    deep = max(deep, 1)
                else:
                    deep = max(findDeep(arr[i].getList()) + 1, deep)
            return deep

        deep = findDeep(nestedList)

        return dfs(nestedList, deep, 1)

        
