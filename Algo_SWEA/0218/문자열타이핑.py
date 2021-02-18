T = int(input())

for t in range(1, T+1):
    long, short = input().split()
    long_len = len(long)
    short_len = len(short)
    idx = 0
    count = 0

    while idx < long_len:
        count += 1
        check = 2
        # 같은 문자열이 있는지 확인하는 변수
        if idx < long_len - short_len + 1:
            check = 0
            for i in range(short_len):
                if long[idx+i] != short[i]:
                    check = 1
                    break
        # 같은 문자열이 있는 경우
        if check == 0:
            idx += short_len
        else:
            idx += 1

    print('#{} {}'.format(t, count))


    # while idx < len(long):
    #     count += 1
    #     # long 문자열을 돌면서 short의 첫 번째 문자와 같고
    #     # 뒤에 짧은 문자열의 길이만큼 여유가 있는 경우 비교
    #     if long[idx] == short[0] and idx + l <= len(long):
    #         # long 문자열에서 short 길이만큼의 부분문자열을 뽑아낸다. long2 = long[idx:idx+l] => 복사하는데 시간이 많이 걸림
    #
    #         # 같은 문자열인지 확인하는 변수
    #         check = 1
    #         for s in range(l):
    #             if long[idx + s] != short[s]:
    #                 check = 0
    #                 break
    #         if check == 1:
    #             idx += l
    #     # 같은게 안나온 경우 인덱스는 +1로 이동해준다.
    #     else:
    #         idx += 1
