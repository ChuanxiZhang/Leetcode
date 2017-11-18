num = 5
s = [5,4,3,5,2]
t = [2,2,3,5,1]
time = 10

dp = [0 for _ in range(time + 1)]

dic = {}
for i in range(len(t)):
    if t[i] not in dic:
        dic[t[i]] = [s[i]]
    else:
        dic[t[i]].append(s[i])
        dic[t[i]].sort(reverse= True)
print dic
next = 0

for i in range(time + 1):
    for a in t:
        if i - a >= 0 and next < len(dic[a]):
            dp[i] = max(dp[i], dp[i - a] + dic[a][next])

    next = 0

print dp
print dp[time]
