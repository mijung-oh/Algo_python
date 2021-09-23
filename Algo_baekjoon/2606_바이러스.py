computer_cnt = int(input())
N = int(input())
computers = [[] for _ in range(computer_cnt + 1)]

for n in range(N):
    st, en = map(int, input().split())
    computers[st].append(en)
    computers[en].append(st)

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