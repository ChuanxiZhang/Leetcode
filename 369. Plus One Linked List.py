# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        value = 0
        res = cal = ListNode(0)
        while head:
            value = value * 10 + head.val
            head = head.next
        value = str(value + 1)
        for s in value:
            a = ListNode(s)
            cal.next = a
            cal = a
        return res.next

