class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordhash = {}
        degreehash = {}
        hashset =[]
        for i in words:
            for j in i:
                degreehash[j] = 0

        for i in range(len(words)-1):
            cur = words[i]
            next = words[i+1]
            length = min(len(cur), len(next))
            for j in range(length):
                c1 = cur[j]
                c2 = next[j]
                if not c1 == c2:
                    hashset = []
                    if c1 in wordhash:
                        hashset = wordhash.get(c1)
                    if c2 not in hashset:
                        hashset.append(c2)
                        wordhash[c1] = hashset
                        degreehash[c2] += 1
                    break

        queue, result = [], ""
        print wordhash
        for i in degreehash.keys():
            if degreehash[i] == 0:
                 queue.append(i)
        while len(queue)>0:
            res = queue.pop()
            result += res
            if res in wordhash.keys():
                for c2 in wordhash[res]:
                    degreehash[c2] -= 1
                    if degreehash[c2] == 0:
                        queue.append(c2)
        if not len(result) == len(degreehash): return ""
        return result






            
