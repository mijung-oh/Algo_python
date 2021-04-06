node = int(input())
lst = list(map(int, input().split()))

tree = []
for n in range(node):
    tree.append([0])
print((len(tree)))
for i in range(0, len(lst), 2):
    # i: 0, 2, 4, 6, 8 ...
    tree[lst[i]].append(lst[i+1])

print(tree)


def search(x):
    # 루트인경우 먼저 자기자신 출력
    print(x)
    if len(tree[x])>1:
        if len(tree[x])>=2 and tree[x][1]: search(tree[x][1])
        if len(tree[x])>=3 and tree[x][2]: search(tree[x][2])


search(1)