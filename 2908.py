number_list = list(map(str,input().split()))
number1 = ''.join(reversed(number_list[0]))
number2 = ''.join(reversed(number_list[1]))

print(number1 if number1 > number2 else number2)
