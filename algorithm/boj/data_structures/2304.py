n = int(input())
graph = [0] * 1001
x_arr = []
y_arr = []
for i in range(n):
    x, y = map(int, input().split())
    graph[x] = y
    x_arr.append(x)
    y_arr.append(y)
max_h = max(y_arr)
max_w = max(x_arr)
prefix = [0] * (max_w+2)
suffix = [0] * (max_w+2)
max_p = []

# prefix 계산
h = 0
for i in range(1, max_w+3):
    if graph[i] == max_h:
        max_p.append(i)
        break
    h = max(h, graph[i])
    prefix[i] = prefix[i-1] + h
h = 0
for i in range(max_w, 0, -1):
    if graph[i] == max_h:
        max_p.append(i)
        break
    h = max(h, graph[i])
    suffix[i] = suffix[i+1] + h
ans = max(prefix) + max(suffix)
ans += (max_p[1] - max_p[0] + 1) * max_h
print(ans) 