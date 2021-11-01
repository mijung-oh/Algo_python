A, B = input().split()
print(A, B)

def dfs(a):
    global B, min_gap
    gap = 0

    if len(a) > len(B):
        return

    if len(a) == len(B):
        for i in range(len(a)):
            if a[i] != B[i]:
                gap += 1
        if min_gap > gap:
            min_gap = gap
        return
        
    alphabet = [chr(i) for i in range(97,123)] ## a ~ z

    # A 앞에 알파벳 추가
    for i in alphabet:
        dfs(a+i)
        dfs(i+a)

min_gap = 9999
dfs(A)
for i in range(len(B) - len(A) + 1):
    gap = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            gap += 1

    if min_gap > gap:
        min_gap = gap


    
print(min_gap)