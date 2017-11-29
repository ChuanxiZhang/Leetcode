class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = collections.deque()
        res = 0
        flag = 0
        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except:
                if token == '+':
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                if token == '-':
                    diffed = stack.pop()
                    differ = stack.pop()
                    res = differ - diffed
                    stack.append(res)
                if token == '*':
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                if token == '/':
                    divided = stack.pop()
                    divider = stack.pop()
                    res = int(float(divider) / divided)
                    stack.append(res)
        return stack[-1]
                    
