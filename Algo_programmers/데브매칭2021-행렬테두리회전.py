def solution(rows, columns, queries):
    answer = []
    BRD = []
    v = 1
    for row in range(rows):
        sub_BRD = []
        for column in range(columns):
            sub_BRD.append(v)
            v += 1
        BRD.append(sub_BRD)

    print("!!!")
    for p in range(len(BRD)):
            print(*BRD[p])
    def rotation(r1, c1, r2, c2):
        nonlocal BRD
        r1 -= 1
        r2 -= 1
        c1 -= 1
        c2 -= 1
        # 테두리의 인덱스를 배열에 담는다.
        lst = []
        for c in range(c1, c2):
            lst.append((r1,c))
        
        for r in range(r1, r2):
            lst.append((r,c2))
        
        for c in range(c2, c1, -1):
            lst.append((r2, c))
        
        for r in range(r2, r1, -1):
            lst.append((r, c1))
        
        # 테두리의 값을 배열에 담는다.
        value = []
        for l in lst:
            value.append(BRD[l[0]][l[1]])
        # 맨 앞 칸을 뒤로 옮긴다.
        print("value", value)
        # 다시 lst를 돌면서 BRD를 초기화시킨다.
        for idx, l in enumerate(lst):
            BRD[l[0]][l[1]] =  value[idx-1]

        return min(value)
        
    for query in queries:
        answer.append(rotation(query[0], query[1], query[2], query[3]))
        print("??")
        for p in range(len(BRD)):
            print(*BRD[p])

        
    return answer

print(solution(100, 97,[[1,1,100,97]]))