# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        def construction(value,low,high):
            if low>high:
                return
            else:
                mid=(low+high)/2
                node = TreeNode(value[mid])
                node.left=construction(value,low,mid-1)
                node.right=construction(value,mid+1,high)
                return node
        head = construction(nums,0,len(nums)-1)
        return head

solution=Solution()
print solution.sortedArrayToBST([1,2,3,4,5,6])