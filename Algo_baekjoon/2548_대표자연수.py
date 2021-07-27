N = int(input())

numbers = list(map(int, input().split()))
max_num = max(numbers)
numbers = sorted(numbers)

min_sum = 0xffffff
jjang = 0xfffffff

for i in range(1, max_num+1):
    # 차이값들의 합 구하기
    sub_sum = 0
    for j in numbers:
        sub_sum += abs(i - j)
        if sub_sum >= min_sum:
            break

    print(i, sub_sum) 
    if sub_sum == min_sum:
        if i < jjang:
            jjang = i

    elif sub_sum < min_sum:
        min_sum = sub_sum
        jjang = i

print(jjang)
    