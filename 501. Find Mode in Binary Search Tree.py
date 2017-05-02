class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        arr=collections.Counter()
        def dfs(node):
           if node:
               arr[node.val]+=1
               dfs(node.left)
               dfs(node.right)
        dfs(root)
        max_value=max(arr.itervalues())
        return [num for num,value in arr.iteritems() if value==max_value]