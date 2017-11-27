class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = collections.defaultdict(lambda:list)
        for s in strs:
            char = str(sorted(s))
            if char in ht:
                ht[char].append(s)
            else:
                ht[char] = [s]
        return ht.values()

        
