class Solution(object):
    def findRestaurant(self, list1, list2):
        minsum,res=len(list1)+len(list2),[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j] and i+j<=minsum:
                    minsum=i+j
                    res.append(list1[i])
        return res