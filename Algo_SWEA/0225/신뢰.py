# 움직이는건 동시에 가능
# 버튼 누르는건 동시에 불가능
# 버튼은 순서대로 눌러야 함

T = int(input())
for t in range(1, T+1):
    lst = list(input().split())
    order = []
    # B와 O가 눌러야 할 버튼 숫자 담을 리스트
    B = []
    O = []
    for i in range(len(lst)):
        if lst[i] == 'B':
            B.append(int(lst[i+1]))
        elif lst[i] == 'O':
            O.append(int(lst[i+1]))

    for i in range(1, len(lst), 2):
        order.append((lst[i], int(lst[i+1]))) # B,2 O,1 O,2 B,4

    # B와 O 위치
    B_idx = 1
    O_idx = 1

    # B_max = max(B) if len(B) else 101
    # O_max = max(O) if len(O) else 101

    # 버튼 눌렀는지 확인하는 배열 -> 안눌렀으면 1
    button_B = [0]*101
    button_O = [0]*101

    for i in B:
        button_B[i] = 1
    for i in O:
        button_O[i] = 1

    time = 0
    while 1:
        # B차례 O차례 지났는지? 안지났으면 0
        B_check = 0
        O_check = 0
        time += 1
        # 1. 버튼 누를게 있는지 확인 -> 한번에 한번만 누를 수 있음
        if button_B[B_idx] == 1 and len(order) and order[0] == ('B', B_idx):
            B_check = 1
            button_B[B_idx] = 0
            order.remove(order[0])
        elif button_O[O_idx] == 1 and len(order) and order[0] == ('O', O_idx):
            O_check = 1
            button_O[O_idx] = 0
            order.remove(order[0])

        # 2. 움직일 수  있는지 확인
        if B_check == 0 and button_B[B_idx] != 1:
            B_idx += 1
            B_check = 1
        if O_check == 0 and button_O[O_idx] != 1:
            O_idx += 1
            O_check = 1
        # 최대값에 가있고 버튼 누를 필요가 없다면 break
        if button_B.count(1) == 0 and button_O.count(1) == 0:
            break
    print(time)
