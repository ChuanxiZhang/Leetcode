# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.val = []
        while head:
            self.val.append(head.val)
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        pos = random.randint(0,len(self.val)-1)
        return self.val[pos]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
