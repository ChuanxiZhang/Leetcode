class Solution(object):
    def searchRange(self, nums, target):
        result=[]
        def binarySearch(low,high,target=target):
            mid=(low+high)/2
            while not low==high:
                if nums[mid]==target:
                    result.append(mid)
                    if nums[mid-1]==target:
                        result.append(mid-1)
                        return binarySearch(low, mid-2)
                    elif nums[mid+1]==target:
                        result.append(mid +1)
                        return binarySearch(mid+2, high-1)
                elif nums[mid]<target:
                    return binarySearch(mid,high)
                else:
                    return binarySearch(low,mid)
        binarySearch(0,len(nums),target)
        return result if result else [-1,-1]
solution=Solution()
print solution.searchRange([5,7,7,8,8,10],8)






