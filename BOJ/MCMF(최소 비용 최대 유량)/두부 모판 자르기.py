import sys
input = sys.stdin.readline
INF = 9876543210

def MCMF(source, sink):
    answer = [0, 0] # 최소 비용, 최대 유량
    while True:
        path, dist = [-1]*v, [INF]*v
        inQueue, queue = [0]*v, [source] # 다음에 방문할 정점들
        dist[source], inQueue[source] = 0, 1
        while queue:
            present = queue[0] # 현재 정점
            del queue[0]
            inQueue[present] = 0
            for _next in adj[present]:
                # 최소 비용이고, 최대 유량일 경우
                if dist[_next] > dist[present] + cost[present][_next] and capacity[present][_next] - flow[present][_next] > 0:
                    dist[_next], path[_next] = dist[present] + cost[present][_next], present
                    if not inQueue[_next]:
                        queue.append(_next)
                        inQueue[_next] = 1
        if path[sink] == -1: # 가능한 모든 경로를 찾았을 경우
            break
        # 현재 경로에서의 최소 유량 찾음
        flowRate = INF
        present = sink
        while present != source:
            previous = path[present]
            flowRate = min(flowRate, capacity[previous][present] - flow[previous][present])
            present = path[present]
        # 유량 흘림
        save = answer[0]
        present = sink
        while present != source:
            previous = path[present]
            answer[0] += flowRate*cost[previous][present] # 총 비용이 각 간선 비용만큼 증가
            flow[previous][present] += flowRate
            flow[present][previous] -= flowRate # 음의 유량
            present = path[present]
        answer[1] += flowRate
        # 비용이 전보다 작아졌을 경우
        if abs(answer[0]) < abs(save):
            answer[0] = save
            break
    return answer

size = int(input())
li = [list(map(str, input())) for _ in range(size)]
name, price = {}, {('A','A'):100, ('A','B'):70, ('A','C'):40, ('A','F'):0, ('B','A'):70, ('B','B'):50, ('B','C'):30, ('B','F'):0, ('C','A'):40, ('C','B'):30, ('C','C'):20, ('C','F'):0, ('F','A'):0, ('F','B'):0, ('F','C'):0, ('F','F'):0}
n, m, n_idx, m_idx = 0, 0, 1, 1
for i in range(size):
    for j in range(size):
        if (i+j) % 2 == 0:
            n += 1
            name[(i, j)] = n_idx
            n_idx += 1
        else:
            m += 1
            name[(i, j)] = m_idx
            m_idx += 1
for i in range(size):
    for j in range(size):
        if (i+j) % 2 == 1:
            name[(i, j)] += n
v = n + m + 2 # 정점의 수
capacity = [[0]*v for _ in range(v)] # 용량
flow = [[0]*v for _ in range(v)] # 유량
cost = [[0]*v for _ in range(v)] # 비용
adj = [[] for _ in range(v)] # 연결된 정점 (source + 체스판 흑 위치 + 체스판 백 위치 + sink)
for i in range(size):
    for j in range(size):
        if (i+j) % 2 == 0:
            # source와 체스판 흑 위치 매칭
            adj[0].append(name[(i, j)])
            adj[name[(i, j)]].append(0)
            capacity[0][name[(i, j)]] = 1
            # 체스판 흑 위치와 체스판 백 위치 매칭
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i+dx, j+dy
                if 0 <= nx < size and 0 <= ny < size:
                    adj[name[(i, j)]].append(name[(nx, ny)])
                    adj[name[(nx, ny)]].append(name[(i, j)])
                    capacity[name[(i, j)]][name[(nx, ny)]] = 1
                    cost[name[(i, j)]][name[(nx, ny)]] = -price[(li[i][j], li[nx][ny])]
                    cost[name[(nx, ny)]][name[(i, j)]] = price[(li[i][j], li[nx][ny])]
        else:
            # 체스판 백 위치와 sink 매칭
            adj[name[(i, j)]].append(v-1)
            adj[v-1].append(name[(i, j)])
            capacity[name[(i, j)]][v-1] = 1
min_cost, max_flow = MCMF(0, v-1)
print(abs(min_cost))