N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

jjang = 0xfffffff
if len(numbers):
    print(numbers[len(numbers)//2-1])
else:
    print(numbers[len(numbers) // 2])
    