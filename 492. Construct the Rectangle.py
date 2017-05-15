class Solution(object):
    def constructRectangle(self, area):
        sim = int(math.sqrt(area))
        while not area % sim == 0:
            sim -= 1
        return [area / sim, sim]
