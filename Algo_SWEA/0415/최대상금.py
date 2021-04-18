import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    number, count = input().split()

    lst = list(map(int, number))

    idx = 0
    change_count = 0
    while change_count < int(count):
        # idx원소가 뒤에 숫자보다 더 크면 pass
        check = 0
        for i in range(idx+1, len(lst)):
            if lst[i] > lst[idx]:
                check = 1
                break
        
        if check:
            # 한 원소씩 바꿔준다.
            max_lst = ''.join(map(str, lst))
            change_idx = 0
            for i in range(idx+1, len(lst)):
                if lst[idx] <= lst[i]:
                    lst2 = lst[::]
                    lst2[i], lst2[idx] = lst2[idx], lst[i]
                    b = ''.join(map(str, lst2))
                    print(max_lst, b)
                    if max_lst < b:
                        max_lst = b
                        change_idx = i
            
            lst[idx], lst[change_idx] = lst[change_idx], lst[idx]
            change_count += 1
        
        idx += 1

    print('#{} {}'.format(tc, ''.join(map(str, lst))))