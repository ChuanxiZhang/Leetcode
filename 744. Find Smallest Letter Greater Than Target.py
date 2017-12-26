class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters.sort()
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        else:
            return letters[0]
        
