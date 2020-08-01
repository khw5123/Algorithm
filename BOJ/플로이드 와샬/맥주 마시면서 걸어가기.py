import sys
input = sys.stdin.readline
INF = 9876543210

for _ in range(int(input())):
    n, coords = int(input())+2, []
    dist = [[INF]*n for _ in range(n)]
    for _ in range(n):
        coords.append(tuple(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            distance = abs(coords[i][0]-coords[j][0]) + abs(coords[i][1]-coords[j][1])
            if distance <= 1000:
                dist[i][j] = distance
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    if dist[0][n-1] == INF:
        print('sad')
    else:
        print('happy')