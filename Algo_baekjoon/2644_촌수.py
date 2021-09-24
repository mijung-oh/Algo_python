people = int(input())
a, b = map(int, input().split())

M = int(input())
relation = [[] for _ in range(people+1)]

for m in range(M):
    st, en = map(int, input().split())
    relation[st].append(en)
    relation[en].append(st)

result = []
def checkRelation(x):

    if len(relation[x]) == 0:
        return
    
    result.append(x)

    # 만약 x가 b라면 끝
    if x == b:
        return True

    for i in relation[x]:
        if i in result:
            continue
        if checkRelation(i):
            return True
        result.pop()
    
    return

checkRelation(a)
# print(result)
if b in result:
    print(len(result) - 1)
else:
    print("-1")