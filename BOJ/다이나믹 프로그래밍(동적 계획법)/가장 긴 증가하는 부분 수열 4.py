n, arr = int(input()), list(map(int, input().split()))
dp, answer = [1]*n, {}
for i in range(n):
    answer[i] = [arr[i]]
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i], answer[i] = dp[j]+1, [arr[i]]+answer[j]
print(max(dp))
print(' '.join(map(str, answer[dp.index(max(dp))][::-1])))