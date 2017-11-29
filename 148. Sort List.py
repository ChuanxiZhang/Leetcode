# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def merge_sort(l1, l2):
        p = ListNode(0)
        res = p
        while l1 and l2:
            if  l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        if l1:
            p.next = l1
            l1 = l1.next
        if l2:
            p.next = l2
            l2 = l2.next

        return res.next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prev = None
        slow, fast = head, head
        while not fast == None and not fast.next == None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return merge_sort(l1, l2)



        
