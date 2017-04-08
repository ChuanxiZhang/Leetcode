class Solution(object):
    def mergeTwoLists(self, l1, l2):
        pos= new = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                new.next=l2
                l2=l2.next
            else:
                new.next=l1
                l1=l1.next
            new=new.next
        new=(l1,l2)[not l1]
        return pos.next

