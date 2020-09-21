import sys
from collections import deque
input = sys.stdin.readline

def dfs(node, visit):
    if visit[node]:
        return
    visit[node] = 1
    path.append(str(node))
    tmp = []
    for i in range(len(arr)):
        if arr[i][0] == node:
            tmp.append(arr[i][1])
        if arr[i][1] == node:
            tmp.append(arr[i][0])
    for v in sorted(tmp):
        dfs(v, visit)

def bfs():
    queue = deque()
    queue.append(s)
    visit, path = [0]*(n+1), []
    while queue:
        node = queue.popleft()
        if not visit[node]:
            visit[node] = 1
            path.append(str(node))
            tmp = []
            for i in range(len(arr)):
                if arr[i][0] == node:
                    tmp.append(arr[i][1])
                if arr[i][1] == node:
                    tmp.append(arr[i][0])
            for v in sorted(tmp):
                queue.append(v)
    return path

n, m, s = map(int, input().split())
arr, path = [], []
for i in range(m):
    num = input()
    arr.append([int(num.split(' ')[0]), int(num.split(' ')[1])])
dfs(s, [0]*(n+1))
print(' '.join(path))
print(' '.join(bfs()))