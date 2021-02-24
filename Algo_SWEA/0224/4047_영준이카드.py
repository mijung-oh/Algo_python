T = int(input())
# 1. S, D, H, C 별로 각각 몇장이 더 필요한지? 총 13장씩 있어야함
# 2. 영준이가 가지고 있는 카드가 중복되어있는게 있는 경우 ERROR

for tc in range(1, T+1):
    string = input()
    S = []
    D = []
    H = []
    C = []
    # 만약 중복된게 있으면 check=0
    check = 1

    for s in range(0, len(string), 3):
        if string[s] == 'S' and string[s:s+3] not in S:
            S.append(string[s:s+3])
        elif string[s] == 'D' and string[s:s+3] not in D:
            D.append(string[s:s+3])
        elif string[s] == 'H' and string[s:s+3] not in H:
            H.append(string[s:s+3])
        elif string[s] == 'C' and string[s:s+3] not in C:
            C.append(string[s:s+3])
        else:
            check = 0
            print('#{} {}'.format(tc, 'ERROR'))
            break
    if check:
        print('#{} {} {} {} {}'.format(tc, 13-len(S), 13-len(D), 13-len(H), 13-len(C) ))
