n, dp = int(input()), [0]*1001
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
print(dp[n])