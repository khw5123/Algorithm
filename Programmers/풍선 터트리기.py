def solution(a):
    answer, INF = 0, 1000000001
    left, right = INF, INF
    dp = [[0]*2 for _ in range(len(a))]
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        dp[i][0] = left
    for i in range(len(a)-1, -1, -1):
        if right > a[i]:
            right = a[i]
        dp[i][1] = right
    for i in range(len(a)):
        if not (a[i] > dp[i][0] and a[i] > dp[i][1]):
            answer += 1
    return answer