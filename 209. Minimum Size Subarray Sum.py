class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        sums = 0
        res = len(nums) + 1
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                res = min(res, i + 1 - left)
                sums -=nums[left]
                left += 1
        return res if res != len(nums) + 1 else 0

if __name__ == '__main__':
    sol = Solution()
    s = 10
    nums = [1,4,6,7,23,10,3,-2,-10,10]
    print sol.minSubArrayLen(s, nums)
