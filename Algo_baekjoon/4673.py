def d(n):
    total = n
    while 1:
        total += n%10
        n //= 10
        if n==0:
            break

    return total

number_list = range(1,10001)
d_list = []
result = []
for i in range(1,10001):
    # d = d(i)
    d_list.append(d(i))

for i in number_list:
    if i not in d_list:
        result.append(i)

for i in result:
    print(i)