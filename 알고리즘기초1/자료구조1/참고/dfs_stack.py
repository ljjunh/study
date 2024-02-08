'''
7, 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i, V): # i : 시작    V : 마지막
    visited = [0] * (V + 1)
    stack = [] 
    # visited, stack 생성 및 초기화
    visited[i] = 1 # 시작점 방문
    print(i)        #정점에서 할 일
    while True: # 탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점w가 있으면
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i) # push(i), i를 지나서 
                i = w           # w에 방문
                visited[i] = 1
                print(i)
                break
        else:   # i에 남은 인접 정점이 없으면
            if stack:   # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)  
                i = stack.pop()
            else:   # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break



V, E = map(int, input().split())
arr = list(map(int, input().split())) # 입력값
adjl = [[] for _ in range(V+1)] # 그래프 노드 정리
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우
dfs(1, V)
