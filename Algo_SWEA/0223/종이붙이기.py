T = int(input())

def paper(n):
    if n==1:
        return 1
    elif n==2:
        return 3
    else:
        return paper(n-1)+ 2*paper(n-2)

for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc,paper(N//10)))
