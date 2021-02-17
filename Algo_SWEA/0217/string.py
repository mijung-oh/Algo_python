
def bruteForce(s, t):
    # s: 주어진 문자열, t: 검색할 문자열
    count = 0
    for i in range(len(s)):
        # 검색할 문자열과 비교하면서 계속 같은지 체크
        check = 0
        if s[i] == t[0]:
            for j in range(len(t)):
                if i+j > len(s)-1 or s[i+j] != t[j]:
                    check = 1
                    break
            # 검색할 문자열이 있으면
            if check == 0:
                count += 1
    return count

for t in range(10):
    tc = int(input())
    # 찾아야 하는 문자열
    t = input()
    # 주어진 문자열
    s = input()
    c = bruteForce(s,t)
    print('#{} {}'.format(tc, c))