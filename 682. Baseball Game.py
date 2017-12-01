class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        sum_num = 0

        for opt in ops:
            try:
                int(opt)
                stack.append(opt)
                sum_num += int(opt)
            except:
                if opt == 'C':
                    prev = stack.pop()
                    sum_num -= int(prev)
                elif opt == 'D':
                    prev = stack[-1]
                    double = 2 * int(prev)
                    sum_num += double
                    stack.append(double)
                elif opt == '+':
                    two = int(stack[-1]) + int(stack[-2])
                    sum_num += two
                    stack.append(two)
        return sum_num




                
