class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        count = sorted(count.items(), lambda x,y : cmp(x[1],y[1]), reverse = True)
        res =""
        for s, num in count:
            res += s * num
        return res
