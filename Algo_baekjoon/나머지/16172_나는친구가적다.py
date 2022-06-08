origin = list(input())
keyword = input()

# origin에서 숫자를 뺀 것으로 업데이트한다.
new_origin = []
for o in origin:
    if o.isalpha():
        new_origin.append(o)
print(new_origin)

# 문자열찾기
l = 0
l_cnt = 0
r = len(new_origin)-1
r_cnt = len(keyword)-1

answer = 0
while l < r:
    if r-l == 1 and l_cnt + r_cnt == len(keyword)-1:
        answer = 1
        break

    if new_origin[l] == keyword[l_cnt]:
        l_cnt += 1
    else:
        l_cnt = 0

    if new_origin[r] == keyword[r_cnt]:
        r_cnt -= 1
    else:
        r_cnt = len(keyword)-1
    l += 1
    r -= 1


print(answer)