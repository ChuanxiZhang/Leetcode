class Solution(object):
    def reverseWords(self, s):
        list = s.split()
        for i in range(len(list)):
            list[i] = list[i][::-1]
        return " ".join(list)
