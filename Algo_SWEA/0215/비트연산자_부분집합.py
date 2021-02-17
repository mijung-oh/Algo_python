arr = [5, 5, 5, 5, 5]

n = len(arr)

def isTrue(arr):
    for i in range(1<<n):
        sub_sum = 0
        for j in range(n+1):
            if i & (1 << j):
                print(i, j)
                # sub_sum += arr[j]
    #     if sub_sum == 0:
    #         return True 
    # return False

print(isTrue(arr))
