import sys
import heapq
input = sys.stdin.readline
INF = 9876543210

def dijkstra(start_node):
    dist, pq = [INF]*(n+1), []
    dist[start_node] = 0
    heapq.heappush(pq, [0, start_node])
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        for next_node, weight in adj[current_node].items():
            next_dist = dist[current_node] + weight
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heapq.heappush(pq, [next_dist, next_node])
    return dist

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj, dst, answer = [{} for _ in range(n+1)], [], []
    for _ in range(m):
        a, b, d = map(int, input().split())
        adj[a][b], adj[b][a] = d, d
    for _ in range(t):
        dst.append(int(input()))
    s_dist, g_dist, h_dist = dijkstra(s), dijkstra(g), dijkstra(h)
    for x in dst:
        cost = min(s_dist[h] + h_dist[g] + g_dist[x], s_dist[g] + g_dist[h] + h_dist[x]) # s-h-g-x, s-g-h-x 두 경로 중 더 짧은 경로의 길이
        if cost == s_dist[x]:
            answer.append(x)
    print(' '.join(map(str, sorted(answer))))
'''
import sys
import heapq
input = sys.stdin.readline
INF = 9876543210

def dijkstra(start_node):
    dist, pq = [INF]*(n+1), []
    dist[start_node] = 0
    heapq.heappush(pq, [0, start_node])
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        for next_node, weight in adj[current_node].items():
            next_dist = dist[current_node] + weight
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heapq.heappush(pq, [next_dist, next_node])
    return dist

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj, dst, answer = [{} for _ in range(n+1)], [], []
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            adj[a][b], adj[b][a] = d*2 - 1, d*2 - 1 # g-h 도로의 길이는 홀수로 설정
        else:
            adj[a][b], adj[b][a] = d*2, d*2 # 그 외 도로의 길이는 짝수로 설정
    for _ in range(t):
        dst.append(int(input()))
    dist = dijkstra(s)
    for x in dst:
        if dist[x] != INF and dist[x] % 2: # g-h 도로를 지났을 경우 최단 거리는 홀수가 됨 (짝수들 + 홀수 = 홀수)
            answer.append(x)
    print(' '.join(map(str, sorted(answer))))
'''