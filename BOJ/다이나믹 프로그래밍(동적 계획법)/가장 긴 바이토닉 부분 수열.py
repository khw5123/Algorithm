n, arr = int(input()), list(map(int, input().split()))
dp, dp2 = [1]*n, [0]*n
for i in range(n):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[i] > arr[j] and dp2[i] < dp2[j]+1:
            dp2[i] = dp2[j]+1
print(max([dp[i]+dp2[i] for i in range(n)]))