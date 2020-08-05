n, dp = int(input()), [0]+list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(i//2, i+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
print(dp[n])
'''
n, arr = int(input()), [0]+list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], arr[j]+dp[i-j])
print(dp[n])
'''