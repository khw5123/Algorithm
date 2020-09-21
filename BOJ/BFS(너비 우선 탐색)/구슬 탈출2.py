from collections import deque

def move(x, y, dx, dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visit[rx][ry][bx][by] = True
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrx, nry, rc = move(rx, ry, dx, dy)
            nbx, nby, bc = move(bx, by, dx, dy)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return depth
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth+1))
    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
rx, ry, bx, by = [-1]*4
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
print(bfs(rx, ry, bx, by))