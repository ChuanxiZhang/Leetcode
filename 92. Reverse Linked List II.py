# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        times = n - m
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while m - 1:
            pre = pre.next
            m -= 1
        start = pre.next
        nxt = start.next

        while times:
            start.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = start.next
            times -= 1
        return dummy.next
            
