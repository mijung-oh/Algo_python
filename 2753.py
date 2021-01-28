T = int(input())
def is_leap_year(T):
    if T%4 == 0:
        if T%100 or T%400 == 0:
            return 1   
    return 0
print(is_leap_year(T))

