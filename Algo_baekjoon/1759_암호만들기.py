L, C = map(int, input().split())

words = list(input().split())

# 받은 문자들을 사전식을 기준으로 정렬한다.
words = sorted(words)
visited = [0 for _ in range(len(words))]
# cur_word = []

def dfs(cur_word):
    global L, C
    # 단어길이가 L이 되었을 때 모음이 한개이상 있는지 확인한다.
    if(len(cur_word) == L):
        mo = 0
        za = 0
        for word in cur_word:
            if word in ['a', 'e', 'i', 'o', 'u']:
                mo += 1
            else:
                za += 1
        if mo >= 1 and za >= 2:
            print(''.join(cur_word))
            return
    
    for idx, word in enumerate(words):
        if visited[idx]: continue
        if cur_word and cur_word[-1] > word: continue
        cur_word.append(word)
        visited[idx] = 1
        dfs(cur_word)
        cur_word.pop()
        visited[idx] = 0

dfs([])





# results = []

# for i in range(len(words)):
#     for j in range(i+1, len(words)):
#         for k in range(j+1, len(words)):
#             for l in range(k+1, len(words)):
#                 # 모음이 있는지 확인
#                 aeiou = ['a', 'e', 'i', 'o', 'u']
#                 if words[i] in aeiou or words[j] in aeiou or words[k] in aeiou or words[l] in aeiou:
#                     result = words[i] + words[j] + words[k] + words[l]
#                     results.append(result)

# for r in range(len(results)):
#     if r == len(results)-1:
#         print(results[r], end="")
#     else:
#         print(results[r], end="\n")