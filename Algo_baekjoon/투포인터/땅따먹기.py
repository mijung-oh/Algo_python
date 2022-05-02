def solution(land):
    answer = 0
    l = len(land)
    
    def dfs(cur_r, cur_c, point):
        nonlocal answer
        
        print(cur_r, cur_c, point)
        if cur_r == l:
            answer = max(answer, point)
            return
        
        for i in range(4):
            if i == cur_c: continue
            dfs(cur_r+1, i, point + land[cur_r][i])
            
    for i in range(4):
        dfs(0, i, 0)

    return answer
print(solution([[1,2,3,5]]))