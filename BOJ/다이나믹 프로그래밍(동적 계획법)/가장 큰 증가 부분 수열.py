n, arr = int(input()), list(map(int, input().split()))
dp = [arr[i] for i in range(n)]
for i in range(n):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j] and dp[i] < dp[j]+arr[i]:
            dp[i] = dp[j]+arr[i]
print(max(dp))