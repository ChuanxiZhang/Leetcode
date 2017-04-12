# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        dummy= head
        if not head:
            return head
        while head.next:
            if head.next.next.val==val:
                head.next=head.next.next
            else:
                head=head.next
        if dummy.val==val:
            dummy=dummy.next
        return dummy
