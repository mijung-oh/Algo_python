N = int(input())

def isSequence(seq):
    # 처음 차이 - seq는 기본적으로 길이가 2 이상인 문자열
    gap = int(seq[1]) - int(seq[0])
    for idx, s in enumerate(seq):
        if idx > 0 and int(seq[idx]) - int(seq[idx-1]) != gap:
            return False
    return True
            


if len(str(N)) == 1: 
    print(N)
    exit()

answer = 0
for n in range(10, N+1):
    if isSequence(str(n)):
        answer += 1
print(answer + 9)