class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ht = collections.defaultdict(lambda:[])

        for s in strings:
            standard = ord(s[0]) - ord('a')
            key = ""
            for i in range(len(s)):
                key_c = ord(s[i]) - standard
                if key_c < ord('a'):
                    key_c += 26
                key += chr(key_c)
            ht[key].append(s)
        return ht.values()
            
