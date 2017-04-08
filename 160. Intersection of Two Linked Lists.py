# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        lena, lenb = 0, 0
        while ha:
            lena += 1
            ha = ha.next
        while hb:
            lenb += 1
            hb = hb.next
        ha, hb = headA, headB
        if lena > lenb:
            for i in range(lena - lenb):
                ha = ha.next
        if lenb > lena:
            for i in range(lenb - lena):
                hb = hb.next
        while not ha == hb:
            ha=ha.next
            hb=hb.next
        return ha

