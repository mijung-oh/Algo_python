N = int(input())
l, r = 1, 2
answer = 0
sub_sum = 1
while l<r and r<=N:
    if sub_sum < N:
        sub_sum += r
        r += 1
    elif sub_sum > N:
        sub_sum -= l
        l += 1
    else:
        answer += 1
        l += 1
        r = l + 1
        sub_sum = l
print(answer+1)
