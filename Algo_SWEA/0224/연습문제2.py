# 배열의 부분집합 중 원소 합이 10인 부분집합
### Q. 이걸 어떻게 백트래킹??
arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,3]
N = len(arr)
sel = []
visited = [0]*N

def powerset(k):
    if k == N:
        print(sel)
        return
    for i in range(N):
        if visited[i]: continue


# ## 그냥 부분집합으로 해결하기
# result = []
# # 2^N번 실행
# for i in range(1<<N):
#     total = 0
#     sublst = []
#     for j in range(N):
#         if i & (1<<j):
#             sublst.append(arr[j])
#             total += arr[j]
#     if total == 10:
#         result.append(sublst)
# print(result)