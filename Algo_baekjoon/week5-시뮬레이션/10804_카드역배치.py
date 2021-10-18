cards = [i for i in range(21)]

for i in range(10):
    st, en = map(int, input().split())
    for j in range(st, (st+en)//2+1):
        cards[j], cards[en-j+st] = cards[en-j+st], cards[j]

print(*cards[1:])