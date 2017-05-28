class Solution(object):
    def checkRecord(self, s):
        return s.count("A") < 2 and reduce(max, map(len, re.split(r'A|P', s))) < 3

