class Solution(object):
    def topKFrequent(self, nums, k):
        arr = sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return [arr[i][0] for i in range(0, k)]
