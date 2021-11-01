a = input()
b = input()

roma = {
    "M": [1000, 0],
    "D": [500, 0],
    "C": [100, 0],
    "L": [50, 0],
    "X": [10, 0],
    "V": [5, 0],
    "I": [1, 0]
}

small_first = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}
roma_list = [1000, 500, 100, 50, 10, 5, 1]

# 아라비아숫자로 변경하기
def charToNumber(a):
    sub_sum = 0
    i = 0
    while i < len(a):
        # 작은 값이 먼저인 경우
        if i+1 < len(a) and a[i:i+2] in small_first.keys():
            sub_sum += small_first[a[i:i+2]]
            i += 2
        else:
            sub_sum += roma[a[i]][0]
            i += 1
    return sub_sum
    

# 로마 숫자로 변경하기
def NumberToChar(n):
    result = ""
    # 각각의 자릿수 값 빼기 2493 => 2000 400 90 3
    string_n = str(n)
    for i in range(len(string_n)):
        curV = int(string_n[i]) * (10 ** (len(string_n) - 1 - i))
        check = 1
        # 해당 숫자가 로마숫자인 경우
        for key, value in roma.items():
            if curV == value[0]:
                result += key
                check = 0
                break
        # small first가 아닌 경우 
        if check:
            for key, value in small_first.items():
                if curV == value:
                    result += key
                    check = 0
                    break
        
        # 둘 다 아닌 경우, 로마숫자 여러개로 만든다.
        if check:
            x = y = 0
            for r in roma_list:
                if curV % r == 0:
                    x = curV // r
                    y = r
                    break

            for key, value in roma.items():
                if value[0] == y:
                    result += key * x
                    break
    return result

        

a_sum = charToNumber(a)
b_sum = charToNumber(b)
print(a_sum + b_sum)
print(NumberToChar(60))
