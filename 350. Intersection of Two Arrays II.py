class Solution(object):
    def intersect(self, nums1, nums2):
        result =list()
        for n in nums1:
            for m in nums2:
                if n==m:
                    result.append(m)
                    nums2.remove(m)
                    break
        return result

solution =Solution()
print solution.intersect([1,2,2,3],[2,2])