N = int(input())

default = 666

sort_list= [default]

one = [i for i in range(0, 10)]
# two = [i for i in range(11, 100)]

pre_len = 3
test = [default]
# for t in range(2):
while len(sort_list) < 10000:
    sub_list = []
    for i in test:
        for j in one:
            sub_list.append(int(str(i) + str(j)))
            sub_list.append(int(str(j) + str(i)))
    test = sub_list[:]
    sort_list += sub_list
    if len(sort_list) >= 10000:
        break

sort_list = list(set(sort_list))
# print(sorted(sort_list))
print(sorted(sort_list)[N-1])
# print('길이:', len(sort_list))
# a = ['1', '01', '2', '02']
# print(sorted(a))
# print(sorted(sort_list)[N-1])

