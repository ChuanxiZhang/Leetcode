# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=dummy2=head
        length=0
        while dummy:
            length+=1
            dummy=dummy.next
        if length-n==0:
            return head.next
        else:
            delete=length-n-1
            while delete:
                delete-=1
                dummy2=dummy2.next
        if dummy2.next.next:
            dummy2.next=dummy2.next.next
        else:
            dummy2.next=None
        return head