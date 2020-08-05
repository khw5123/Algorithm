from bisect import bisect_left

n, arr, dp = int(input()), list(map(int, input().split())), []
for i in range(n):
    idx = bisect_left(dp, arr[i])
    if len(dp) <= idx:
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]
print(len(dp))