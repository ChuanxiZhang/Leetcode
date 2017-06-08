# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a, b = 0, 0
        while l1:
            a *= 10
            a += l1.val
            l1 = l1.next
        while l2:
            b *= 10
            b += l2.val
            l2 = l2.next
        res = ListNode(0)
        cres = res
        for i in str(a + b):
            cres.next = ListNode(int(i))
            cres = cres.next
        return res.next
