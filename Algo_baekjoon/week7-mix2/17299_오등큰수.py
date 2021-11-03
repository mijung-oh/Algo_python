N = int(input())
num = list(map(int, input().split()))

# 오른쪽에 있으면서, 등장 횟수가 큰 것
count = {}
for i in num: # O(1,000,000)
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

result = []
for i in range(len(num)-1):
    cur_cnt = count[num[i]]

    check = True
    for j in range(i+1, len(num)):
        if num[i] != num[j] and count[num[i]] < count[num[j]]:
            result.append(num[j])
            check = False
            break
    if check:
        result.append(-1)
result.append(-1)
print(*result)
            

