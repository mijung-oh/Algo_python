def solution(new_id):
    answer = ''
    answer = upperToLower(new_id)
    print("level1 ==> ", answer)
    answer = deleteSpecial(answer)
    print("level2 ==> ", answer)
    answer = replaceTwoToOne(answer)
    print("level3 ==> ", answer)
    answer = deleteStartAndEnd(answer)
    print("level4 ==> ", answer)
    if answer == "":
        answer = "a"
    print("level5 ==> ", answer)
    answer = stage6(answer)
    print("level6 ==> ", answer)
    answer = stage7(answer)
    print("level7 ==> ", answer)
    return answer

def upperToLower(id):
    return id.lower()

def deleteSpecial(id):
    replace = ""
    for word in id:
        print(word, ord(word))
        if "a" <= word <= "z":
            replace += word
            continue
        if word.isdigit() and 0 <= int(word) <= 9:
            print(word)
            replace += word
            continue
        if word == "-" or word == "." or word == "_":
            replace += word
            continue
    return replace

def replaceTwoToOne(id):
    stack = []
    for w in id:
        if stack and stack[-1] == w == ".":
            continue
        stack.append(w)
    return "".join(stack)

def deleteStartAndEnd(id):
    stack = []
    ## 처음이 마침표인 경우
    for w in id:
        if not stack and w == ".":
            continue
        stack.append(w)
    ## 마지막이 마침표인 경우
    while stack and stack[-1] == ".":
        stack.pop()
    return "".join(stack)

def stage6(id):
    stack = list(id)
    if len(stack) >= 16:
        stack = stack[:15]
    ## 마지막이 마침표인 경우
    while stack and stack[-1] == ".":
        stack.pop()
    return "".join(stack)

def stage7(id):
    stack = list(id)
    if len(stack) <= 2:
        while len(stack) <=2:
            stack.append(stack[-1])
    return "".join(stack)


print(solution("abcdefghijklmn.p"))