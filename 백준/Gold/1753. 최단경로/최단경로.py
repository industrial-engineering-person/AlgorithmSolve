## 다익스트라 / 최단경로.1753 / 2022-09-04
import heapq,sys
input = sys.stdin.readline

V, E = map(int, input().split()) # V는 정점 수, E는 간선의 수
start_K = int(input()) # 시작 정점 번호

graph = [[] for _ in range(V+1)]
distances = [float('inf')] * (V+1) # 1번 노드부터 V번 노드까지 최단 거리를 기록
distances[start_K] = 0

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 로가는 w 가중치
    graph[u].append([w, v]) # 각 키마다  [가중치, 인접노드] 로 들어있음

def dijkstra():
    q = []
    heapq.heappush(q, [0, start_K])

    while q:
        current_distance, current_node = heapq.heappop(q)

        if distances[current_node] < current_distance:
            continue

        for weight, adjacent_node in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                heapq.heappush(q, [distance, adjacent_node])

dijkstra()
for i in range(1, V+1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])


