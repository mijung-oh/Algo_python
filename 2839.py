N = int(input())


five_max = 5000//5
three_max = 5000//3
min_count = three_max
for i in range(three_max,-1,-1):
    total = 3*i
    if total == N and i < min_count:
        min_count = i
    else:
        for j in range(0,five_max+1):
            total = 5*j + 3*i
            if total == N and i + j < min_count:
                min_count = i+j
            elif total > N:
                break

    
print(min_count if min_count != three_max else -1)


# five_max = 5000//5
# three_max = 5000//3
# min_count = three_max
# for i in range(0,five_max+1):
#     for j in range(0,three_max+1):
#         total = 5*i + 3*j
#         if total > N:
#             continue
#         if total == N and min_count > (i+j):
#             min_count = i + j

# print(min_count if min_count != three_max else -1)