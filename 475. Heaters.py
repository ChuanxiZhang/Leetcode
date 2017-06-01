class Solution(object):
    def findRadius(self, houses, heaters):
        heaters = sorted(heaters) + [float('inf')]
        start = distance = 0
        for house in sorted(houses):
            while house >= (heaters[start] + heaters[start + 1]) / 2.:
                print (heaters[start] + heaters[start + 1]) / 2
                start += 1
            distance = max(distance, abs(heaters[start] - house))
        return distance

