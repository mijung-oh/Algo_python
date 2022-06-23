import heapq

N = int(input())
numbers = []

for n in range(N):
    heapq.heappush(numbers, int(input()))
    print(numbers)
