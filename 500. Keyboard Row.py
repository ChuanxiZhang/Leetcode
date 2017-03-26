class Solution(object):
    def findWords(self, words):
        judge=['qwertyuiop','asdfghjkl','zxcvbnm']
        count=0
        result=list()
        for word in words:
            new_word=word.lower()
            for letter in new_word:
                if letter in judge[0]:
                    count+=1
            if count==len(word):
                result.append(word)
            count=0
            for letter in new_word:
                if letter in judge[1]:
                    count+=1
            if count==len(word):
                result.append(word)
            count = 0
            for letter in new_word:
                if letter in judge[2]:
                    count+=1
            if count==len(word):
                result.append(word)
            count = 0
        return result
solution=Solution()
print solution.findWords(['hello','Alaska','Dad','Peace'])