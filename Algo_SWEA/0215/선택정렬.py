arr = [10, 15, 2, 19, 6, 14]

for i in range(len(arr)-1):
    min_idx = 1

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[j]