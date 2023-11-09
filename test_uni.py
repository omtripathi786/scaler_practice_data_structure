a = [1,2,3,4,5]
n = len(a)
for s in range(n):
    for e in range(s,n):
        print(a[s:e+1])

