def solution(begin, target, words):
    answer = 0
    min_cnt = 0xffff
    if target not in words:
        return 0

    def dfs(cur, cnt):
        nonlocal min_cnt
        # 최소 cnt보다 현재 cnt가 더 큰 경우, 더 볼 필요가 없어지므로 return
        if min_cnt < cnt:
            return
        # cnt가 words의 길이보다 클 경우 이미 모든 경로를 탐색하게 된 것이므로 return
        if len(words) < cnt:
            return

        if cur == target:
            if min_cnt > cnt:
                min_cnt = cnt
                return
        
        
        for word in words:
            # 현재 단어와 word가 한 자리만 다른 경우 dfs
            difcnt = 0
            for i in range(len(cur)):
                if word[i] != cur[i]:
                    difcnt += 1
                    if difcnt >1 : break
            if difcnt == 1:
                dfs(word, cnt + 1)
        
        return 

    dfs(begin, 0)
    if min_cnt == 0xffff:
        return 0
    return min_cnt

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))