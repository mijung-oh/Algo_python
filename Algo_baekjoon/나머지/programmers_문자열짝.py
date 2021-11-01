# def solution(s):

#     stack = []
#     i = 0
#     while i < len(s):
#         if i+1 < len(s) and s[i] == s[i+1]:
#             i += 2
#             continue
#         stack.append(s[i])
#         i += 1

#     print(stack)
#     if len(stack) % 2:
#         return 0
#     else:
#         count = 0
#         for i in range(0, len(stack), 2):
#             if stack[i] == stack[i+1]:
#                 count +=2
#         if len(stack) == count:
#             return 1
#         else:
#             return 0
#     return


# print(solution('aaaaaa'))

def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) and stack[-1] == s[i]:
            stack.pop()
            continue
        stack.append(s[i])
    if stack: return 0
    else: return 1

    return answer
    