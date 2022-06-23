N, K = map(int, input().split())

def transfer(n, k):
    if n == k or k == 0:
        return 1
    
    return transfer(n-1, k) + transfer(n-1, k-1)

print(transfer(N, K) % 1000000007)