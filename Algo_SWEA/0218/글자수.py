T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    dict ={}
    # dict에 str1 넣기
    for s1 in str1:
        dict[s1] = 0

    for s1 in dict.keys():
        for s2 in str2:
            if s1 == s2:
                dict[s1] += 1
    print('#{} {}'.format(t, max(dict.values())))

