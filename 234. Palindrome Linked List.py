# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        val=[]
        while head:
            val.append(head.val)
            head=head.next
        return val==val[::-1]
