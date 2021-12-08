N = int(input())
lst = []
for n in range(N):
    lst.append(input())
result = list(lst[0])
for n in range(1, N):
    for i in range(len(lst[n])):
        if result[i] == "?": continue

        if result[i] != lst[n][i]:
            result[i] = "?"

print(''.join(result))