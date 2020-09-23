from collections import deque

def bfs(x, y):
    queue, visit = deque(), [[0]*w for _ in range(h)]
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        board[x][y] = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return answer

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    answer = 0
    board = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)