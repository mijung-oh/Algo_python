T = int(input())
'''
8자리의 암호를 뽑기 위해서
긴 암호코드에서 56배수길이의 비트문자열을 뽑아야한다.
16진수이기 때문에 14자리씩 뽑아내면 된다.
뽑아낸 16진수를 2진수 비트로 변환한다.
변환된 2진수비트를 7개씩 끊어서
암호로 변환한다.
'''

# 암호코드 변환
strTonum = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}
# 코드를 숫자로 번역
def rat(a):
    print(a, len(a))
    cnt = 1
    result = ''
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            result += str(cnt)
            cnt = 1
        else:
            cnt += 1
    result += str(cnt)
    print(result)
    # result : ex 1221 2442 ..
    # 숫자로 번역된 후 모든 자리수가 2로 나눠질 경우
    # 2로 나눠준다.
    # check = 1
    # while check:
    #     t=''
    #     for i in result:
    #         if int(i) % 2:
    #             check = 0
    #             break
    #     for i in result:
    #         t += str(int(i)//2)
    #     result = t
        
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
    for n in range(N):
        # 리스트 받기
        t = list(input())
        # 한 줄이 모두 0인 경우
        if t.count(0) == len(t): 
            continue
        # 56 56*2 56*3 ... 길이로 뽑아내기 위해서
        # 16진수는 1 자리당 4개비트니까 
        # 14, 28, 42 길이로 뽑아낸다.
        
        for i in range(len(t)):
            if t[i] == '0':
                continue
            real = []
            # 14자리 문자열 뽑은 후 56개 비트로 변경
            binary = strtobit(t[i:i+14])
            print(t[i:i+14])
            for j in range(0, len(binary), 7):
                if rat(binary[j:j+7]) in strTonum:
                    real.append(str(strTonum[rat(binary[j:j+7])]))
                    # print(real)
                else:
                    # print('16진수:', t[i:i+14])
                    real = []
                    break
            if len(real) and isCode(real):
                result = real

    print(result, len(result))
    print('#{} {}'.format(tc, sum(result)))

