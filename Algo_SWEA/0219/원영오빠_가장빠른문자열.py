# a = 'bananabana'
# bo = 'bana'
# a = 'cccccca'
# bo = 'ccc'
# a = 'asakusa'
# bo = 'sa'

# a='cccaaa'
# bo='ccc'

T =int(input())
for t in range(1, T+1):
    a, bo = input().split()
    long = len(a)
    short = len(bo)

    cnt = 0
    emp = []

    st = -1
    en = -1


    # i는 0부터 끝까지 돌아야함
    for i in range(long):
        if st<= i <= en:
            continue
        # cccaaa ccc인 경우는?
        # abcabc abc
        # abcabcabc abc
        # cccccc ccc 인 경우
        if long%short == 0 and bo == a[i:i+short]:
            check = 1
            for j in range(long-short+1):
                if j%short == 0 and bo != a[j:j+short]:
                    check = 0
                    break
            if check == 1:
                cnt = long//short
                break
        # 같은 문자열 발견한 경우
        # cnt += 1해주고
        # st랑 en을 설정
        # cccaaa ccc 인 경우 st는 0, en은 2가 됨 -> i가 0,1,2 일때 그냥 넘어가도록 설정(위에서)
        if i+short <= long and bo == a[i:i+short]:
            cnt+=1
            st =i
            en = i+short-1
            continue
        cnt += 1

    print('#{} {}'.format(t, cnt))