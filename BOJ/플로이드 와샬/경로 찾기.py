import sys
input = sys.stdin.readline
INF = 9876543210

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dist[i][j] == 0:
            dist[i][j] = INF
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(n):
    for j in range(n):
        if dist[i][j] != INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()