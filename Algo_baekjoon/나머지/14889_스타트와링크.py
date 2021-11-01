N = int(input())

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

# 팀 나누기
def combi(arr):
    n = len(arr)
    result = []
    for i in range(1<<n):
        total = []
        for j in range(n):
            if i & (1<<j):
                total.append(arr[j])
        if len(total) == n//2:
            result.append(total)
    # print(result)
    return result

# # N/2명씩 스타트팀, 링크팀
number = [i for i in range(1, N+1)]
teams = combi(number)
st = 0
en = len(teams) -1
min_gap = 0xffff

while st < en:
    start = teams[st]
    link = teams[en]

    # 팀 계산
    start_sum = 0
    link_sum = 0

    # for i in range(len(start)): 
    #     for j in range(i+1, len(start)):
    #         start_sum += BRD[start[i]-1][start[j]-1]
    #         start_sum += BRD[start[j]-1][start[i]-1]

    # for i in range(len(link)):
    #     for j in range(i+1, len(link)):
    #         link_sum += BRD[link[i]-1][link[j]-1] 
    #         link_sum += BRD[link[j]-1][link[i]-1]

    for i in start: 1 2 3
        for j in start: 1 2 3
            if i == j: continue
            start_sum += BRD[i-1][j-1]

    for i in link:
        for j in link:
            if i == j: continue
            link_sum += BRD[i-1][j-1]

    # print(start_sum, link_sum)
    if min_gap > abs(start_sum - link_sum):
        min_gap = abs(start_sum - link_sum)
            
            
    st += 1
    en -= 1
    
print(min_gap)
    