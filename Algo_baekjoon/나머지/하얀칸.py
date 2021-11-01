cnt = 0
for i in range(8):
    a = list(input())
    for j in range(8):
        if (i+j) % 2 == 0 and a[j] == 'F':
            cnt += 1
print(cnt)
    