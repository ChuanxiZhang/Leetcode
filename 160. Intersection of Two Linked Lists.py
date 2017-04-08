# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next = node.next
                node.next = prev
                prev = curr
                curr = next
            return prev

        ra = reverse(headA)
        rb = reverse(headB)
        pos = None
        while ra and rb and ra.val == rb.val:
            pos = ra
            ra = ra.next
            rb = rb.next
        headA=reverse(ra)
        headB=reverse(rb)
        return pos
