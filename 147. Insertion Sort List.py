# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        cur = head
        pre = start

        while cur:
            next = cur.next
            while pre.next != None and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = start
            cur = next
        return start.next


            
