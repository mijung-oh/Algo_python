computer_cnt = int(input())
N = int(input())
computers = [[] for _ in range(computer_cnt + 1)]

for n in range(N):
    st, en = map(int, input().split())
    computers[st].append(en)

virus = []
def countVirus(x):
    global virus
    if x in virus:
        return

    if len(computers[x]) == 0:
        return
    
    virus.append(x)
    for i in computers[x]:
        countVirus(i)
    return
    
countVirus(1)
print(virus)
print(len(virus))