class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n + 1)
        factorial = [1]
        mul = 1
        for i in range(1, n + 1):
            mul *= i
            factorial.append(mul)
        k -= 1
        res = ""
        for i in range(1, n + 1):
            index = k / factorial[n - i]
            res += str(nums[index])
            nums.pop(index)
            k -= index * factorial[n - i]
        return res


            
