class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = collections.deque()
        q.append((sr,sc))
        color = image[sr][sc]
        image[sr][sc] = newColor
        while q:
            cur = q.popleft()
            a = cur[0]
            b = cur[1]
            for d in dirs:
                x = a + d[0]
                y = b + d[1]
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == color and image[x][y] != newColor:
                    q.append((x,y))
                    image[x][y] = newColor
        return image
