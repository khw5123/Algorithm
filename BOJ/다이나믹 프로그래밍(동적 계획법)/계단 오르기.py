n, arr, dp = int(input()), [0]*301, [0]*301
for i in range(1, n+1):
    arr[i] = int(input())
dp[1], dp[2] = arr[1], arr[1]+arr[2]
for i in range(3, n+1):
    dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3])
print(dp[n])