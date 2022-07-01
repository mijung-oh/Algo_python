import sys
def solution(begin, target, words):
    if target in words:
        answer = sys.maxsize
        visited = {}
        for word in words:
            visited[word] = 0

        def dfs(cur, cnt):
            nonlocal answer
            if cnt > answer:
                return

            if cur == target:
                answer = min(answer, cnt)
                return

            # 단어들 중에 한 자리수만 다르면서 방문하지 않은 단어를 탐색한다.
            for word in words:
                if visited[word] == 0:
                    count = 0
                    for i in range(len(word)):
                        if cur[i] != word[i]:
                            count += 1
                    if count == 1:
                        visited[word] = 1
                        dfs(word, cnt+1)
                        visited[word] = 0
            return
        dfs(begin, 0)


        return answer
    return 0
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "hog", "cig"]))