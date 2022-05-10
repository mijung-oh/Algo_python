from itertools import combinations

# 1. 선택할 수 있는 후보키 쌍을 구한다.
# 2. 가능하지 않는 후보키들을 딕셔너리에 넣는다.

def solution(relation):
    answer = 0
    key_num = []

    # 최소성 확인
    notMinimality = {}
    def isMinimality():

        pass
    # 0, 1, 2, 3
    for i in range(len(relation[0])):
        key_num.append(i)

    for l in range(1,len(key_num)+1):
        for combi in combinations(key_num, l):
            # 유일성 확인
            s = set()
            idx = 0
            while idx < len(relation):
                t = []
                for c in combi:
                    t.append(relation[idx][c])
                idx += 1
                s.add(tuple(t))
            if len(s) != len(relation):
                notMinimality[combi] = 1
            # 유일성 어긋나면 break
            # if len(s) != len(relation): break

    print(notMinimality)
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	)
