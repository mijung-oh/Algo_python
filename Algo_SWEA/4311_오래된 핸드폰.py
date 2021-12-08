T = int(input())
for t in range(T):
    N, O, M = map(int, input().split())
    ga = list(map(int, input().split()))
    op = list(map(int, input().split()))
    W = int(input())

    result = [M+1] * 1000 # 0~999
    q = []
    # 한 개로 만들 수 있는 숫자
    for i in ga:
        result[i] = 1
    # 두 개의 숫자로 만들 수 있는 조합 초기화
    for i in ga:
        for j in ga:
            for k in op:
                print(int(str(i) + str(j)))
                if k == 3 and i * j <= 999:
                    if result[i*j] > 3:
                        result[i*j] = 3
                        q.append(i*j)
                elif k == 2 and i - j >= 0:
                    if result[i-j] > 3:
                        result[i-j] = 3
                        q.append(i-j)
                elif k == 4 and j != 0 and i//j >= 0:
                    if result[i//j] > 3:
                        result[i//j] = 3
                        q.append(i//j)
                elif k == 1 and i + j <= 999:
                    if result[i+j] > 3:
                        result[i+j] = 3
                        q.append(i+j)
                elif 0 <= int(str(i) + str(j)) <= 999 :
                    if result[int(str(i) + str(j))] > 2:
                        result[int(str(i) + str(j))] = 2
                        q.append(int(str(i) + str(j)))

    while q:
        number = q.pop()
        # 모든 숫자와 연산한 뒤, 연산 횟수의 값을 넣는다.
        for j in ga:
            for k in op:
                if k == '*' and number * j <= 999:
                    if result[number*j] > result[number] + 2:
                        result[number*j] = result[number] + 2
                        q.append(number*j)
                elif k == '-' and number - j >= 0:
                    if result[number-j] > result[number] + 2:
                        result[number-j] = result[number] + 2
                        q.append(number-j)
                elif k == '/' and j != 0 and number//j >= 0:
                    if result[number//j] > result[number] + 2:
                        result[number//j] = result[number] + 2
                        q.append(number//j)
                elif k == '+' and number + j <= 999:
                    if result[number+j] > result[number] + 2:
                        result[number+j] = result[number] + 2
                        q.append(number+j)
    
    print("#", t+1, result[W])