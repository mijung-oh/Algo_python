# T = int(input())
#
# for tc in range(1, T+1):
#     try:
#         words = input()
#         sentence = []
#
#         opener = '({'
#         closer = ')}'
#         check = 1
#
#         # input 값을 하나씩 추출하여 for 문을 돌린다.
#         for word in words:
#             # 여는 괄호면 빈 리스트에 넣어준다
#             if word in opener:
#                 sentence.append(word)
#
#             # 닫는 괄호면
#             elif word in closer:
#                 # 리스트가 비어있을 때 결과값을 -1
#                 # if len(sentence) == 0:
#                 #     check = 0
#                 #     break
#                 # 리스트가 비어있지 않을 때 여는괄호와 같은 종류면 리스트에서 그 값을 뺀다.
#                 if len(sentence) and sentence[-1] == '(' and word == ')':
#                     sentence.pop()
#                 elif len(sentence) and sentence[-1] == '{' and word == '}':
#                     sentence.pop()
#                 else:
#                     check = 0
#         if check and len(sentence) == 0:
#             result = 1
#         else:
#             result = 0
#     except:
#         result = 0
#
#
#     print('#{} {}'.format(tc, result))

T = int(input())

for tc in range(1, T+1):
    try:
        words = input()
        sentence = []
        opener = '({'
        closer = ')}'
        result = 1

        # input 값을 하나씩 추출하여 for 문을 돌린다.
        for word in words:
            # 여는 괄호면 빈 리스트에 넣어준다
            if word in opener:
                sentence.append(word)

            # 닫는 괄호면
            elif word in closer:
                # 빈 리스트가 비어있을 때 결과값을 -1
                if len(sentence) == 0:
                    result = 0
                    break
                # 리스트가 비어있지 않을 때 여는괄호와 같은 종류면 리스트에서 그 값을 뺀다.
                elif sentence[-1] == '(' and word == ')':
                    sentence.pop()
                elif sentence[-1] == '{' and word == '}':
                    sentence.pop()
                else:
                    result = 0

        if result and len(sentence) == 0:
            result = 1
        else:
            result = 0
    except:
        result = 0


    print('#{} {}'.format(tc, result))