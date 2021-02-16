for i in range(10):
    t = int(input())
    ladder = []
    
    for j in range(100):
        ladder.append(list(map(int, input().split())))
    
    result = 0
    for k in range(100):
        if result:
            break
        
        i = 0
        j = k
        visited = [[0 for _ in range(100)] for _ in range(100)]

        if ladder[i][j] == 1:
            while 1:
                if i == 99 :
                    print('===',j, ladder[i][j])
                    if ladder[i][j] == 2:
                        result = k
                    break

                # 왼쪽 길이 있는 경우
                if j - 1 >= 0 and ladder[i][j-1] == 1 and visited[i][j-1] == 0:
                    visited[i][j-1] = 1
                    j -= 1
                # 오른쪽 길이 있는 경우
                elif j + 1 < 100 and ladder[i][j+1] == 1 and visited[i][j+1] == 0:
                    visited[i][j + 1] = 1
                    j += 1
                # 아래로
                elif i+1 < 100:
                    visited[i + 1][j] = 1
                    i += 1
            
        

    print(f'#{t} {result}')