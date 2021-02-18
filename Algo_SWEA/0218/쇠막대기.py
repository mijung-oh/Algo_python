T = int(input())

for t in range(1, T+1):
    lst = list(input())
    sublst = []
    # 레이저 개수
    total_r = 0
    sub_r = 0
    # 막대 개수
    m = 0
    # 쪼개진 막대 개수
    c = 0

    for idx in range(len(lst)):
        if lst[idx] == '(':
            sublst.append(lst[idx])
        elif lst[idx] == ')':
            # 빈 리스트에 레이저만 들어온 경우 -> pass
            if len(sublst) == 1 and sublst[0] == '(':
                sublst.remove('(')
            # 레이저인 경우
            elif idx -1 >= 0 and lst[idx-1] == '(':
                sublst.remove('(')
                sub_r += 1
            # ---))인 경우
            elif len(sublst) > 1 and sublst[-1] == '(':
                print(sub_r)
                if sub_r == 0:
                    c +=  total_r + 1
                    if len(lst) == 1:
                        total_r = 0
                else:
                    # 작은 막대의 쪼개진 개수
                    c += sub_r+1
                    total_r += sub_r
                    sub_r = 0
                    sublst.remove('(')

    print(c)