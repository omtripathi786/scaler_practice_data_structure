A = [1, 12, 10, 3, 14, 10, 5]
B = 8
n = len(A)
k = 0
for i in range(n):
    if A[i] <= B:
        k += 1

print(k)

count = 0
ans = -99999
for i in range(k):
    if A[i] <= B:
        count += 1
ans = max(ans, count)
print(ans, count)

s = 1
e = k
while e < n:
    if A[s-1] <= B:
        count -= 1
    if A[e] <= B:
        count += 1
    ans = max(ans,count)
    s += 1
    e += 1

print(ans)
