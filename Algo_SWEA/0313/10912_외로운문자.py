T = int(input())

for tc in range(1, T+1):
    string = list(input())
    string.sort()
    new_string = ''
    idx = -1
    while idx < len(string)-1:
        idx += 1
        if idx+1 < len(string) and string[idx] == string[idx+1]:
            idx +=1 
        else:
            new_string += string[idx]
    
    result = new_string if len(new_string) else 'Good'
    print(f'#{tc} {result}')