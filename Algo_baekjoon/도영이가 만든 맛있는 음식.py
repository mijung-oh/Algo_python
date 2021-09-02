N = int(input())

ingredients = []
for n in range(N):
    ingredients.append(tuple(map(int, input().split())))

min_gap = 0xffffffff


def combi(n):
    combis = []
    for i in range(1<<n):
        t = []
        for j in range(n):
            if i & (1 << j):
                t.append(j)
        combis.append(t)
    return combis


# 조합 리스트를 돌면서
# 각각 신맛과 쓴맛의 차이를 구해준다.
combi_list = combi(N)
for combis in combi_list:
    s = 1
    b = 0
    # 공집합이 아닌 경우에만
    if combis:
        for c in combis:
            s *= ingredients[c][0]
            b += ingredients[c][1]
        gap = abs(s-b)
        if min_gap > gap:
            min_gap = gap

print(min_gap)
        