T = int(input())

def bruteforce(short, long):
    # 안에 문자열 있으면 check==0
    check = 0
    for l in range(len(long)):
        if long[l] == short[0]:
            check = 1
            for s in range(len(short)):
                if l+s > len(long) -1 or long[l+s] != short[s]:
                    check = 0
                    break
        if check == 1:
            return True
    return False

for t in range(1, T+1):
    short = input()
    long = input()
    if bruteforce(short, long):
        print('#{} {}'.format(t,1))
    else:
        print('#{} {}'.format(t, 0))