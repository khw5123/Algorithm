import sys
input = sys.stdin.readline
INF = 9876543210

n, m = map(int, input().split())
dist = [[INF]*n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
for _ in range(m):
    i, j = map(int, input().split())
    dist[i-1][j-1] = 1
for k in range(n):
    for i in range(n):
        if dist[i][k] == INF:
            continue
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for _ in range(int(input())):
    i, j = map(int, input().split())
    if dist[i-1][j-1] == INF:
        if dist[j-1][i-1] == INF:
            print(0)
        else:
            print(1)
    else:
        print(-1)