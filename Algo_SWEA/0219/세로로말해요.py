T = int(input())

for t in range(1, T+1):
    lst = []
    # 가장 긴 문자열의 길이
    max_len = -1
    for n in range(5):
        t= list(input())
        lst.append(t)
        if max_len < len(t):
            max_len = len(t)
    result = ''
    for i in range(max_len):
        for j in range(5):
            if len(lst[j])<= i:
                continue
            result += lst[j][i]
    print('#{} {}'.format(t, result))

