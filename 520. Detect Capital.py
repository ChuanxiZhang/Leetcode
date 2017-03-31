class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper():
            if word[1:].islower():
                return True
            else:
                return False
        else:
            return False
