class Solution(object):
    def wiggleSort(self, nums):
        def comp(x, y):
            if x < y:
                return 1
            elif x > y:
                return -1
            else:
                return 0
        nums.sort(comp)
        i=1
        while i<=(len(nums)-1):
            nums[i],nums[i-1]=nums[i-1],nums[i]
            i+=2