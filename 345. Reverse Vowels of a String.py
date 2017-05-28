class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        head, rare = 0, len(s) - 1
        while head < rare:
            if s[head] not in "AOEUIaoeui":
                head += 1
            elif s[rare] not in "AOEUIaoeui":
                rare -= 1
            elif s[head] in "AOEUIaoeui" and s[rare] in "AOEUIaoeui":
                s[head], s[rare] = s[rare], s[head]
                head += 1
                rare -= 1
        return "".join(s)
