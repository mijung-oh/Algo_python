N, M = map(int, input().split())

numbers = list(map(int, input().split()))

max_sum = -1
sub_sum = 0

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            sub_sum = numbers[i] + numbers[j] + numbers[k]

            if sub_sum <= M:
                if max_sum < sub_sum:
                    max_sum = sub_sum



print(max_sum)