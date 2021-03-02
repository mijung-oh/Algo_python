def q(a, begin, end):
    if len(a[begin:end+1]) > 2:
        p = (begin+end)//2
        print('2이상',begin, end)
        st = q(a, begin, p)
        en = q(a, p+1, end)
        if a[st] == a[en]:
            return st if st < en else en
        elif a[st] == 1 and a[en] == 2:
            return en
        elif a[st] == 1 and a[en] == 3:
            return st
        elif a[st] == 2 and a[en] == 3:
            return en
        elif a[st] == 2 and a[en] == 1:
            return st
        elif a[st] == 3 and a[en] == 1:
            return en
        elif a[st] == 3 and a[en] == 2:
            return st

    elif len(a[begin:end+1]) == 2:
        print('2일때',begin, end)
        if a[begin] == a[end]:
            return begin if begin < end else end
        elif a[begin] == 1 and a[end] == 2:
            return end
        elif a[begin] == 1 and a[end] == 3:
            return begin
        elif a[begin] == 2 and a[end] == 3:
            return end
        elif a[begin] == 2 and a[end] == 1:
            return begin
        elif a[begin] == 3 and a[end] == 1:
            return end
        elif a[begin] == 3 and a[end] == 2:
            return begin
    #  길이가 1일 경우
    else:
        print(begin)
        return begin


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print('#{} {}'.format(tc,q(lst, 0, len(lst)-1)+1))