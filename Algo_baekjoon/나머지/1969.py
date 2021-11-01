N, M = map(int, input().split())

DNAs = []
for n in range(N):
    DNAs.append(input())

min_sum = 0xffffffff
# target = []

# 길이가 M인 문자열을 돌면서 가장 알파벳이 많이 나온 것을 찾아서 조합한다.
result = ""
# 길이가 M이니까 앞에서부터 돌면서
for m in range(M):
    # 각각 알파벳의 개수를 세어준다.
    atgc = [[0, "A"], [0, "T"], [0, "G"], [0, "C"]]
    # 모든 DNA를 돌면서 해당 인덱스에 맞는 알파벳에 +1를 해준다.
    for dna in DNAs:
        if dna[m] == "A": atgc[0][0] += 1
        elif dna[m] == "T": atgc[1][0] += 1
        elif dna[m] == "G": atgc[2][0] += 1
        elif dna[m] == "C": atgc[3][0] += 1
    
    # 가장 많이 나온 알파벳부터 추가를 해본다.
    max_alphabet = ""
    maxV= -1
    for i in atgc:
        # print(type(i[0]), type(maxV))
        if i[0] > maxV:
            max_alphabet = i[1]
            maxV = i[0]
        elif i[0] == maxV:
            max_alphabet = i[1] if ord(i[1]) < ord(max_alphabet) else max_alphabet

    result += max_alphabet

dist = 0
for dna in DNAs:
    for m in range(M):
        if result[m] != dna[m]:
            dist += 1
print(result)
print(dist)
    
    
    
