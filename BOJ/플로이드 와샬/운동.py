import sys
input = sys.stdin.readline
INF = 9876543210

n, m = map(int, input().split())
dist = [[INF]*n for _ in range(n)]
answer = INF
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        if dist[i][k] == INF:
            continue
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(n):
    for j in range(n):
        if dist[i][j] != INF and dist[j][i] != INF:
            answer = min(answer, dist[i][j]+dist[j][i])
if answer != INF:
    print(answer)
else:
    print(-1)