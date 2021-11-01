# dfs + dp

def dfs(day, delay, cost):
    global N, max_prop

    if day > N:
        if max_prop < cost:
            max_prop = cost
        return

    # 상담 신청 할지 안할지 선택지는 두가지
    for choice in [True, False]:
        if choice:
            if day+prop[day][0] > N+1: continue
            dfs(day+prop[day][0], delay+prop[day][0], cost+prop[day][1])
        else:
            dfs(day+1, delay, cost)
    
        


N = int(input())
dp = [0] * (N+1)
max_prop = -1

prop = [0]
for n in range(N):
    t, p = map(int, input().split())
    prop.append((t,p))

dfs(1, 0, 0)
print(max_prop)

'''
n=int(input());
v=[0]*30;
r=s=0
while s<n:
    t,p=map(int,input().split());
    # s+t날때의 최대 값
    v[s+t]=max(v[s+t],r+p);
    # s: 현재위치
    s+=1;
    # 현재위치일때의 저장해놓은 최대값 vs 현재 r
    r=max(r,v[s])
print(r)
'''