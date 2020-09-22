import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue, visit = deque(), [[0]*m for _ in range(n)]
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        board[x][y] = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return answer

for _ in range(int(input())):
    answer = 0
    m, n, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)