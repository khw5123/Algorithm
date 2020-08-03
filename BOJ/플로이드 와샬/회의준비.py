import sys
input = sys.stdin.readline
INF = 9876543210

n, m = int(input()), int(input())
dist, cluster = [[INF]*n for _ in range(n)], []
answer = []
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
for _ in range(m):
    i, j = map(int, input().split())
    dist[i-1][j-1], dist[j-1][i-1] = 1, 1
for k in range(n):
    for i in range(n):
        if dist[i][k] == INF:
            continue
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(n):
    idx = -1
    for j in range(len(cluster)):
        if i in cluster[j]:
            idx = j
            break
    if idx == -1:
        cluster.append([i])
        idx = len(cluster)-1
    for j in range(n):
        if dist[i][j] != INF:
            if j not in cluster[idx]:
                cluster[idx].append(j)
print(len(cluster))
for li in cluster:
    _min, tmp = INF, -1
    for idx in li:
        _max = -1
        for v in dist[idx]:
            if v != INF:
                _max = max(_max, v)
        if _min > _max:
            _min, tmp = _max, idx+1
    answer.append(tmp)
for v in sorted(answer):
    print(v)