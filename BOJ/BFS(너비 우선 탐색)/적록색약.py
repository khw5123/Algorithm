import copy
from collections import deque

def bfs(x, y, color):
    queue, visit = deque(), [[0]*n for _ in range(n)]
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        board[x][y] = 'X'
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in color and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return answer

n, answer = int(input()), [0]*2
board = [list(input()) for _ in range(n)]
save = copy.deepcopy(board)
for i in range(n):
    for j in range(n):
        if board[i][j] != 'X':
            bfs(i, j, board[i][j])
            answer[0] += 1
board = save
for i in range(n):
    for j in range(n):
        if board[i][j] != 'X':
            if board[i][j] == 'B':
                bfs(i, j, board[i][j])
            else:
                bfs(i, j, 'RG')
            answer[1] += 1
print(answer[0], answer[1])