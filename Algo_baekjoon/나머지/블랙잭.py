N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# numbers.sort()
max_sum = -1
sub_sum = 0

for i in range(len(numbers)-1, -1, -1):
    # i: 9 8 7 6 5
    for j in range(i-1, -1, -1):
        # j: 8 7 6 5
        for k in range(j-1, -1, -1):
            # k: 7 6 5
            sub_sum = numbers[i] + numbers[j] + numbers[k]

            if sub_sum <= M:
                if max_sum < sub_sum:
                    max_sum = sub_sum



print(max_sum)