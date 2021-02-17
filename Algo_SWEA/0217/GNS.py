T = int(input())

for t in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    
    lst = input().split()

    for i in range(len(lst)):
        if lst[i] == "ZRO":
            lst[i] = 0
        elif lst[i] == "ONE":
            lst[i] = 1
        elif lst[i] == "TWO":
            lst[i] = 2
        elif lst[i] == "THR":
            lst[i] = 3
        elif lst[i] == "FOR":
            lst[i] = 4
        elif lst[i] == "FIV":
            lst[i] = 5
        elif lst[i] == "SIX":
            lst[i] = 6
        elif lst[i] == "SVN":
            lst[i] = 7
        elif lst[i] == "EGT":
            lst[i] = 8
        elif lst[i] == "NIN":
            lst[i] = 9
        
    lst = sorted(lst)

    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = "ZRO"
        elif lst[i] == 1:
            lst[i] = "ONE"
        elif lst[i] == 2:
            lst[i] = "TWO"
        elif lst[i] == 3:
            lst[i] = "THR"
        elif lst[i] == 4:
            lst[i] = "FOR"
        elif lst[i] == 5:
            lst[i] = "FIV"
        elif lst[i] == 6:
            lst[i] = "SIX"
        elif lst[i] == 7:
            lst[i] = "SVN"
        elif lst[i] == 8:
            lst[i] = "EGT"
        elif lst[i] == 9:
            lst[i] = "NIN"
    print(f'#{t}')
    print(lst)