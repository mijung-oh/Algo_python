total_string = list(input())
pang = input()
# 문자열 앞에서부터 돌면서
# 폭발 문자열길이만큼 비교한다.
# 비교 후 같을 경우, 그 문자열을 제외한 전 문자열과 후 문자열을 합쳐준다.
# 전 문자열이 있을 경우, 전 문자열의 끝이 인덱스가 된다.
# 없을 경우, 후 문자열의 첫번째가 인덱스가 된다.

index = 0
check = True
while 1:
    # print(total_string[index:index+len(pang)])
    if ''.join(total_string[index:index+len(pang)]) == pang:
        pre = total_string[:index]
        post = total_string[index+len(pang):]

        if len(pre):
            index = len(pre)-1
            total_string = pre + post
        else:
            index = 0
            total_string = post

    else:
        index += 1
        if index == len(total_string):
            break
        elif len(total_string) == 0:
            check = False
            break

if check:
    print(''.join(total_string))
else:
    print("FRULA")