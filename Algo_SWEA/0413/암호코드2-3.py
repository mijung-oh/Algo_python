import sys
sys.stdin = open('input.txt', 'r')
decode = {'211': 0, '221': 1, '122': 2, '411': 3,
    '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9,
}


# 16진수 -> 2진수
d = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}
def hex_to_bin(string):
    result = ''
    for i in string:
        for j in range(3, -1, -1):
            target = int(i) if i.isdecimal() else d[i]
            if target & 1<<j:
                result += '1'
            else:
                result += '0'
    return result


# 8자리의 숫자가 정상적인 암호인지 확인
def check(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    if ((a[0]+a[2]+a[4]+a[6]) * 3 + a[1]+a[3]+a[5]+a[7]) % 10:
        return False
    return True


T = int(input())
for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    # 이미 생성됐던 암호 저장
    v = []
    total = 0
    visited_row = []

    for n in range(N):
        # 리스트 받기
        t = list(input()[:M])
        # 한 줄이 모두 0인 경우
        if t.count('0') == len(t): 
            continue
        if len(visited_row) and t in visited_row:
            continue
        visited_row.append(t)
        # 16진수 코드를 2진수로 변환한다.
        binary = hex_to_bin(t)
        lst = []
        f1 = f2 = f3 = 0
        for i in range(len(binary)-1, -1, -1):
            if f2==0 and f3==0 and binary[i] == '1':
                f1 += 1
            elif f1 and f3== 0 and binary[i] == '0':
                f2 += 1
            elif f1 and f2 and binary[i] == '1':
                f3 += 1
            elif f1 and f2 and f3 and binary[i] == '0':
                minV = min(f1, f2, f3)
                # 211
                f1 //= minV
                f2 //= minV
                f3 //= minV                
                lst.append(str(decode[str(f3) + str(f2) + str(f1)]))

                f1 = f2 = f3 = 0
        # print(lst)
        lst = lst[::-1]
        for i in range(0, len(lst), 8):
            if len(v) and ''.join(lst[i:i+8]) in v:
                continue
            if check(lst[i:i+8]):
                v.append(''.join(lst[i:i+8]))
    # 유효한 암호들 합 구하기
    for i in v:
        for j in i:
            total += int(j)
    print('#{} {}'.format(tc, total))