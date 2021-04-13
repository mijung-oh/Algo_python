# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())

# 암호코드 변환
str_to_num = {'211': 0, '221': 1, '122': 2, '411': 3,
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


# 0100 -> 112
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
def check(a):
    if ((a[0]+a[2]+a[4]+a[6]) * 3 + a[1]+a[3]+a[5]+a[7]) % 10:
        return False
    return True



for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    visited = [0] * M * 4
    lst = []
    minV = 9999
    for n in range(N):
        # 리스트 받기
        t = list(input())
        # 한 줄이 모두 0인 경우
        if t.count('0') == len(t): 
            continue
        # 뒤에서부터 오면서
        # 비트가 1인 경우를 찾음
        binary = hex_to_bin(t)
        # 코드부분 한 덩어리를 찾기
        # 1로시작하면서 끝이 0인거
        bianry_lst = []
        i = len(binary)-1
        print(binary)
        while i>0:
            binary2 = ''
            if binary[i] == '1':
                # print('visi', visited[i])
                if visited[i]: 
                    i -= 1
                    continue
                visited[i] = 1
                start = i
                while start >= 4:
                    if '1' in binary[start:start-5:-1]:
                        binary2 += binary[start:start-5:-1]
                        start -= 5
                        continue
                    else:
                        print('끊기는부분', start)
                        print(binary[start:start-5:-1])
                        i = start-5
                        break
                bianry_lst.append(binary2[::-1])
            else:
                i -= 1
        print('list: ',bianry_lst)
        for i in bianry_lst:
            real = []
            rat_lst = rat(i)
            j = 0
            while j < len(i)-3:
                a = ''.join(rat_lst[j:j+3])
                if a in str_to_num:
                    j += 3
                    real.append(str_to_num[a])
                else: j += 1
            # print(real)
            # 정확한 코드인지 확인`
            k = 0
            while k < len(real)-8+1:
                if check(real[k:k+8]):
                    if minV > sum(real[k:k+8]):
                        minV = sum(real[k:k+8])
                k += 1
        
    print('#{} {}'.format(tc, minV))
