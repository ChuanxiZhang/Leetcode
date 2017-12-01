class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        ht = {}
        res= []
        for path in paths:
            relation = path.split(" ")
            for i in range(1,len(relation)):
                index1 = relation[i].find('(')
                index2 = relation[i].find(')')
                content = relation[i][index1+1:index2]
                if ht.has_key(content):
                    ht[content].append((relation[0],relation[i][:index1]))
                else:
                    ht[content] = [(relation[0],relation[i][:index1])]

        for combine in ht.keys():
            if len(ht[combine])>1:
                group = []
                for same in ht[combine]:
                    s = same[0]+'/'+same[1]
                    group.append(s)
                res.append(group)
        return res



                
