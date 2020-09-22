import sys
from collections import deque
input = sys.stdin.readline

def bfs(queue):
    answer = -1
    while queue:
        answer += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0:
                        board[nx][ny] = board[x][y]+1
                        queue.append((nx, ny))
    for i in range(n):
        if 0 in board[i]:
            answer = -1
            break
    return answer

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))
print(bfs(queue))