class Solution(object):
    def countAndSay(self, n):
        cur = '1'
        for _ in range(1, n):
            pre = cur
            cur = ''
            count = 1
            num = pre[0]
            for char in pre[1:]:
                if char == num:
                    count += 1
                else:
                    cur += (str(count) + num)
                    count = 1
                    num = char
            else:
                cur += (str(count) + num)
        return cur

