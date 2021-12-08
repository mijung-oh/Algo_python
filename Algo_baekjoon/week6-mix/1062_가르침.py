max_result = -1

def dfs(cnt, goal, get):
    global max_result

    max_cnt = 0
    if cnt == goal:
        for word in words:
            check = True
            for i in word:
                if not alphabet[ord(i) - ord('a')]:
                    check = False
            if check:
                max_cnt += 1
        if max_cnt > max_result:
            max_result = max_cnt
        return


    for i in range(26):
        if i != ord('a')-ord('a') and i != ord('n')-ord('a') and i != ord('t')-ord('a') and i != ord('c')-ord('a') and i != ord('i')-ord('a'):
            if not alphabet[i]:
                alphabet[i] = 1
                get.append(chr(ord('a') + i))
                dfs(cnt + 1, goal, get)
                alphabet[i] = 0
                get.pop()

N, K = map(int, input().split())

words = []
for n in range(N):
    input_string = list(input())
    words.append(input_string[4:len(input_string)-4])

alphabet = [0] * 26
for i in ['a', 'n', 't', 'i', 'c']:
    alphabet[ord(i)-ord('a')] = 1


if K <= 5:
    print("0")
elif K > 26:
    print("0")
else:
    get_lst = ['a', 'n', 't', 'i', 'c']
    dfs(0, K-5, get_lst)
    print(max_result)




# def combi(n, k):
#     result = []
#     for i in range(1 << n):
#         if i != ord('a')-ord('a') and i != ord('a')-ord('n') and i != ord('a')-ord('t') and i != ord('a')-ord('c') and i != ord('a')-ord('i'):
#             t = []
#             for j in range(n):
#                 if i & (1 << j):
#                     t.append(j)
#             if len(t) == k:
#                 result.append(t)
#     return result
