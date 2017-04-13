from collections import defaultdict
class Solution(object):
    def countAndSay(self, n):
        arr=defaultdict(int)
        def count(nums,n):
            res=""
            arr = defaultdict(int)
            if n==0:
                return nums
            for i in nums:
                arr[i]+=1
            for a in set(nums):
                res+=(str(arr[a])+a)
            return count(res,n-1)
        return int(count("1",n))

solution=Solution()
print solution.countAndSay(3)
