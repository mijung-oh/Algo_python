T = int(input())

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
# 코드 -> 숫자로 바꿔줌
def rat(a):
    cnt = 1
    result = ''
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            result += str(cnt)
            cnt = 1
        else:
            cnt += 1
    result += str(cnt)
    return result
    
# 정상적인 암호인지 확인
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


for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    lst = []
    for n in range(N):
        # 리스트 받기
        t = list(map(int, input()))
        # 한 행 안에 1이 있을 경우에만 코드탐색
        if 1 in t:
            for i in range(M - 56 + 1):
                # 56길이의 리스트를 뽑아내기
                code = []
                longlist = t[i:i+56]
                for j in range(0, len(longlist), 7):
                    k = rat(longlist[j:j+7])
                    if k in strTonum:
                        code.append(strTonum[k])
                    else:
                        code = []
                        break
                    if len(code) == 8 and isCode(code):
                        result = code
                        break
                if result: break

        else:
            continue
    print(result)
    print('#{} {}'.format(tc, sum(result)))

