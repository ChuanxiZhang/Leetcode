class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        new_sen = sentence.strip().split()
        for i in range(len(new_sen)):
            for j in dict:
                l = len(j)
                if len(new_sen[i]) >= l:
                    card = new_sen[i][:l]
                    if j  == card:
                        new_sen[i] = j
        return " ".join(new_sen)
                    
