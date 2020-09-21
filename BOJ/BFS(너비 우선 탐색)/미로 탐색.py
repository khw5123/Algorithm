from collections import deque

def bfs():
    answer = -1
    queue, visit = deque(), [[0]*m for _ in range(n)]
    queue.append((0, 0, 1))
    while queue:
        x, y, depth = queue.popleft()
        if x+1 == n and y+1 == m:
            answer = depth
            break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '1' and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx, ny, depth+1))
    return answer

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
print(bfs())