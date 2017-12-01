class Solution(object):
    def reverseString(self, s):
        list1 = list()
        list2 = list()
        list1 = s
        for i in range(0,len(list1))[::-1]:
            list2.append(list1[i])
        return ''.join(list2)
