import sys
input = sys.stdin.readline
INF = 9876543210

n, m = int(input()), int(input())
dist = [[INF]*n for _ in range(n)]
answer = 0
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
for i in range(1, n):
    if dist[0][i] != INF:
        answer += 1
print(answer)