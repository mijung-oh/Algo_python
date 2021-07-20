N = int(input())

default = 666

sort_list= [default]

one = [i for i in range(0, 10)]
# two = [i for i in range(11, 100)]

pre_len = 3
for t in range(30):
    for i in sort_list:
        if len(str(i)) > pre_len:
            continue
        sub_list = []
        for j in one:
            sub_list.append(int(str(i) + str(j)))
            sub_list.append(int(str(j) + str(i)))
        # sublist 중복 제거
    sort_list += (sub_list)
    pre_len += 1
    # sort_list = list(set(sort_list))
    # print(sort_list)
    # print(len(sort_list))
    # if len(sort_list) > 1000:
    #     break

# print(sort_list)
print(sorted(sort_list))
print('길이:', len(sort_list))
# a = ['1', '01', '2', '02']
# print(sorted(a))
# print(sorted(sort_list)[N-1])

