T = input()
T_zero_cnt = T.count("0")
T_one_cnt = T.count("1")

# 100a1a로 만들 수 있는 문자열 구하기

def plusString(a, b, visited):
    global T, T_zero_cnt, T_one_cnt, resource

    if len(a+b) > len(T):
        return False
        

    if a + b == T or a + b + "01" == T or "01" + a + b == T:
        return True

    if len(T) % len(a + b) == 0 and (a + b) * (len(T) // len(a + b)) == T:
        return True
    if len(T) % len(a + b + "01") == 0 and (a + b + "01") * (len(T) // len(a + b + "01")) == T:
        return True
    if len(T) % len("01" + a + b) == 0 and ("01" + a + b) * (len(T) // len("01" + a + b)) == T:
        return True

    100 a 1 b
    for d in [("0", ""), ("0", "1"), ("", "1")]:
        result = a + d[0] + b + d[1]
            
        # 정답보다 길면 패스
        if len(result) > len(T):
            continue

        if result in visited:
            continue
        visited.add(result)

        # 정답과 같으면 바로 리턴
        i = 0
        while 1:
            sub = result + "01" * i
            if len(sub) > len(T):
                break

            if sub == T:
                return True
            else: i += 1
        
        i = 0
        while 1:
            sub = "01" * i + result
            if len(sub) > len(T):
                break

            if sub == T:
                return True
            else: i += 1


        if result == T or result + "01" == T or "01" + result == T:
            return True

        

        if result.count("1") > T_one_cnt or result.count("1") > T_zero_cnt:
            continue


        if plusString(a + d[0], b + d[1], visited):
            return True

        
    return False

a = "100"
b = "1"
visited = set()
visited.add(a + b)

if T[:3] == "101":
    print("NOISE")
elif len(T) % len("01") == 0 and "01" * (len(T) // len("01")) == T:
    print("SUBMARINE")
elif plusString(a,b, visited):
    print("SUBMARINE")
else:
    print("NOISE")
    
