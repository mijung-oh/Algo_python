T = int(input())

def isPalindrome(string, M):
    # 주어진 문자열에서 시작지점을 정한다.
    for start in range(len(string)-1):
        for s in range(1, len(string)):
            # start+s가 string을 벗어나면 안됨
            if start + s < len(string):
                # start~ start+s 까지의 sub string을 가져온다.
                sub = string[start:start+s+1]
                # substring의 길이가 M 인 경우에만
                if len(sub) == M:
                    # 중간에 좌우대칭이 아닌 경우 check는 0으로 변함
                    check = 1
                    for i in range(len(sub)//2):
                        st = sub[i]
                        en = sub[-1-i]
                        if st != en:
                            check = 0
                            break
                    # 좌우대칭 존재하는 경우
                    if check == 1:
                        return sub
    return False


for t in range(1, T+1):
    N, M = map(int, input().split())

    lst = []
    for n in range(N):
        lst.append(list(input()))
    # 행
    for n in range(N):
        if isPalindrome(lst[n], M):
            P_lst = isPalindrome(lst[n], M)
            print('#{} {}'.format(t, ''.join(P_lst)))
    # 열
    for r in range(N):
        total = []
        for c in range(N):
            total.append(lst[c][r])
        if isPalindrome(total,M):
            P_lst = isPalindrome(total,M)
            print('#{} {}'.format(t, ''.join(P_lst)))
