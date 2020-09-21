from collections import deque

def bfs(x, y):
    result = {}
    queue, visit = deque(), [[0]*n for _ in range(n)]
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        result[(x, y)] = 1
        board[x][y] = '0'
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == '1' and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return len(result)

n = int(input())
board = [list(input()) for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            answer.append(bfs(i, j))
print(len(answer))
for v in sorted(answer):
    print(v)