class Solution(object):
    def guessNumber(self, n):
        mid,low,high=1,n,n
        while guess(mid)!=0:
            mid=(low+high)/2
            if guess(mid)==-1:
                low=mid
            if guess(mid)==1:
                high=mid
      return mid
