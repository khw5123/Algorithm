n, arr = int(input()), list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(1, n+1):
    if dp[i-1] + arr[i-1] > 0:
        dp[i] = dp[i-1] + arr[i-1]
    else:
        dp[i] = 0
if max(dp) == 0:
    print(max(arr))
else:
    print(max(dp))