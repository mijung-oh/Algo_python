def solution(numbers, hand):
    answer = ''
    phone = {
        "1": (0,0),
        "2": (0,1),
        "3": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "7": (2,0),
        "8": (2,1),
        "9": (2,2),
        "*": (3,0),
        "0": (3,1),
        "#": (3,2),
    }

    left_loc = phone['*']
    right_loc = phone['#']

    for number in numbers:
        cur = ""
        if number in [1,4,7]:
            cur = "L"
            left_loc = phone[str(number)]
        elif number in [3,6,9]:
            cur = "R"
            right_loc = phone[str(number)]
        else:
            left_d = (phone[str(number)][0] - left_loc[0])**2  + (phone[str(number)][1] - left_loc[1])**2
            right_d = (phone[str(number)][0] - right_loc[0])**2  + (phone[str(number)][1] - right_loc[1])**2
            print(number, left_d, right_d)
            if left_d > right_d:
                cur = "R"
                right_loc = phone[str(number)]
            elif left_d < right_d:
                cur = "L"
                left_loc = phone[str(number)]
            elif left_d == right_d:
                if hand == "left":
                    cur = "L"
                    left_loc = phone[str(number)]
                else:
                    cur = "R"
                    right_loc = phone[str(number)]
        answer += cur
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))