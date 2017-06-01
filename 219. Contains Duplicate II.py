class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        ht = dict()
        for i in range(len(nums)):
            if ht.has_key(nums[i]):
                if i - ht[nums[i]] <= k:
                    return True
                else:
                    ht[nums[i]] = i
            else:
                ht[nums[i]] = i
        return False

