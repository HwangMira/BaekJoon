# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상방문할 수 
# 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
import sys

def dfs(idx) :
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N +1):
        # 만약 visited[next]에 간적이 없고 graph에서도 간적이 없다면 dfs(next)를 대입해라
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    # bfs는 q가 필요하고 q의 요소가 남아있지 않을때까지 계속해서 돌도록 한다.
    # q의 가장 앞의 요소를 꺼내오고 계속 이어서 붙이고
    # 남아있는 q를 비우면 끝이 난다. 
    while q:
        cur = q.pop(0)
        visited[cur] = True
        print(cur, end = ' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
    
    
input = sys.stdin.readline
N, M, V = map(int, input().split())
# 1. graph 정보 입력
# 1.1 기본적으로 graph의 배열을 초기화하기 위해 0이나 false로 초기화를한다. 
# 1.2 N+1을 사용하는 이유 : 그래프를 5 X 5로 만들어야 0~4로 만들 수 있고 이후 인덱스에 접근할 때
#                           index -1로 접근하지 않고 index로 바로 접근할 수 있어서 골치아픈 인덱스 계산을
#                           간소화할 수 있다. (약간의 센스!)
# graph는 2차원배열
# visited는 1차월 배열
graph = [[False] * (N +1) for _ in range(N +1)]

visited = [False] * (N +1)

for _ in range(M):
    a, b = map(int, input().split())
    # 입력 정보를 a,b 도 그래프에서 True, b,a에서도 그래프에서 True로 바꿔줄 수 있다.
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(V)
# 2.2 엔터를 치고 마무리.
print()
# 3. bfs
# 3.1 먼저 visited 초기화
visited = [False] * (N + 1)
q = [V]
# V라는 노드를 다시 재방문하지 않도록 막은것
visited[V] = True
bfs()


