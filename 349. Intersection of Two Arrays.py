class Solution(object):
    def intersection(self, nums1, nums2):
        result=list()
        for num in nums2:
            if num in nums1:
                result.append(num)
        return list(set(result))

solution =Solution()
print solution.intersection([1,2,2,3],[2,2])