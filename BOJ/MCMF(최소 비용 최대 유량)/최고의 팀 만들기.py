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
            inQueue[present] = False
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

n, m = 1000, 2 # 선수 수, 팀 수
v = n + m + 2 # 정점의 수
capacity = [[0]*v for _ in range(v)] # 용량
flow = [[0]*v for _ in range(v)] # 유량
cost = [[0]*v for _ in range(v)] # 비용
adj = [[] for _ in range(v)] # 연결된 정점 (source + 선수 + 팀 + sink)
_n = 1
while True:
    try:
        a, b = map(int, input().split()) # 흑, 백 능력치
        for _m in range(n+1, n+m+1): # 선수와 팀 매칭
            adj[_n].append(_m)
            adj[_m].append(_n)
            capacity[_n][_m] = 1
            if _m == n+1: # 흑으로 플레이할 경우
                cost[_n][_m] = -a # 순방향 간선의 비용
                cost[_m][_n] = a # 역방향 간선의 비용
            else: # 백으로 플레이할 경우
                cost[_n][_m] = -b # 순방향 간선의 비용
                cost[_m][_n] = b # 역방향 간선의 비용
        _n += 1
    except:
        break
for _n in range(1, n+1): # source와 선수 매칭
    adj[0].append(_n)
    adj[_n].append(0)
    capacity[0][_n] = 1
for _m in range(n+1, n+m+1): # 팀과 sink 매칭
    adj[_m].append(v-1)
    adj[v-1].append(_m)
    capacity[_m][v-1] = 15 # 참가 가능한 플레이어 수
min_cost, max_flow = MCMF(0, v-1)
print(abs(min_cost))