import sys
import copy
input = sys.stdin.readline

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
path = copy.deepcopy(dist)
answer = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != k and j != k:
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    answer = -1
                if dist[i][j] == dist[i][k]+dist[k][j]:
                    path[i][j] = 0
if answer != -1:
    for i in range(n):
        for j in range(i+1, n):
            answer += path[i][j]
print(answer)