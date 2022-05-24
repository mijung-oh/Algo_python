# def solution(info, query):
#     answer = []
#     # information[a] = [언어, 직군, 경력, 소울푸드, 점수]

#     information = []
#     for i in info:
#         information.append(i.split(" "))

#     def find(l, w, c, f, score):
#         cnt = 0
#         for i in information:
#             if (l == "-" or l == i[0]) \
#                 and (w == "-" or w == i[1])\
#                     and (c == "-" or c == i[2])\
#                         and (f == "-" or f == i[3])\
#                             and int(i[4]) >= score:
#                             cnt += 1
#                             print(l, w, c, f, score, i)
#         return cnt
                
#     for q in query:
#         q = q.split(" ")
#         answer.append(find(q[0], q[2], q[4], q[6], int(q[7])))
#     print(answer)
#     return answer

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	)