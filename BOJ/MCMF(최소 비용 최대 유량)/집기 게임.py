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

for _ in range(int(input())):
    n, m = map(int, input().split())
    v = n + m + 2 # 정점의 수
    capacity = [[0]*v for _ in range(v)] # 용량
    flow = [[0]*v for _ in range(v)] # 유량
    cost = [[0]*v for _ in range(v)] # 비용
    adj = [[] for _ in range(v)] # 연결된 정점 (source + 가로 선 + 세로 선 + sink)
    n_info, m_info = {}, {}
    for _n in range(1, n+1):
        n_info[_n] = list(map(int, input().split()))
        # source와 가로 선 매칭
        adj[0].append(_n)
        adj[_n].append(0)
        capacity[0][_n] = 1
    for _m in range(n+1, n+m+1):
        m_info[_m] = list(map(int, input().split()))
        # 세로 선과 sink 매칭
        adj[_m].append(v-1)
        adj[v-1].append(_m)
        capacity[_m][v-1] = 1
    for _n in range(1, n+1):
        for _m in range(n+1, n+m+1):
            # 교점이 있을 경우
            if (n_info[_n][0] < m_info[_m][0] < n_info[_n][2] or n_info[_n][2] < m_info[_m][0] < n_info[_n][0]) and (m_info[_m][1] < n_info[_n][1] < m_info[_m][3] or m_info[_m][3] < n_info[_n][1] < m_info[_m][1]):
                # 가로 선과 세로 선 매칭
                adj[_n].append(_m)
                adj[_m].append(_n)
                capacity[_n][_m] = 1
                cost[_n][_m] = -n_info[_n][4]*m_info[_m][4] # 순방향 간선의 비용
                cost[_m][_n] = n_info[_n][4]*m_info[_m][4] # 역방향 간선의 비용
    min_cost, max_flow = MCMF(0, v-1)
    print(max_flow, abs(min_cost))