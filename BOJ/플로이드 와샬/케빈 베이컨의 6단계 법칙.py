import sys
input = sys.stdin.readline
INF = 9876543210

n, m = map(int, input().split())
dist = [[INF]*n for _ in range(n)]
answer = [0, INF]
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
for _ in range(m):
    i, j = map(int, input().split())
    dist[i-1][j-1], dist[j-1][i-1] = 1, 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += dist[i][j]
    if tmp < answer[1]:
        answer = [i+1, tmp]
    elif tmp == answer[1]:
        if i+1 < answer[0]:
            answer[0] = i+1
print(answer[0])