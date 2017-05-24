class Solution(object):
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for pos in range(len(nums)-2):
            if pos>0 and nums[pos]==nums[pos-1]:
                continue
            head,rare=pos+1,len(nums)-1
            while head<rare:
                sum=nums[pos]+nums[head]+nums[rare]
                if sum>0:
                    rare-=1
                if sum<0:
                    head+=1
                else:
                    res.append([nums[pos],nums[head],nums[rare]])
                    while head<rare and nums[head+1]==nums[head]:
                        head+=1
                    while head<rare and nums[rare-1]==nums[rare]:
                        rare-=1
                    head+=1
                    rare-=1
        return res
s=Solution()
print s.threeSum([-1,0,1,2,-1,-4])