import sys
input = sys.stdin.readline
INF = 9876543210

n = int(input())
dist = [[INF]*n for _ in range(n)]
answer = [INF, []]
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
while True:
    i, j = map(int, input().split())
    if i == -1 and j == -1:
        break
    dist[i-1][j-1], dist[j-1][i-1] = 1, 1
for k in range(n):
    for i in range(n):
        if dist[i][k] == INF:
            continue
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(n):
    if max(dist[i]) < answer[0]:
        answer = [max(dist[i]), [i+1]]
    elif max(dist[i]) == answer[0]:
        answer[1].append(i+1)
print(answer[0], len(answer[1]))
print(' '.join(map(str, sorted(answer[1]))))