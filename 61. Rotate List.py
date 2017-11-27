# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        l = head
        while l:
            length += 1
            l = l.next
        if not head:
            return
        k %= length
        if k == 0:
            return head
        cur = head
        k = length- 1 - k
        while k:
            k -= 1
            cur = cur.next

        res = cur.next
        mid = cur.next
        cur.next = None
        while mid.next:
            mid = mid.next
        mid.next = head

        return res



        
