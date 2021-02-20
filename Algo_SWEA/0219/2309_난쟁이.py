lst = []
for i in range(9):
    lst.append(int(input()))

n = len(lst)

for i in range(1<<n):
    total = []
    for j in range(n+1):
        if i & (1<<j):
            total.append(lst[j])
    if len(total) == 7 and sum(total) == 100:
        for t in sorted(total):
            print(t)
        break


