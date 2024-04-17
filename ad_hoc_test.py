a = [4,6,8]

for i in range(len(a)):
    for j in range(i, len(a)):
        print(a[i:j+1])