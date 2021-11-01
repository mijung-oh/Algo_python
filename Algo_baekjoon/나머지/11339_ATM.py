N = int(input())

costs = list(map(int, input().split()))
costs = sorted(costs)

sum_cost = [costs[0]]
for cost in range(1, len(costs)):
    sum_cost.append(sum_cost[cost-1] + costs[cost])

print(sum(sum_cost))    