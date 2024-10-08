from collections import deque

#학생 수, 비교 조건 수
n, m = map(int, input().split())

#진입 차수 기록용 ingraph, 인접 리스트 기록용 graph
ingraph = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

#입력 받아서 graph에 인접 리스트 기록하고, ingraph 카운트 늘려서 진입차수 증가
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ingraph[b] += 1

# 진입 차수가 0인 노드가 있으면 큐에 삽입(초기)
q = deque()
for i in range(1, n+1):
    if ingraph[i] == 0:
        q.append(i)

res = []
while q: #큐에 노드가 없어질 때 까지
    k = q.popleft() # 큐에 먼저 들어온것부터 내보내기
    res.append(k)

    for next in graph[k]: # 방금 내보낸 노드랑 연결된 모든 노드에 대해
        ingraph[next] -= 1 # 하나가 나갔으니 진입차수 1씩 감소
        if ingraph[next] == 0: # 만약 진입차수가 감소해서 0이 된 노드가 있으면
            q.append(next) # 큐에 삽입

print(*res)