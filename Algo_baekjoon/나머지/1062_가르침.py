from itertools import combinations

N, k = map(int, input().split())
words = []
if k < 5:
    print(0)
    exit()
elif k >= 26:
    print(N)
    exit()

mustKnow = ['a', 'n', 't', 'i', 'c']
iKnow = [0 for _ in range(26)]

# 이미 아는 단어는 체크
for m in mustKnow: 
    iKnow[ord(m) -ord('a')] = 1

# k = k - len(mustKnow)
for n in range(N):
    words.append(input())

def findMaxCnt(words):
    # 1. 조합으로 words 개수부터 1개까지 for문 돌면서
    for w in range(len(words), 0, -1):
        # 2. 구한 조합이 k개 미만으로 구할 수 있는지 확인
        for combi in combinations(words, w):
            learnWord = set()
            print(combi)
            for c in combi:
                for ww in c:
                    learnWord.add(ww)
            if len(learnWord) <= k: 
                return len(combi)
result = findMaxCnt(words)
print(result if result else 0)
    