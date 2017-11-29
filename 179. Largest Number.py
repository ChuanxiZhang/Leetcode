class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = map(str,nums)
        num.sort(cmp = lambda x, y: cmp(x + y, y + x), reverse = True)
        return ''.join(num).lstrip('0') or '0'


        
