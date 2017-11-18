# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = (len(lists)) >> 1
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.Merge(left, right)

    def Merge(self, left, right):
        dummy = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        res.next = left or right
        return dummy.next



