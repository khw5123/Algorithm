import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        visit[node] = 1
        for next_ in range(1, len(adj[node])):
            if adj[node][next_] == 1 and not visit[next_]:
                visit[next_] = 1
                queue.append(next_)

n, m = map(int, input().split())
adj, visit = [[0]*(n+1) for _ in range(n+1)], [0]*(n+1)
answer = 0
for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v], adj[v][u] = 1, 1
for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        answer += 1
print(answer)