def isPallindrome2(string):
    # check가 1이면 팰린드롬
    for i in range(len(string)//2):
        st = string[i]
        en = string[-1-i]
        if st != en:
            return False
    return True

# 부분 문자열들을 돌면서 팰린드롬인지 확인한 후 맞으면 길이를 리턴.
def find(string, l):
    result = []
    for i in range(len(string)-l+1):
        result = string[i:i+l]
        if isPallindrome2(result):
            return l
    return False


for t in range(10):
    tc = int(input())
    BRD = []
    for r in range(100):
        BRD.append(list(input()))

    # 구해야 하는 팰린드롬 최대 길이
    max_len = -1

    # 행
    # 모든 행을 돌면서
    for r in range(100):
        # 길이가 99 98 97 --- 0까지 find 함수를 이용하여 서브 스트링을 구한 후 팰린드롬인지 확인
        for count in range(99, -1, -1):
            if find(BRD[r], count) and max_len < find(BRD[r], count):
                max_len = find(BRD[r], count)

    # 열
    # 모든 열을 돌면서
    for c in range(100):
        # 그 열의 모든 행에 대한 원소를 빈 리스트에 넣어준다.
        lst = []
        for r in range(100):
            lst.append(BRD[r][c])
        # 만들어진 리스트를 find에 넣어서 서브스트링을 구한 후 팰린드롬인지 확인한다.
        for count in range(99, -1, -1):
            if find(lst, count) and max_len < find(lst, count):
                max_len = find(lst, count)

    print('#{} {}'.format(t, max_len))


