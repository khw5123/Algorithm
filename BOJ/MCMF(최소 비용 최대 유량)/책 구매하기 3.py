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

MAX_N, MAX_M = 100, 100 # 최대 사람의 수, 최대 서점의 수
n, m = map(int, input().split()) # 사람의 수, 서점의 수
v = MAX_N + MAX_M + 2 # 정점의 수 (최대 사람 수 + 최대 서점 수 + source + sink)
capacity = [[0]*v for _ in range(v)] # 용량
flow = [[0]*v for _ in range(v)] # 유량
cost = [[0]*v for _ in range(v)] # 비용
adj = [[] for _ in range(v)] # 연결된 정점 (source + 서점 + 사람 + sink)
capacity_n = list(map(int, input().split())) # 사람이 사려고 하는 책의 개수
capacity_m = list(map(int, input().split())) # 서점이 가지고 있는 책의 개수
capacity_n_m = [list(map(int, input().split())) for _ in range(m)] # 서점이 최대로 팔 수 있는 책의 개수
cost_n_m = [list(map(int, input().split())) for _ in range(m)] # 배송비
for _m in range(1, m+1): # source와 서점 매칭
    adj[0].append(_m)
    adj[_m].append(0)
    capacity[0][_m] = capacity_m[_m-1]
for _n in range(MAX_M+1, MAX_M+n+1): # 사람과 sink 매칭
    adj[_n].append(v-1)
    adj[v-1].append(_n)
    capacity[_n][v-1] = capacity_n[_n-(MAX_M+1)]
for _m in range(1, m+1): # 서점과 사람 매칭
    for _n in range(MAX_M+1, MAX_M+n+1):
        adj[_m].append(_n)
        adj[_n].append(_m)
        capacity[_m][_n] = capacity_n_m[_m-1][_n-(MAX_M+1)]
        cost[_m][_n] = cost_n_m[_m-1][_n-(MAX_M+1)] # 순방향 간선의 비용
        cost[_n][_m] = -cost_n_m[_m-1][_n-(MAX_M+1)] # 역방향 간선의 비용
min_cost, max_flow = MCMF(0, v-1)
print(max_flow)
print(min_cost)