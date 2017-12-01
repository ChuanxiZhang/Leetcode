class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dict = dict


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        judge = [False] * len(word)
        for dict_word in self.dict:
            if len(word) != len(dict_word):
                continue
            else:
                i = 0
                while i < len(word):
                    if word[i] == dict_word[i]:
                        judge[i] = True
                    i += 1
                if judge.count(False) == 1:
                    return True
            judge = [False] * len(word)
        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
