N = int(input())

# 가장 큰 리스트 선택
max_len = -1
# 임의의 수 고르기
for i in range(N+1):
    result = []
    result.append(N)
    choice = i
    check = 0
    while choice >= 0:
        result.append(choice)
        choice = result[len(result)-2] - result[len(result)-1]

    if max_len < len(result):
        max_len = len(result)
        max_result = result

print(max_len)
print(*max_result)