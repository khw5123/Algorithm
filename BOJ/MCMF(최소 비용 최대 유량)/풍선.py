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
        present = sink
        while present != source:
            previous = path[present]
            answer[0] += flowRate*cost[previous][present] # 총 비용이 각 간선 비용만큼 증가
            flow[previous][present] += flowRate
            flow[present][previous] -= flowRate # 음의 유량
            present = path[present]
        answer[1] += flowRate
    return answer

while True:
    n, a, b = map(int, input().split())
    if n + a + b == 0:
        break
    m = 2
    v = n + m + 2 # 정점의 수
    capacity = [[0]*v for _ in range(v)] # 용량
    flow = [[0]*v for _ in range(v)] # 유량
    cost = [[0]*v for _ in range(v)] # 비용
    adj = [[] for _ in range(v)] # 연결된 정점 (source + 팀 자리 + 풍선 방 + sink)
    _n = 1
    for _ in range(n):
        k, a_cost, b_cost = map(int, input().split())
        # source와 팀 자리 매칭
        adj[0].append(_n)
        adj[_n].append(0)
        capacity[0][_n] = k
        # 팀 자리와 풍선 방(A) 매칭
        adj[_n].append(n+1)
        adj[n+1].append(_n)
        capacity[_n][n+1] = INF
        cost[_n][n+1] = a_cost
        cost[n+1][_n] = -a_cost
        # 팀 자리와 풍선 방(B) 매칭
        adj[_n].append(n+2)
        adj[n+2].append(_n)
        capacity[_n][n+2] = INF
        cost[_n][n+2] = b_cost
        cost[n+2][_n] = -b_cost
        _n += 1
        # 풍선 방(A)과 sink 매칭
        adj[n+1].append(v-1)
        adj[v-1].append(n+1)
        capacity[n+1][v-1] = a
        # 풍선 방(B)과 sink 매칭
        adj[n+2].append(v-1)
        adj[v-1].append(n+2)
        capacity[n+2][v-1] = b
    min_cost, max_flow = MCMF(0, v-1)
    print(min_cost)