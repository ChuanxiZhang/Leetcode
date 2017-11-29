# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result = 0
        if not points:
            return 0
        if len(points) <=2:
            return len(points)
        for i in range(len(points)):
            hashtable = {}
            overlap,maxnum = 0, 0
            for j in range(i + 1, len(points)):
                x = points[i].x - points[j].x
                y = points[i].y - points[j].y
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                else:
                    gcd = self.generateGCD(x, y)
                    if not gcd == 0:
                        x /= gcd
                        y /= gcd
                    if x in hashtable:
                        if y in hashtable[x]:
                            hashtable[x][y] += 1
                        else:
                            hashtable[x][y] = 1
                    else:
                        sub_hashtable = {y:1}
                        hashtable[x] = sub_hashtable
                maxnum = max(maxnum, hashtable[x][y])
            result = max(result, maxnum + overlap + 1)
        return result


    def generateGCD(self, x, y):
        if y == 0:
            return x
        else:
            return self.generateGCD(y, x % y)



        
