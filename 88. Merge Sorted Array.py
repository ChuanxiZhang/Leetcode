class Solution(object):
    def merge(self, nums1, m, nums2, n):
        length=m+n-1
        len1=m-1
        len2=n-1
        while len1>=0 and len2>=0:
            if nums1[len1]>nums2[len2]:
                nums1[length]=nums1[len1]
                len1-=1
                length-=1
            else:
                nums1[length]=nums2[len2]
                len2-=1
                length-=1
        while len2>=0:
                nums1[length]=nums2[len2]
                len2-=1
                length-=1