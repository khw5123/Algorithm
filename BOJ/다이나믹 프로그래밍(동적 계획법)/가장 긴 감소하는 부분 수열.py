n, arr = int(input()), list(map(int, input().split()))
dp = [1]*n
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))