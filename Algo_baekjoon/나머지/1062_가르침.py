from itertools import combinations
from math import comb

def convertAlphabetToInt(x):
    return ord(x) - ord('a')

def intToBit(arr):
    result = 0
    for a in arr:
        result |= (1<<a)
    return result

N, k = map(int, input().split())

# 꼭 배워야 하는 알파벳을 문자 a를 뺀 int 값으로 바꾼 뒤, base 변수에 비트값으로 저장한다.
s = set([convertAlphabetToInt(a) for a in ['a', 'c', 'i', 'n', 't']])
base = 0
for i in s:
    base |= (1 << i)

# 입력 받은 단어 한 글자마다 숫자로 바꾼 뒤, 
arr = [set(map(convertAlphabetToInt, input().strip())) for _ in range(N)]
# 비트값으로 저장해놓는다.
words = [intToBit(a) for a in arr]
# 꼭 배워야 하는 단어 제외한 모든 단어들을 담는다. 
# 즉 앞으로 배워야 할 단어들
candidates = set().union(*arr) - s
print("arr: ", arr)
print(candidates)

answer = 0
# k가 5보다 작을 경우 단어를 배울 수 없음
if k < 5:
    print(0)
else:
    if len(candidates) <= (k-5):
        print(N)
    else:
        # 배워야 할 단어들을 조합한 것을 돌면서
        for c in combinations(candidates, k-5):
            # 이미 알고 있는 단어와 조합된 단어들을 
            # 비트로 합친다.
            temp = base
            for i in c:
                temp |= (1 << i)
            # 이건 무슨 의미인지 모르겠다.. temp 뒤집기..?
            print(1 << 26)
            temp ^= (1 << 26) - 1
            # words를 돌면서 temp를 뒤집은 상태이기 때문에 and연산 했을 때 0이 나올 경우 같은 단어이므로..?
            # 그러면 뒤집지 않고 temp & a 가 1일 때 1을 더해주면 되지 않나?
            answer = max(answer, sum(1 if (temp & a) == 0 else 0 for a in words))
        print(answer)