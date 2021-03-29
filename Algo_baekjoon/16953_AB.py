A, B = map(int, input().split())

min_count = 1e9

def dfs(n, count):
    global min_count
    if n == B:
        if min_count > count:
            min_count = count
        return True
    if n > B:
        return False

    for i in range(1, 3):
        if i == 1:
            newV = n * 2
            if newV <= B:
                # print(newV, count)
                dfs(n*2, count+1)
        else:
            newV = int(str(n)+'1')
            if newV <= B:
                # print(newV, count)
                dfs(int(str(n)+'1'), count+1)
    return False

dfs(A, 0)

if min_count == 1e9:
    print("-1")
else:
    print(min_count+1)
