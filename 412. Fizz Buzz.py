class Solution(object):
    def fizzBuzz(self, n):
        result=list()
        for i in range(n):
            if (i+1)%3==0:
                save='Fizz'
                if(i+1)%5==0:
                    result.append('FizzBuzz')
                else:
                    result.append(save);
            elif (i+1)%5==0:
                result.append('Buzz')
            else:
                result.append(str(i+1))
        return result

solution = Solution()
print solution.fizzBuzz(15)