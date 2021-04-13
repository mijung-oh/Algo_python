import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
'''
긴 문자열 자체를 2진수로 변환.
비율을 다 측정
숫자로 변환
4개씩 끊어서 코드로 변환가능한지 확인
가능한거 8개 연속으로 있는 경우 정확한 코드인지 확인
'''

# 암호코드 변환
strTonum = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}
# 코드를 숫자로 번역
def rat(a):
    cnt = 1
    result = []
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            result.append(str(cnt))
            cnt = 1
        else:
            cnt += 1
    result += str(cnt)
    return result
    
# 8자리의 숫자가 정상적인 암호인지 확인
def isCode(a):
    # 8자리이고 홀수인거 더한다음에 3 곱하고
    # 짝수인거 더한 다음
    # 마지막자리 더한게 10의 배수이면 성공
    odd = 0
    even = 0
    for idx, v in enumerate(a):
        if (idx+1) % 2:
            odd += v
        else:
            even += v
    if (odd*3 + even) % 10 == 0:
        return True
    return False

# 16진수 -> 2진수
d = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}
def strtobit(string):
    result = ''
    for i in string:
        for j in range(3, -1, -1):
            target = int(i) if i.isdecimal() else d[i]
            if target & 1<<j:
                result += '1'
            else:
                result += '0'
        # print(i, result)
    return result


for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    lst = []
    real = []
    for n in range(N):
        # 리스트 받기
        t = list(input())
        # 한 줄이 모두 0인 경우
        if t.count(0) == len(t): 
            continue

        binary = strtobit(t)
        tlist = rat(binary)
        # 비율측정된 숫자들의 모임을 4개씩 끊어서 코드변환 가능한지 확인
        i = 0
        while i < len(tlist)-3+1:
            if ''.join(tlist[i:i+3]) in strTonum:
                real.append(''.join(tlist[i:i+3]))
                i += 3
            else:
                i += 1
               
        for idx, v in enumerate(real):
            if v in strTonum:
                real[idx] = strTonum[v]
        # print(real)
        # 정확한 코드인지 확인
        minV = 9999
        i = 0
        while i < len(real)-8+1:
            if isCode(real[i:i+8]):
                if minV > sum(real[i:i+8]):
                    minV = sum(real[i:i+8])
            i += 1
    print('#{} {}'.format(tc, minV))

