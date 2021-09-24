computer_cnt = int(input())
N = int(input())
computers = [[] for _ in range(computer_cnt + 1)]

for n in range(N):
    st, en = map(int, input().split())
    computers[st].append(en)
    # computers[en].append(st)

virus = []
def countVirus(x):
    global virus
    if x in virus:
        return
    
    virus.append(x)
    for i in computers[x]:
        countVirus(i)
    return
    
countVirus(1)
# print(virus)
print(len(virus)-1)

'''
반례: 
7
6
2 1
2 3
5 1
5 2
5 6
4 7

양방향이 아닐 경우, 1에서 연결돼있는 노드가 없어서 값이 0이 나옴
정답은 4
'''