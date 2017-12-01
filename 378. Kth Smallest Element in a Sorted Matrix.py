class Solution(object):
    def kthSmallest(self,matrix, k):
        onelist = list()
        for index in range(0,len(matrix)):
            for val in range(0,len(matrix[index])):
                onelist.append(matrix[index][val])
        return sorted(onelist)[k-1]
