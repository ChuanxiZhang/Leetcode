class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]+=nums2
        return sorted(nums1)

solution=Solution()
print solution.merge([1],1,[],0)