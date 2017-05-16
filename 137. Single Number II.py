
res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if i + j + k == 0:
                res.append([i, j, k])
return res
