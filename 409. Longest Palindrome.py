class Solution(object):
    def longestPalindrome(self, s):
        list=list()
        count=0
        for i in s:
            if i not in list:
                list.append(i)
            else:
                count+=2
                list.remove(i)
        return count+1 if len(list)>0 else count
