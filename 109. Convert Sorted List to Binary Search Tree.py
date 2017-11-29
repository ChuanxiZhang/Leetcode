# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        node = head
        runner = head
        arr = []
        while runner:
            arr.append(runner.val)
            runner = runner.next
        length = len(arr)
        return self.buildTree(arr, 0, length - 1)

    def buildTree(self, arr, left, right):
        if left > right:
            return None
        mid = (left + right) >> 1
        treenode = TreeNode(arr[mid])
        treenode.left = self.buildTree(arr, left, mid - 1)
        treenode.right = self.buildTree(arr, mid + 1, right)
        return treenode
