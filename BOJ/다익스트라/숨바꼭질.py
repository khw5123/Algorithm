import sys
import heapq
input = sys.stdin.readline
INF = 9876543210

def dijkstra(start_node):
    dist, pq = [INF]*(v+1), []
    dist[start_node] = 0
    heapq.heappush(pq, [0, start_node])
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        for next_node, weight in li[current_node].items():
            next_dist = dist[current_node] + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(pq, [next_dist, next_node])
    return dist

v, e = map(int, input().split())
li = [dict() for _ in range(v+1)]
answer = [0, 0, 0]
for _ in range(e):
    a, b = map(int, input().split())
    li[a][b], li[b][a] = 1, 1
dist = dijkstra(1)
answer[1] = max(dist[1:])
answer[0] = dist.index(answer[1])
answer[2] = dist.count(answer[1])
print(answer[0], answer[1], answer[2])