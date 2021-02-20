n = int(input())

# 그룹 단어의 개수
count = 0
for i in range(n):
    word = input()
    # 한번 나왔던 단어들이 들어갈 딕셔너리
    dict = {}
    for i in word:
        dict[i] = 0

    check = 0
    for w in range(len(word)):
        # 그룹단어 아니 경우
        if w-1>=0 and word[w-1] != word[w] and dict[word[w]] >0:
            check = 1
            break
        dict[word[w]] += 1
    if check == 0:
        count += 1

print(count)