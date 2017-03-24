# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def listToInt(node):
            return node.val + 10 * listToInt(node.next) if node else 0

        def intToList(num):
            node = ListNode(num % 10)
            if num > 9:
                node.next = intToList(num / 10)
            return node;

        return intToList(listToInt(l1) + listToInt(l2))


solution = Solution()
