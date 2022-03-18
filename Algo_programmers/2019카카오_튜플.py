def solution(s):
    answer = []
    tuples = []
    subTuple = []
    subString = ""

    for i in range(1, len(s)-1):
        if s[i] != '{' and s[i] != '}' and s[i] != ',':
            subString += s[i]
        elif s[i] == ',' and s[i+1] != '{':
            subTuple.append(subString)
            subString = ""
        elif s[i] == '}' and i != len(s)-1:
            subTuple.append(subString)
            subString = ""
            tuples.append(subTuple)
            subTuple = []

    tuples = sorted(tuples, key=len)
    for t in tuples:
        for k in t:
            if int(k) in answer:
                continue
            answer.append(int(k))
    return answer

solution("{{20,111},{111}}")