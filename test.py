a=0
def b(i,a=0):
    if i==0:
        return a
    else:
        a += 1
        b(i-1)

    return a
print b(5)
